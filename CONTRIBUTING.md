# Contributing to Personal Security Walkthrough

Thank you for helping make personal-safety investigation guidance clearer, calmer, and more accessible. This project is part of the **Interwoven Projects** open-source community.

---

## What we welcome

- Documentation clarity, typo fixes, and beginner-friendly rewrites
- Cross-platform parity (Windows, macOS, Linux frameworks stay aligned)
- Template and example improvements that model evidence-first practice
- Safer command examples with brief "why this matters" context
- Links, diagrams, and checklists that reduce anxiety without alarmism
- Bug reports when instructions are wrong, broken, or unsafe

---

## What we will not merge

To protect readers and maintain project intent, the following are **out of scope**:

- **Offensive security** — exploitation, unauthorized access, "hacking back," or aggressive scanning beyond passive home monitoring
- **Legal advice** — or claims that DIY steps produce court-admissible forensic results
- **Evidence-destructive guidance** — steps that encourage deleting, altering, or executing suspicious files before documentation
- **DIY forensic imaging as a substitute for escalation** — companion docs may explain *when* to hand off; they must not replace professional help for serious incidents

**Required tone:** Calm, evidence-first, escalation-aware — match the [Quick Start Guide](Start-Guide/Quick-Start-Guide.md) and framework invariants.

---

## How to contribute

### 1. Report an issue

Use GitHub Issues for:

- Incorrect or dangerous instructions
- Broken links after folder changes
- Platform-specific gaps
- Suggestions for new Start-Guide companion docs

Use the issue templates when available (`.github/ISSUE_TEMPLATE/`).

### 2. Propose a change (PR)

1. Fork the repository and create a branch from `main`.
2. Make focused changes — one logical improvement per PR when possible.
3. If you touch command blocks, note in the PR that you verified they are **read-only** or **non-destructive** by default.
4. Open a pull request with:
   - What changed and why
   - Which files/platforms you tested or reviewed
   - Any security or ethics considerations

**CI:** Pull requests to `main` run the internal link validator (`.github/workflows/validate-links.yml`). Fix broken relative links before merge. Locally: `python tools/validate_walkthrough_links.py`.

### 3. Content standards

- **Commands:** Prefer built-in, read-only inspection (`stat`, Properties, `ss`, exports to CSV). Flag anything requiring admin rights or third-party uploads (e.g. VirusTotal) with a privacy note.
- **Escalation:** New investigation steps should point to [When & How to Escalate](Start-Guide/When-and-How_to-Escalate.md) when findings cross into professional territory.
- **Examples:** Use redacted, fictional paths and names in templates/examples — no real PII.
- **Sources:** When citing reliability, keep percentage ratings where they exist in source material.

---

## License note for contributors

By contributing documentation, you agree that your contributions are licensed under **CC BY-SA 4.0**. Code contributions (if any) are licensed under **MIT**. See [LICENSE](LICENSE).

---

## Code of conduct

Be respectful and constructive. This project serves people who may be anxious or targeted. Prioritize clarity and safety over cleverness.

Questions? Open an issue. We appreciate careful, evidence-minded contributions.