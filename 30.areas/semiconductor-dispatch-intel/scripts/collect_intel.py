from __future__ import annotations

import hashlib
import json
import os
import sys
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import feedparser
import requests
import yaml
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config" / "sources.yml"
ENV_PATH = ROOT / ".env"

load_dotenv(ENV_PATH)

UA = os.getenv("REDDIT_USER_AGENT") or "obsidian-semiconductor-dispatch-intel/0.1"
SESSION = requests.Session()
SESSION.headers.update({"User-Agent": UA})

@dataclass
class Item:
    source: str
    platform: str
    title: str
    url: str
    published: str = ""
    summary: str = ""
    tags: list[str] | None = None
    category: str = "未分类"
    score: int = 0

    @property
    def id(self) -> str:
        return hashlib.sha256(self.url.encode("utf-8")).hexdigest()[:16]


def load_config() -> dict[str, Any]:
    with CONFIG_PATH.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def norm_text(s: Any) -> str:
    if s is None:
        return ""
    return str(s).replace("\n", " ").strip()


def score_item(item: Item, keywords: Iterable[str]) -> int:
    hay = f"{item.title} {item.summary}".lower()
    score = 0
    for kw in keywords:
        parts = [p for p in kw.lower().replace('"', '').split() if p]
        if not parts:
            continue
        if all(p in hay for p in parts):
            score += max(1, len(parts))
    return score


def collect_rss(cfg: dict[str, Any]) -> list[Item]:
    out: list[Item] = []
    if not cfg.get("rss", {}).get("enabled", False):
        return out
    for feed in cfg["rss"].get("feeds", []):
        parsed = feedparser.parse(feed["url"], agent=UA)
        for e in parsed.entries[:30]:
            url = norm_text(getattr(e, "link", ""))
            if not url:
                continue
            out.append(Item(
                source=feed.get("name", feed["url"]),
                platform="RSS",
                title=norm_text(getattr(e, "title", "(no title)")),
                url=url,
                published=norm_text(getattr(e, "published", getattr(e, "updated", ""))),
                summary=norm_text(getattr(e, "summary", ""))[:800],
                tags=feed.get("tags", []),
            ))
    return out


def github_headers() -> dict[str, str]:
    h = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
    token = os.getenv("GITHUB_TOKEN", "").strip()
    if token:
        h["Authorization"] = f"Bearer {token}"
    return h


def collect_github(cfg: dict[str, Any]) -> list[Item]:
    out: list[Item] = []
    gh = cfg.get("github", {})
    if not gh.get("enabled", False):
        return out
    for s in gh.get("searches", []):
        stype = s.get("type", "repositories")
        endpoint = "repositories" if stype == "repositories" else "issues"
        url = f"https://api.github.com/search/{endpoint}"
        params = {"q": s["query"], "sort": s.get("sort", "updated"), "order": s.get("order", "desc"), "per_page": 20}
        try:
            r = SESSION.get(url, headers=github_headers(), params=params, timeout=25)
            r.raise_for_status()
        except Exception as ex:
            print(f"[WARN] GitHub search failed: {s.get('name')}: {ex}")
            continue
        for it in r.json().get("items", []):
            if endpoint == "repositories":
                out.append(Item(
                    source=s.get("name", "GitHub"), platform="GitHub",
                    title=it.get("full_name") or it.get("name") or "GitHub repository",
                    url=it.get("html_url", ""), published=it.get("updated_at", ""),
                    summary=it.get("description") or "", tags=["github", "repo"],
                ))
            else:
                out.append(Item(
                    source=s.get("name", "GitHub"), platform="GitHub",
                    title=it.get("title") or "GitHub issue/PR",
                    url=it.get("html_url", ""), published=it.get("updated_at", ""),
                    summary=(it.get("body") or "")[:800], tags=["github", "issue"],
                ))
    return [x for x in out if x.url]


def collect_reddit(cfg: dict[str, Any]) -> list[Item]:
    out: list[Item] = []
    rd = cfg.get("reddit", {})
    if not rd.get("enabled", False):
        return out
    for s in rd.get("searches", []):
        parsed = feedparser.parse(s["url"], agent=UA)
        for e in parsed.entries[:25]:
            url = norm_text(getattr(e, "link", ""))
            if not url:
                continue
            out.append(Item(
                source=s.get("name", "Reddit"), platform="Reddit",
                title=norm_text(getattr(e, "title", "Reddit post")), url=url,
                published=norm_text(getattr(e, "published", getattr(e, "updated", ""))),
                summary=norm_text(getattr(e, "summary", ""))[:800], tags=s.get("tags", ["reddit"]),
            ))
    return out


