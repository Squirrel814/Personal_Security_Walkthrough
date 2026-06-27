# My Security Investigation Framework - macOS (Full Deep Dive)
**Version:** 1.1 - Full Deep Dive (2026-06-24)  
**Purpose:** This is the comprehensive macOS version. Paste the entire file at the start of any LLM conversation. It provides deeper tool recommendations, richer analysis techniques, and more thorough investigation steps while remaining educational, calm, and evidence-focused.

---

## Full Deep Dive vs Minimal Tools Path

This version supports two tracks:

- **Ultra-Light Path** — Same as the Minimal Tools v1.1 version (built-in Terminal + Finder focus). Good for quick starts or limited resources.
- **Full Deep Dive Path** — Recommended when you want maximum visibility. Includes more powerful free tools, deeper persistence and network analysis, and richer forensic techniques.

You can begin with the light path and move into deep dive steps as needed. The framework works well with local LLMs (Ollama and similar), though stronger models help with complex log or packet analysis.

---

## Crisp Goal Statement
Deliver a thorough, evidence-first investigation framework for macOS users dealing with suspicious files (future timestamps, weird flags, possible targeted scare tactics) and network anomalies. Combine native macOS tools with high-quality free utilities for deeper insight while staying accessible and safe for non-experts.

## Success Criteria
- User can confidently follow either path and produce well-documented findings.
- LLM provides structured, actionable, copy-paste-ready guidance with clear reasoning.
- User understands when findings require professional escalation.
- Framework remains reusable and consistent across sessions.

## Hard Invariants (Never Break)
- Evidence preservation comes first — document everything before making changes.
- Never execute unknown files, scripts, or applications.
- Stay calm and methodical. Scare tactics often aim to provoke mistakes that destroy evidence.
- Escalate promptly for confirmed data theft, financial harm, or ongoing personal targeting.
- This is educational self-help material, not a replacement for certified digital forensics or legal advice.

## Key Files to Create
- `investigation_log.md` — Master running log with dates, screenshots, decisions, and LLM outputs.
- `suspicious_files_inventory.md` — Detailed inventory of concerning files (paths, timestamps, metadata, observations).
- `network_captures/` — Folder for .pcapng or .pcap files with clear date-based naming.
- `tools/` (optional) — Dedicated folder for downloaded free utilities (ExifTool, KnockKnock, Wireshark, etc.).

## Phased Plan

### Phase 0: Immediate Safety, Documentation & System Basics (Both Paths)
**Goal:** Secure the current state and eliminate simple explanations.  
**Actions (required):**
1. For every suspicious file, use Finder → right-click → Get Info. Screenshot the General and More Info sections, paying special attention to Created, Modified, and Accessed dates.
2. Verify system date and time (System Settings → General → Date & Time). Correct if significantly wrong and record the change.
3. Create the key files listed above.
4. Do **not** open, move, rename, delete, or execute suspicious files.

**Comprehension Gate:** Have you fully documented the initial state and checked system time? Ready to continue?

### Phase 1: Multi-Layered Detection & Persistence Hunting (Deep Dive Path)
**Goal:** Thoroughly check for malware, persistence mechanisms, and anomalies using both built-in and high-quality free tools.

**Recommended tools (install in this order):**
- Built-in: System Settings → Privacy & Security review (Login Items, Full Disk Access, Files and Folders, Extensions).
- **KnockKnock** (free from Objective-See) — Excellent for spotting persistence (LaunchAgents, LaunchDaemons, cron jobs, etc.).
- **BlockBlock** (free from Objective-See) — Real-time persistence monitoring (optional but very useful).
- ExifTool (free, install via Homebrew: `brew install exiftool`).
- Wireshark (official site or via Homebrew).
- Activity Monitor + Terminal commands for process inspection.

