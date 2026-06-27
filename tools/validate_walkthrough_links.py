#!/usr/bin/env python3
"""
Validate internal relative links in Personal_Security_Walkthrough markdown and web hub.

Checks paths like ../Start-Guide/foo.md and Infographs/bar.jpg resolve under repo root.
Skips http(s), mailto, and anchor-only links.

Usage (from repo root):
    python tools/validate_walkthrough_links.py
    python tools/validate_walkthrough_links.py --strict   # also warn on legacy root Infograph_* refs

Exit code: 0 if all checked links resolve; 1 if any broken.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Files to scan for links
SCAN_GLOBS = (
    "README.md",
    "CONTRIBUTING.md",
    "Next-Steps_and_File-Path-Map.md",
    "My_Security_Investigation_Framework_v1.0.md",
    "Start-Guide/**/*.md",
    "defense/**/*.md",
    "minimal-tools/**/*.md",
    "full-deep-dive/**/*.md",
    "Infographs/**/*.md",
    "web/index.html",
)

# Markdown: [text](path) and <img src="path">
MD_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
HTML_HREF = re.compile(r"""href=["']([^"']+)["']""")
HTML_SRC = re.compile(r"""src=["']([^"']+)["']""")

SKIP_PREFIXES = ("http://", "https://", "mailto:", "#", "javascript:")


def collect_source_files() -> list[Path]:
    files: list[Path] = []
    for pattern in SCAN_GLOBS:
        files.extend(REPO_ROOT.glob(pattern))
    return sorted(set(files))


def extract_links(content: str, is_html: bool) -> list[str]:
    links: list[str] = []
    if is_html:
        for pat in (HTML_HREF, HTML_SRC):
            links.extend(m.group(1).strip() for m in pat.finditer(content))
    else:
        for m in MD_LINK.finditer(content):
            raw = m.group(1).strip()
            if " " in raw:
                raw = raw.split()[0]
            links.append(raw)
    return links


def should_skip(link: str) -> bool:
    if not link or link.startswith(SKIP_PREFIXES):
        return True
    if link.startswith("//"):
        return True
    return False


def resolve_link(source: Path, link: str) -> Path | None:
    """Return resolved path if file or directory exists; None if broken."""
    path_part = link.split("#", 1)[0].strip()
    if not path_part:
        return source if source.is_file() else None
    if path_part.startswith("/"):
        target = REPO_ROOT / path_part.lstrip("/")
    else:
        target = (source.parent / path_part).resolve()
    try:
        target.relative_to(REPO_ROOT.resolve())
    except ValueError:
        return None
    if target.is_file() or target.is_dir():
        return target
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate internal repo links.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat legacy root Infograph_* paths as warnings (prefer Infographs/).",
    )
    args = parser.parse_args()

    broken: list[tuple[Path, str]] = []
    warnings: list[tuple[Path, str]] = []
    checked = 0

    for source in collect_source_files():
        try:
            text = source.read_text(encoding="utf-8")
        except OSError as exc:
            print(f"ERROR: cannot read {source}: {exc}", file=sys.stderr)
            return 1

        is_html = source.suffix.lower() == ".html"
        for link in extract_links(text, is_html):
            if should_skip(link):
                continue
            checked += 1
            if resolve_link(source, link) is None:
                broken.append((source.relative_to(REPO_ROOT), link))
            elif args.strict and "Infograph_" in link and not link.startswith("../Infographs/"):
                warnings.append((source.relative_to(REPO_ROOT), link))

    if warnings:
        print("Warnings (legacy infograph paths):")
        for src, link in warnings:
            print(f"  {src}: {link}")
        print()

    if broken:
        print(f"Broken links ({len(broken)} of {checked} checked):")
        for src, link in broken:
            print(f"  {src}: {link}")
        return 1

    print(f"OK — {checked} internal links validated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())