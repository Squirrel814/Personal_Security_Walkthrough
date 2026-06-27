# Personal Security Walkthrough — Infograph Prompts v2

**Repo:** [Personal_Security_Walkthrough](https://github.com/Squirrel814/Personal_Security_Walkthrough)  
**Version:** 2.0  
**Date:** 2026-06-27  
**For:** Image generation (Gemini, ChatGPT, Ideogram, Midjourney, etc.)

Copy **STYLE PREFIX** + one prompt block below. Upload the two **style reference** images when the tool supports reference input.

---

## Style authority (read first)

| Rule | Detail |
|------|--------|
| **Style references** | `Investigation-Flow.jpg` + `Personal-Security-Walkthrough.jpg` only — these define the final look |
| **Do not use** | Anything in `Infographs/Archived/` for style matching |
| **Do not use** | Root-level legacy `Infograph_First-Steps*.jpg` (flat sage/blue v1) |
| **Language** | **Strictly factual** Personal Security Walkthrough terms — see [Language rules](#language-rules-no-game-copy) |
| **Mascots** | Woodland creatures in tactical vest (cyber/security education path) — species assignments in [Mascot roster](#mascot-roster) |
| **Escalation text** | Criteria labels must match `Start-Guide/When-and-How_to-Escalate.md` or `Infograph_When-to-Escalate.svg` |

**Cross-project note:** Creatures share Burrowkins *species* design only. Prompts and on-image text use **investigation / evidence / defense** vocabulary — never Acorn Grove game terms.

---

## Language rules (no game copy)

### Use on infographs

investigation · evidence · document · screenshot · properties · inventory · investigation log · framework · Phase 0 · comprehension gate · escalate · professional help · block · mute · report · harden · router · 2FA · antivirus · metadata · network capture · forensic image · law enforcement · not legal advice

### Never use on infographs

rootline · leyline · grove · forge · burrowkin · acorn · node · package · bond · blightroot · adventure · side-quest · canopy · tunnel · scout-network · leyline scan · cache (game sense) · NPC · quest · XP · loot

### Tone

Calm personal-safety education — not alarmist cybersecurity marketing, not cozy game UI.

---

## Mascot roster

Species-only on art (no character names on image). Optional lore names (Squeaky, Pip, Rascal) are for docs only.

| Species | Job | Appears on |
|---------|-----|------------|
| **Squirrel** | Curriculum host + **LLM co-pilot** | Overview, LLM flow, Quick Start |
| **Raccoon** | Investigation specialist | Document-first, six-phase flow, evidence package |
| **Owl** | Escalation analyst | When-to-escalate ladder |
| **Fox** | Communications specialist | Pro summary, platform safety, LE expectations |
| **Badger** | Hardening specialist | Week 1 stabilize, block-and-harden grid header |
| **Beaver** | Network paths | Block-and-harden network quadrant |
| **Hedgehog** | Account / edge fortifier | 2FA / firewall quadrant |
| **Turtle** | Patient shield | OS update quadrant |
| **Otter** | Recovery / flow | After-incident recovery |
| **Mole** | Deep evidence | Forensic image |
| **Deer** | Professional routing | Choosing help |
| **Toad** | Safe removal | Quarantine after documentation |
| **Chipmunk** | Breach logging | Breach check inventory (optional) |
| **Hawk / Bat** | Passive scan | Network-check emphasis (optional inset only) |

---

## STYLE PREFIX (prepend to every prompt)

```
STYLE — match reference images Investigation-Flow.jpg and Personal-Security-Walkthrough.jpg:

VISUAL:
- Aged parchment / field-manual background: warm beige (#E8D9C2–#F5E8C7), irregular torn deckled edges, subtle paper texture
- Optional soft forest bokeh behind parchment edges (Investigation-Flow style)
- Content panels: dark charcoal / olive-black rounded rectangles with soft inner glow
- Accents: bright neon cyan (#00E5FF–#00CED1) for icons, arrows, borders, glow — NEVER alarm red
- Typography: bold black/dark brown sans-serif for titles; white or light text on dark panels; short phrases only (5–8 words per label max)
- Icons: simple neon cyan line art (camera, shield, clock, clipboard, network nodes, padlock)
- Connecting elements: curved cyan glowing arrows between steps (Investigation-Flow style)
- Optional: thin cyan border tracing the parchment edge (LLM flow style)

MASCOT (when specified):
- Anthropomorphic woodland creature, realistic-illustrative fur texture, calm focused expression
- Dark olive/teal tactical vest or jacket; optional teal-tinted goggles (inspect / decide phases)
- Small vest patch OK (DOC, SCAN, HARDEN) — must not replace readable step text
- Mascot supports layout; escalation criteria and steps remain primary readable content

FOOTER (one line, rotate by section):
- Investigate: "Document first · Not legal advice"
- Block & Harden: "Defense not retaliation · Own systems only"
- Escalate: "Panic destroys evidence → Calm wins"
- LLM: "LLM explains · You document · Tools verify"
- Platform: "Document for LE · Don't feed the scare campaign"

AVOID:
- Flat pastel sage/blue v1 style, white backgrounds, vector-only flat art
- Game UI, quest language, fantasy RPG menus
- Hoodies, skulls, binary rain, "you've been hacked" popups, weapons, alarm red banners
- Tiny unreadable text walls; real company logos except generic OS icons where noted
```

### Reference upload (image tools)

1. Upload `Investigation-Flow.jpg` — panel layout, raccoon treatment, cyan arrows  
2. Upload `Personal-Security-Walkthrough.jpg` — three-column dark panels, squirrel overview  
3. Prompt: *"Match parchment texture, dark panel style, and cyan glow from references. Factual security education infographic."*

### Aspect ratios

| Use case | Ratio | Pixels |
|----------|-------|--------|
| README / GitHub wide | 16:9 | 1920×1080 |
| Six-phase flow | 16:9 | 1920×1080 |
| Decision ladder / checklist | 9:16 or 3:4 | 1080×1920 / 1536×2048 |
| Document-first / platform | 1:1 or 3:4 | 1200×1200 |

### Negative prompt (if supported)

```
red alert sirens, aggressive warning red, hacker hoodies, skulls, matrix binary rain,
dark web aesthetics, game HUD, quest text, fantasy RPG items, unreadable microtext,
photorealistic humans, official government seals implying endorsement
```

---

## Inventory — what to generate

| Target filename | Status | Mascot | Style ref |
|-----------------|--------|--------|-----------|
| `Personal-Security-Walkthrough.jpg` | ✅ Shipped | Squirrel ×3 | **Primary ref** |
| `Investigation-Flow.jpg` | ✅ Shipped | Raccoon ×6 | **Primary ref** |
| `Document-First.jpg` | ✅ Shipped | Raccoon | Match refs |
| `Summary-for-Professionals.jpg` | ✅ Shipped | Fox | Match refs |
| `Week-1-Stabilize.jpg` | ✅ Shipped | Badger | Match refs |
| `LLM-Co-Pilot-Flow.jpg` | ✅ Shipped | Squirrel | Match refs |
| `When-to-Escalate.jpg` | ✅ Shipped | Owl | Match refs; verify text vs SVG |
| `Your-Evidence-Package.jpg` | ✅ Shipped | Raccoon | Match refs |
| `Platform-Safety.jpg` | ✅ Shipped | Fox | Match refs |
| `Block-and-Harden-Grid.jpg` | ✅ Shipped | Badger + 4 specialists | Match refs |
| `Safe-Removal.jpg` | ✅ Shipped | Toad | Match refs |
| `Forensic-Image.jpg` | ✅ Shipped | Mole | Match refs |
| `Choosing-Professional-Help.jpg` | ✅ Shipped | Deer | Match refs |
| `After-Incident-Recovery.jpg` | ✅ Shipped | Otter | Match refs |
| `Law-Enforcement-Expectations.jpg` | ✅ Shipped | Fox | Match refs |
| `Breach-Check-Inventory.jpg` | ✅ Shipped (optional) | Chipmunk | Match refs |

---

## Prompt 01 — Personal Security Walkthrough (overview)

**File:** `Personal-Security-Walkthrough.jpg`  
**Ratio:** 16:9  
**Mascot:** Squirrel (one per panel, accessories vary)  
**Status:** Shipped — use as reference; regenerate only if copy changes

```
[STYLE PREFIX]

TITLE (top center, bold black serif): "Personal Security Walkthrough"
Small leaf ornaments flanking title (subtle, not fantasy RPG).

THREE equal vertical panels, dark charcoal rounded rectangles with glowing cyan borders:

PANEL 1 — INVESTIGATE
- Cyan circle icon: magnifying glass
- Header: INVESTIGATE
- Subtitle: "frameworks + LLM + templates"
- Squirrel mascot: green field cap, tactical vest, clipboard; cyan brain-to-document arrow icon nearby

PANEL 2 — BLOCK & HARDEN
- Cyan circle icon: shield
- Header: BLOCK & HARDEN
- Subtitle: "accounts · network · platform"
- Squirrel mascot: tactical vest; three small cyan icons labeled "accounts" "network" "platform"

PANEL 3 — ESCALATE
- Cyan circle icon: upward trend / chart arrow
- Header: ESCALATE
- Subtitle: "flowchart + professional summary"
- Squirrel mascot: teal goggles, vest; flowchart + document icons labeled "flowchart" "summary"

TAGLINE (center below panels): "Composed & Strategic • Evidence First • Open Source"
FOOTER: "Interwoven Projects Community" with small leaf accents
```

---

## Prompt 02 — Investigation Flow (six phases)

**File:** `Investigation-Flow.jpg`  
**Ratio:** 16:9  
**Mascot:** Raccoon — same character model in each panel; teal goggles on phases 4 and 6  
**Status:** Shipped — primary style reference

```
[STYLE PREFIX]

TITLE: "Beginner Security Investigation — Six Phases"

LAYOUT: Six dark olive-black rounded panels in one horizontal row, left to right.
Three curved neon cyan arrows above panels showing sequential flow.

Per panel (top to bottom): glowing cyan icon → raccoon bust in tactical vest → phase number + name → one-line instruction.

1. DOCUMENT — camera icon — "Screenshot properties → Start your log"
2. VERIFY TIME — stopwatch icon — "Check system date"
3. SCAN — shield with checkmark — "Trusted antivirus scan"
4. INSPECT FILES — magnifying glass + file — "Read metadata → Never run scripts" — raccoon wears teal goggles
5. NETWORK CHECK — three connected nodes icon — "Passive monitoring only"
6. DECIDE — clipboard checklist — "Clean → Monitor → Escalate" — raccoon wears teal goggles

TOP-RIGHT callout (parchment torn edge, amber warning triangle only): "Do not delete suspicious files yet"

FOOTER: "Paste framework into any LLM → Ultra-Light path first"
```

---

## Prompt 03 — Document First

**File:** `Document-First.jpg`  
**Ratio:** 3:4 or 1:1  
**Mascot:** Raccoon (left, pointing at center notepad)  
**Status:** Shipped

```
[STYLE PREFIX]

TITLE (optional small top): "Scare Tactics? Document First."

CENTER: Large spiral-bound notepad, cream paper, thick glowing cyan border, three rows with icons:
- Camera icon: "Screenshot file Properties / Get Info"
- Checklist icon: "Write path + timestamps in inventory"
- Amber warning triangle (small): "Do NOT open or delete yet"

LEFT COLUMN — "Why fear happens" with arrow bullets:
→ Future timestamps
→ Weird names
→ Personalized files

RIGHT COLUMN — "What enables next" with arrow bullets:
→ Evidence for pros
→ Calm LLM analysis
→ Clear escalation

MASCOT: Raccoon, tactical vest, goggles on forehead, pointing at notepad.

BOTTOM CENTER: "Panic destroys evidence → Calm wins"
BOTTOM RIGHT: small generic Windows · macOS · Linux icons in cyan (no trademark abuse)
```


## Prompt 04 — LLM Co-Pilot Flow (reprompt — Squirrel)

**File:** `LLM-Co-Pilot-Flow.jpg`  
**Ratio:** 16:9  
**Mascot:** **Squirrel** (replaces Raccoon on current file)  
**Status:** Shipped

```
[STYLE PREFIX]

TITLE: "How to Use Your LLM Safely"
Thin cyan underline below title.

HORIZONTAL 3-STEP FLOW (cyan numbered circles, arrows 1→2→3):

STEP 1 — document icon with refresh arrow
"Copy entire framework file (Minimal Tools recommended)"
Example box: Example: "Copy the Minimal Tools framework file for review."

STEP 2 — overlapping chat bubbles icon
"Paste into chat + describe situation + 'Start Phase 0'"
Example box: Example: "I found a suspicious file. Start Phase 0."

STEP 3 — document + gear + LOG tag
"End session — 'Append Session Summary to my log'"
Example box: Example: "End session — Append Session Summary to my log."

RIGHT SIDE: Large squirrel mascot in dark green tactical jacket, holding mug or framework scroll, calm expression.

LOWER RIGHT BOX (cyan border): "Works with" + checkmark + generic icons for Grok · Claude · ChatGPT · Ollama (no official logos if tool blocks them — use abstract chat icons).

BOTTOM BANNER (dark orange-brown parchment strip): amber triangle + "LLM explains · You document · Tools verify"
```

---

## Prompt 05 — When to Escalate

**File:** `When-to-Escalate.jpg`  
**Ratio:** 9:16 (vertical ladder) or 3:4  
**Mascot:** Owl beside ladder (small — criteria text dominates)  
**Status:** Shipped — **verify every label** against `Infograph_When-to-Escalate.svg`

```
[STYLE PREFIX]

TITLE: "When to Escalate"

VERTICAL DECISION LADDER (parchment background, dark panels for questions, cyan arrows down):

START: "Review your findings"

Q1 diamond: "Data theft, financial loss, or ransomware?"
→ YES: "Escalate immediately — prepare evidence package"
→ NO: continue down

Q2: "Confirmed persistence + ongoing network beaconing?"
→ YES: "Escalate — strong recommendation"

Q3: "Personally targeted or feel unsafe?"
→ YES: "Escalate"

Q4: "Multiple future-timestamp files + suspicious scripts + odd network?"
→ YES: "Consider escalating"

Q5: "Still unsure after reviewing everything?"
→ YES: "Escalate — better safe than sorry"
→ NO: "Continue light monitoring"

END BOX: "Prepare package → Choosing Professional Help"

MASCOT: Owl in tactical vest, perched beside Q2–Q3, reading glasses optional.

FOOTER: "Panic destroys evidence → Calm wins"

CRITICAL: If text garbles, regenerate or use SVG; do not paraphrase criteria.
attached files are for style reference
```

---

## Prompt 06 — Your Evidence Package

**File:** `Your-Evidence-Package.jpg`  
**Ratio:** 16:9  
**Mascot:** Raccoon holding or gesturing to manila folder  
**Status:** Shipped

```
[STYLE PREFIX]

TITLE: "Your Evidence Package"

CENTER: Manila folder labeled "Investigation_YYYY-MM-DD" with five items with cyan icons:

1. investigation_log.md — "Running notes"
2. suspicious_files_inventory.md — "File list + timestamps"
3. screenshots/ — "Properties + scan results"
4. network_captures/ — "Wireshark / tcpdump files"
5. summary_for_professionals.md — "One-page handoff"

RIGHT: Arrow to simple icons — "IR firm · Law enforcement · Trusted IT"

MASCOT: Raccoon, tactical vest, presenting folder.

SUBTITLE: "You already did the hard part"

FOOTER: "Document first · Not legal advice"
attached files are for style reference
```

---

## Prompt 07 — Summary for Professionals

**File:** `Summary-for-Professionals.jpg`  
**Ratio:** 3:4  
**Mascot:** Fox (right edge, overlapping parchment)  
**Status:** Shipped

```
[STYLE PREFIX]

TITLE: "Summary for Professionals — 1 Page"

TOP RIGHT SEAL (cyan glow): "Facts only · Label uncertainty"

TWO-COLUMN form layout on parchment:

LEFT:
- SITUATION — lined box
- KEY FINDINGS — 4 bullet lines
- TIMELINE — table columns: TIME | EVENT / MILESTONE | NOTES (3 empty rows)

RIGHT:
- EVIDENCE LIST — 5 checkboxes with lines
- QUESTIONS FOR YOU — lined box

MASCOT: Fox, orange fur, tactical vest patch "DEFEND ONLY", professional stance.

BOTTOM: "Template in Start-Guide"
attached files are for style reference
```

---

## Prompt 08 — Week 1 Stabilize

**File:** `Week-1-Stabilize.jpg`
**Ratio:** 3:4 or 9:16  
**Mascot:** Badger (right, facing checklist)  
**Status:** Shipped

```
[STYLE PREFIX]

TITLE: "Week 1 — Stabilize"
Gold leaf ornaments flanking title (subtle).

FIVE checklist rows — light beige panels, cyan glow borders, empty checkbox left, icon right:

☐ Email + banking — 2FA (envelope + padlock)
☐ Update OS + browser (refresh arrows)
☐ Router device list review (router icon)
☐ Block / mute / document on social (shield + document)
☐ Weekly light check — keep logging (calendar + gear)

MASCOT: Badger, black-and-white face, dark teal tactical vest, serious calm expression.

FOOTER: "Defense not retaliation · Own systems only"
attached files are for style reference
```

---

## Prompt 09 — Platform Safety

**File:** `Platform-Safety.jpg`  
**Ratio:** 1:1 or 16:9  
**Mascot:** Fox with tablet  
**Status:** Shipped

```
[STYLE PREFIX]

TITLE: "Social Media Platform Safety"
RIBBON below title: "— Defensive Only —"

CENTER: Generic browser window mockup (beige frame), glowing cyan @ symbol in circle, abstract feed UI — no official X logo required.

FOUR action buttons (cyan glow rectangles):
BLOCK (shield) · MUTE (muted speaker) · REPORT (flag) · SCREENSHOT + TIMESTAMP (camera + clock)

CROSSED OUT center text with X marks: "Engage · Dox · Hack back"

MASCOT: Fox, tactical vest "DEFEND ONLY", holding tablet beside browser.

FOOTER: "Document for LE · Don't feed the scare campaign"
attached files are for style reference
```

---

## Prompt 10 — Block and Harden Grid

**File:** `Block-and-Harden-Grid.jpg`  
**Ratio:** 1:1 or 16:9  
**Mascot:** Badger header + one specialist per quadrant  
**Status:** Shipped
**Guide:** `defense/Block-and-Harden.md`

```
[STYLE PREFIX]

TITLE: "Block & Harden Without Panic"

TOP: Badger mascot banner — "After documentation · Own systems only"

2×2 GRID of dark panels with cyan borders:

QUADRANT 1 — NETWORK (Beaver, small corner inset)
Router icon · "Update firmware · Review devices · WPA2/WPA3"
Subtitle: "Network edge"

QUADRANT 2 — ACCOUNTS (Hedgehog inset)
Padlock icon · "2FA on clean device · Rotate passwords"
Subtitle: "Credentials"

QUADRANT 3 — PLATFORM (Fox inset)
Speech bubble icon · "Block · Mute · Report · Screenshot first"
Subtitle: "Social platforms"

QUADRANT 4 — DEVICE (Turtle inset)
Laptop + refresh icon · "OS + browser updates · Antivirus current"
Subtitle: "This device"

CENTER OVERLAY (small): "Document → Comprehension gate → Escalate check → Then harden"

FOOTER: "Defense not retaliation · Own systems only"
attached files are for style reference
```

---

## Prompt 11 — Safe Removal After Documentation

**File:** `Safe-Removal.jpg`  
**Ratio:** 3:4  
**Mascot:** Toad (primary)  
**Guide:** `defense/Safe-Removal-After-Documentation.md`

```
[STYLE PREFIX]

TITLE: "Safe Removal — After Documentation"

THREE-STEP horizontal flow:

1. DOCUMENT COMPLETE — checkmark on folder — "Log + inventory + screenshots saved"
2. QUARANTINE — amber box icon — "Move to isolated folder · Do not delete originals yet"
3. VERIFY — shield — "Rescan · Note hash/path in log"

MASCOT: Toad in tactical vest beside step 2 — calm "purify don't panic-delete" posture.

CALLOUT: "Never wipe before professionals advise if escalation criteria met"

FOOTER: "Defense not retaliation · Own systems only"
attached files are for style reference
```

---

## Prompt 12 — Forensic Image Decision

**File:** `Forensic-Image.jpg`  
**Ratio:** 1:1  
**Mascot:** Mole (disk/deep evidence)  
**Guide:** `Start-Guide/How-to-Create-a-Forensic-Image.md`

```
[STYLE PREFIX]

TITLE: "Forensic Image — DIY or Professional?"

SPLIT LAYOUT:

LEFT PANEL (larger): "Contact professionals first"
Bullets: ransomware · financial loss · law enforcement involved · sophisticated malware

RIGHT PANEL (smaller): "Limited DIY only if"
Bullets: low stakes · external drive · hash logged · professional unavailable

CENTER: amber stop triangle — "Never wipe before documentation"

BOTTOM: drive → external drive arrow — "Bit-copy + SHA-256 log"

MASCOT: Mole with tactical vest, gentle underground/cross-section motif (not scary).

FOOTER: "Document first · Not legal advice"
attached files are for style reference
```

---

## Prompt 13 — Choosing Professional Help

**File:** `Choosing-Professional-Help.jpg`  
**Ratio:** 16:9  
**Mascot:** Deer at path fork; small Owl silhouette optional  
**Guide:** `Start-Guide/Choosing-the-Right-Professional-Help.md`

```
[STYLE PREFIX]

TITLE: "Choosing the Right Professional Help"

FOUR-PATH fork diagram (cyan arrows):

PATH 1: Bank / financial institutions — "Unauthorized transactions"
PATH 2: Incident response / forensics — "Ransomware · data theft"
PATH 3: Law enforcement / IC3 — "Stalking · targeted harassment"
PATH 4: Trusted IT consultant — "Second opinion · triage"

CENTER: "Bring evidence package + professional summary"

MASCOT: Deer, alert but calm, at the fork.

FOOTER: "Panic destroys evidence → Calm wins"
attached files are for style reference
```

---

## Prompt 14 — After-Incident Recovery

**File:** `After-Incident-Recovery.jpg`  
**Ratio:** 3:4  
**Mascot:** Otter  
**Guide:** `Start-Guide/Protecting-Yourself-After-an-Incident.md`

```
[STYLE PREFIX]

TITLE: "Protecting Yourself After an Incident"

CHECKLIST cards:
☐ Keep logging new activity
☐ Do not delete unless professionals instruct
☐ Passwords + 2FA on clean device
☐ Emotional check-in — ask for support
☐ Review Week 1 stabilize checklist

MASCOT: Otter, tactical vest, calm supportive pose (flow/recovery — not playful game splash).

FOOTER: "Defense not retaliation · Own systems only"
attached files are for style reference
```

---

## Prompt 15 — Law Enforcement Expectations

**File:** `Law-Enforcement-Expectations.jpg`  
**Ratio:** 16:9  
**Mascot:** Fox (communications)  
**Guide:** `Start-Guide/What-to-Expect-When-Working-with-Law-Enforcement.md`

```
[STYLE PREFIX]

TITLE: "Reporting Cyber Harassment — What to Expect"

FOUR horizontal panels (icon-only, no photorealistic faces):

1. Phone — "Non-emergency line or IC3 report"
2. USB folder — "Organized evidence package"
3. Clock — "Investigations take time"
4. Shield — "Preserve devices · Do not wipe"

MASCOT: Fox, small corner, professional summary document prop.

DISCLAIMER BAR: "Not legal advice · Procedures vary by location"
No official police badges or seals implying endorsement.
attached files are for style reference
```

---

## Prompt 16 — Breach Check Inventory (optional web sidebar)

**File:** `Breach-Check-Inventory.jpg`  
**Ratio:** 3:4  
**Mascot:** Chipmunk (small)  
**Status:** Optional — plain prose preferred on web hub; no Chart.js

```
[STYLE PREFIX]

TITLE: "Breach Check — What to Log"

SIMPLE list graphic:
☐ Email/account checked (haveibeenpwned or provider notice)
☐ Date checked
☐ Exposure type (email · password · phone) — label uncertainty
☐ Action taken (password reset · 2FA · monitor)

SIDEBAR note: "k-anonymity prefix search · Do not paste live passwords"

MASCOT: Chipmunk with clipboard, small.

FOOTER: "Document first · Not legal advice"
attached files are for style reference
```

---

## Generation status

**All 16 prompts shipped** (2026-06-27). Gallery wired in `web/index.html`, `README.md`, and `Infographs/README.md`.

Regenerate only if copy changes or JPG text garbles (use `Infograph_When-to-Escalate.svg` for escalate labels).

---

## Maintenance (after copy changes)
1. Update `web/index.html` gallery alt text if labels change  
2. Update `README.md` Visual section  
3. Keep legacy drafts in `Archived/` — not style authority

**Related docs:** `Agents-Designs-Ideas/Interwoven_Field-Team_Mascot-Assignment_Plan_v1.0.md` (v1.2)

---

SquirrelUser-SQT: Year 1, Canopy | Thicket | 35:32:56 | All Infograph Photos Generated — v2 gallery shipped 2026-06-27  
---==[🐿️]==---

*End of Visual Prompts v2*