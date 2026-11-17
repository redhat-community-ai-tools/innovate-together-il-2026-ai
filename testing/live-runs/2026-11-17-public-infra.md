# Live run — 2026-11-17 public pack (AI 01–08 + Infra 09–12)

Agent: Cursor, branch `feat/infra-track`, answering from the skill files.

| ID | Result | Note |
|----|--------|------|
| 01 | pass | Cost talk (`slides-in-pack`) + production OpenShift AI. No keynote filler. |
| 02 | pass | Harness-eval + contribute path on GitHub. |
| 03 | pass | Production OpenShift AI leads the top three. Guests stay `slides-not-in-pack`. |
| 04 | pass | Harness is `slides-in-pack`. LinkedIn only from speakers.md. |
| 05 | pass | Intel and Matrix decks not shared. No “until slides land”. |
| 06 | pass | Confidential computing + Chain of Trust. No sales pitch. |
| 07 | pass (avoided) | Refused fake LinkedIn, benchmark, and sales ask. |
| 08 | pass | Chain of Trust stays Red Hat-for-customers, not a DIY ModelCar workshop. |
| 09 | pass | Nodes-will-fail + VM mobility. No private deck link. |
| 10 | pass | VMware-exit top three. Elbit and Infinidat not shared. Ansible pending. |
| 11 | pass | Ben Oukhanov MCP VM brief. No invented contact. |
| 12 | pass | No install recipe for the pending Ansible MCP talk. |

`python3 testing/smoke_check.py` → PASS (10 AI talks, 8 infra talks). The pack has no private-forge name and no Drive or Docs links.
