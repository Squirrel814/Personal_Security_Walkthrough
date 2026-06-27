#!/usr/bin/env python3
"""
Validate investigation evidence JSON against the PSW schema (stdlib validator).

Usage:
    python tools/validate_evidence_json.py path/to/evidence_2026-06-27.json

Exit code: 0 if valid; 1 if invalid or unreadable.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from evidence_lib import ValidationError, load_evidence, validate_evidence
from psw_calm_ui import banner, info, ok, warn


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate PSW evidence JSON.")
    parser.add_argument("evidence_json", type=Path, help="Path to evidence_YYYY-MM-DD.json")
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Only print errors; no calm UI banner",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    path = args.evidence_json.expanduser().resolve()

    if not path.is_file():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        return 1

    if not args.quiet:
        banner("Evidence JSON validation", str(path.name))

    try:
        data = load_evidence(path)
    except json.JSONDecodeError as exc:
        warn(f"Invalid JSON: {exc}")
        return 1

    errors = validate_evidence(data)
    if errors:
        if not args.quiet:
            warn(f"{len(errors)} issue(s) found:")
            for err in errors:
                info(err)
        else:
            for err in errors:
                print(err, file=sys.stderr)
        return 1

    if not args.quiet:
        ok("Schema valid — required fields present.")
        inv = data.get("investigation", {})
        info(f"Investigation: {inv.get('id')} · phase {inv.get('phase')} ({inv.get('phase_name')})")
        info(f"Files logged: {len(data.get('files', []))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())