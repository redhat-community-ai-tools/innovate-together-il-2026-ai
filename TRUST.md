# Trust & security

This repository is a **markdown-only knowledge pack** for Innovate Together Israel 2026 (AI and Infrastructure tracks). Read this before installing a skill in any coding agent.

## What this pack is

- Public talk summaries, abstracts, product documentation links, and open-source repo links
- Agent skills that help match *your* project context to conference takeaways
- A human-readable GitHub Pages agenda for sharing with non-engineers

## What this pack is NOT

- It does **not** include executable scripts, hooks, MCP servers, or installers that run on your machine
- It does **not** phone home, collect telemetry, or require credentials
- It does **not** grant the agent new network or shell powers beyond what your agent already has
- It is **not** a sales pitch or account-team playbook — but if you like what you see, you are welcome to [contact Red Hat](https://www.redhat.com/en/contact)

## Official source

Prefer content only from this open-source org repository:

`https://github.com/redhat-community-ai-tools/innovate-together-il-2026-ai`

Do not install forks or third-party mirrors without reviewing the full diff. Prefer a tagged release over floating `main` once tags exist.

## Before you enable the skill

1. Skim `skills/innovate-together-il-ai/` and/or `skills/innovate-together-il-infra/` — especially `SKILL.md` and `references/`.
2. Confirm there are no `scripts/`, hook configs, or MCP manifests in this repo.
3. Optionally scan with [harness-eval](https://github.com/redhat-community-ai-tools/harness-eval):

```bash
uvx harness-eval harness-security skills/
```

## What the agent may do after install

Once enabled, your coding agent may *read* these markdown files and use them with the project context you already opened. The skill does not inject secrets. Treat agent output as advice — verify before changing production systems.

## Presenter contact

Speaker LinkedIn/GitHub links appear only when the speaker opted in (`references/speakers.md`). The skill must not invent emails or private contact details.

## Report a problem

Open an issue on the official GitHub repository if you find unexpected executable content or malicious instructions.
