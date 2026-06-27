# Block and Harden

**Personal Security Investigation Framework**  
Version 1.0 | Cross-Platform  
**Phase:** Defense layer — use **after** documentation and escalation check

This guide covers **blocking and hardening on systems you own**: home network edge, accounts, and credentials. It does not replace investigation — it follows it.

**Prerequisites:** Complete Phase 0 documentation (screenshots, inventory, log). See [Quick Start Guide](../Start-Guide/Quick-Start-Guide.md) and your OS [Minimal Tools framework](../minimal-tools/windows/My_Security_Framework_Windows-OS_v1.1_Minimal_Tools.md).

**Scope:** Own network, own accounts. Not hacking back, not scanning third-party networks, not blocking entire platforms to silence harassers (use [platform safety](Platform-Safety-X-and-Social.md) instead).

---

## Mandatory action ladder

Blocking changes system state. Do not skip ahead.

| Step | Action |
|------|--------|
| 1 | **Document** — inventory, screenshots, metadata |
| 2 | **Comprehension gate** — do you understand what you found? |
| 3 | **Escalate check** — [When & How to Escalate](../Start-Guide/When-and-How_to-Escalate.md) |
| 4 | **Block & harden** (this guide) — only if DIY is still appropriate |

**Credential rotation:** Change passwords and enable 2FA on a **clean device** (phone on cellular, or a machine you trust), not on a host you suspect is compromised (~85% — keylogger risk if rotated on infected PC).

---

## Network edge

### Router basics (~85–90% home hygiene)

- [ ] Update **router firmware** from vendor site or admin panel
- [ ] Change **default admin password** — do this from a clean phone on cellular if the PC is suspect (~85%)
- [ ] Use **WPA2-AES or WPA3** for Wi-Fi
- [ ] Review **connected devices** list; note unknown MAC addresses in your investigation log
- [ ] Enable **guest network** for IoT and visitors if supported (~80%)

**Alex note:** Router changes are logged in `investigation_log` with date and what you changed.

### DNS filtering (Pi-hole or router DNS) (~80–85%)

DNS sinkholing drops resolution for known malware, phishing, and ad-tracking domains on **your LAN**. It is a layer, not a cure.

**Typical setup:**

1. Pi-hole or router DNS blocklist on your network only
2. Point LAN clients to the filter (Pi-hole IP or router DNS)
3. Optional: block outbound DNS (UDP/TCP 53) from clients **except** your Pi-hole (~90% — prevents malware bypassing filter with 8.8.8.8)

**Guest network + Pi-hole (~90%):** Many routers isolate guest Wi-Fi from the LAN. Guest devices may not reach a Pi-hole on your main subnet without firewall rules (allow guest → Pi-hole port 53 only). Otherwise guests may lose DNS — use upstream DNS for guest or accept that tradeoff.

**What to block:** Malware C2 lists, phishing feeds, telemetry domains you choose to drop.

**What not to block:** Entire social platforms or harasser-owned sites on your home DNS as retaliation — use X block/mute and LE/IR paths instead (~95% ethics scope).

### Blocklist export (for Pi-hole / hosts)

Save custom domains you documented from investigation (harassment-related C2 only, not people’s blogs) to a local list. Future repo `tools/blocklist_export_template.txt` will mirror this format:

```
# Personal blocklist — YYYY-MM-DD — investigation ref
# One domain per line
malware-example.bad
```

---

## Accounts and credentials

### Week 1 — stabilize (~90% industry alignment)

| Priority | Action |
|----------|--------|
| Email | Unique strong password; **app-based 2FA** (Authenticator app or security key) |
| Banking / payments | Unique passwords; 2FA; review recent transactions |
| Password manager | Adopt if not in use (~90%) |
| Recovery codes | Print or store offline — avoid lockout |

**SMS 2FA (~80%):** Better than nothing; SIM-swap risk makes app-based 2FA preferable where available.

### Week 2 — audit (~85%)

| Action | Notes |
|--------|-------|
| [Have I Been Pwned](https://haveibeenpwned.com) | Shows **known breaches**, not live malware (~85%) |
| OAuth / connected apps | Revoke unknown apps in Google, Microsoft, Apple, X settings |
| Alias emails | SimpleLogin, Firefox Relay, or provider aliases for new signups (~80%) |

**HIBP k-anonymity (~95%, sourced):** Password check sends only the first 5 characters of the SHA-1 hash prefix; full hash stays local. Still use only on a device you trust.

### Ongoing

- OS and browser auto-updates on (~90% — [cyber.gov.au device guidance](https://www.cyber.gov.au/protect-yourself/securing-your-devices/how-secure-your-devices))
- Standard user account for daily work; admin only for installs (~85% — least privilege)
- Dedicated browser profile for banking (~75%)

---

## Block action reference

| Action | Difficulty | Evidence preserved? | Risk if misconfigured |
|--------|------------|---------------------|------------------------|
| Router DNS / Pi-hole | Medium | Yes, if PCAPs/logs done first | Over-blocking breaks normal browsing |
| Guest network isolation | Low | Yes | Guests may not resolve DNS via Pi-hole without rules |
| X block / mute / report | Low | **Screenshot first** — platform may remove posts (~85% X Help Center) | Block may notify harasser; mute is quieter |
| 2FA + password rotation | Low | Yes | Lockout without recovery codes |
| HIBP breach check | Low | Yes | Shows historical breaches only |
| Firewall egress deny (advanced) | High | Yes | Can break updates and apps |

---

## Device hardening (quick)

- [ ] Full-disk encryption on (BitLocker, FileVault, LUKS) (~90%)
- [ ] Disable remote access you do not use (RDP, SSH, screen sharing)
- [ ] Pause **cloud sync** during active investigation if scare files might upload (~85%)
- [ ] Air-gapped or offline backups for important data — not NAS always-on during active compromise (~85%)

Longer cadence: [Protecting Yourself After an Incident](../Start-Guide/Protecting-Yourself-After-an-Incident.md).

---

## When to stop blocking and escalate

- Unauthorized financial transactions → bank **first**, then IR/LE
- Persistence survives reboot → pro/IR
- Confirmed beaconing to unknown IPs → [escalate](../Start-Guide/When-and-How_to-Escalate.md)
- You are unsure → escalate early with your evidence package

---

## Related guides

- [Safe Removal After Documentation](Safe-Removal-After-Documentation.md) — quarantine **after** this guide’s prerequisites
- [Platform Safety (X & Social)](Platform-Safety-X-and-Social.md)
- [Protecting Yourself After an Incident](../Start-Guide/Protecting-Yourself-After-an-Incident.md)
- [When & How to Escalate](../Start-Guide/When-and-How_to-Escalate.md)

---

**End of Block and Harden**

Layer defenses over time. Document what you change.