# Tools — Personal Security Walkthrough

Small MIT-licensed helpers for maintainers and advanced readers. **Not required** to use the walkthrough.

| Tool | Purpose |
|------|---------|
| [scaffold_investigation_folder.py](scaffold_investigation_folder.py) | Create `Investigation_YYYY-MM-DD/` with templates and subfolders on your machine |
| [blocklist_export_template.txt](blocklist_export_template.txt) | Pi-hole / hosts file format for domains you documented in investigation |
| [validate_walkthrough_links.py](validate_walkthrough_links.py) | Check internal markdown and `web/index.html` links still resolve |

---

## scaffold_investigation_folder.py

Creates a dated investigation folder **outside** this git repo (defaults to current directory).

```bash
python tools/scaffold_investigation_folder.py --output-dir C:\Users\You\Documents
```

Preview without writing:

```bash
python tools/scaffold_investigation_folder.py --output-dir . --dry-run
```

Includes: dated log + inventory templates, screenshot/capture/tool subfolders, `START_HERE.md`, optional blocklist copy in `tool_exports/`.

**Requires:** Python 3.8+ (stdlib only).

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

Optional — flag legacy root `Infograph_*` references:

```bash
python tools/validate_walkthrough_links.py --strict
```

Exit code `1` if any relative link is broken (useful before releases or after moving files).

**Requires:** Python 3.8+ (stdlib only).

---

## CI (GitHub Actions)

On every **pull request** and **push** to `main`, `.github/workflows/validate-links.yml` runs the link validator. See below for what PRs mean.

---

## Not in scope (deferred)

- Quiz / flashcards (`curriculum/`) — optional v2 community layer
- Personal Security Command Center app — future local JSON dashboard (gem Section 10)
- `export_blocklist.py` — Pi-hole/hosts converter from filled domain list (see cons in tools README discussion)