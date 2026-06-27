# My Security Investigation Framework - Windows (Full Deep Dive)
**Version:** 1.1 - Full Deep Dive (2026-06-24)  
**Purpose:** Paste this entire file at the start of any LLM conversation. This is the comprehensive Windows version with deeper tool recommendations, richer analysis steps, and more advanced (but still educational) techniques while maintaining safety, evidence preservation, and accessibility.

---

## Full Deep Dive vs Minimal Tools Path

This version includes both paths:

- **Ultra-Light Path** (same as Minimal Tools v1.1) — for when you want speed and minimal installs.
- **Full Deep Dive Path** — recommended when you want thorough visibility. Uses more powerful free tools (Sysinternals, full Wireshark, etc.) and provides richer analysis guidance.

You can start with Ultra-Light and escalate to Deep Dive at any point.

**Local LLM friendly:** Works well with Ollama + capable models, though some sections benefit from stronger models for complex log analysis.

---

## Crisp Goal Statement
Provide a comprehensive, evidence-first investigation framework for Windows users facing suspicious files (future timestamps, weird flags, targeted scare tactics) and potential network anomalies. Combine built-in tools with powerful free utilities for deeper visibility while keeping everything educational, calm, and escalation-aware.

## Success Criteria
- User can follow either the light or deep path and produce high-quality documentation.
- LLM delivers structured, copy-paste-ready guidance with clear rationale.
- User understands when findings warrant professional incident response.
- Framework remains reusable across sessions and different LLMs.

## Hard Invariants (Never Break)
- Evidence preservation is non-negotiable — document before any changes.
- Never execute unknown files or scripts.
- Stay calm and methodical — panic destroys evidence and plays into scare tactics.
- Escalate immediately for confirmed data theft, financial impact, or ongoing personal targeting.
- This is educational self-help, not a substitute for certified digital forensics or legal advice.

## Key Files to Create
- `investigation_log.md` — Master running log with timestamps, screenshots, decisions, and LLM outputs.
- `suspicious_files_inventory.md` — Detailed list of concerning files (path, timestamps, hashes, observations).
- `network_captures/` — Folder for .pcapng files with date-prefixed names.
- `tools/` (optional) — Place downloaded free tools here (Sysinternals, etc.).

## Phased Plan

### Phase 0: Immediate Safety, Documentation & System Basics (Both Paths)
**Goal:** Lock evidence and rule out simple causes.  
**Actions (required for both paths):**
1. Take clear screenshots of every suspicious file’s Properties (General + Details tabs) — especially Created, Modified, Accessed timestamps.
2. Check and correct system date/time if wrong. Note the before/after values.
3. Create the key files listed above.
4. Do **not** delete, move, rename, or open suspicious files yet.

**Comprehension Gate:** Have you fully documented the initial state and verified system time? Ready to proceed?

### Phase 1: Multi-Layered Scanning (Deep Dive Path)
**Goal:** Thorough detection using reputable free tools.  
**Recommended tools (install in this order):**
- Microsoft Defender Offline scan (built-in, run first).
- Malwarebytes Free (excellent second opinion).
- ESET Online Scanner or HitmanPro (free, cloud-assisted, very low false positives).
- Autoruns (Sysinternals) — for deep persistence hunting (startup items, scheduled tasks, services, drivers, etc.).
- Process Explorer + TCPView (Sysinternals) — for running processes and network connections with more detail than Task Manager.

**Actions:**
1. Run full offline Defender scan.
2. Install and scan with Malwarebytes.
3. Use Autoruns (run as Administrator) → Look for unsigned or suspicious entries. Save the results (File → Save).
4. Use Process Explorer to inspect suspicious processes (right-click → Properties → Verify signature, check strings, etc.).
5. Use TCPView to see real-time network connections.

**Comprehension Gate:** All scans and Autoruns review complete? Any red flags logged in your inventory? Ready for file forensics?

### Phase 2: Advanced File Forensics & Timestamp Analysis (Deep Dive Path)
**Goal:** Deep inspection of suspicious files and timeline anomalies.