**Actions:**
1. Review all Privacy & Security sections in System Settings for unexpected entries.
2. Run KnockKnock and examine results for unsigned or suspicious items. Export/save the output.
3. Use Terminal for deeper persistence checks:
   ```bash
   ls -la ~/Library/LaunchAgents
   ls -la /Library/LaunchAgents
   ls -la /Library/LaunchDaemons
   crontab -l
   launchctl list | grep -v com.apple
   ```
4. For running processes and network connections:
   ```bash
   ps aux
   lsof -i -n -P
   netstat -an | grep ESTABLISHED
   ```

**Comprehension Gate:** Persistence and process reviews complete? Any concerning items logged? Ready for advanced file forensics?

### Phase 2: Advanced File Forensics & Timestamp Analysis (Deep Dive Path)
**Goal:** Perform deeper inspection of suspicious files and timeline manipulation.

Future timestamps are a known sign of **timestomping**. On macOS (APFS/HFS+), native metadata and extended attributes can provide additional clues.

**Actions:**
- Basic: Finder Get Info + Terminal `stat` and `mdls`.
- Deeper:
  - Install and use **ExifTool** for rich metadata:
    ```bash
    exiftool "/path/to/file"
    ```
  - Check extended attributes and quarantine flags:
    ```bash
    xattr -l "/path/to/file"
    ls -l@ "/path/to/file"
    ```
  - For scripts and binaries: Use `file`, `strings`, and `otool` (for Mach-O binaries) to inspect without executing.
  - Simple recursive timestamp hunt (example):
    ```bash
    find ~ -type f -newermt "30 days" -ls 2>/dev/null | head -50
    ```
    (Adjust the time window as needed and review results carefully.)

**Powerful but concise LLM Prompt:**
```
You are a calm, experienced digital forensics mentor helping a macOS user.

Context: Investigating files with future timestamps and possible targeted anomalies on macOS.

Analyze the following:

[PASTE Get Info details, ExifTool output, stat/mdls/xattr results, script content, or Terminal output]

Tasks:
1. Summarize key findings in plain language.
2. Highlight any indicators of timestomping, obfuscation, persistence, or malicious behavior.
3. Give confidence level (Low/Medium/High) with brief reasoning.
4. Recommend the single safest and most useful next action.

Output in clear bullets + one short "Bottom line" sentence.
```

**Comprehension Gate:** Have you completed deeper file analysis? What stood out? Ready for network deep dive?

### Phase 3: Comprehensive Network Monitoring & Analysis (Deep Dive Path)
**Goal:** Gain strong visibility into network behavior and potential command-and-control activity.

**Core Tool: Wireshark**
1. Install Wireshark (official site or `brew install wireshark`).
2. Capture on your primary interface (usually Wi-Fi or en0/en1) for 10–15 minutes of normal + idle activity.
3. Save captures with clear date-based names in your `network_captures/` folder.
4. Useful starting display filters:
   - `dns`
   - `http or http2`
   - `tcp.flags.syn == 1 && tcp.flags.ack == 0`
   - `ip.addr == x.x.x.x`
   - Look for periodic small packets to the same external destination (beaconing).

**Complementary macOS-native or lightweight tools:**
- Terminal: `lsof -i`, `netstat -an`, `tcpdump` (for quick captures).
- Little Snitch (optional paid tool with excellent free trial) for application-level network control and visibility.
- Activity Monitor → Network tab for high-level overview.

**LLM Prompt for Network Data:**
```
You are a calm network forensics analyst helping a macOS beginner.

Here is network or Terminal output from my system:

[PASTE lsof / netstat / Wireshark filtered output / tcpdump results]

Analyze for:
- Beaconing or C2 patterns
- Data exfiltration
- Suspicious domains or connections
- Unexpected listening ports or processes

Explain findings simply but accurately. List any concerning IPs or behaviors with confidence level. Suggest one useful next filter or command.
```

**Comprehension Gate:** Network analysis complete? Any suspicious activity identified? Ready to synthesize everything?

