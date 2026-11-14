# Is Your AI Agent Harness Safe?

- **Time:** 11:35 (20 min)
- **Speakers:** Benjamin Kapner (Data Scientist, Red Hat)
- **Materials:** slides-in-pack
- **Full title:** Is Your AI Agent Harness Safe? Finding Defects in Skills, Hooks, and MCPs Before Agents Merge on Their Own
- **Note:** Deck in organizer [AI-track Drive](https://drive.google.com/drive/folders/1vYeadTnV85-fCSKPqBV7fagq-IpStKGl) (access-controlled).

## Abstract

Teams using Claude Code, Cursor, Copilot, Gemini CLI, Codex CLI, and similar tools commit harness config: skills, hooks, MCP servers, and instruction files that decide what the agent may read, run, and send. Misconfiguration can leak credentials or trigger unintended actions. This talk covers a two-layer methodology: deterministic static analysis across the harness as a graph, then LLM review. Walkthrough of **harness-eval**, findings from thousands of public repos, and a path toward evidence-based agent merge permission (checked harness as first evidence).

## Takeaways to borrow

- Treat skills/hooks/MCPs as security-sensitive code, not docs
- Lint the harness as a whole (cross-file flows), not file-by-file only
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
```

Ask: “Scan this repo’s agent harness and prioritize the top security findings with fixes.”
