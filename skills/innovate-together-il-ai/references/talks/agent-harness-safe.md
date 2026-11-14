# Is Your AI Agent Harness Safe?

- **Time:** 11:35 (20 min)
- **Speakers:** Benjamin Kapner (Data Scientist, Red Hat)
- **Materials:** slides-in-pack
- **Full title:** Is Your AI Agent Harness Safe? Finding Defects in Skills, Hooks, and MCPs Before Agents Merge on Their Own

## Abstract

Teams using Claude Code, Cursor, Copilot, Gemini CLI, Codex CLI, and similar tools commit harness config: skills, hooks, MCP servers, and instruction files that decide what the agent may read, run, and send. Misconfiguration can leak credentials or trigger unintended actions. This talk covers a two-layer methodology: deterministic static analysis across the harness as a graph, then LLM review. Walkthrough of **harness-eval**, findings from thousands of public repos, and a path toward evidence-based agent merge permission (checked harness as first evidence).

## Outline (from deck)

1. **Audience** — full ADLC and people new to Claude Code / Codex / Cursor
2. **Why evaluate the harness** — same model, different results; setup bugs are silent; harness *is* code (shell, files, network) that often reviews as “just markdown/JSON”
3. **Marketplace risk signal** — large skill samples with non-trivial vulnerability / likely-malicious rates (speaker-cited study)
4. **Attack / failure surfaces** — unpinned `npx` MCPs; marketplace skills with scripts; committed `settings.json`; instruction files (`AGENTS.md` / rules) including hidden Unicode / dependency-written prompts (NVIDIA AI Red Team / Pillar examples)
5. **Concrete fail modes** — contradictory allow/deny shell grants; `defaultMode: bypassPermissions`; `enableAllProjectMcpServers`; repo-level `ANTHROPIC_BASE_URL` / API key exfil; cross-assistant MCP version skew
6. **Cross-component bugs** — conflicting skills (“comment every line” vs “never comment”); skill A → skill B instruction loops
7. **Why review misses it** — invisible Unicode; prose skipped by reviewers; non-engineers approving installs
8. **harness-eval** — auto-detect assistants, one component graph, ~92 rules; commands: `harness-autonomy`, `harness-gate`, `harness-security`, `harness-lint`, `harness-review`; CLI, GitHub Action/SARIF, pre-commit, Cursor/Claude plugins, Tekton / OpenShift Pipelines
9. **Goal** — evidence-based merge permission: checked harness as first evidence before agents merge on their own

## Takeaways to borrow

- Treat skills/hooks/MCPs as security-sensitive code, not docs
- Lint the harness as a **graph** (cross-file flows), not file-by-file only
- Pin MCP packages; never commit API keys or proxy base URLs in project settings
- Gate merges on validated rules; keep human authority reclaimable

## Repos & docs

- **harness-eval:** https://github.com/redhat-community-ai-tools/harness-eval
- Claude/Cursor install options documented in that repo
- Related community: https://github.com/redhat-community-ai-tools

## Contribution opportunities

- Add lint/security rules via harness-eval PRs
- Run `uvx harness-eval harness-security .` on your org’s agent configs and file issues for false positives / new patterns
- Contribute fixtures from real (sanitized) harness defects

## Try this in your environment

```bash
uvx harness-eval harness-security .
uvx harness-eval harness-lint .
uvx harness-eval harness-autonomy .
```

Ask: “Scan this repo’s agent harness and prioritize the top security findings with fixes.”