### Phase 4: Synthesis, Decision Making & Escalation (Both Paths)
**Goal:** Combine all evidence and decide on appropriate next steps.

**Common outcomes:**
- Clean results + timestamps explained by clock issues → Focus on baseline hardening (keep macOS and apps updated, review Login Items regularly, enable FileVault and Firewall, use strong unique passwords + 2FA).
- Confirmed anomalies, persistence mechanisms, or clear targeting → Stop normal use of the machine if possible. Create a full backup or forensic image before further changes. Your documentation (logs + captures + inventory) becomes extremely valuable for professionals.
- High uncertainty or sophisticated indicators → Strongly consider engaging a professional incident responder or law enforcement. Do not continue extensive DIY work alone.

**Comprehension Gate:** What is your overall assessment of the situation? Do you need help creating a clean escalation summary?

### Phase 5: Ongoing Monitoring & Hardening (Deep Dive Path)
- Periodically re-run KnockKnock or review LaunchAgents/Daemons.
- Schedule occasional Wireshark or `tcpdump` captures for baseline comparison.
- Keep macOS, apps, and Homebrew packages updated.
- Consider enabling more detailed logging where practical and reviewing it periodically.
- Maintain your investigation log as a living document.

---

## Optional Role Emulation (Advanced)
You can tell the LLM at the start of a response: "Use [Role] mode for this turn."

- **Cyber-SQRRL Mode**: Clear educational structure, investigation pedagogy, learning progressions, and explanations suitable for teaching or curriculum development.
- **Rusty Mode**: Precise, safe Terminal commands, small experiments, and implementation-focused details.
- **Crystal Mode**: Visual design ideas, checklist layouts, infographic suggestions, and calm motivational framing.
- **Damian Mode**: Strong cybersecurity implementation notes, defense-in-depth thinking, psychological aspects of scare tactics, legal/OPSEC considerations, and clear escalation guidance.

---

## Context Handoff Ritual (End of Every Session)
At the end of each conversation, ask the LLM:
"Please append a short dated 'Session Summary' to my `investigation_log.md` that includes: actions taken, key findings, decisions made, open questions, and the single most important recommended next action. Also note any suggested improvements to this framework."

---

## Ultra-Light Checklist
The shorter Ultra-Light Checklist from the macOS Minimal Tools v1.1 version remains available if you want to begin with the lightest possible approach before expanding into deep dive steps.

---

## Escalation & Professional Help

This framework is educational self-help — not certified digital forensics or legal advice. If you confirm data theft, financial impact, sophisticated persistence, or feel personally targeted, **stop DIY investigation** and read [When & How to Escalate](../../Start-Guide/When-and-How_to-Escalate.md). Your investigation log, file inventory, and network captures become your evidence package for professionals.

## Sources & Reliability Notes
- Objective-See tools (KnockKnock, BlockBlock): Highly regarded free macOS security utilities created by a respected researcher.
- Wireshark: Industry-standard network analysis tool with extensive documentation and community validation.
- Timestomping and metadata analysis: Established concepts in digital forensics literature and incident response practice.
- macOS built-in tools and Terminal commands: Reliable native capabilities for investigation.

All guidance emphasizes safety, documentation, and knowing when to escalate. This remains educational material for personal use.

**Next Step When Starting a New Session:**
Paste this entire file into a new chat and say:  
"Current situation: [brief description]. I want the Full Deep Dive Path on macOS. Please start with Phase 0 and guide me step by step with comprehension gates."

---

**End of My Security Investigation Framework - macOS v1.1 Full Deep Dive**

This version provides substantially more depth for macOS while preserving the calm, structured, and beginner-friendly approach of the overall project. It is released for open-source personal safety and educational purposes. Update the version and date when making improvements.

You now have matching Full Deep Dive coverage for Windows and macOS. The Linux Full Deep Dive version can be created next if desired.