# Local skill eval

Manual / agent-assisted checks of both skills, plus a runnable structural smoke check.

New scenario files (gitignored by default): `git add -f testing/<file>`.

## Runnable check

```bash
python3 testing/smoke_check.py
```

## Tags

| Tag | Meaning |
|-----|---------|
| `happy` | Full materials; expect dense, actionable answer |
| `stub-honesty` | Guest/partner or pending content; must not invent claims; no “until slides land” for `slides-not-in-pack` |
| `framing` | Must keep talk intent (e.g. RH-for-customers vs DIY) |
| `multi-mode` | Exercises event or session brief shapes |
| `anti-example` | Documented *bad* response (fail bar) |

## Layout

### AI skill

| File | Tags | Mode |
|------|------|------|
| [01-project-gpu-cost.md](01-project-gpu-cost.md) | `happy` | Project match |
| [02-project-agent-harness.md](02-project-agent-harness.md) | `happy` | Project match |
| [03-event-brief.md](03-event-brief.md) | `happy` `multi-mode` | Event brief |
| [04-session-brief-harness.md](04-session-brief-harness.md) | `happy` `multi-mode` | Session brief |
| [05-session-stub-honesty.md](05-session-stub-honesty.md) | `stub-honesty` `multi-mode` | Session brief |
| [06-project-confidential.md](06-project-confidential.md) | `happy` | Project match |
| [07-anti-example-fail.md](07-anti-example-fail.md) | `anti-example` `stub-honesty` | Fail bar |
| [08-session-packaging-framing.md](08-session-packaging-framing.md) | `happy` `multi-mode` `framing` | Session brief |

### Infra skill

| File | Tags | Mode |
|------|------|------|
| [09-infra-project-virt-ha.md](09-infra-project-virt-ha.md) | `happy` | Project match |
| [10-infra-event-brief.md](10-infra-event-brief.md) | `happy` `multi-mode` | Event brief |
| [11-infra-session-mcp-vms.md](11-infra-session-mcp-vms.md) | `happy` `multi-mode` | Session brief |
| [12-infra-stub-ansible-pending.md](12-infra-stub-ansible-pending.md) | `stub-honesty` `multi-mode` | Session brief |

Each file: **Question** → **Skill response** → **Evaluation** → **Live agent delta** (fill after a real Cursor/Claude/Codex run with the skill installed).

## Rubric (pass / fail / mixed)

- Correct mode selected
- Used agenda/talk files; no invented guest/customer claims
- Speakers: LinkedIn/GitHub only if in `speakers.md`
- Project match: prefer 1–2 deep talks over weak framing fillers
- Event brief: user’s stated goal leads “only three” when present
- Stubs / `slides-not-in-pack`: “what to listen for”; no empty fake contribute/repos; never “until slides land”
- Packaging/gating talk: RH validates for customers — not a DIY ModelCar workshop
- Not a sales pitch
- Response shape roughly matches `SKILL.md`
