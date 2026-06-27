# My Security Investigation Framework - Linux (Full Deep Dive)
**Version:** 1.1 - Full Deep Dive (2026-06-24)  
**Purpose:** This is the comprehensive Linux version. Paste the entire file at the start of any LLM conversation. It provides deeper tool recommendations, richer analysis techniques, and more thorough investigation steps while remaining educational, calm, and evidence-focused for Linux users.

---

## Full Deep Dive vs Minimal Tools Path

This version supports two tracks:

- **Ultra-Light Path** — Same as the Minimal Tools v1.1 version (standard Terminal commands with minimal or no extra packages). Good for quick starts.
- **Full Deep Dive Path** — Recommended when you want maximum visibility. Includes more powerful free tools, deeper persistence and network analysis, advanced file forensics, and richer guidance.

You can start with the light path and expand into deep dive steps as needed. The framework works well with local LLMs (Ollama and similar), though stronger models are helpful for complex log or packet analysis.

**Note on distributions:** Commands are chosen for broad compatibility. Adjust package installation commands (`apt`, `dnf`, `pacman`, `zypper`, etc.) according to your distribution. Most core investigation commands work across major distros.

---

## Crisp Goal Statement
Deliver a thorough, evidence-first investigation framework for Linux users facing suspicious files (future timestamps, weird flags, possible targeted scare tactics) and network anomalies. Combine native Terminal tools with high-quality free utilities for deeper insight while staying accessible and safe for non-experts.

## Success Criteria
- User can follow either path and produce well-documented findings.
- LLM provides structured, actionable, copy-paste-ready guidance with clear reasoning.
- User understands when findings require professional escalation.
- Framework remains reusable and consistent across sessions and distributions.

## Hard Invariants (Never Break)
- Evidence preservation is non-negotiable — document before any changes.
- Never execute unknown files, scripts, or binaries.
- Stay calm and methodical. Scare tactics often rely on inducing mistakes that destroy evidence.
- Escalate promptly for confirmed data theft, financial harm, or ongoing personal targeting.
- This is educational self-help material, not a substitute for certified digital forensics or legal advice.

## Key Files to Create
- `investigation_log.md` — Master running log with dates, observations, decisions, and LLM outputs.
- `suspicious_files_inventory.md` — Detailed inventory of concerning files (paths, timestamps, metadata, observations).
- `network_captures/` — Folder for .pcap / .pcapng files with clear date-based naming.
- `tools/` (optional) — Dedicated folder for downloaded free utilities (ExifTool, Wireshark, ClamAV, etc.).

## Phased Plan

### Phase 0: Immediate Safety, Documentation & System Basics (Both Paths)
**Goal:** Secure the current state and rule out simple causes.  
**Actions (required for both paths):**
1. Use Terminal to inspect suspicious files (replace `/path/to/file`):
   ```bash
   stat "/path/to/file"
   ls -l "/path/to/file"
   file "/path/to/file"
   ```
   Record or screenshot the output, especially timestamps.
2. Check system time:
   ```bash
   timedatectl status
   ```
   Correct if significantly wrong and note the change.
3. Create the key files listed above.
4. Do **not** delete, move, rename, or execute suspicious files.

**Comprehension Gate:** Have you fully documented the initial state and verified system time? Ready to proceed?

### Phase 1: Multi-Layered Detection & Persistence Hunting (Deep Dive Path)
**Goal:** Thoroughly check for malware, persistence mechanisms, and anomalies using both built-in and high-quality free tools.

**Recommended tools (install as needed):**
- Built-in: `ps`, `systemctl`, `journalctl`, `crontab`, `lsattr`, `getfattr`.
- **ClamAV** (lightweight antivirus scanner) — `sudo apt install clamav` or equivalent.
- **rkhunter** or **chkrootkit** (rootkit scanners) — optional but useful for deeper checks.
- **Lynis** (system auditing tool) — excellent for security posture review.
- ExifTool and Wireshark (via package manager or source).

**Actions:**
1. Review running processes and services:
   ```bash
   ps auxf
   systemctl list-units --type=service --state=running
   systemctl list-unit-files --type=service | grep enabled
   ```
2. Check persistence locations:
   ```bash
   crontab -l
   cat /etc/crontab
   ls -la /etc/init.d/
   ls -la ~/.config/autostart/ 2>/dev/null
   cat ~/.bashrc ~/.zshrc ~/.profile 2>/dev/null | grep -E 'curl|wget|bash -c|sh -c'
   ```
3. Review recent system logs for errors or anomalies:
   ```bash
   journalctl -p err..alert -n 100 --no-pager
   ```
4. Optional deeper scans:
   - Run ClamAV: `sudo freshclam && sudo clamscan -r /home --bell`
   - Run rkhunter or Lynis for broader auditing.

**Comprehension Gate:** Persistence and process reviews complete? Any concerning items logged in your inventory? Ready for advanced file forensics?

### Phase 2: Advanced File Forensics & Timestamp Analysis (Deep Dive Path)
**Goal:** Perform deeper inspection of suspicious files and timeline manipulation.

