#!/usr/bin/env python3
"""Build/extend CSL-JSON evidence registry from URL seeds.

Usage:
  python scripts/scrape_citations.py --seed-file seed-urls.txt
  python scripts/scrape_citations.py --url https://example.org/page

Notes:
- Uses Crossref when DOI is detected.
- Falls back to webpage <title> extraction.
- Adds project metadata into CSL `note` field.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "evidence-registry.csl.json"

DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.I)
TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.I | re.S)


def load_registry() -> list[dict]:
    if not REGISTRY_PATH.exists():
        return []
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


def save_registry(items: list[dict]) -> None:
    REGISTRY_PATH.write_text(json.dumps(items, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def fetch_text(url: str) -> str:
    req = Request(url, headers={"User-Agent": "agentic-research-patterns/1.0"})
    with urlopen(req, timeout=20) as resp:
        return resp.read(1_000_000).decode("utf-8", errors="ignore")


def find_doi(url: str, html: str) -> str | None:
    from_url = DOI_RE.search(url)
    if from_url:
        return from_url.group(0)
    from_html = DOI_RE.search(html)
    return from_html.group(0) if from_html else None


def fetch_crossref(doi: str) -> dict | None:
    api_url = f"https://api.crossref.org/works/{doi}"
    try:
        raw = fetch_text(api_url)
    except Exception:
        return None
    data = json.loads(raw)
    msg = data.get("message", {})
    title = (msg.get("title") or [""])[0]
    issued = msg.get("issued") or {"date-parts": [[None]]}
    authors = []
    for a in msg.get("author", []):
        authors.append({"family": a.get("family", ""), "given": a.get("given", "")})
    return {
        "type": "article-journal",
        "title": title,
        "author": authors,
        "container-title": (msg.get("container-title") or [""])[0],
        "DOI": doi,
        "URL": msg.get("URL", ""),
        "issued": issued,
    }


def fallback_entry(url: str, html: str) -> dict:
    title_match = TITLE_RE.search(html)
    title = title_match.group(1).strip() if title_match else urlparse(url).netloc
    return {
        "type": "webpage",
        "title": re.sub(r"\s+", " ", title),
        "URL": url,
        "issued": {"date-parts": [[date.today().year]]},
    }


def make_id(idx: int, url: str) -> str:
    host = urlparse(url).netloc.replace("www.", "").split(":")[0].replace(".", "-")
    return f"hitl-{date.today().year}-{host}-{idx:04d}"


def merge(existing: list[dict], new_items: list[dict]) -> list[dict]:
    seen = {item.get("URL") for item in existing}
    for item in new_items:
        if item.get("URL") not in seen:
            existing.append(item)
            seen.add(item.get("URL"))
    return existing


def build_note(tier: str, cluster: str) -> str:
    return "\n".join([
        f"evidence_tier: {tier}",
        f"cluster: {cluster}",
        "method_tags: to_tag",
        "hitl_role: to_tag",
        "limitations: to_fill",
        "use_for: to_fill",
        "do_not_use_for: to_fill",
        f"accessed_date: {date.today().isoformat()}",
    ])


def process_url(url: str, idx: int, tier: str, cluster: str, offline: bool=False) -> dict:
    if offline:
        base = {"type":"webpage","title":urlparse(url).netloc.replace("www.",""),"URL":url,"issued":{"date-parts":[[date.today().year]]}}
        base["id"] = make_id(idx, url)
        base["note"] = build_note(tier, cluster)
        return base
    html = fetch_text(url)
    doi = find_doi(url, html)
    if doi:
        base = fetch_crossref(doi) or fallback_entry(url, html)
        base.setdefault("DOI", doi)
        base.setdefault("URL", url)
    else:
        base = fallback_entry(url, html)
    base["id"] = make_id(idx, url)
    base["note"] = build_note(tier, cluster)
    return base


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed-file", type=Path)
    parser.add_argument("--url", action="append", default=[])
    parser.add_argument("--tier", default="T4")
    parser.add_argument("--cluster", default="framework_implementation_docs")
    parser.add_argument("--offline", action="store_true", help="Skip network fetch and create URL-only stubs")
    parser.add_argument("--query-file", type=Path, help="JSON file of search queries for batch planning")
    args = parser.parse_args()

    urls = list(args.url)
    if args.seed_file and args.seed_file.exists():
        urls.extend([ln.strip() for ln in args.seed_file.read_text(encoding="utf-8").splitlines() if ln.strip() and not ln.startswith("#")])
    if args.query_file and args.query_file.exists():
        print(f"Loaded query plan: {args.query_file}")
    if not urls and not args.query_file:
        raise SystemExit("Provide --url or --seed-file or --query-file")

    existing = load_registry()
    start_idx = len(existing) + 1
    scraped = []
    for i, u in enumerate(urls, start=start_idx):
        try:
            scraped.append(process_url(u, i, args.tier, args.cluster, args.offline))
            print(f"OK {u}")
        except Exception as exc:
            print(f"ERR {u}: {exc}")

    if args.query_file and args.query_file.exists():
        try:
            q = json.loads(args.query_file.read_text(encoding="utf-8"))
            for entry in q.get("queries", []):
                qid = entry.get("id", "q")
                qq = entry.get("q", "")
                clu = entry.get("cluster", "to_cluster")
                rec = {"id": f"hitl-query-{qid}", "type": "dataset", "title": f"Query plan: {qq}", "URL": f"query://{qid}", "issued": {"date-parts": [[date.today().year]]}, "note": build_note("T5", clu)}
                scraped.append(rec)
        except Exception as exc:
            print(f"WARN query-file parse failed: {exc}")

    merged = merge(existing, scraped)
    save_registry(merged)
    print(f"Saved {len(merged)} records to {REGISTRY_PATH}")


if __name__ == "__main__":
    main()
