#!/usr/bin/env python3
"""
Generate a paste-ready LLM session prompt from evidence JSON + framework context.

Usage:
    python tools/generate_llm_prompt.py --evidence ./Investigation_2026-06-27/evidence_2026-06-27.json

    python tools/generate_llm_prompt.py --evidence evidence.json --phase 0 \\
        --framework minimal-tools/windows/My_Security_Framework_Windows-OS_v1.1_Minimal_Tools.md \\
        --output ./Investigation_2026-06-27/llm_prompt_phase0.txt

The output file is meant to be pasted *after* the full OS framework in chat.
Exit code: 0 on success; 1 on error.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from evidence_lib import load_evidence
from psw_calm_ui import banner, info, ok

REPO_ROOT = Path(__file__).resolve().parent.parent

PHASE_INSTRUCTIONS = {
    0: (
        "Start Phase 0 (Documentation First). Guide me step by step with comprehension gates. "
        "I need help screenshotting file properties, verifying system time, and starting my log "
        "and inventory. Do not tell me to delete or execute suspicious files."
    ),
    1: (
        "Continue to Phase 1 (Scanning & Detection). Use the Ultra-Light path first. "
        "Explain each command before I run it. Summarize findings for my investigation log."
    ),
    2: (
        "Continue to Phase 2 (Inspect Files & Metadata). Read-only inspection only — "
        "never run scripts. Help me interpret metadata and update my inventory."
    ),
    4: (
        "Continue to Phase 4 (Network Check). Passive monitoring only on my home network. "
        "No aggressive scanning. Help me interpret captures safely."
    ),
    6: (
        "Help me with Phase 6 (Documentation Handoff). Review my evidence package and "
        "whether escalation criteria apply. Prepare a calm session summary for my log."
    ),
}

FRAMEWORK_PATHS = {
    "windows": REPO_ROOT
    / "minimal-tools/windows/My_Security_Framework_Windows-OS_v1.1_Minimal_Tools.md",
    "macos": REPO_ROOT / "minimal-tools/macos/My_Security_Framework_macOS_v1.1_Minimal_Tools.md",
    "linux": REPO_ROOT / "minimal-tools/linux/My_Security_Framework_Linux_v1.1_Minimal_Tools.md",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate paste-ready LLM prompt from evidence JSON.")
    parser.add_argument("--evidence", type=Path, required=True, help="evidence_YYYY-MM-DD.json")
    parser.add_argument("--phase", type=int, help="Override investigation phase (0–6)")
    parser.add_argument(
        "--framework",
        type=Path,
        help="Path to framework markdown (default: inferred from os.family)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Write prompt to file (default: llm_prompt_phaseN.txt beside evidence JSON)",
    )
    return parser.parse_args()


def build_prompt(data: dict, phase: int, framework_path: Path | None) -> str:
    inv = data["investigation"]
    os_info = inv.get("os", {})
    family = os_info.get("family", "unknown")
    situation = inv.get("situation_summary") or "(describe your situation in the evidence JSON)"
    phase_text = PHASE_INSTRUCTIONS.get(
        phase,
        f"Continue investigation at phase {phase}. Follow the framework with comprehension gates.",
    )

    files = data.get("files", [])
    file_lines = []
    for entry in files[:12]:
        if not isinstance(entry, dict):
            continue
        path = entry.get("path", "?")
        why = entry.get("why_suspicious", "")
        file_lines.append(f"- {path}" + (f" — {why}" if why else ""))
    if len(files) > 12:
        file_lines.append(f"- … plus {len(files) - 12} more (see evidence JSON)")

    fw_hint = ""
    if framework_path and framework_path.is_file():
        fw_hint = f"\n**Framework file to paste first (entire file):** `{framework_path}`\n"
    elif family in FRAMEWORK_PATHS and FRAMEWORK_PATHS[family].is_file():
        fw_hint = (
            f"\n**Framework file to paste first (entire file):** `{FRAMEWORK_PATHS[family]}`\n"
        )

    files_block = "\n".join(file_lines) if file_lines else "- (none logged yet — add via collect_file_metadata.py)"

    return f"""# LLM session prompt — Personal Security Walkthrough
**Generated for:** {inv.get('id', 'Investigation')}
**Phase:** {phase} ({inv.get('phase_name', 'documentation')})
**OS:** {family} {os_info.get('version', '')}
{fw_hint}
---

## How to use this prompt

1. Paste your **entire** OS framework file into the chat first.
2. Paste this prompt below it.
3. End the session with: **Append Session Summary to my log**

---

## My situation (facts only — label uncertainty)

{situation}

## Files documented so far

{files_block}

## What I need from you now

{phase_text}

**Hard rules:** Document first. Never delete suspicious files before documentation. Never execute unknown scripts. Calm tone. Escalate when criteria match When-to-Escalate guide.
"""


def main() -> int:
    args = parse_args()
    evidence_path = args.evidence.expanduser().resolve()
    if not evidence_path.is_file():
        print(f"ERROR: evidence file not found: {evidence_path}", file=sys.stderr)
        return 1

    banner("Generate LLM prompt", evidence_path.name)
    data = load_evidence(evidence_path)
    inv = data.get("investigation", {})
    phase = args.phase if args.phase is not None else int(inv.get("phase", 0))

    framework_path = args.framework.expanduser().resolve() if args.framework else None
    prompt = build_prompt(data, phase, framework_path)

    out = args.output
    if out is None:
        out = evidence_path.parent / f"llm_prompt_phase{phase}.txt"
    else:
        out = out.expanduser().resolve()

    out.write_text(prompt, encoding="utf-8")
    ok(f"Wrote {out}")
    info("Paste framework first, then this file, into your LLM chat.")
    return 0


if __name__ == "__main__":
    sys.exit(main())