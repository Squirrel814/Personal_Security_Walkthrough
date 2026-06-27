# Quick Start Guide

**Personal Security Investigation Framework**  
Version 1.1 | Cross-Platform (Windows • macOS • Linux)

Welcome. This short guide will help you start your first investigation safely and calmly, even if you have no security background.

---

## What You Need (Minimum)

1. One **Framework** file that matches your operating system:
   - Windows → [`minimal-tools/windows/My_Security_Framework_Windows-OS_v1.1_Minimal_Tools.md`](../minimal-tools/windows/My_Security_Framework_Windows-OS_v1.1_Minimal_Tools.md) (start here)
   - macOS → [`minimal-tools/macos/My_Security_Framework_macOS_v1.1_Minimal_Tools.md`](../minimal-tools/macos/My_Security_Framework_macOS_v1.1_Minimal_Tools.md)
   - Linux → [`minimal-tools/linux/My_Security_Framework_Linux_v1.1_Minimal_Tools.md`](../minimal-tools/linux/My_Security_Framework_Linux_v1.1_Minimal_Tools.md)

2. The two **shared templates** (from this repo’s `Start-Guide/shared-templates/templates/`):
   - [`investigation_log_template.md`](shared-templates/templates/investigation_log_template.md)
   - [`suspicious_files_inventory_template.md`](shared-templates/templates/suspicious_files_inventory_template.md)

3. A calm mindset and willingness to document everything.

You can upgrade to the **Full Deep Dive** version of your platform later if you want more tools and depth.

---

## Step-by-Step: Start Your First Investigation

### Step 1: Set Up Your Workspace (5 minutes)
1. Create a dated folder on your computer — fastest: `python tools/scaffold_investigation_folder.py --output-dir <your Documents path>` from the cloned repo (creates `Investigation_YYYY-MM-DD/` with templates and subfolders). Or create manually; see [Project Structure Recommendation](shared-templates/templates/project_structure_recommendation.md).
2. Copy the following files into it:
   - The framework file for your OS (Minimal Tools version recommended for first time)
   - `investigation_log_template.md`
   - `suspicious_files_inventory_template.md`
3. Rename the two templates with today’s date so they are easy to find later:
   - `investigation_log_2026-06-24.md`
   - `suspicious_files_inventory_2026-06-24.md`

### Step 2: Paste the Framework into an LLM (Any AI)
1. Open any LLM chat (Grok, Claude, GPT, local Ollama model, etc.).
2. Paste the **entire contents** of your chosen framework file.
3. Then type something like:

> Current situation: I have files with future timestamps and weird names that seem targeted at me. I want to follow the Ultra-Light Path. Please start with Phase 0 and guide me step by step with comprehension gates.

The LLM now understands exactly how to help you.

### Step 3: Begin with Phase 0 (Documentation First)
Follow the framework’s Phase 0 instructions:
- Take screenshots of suspicious file Properties / Get Info.
- Check and correct your system date/time if it’s wrong.
- Start filling in your `investigation_log_2026-06-24.md` and `suspicious_files_inventory_2026-06-24.md`.

**Important rule:** Do **not** delete or open the suspicious files yet.

### Step 4: Continue Through the Phases
Work through the phases one at a time. After each major step, ask the LLM for a **Session Summary** and append it to your log (the template has a ready section for this).

You can move at your own pace — there is no rush.

### Step 5: End Each Session Properly
Before closing the LLM chat, ask:

> Please append a short dated Session Summary to my investigation log with: what we did, key findings, decisions made, and the single most important recommended next action.

This keeps everything organized and traceable.

---

## Quick Tips for Success

- **Document everything.** Screenshots, terminal output, and timestamps are your evidence.
- **Stay calm.** Future timestamps and weird files are often used to scare people into making mistakes.
- **Use the Ultra-Light path first.** You can always go deeper later.
- **Never execute unknown files.** Open scripts in a text editor only (read-only).
- **When in doubt, escalate.** If something feels serious (financial accounts, personal data, ongoing targeting), stop and seek professional help. Your logs and inventory will be very useful to them.

---

## When to Go Deeper or Escalate

- **Go Deeper:** If the light path shows clear anomalies or you want more visibility, switch to the Full Deep Dive version in `full-deep-dive/{windows,macos,linux}/`.
- **Escalate:** If you find confirmed malicious behavior, persistence mechanisms, data theft, or feel personally targeted, use the [decision flowchart](When-and-How_to-Escalate.md#decision-flowchart), read [Choosing the Right Professional Help](Choosing-the-Right-Professional-Help.md), prepare your evidence package (log + inventory + captures), and contact the appropriate professional or agency.

---

## Next Steps After Your First Session

1. Review what you learned.
2. Decide whether to continue monitoring lightly or close the investigation.
3. Keep the templates and frameworks for future use — they work for any new incident.

You now have everything needed to begin a safe, well-documented investigation.

Take it one calm step at a time.

---

**This Quick Start Guide** is part of the open-source Personal Security Investigation Framework project.  
It is designed to work with all Minimal Tools and Full Deep Dive framework versions.

Stay safe. Document everything. You’ve got this.