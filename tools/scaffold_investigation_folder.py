#!/usr/bin/env python3
"""
Create a dated Investigation_YYYY-MM-DD/ folder with templates and subfolders.

Designed for the reader's machine (Desktop, Documents, etc.) — not inside this git repo.

Usage:
    python tools/scaffold_investigation_folder.py
    python tools/scaffold_investigation_folder.py --output-dir C:\\Users\\You\\Documents
    python tools/scaffold_investigation_folder.py --date 2026-06-27 --dry-run

Exit code: 0 on success; 1 on error or if target exists without --force.
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from evidence_lib import new_evidence_document
from psw_calm_ui import banner, info, ok

REPO_ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = REPO_ROOT / "Start-Guide" / "shared-templates" / "templates"

SUBDIRS = (
    "screenshots/file_properties",
    "screenshots/scan_results",
    "screenshots/network_router",
    "network_captures",
    "tool_exports",
    "scripts_reviewed",
    "framework_session",
)

START_HERE = """# Investigation folder — start here

**Created:** {date_stamp}

## First steps

1. Open `investigation_log_{date_stamp}.md` and begin Phase 0 (document first).
2. Add suspicious files to `suspicious_files_inventory_{date_stamp}.md`.
3. Paste your OS framework into an LLM — see `framework_session/README.md`.
4. Save screenshots under `screenshots/` (never delete originals on disk until pros advise).
5. Optional: use `evidence_{date_stamp}.json` + tools in Personal_Security_Walkthrough/tools/

## Evidence JSON (optional automation)

- `evidence_{date_stamp}.json` — structured metadata (validates against evidence_schema.json)
- `python .../tools/collect_file_metadata.py --evidence evidence_{date_stamp}.json --path <file>`
- `python .../tools/generate_llm_prompt.py --evidence evidence_{date_stamp}.json`
- `python .../tools/generate_pro_summary.py --evidence evidence_{date_stamp}.json`

Markdown logs remain your primary human-readable record.

## Guides (Personal Security Walkthrough)

- Quick Start: https://github.com/Squirrel814/Personal_Security_Walkthrough/blob/main/Start-Guide/Quick-Start-Guide.md
- When to escalate: https://github.com/Squirrel814/Personal_Security_Walkthrough/blob/main/Start-Guide/When-and-How_to-Escalate.md

**Not legal advice.** Document everything. Do not run suspicious scripts.
"""

FRAMEWORK_README = """# Framework session

Copy your OS framework file here for convenience (optional):

- Windows Minimal: Personal_Security_Walkthrough/minimal-tools/windows/
- macOS Minimal: Personal_Security_Walkthrough/minimal-tools/macos/
- Linux Minimal: Personal_Security_Walkthrough/minimal-tools/linux/

Paste the framework into your LLM at the start of each session.
End with: "Append Session Summary to my log"
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Scaffold Investigation_YYYY-MM-DD/ with templates and subfolders."
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path.cwd(),
        help="Parent directory for the new folder (default: current directory)",
    )
    parser.add_argument(
        "--date",
        type=str,
        default=date.today().isoformat(),
        help="Date stamp YYYY-MM-DD (default: today)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print actions without creating files",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Allow creating into an existing empty or non-empty folder name collision",
    )
    parser.add_argument(
        "--os",
        choices=("windows", "macos", "linux", "unknown"),
        default="unknown",
        help="OS family for evidence JSON (default: unknown)",
    )
    return parser.parse_args()


def validate_date(stamp: str) -> None:
    if len(stamp) != 10 or stamp[4] != "-" or stamp[7] != "-":
        raise ValueError(f"Invalid --date {stamp!r}; use YYYY-MM-DD")


def is_inside_repo(target: Path) -> bool:
    try:
        target.resolve().relative_to(REPO_ROOT.resolve())
        return True
    except ValueError:
        return False


def scaffold(
    output_dir: Path, date_stamp: str, dry_run: bool, force: bool, os_family: str
) -> Path:
    root_name = f"Investigation_{date_stamp}"
    inv_root = (output_dir / root_name).resolve()

    if is_inside_repo(inv_root):
        print(
            "ERROR: Refusing to create investigation folder inside the git repo.\n"
            "Use --output-dir pointing to Documents, Desktop, or another local path.",
            file=sys.stderr,
        )
        sys.exit(1)

    if inv_root.exists() and not force:
        print(f"ERROR: {inv_root} already exists. Use --force to proceed anyway.", file=sys.stderr)
        sys.exit(1)

    log_src = TEMPLATES / "investigation_log_template.md"
    inv_src = TEMPLATES / "suspicious_files_inventory_template.md"
    blocklist_src = REPO_ROOT / "tools" / "blocklist_export_template.txt"

    for src in (log_src, inv_src):
        if not src.is_file():
            print(f"ERROR: missing template {src}", file=sys.stderr)
            sys.exit(1)

    actions: list[str] = []

    def mkdir(p: Path) -> None:
        actions.append(f"mkdir {p}")
        if not dry_run:
            p.mkdir(parents=True, exist_ok=True)

    def write_text(p: Path, content: str) -> None:
        actions.append(f"write {p}")
        if not dry_run:
            p.write_text(content, encoding="utf-8")

    def copy_file(src: Path, dest: Path) -> None:
        actions.append(f"copy {src} -> {dest}")
        if not dry_run:
            shutil.copy2(src, dest)

    mkdir(inv_root)
    for sub in SUBDIRS:
        mkdir(inv_root / sub)

    copy_file(log_src, inv_root / f"investigation_log_{date_stamp}.md")
    copy_file(inv_src, inv_root / f"suspicious_files_inventory_{date_stamp}.md")

    summary_path = inv_root / f"summary_for_professionals_{date_stamp}.md"
    write_text(
        summary_path,
        f"# Summary for Professionals\n\n**Date:** {date_stamp}\n\n"
        "Use when escalating. See Start-Guide/How-to-Prepare-a-Professional-Summary.md\n",
    )

    if blocklist_src.is_file():
        copy_file(blocklist_src, inv_root / "tool_exports" / "blocklist_template.txt")

    write_text(inv_root / "START_HERE.md", START_HERE.format(date_stamp=date_stamp))
    write_text(inv_root / "framework_session" / "README.md", FRAMEWORK_README)

    evidence_doc = new_evidence_document(date_stamp, os_family=os_family)
    evidence_json = json.dumps(evidence_doc, indent=2, ensure_ascii=False) + "\n"
    write_text(inv_root / f"evidence_{date_stamp}.json", evidence_json)

    gitkeep = "# Keep this folder in your backup scope.\n"
    for sub in ("screenshots/file_properties", "network_captures", "tool_exports", "scripts_reviewed"):
        write_text(inv_root / sub / ".gitkeep", gitkeep)

    for line in actions:
        print(line)
    print(f"\n{'[dry-run] ' if dry_run else ''}Ready: {inv_root}")
    return inv_root


def main() -> int:
    args = parse_args()
    try:
        validate_date(args.date)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    output_dir = args.output_dir.expanduser().resolve()
    if not output_dir.is_dir():
        print(f"ERROR: output directory does not exist: {output_dir}", file=sys.stderr)
        return 1

    if not args.dry_run:
        banner("Scaffold investigation folder", f"Investigation_{args.date}")
    scaffold(output_dir, args.date, args.dry_run, args.force, args.os)
    if not args.dry_run:
        ok(f"Investigation_{args.date} ready")
        info("Markdown logs + evidence JSON created. Document first.")
    return 0


if __name__ == "__main__":
    sys.exit(main())