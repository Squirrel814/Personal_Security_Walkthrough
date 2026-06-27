## File Structure Map

Personal_Security_Walkthrough/
├── README.md                    ← DONE (Phase 3) — v2 Visual table 2026-06-27
├── LICENSE                      ← DONE (dual CC-BY-SA + MIT)
├── CONTRIBUTING.md              ← DONE (Phase 3)
├── Infographs/                  ← v2 art + VISUAL-PROMPTS_v2.md + README.md
│   └── Archived/                ← not style authority
├── minimal-tools/
│   ├── windows/
│   │   └── My_Security_Framework_Windows-OS_v1.1_Minimal_Tools.md
│   ├── macos/
│   │   └── My_Security_Framework_macOS_v1.1_Minimal_Tools.md
│   └── linux/
│       └── My_Security_Framework_Linux_v1.1_Minimal_Tools.md
├── full-deep-dive/          
│   ├── windows/
│       └── My_Security_Framework_Windows-OS_v1.1_Full_Deep_Dive.md
│   ├── macos/ 
│       └── My_Security_Framework_macOS_v1.1_Full_Deep_Dive.md
│   └── linux/ 
│       └── My_Security_Framework_Linux_v1.1_Full_Deep_Dive.md
├── defense/                     ← Phase 5 DONE
├── tools/                       ← Phase 7 DONE
│   ├── scaffold_investigation_folder.py
│   ├── validate_walkthrough_links.py
│   └── blocklist_export_template.txt
├── .github/workflows/
│   └── validate-links.yml       ← Phase 7b CI (push + PR to main)
├── web/
│   ├── index.html               ← Phase 6b DONE 2026-06-27 (v2 hub)
│   ├── design-tokens.css
│   └── hub.css
├── Start-Guide/
		├── When-and-How_to-Escalate.md
		├── Quick-Start-Guide.md
		└── shared-templates/
			├── templates/
			│   ├── investigation_log_template.md
			│   └── suspicious_files_inventory.md
			└── examples/
				├── example_investigation_log.md
				└── example_suspicious_files_inventory.md


**Phase 4 complete (2026-06-27):**
- Escalate Mermaid flowchart + text + image prompt in `When-and-How_to-Escalate.md` (v1.2)
- `Choosing-the-Right-Professional-Help.md`
- `project_structure_recommendation.md` template

**Phase 4 companions (DONE 2026-06-27):**
- `How-to-Create-a-Forensic-Image.md`
- `What-to-Expect-When-Working-with-Law-Enforcement.md`
- `How-to-Prepare-a-Professional-Summary.md`
- `Protecting-Yourself-After-an-Incident.md`

**Phase 5 defense layer (DONE 2026-06-27):**
- `defense/Block-and-Harden.md`
- `defense/Safe-Removal-After-Documentation.md`
- `defense/Platform-Safety-X-and-Social.md`
- Source: `Personal-Security-Defense_CANONICAL.md` (Gemini) — Options A + C

**Phase 6a web hub (DONE 2026-06-27):**
- `web/index.html` — Option B from CANONICAL §7 (flat pastel v1)

**Phase 6b visual + web alignment (DONE 2026-06-27):**

| Task | Status | Owner |
|------|--------|-------|
| `Infographs/VISUAL-PROMPTS_v2.md` | ✅ DONE | Agent |
| `Infographs/README.md` inventory | ✅ DONE | Agent |
| `web/design-tokens.css` + `hub.css` | ✅ DONE | Agent |
| `web/index.html` v2 — gallery, escalate criteria, platform table, HIBP prose | ✅ DONE | Agent |
| `README.md` Visual section v2 | ✅ DONE | Agent |
| Mascot assignment plan v1.2 | ✅ DONE (Agents-Designs-Ideas) | Agent |
| Legacy root `Infograph_*` → `Archived/` | ✅ DONE | Agent |

**Phase 6c — v2 infograph gallery (DONE 2026-06-27):**

| Task | Status | Owner |
|------|--------|-------|
| All 16 v2 JPGs on disk | ✅ DONE | User |
| Full gallery in `web/index.html` (16 figures, roadmap table removed) | ✅ DONE | Agent |
| `README.md` + `Infographs/README.md` — complete inventory | ✅ DONE | Agent |
| `VISUAL-PROMPTS_v2.md` — all ✅ Shipped | ✅ DONE | Agent |
| Git push | ✅ This session | Agent |

**Phase 7 tools (DONE 2026-06-27):**
- `tools/scaffold_investigation_folder.py` — dated Investigation_YYYY-MM-DD/ on reader machine
- `tools/blocklist_export_template.txt` — Pi-hole / hosts format (linked from Block-and-Harden.md)
- `tools/validate_walkthrough_links.py` — internal link checker (stdlib Python)
- `.github/workflows/validate-links.yml` — runs validator on push/PR to main
- `tools/README.md`

**Phase 7b — CI / Pull Requests (DONE 2026-06-27):**

| What | Detail |
|------|--------|
| **PR** | Pull Request — proposed changes merged into `main` after review |
| **Workflow** | `.github/workflows/validate-links.yml` |
| **Triggers** | Every `pull_request` to `main` and every `push` to `main` |
| **Check** | `python tools/validate_walkthrough_links.py` must pass |
| **Contributor flow** | Fork → branch → PR → green check → merge (see CONTRIBUTING.md) |

**Deferred (not required for walkthrough):**
- Phase 6 curriculum — quiz + flashcards (`curriculum/`) — optional v2 community layer
- Personal Security Command Center app — future (gem Section 10)

**Next backlog:** Optional `export_blocklist.py`; link infographs from individual markdown guides as needed

**Back Burner for Full context/scope of project: **
README.md for the repo:
- Create a comparison table or visual showing key differences between Minimal Tools and Full Deep Dive versions across Windows, macOS, and Linux (great for the README).
- Link to "Quick-Start-Guide.md" - tracks and includes quick-start instructions for all platforms.
- Show how to use the templates + frameworks together.
- Organized folder structure for the repo with a basic .github/ folder structure (issue templates, etc.) optimized for an open-source personal safety project.

**LICENSE file:** (current recommendation: MIT or CC-BY-SA) 

**CONTRIBUTING.md:** for the open-source repo. located on Interwoven-Projects with the specific guidelines for the community policy.