Future timestamps are a classic sign of **timestomping** (anti-forensic technique where malware alters MAC times). On NTFS, more reliable artifacts exist in the $MFT, $USNjrnl, and Prefetch files.

**Actions:**
- Basic (always): Right-click → Properties → Details.
- Deeper:
  - Download **ExifTool** (free) for rich metadata on many file types.
  - For scripts: Open in Notepad++ or VS Code. Look for obfuscation, base64, download cradles, persistence commands.
  - PowerShell timestamp hunting (example — run in Administrator PowerShell):
    ```powershell
    Get-ChildItem -Path C:\Users -Recurse -Force -ErrorAction SilentlyContinue |
      Where-Object { $_.CreationTime -gt (Get-Date).AddDays(30) -or $_.LastWriteTime -gt (Get-Date).AddDays(30) } |
      Select-Object FullName, CreationTime, LastWriteTime, LastAccessTime |
      Export-Csv "$env:USERPROFILE\Desktop\future_timestamps.csv" -NoTypeInformation
    ```
  - For deeper NTFS analysis (advanced): Consider tools like MFTECmd (from Eric Zimmerman’s suite) or KAPE for targeted collection — only after basic investigation and if you are comfortable or escalating.

**Short but powerful LLM Prompt (copy-paste):**
```
You are an experienced but calm digital forensics mentor helping a non-expert on Windows.

Context: Investigating files with future timestamps and possible targeted anomalies.

Analyze the following output or file content:

[PASTE PROPERTIES, EXIFTOOL OUTPUT, SCRIPT CONTENT, OR POWERSHELL RESULTS]

Tasks:
1. Summarize findings in plain language.
2. Flag indicators of timestomping, obfuscation, persistence, C2, or data exfil.
3. Assess confidence (Low/Medium/High) with reasoning.
4. Recommend the single most important next safe action.

Output in clear bullet points + one-sentence "Bottom line for the user".
```

**Comprehension Gate:** Have you performed deeper file analysis? What did you discover? Ready for network deep dive?

### Phase 3: Comprehensive Network Monitoring & Analysis (Deep Dive Path)
**Goal:** Establish strong visibility into network behavior.

**Core Tool: Wireshark (Full Guidance)**
1. Download Wireshark + Npcap from the official site.
2. Capture on your primary interface (usually Wi-Fi or Ethernet) for 10–15 minutes of mixed activity (normal use + idle).
3. Save as dated `.pcapng` in your `network_captures/` folder.
4. Useful display filters to start with:
   - `dns` — Look for suspicious or DGA-like domains.
   - `http` or `http2` — Unexpected POSTs or downloads.
   - `tcp.flags.syn == 1 && tcp.flags.ack == 0` — SYN scans.
   - `ip.addr == x.x.x.x` — Focus on one host.
   - `frame contains "beacon"` or common C2 strings (advanced).
   - Beaconing pattern: Look for regular small packets to the same external IP at consistent intervals.

**Complementary free tools:**
- Sysinternals TCPView (real-time connections with process mapping).
- GlassWire (free tier) for visual network monitoring and historical data.
- Simple command line: `netstat -ano`, `Get-NetTCPConnection` (PowerShell).

**LLM Prompt for Wireshark / tshark output:**
```
You are a calm, methodical network forensics analyst helping a beginner.

I have Wireshark or command-line network output from my Windows machine. Here is the relevant data:

[PASTE FILTERED PACKETS, TSHARK OUTPUT, OR TCPVIEW LOG]

Analyze for:
- C2 / beaconing behavior
- Data exfiltration
- Scanning or lateral movement
- DNS tunneling or suspicious domains
- ARP poisoning or unusual protocols

Explain findings simply but with technical accuracy. List any suspicious IPs/domains with confidence level. Suggest the next best filter or action.
```

**Comprehension Gate:** Network capture(s) analyzed? Any concerning traffic identified? Ready to synthesize findings?

