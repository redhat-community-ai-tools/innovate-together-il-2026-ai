# 02 — Project match: agent harness safety

Tags: `happy`

## Question

> We commit Cursor skills and MCP configs in our monorepo. Using the Innovate Together IL AI skill, what should we adopt from the conference, and how do we contribute back?

## Skill response

## Relevant talks

### Is Your AI Agent Harness Safe? — why it fits
- **Borrow:** Treat skills/hooks/MCPs as security-sensitive code; lint the harness as a graph; gate merges on validated rules with reclaimable human authority.
- **Try:**
  ```bash
  uvx harness-eval harness-security .
  uvx harness-eval harness-lint .
  ```
- **Repos / docs:** [harness-eval](https://github.com/redhat-community-ai-tools/harness-eval)
- **Contribute:** Rules, sanitized fixtures, false-positive reports, PRs.

### Leveraging Sandboxing and Confidential Computing for Agents and Models — why it fits
- **Borrow:** Sandbox untrusted agent-generated code (Kata / agent-sandbox patterns) separately from confidential inference.
- **Try:** Inventory where agent tool calls execute shell today; mark sandbox candidates.
- **Repos / docs:** [Kata](https://katacontainers.io/), [Confidential Containers](https://confidentialcontainers.org/), [KServe](https://kserve.github.io/website/)
- **Contribute:** Upstream issues once speaker materials confirm exact agent-sandbox repos.

## Suggested next step

Run `harness-eval` on the monorepo harness, triage critical security findings, open one upstream issue or PR with a sanitized repro.

## Evaluation

| Criterion | Result | Notes |
|-----------|--------|-------|
| Correct mode | Pass | |
| Talk selection | Pass | 2 talks, both high-signal |
| Contribution path | Pass | |
| Shape | Pass | |

**Verdict: good (pass)**

## Live agent delta

- Date / agent: 2026-11-05 / Cursor (Composer)
- Drift vs hand-authored: Negligible — harness-eval + sandboxing; same commands and contribute path.
- Re-eval verdict: **pass**
- Full live text: [live-runs/2026-11-05-cursor.md](live-runs/2026-11-05-cursor.md#q02--project-match-harness)
