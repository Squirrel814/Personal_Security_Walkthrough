# Suspicious Files Inventory Template

**Investigation Log Reference:** [Link or filename of your investigation_log.md]  
**Date Created:** [YYYY-MM-DD]  
**Last Updated:** [YYYY-MM-DD]  
**Device/OS:** [e.g., Windows 11 / macOS Sonoma / Ubuntu 24.04]

---

## Instructions
- Add every file you consider suspicious or worth tracking.
- Fill in as much metadata as possible (timestamps are critical).
- Update the "Status / Actions Taken" and "Findings / Notes" columns as you investigate.
- Do **not** delete files from this inventory even if later cleared — keep historical record.
- This inventory + your investigation log + network captures = your core evidence package.
- Works with all platform frameworks (Windows, macOS, Linux — Minimal or Full Deep Dive).

---

## File Inventory

| # | Full Path / Filename | Created | Modified | Accessed | Size | Hash (SHA256 optional) | Why Suspicious | Status / Actions Taken | Findings / Notes |
|---|----------------------|---------|----------|----------|------|------------------------|----------------|------------------------|------------------|
| 1 | `/Users/name/Downloads/suspicious.exe` (Windows example)<br>or<br>`~/Downloads/suspicious` (macOS/Linux) | 2027-03-15 14:22 | 2026-06-20 09:15 | 2026-06-24 03:41 | 2.4 MB | `a1b2c3d4...` | Future Created timestamp + targets user by name in filename | Screenshot taken. Properties inspected. Added to inventory. Not executed. | Timestomping suspected. Script contains base64 + download command. LLM analysis flagged high risk. |
| 2 | `C:\Users\name\AppData\Roaming\bad.dll` | 2026-06-10 22:05 | 2026-06-10 22:05 | 2026-06-24 04:12 | 856 KB | | Appeared after suspicious download + unknown publisher | Autoruns flagged as new startup item. Process Explorer used to inspect. | Unsigned. Loaded by unknown process. Will monitor. |
| 3 | `~/Library/LaunchAgents/com.user.update.plist` (macOS) | 2026-05-01 08:00 | 2026-06-22 11:30 | — | 4 KB | | New LaunchAgent with future Modified time | KnockKnock review + `launchctl list`. ExifTool run. | Contains encoded URL. Documented; do not remove unless directed by a professional. |
| 4 | `/etc/systemd/system/malicious.service` (Linux) | 2026-06-15 03:00 | 2026-06-23 19:45 | — | 1.2 KB | | New systemd service with odd name and future timestamp | `systemctl status` + `journalctl` review. `stat` + `getfattr` run. | Service runs a script that beacons every 60s. Escalation candidate. |

**Add new rows above this line as needed.**

---

## Summary Statistics

- **Total Files in Inventory:** [Number]
- **Files with Future / Anomalous Timestamps:** [Number]
- **Files Flagged by Scanners (Defender / Malwarebytes / ClamAV / etc.):** [Number]
- **Files with Persistence Mechanisms:** [Number]
- **Files Analyzed with LLM:** [Number]
- **Overall Risk Assessment:** [Low / Medium / High / Unknown] — Brief reason: [e.g., Multiple timestomped files + one script with clear malicious behavior + network beaconing]

---

## Notes & Observations

- [Any general patterns noticed across files, e.g., "All suspicious files appeared in Downloads and AppData after one specific date."]
- [Any tools that were particularly helpful on this platform.]
- [Questions still open or items needing deeper analysis.]

---

## Escalation / Hand-off Notes

If escalating to a professional or law enforcement:

- Date of escalation: [YYYY-MM-DD]
- Who was contacted: [Organization / person]
- Evidence package provided: [This inventory + investigation_log.md + network_captures/ folder + screenshots]
- Summary of key concerns provided to them: [Short paragraph]

---

**End of Suspicious Files Inventory Template**

**How to Use:**  
Copy this file into your investigation folder and rename it with today's date (e.g., `suspicious_files_inventory_2026-06-24.md`). Fill in rows as you discover files. Update the Status and Findings columns as you investigate. This template is designed to work alongside any of the platform-specific Minimal or Full Deep Dive frameworks and the `investigation_log_template.md`. 

Keep both templates in a consistent location (e.g., a `templates/` or root investigation folder) so you can copy fresh versions for new incidents.