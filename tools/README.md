# Tools — Personal Security Walkthrough

Small MIT-licensed helpers for maintainers and advanced readers. **Not required** to use the walkthrough.

| Tool | Purpose |
|------|---------|
| [scaffold_investigation_folder.py](scaffold_investigation_folder.py) | Create `Investigation_YYYY-MM-DD/` with templates, subfolders, and `evidence_*.json` |
| [collect_file_metadata.py](collect_file_metadata.py) | Append read-only file metadata (timestamps, optional SHA-256) to evidence JSON |
| [validate_evidence_json.py](validate_evidence_json.py) | Validate evidence JSON against [evidence_schema.json](evidence_schema.json) |
| [generate_llm_prompt.py](generate_llm_prompt.py) | Build a paste-ready LLM session prompt from evidence JSON + phase |
| [generate_pro_summary.py](generate_pro_summary.py) | Auto-draft `summary_for_professionals_*.md` from evidence JSON |
| [psw_calm_ui.py](psw_calm_ui.py) | Shared calm terminal output (muted cyan/amber; used by other tools) |
| [evidence_lib.py](evidence_lib.py) | Shared evidence JSON helpers (stdlib validator) |
| [blocklist_export_template.txt](blocklist_export_template.txt) | Pi-hole / hosts file format for domains you documented in investigation |
| [validate_walkthrough_links.py](validate_walkthrough_links.py) | Check internal markdown and `web/index.html` links still resolve |

**Requires:** Python 3.8+ (stdlib only).

**AI editor:** [.cursor/rules/personal-security-investigation.mdc](../.cursor/rules/personal-security-investigation.mdc) aligns Cursor with framework guardrails when this repo is open.

---

## Evidence pipeline (JSON + Markdown)

Markdown logs remain the **human-readable authority**. Optional `evidence_YYYY-MM-DD.json` mirrors structured metadata for:

- Schema validation (fewer missed fields under stress)
- LLM ingest without copy-paste between files
- Auto-generated prompts and professional summary drafts

Schema: [evidence_schema.json](evidence_schema.json)

### Typical workflow

```bash
# 1. Scaffold folder on your machine (not inside this git repo)
python tools/scaffold_investigation_folder.py --output-dir C:\Users\You\Documents --os windows

# 2. Document suspicious files (read-only — never executes them)
python tools/collect_file_metadata.py ^
  --evidence C:\Users\You\Documents\Investigation_2026-06-27\evidence_2026-06-27.json ^
  --path "C:\Users\You\Downloads\suspicious.txt" ^
  --why "Future timestamp in filename"

# 3. Validate JSON
python tools/validate_evidence_json.py C:\Users\You\Documents\Investigation_2026-06-27\evidence_2026-06-27.json

# 4. Generate paste-ready LLM prompt (paste OS framework first, then this file)
python tools/generate_llm_prompt.py --evidence C:\Users\You\Documents\Investigation_2026-06-27\evidence_2026-06-27.json --phase 0

# 5. Draft professional summary when escalating
python tools/generate_pro_summary.py --evidence C:\Users\You\Documents\Investigation_2026-06-27\evidence_2026-06-27.json
```

Edit `situation_summary` in the JSON (or via your editor) before generating prompts or summaries.

---

## scaffold_investigation_folder.py

Creates a dated investigation folder **outside** this git repo (defaults to current directory).

```bash
python tools/scaffold_investigation_folder.py --output-dir C:\Users\You\Documents --os windows
```

Preview without writing:

```bash
python tools/scaffold_investigation_folder.py --output-dir . --dry-run
```

Includes: dated log + inventory templates, `evidence_YYYY-MM-DD.json`, screenshot/capture/tool subfolders, `START_HERE.md`, optional blocklist copy in `tool_exports/`.

---

## Calm terminal UI

Scripts use [psw_calm_ui.py](psw_calm_ui.py) for structured, muted output when stdout is a TTY. Plain text on pipes and logs. No alarm red — psychological anchor, not gamification.

---

## blocklist_export_template.txt

Copy to your investigation folder, add domains from your log, apply on **your** router or Pi-hole only.

See [defense/Block-and-Harden.md](../defense/Block-and-Harden.md) — block malware/phishing domains, not platforms or people’s sites.

---

## validate_walkthrough_links.py

From repo root:

```bash
python tools/validate_walkthrough_links.py
```

Exit code `1` if any relative link is broken (useful before releases or after moving files).

---

## CI (GitHub Actions)

On every **pull request** and **push** to `main`, `.github/workflows/validate-links.yml` runs the link validator.

---

## Deferred

- Quiz / flashcards (`curriculum/`) — optional v2 community layer
- Personal Security Command Center app — future local JSON dashboard
- `export_blocklist.py` — Pi-hole/hosts converter from filled domain list
- Full retro TUI skin — optional Phase 2 polish on `psw_calm_ui.py`