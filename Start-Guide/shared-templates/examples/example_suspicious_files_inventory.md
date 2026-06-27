# Suspicious Files Inventory - EXAMPLE (Redacted)

**Investigation Log Reference:** `investigation_log_2026-06-20.md`  
**Date Created:** 2026-06-20  
**Last Updated:** 2026-06-21  
**Device/OS:** Windows 11 Home

---

## File Inventory

| # | Full Path / Filename                          | Created          | Modified         | Accessed         | Size    | Why Suspicious                              | Status / Actions Taken                          | Findings / Notes |
|---|-----------------------------------------------|------------------|------------------|------------------|---------|---------------------------------------------|--------------------------------------------------|------------------|
| 1 | `C:\Users\Alex\Downloads\update_helper.exe`   | 2027-03-15 14:22 | 2026-06-18 23:45 | 2026-06-20 14:10 | 2.4 MB  | Future Created timestamp + flagged by Malwarebytes as Riskware | Screenshot taken. Properties inspected. Not executed. Added to inventory. | Contains base64 + download command. LLM analysis flagged as suspicious. Monitoring. |
| 2 | `C:\Users\Alex\Downloads\Project_Plan.docx`   | 2027-03-15 14:25 | 2026-06-19 09:05 | 2026-06-20 14:12 | 187 KB  | Future Created timestamp + filename contains personal name | Screenshot taken. Opened in Word (read-only preview). No macros found. | Appears to be a decoy document. Low activity. |
| 3 | `C:\Users\Alex\Downloads\Invoice_June.pdf`    | 2027-03-15 14:28 | 2026-06-19 09:07 | 2026-06-20 14:15 | 412 KB  | Future Created timestamp + unusual filename pattern | Screenshot taken. Inspected metadata. | Standard PDF. No obvious malicious content. Likely decoy. |
| 4 | `C:\Users\Alex\AppData\Roaming\config.dat`    | 2026-06-10 03:15 | 2026-06-19 22:40 | 2026-06-21 08:30 | 856 KB  | New file in AppData after suspicious download + unknown origin | Found via Autoruns. Process Explorer used to inspect. | Obfuscated strings inside. No clear C2 yet. Will continue monitoring. |

---

## Summary Statistics

- **Total Files in Inventory:** 4
- **Files with Future / Anomalous Timestamps:** 3
- **Files Flagged by Scanners:** 1 (Malwarebytes)
- **Files with Persistence Mechanisms:** 0 confirmed
- **Files Analyzed with LLM:** 1
- **Overall Risk Assessment:** Low-to-Medium — Multiple future-timestamp files + one script with download behavior, but no confirmed data theft or active beaconing observed so far.

---

## Notes & Observations

- All three future-timestamp files appeared within a short window after one suspicious download.
- The flagged executable contains a download cradle. It has not been executed.
- No new files with future timestamps have appeared in the last 24 hours.
- Will re-scan with Malwarebytes and review Autoruns again in 7 days.

---

## Escalation / Hand-off Notes

**Not escalated at this time.**  
Current plan is to continue light monitoring for 7–10 days. Will escalate if:
- New files with future timestamps continue to appear, or
- Network beaconing is detected, or
- The flagged file shows signs of execution/persistence.

---

**End of Example Suspicious Files Inventory**

*Note: This is a fictional but realistic example created for educational purposes only. All names, paths, timestamps, and technical details have been redacted or fabricated to demonstrate proper documentation practices.*