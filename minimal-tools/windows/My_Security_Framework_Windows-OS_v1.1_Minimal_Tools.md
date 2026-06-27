# My Security Investigation Framework
**Version:** 1.1 - Minimal Tools & Low-Token Optimized (2026-06-24)  
**Purpose:** Paste this entire file at the start of any LLM conversation (including free-tier or local models like Ollama). Then describe your current situation. Designed for maximum accessibility, minimal token usage, and the fewest possible external tools while keeping users safe and evidence-focused.

---

## Optimized for Low-Token & Minimal Tools Use (Start Here)

**This version prioritizes:**
- Built-in Windows tools first (no extra installs where possible)
- Short, directive LLM prompts (lower token count when pasted)
- Clear "Ultra-Light Path" that works with almost any LLM
- Optional deeper tools clearly marked

**Ultra-Light Path (Recommended if tokens or tools are limited):**
Phase 0 → Phase 1 (Defender only) → Phase 2 (built-in only) → Phase 4

You can skip Wireshark and extra scanners initially. Add them only if needed after the light path.

**Local / Free LLM Note:** This framework works excellently with local models (Ollama + phi3, gemma2, qwen2.5, or mistral). No premium subscription required.

---

## Crisp Goal Statement
Guide a non-expert through safe, evidence-first investigation of suspicious files (future timestamps, weird flags, possible targeted scare tactics) and basic home network checks. Use LLM help for analysis while building simple, reusable skills. Stay calm, document everything, and know when to escalate.

## Success Criteria
- User produces a clear investigation log with documented findings.
- LLM gives calm, actionable, copy-paste-ready guidance.
- User knows when to stop and get professional help.
- Works on free-tier or local LLMs with low token overhead.

## Current Status Snapshot
- **Phase:** Initial concern
- **Symptoms:** Files targeting user, future timestamps, weird flags. Possible scare tactic.
- **Immediate needs:** Documentation + rule out simple causes first.

## Hard Invariants (Never Break)
- Never delete or alter suspicious files until documented and copied.
- Stay calm — fear is often the goal of scare tactics.
- Work on copies when possible.
- Escalate to professionals if personal data, money, or ongoing targeting is involved.
- This is educational self-help only — not professional forensics or legal advice.

## Key Files to Create Locally (Minimal)
- `investigation_log.md` — Your running notes + dates + screenshots
- `suspicious_files_inventory.md` — List of concerning files with paths and observations

## Phased Plan (Ultra-Light First)

**Phase 0: Document & Check Basics**  
Goal: Capture evidence and rule out clock issues.  
Actions:
1. Screenshot Properties of every suspicious file (timestamps, location, size).
2. Check system date/time. Fix if wrong and note the change.
3. Create the two key files above.
4. Do **not** delete or open the files yet.

**Comprehension Gate:** Documented symptoms and system time? Ready for scanning?

**Phase 1: Quick Built-in Scan (Ultra-Light)**  
Goal: Get a fast second opinion with zero extra installs.  
Actions:
- Run full Microsoft Defender Offline scan (Windows Security → Virus & threat protection → Scan options).
- Optionally install Malwarebytes Free for a second opinion (still very lightweight).

**Comprehension Gate:** Scans done? Any obvious flags? Ready to check file details?

**Phase 2: File Inspection (Built-in Tools Only)**  
Goal: Examine timestamps and content safely.  
Future timestamps often mean either a wrong system clock or **timestomping** (malware trying to hide when files were created/modified).

Actions:
- Right-click suspicious files → Properties → Details tab. Compare dates.
- For scripts: Open in Notepad or Notepad++ (do **not** run them).
- Paste file properties or script content into the LLM using the short prompt below.

**Short LLM Prompt (copy-paste, low token):**
```
You are a calm security helper. Analyze this file info or script for a non-expert:

[PASTE FILE PROPERTIES OR SCRIPT CONTENT HERE]

1. What stands out simply?
2. Any signs of tampering, weird behavior, or obfuscation?
3. Confidence (Low/Medium/High) and why?
4. Safest single next step?

Keep it short and non-alarmist.
```