def collect_x(cfg: dict[str, Any]) -> list[Item]:
    out: list[Item] = []
    xc = cfg.get("x", {})
    token = os.getenv("X_BEARER_TOKEN", "").strip()
    if not xc.get("enabled", False) or not token:
        return out
    headers = {"Authorization": f"Bearer {token}", "User-Agent": UA}
    for s in xc.get("searches", []):
        params = {
            "query": s["query"], "max_results": int(s.get("max_results", 10)),
            "tweet.fields": "created_at,author_id,public_metrics,lang",
        }
        try:
            r = SESSION.get("https://api.x.com/2/tweets/search/recent", headers=headers, params=params, timeout=25)
            r.raise_for_status()
        except Exception as ex:
            print(f"[WARN] X search failed: {s.get('name')}: {ex}")
            continue
        for tw in r.json().get("data", []):
            tid = tw.get("id")
            out.append(Item(
                source=s.get("name", "X"), platform="X",
                title=(tw.get("text") or "X post")[:120],
                url=f"https://x.com/i/web/status/{tid}",
                published=tw.get("created_at", ""), summary=tw.get("text", ""), tags=["x"],
            ))
    return out


CATEGORY_RULES: dict[str, list[str]] = {
    "派工规则": ["dispatch", "dispatching", "dispatch rule", "lot dispatch", "real-time dispatch", "priority rule", "scheduling rule", "派工", "派工规则"],
    "WIP": ["wip", "work in process", "work-in-process", "queue", "queue time", "cycle time", "throughput", "bottleneck", "在制品", "瓶颈", "周期"],
    "AMHS": ["amhs", "automated material handling", "material handling", "oht", "stocker", "transport", "搬送", "物料搬运"],
    "MES": ["mes", "manufacturing execution", "camstar", "opcenter", "critical manufacturing", "eyelit", "recipe", "lot tracking"],
    "AI 调度": ["ai", "machine learning", "deep learning", "reinforcement learning", "rl", "optimization", "genetic algorithm", "digital twin", "neural", "强化学习", "机器学习", "数字孪生"],
    "论文": ["arxiv", "paper", "journal", "conference", "doi", "abstract"],
    "专利": ["patent", "patentsview", "uspto", "invention", "claim"],
    "厂商动态": ["applied materials", "siemens", "pdf solutions", "onto innovation", "synopsys", "kla", "asml", "vendor"],
}


def classify_item(item: Item) -> str:
    hay = f"{item.platform} {item.source} {item.title} {item.summary} {' '.join(item.tags or [])}".lower()
    best_cat = "未分类"
    best_score = 0
    for cat, terms in CATEGORY_RULES.items():
        sc = sum(1 for t in terms if t.lower() in hay)
        if sc > best_score:
            best_score = sc
            best_cat = cat
    return best_cat


PLATFORM_CN = {
    "GitHub": "GitHub 开源动态",
    "RSS": "RSS 行业/论文资讯",
    "Reddit": "Reddit 社区讨论",
    "X": "X / Twitter 实时动态",
    "Paper": "论文与学术资料",
    "Patent": "专利监控",
}


