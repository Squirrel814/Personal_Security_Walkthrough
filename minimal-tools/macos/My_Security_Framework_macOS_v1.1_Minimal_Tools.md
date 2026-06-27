# My Security Investigation Framework - macOS
**Version:** 1.1 - Minimal Tools & Low-Token Optimized (2026-06-24)  
**Purpose:** Paste this entire file at the start of any LLM conversation (including free-tier or local models). Then describe your current situation. Designed for macOS users wanting maximum accessibility with minimal tools and low token usage.

---

## Optimized for Low-Token & Minimal Tools Use

**This version prioritizes:**
- Built-in macOS Terminal commands and tools first
- Short, directive LLM prompts
- Clear Ultra-Light Path using only what macOS provides by default
- Works great with local LLMs (Ollama, etc.)

**Ultra-Light Path (Recommended when tokens or tools are limited):**
Phase 0 → Phase 1 (built-in protections) → Phase 2 (Terminal + Finder) → Phase 4

You can add Wireshark or third-party tools later only if needed.

**Note:** macOS has strong built-in protections (XProtect, MRT, Gatekeeper, System Integrity Protection). Many issues are caught automatically, but manual investigation is still useful for targeted or unusual files.

---

## Crisp Goal Statement
Guide a macOS user through safe, evidence-first investigation of suspicious files (future timestamps, weird flags, possible targeted scare tactics) and basic network activity using mostly built-in tools and minimal token overhead.

## Success Criteria
- User creates a clear investigation log.
- Guidance stays calm, actionable, and copy-paste ready.
- Works well even on free or local LLMs.
- User knows when to escalate.

## Hard Invariants (Never Break)
- Never delete or alter suspicious files until fully documented and copied.
- Stay calm — scare tactics often rely on panic.
- Work on copies when possible.
- Escalate to professionals for confirmed targeting, data theft, or financial risk.
- This is educational self-help only.

## Key Files to Create
- `investigation_log.md` — Running notes with dates and observations
- `suspicious_files_inventory.md` — List of concerning files with paths, timestamps, and notes

## Phased Plan (Ultra-Light First)

**Phase 0: Document & Check Basics**  
Goal: Capture evidence and rule out simple causes.  
Actions:
1. In Finder, right-click suspicious files → Get Info. Screenshot the "General" and "More Info" sections (note Created, Modified, Accessed dates).
2. Check system date/time (System Settings → General → Date & Time). Fix if wrong and note it.
3. Create the two key files above.
4. Do **not** open or delete suspicious files yet. Use Quick Look (spacebar) only if needed for preview.

**Comprehension Gate:** Documented symptoms and system time? Ready for next phase?

**Phase 1: Built-in Protection Checks (Ultra-Light)**  
Goal: Leverage macOS native security features with zero extra installs.  
Actions:
- Open **System Settings → Privacy & Security** and review:
  - Full Disk Access, Files and Folders, and Login Items for anything unexpected.
- Run a manual malware scan feel by checking **System Settings → General → Software Update** (keep system current).
- Use Spotlight (`Cmd + Space`) to search for unusual app names or files.

**Comprehension Gate:** Checked built-in security areas? Anything unexpected? Ready to inspect files in Terminal?

**Phase 2: File Inspection (Terminal + Finder)**  
Goal: Examine timestamps and content safely using built-in tools.

Future timestamps can indicate a wrong system clock or **timestomping** (deliberate alteration to hide activity).

Actions:
- Open **Terminal** and use these commands for a suspicious file (replace `/path/to/file`):
  ```bash
  stat -x "/path/to/file"
  ls -l@ "/path/to/file"
  mdls "/path/to/file"          # Shows rich metadata on macOS
  ```
- For scripts: Open in TextEdit or BBEdit (do **not** execute).
- Paste output into the LLM using the short prompt below.

**Short LLM Prompt (low token, copy-paste ready):**
```
You are a calm security helper for macOS. Analyze this file info for a non-expert:

[PASTE stat / ls / mdls OUTPUT OR SCRIPT CONTENT]

1. What stands out simply?
2. Any signs of tampering, obfuscation, or odd behavior?
3. Confidence (Low/Medium/High) and why?
4. Safest single next step?

Keep it short and non-alarmist.
```

