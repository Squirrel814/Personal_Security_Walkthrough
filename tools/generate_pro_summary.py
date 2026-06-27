#!/usr/bin/env python3
"""
Auto-draft summary_for_professionals markdown from evidence JSON.

Usage:
    python tools/generate_pro_summary.py --evidence ./Investigation_2026-06-27/evidence_2026-06-27.json

Exit code: 0 on success; 1 on error.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from evidence_lib import iso_now, load_evidence
from psw_calm_ui import banner, info, ok, warn


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Draft professional summary markdown from evidence JSON."
    )
    parser.add_argument("--evidence", type=Path, required=True, help="evidence_YYYY-MM-DD.json")
    parser.add_argument(
        "--output",
        type=Path,
        help="Output path (default: summary_for_professionals_YYYY-MM-DD.md beside evidence)",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing summary file")
    return parser.parse_args()


def bullet_files(files: list) -> str:
    if not files:
        return "- (No files in evidence JSON yet.)"
    lines = []
    for entry in files[:20]:
        if not isinstance(entry, dict):
            continue
        path = entry.get("path", "?")
        why = entry.get("why_suspicious", "")
        status = entry.get("status", "documented")
        line = f"- `{path}` — status: {status}"
        if why:
            line += f"; {why}"
        lines.append(line)
    if len(files) > 20:
        lines.append(f"- … plus {len(files) - 20} more in evidence JSON")
    return "\n".join(lines)


def session_timeline(sessions: list) -> str:
    if not sessions:
        return "| — | — | — |"
    rows = []
    for sess in sessions[-8:]:
        if not isinstance(sess, dict):
            continue
        at = sess.get("at", "—")
        phase = sess.get("phase", "—")
        summary = (sess.get("summary") or "").replace("\n", " ")[:120]
        rows.append(f"| {at} | Phase {phase} | {summary or '—'} |")
    return "\n".join(rows) if rows else "| — | — | — |"


def build_summary(data: dict) -> str:
    inv = data.get("investigation", {})
    date_stamp = inv.get("started_at", "YYYY-MM-DD")
    situation = inv.get("situation_summary") or "[One paragraph — facts only, label uncertainty]"
    esc = data.get("escalation", {})
    criteria = esc.get("criteria_met") or []
    criteria_text = (
        "\n".join(f"- {c}" for c in criteria)
        if criteria
        else "- [None flagged in JSON yet — review When-to-Escalate criteria]"
    )

    artifacts = data.get("artifacts", {})
    artifact_lines = []
    for key in ("screenshots", "network_captures", "tool_exports"):
        items = artifacts.get(key, [])
        if items:
            artifact_lines.append(f"- **{key}:** {len(items)} item(s)")
    artifact_block = (
        "\n".join(artifact_lines) if artifact_lines else "- [List screenshots, captures, exports]"
    )

    return f"""# Summary for Professionals

**Date of this summary:** {date_stamp}  
**Generated:** {iso_now()} (auto-draft from evidence JSON — review and edit before sending)  
**Investigation ID:** {inv.get('id', 'Investigation')}

> Facts only · Label uncertainty · Not legal advice

---

## Situation (one paragraph)

{situation}

---

## Key findings

{bullet_files(data.get('files', []))}

---

## Timeline (recent LLM sessions)

| Time | Phase | Summary |
|------|-------|---------|
{session_timeline(data.get('sessions', []))}

---

## Evidence package contents

{artifact_block}

- `investigation_log_{date_stamp}.md`
- `suspicious_files_inventory_{date_stamp}.md`
- `evidence_{date_stamp}.json` (structured metadata)

---

## Escalation notes

**Recommended in JSON:** {esc.get('recommended', False)}

{criteria_text}

{esc.get('notes', '')}

---

## What I have already done

- [ ] Phase 0 documentation (screenshots, inventory, system time check)
- [ ] Scanning / inspection per framework
- [ ] Network capture (if applicable)
- [ ] Stopped sensitive use on suspect device (if applicable)

---

## Questions for professionals

- [Add your questions here]

---

*Template reference: Start-Guide/How-to-Prepare-a-Professional-Summary.md*
"""


def main() -> int:
    args = parse_args()
    evidence_path = args.evidence.expanduser().resolve()
    if not evidence_path.is_file():
        print(f"ERROR: evidence file not found: {evidence_path}", file=sys.stderr)
        return 1

    banner("Generate professional summary", evidence_path.name)
    data = load_evidence(evidence_path)
    inv = data.get("investigation", {})
    date_stamp = inv.get("started_at", "YYYY-MM-DD")

    out = args.output
    if out is None:
        out = evidence_path.parent / f"summary_for_professionals_{date_stamp}.md"
    else:
        out = out.expanduser().resolve()

    if out.exists() and not args.force:
        warn(f"{out.name} exists — use --force to overwrite.")
        return 1

    out.write_text(build_summary(data), encoding="utf-8")
    ok(f"Wrote {out}")
    info("Review and edit before sending to IR, LE, or consultants.")
    return 0


if __name__ == "__main__":
    sys.exit(main())