Future timestamps are a classic sign of **timestomping**. Linux filesystems (ext4, btrfs, xfs, etc.) offer additional attributes via `lsattr` and extended attributes.

**Actions:**
- Basic: `stat`, `ls -l`, `file`.
- Deeper:
  - Install and use **ExifTool**:
    ```bash
    exiftool "/path/to/file"
    ```
  - Check extended attributes and immutable flags:
    ```bash
    getfattr -d "/path/to/file"
    lsattr "/path/to/file"
    ```
  - Inspect binaries and scripts without executing:
    ```bash
    file "/path/to/file"
    strings "/path/to/file" | head -30
    ldd "/path/to/file" 2>/dev/null
    ```
  - Recursive timestamp hunting example:
    ```bash
    find /home /tmp /var/tmp -type f -newermt "30 days ago" -ls 2>/dev/null | head -50
    ```
    (Adjust the time window and review results carefully.)

**Powerful but concise LLM Prompt:**
```
You are a calm, experienced digital forensics mentor helping a Linux user.

Context: Investigating files with future timestamps and possible targeted anomalies on Linux.

Analyze the following:

[PASTE stat / ls / exiftool / getfattr / strings / journalctl / ps output OR script content]

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
1. Install Wireshark (`sudo apt install wireshark` or equivalent; may require adding user to `wireshark` group).
2. Capture on your primary interface (use `ip link` or `ifconfig` to identify) for 10–15 minutes of normal + idle activity.
3. Save captures with clear date-based names in your `network_captures/` folder.
4. Useful starting display filters:
   - `dns`
   - `http or http2`
   - `tcp.flags.syn == 1 && tcp.flags.ack == 0`
   - `ip.addr == x.x.x.x`
   - Look for periodic small packets to the same external destination (beaconing).

**Complementary native or lightweight tools:**
- `ss -tulnpe` (modern replacement for netstat with process info)
- `lsof -i -n -P`
- `tcpdump -i any -w capture.pcap` for quick captures
- `journalctl` for reviewing network-related logs

**LLM Prompt for Network Data:**
```
You are a calm network forensics analyst helping a Linux beginner.

Here is network or Terminal output from my system:

[PASTE ss / lsof / journalctl / Wireshark filtered output / tcpdump results]

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
- Clean results + timestamps explained by clock issues → Focus on baseline hardening (keep system and packages updated, review services and cron jobs regularly, use strong unique passwords + 2FA, enable firewall with `ufw`/`firewalld`/`nftables`).
- Confirmed anomalies, persistence mechanisms, or clear targeting → Stop normal use of the machine if possible. Create a full backup or forensic image before further changes. Your documentation becomes extremely valuable for professionals.
- High uncertainty or sophisticated indicators → Strongly consider engaging a professional incident responder. Do not continue extensive DIY work alone.

**Comprehension Gate:** What is your overall assessment of the situation? Do you need help creating a clean escalation summary?

### Phase 5: Ongoing Monitoring & Hardening (Deep Dive Path)
- Periodically re-check services (`systemctl`), cron jobs, and persistence locations.
- Schedule occasional Wireshark or `tcpdump` captures for baseline comparison.
- Keep your distribution and packages updated.
- Consider running Lynis or similar auditing tools on a schedule.
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
The shorter Ultra-Light Checklist from the Linux Minimal Tools v1.1 version remains available if you want to begin with the lightest possible approach before expanding into deep dive steps.

---

## Escalation & Professional Help

This framework is educational self-help — not certified digital forensics or legal advice. If you confirm data theft, financial impact, sophisticated persistence, or feel personally targeted, **stop DIY investigation** and read [When & How to Escalate](../../Start-Guide/When-and-How_to-Escalate.md). Your investigation log, file inventory, and network captures become your evidence package for professionals.

## Sources & Reliability Notes
- Standard Linux Terminal tools (`stat`, `ss`, `lsof`, `journalctl`, `ps`, `find`) are reliable and widely available across distributions.
- Tools like ClamAV, rkhunter, Lynis, and Wireshark are well-established in the Linux security community.
- Timestomping and metadata analysis: Established concepts in digital forensics literature and incident response practice.
- This remains educational self-help guidance. Escalate confirmed incidents to professionals.

**Next Step When Starting a New Session:**
Paste this entire file into a new chat and say:  
"Current situation: [brief description]. I want the Full Deep Dive Path on Linux. Please start with Phase 0 and guide me step by step with comprehension gates."

---

**End of My Security Investigation Framework - Linux v1.1 Full Deep Dive**

This version provides substantially more depth for Linux while preserving the calm, structured, and beginner-friendly approach of the overall project. It is released for open-source personal safety and educational purposes. Update the version and date when making improvements.

You now have a complete matching set: Minimal Tools and Full Deep Dive versions for Windows, macOS, and Linux. The framework collection is ready for your open-source repository. Next steps could include creating a root README, shared templates, or contribution guidelines. Let me know how you would like to proceed.