def chinese_digest(item: Item) -> str:
    """Generate a short Chinese reading guide without changing original title/summary.

    This is rule-based so it can run locally without sending internal data to an LLM.
    """
    text = f"{item.title} {item.summary} {' '.join(item.tags or [])}".lower()
    parts: list[str] = []

    category_hint = {
        "派工规则": "与 Dispatch Rule、Lot 排序或机台选择有关，建议关注其可派工性过滤、优先级计算和异常原因回溯。",
        "WIP": "与 WIP、Queue Time、Cycle Time 或瓶颈控制有关，建议关注其对产线节拍和在制品水位的影响。",
        "AMHS": "与 AMHS、搬送、Stocker、OHT 或 FOUP 流转有关，建议关注其是否会影响机台空等和派工结果落地。",
        "MES": "与 MES、生产执行、Lot Tracking 或工厂系统集成有关，建议关注数据接口、状态同步和派工结果回写。",
        "AI 调度": "与 AI Scheduling、优化算法、仿真或 Digital Twin 有关，建议关注其是否可用于派工策略评估或规则优化。",
        "论文": "属于论文或学术资料，建议重点提取模型假设、优化目标、约束条件和实验指标。",
        "专利": "属于专利监控入口，建议关注其权利要求、适用场景和与现有派工逻辑的差异。",
        "厂商动态": "属于厂商或行业动态，建议关注产品能力、系统架构和可借鉴的功能模块。",
    }
    parts.append(category_hint.get(item.category, "建议先判断该条目是否与自动派工、产线控制或工厂系统集成相关。"))

    signals = []
    if any(k in text for k in ["wafer fab", "fab", "semiconductor"]):
        signals.append("晶圆厂 / 半导体制造")
    if any(k in text for k in ["dispatch", "dispatching", "scheduling", "schedule"]):
        signals.append("派工 / 调度")
    if any(k in text for k in ["digital twin", "simulation", "simpy"]):
        signals.append("Digital Twin / Simulation")
    if any(k in text for k in ["reinforcement learning", "machine learning", " ai ", "optimization"]):
        signals.append("AI / Optimization")
    if any(k in text for k in ["mes", "manufacturing execution"]):
        signals.append("MES")
    if any(k in text for k in ["amhs", "oht", "stocker", "foup", "transport"]):
        signals.append("AMHS / FOUP 搬送")
    if any(k in text for k in ["cycle time", "throughput", "bottleneck", "wip"]):
        signals.append("Cycle Time / WIP / Bottleneck")

    if signals:
        parts.append("关键词信号：" + "、".join(dict.fromkeys(signals)) + "。")
    else:
        parts.append("关键词信号不明显，建议只做低优先级浏览。")

    if item.score >= 6:
        parts.append("相关度较高，建议优先阅读并判断是否可沉淀为专题笔记。")
    elif item.score >= 3:
        parts.append("相关度中等，可快速浏览摘要后决定是否保留。")
    else:
        parts.append("相关度较低，可作为背景信息或后续关键词调优参考。")
    return "".join(parts)


def collect_semantic_scholar(cfg: dict[str, Any]) -> list[Item]:
    out: list[Item] = []
    pc = cfg.get("papers", {})
    if not pc.get("enabled", False):
        return out
    headers = {"User-Agent": UA}
    api_key = os.getenv("SEMANTIC_SCHOLAR_API_KEY", "").strip()
    if api_key:
        headers["x-api-key"] = api_key
    for s in pc.get("semantic_scholar", []):
        params = {
            "query": s["query"],
            "limit": int(s.get("limit", 10)),
            "fields": "title,url,abstract,year,publicationDate,authors,venue,citationCount",
        }
        try:
            r = SESSION.get("https://api.semanticscholar.org/graph/v1/paper/search", headers=headers, params=params, timeout=25)
            r.raise_for_status()
        except Exception as ex:
            print(f"[WARN] Semantic Scholar search failed: {s.get('name')}: {ex}")
            continue
        for paper in r.json().get("data", []):
            authors = ", ".join(a.get("name", "") for a in paper.get("authors", [])[:3])
            summary = (paper.get("abstract") or "")[:900]
            if authors:
                summary = f"Authors: {authors}. " + summary
            out.append(Item(
                source=s.get("name", "Semantic Scholar"), platform="Paper",
                title=paper.get("title") or "Paper", url=paper.get("url") or "",
                published=paper.get("publicationDate") or str(paper.get("year") or ""),
                summary=summary, tags=["paper", "semantic-scholar"],
            ))
    return [x for x in out if x.url]


def collect_europe_pmc(cfg: dict[str, Any]) -> list[Item]:
    out: list[Item] = []
    pc = cfg.get("papers", {})
    if not pc.get("enabled", False):
        return out
    for s in pc.get("europe_pmc", []):
        params = {"query": s["query"], "format": "json", "pageSize": int(s.get("limit", 10)), "sort": "FIRST_PDATE_D desc"}
        try:
            r = SESSION.get("https://www.ebi.ac.uk/europepmc/webservices/rest/search", params=params, timeout=25)
            r.raise_for_status()
        except Exception as ex:
            print(f"[WARN] Europe PMC search failed: {s.get('name')}: {ex}")
            continue
        for rec in r.json().get("resultList", {}).get("result", []):
            doi = rec.get("doi", "")
            url = f"https://doi.org/{doi}" if doi else rec.get("fullTextUrlList", {}).get("fullTextUrl", [{}])[0].get("url", "")
            if not url and rec.get("pmid"):
                url = f"https://europepmc.org/article/MED/{rec.get('pmid')}"
            out.append(Item(
                source=s.get("name", "Europe PMC"), platform="Paper",
                title=rec.get("title") or "Paper", url=url,
                published=rec.get("firstPublicationDate") or rec.get("pubYear", ""),
                summary=rec.get("abstractText", "")[:900], tags=["paper", "europe-pmc"],
            ))
    return [x for x in out if x.url]


