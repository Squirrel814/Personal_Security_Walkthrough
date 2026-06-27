# How to Prepare a Professional Summary

**Personal Security Investigation Framework**  
Version 1.0 | Cross-Platform

This companion expands the short summary template in [When & How to Escalate](When-and-How_to-Escalate.md) into a **complete, reusable document** for incident response firms, IT consultants, law enforcement, or legal counsel. It is not legal advice.

---

## Purpose

Busy professionals need a **fast, factual overview** before reading your full investigation log. A good summary:

- Saves time in the first meeting or call
- Reduces miscommunication under stress
- Shows you preserved evidence deliberately
- Separates **observed facts** from **your interpretations**

---

## When to create this

Create or update the summary when:

- You decide to escalate per the [decision flowchart](When-and-How_to-Escalate.md#decision-flowchart)
- You contact [professional help](Choosing-the-Right-Professional-Help.md)
- You file a [law enforcement report](What-to-Expect-When-Working-with-Law-Enforcement.md)

**Filename suggestion:** `summary_for_professionals_YYYY-MM-DD.md` in your investigation folder.

---

## Full template (copy and fill in)

```markdown
# Summary for Professionals

**Date of summary:** YYYY-MM-DD  
**Prepared by:** [Your name or "Self"]  
**Contact (optional):** [Email or phone you are comfortable sharing]  
**Device(s) involved:** [e.g., Windows 11 laptop, home router model]

---

## 1. Situation in one paragraph (facts only)

[Example: Between 2026-06-18 and 2026-06-22 I found three files in Downloads with 
Created timestamps in 2027 and filenames containing my first name. I did not open 
or delete them. I completed documentation, offline scans, and light network checks. 
No unauthorized bank charges observed.]

---

## 2. Key findings (bullets — most important first)

- [e.g., Three files with future Created dates; paths listed in inventory]
- [e.g., Defender offline scan: clean; Malwarebytes: one Riskware flag — quarantined in log]
- [e.g., Wireshark 10-min capture: periodic small packets to IP x.x.x.x — confidence medium]
- [e.g., No system clock error; time verified correct]

---

## 3. Timeline (chronological, short)

| Date | Event |
|------|-------|
| YYYY-MM-DD | First noticed [symptom] |
| YYYY-MM-DD | Began investigation; created log + inventory |
| YYYY-MM-DD | Completed Phase 1 scans |
| YYYY-MM-DD | [Add rows as needed] |

---

## 4. Evidence package contents

| Item | Location / filename |
|------|-------------------|
| Investigation log | investigation_log_YYYY-MM-DD.md |
| File inventory | suspicious_files_inventory_YYYY-MM-DD.md |
| Screenshots | screenshots/ |
| Network captures | network_captures/ |
| Tool exports | tool_exports/ |
| Forensic image (if any) | [filename + SHA-256] |

---

## 5. What I have already done

- [ ] Documented file properties / metadata before changes
- [ ] Verified system date/time
- [ ] Ran [list scans/tools]
- [ ] Did **not** delete original suspicious files [or: quarantined per log entry DATE]
- [ ] Stopped using device for [banking / work / none yet]

---

## 6. What I have **not** done (optional but helpful)

- [e.g., No full disk forensic image — awaiting guidance]
- [e.g., No contact with suspected harasser]
- [e.g., No factory reset]

---

## 7. Current assessment (label confidence)

**Overall risk:** [Low / Medium / High / Unknown]  
**Confidence:** [Low / Medium / High]  
**One-sentence assessment:** [e.g., Likely low-sophistication scare tactic; possible targeted harassment; uncertain on network beaconing.]

---

## 8. Questions for you

1. [e.g., Is my evidence package sufficient to start, or do you need a full disk image?]
2. [e.g., Should I stop using this device entirely until you advise?]
3. [e.g., Should I file a police report given the targeted filenames?]

---

## 9. Supporting detail location

Full chronological notes: see **investigation_log_YYYY-MM-DD.md**  
File-level detail: see **suspicious_files_inventory_YYYY-MM-DD.md**

---

**End of summary**
```

---

## Writing tips

| Do | Don't |
|----|-------|
| Use dates and exact paths from your inventory | Guess attacker identity |
| Say "observed," "logged," "screenshot shows" | Claim court-admissible forensics |
| Note confidence (low/medium/high) | Use alarmist language |
| Keep to 1–2 pages when printed | Paste entire LLM chat logs |

---

## One-page ultra-short variant

For phone intake or email subject line follow-up:

```
Subject: Cyber incident summary — [Your name] — [DATE]

Devices: [list]
Top findings: [3 bullets max]
Evidence: log + inventory + [captures?] on USB / shared folder
Urgent ask: [one question]
Full summary: attached summary_for_professionals_YYYY-MM-DD.md
```

---

## LLM assist (optional)

Paste your filled investigation log and inventory into an LLM with:

```
You are a calm technical editor. Turn the following investigation notes into a 
professional summary using the sections in How-to-Prepare-a-Professional-Summary.md. 
Facts only; label uncertainty; keep under 2 pages. Do not invent findings.
```

Review every line before sending — **you** are responsible for accuracy.

---

## Related guides

- [When & How to Escalate](When-and-How_to-Escalate.md)
- [Choosing the Right Professional Help](Choosing-the-Right-Professional-Help.md)
- [What to Expect When Working with Law Enforcement](What-to-Expect-When-Working-with-Law-Enforcement.md)
- [Project Structure Recommendation](shared-templates/templates/project_structure_recommendation.md)

---

**End of How to Prepare a Professional Summary**