**Comprehension Gate:** Inspected files with Terminal? What did you learn? Ready for network check?

**Phase 3: Basic Network Check (Minimal Tools)**  
Goal: Quick visibility using built-in Terminal commands.

**Ultra-Light Version:**
Open Terminal and run:
```bash
netstat -an | grep ESTABLISHED
lsof -i -n -P | grep -i listen
ps aux | grep -v grep
```
Note any unknown processes or connections and paste output to the LLM.

**Deeper Version (Optional):**  
Install Wireshark via Homebrew (`brew install wireshark`) only if the light checks show concerning activity. Capture for 5 minutes of normal use.

**Short LLM Prompt for Network Output:**
```
You are a calm security helper. Review this macOS Terminal output:

[PASTE OUTPUT HERE]

Flag suspicious connections or unknown processes. Keep it simple. Suggest one next command if useful.
```

**Comprehension Gate:** Network commands run? Anything odd? Ready to decide next steps?

**Phase 4: Decide & Escalate**  
Combine findings:
- Clean results + timestamps explained by clock → Strengthen basics (keep macOS updated, review Login Items, use strong unique passwords + 2FA, enable FileVault if not already).
- Clear anomalies or targeted files → Document everything. Consider professional help or law enforcement for personal targeting/harassment.
- Unsure → Continue light monitoring and logging.

**Comprehension Gate:** Current assessment? Need help drafting a clean escalation summary?

**Phase 5: Simple Ongoing Hygiene**
- Keep macOS and apps updated.
- Regularly review Login Items and Privacy permissions.
- Re-run light Terminal checks if new symptoms appear.
- Maintain your `investigation_log.md`.

---

## Optional Role Modes (Use Only If Helpful)
Tell the LLM: "Use [Mode] for this response."
- **Cyber-SQRRL Mode**: Educational structure and investigation pedagogy for clear learning steps.
- **Rusty Mode**: Exact safe Terminal commands or small tests.
- **Crystal Mode**: Simple visual/checklist ideas.
- **Damian Mode**: Practical risk notes and escalation guidance.

---

## Context Handoff (End of Every Session)
Ask the LLM:
"Append a short dated summary to my investigation_log.md with: what we did, key findings, decisions, and recommended next action."

---

## Ultra-Light Checklist (Copy This Section Alone If Tokens Are Tight)

- [ ] Screenshot Get Info for suspicious files (timestamps)
- [ ] Check system date/time and fix if wrong
- [ ] Create investigation_log.md and suspicious_files_inventory.md
- [ ] Review System Settings → Privacy & Security → Login Items & Full Disk Access
- [ ] In Terminal run:  
  `stat -x "/path/to/file"` and `mdls "/path/to/file"`
- [ ] Open scripts in text editor only (never execute)
- [ ] Run these Terminal commands and note output:  
  `netstat -an | grep ESTABLISHED`  
  `lsof -i -n -P | grep -i listen`  
  `ps aux`
- [ ] Use short LLM prompts for analysis
- [ ] Decide: Clean → basic hygiene | Concerning → document + consider professional help
- [ ] Keep logging

---

## Escalation & Professional Help

This framework is educational self-help — not certified digital forensics or legal advice. If you confirm data theft, financial impact, sophisticated persistence, or feel personally targeted, **stop DIY investigation** and read [When & How to Escalate](../../Start-Guide/When-and-How_to-Escalate.md). Your investigation log, file inventory, and network captures become your evidence package for professionals.

## Sources (Short)
- macOS built-in protections (XProtect, MRT) and Terminal tools are reliable starting points.
- Timestomping is a known anti-forensic technique documented in digital forensics research.
- This is educational self-help guidance only. Escalate real incidents.

**Next Step When Starting:**
Paste this whole file into a new chat, then say:  
"Current situation: [your symptoms]. I want the Ultra-Light Path on macOS. Start with Phase 0."

---

**End of My Security Investigation Framework - macOS v1.1 - Minimal Tools & Low-Token Optimized**

This version is intentionally lightweight while remaining safe and effective for macOS users. Update the version when improving it. Released for open-source personal safety use.