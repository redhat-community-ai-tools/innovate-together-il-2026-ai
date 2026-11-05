# Local skill eval (gitignored)

Manual / agent-assisted checks of `skills/innovate-together-il-ai/`.

Listed in `.gitignore` so *new* local scratch stays private; the suite itself is force-added and tracked on GitLab. New scenario files: `git add -f testing/<file>`.

## Tags

| Tag | Meaning |
|-----|---------|
| `happy` | Full materials; expect dense, actionable answer |
| `stub-honesty` | Pending/guest content; must not invent claims |
| `multi-mode` | Exercises event or session brief shapes |
| `anti-example` | Documented *bad* response (fail bar) |

## Layout

| File | Tags | Mode |
|------|------|------|
| [01-project-gpu-cost.md](01-project-gpu-cost.md) | `happy` | Project match |
| [02-project-agent-harness.md](02-project-agent-harness.md) | `happy` | Project match |
| [03-event-brief.md](03-event-brief.md) | `happy` `multi-mode` | Event brief |
| [04-session-brief-harness.md](04-session-brief-harness.md) | `happy` `multi-mode` | Session brief |
| [05-session-stub-honesty.md](05-session-stub-honesty.md) | `stub-honesty` `multi-mode` | Session brief |
| [06-project-confidential.md](06-project-confidential.md) | `happy` | Project match |
| [07-anti-example-fail.md](07-anti-example-fail.md) | `anti-example` `stub-honesty` | Fail bar |

Each file: **Question** → **Skill response** → **Evaluation** → **Live agent delta** (fill after a real Cursor/Claude/Codex run with the skill installed).

## Rubric (pass / fail / mixed)

- Correct mode selected
- Used agenda/talk files; no invented guest/customer claims
- Speakers: LinkedIn/GitHub only if in `speakers.md`
- Project match: prefer 1–2 deep talks over weak framing fillers
- Event brief: user’s stated goal leads “only three” when present
- Stubs: “what to listen for”; no empty fake contribute/repos
- Not a sales pitch
- Response shape roughly matches `SKILL.md`
