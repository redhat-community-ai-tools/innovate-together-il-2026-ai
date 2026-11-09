---
layout: default
title: Agent skill handoff
---

# Agent skill — what it is and how to share it

## Who this is for

**You (non-engineer / manager):** share this page + the repo link with developers.

**Developers:** install the skill in Cursor, Claude Code, or Codex so the agent can answer “what from the AI track applies to *our* repo?”

## What it’s good for

- Matching your project to the right talks
- Briefing the whole AI track or specific sessions (for people who missed talks or need a quick recap)
- Finding open-source repos and contribution paths from the sessions
- Linking official Red Hat product documentation (not a sales pitch)
- Grounding follow-up work in abstracts and (when in-pack) slide outlines; partner/customer decks may never be in the pack

## Security (read this)

The skill is **markdown only** — no scripts, hooks, or MCP servers. Review TRUST.md before installing:

- [TRUST.md on GitLab](https://gitlab.cee.redhat.com/qe-ds/innovate-together-il-2026-ai/-/blob/main/TRUST.md)
- [TRUST.md on GitHub](https://github.com/redhat-community-ai-tools/innovate-together-il-2026-ai/blob/main/TRUST.md)

## 3-step handoff to a developer

1. Send them a repo link (whichever is available to them):
   - Internal: https://gitlab.cee.redhat.com/qe-ds/innovate-together-il-2026-ai
   - Public: https://github.com/redhat-community-ai-tools/innovate-together-il-2026-ai  
   and the README install section ([GitLab](https://gitlab.cee.redhat.com/qe-ds/innovate-together-il-2026-ai/-/blob/main/README.md#install-the-skill) · [GitHub](https://github.com/redhat-community-ai-tools/innovate-together-il-2026-ai#install-the-skill)).
2. Ask them to read `TRUST.md`, then follow install steps in the README (symlink for Cursor/Codex, or Claude plugin marketplace from the GitHub URL when published).
3. In their agent chat: *“Using the Innovate Together IL AI skill, look at this repo and suggest which talks and projects we should borrow from.”*

## Install (short)

**GitLab (internal):**

```bash
git clone git@gitlab.cee.redhat.com:qe-ds/innovate-together-il-2026-ai.git
cd innovate-together-il-2026-ai
```

**GitHub (public):**

```bash
git clone https://github.com/redhat-community-ai-tools/innovate-together-il-2026-ai.git
cd innovate-together-il-2026-ai
```

Then symlink (either clone):

```bash
# Cursor (project)
mkdir -p /path/to/project/.cursor/skills
ln -s "$(pwd)/skills/innovate-together-il-ai" \
  /path/to/project/.cursor/skills/innovate-together-il-ai

# Codex / Agent Skills path
mkdir -p /path/to/project/.agents/skills
ln -s "$(pwd)/skills/innovate-together-il-ai" \
  /path/to/project/.agents/skills/innovate-together-il-ai

# Claude Code (GitHub marketplace URL when the public repo is live)
claude plugin marketplace add https://github.com/redhat-community-ai-tools/innovate-together-il-2026-ai
claude plugin install innovate-together-il-ai
```

Full details: [Install on GitLab README](https://gitlab.cee.redhat.com/qe-ds/innovate-together-il-2026-ai/-/blob/main/README.md#install-the-skill) · [Install on GitHub README](https://github.com/redhat-community-ai-tools/innovate-together-il-2026-ai#install-the-skill).

[← Back to agenda](index.md)
