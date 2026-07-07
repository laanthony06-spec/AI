from __future__ import annotations

"""A tiny read-only JSON-RPC style server for local Obsidian vault search.

This is intentionally conservative:
- read-only
- workspace-root bounded
- no network server by default; communicates over stdio

It is not a full production MCP implementation yet. It is a safe local
prototype that can be adapted to a proper MCP SDK server later.
"""

import json
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[3]
ALLOWED_EXTS = {".md", ".txt", ".json", ".csv", ".yml", ".yaml"}
EXCLUDED_PARTS = {".git", ".obsidian", ".venv", "__pycache__"}


def safe_path(path: str) -> Path:
    p = (VAULT / path).resolve()
    if VAULT.resolve() not in p.parents and p != VAULT.resolve():
        raise ValueError("path escapes vault")
    if not p.exists() or not p.is_file():
        raise FileNotFoundError(path)
    if p.suffix.lower() not in ALLOWED_EXTS:
        raise ValueError("unsupported file type")
    return p


def list_notes(prefix: str = "", limit: int = 200) -> list[str]:
    base = (VAULT / prefix).resolve() if prefix else VAULT.resolve()
    if VAULT.resolve() not in base.parents and base != VAULT.resolve():
        raise ValueError("prefix escapes vault")
    out = []
    for p in base.rglob("*"):
        if len(out) >= limit:
            break
        if p.is_file() and p.suffix.lower() in ALLOWED_EXTS and not any(part in EXCLUDED_PARTS for part in p.parts):
            out.append(p.relative_to(VAULT).as_posix())
    return out


def read_note(path: str, max_chars: int = 20000) -> dict:
    p = safe_path(path)
    text = p.read_text(encoding="utf-8", errors="replace")[:max_chars]
    return {"path": p.relative_to(VAULT).as_posix(), "text": text}


def search_notes(query: str, prefix: str = "", limit: int = 50) -> list[dict]:
    terms = [t.lower() for t in query.split() if t.strip()]
    results = []
    for path in list_notes(prefix, limit=2000):
        p = VAULT / path
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        low = text.lower()
        if all(t in low for t in terms):
            snippet = text[:500].replace("\n", " ")
            results.append({"path": path, "snippet": snippet})
        if len(results) >= limit:
            break
    return results


def handle(method: str, params: dict) -> object:
    if method == "list_notes":
        return list_notes(params.get("prefix", ""), int(params.get("limit", 200)))
    if method == "read_note":
        return read_note(params["path"], int(params.get("max_chars", 20000)))
    if method == "search_notes":
        return search_notes(params["query"], params.get("prefix", ""), int(params.get("limit", 50)))
    raise ValueError(f"unknown method: {method}")


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stdin.reconfigure(encoding="utf-8")
    except Exception:
        pass
    for line in sys.stdin:
        try:
            req = json.loads(line)
            result = handle(req.get("method", ""), req.get("params", {}) or {})
            resp = {"id": req.get("id"), "result": result}
        except Exception as e:
            resp = {"id": None, "error": str(e)}
        print(json.dumps(resp, ensure_ascii=False), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