**Comprehension Gate:** Inspected files? What did you learn? Ready for network check?

**Phase 3: Basic Network Check (Minimal Tools)**  
Goal: Quick visibility without heavy tools.

**Ultra-Light Version (Built-in commands):**
Open Command Prompt or PowerShell and run:
```
netstat -ano | findstr ESTABLISHED
arp -a
tasklist /svc
```
Look for unknown programs or connections. Note anything suspicious and ask the LLM to review the output.

**Deeper Version (Optional):**  
Use Wireshark only if the light path shows concerning traffic. Capture 5 minutes of normal activity, then use the short prompt below.

**Short LLM Prompt for Network Output:**
```
You are a calm security helper. Review this network/command output for a beginner:

[PASTE OUTPUT HERE]

Flag any suspicious connections, unknown programs, or odd behavior. 
Keep explanation simple. Suggest one next filter or action if needed.
```

**Comprehension Gate:** Network check done? Anything odd? Ready to decide next steps?

**Phase 4: Decide & Escalate**  
Combine what you found:

- Everything clean + timestamps explained by clock → Strengthen basics (updates, strong unique passwords, 2FA).
- Clear anomalies or targeted files → Document thoroughly in your log. Consider professional help or law enforcement if this feels like targeted harassment.
- Unsure → Keep logging and repeat light checks weekly.

**Comprehension Gate:** What is your assessment? Need help writing a clean summary for escalation?

**Phase 5: Simple Ongoing Hygiene**
- Keep Defender real-time protection on.
- Update Windows and apps regularly.
- Re-check suspicious files or run light network commands if new symptoms appear.
- Maintain your `investigation_log.md`.

---

## Optional Role Modes (Use Only If Helpful)
Tell the LLM: "Use [Mode] for this response."

- **Cyber-SQRRL Mode**: Clear educational structure and investigation pedagogy for learning steps.
- **Rusty Mode**: Exact safe commands or small tests.
- **Crystal Mode**: Simple visual or checklist ideas.
- **Damian Mode**: Practical risk notes and when to stop DIY.

(These are optional — the core phases work without them.)

## Context Handoff (End of Every Session)
Ask the LLM:
"Append a short dated summary to my investigation_log.md with: what we did, key findings, decisions, and recommended next action."

## Ultra-Light Checklist (Copy This Section Alone If Tokens Are Very Tight)

- [ ] Screenshot suspicious file Properties
- [ ] Check & fix system time if wrong
- [ ] Create investigation_log.md
- [ ] Run Microsoft Defender Offline scan
- [ ] Check file Properties & compare timestamps
- [ ] Open scripts in text editor only (never run)
- [ ] Run these 3 commands and note output:  
  `netstat -ano | findstr ESTABLISHED`  
  `arp -a`  
  `tasklist /svc`
- [ ] Use short LLM prompts above for analysis
- [ ] Decide: Clean → basic hygiene | Concerning → document + consider help
- [ ] Keep logging

---

## Escalation & Professional Help

This framework is educational self-help — not certified digital forensics or legal advice. If you confirm data theft, financial impact, sophisticated persistence, or feel personally targeted, **stop DIY investigation** and read [When & How to Escalate](../../Start-Guide/When-and-How_to-Escalate.md). Your investigation log, file inventory, and network captures become your evidence package for professionals.

## Sources (Short)
- Timestomping is a documented anti-forensic technique (incident response reports and forensic research).
- Built-in Windows tools and Defender are reliable first-line options.
- This is educational guidance only. Escalate real incidents to professionals.

**Next Step When Starting:**
Paste this whole file into a new chat, then say:  
"Current situation: [your symptoms]. I want the Ultra-Light Path. Start with Phase 0."

---

**End of My Security Investigation Framework v1.1 - Minimal Tools & Low-Token Optimized**

This version is intentionally shorter and tool-light while preserving safety, evidence focus, and effectiveness. It is released for open-source personal safety use. Update the version number when you improve it.