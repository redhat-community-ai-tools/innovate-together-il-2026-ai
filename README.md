# Innovate Together IL 2026 — AI Track Takeaway Pack

Practical takeaways from the **AI track** at Innovate Together / OpenShift Commons Gathering Israel (**16 November 2026**).

Most conference talks leave you with slides and a vague “we should look into that.” This pack is different: install a **markdown-only** agent skill (Cursor, Claude Code, or Codex), describe your environment, and get concrete borrow ideas, open-source repos, contribution paths, and official Red Hat product docs tied to what you heard on stage.

**Non-engineers:** use the agenda site and share the [skill handoff](docs/skill.md) with your developers.

- **Internal (GitLab Pages):** https://qe-ds.pages.redhat.com/innovate-together-il-2026-ai — agenda site; install steps live in this README.
- **Public (GitHub Pages):** [redhat-community-ai-tools.github.io/innovate-together-il-2026-ai](https://redhat-community-ai-tools.github.io/innovate-together-il-2026-ai/) (live after the public GitHub publish).

## Security first

Read **[TRUST.md](TRUST.md)** before installing.

- Official source: this repository in the open-source org [redhat-community-ai-tools](https://github.com/redhat-community-ai-tools)
- **Markdown / reference content only** — no skill scripts, hooks, or MCP servers
- Review the skill tree; optionally scan with [harness-eval](https://github.com/redhat-community-ai-tools/harness-eval)

## Install the skill

Clone once:

```bash
git clone https://github.com/redhat-community-ai-tools/innovate-together-il-2026-ai.git
cd innovate-together-il-2026-ai
```

### Cursor

Project-scoped:

```bash
mkdir -p /path/to/your-project/.cursor/skills
ln -s "$(pwd)/skills/innovate-together-il-ai" \
  /path/to/your-project/.cursor/skills/innovate-together-il-ai
```

Personal (all projects):

```bash
mkdir -p ~/.cursor/skills
ln -s "$(pwd)/skills/innovate-together-il-ai" ~/.cursor/skills/innovate-together-il-ai
```

### Codex / Agent Skills path

```bash
mkdir -p /path/to/your-project/.agents/skills
ln -s "$(pwd)/skills/innovate-together-il-ai" \
  /path/to/your-project/.agents/skills/innovate-together-il-ai
```

### Claude Code

```bash
claude plugin marketplace add https://github.com/redhat-community-ai-tools/innovate-together-il-2026-ai
claude plugin install innovate-together-il-ai
```

## How to use it

After install, ask in your agent chat. Short examples:

**Match talks to your stack**

> Using the Innovate Together IL AI skill, look at this repo and suggest which conference talks and open-source projects I should borrow from. We run OpenShift on-prem and care about GPU cost.

**Agent harness safety**

> We commit Cursor skills and MCP configs. Using the Innovate Together IL AI skill, what should we adopt from the harness-eval talk, and how do we contribute back?

**Product docs for a use case**

> Using the Innovate Together IL AI skill: we need confidential inference for a regulated workload. Which talk, docs, and upstream projects apply?

**Brief on the whole AI track**

> Using the Innovate Together IL AI skill, give me a short brief on the entire AI track — what the day covers and which three sessions matter most if I care about production OpenShift AI.

**Brief on a specific session**

> Using the Innovate Together IL AI skill, brief me on the harness-eval / agent harness safety talk: summary, takeaways, and how to try it afterward.

The skill matches your context to talk notes under `skills/innovate-together-il-ai/references/` (project match, full-event brief, or session brief).

## What’s inside

| Path | Purpose |
|------|---------|
| `skills/innovate-together-il-ai/` | Agent skill + progressive-disclosure references |
| `docs/` | Human agenda site (GitHub Pages) |
| `TRUST.md` | Security / trust boundary |
| `CONTRIBUTING.md` | Speaker opt-in, slides, and link updates |

## Registration

Conference registration: [Red Hat Experiences](https://reg.experiences.redhat.com/flow/redhat/4804050/rhexpressregistrationapp/page/expressregistration)

## License

[Apache License 2.0](LICENSE)