### Phase 4: Synthesis, Decision Making & Escalation (Both Paths)
**Goal:** Combine all findings into a clear picture and decide on next actions.

**Possible outcomes & recommended responses:**
- Mostly clean + timestamps explained by clock error → Strengthen baseline hygiene (updates, unique passwords + password manager, 2FA everywhere, Windows Security features enabled, consider Sysinternals Autoruns in monitoring mode).
- Confirmed anomalies, persistence, or targeted files → Stop active use of the machine if possible. Create a full backup/image if comfortable (or take the machine to a professional). Document everything meticulously — this package (logs + captures + inventory) becomes very valuable.
- High uncertainty or signs of sophisticated activity → Strongly consider professional incident response. Do not continue deep DIY investigation alone.

**Comprehension Gate:** What is your overall assessment? Do you need help drafting a professional summary for escalation or law enforcement?

### Phase 5: Ongoing Monitoring & Hardening (Deep Dive Path)
- Schedule periodic Wireshark captures or use GlassWire / Sysinternals tools for ongoing visibility.
- Use Autoruns regularly (or configure it to highlight new items).
- Consider enabling more Windows logging (Event Viewer → Windows Logs → Security) and reviewing with tools like Event Log Explorer or PowerShell.
- Maintain excellent patch hygiene and application allow-listing where practical.

---

## Optional Role Emulation (Advanced)
You can instruct the LLM: "Switch to [Role] mode for this turn."

- **Cyber-SQRRL Mode**: Theoretically sound educational structure, investigation pedagogy, learning progressions, and clear explanations suitable for teaching or curriculum use.
- **Rusty Mode**: Precise, safe lab-style commands, small experiments, and implementation details (e.g., exact PowerShell one-liners or Wireshark filter chains).
- **Crystal Mode**: Visual design suggestions, infographic ideas, checklist layouts, and motivational but calm framing.
- **Damian Mode**: Strong cybersecurity implementation notes, defense-in-depth, psychological aspects of scare tactics, legal/OPSEC considerations, and clear escalation triggers. Excellent for risk management.

---

## Context Handoff Ritual (End of Every Session)
At the end of each conversation, ask:
"Please append a dated 'Session Summary' section to my `investigation_log.md` covering: actions taken, key findings, decisions made, open questions, and the single most important recommended next action. Also note any suggested improvements to this framework."

---

## Ultra-Light Checklist (Still Available)
Use the shorter checklist from the Minimal Tools version if you want to start very light before going deep.

---

## Escalation & Professional Help

This framework is educational self-help — not certified digital forensics or legal advice. If you confirm data theft, financial impact, sophisticated persistence, or feel personally targeted, **stop DIY investigation** and read [When & How to Escalate](../../Start-Guide/When-and-How_to-Escalate.md). Your investigation log, file inventory, and network captures become your evidence package for professionals.

## Sources & Reliability Notes
- Sysinternals tools (Autoruns, Process Explorer, TCPView): Created by Microsoft, extremely widely used and trusted in professional incident response.
- Wireshark: De-facto standard for network forensics; official documentation and community-validated.
- Timestomping & NTFS artifacts: Well-established in peer-reviewed digital forensics research and real-world IR reports (high reliability ~93-95%).
- General evidence handling: Aligned with NIST and SWGDE best practices.

All recommendations prioritize safety and documentation. This remains educational material.

**Next Step When Starting a New Session:**
Paste this entire file, then say:  
"Current situation: [brief description of symptoms]. I want the Full Deep Dive Path. Start with Phase 0 and guide me step by step with comprehension gates."

---

**End of My Security Investigation Framework - Windows v1.1 Full Deep Dive**

This version provides significantly more depth while remaining structured, calm, and beginner-accessible. It is released for open-source personal safety and educational use. Update the version number and date when you make improvements. 

Minimal Tools and Full Deep Dive versions are available for Windows, macOS, and Linux in this repository. See `Start-Guide/Quick-Start-Guide.md` to begin.