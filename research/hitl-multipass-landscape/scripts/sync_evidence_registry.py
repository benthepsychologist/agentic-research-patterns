#!/usr/bin/env python3
"""Sync evidence registry between CSL-JSON and YAML mirror.

Usage:
  python scripts/sync_evidence_registry.py --from-json
  python scripts/sync_evidence_registry.py --from-yaml

Note:
  --from-yaml requires PyYAML installed.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JSON_PATH = ROOT / "evidence-registry.csl.json"
YAML_PATH = ROOT / "evidence-registry.yaml"


def load_json() -> list[dict]:
    if not JSON_PATH.exists():
        return []
    return json.loads(JSON_PATH.read_text(encoding="utf-8"))


def write_json(data: list[dict]) -> None:
    JSON_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_yaml_from_json(data: list[dict]) -> None:
    try:
        import yaml  # type: ignore
    except ModuleNotFoundError:
        YAML_PATH.write_text(
            "# Install PyYAML for structured YAML sync: pip install pyyaml\n"
            "# Placeholder mirror generated without PyYAML\n[]\n",
            encoding="utf-8",
        )
        print(f"Wrote placeholder {YAML_PATH} (PyYAML missing)")
        return

    YAML_PATH.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8")


def load_yaml() -> list[dict]:
    try:
        import yaml  # type: ignore
    except ModuleNotFoundError as exc:
        raise SystemExit("PyYAML is required for --from-yaml. Install with: pip install pyyaml") from exc

    if not YAML_PATH.exists():
        return []
    parsed = yaml.safe_load(YAML_PATH.read_text(encoding="utf-8"))
    return parsed if isinstance(parsed, list) else []


def main() -> None:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--from-json", action="store_true")
    group.add_argument("--from-yaml", action="store_true")
    args = parser.parse_args()

    if args.from_json:
        write_yaml_from_json(load_json())
        print(f"Synced JSON -> YAML at {YAML_PATH}")
    else:
        write_json(load_yaml())
        print(f"Synced YAML -> JSON at {JSON_PATH}")


if __name__ == "__main__":
    main()
