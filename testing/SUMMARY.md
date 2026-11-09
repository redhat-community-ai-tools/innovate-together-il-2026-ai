# Eval summary (local)

| ID | Tags | Mode | Hand-authored | Live 2026-11-05 |
|----|------|------|---------------|-----------------|
| 01 | `happy` | Project match | pass | **pass** |
| 02 | `happy` | Project match | pass | **pass** |
| 03 | `happy` `multi-mode` | Event brief | pass | **pass** |
| 04 | `happy` `multi-mode` | Session brief | pass | **pass** |
| 05 | `stub-honesty` `multi-mode` | Session brief | pass (updated: slides-not-in-pack) | **pass** (prior); re-check wording |
| 06 | `happy` | Project match | pass | **pass** |
| 07 | `anti-example` | Fail bar | fail (intentional) | **avoided** |
| 08 | `happy` `framing` | Session brief | pass (hand-authored) | — pending |

**Live run:** [live-runs/2026-11-05-cursor.md](live-runs/2026-11-05-cursor.md)  
Agent: Cursor (Composer); skill loaded by following `SKILL.md` + `references/` in-session.

**Result:** 6/6 live passes on 2026-11-05 suite; anti-example failure modes avoided. Re-run 05 + new 08 after materials-status / packaging framing edits.

## Caveat

This live pass is the same agent family that wrote the fixtures. For an independent check, re-run 01–06 in a fresh Claude Code or Codex session with the skill installed and append another `live-runs/` file.
