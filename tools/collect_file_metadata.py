#!/usr/bin/env python3
"""
Append file metadata (timestamps, size, optional SHA-256) to evidence JSON.

Document first — reads files only; never executes suspicious binaries.

Usage:
    python tools/collect_file_metadata.py --evidence ./Investigation_2026-06-27/evidence_2026-06-27.json \\
        --path "C:\\Users\\You\\Downloads\\suspicious.txt" --why "Future timestamp in filename"

    python tools/collect_file_metadata.py --evidence evidence.json --path ./folder --recursive --hash

Exit code: 0 on success; 1 on error.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from evidence_lib import assert_valid, iso_now, load_evidence
from psw_calm_ui import banner, info, ok, step, warn


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Collect file metadata into PSW evidence JSON (read-only)."
    )
    parser.add_argument("--evidence", type=Path, required=True, help="evidence_YYYY-MM-DD.json")
    parser.add_argument(
        "--path",
        type=Path,
        required=True,
        help="File or directory to document (not executed)",
    )
    parser.add_argument("--why", type=str, default="", help="Why suspicious (short note)")
    parser.add_argument(
        "--hash",
        action="store_true",
        help="Compute SHA-256 (skips files larger than --max-hash-mb)",
    )
    parser.add_argument(
        "--max-hash-mb",
        type=int,
        default=50,
        help="Max file size in MB to hash (default: 50)",
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="If --path is a directory, include files recursively",
    )
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing JSON")
    return parser.parse_args()


def stat_to_iso(ts: float) -> str:
    return datetime.fromtimestamp(ts, tz=timezone.utc).astimezone().replace(microsecond=0).isoformat()


def sha256_file(path: Path, max_bytes: int) -> str | None:
    size = path.stat().st_size
    if size > max_bytes:
        return None
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def iter_paths(root: Path, recursive: bool) -> list[Path]:
    if root.is_file():
        return [root]
    if not root.is_dir():
        return []
    if recursive:
        return [p for p in root.rglob("*") if p.is_file()]
    return [p for p in root.iterdir() if p.is_file()]


def entry_for(path: Path, why: str, do_hash: bool, max_hash_bytes: int) -> dict:
    st = path.stat()
    entry: dict = {
        "path": str(path.resolve()),
        "created": stat_to_iso(st.st_ctime),
        "modified": stat_to_iso(st.st_mtime),
        "accessed": stat_to_iso(st.st_atime),
        "size_bytes": st.st_size,
        "sha256": None,
        "why_suspicious": why,
        "status": "documented",
        "notes": f"Collected {iso_now()} via collect_file_metadata.py",
        "screenshot": None,
    }
    if do_hash:
        entry["sha256"] = sha256_file(path, max_hash_bytes)
        if entry["sha256"] is None and st.st_size > max_hash_bytes:
            entry["notes"] += f"; hash skipped (>{max_hash_bytes // (1024 * 1024)} MB)"
    return entry


def main() -> int:
    args = parse_args()
    evidence_path = args.evidence.expanduser().resolve()
    target = args.path.expanduser().resolve()

    if not evidence_path.is_file():
        print(f"ERROR: evidence file not found: {evidence_path}", file=sys.stderr)
        return 1
    if not target.exists():
        print(f"ERROR: path not found: {target}", file=sys.stderr)
        return 1

    banner("Collect file metadata", "Read-only · document first")
    data = load_evidence(evidence_path)
    paths = iter_paths(target, args.recursive)
    if not paths:
        warn("No files found to document.")
        return 1

    existing = {e.get("path") for e in data.get("files", []) if isinstance(e, dict)}
    max_hash_bytes = args.max_hash_mb * 1024 * 1024
    added = 0

    for i, fp in enumerate(paths, start=1):
        step(i, len(paths), fp.name)
        resolved = str(fp.resolve())
        if resolved in existing:
            info(f"Skip (already in JSON): {fp.name}")
            continue
        try:
            entry = entry_for(fp, args.why, args.hash, max_hash_bytes)
        except OSError as exc:
            warn(f"Could not read {fp}: {exc}")
            continue
        if not args.dry_run:
            data.setdefault("files", []).append(entry)
        ok(f"Documented {fp.name} ({entry['size_bytes']} bytes)")
        added += 1

    if added == 0:
        info("No new entries added.")
        return 0

    if args.dry_run:
        info(f"[dry-run] Would append {added} file(s).")
        return 0

    assert_valid(data)
    evidence_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    ok(f"Wrote {added} new file(s) to {evidence_path.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())