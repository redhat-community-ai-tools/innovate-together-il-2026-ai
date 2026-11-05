---
name: innovate-together-il-ai
description: >-
  Matches a user's project to Innovate Together Israel 2026 AI-track talks,
  repos, contribution paths, and Red Hat product docs; also produces briefs
  for the whole AI track or specific sessions. Use when the user mentions
  Innovate Together, OpenShift Commons Israel, the AI track takeaway pack,
  conference follow-ups, event/session briefs, or asks what to implement
  from those sessions.
---

# Innovate Together IL 2026 — AI Track

Markdown-only conference takeaway skill. Read [TRUST.md](../../TRUST.md) if the user asks about security.

## Modes

Pick the mode from the request (ask once if ambiguous):

| Mode | When | Source |
|------|------|--------|
| **Project match** | User wants ideas for *their* stack / repo | agenda → talk files + products |
| **Event brief** | Brief on the whole AI track / day | [agenda.md](references/agenda.md) + skim talk files as needed |
| **Session brief** | Brief on one or more named talks | matching [talks/](references/talks/) files |

## Instructions

1. **Orient** — For project match: if goal/stack is unclear, ask briefly (platform, AI use case, constraints). Prefer repo context when already in a project. For briefs: confirm whole track vs which session titles/times.
2. **Load references** — Always start from [references/agenda.md](references/agenda.md). Read the relevant [references/talks/](references/talks/) files. Use [references/products.md](references/products.md) and [references/speakers.md](references/speakers.md) when citing docs or people.
3. **Project match** — Prefer **1–2 high-signal talks** that directly answer the ask. Add a third only if it adds a distinct lever (not a soft “framing” talk like keynote / AI Ready when two deep talks already cover cost, harness, packaging, etc.). For each: why it fits, borrow ideas, try-next, repos/docs, contribution paths.
4. **Event brief** — Short overview: theme of the day, morning vs track, 1–2 sentences per talk. End with “if you only attend three…”:
   - If the user named a priority, pick **those three first** for that goal.
   - Then optionally list other buckets (cost, agents/harness, production OpenShift AI, security/confidential).
5. **Session brief** — One block per requested talk (shared one-line preamble OK if several). Include: title, time, speakers; **LinkedIn/GitHub when present in speakers.md** (never invent); summary; takeaways; repos/docs; contribute; slide status.
6. **Stub protocol** — If a talk file marks materials pending / guest stub / speaker not yet named:
   - Say so up front; give **“what to listen for”** only as provisional themes.
   - Do **not** invent benchmarks, product names, customer metrics, or repos.
   - Omit empty **Contribute** sections (or write “none until materials land”).
   - Prefer platform docs already listed (e.g. OpenShift AI) as context only.
7. **Not sales** — Soft docs links only; commercial contact → https://www.redhat.com/en/contact.

## Response shapes

### Project match

```markdown
## Relevant talks
### [Title] — why it fits
- Borrow: …
- Try: …
- Repos / docs: …
- Contribute: …

## Suggested next step
One concrete action they can take this week.
```

### Event brief

```markdown
## AI track at a glance
[2–4 sentences on the day]

## Sessions
- **HH:MM — Title** (speakers): one-line takeaway
…

## If you only pick three
[If user stated a goal — lead with that]
- <their goal>: talk A; talk B; talk C

[Optional other buckets]
- Cost / inference: …
- Agents / harness: …
- Production OpenShift AI: …
- Security / confidential: …
```

### Session brief (one or many)

```markdown
## Brief: [talk titles or “AI track sessions”]

### [Title]
- When / who: … | LinkedIn: <url or —> | GitHub: <url or —>
- Summary: …
- Takeaways: …   # or “What to listen for” if stub
- Repos / docs: …
- Contribute: …  # omit if stub / none yet
- Slides: available | pending
```

## Additional resources

- Agenda: [references/agenda.md](references/agenda.md)
- Products: [references/products.md](references/products.md)
- Speakers: [references/speakers.md](references/speakers.md)
