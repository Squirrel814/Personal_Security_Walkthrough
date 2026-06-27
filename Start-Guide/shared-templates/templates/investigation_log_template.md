# Investigation Log Template

**Framework Version Used:** [e.g., Windows Full Deep Dive v1.1 or macOS Minimal Tools v1.1]  
**Investigator:** [Your name or "Self"]  
**Device/OS:** [e.g., Windows 11, macOS Sonoma, Ubuntu 24.04]  
**Start Date:** [YYYY-MM-DD]  
**Overall Goal:** Investigate suspicious files (future timestamps, weird flags) and/or network activity while preserving evidence and staying calm.

---

## Instructions
- Append new entries chronologically. Do not delete or edit past entries.
- Always include date + time for every action.
- Reference screenshots, file paths, and tool outputs clearly.
- At the end of each LLM session, add a short **Session Summary** (see template at bottom).
- This log + your `suspicious_files_inventory.md` + network captures = your evidence package.

---

## Log Entries

### [YYYY-MM-DD HH:MM] — Phase 0: Initial Documentation & System Basics
**Action Taken:**  
- Took screenshots of suspicious file Properties / Get Info.  
- Checked and corrected system date/time.  

**Observations / Findings:**  
- System time was [correct / off by X hours]. Corrected at [time].  
- Suspicious files identified: [list paths or count].  

**Files / Screenshots Referenced:**  
- [e.g., `screenshot_file1_properties_2026-06-24.png`]  

**Decisions Made:**  
- Created this investigation log and `suspicious_files_inventory.md`.  

**Next Action:**  
- Proceed to Phase 1 scanning.

---

### [YYYY-MM-DD HH:MM] — Phase 1: Scanning & Detection
**Action Taken:**  
- Ran Microsoft Defender Offline scan / Malwarebytes / KnockKnock / ClamAV, etc.  
- Reviewed Autoruns / LaunchAgents / systemctl services.  

**Observations / Findings:**  
- [e.g., No threats found by Defender. Malwarebytes flagged 2 items (logged in inventory). Autoruns showed one unsigned entry in Startup.]  

**Files / Screenshots Referenced:**  
- [e.g., `malwarebytes_scan_results_2026-06-24.png`, `autoruns_export_2026-06-24.txt`]  

**Decisions Made:**  
- [e.g., Moved flagged items to inventory for deeper analysis. No immediate deletion.]  

**Next Action:**  
- Begin Phase 2 file forensics on flagged items.

---

### [YYYY-MM-DD HH:MM] — Phase 2: File Forensics & Timestamp Analysis
**Action Taken:**  
- Inspected file metadata using [Properties / Get Info / ExifTool / stat / mdls].  
- Ran PowerShell / Terminal timestamp hunt commands.  
- Opened scripts in text editor (read-only).  

**Observations / Findings:**  
- [e.g., File `example.exe` has future Created time of 2027-03-15. Multiple files show timestamp inconsistencies. Script contains base64 and download command.]  

**Files / Screenshots Referenced:**  
- [e.g., `exiftool_output_example.txt`, `future_timestamps.csv`]  

**Decisions Made:**  
- [e.g., Added 3 files to inventory. Will analyze script content with LLM.]  

**Next Action:**  
- Use LLM prompt on script content and suspicious metadata.

---

### [YYYY-MM-DD HH:MM] — Phase 3: Network Monitoring & Analysis
**Action Taken:**  
- Captured network traffic with Wireshark / tcpdump for X minutes.  
- Ran `netstat` / `ss` / `lsof -i` / TCPView commands.  
- Reviewed router device list.  

**Observations / Findings:**  
- [e.g., Wireshark capture saved as `capture_2026-06-24.pcapng`. Noted periodic small packets to IP 203.0.113.45 every ~60 seconds. No obvious scanning from `ss` output.]  

**Files / Screenshots Referenced:**  
- [e.g., `capture_2026-06-24.pcapng`, `ss_output_2026-06-24.txt`]  

**Decisions Made:**  
- [e.g., Will analyze capture with LLM using short prompt. No immediate action on router.]  

**Next Action:**  
- Analyze network capture with LLM.

---

### [YYYY-MM-DD HH:MM] — Phase 4: Synthesis & Decision
**Action Taken:**  
- Reviewed all findings from Phases 0–3 together.  
- [Optional] Drafted escalation summary.  

**Observations / Findings:**  
- [e.g., Multiple future-timestamp files + one script with suspicious download behavior + periodic network beaconing. Overall assessment: Likely targeted low-sophistication activity or scare tactic.]  

**Decisions Made:**  
- [e.g., Will continue light monitoring for 7 days. If new activity appears, escalate to professional. Strengthened baseline hygiene (updates + 2FA).]  

**Escalation Notes:**  
- [If escalating: Professional / law enforcement contact, what evidence package was prepared, date of escalation.]

**Next Action:**  
- Enter Phase 5 ongoing monitoring or close investigation.

---

### [YYYY-MM-DD HH:MM] — Phase 5: Ongoing Monitoring & Hygiene
**Action Taken:**  
- [e.g., Weekly light network check with `ss` / Wireshark. Re-ran Autoruns / KnockKnock.]  

**Observations / Findings:**  
- [e.g., No new suspicious activity in the last 7 days.]  

**Decisions Made:**  
- [e.g., Investigation considered low risk / closed for now. Will re-open if new symptoms appear.]  

---

## Session Summary (Add at End of Every LLM Session)

**Date:** [YYYY-MM-DD]  
**Session Focus:** [e.g., Phase 2 file analysis + LLM review of script]  
**Key Findings:**  
- [Bullet list of main discoveries this session]  

**Decisions Made:**  
- [What was decided]  

**Open Questions / Uncertainties:**  
- [List anything still unclear]  

**Recommended Next Action:**  
- [Single most important next step]  

**Framework Improvements Suggested:**  
- [Optional — any ideas to improve the templates or frameworks]

---

**End of Investigation Log Template**

**How to Use:**  
Copy this file into your investigation folder and rename it with today's date (e.g., `investigation_log_2026-06-24.md`). Append new dated sections as you work. This template is designed to work with any of the platform-specific Minimal or Full Deep Dive frameworks.