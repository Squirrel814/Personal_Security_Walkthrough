# Project Structure Recommendation

**Personal Security Investigation Framework**  
Version 1.0 | Recommended local folder layout

Use this layout when you start a new investigation. Copy templates from this repo into a **dated folder on your machine** — not inside the GitHub repo itself.

---

## Why structure matters

A consistent folder layout helps you:

- Find evidence quickly when stress is high
- Hand off a complete package to professionals
- Resume an LLM session without losing context
- Avoid accidentally mixing old and new incidents

<p align="center">
  <img src="../../../Infographs/Your-Evidence-Package.jpg" width="520" alt="Evidence package folder with investigation log, suspicious files inventory, screenshots, network captures, and summary for professionals.">
</p>

*Infograph — [full gallery](../../../Infographs/README.md)*

---

## Recommended folder tree

```
Investigation_YYYY-MM-DD/                    ← root — use today's date
├── investigation_log_YYYY-MM-DD.md        ← from investigation_log_template.md
├── suspicious_files_inventory_YYYY-MM-DD.md ← from suspicious_files_inventory_template.md
├── summary_for_professionals_YYYY-MM-DD.md  ← optional; create when escalating
│
├── screenshots/
│   ├── file_properties/                   ← Properties / Get Info captures
│   ├── scan_results/                      ← Defender, Malwarebytes, ClamAV, etc.
│   └── network_router/                    ← router admin, device lists (redact passwords)
│
├── network_captures/
│   └── capture_YYYY-MM-DD_HHMM.pcapng     ← Wireshark / tcpdump files
│
├── tool_exports/
│   ├── autoruns_export.txt                ← Windows Autoruns save
│   ├── knockknock_export.txt              ← macOS KnockKnock
│   └── future_timestamps.csv              ← PowerShell / find hunt output
│
├── scripts_reviewed/                      ← copies of suspicious scripts (read-only)
│   └── suspicious_script_copy.txt         ← never execute from this folder
│
└── framework_session/                     ← optional convenience copies
    ├── framework_used.md                  ← Minimal or Full Deep Dive file you pasted
    └── llm_session_notes.md               ← pasted Session Summaries if you prefer one file
```

---

## Naming conventions

| Item | Pattern | Example |
|------|---------|---------|
| Root folder | `Investigation_YYYY-MM-DD` | `Investigation_2026-06-27` |
| Log files | `investigation_log_YYYY-MM-DD.md` | `investigation_log_2026-06-27.md` |
| Inventory | `suspicious_files_inventory_YYYY-MM-DD.md` | `suspicious_files_inventory_2026-06-27.md` |
| Screenshots | `topic_YYYY-MM-DD.png` | `file_properties_downloads_2026-06-27.png` |
| Captures | `capture_YYYY-MM-DD_HHMM.pcapng` | `capture_2026-06-27_1430.pcapng` |

Use **one investigation folder per incident**. If a new concern appears weeks later, start a new dated root folder and reference the old one in your log if relevant.

---

## What to copy from this repo (first session)

From `Personal_Security_Walkthrough` on GitHub:

1. One **framework** file for your OS (`minimal-tools/{windows,macos,linux}/` recommended for first time)
2. [`investigation_log_template.md`](investigation_log_template.md)
3. [`suspicious_files_inventory_template.md`](suspicious_files_inventory_template.md)

Rename the two templates with today's date when you copy them into your `Investigation_YYYY-MM-DD/` folder.

---

## Evidence package checklist (for escalation)

When preparing to contact a professional, confirm you have:

- [ ] `investigation_log_YYYY-MM-DD.md` (up to date)
- [ ] `suspicious_files_inventory_YYYY-MM-DD.md` (up to date)
- [ ] `screenshots/` with file properties and scan results
- [ ] `network_captures/` if you captured traffic
- [ ] `tool_exports/` if you ran Autoruns, KnockKnock, or similar
- [ ] Optional: `summary_for_professionals_YYYY-MM-DD.md` (see [When & How to Escalate](../../When-and-How_to-Escalate.md))

Zip the entire `Investigation_YYYY-MM-DD/` folder or copy to external media if a professional requests it. **Do not delete originals** on the affected system unless instructed.

---

## What not to put in this folder

- Executed malware or unknown binaries you have not documented
- Unredacted passwords, full credit card numbers, or unrelated personal files
- Grok-Agents / internal development notes (keep friend-facing investigation content only)

---

## Related guides

- [Quick Start Guide](../../Quick-Start-Guide.md) — first session walkthrough
- [When & How to Escalate](../../When-and-How_to-Escalate.md) — decision flowchart and handoff prep
- [Choosing the Right Professional Help](../../Choosing-the-Right-Professional-Help.md) — who to contact
- [How to Prepare a Professional Summary](../../How-to-Prepare-a-Professional-Summary.md) — escalation handoff doc

---

**End of Project Structure Recommendation**

Copy this file into your templates reference folder or print the tree once when setting up your first investigation.