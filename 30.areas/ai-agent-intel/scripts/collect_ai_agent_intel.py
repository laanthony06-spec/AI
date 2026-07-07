from __future__ import annotations

import json
import os
import re
import sys
import time
import html
import hashlib
import urllib.parse
import urllib.request
import ssl
import xml.etree.ElementTree as ET
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config" / "sources.json"
ENV_PATH = ROOT / ".env"

UA = "obsidian-ai-agent-intel/0.1"


def load_env() -> None:
    if not ENV_PATH.exists():
        return
    for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        if k and k not in os.environ:
            os.environ[k] = v.strip()


def load_config() -> dict[str, Any]:
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def request_json(url: str, params: dict[str, Any] | None = None, headers: dict[str, str] | None = None, timeout: int = 30) -> dict[str, Any]:
    if params:
        url = url + ("&" if "?" in url else "?") + urllib.parse.urlencode(params)
    req_headers = {"User-Agent": UA, "Accept": "application/json"}
    if headers:
        req_headers.update(headers)
    req = urllib.request.Request(url, headers=req_headers)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = resp.read()
    return json.loads(data.decode("utf-8", errors="replace"))


def request_text(url: str, timeout: int = 30) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/rss+xml, application/atom+xml, text/xml, */*"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read()
    except Exception as e:
        # Some Windows/Python environments lack a complete CA chain for public RSS
        # endpoints such as arXiv. Retry read-only public feeds with an unverified
        # context rather than failing the whole daily brief.
        if "CERTIFICATE_VERIFY_FAILED" not in str(e):
            raise
        ctx = ssl._create_unverified_context()
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            data = resp.read()
    return data.decode("utf-8", errors="replace")


def clean_text(s: Any, limit: int = 900) -> str:
    if s is None:
        return ""
    s = html.unescape(str(s))
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s[:limit]


@dataclass
class Item:
    platform: str
    source: str
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


CATEGORY_RULES: dict[str, list[str]] = {
    "Agent 框架": ["agent framework", "langgraph", "crewai", "autogen", "autogpt", "semantic kernel", "framework"],
    "工具调用 / MCP": ["tool use", "function calling", "model context protocol", " mcp ", "tools", "connector"],
    "多智能体": ["multi-agent", "multi agent", "swarm", "collaboration", "协作", "多智能体"],
    "代码 / 浏览器 Agent": ["coding agent", "code agent", "browser agent", "computer use", "web agent", "automation"],
    "RAG / 记忆": ["rag", "retrieval", "memory", "knowledge base", "vector", "embedding"],
    "评测 / 安全": ["eval", "benchmark", "safety", "guardrail", "alignment", "security", "prompt injection"],
    "论文": ["arxiv", "paper", "abstract", "conference", "benchmark"],
    "产品动态": ["release", "launch", "api", "sdk", "platform", "openai", "anthropic", "google", "microsoft"],
}


def classify(item: Item) -> str:
    hay = f"{item.platform} {item.source} {item.title} {item.summary} {' '.join(item.tags or [])}".lower()
    best = ("未分类", 0)
    for cat, terms in CATEGORY_RULES.items():
        sc = sum(1 for t in terms if t.lower() in hay)
        if sc > best[1]:
            best = (cat, sc)
    return best[0]


def score_item(item: Item, keywords: list[str]) -> int:
    hay = f"{item.title} {item.summary}".lower()
    score = 0
    for kw in keywords:
        parts = [p for p in kw.lower().replace('"', "").split() if p]
        if parts and all(p in hay for p in parts):
            score += max(1, len(parts))
    if item.category != "未分类":
        score += 1
    return score


def chinese_digest(item: Item) -> str:
    category_hint = {
        "Agent 框架": "关注它是否提供 Agent 编排、状态管理、工具调用和生产化部署能力。",
        "工具调用 / MCP": "关注它如何连接外部工具、数据源和上下文，尤其适合沉淀到 MCP / connector 知识。",
        "多智能体": "关注任务分解、角色协作、通信机制和冲突处理。",
        "代码 / 浏览器 Agent": "关注自动写代码、浏览器操作、Computer Use、端到端自动化能力。",
        "RAG / 记忆": "关注长期记忆、检索增强、知识库和上下文压缩策略。",
        "评测 / 安全": "关注 benchmark、可靠性、权限边界、prompt injection 和 guardrail。",
        "论文": "建议提取问题定义、方法、实验指标和可复用模型结构。",
        "产品动态": "关注 API、SDK、平台能力变化，以及是否会影响你的工具链选择。",
    }
    text = f"{item.title} {item.summary}".lower()
    signals = []
    if any(k in text for k in ["mcp", "model context protocol", "tool", "function calling"]):
        signals.append("工具调用 / MCP")
    if any(k in text for k in ["multi-agent", "swarm", "collaboration"]):
        signals.append("多智能体")
    if any(k in text for k in ["coding", "browser", "computer use", "automation"]):
        signals.append("自动化 / Coding Agent")
    if any(k in text for k in ["rag", "retrieval", "memory"]):
        signals.append("RAG / Memory")
    if any(k in text for k in ["benchmark", "eval", "safety", "security"]):
        signals.append("评测 / 安全")
    s = category_hint.get(item.category, "建议判断它是否能补充你的 Agent 方法论、工具链或案例库。")
    if signals:
        s += " 关键词信号：" + "、".join(dict.fromkeys(signals)) + "。"
    if item.score >= 8:
        s += " 相关度较高，建议优先阅读。"
    elif item.score >= 4:
        s += " 相关度中等，可快速浏览。"
    else:
        s += " 相关度较低，可作为背景信息。"
    return s


def collect_github(cfg: dict[str, Any]) -> list[Item]:
    out: list[Item] = []
    gh = cfg.get("github", {})
    if not gh.get("enabled"):
        return out
    token = os.getenv("GITHUB_TOKEN", "").strip()
    headers = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    for s in gh.get("searches", []):
        endpoint = "repositories" if s.get("type") == "repositories" else "issues"
        params = {
            "q": s["query"],
            "sort": s.get("sort", "updated"),
            "order": s.get("order", "desc"),
            "per_page": 20,
        }
        try:
            data = request_json(f"https://api.github.com/search/{endpoint}", params=params, headers=headers)
        except Exception as e:
            print(f"[WARN] GitHub 搜索失败：{s.get('name')}：{e}")
            continue
        for it in data.get("items", []):
            if endpoint == "repositories":
                out.append(Item(
                    platform="GitHub",
                    source=s.get("name", "GitHub"),
                    title=it.get("full_name") or it.get("name") or "GitHub repository",
                    url=it.get("html_url", ""),
                    published=it.get("updated_at", ""),
                    summary=clean_text(it.get("description", "")),
                    tags=["github", "repo"],
                ))
            else:
                out.append(Item(
                    platform="GitHub",
                    source=s.get("name", "GitHub"),
                    title=it.get("title") or "GitHub issue",
                    url=it.get("html_url", ""),
                    published=it.get("updated_at", ""),
                    summary=clean_text(it.get("body", "")),
                    tags=["github", "issue"],
                ))
    return [x for x in out if x.url]


def parse_feed(xml: str, source: str, tags: list[str]) -> list[Item]:
    out: list[Item] = []
    try:
        root = ET.fromstring(xml)
    except Exception:
        return out
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    # RSS
    for e in root.findall(".//item"):
        title = clean_text(e.findtext("title"))
        url = clean_text(e.findtext("link"))
        published = clean_text(e.findtext("pubDate"))
        summary = clean_text(e.findtext("description"))
        if title and url:
            out.append(Item("RSS", source, title, url, published, summary, tags))
    # Atom / arXiv
    for e in root.findall(".//atom:entry", ns):
        title = clean_text(e.findtext("atom:title", default="", namespaces=ns))
        link = ""
        for l in e.findall("atom:link", ns):
            if l.attrib.get("href"):
                link = l.attrib["href"]
                break
        published = clean_text(e.findtext("atom:published", default=e.findtext("atom:updated", default="", namespaces=ns), namespaces=ns))
        summary = clean_text(e.findtext("atom:summary", default="", namespaces=ns))
        if title and link:
            out.append(Item("RSS", source, title, link, published, summary, tags))
    return out


def collect_rss(cfg: dict[str, Any]) -> list[Item]:
    out: list[Item] = []
    rss = cfg.get("rss", {})
    if not rss.get("enabled"):
        return out
    for feed in rss.get("feeds", []):
        try:
            xml = request_text(feed["url"])
            out.extend(parse_feed(xml, feed.get("name", feed["url"]), feed.get("tags", []))[:30])
        except Exception as e:
            print(f"[WARN] RSS 获取失败：{feed.get('name')}：{e}")
    return out


def collect_x(cfg: dict[str, Any]) -> list[Item]:
    out: list[Item] = []
    xc = cfg.get("x", {})
    token = os.getenv("X_BEARER_TOKEN", "").strip()
    if not xc.get("enabled") or not token:
        return out
    headers = {"Authorization": f"Bearer {token}"}
    for s in xc.get("searches", []):
        params = {
            "query": s["query"],
            "max_results": int(s.get("max_results", 10)),
            "tweet.fields": "created_at,author_id,public_metrics,lang"
        }
        try:
            data = request_json("https://api.x.com/2/tweets/search/recent", params=params, headers=headers)
        except Exception as e:
            print(f"[WARN] X 搜索失败：{s.get('name')}：{e}")
            continue
        for tw in data.get("data", []):
            tid = tw.get("id", "")
            text = clean_text(tw.get("text", ""))
            out.append(Item("X", s.get("name", "X"), text[:120] or "X post", f"https://x.com/i/web/status/{tid}", tw.get("created_at", ""), text, ["x"]))
    return out


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


PLATFORM_CN = {
    "GitHub": "GitHub 开源动态",
    "RSS": "RSS / 论文 / 社区资讯",
    "X": "X / Twitter 实时动态"
}


def render_markdown(items: list[Item]) -> str:
    now = datetime.now().astimezone()
    lines = [
        "---",
        f"date: {now.strftime('%Y-%m-%d')}",
        "type: ai-agent-intel",
        "tags: [AI, Agent, 智能体, 情报简报]",
        "---",
        "",
        f"# AI / Agent 每日情报简报 - {now.strftime('%Y-%m-%d')}",
        "",
        f"> 生成时间：{now.strftime('%Y-%m-%d %H:%M:%S %z')}；条目数：{len(items)}",
        "",
        "## 阅读说明",
        "",
        "- 本简报聚焦 AI Agent、LLM Agent、多智能体、工具调用、MCP、Coding Agent、RAG / Memory、评测与安全。",
        "- 标题和原文摘要保留原语言；每条补充中文导读，方便快速判断是否值得深读。",
        "- 如果 X 未配置 Bearer Token，会自动跳过 X。",
        "",
    ]
    grouped: dict[str, list[Item]] = {}
    for it in items:
        grouped.setdefault(it.platform, []).append(it)
    for platform in sorted(grouped):
        lines += [f"## {PLATFORM_CN.get(platform, platform)}", ""]
        for it in grouped[platform]:
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
                lines.append(f"- 原文摘要：{it.summary}")
            lines.append("")
    lines += [
        "## 处理建议",
        "",
        "- [ ] 优先阅读“工具调用 / MCP”“Agent 框架”“评测 / 安全”类高相关度条目",
        "- [ ] 把高价值内容沉淀到 Agent 方法论、工具链或案例库笔记",
        "- [ ] 对明显噪声条目调整 `config/sources.json` 关键词",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    load_env()
    cfg = load_config()
    cache_dir = ROOT / cfg.get("output", {}).get("cache_dir", "cache")
    inbox_dir = ROOT / cfg.get("output", {}).get("inbox_dir", "inbox")
    cache_dir.mkdir(parents=True, exist_ok=True)
    inbox_dir.mkdir(parents=True, exist_ok=True)

    items: list[Item] = []
    items.extend(collect_github(cfg))
    items.extend(collect_rss(cfg))
    items.extend(collect_x(cfg))
    items = dedupe(items)
    for it in items:
        it.category = classify(it)
        it.score = score_item(it, cfg.get("keywords", []))
    items.sort(key=lambda x: (x.score, x.published), reverse=True)
    items = items[: int(cfg.get("output", {}).get("max_items_per_run", 120))]

    today = datetime.now().astimezone().strftime("%Y-%m-%d")
    md_path = inbox_dir / f"{today}.md"
    json_path = cache_dir / f"{today}.json"
    md_path.write_text(render_markdown(items), encoding="utf-8")
    json_path.write_text(json.dumps([asdict(x) | {"id": x.id} for x in items], ensure_ascii=False, indent=2), encoding="utf-8")
    (cache_dir / "last_run.log").write_text(f"{datetime.now().isoformat(timespec='seconds')} wrote {md_path} items={len(items)}\n", encoding="utf-8")
    print(f"Wrote {md_path.relative_to(ROOT)} ({len(items)} items)")
    print(f"Wrote {json_path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