def collect_patent_links(cfg: dict[str, Any]) -> list[Item]:
    """Create watch links for patent searches. This avoids brittle scraping and keeps the workflow legal/stable."""
    out: list[Item] = []
    pc = cfg.get("patents", {})
    if not pc.get("enabled", False):
        return out
    today = datetime.now().astimezone().strftime("%Y-%m-%d")
    for s in pc.get("search_links", []):
        out.append(Item(
            source=s.get("name", "Patent search"), platform="Patent",
            title=s.get("name", "Patent search"), url=s.get("url", ""),
            published=today, summary=s.get("note", "Patent search watch link"), tags=["patent"],
        ))
    return [x for x in out if x.url]


def dedupe(items: list[Item]) -> list[Item]:
    seen = set()
    out = []
    for it in items:
        key = it.url.split("?")[0].rstrip("/")
        if key in seen:
            continue
        seen.add(key)
        out.append(it)
    return out


def render_markdown(items: list[Item], cfg: dict[str, Any]) -> str:
    now = datetime.now().astimezone()
    lines = [
        "---",
        f"date: {now.strftime('%Y-%m-%d')}",
        "type: semiconductor-dispatch-intel",
        "tags: [半导体, 自动派工, 情报简报]",
        "---",
        "",
        f"# 半导体自动派工情报简报 - {now.strftime('%Y-%m-%d')}",
        "",
        f"> 生成时间：{now.strftime('%Y-%m-%d %H:%M:%S %z')}；条目数：{len(items)}",
        "",
        "## 阅读说明",
        "",
        "- 本简报以简体中文为主，保留必要专业词汇，例如 Dispatch Rule、WIP、AMHS、MES、AI Scheduling、Cycle Time。",
        "- 外部来源的标题与摘要可能为英文，已在每条信息下方补充“中文导读”。",
        "- OCR、RSS、API 返回内容可能存在噪声，关键资料请打开原链接确认。",
        "",
    ]
    by_platform: dict[str, list[Item]] = {}
    for it in items:
        by_platform.setdefault(it.platform, []).append(it)
    for platform in sorted(by_platform):
        platform_title = PLATFORM_CN.get(platform, platform)
        lines += [f"## {platform_title}", ""]
        for it in by_platform[platform]:
            tags = " ".join(f"#{t}" for t in (it.tags or []))
            lines += [
                f"### [{it.title}]({it.url})",
                f"- 来源：{it.source}",
                f"- 时间：{it.published or '未知'}",
                f"- 分类：{it.category}",
                f"- 相关度：{it.score}",
                f"- 标签：{tags}" if tags else "- 标签：",
                f"- 中文导读：{chinese_digest(it)}",
            ]
            if it.summary:
                lines.append(f"- 原文摘要：{it.summary[:500]}")
            lines.append("")
    lines += [
        "## 处理建议",
        "",
        "- [ ] 优先阅读相关度高且分类为“派工规则 / WIP / AMHS / MES / AI 调度”的条目",
        "- [ ] 将高价值条目移动到专题笔记或建立 wiki-link",
        "- [ ] 对明显无关的条目记录噪声来源，并更新关键词 / 来源配置",
        "- [ ] 对涉及公司内部派工逻辑的启发，单独沉淀到内部专题笔记",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    cfg = load_config()
    output = cfg.get("output", {})
    cache_dir = ROOT / output.get("cache_dir", "cache")
    inbox_dir = ROOT / output.get("inbox_dir", "inbox")
    cache_dir.mkdir(exist_ok=True)
    inbox_dir.mkdir(exist_ok=True)

    keywords = cfg.get("keywords", {}).get("core", []) + cfg.get("keywords", {}).get("vendors_and_systems", [])
    items: list[Item] = []
    for collector in (collect_rss, collect_github, collect_reddit, collect_x, collect_semantic_scholar, collect_europe_pmc, collect_patent_links):
        items.extend(collector(cfg))
    items = dedupe(items)
    for it in items:
        it.score = score_item(it, keywords)
        it.category = classify_item(it)
    items.sort(key=lambda x: (x.score, x.published), reverse=True)
    items = items[: int(output.get("max_items_per_run", 120))]

    today = datetime.now().astimezone().strftime("%Y-%m-%d")
    md_path = inbox_dir / f"{today}.md"
    json_path = cache_dir / f"{today}.json"
    md_path.write_text(render_markdown(items, cfg), encoding="utf-8")
    json_path.write_text(json.dumps([asdict(i) | {"id": i.id} for i in items], ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {md_path.relative_to(ROOT)} ({len(items)} items)")
    print(f"Wrote {json_path.relative_to(ROOT)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
