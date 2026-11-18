# 04 — Session brief: harness-eval talk

Tags: `happy` `multi-mode`

## Question

> Using the Innovate Together IL AI skill, brief me on the harness-eval / agent harness safety talk: summary, takeaways, and how to try it afterward.

## Skill response

## Brief: Is Your AI Agent Harness Safe?

### Is Your AI Agent Harness Safe?

- **When / who:** 11:35 (20 min) — Benjamin Kapner (Red Hat) | LinkedIn: https://www.linkedin.com/in/benjamin-kapner-ba75a11b5/ | GitHub: —
- **Summary:** Teams commit skills, hooks, MCP servers, and instruction files that decide what agents may read, run, and send. Misconfiguration can leak credentials or trigger unintended actions. Two-layer assessment (deterministic harness-wide static analysis, then LLM review) via open-source **harness-eval**; findings from large public-repo scans; checked harness as early evidence toward controlled agent merge permission.
- **Takeaways:** Treat harness as security-sensitive code; analyze cross-file flows; gate on validated rules; keep human authority reclaimable.
- **Repos / docs:** https://github.com/redhat-community-ai-tools/harness-eval
- **Contribute:** Rules, fixtures, false-positive reports, PRs.
- **Try afterward:**
  ```bash
  uvx harness-eval harness-security .
  uvx harness-eval harness-lint .
  ```
- **Materials:** slides-in-pack (outline in the talk file; no downloadable deck in this repo)

## Evaluation

| Criterion | Result | Notes |
|-----------|--------|-------|
| Correct mode | Pass | |
| LinkedIn from speakers.md | Pass | |
| Shape (new template) | Pass | |
| Materials honesty | Pass | slides-in-pack; outline cited, no invented claims |

**Verdict: good (pass)**

## Live agent delta

- Date / agent: 2026-11-05 / Cursor (Composer)
- Drift vs hand-authored: Negligible — LinkedIn from speakers.md; slides pending; uvx try path present.
- Re-eval verdict: **pass**
- Full live text: [live-runs/2026-11-05-cursor.md](live-runs/2026-11-05-cursor.md#q04--session-brief-harness)
