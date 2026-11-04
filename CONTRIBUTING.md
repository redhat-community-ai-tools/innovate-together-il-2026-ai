# Contributing

Thanks for helping keep the Innovate Together IL 2026 AI takeaway pack accurate and useful.

## Speaker opt-in (LinkedIn / GitHub)

By default we list **name + talk title only**. To add a public LinkedIn and/or GitHub profile:

1. Open a PR that updates `skills/innovate-together-il-ai/references/speakers.md`
2. Add only URLs you want published (no work email)
3. Mention your talk slug in the PR description

Or reply to the track lead with the exact URLs and they will land the PR for you.

## Adding / updating talk material

Preferred updates go in:

- `skills/innovate-together-il-ai/references/talks/<slug>.md` — canonical agent content
- `docs/talks/<slug>.md` — short human summary (keep in sync; do not fork long abstracts)

Useful additions:

- Public OSS repo links and “good first contribution” pointers
- Official product documentation URLs
- Slide **outline** as markdown (not large binaries)
- Link to a publicly shareable PDF/Drive file if the organizer publishes one

Presentation source folder (organizers): [Google Drive presentations](https://drive.google.com/drive/folders/1bnJ7cHjtxkkGpuU-oTxi6x0xfYfSGY4V)

## What not to add

- Work emails or private phone numbers
- Sales scripts, discount codes, or account-team playbooks
- Secrets, internal-only URLs, or customer-confidential case details without clearance
- Executable skill scripts, hooks, or MCP server configs

## Security review

PRs that touch `skills/` should stay markdown-only. CI runs harness-eval security checks when configured.

## License

Contributions are under the Apache License 2.0.
