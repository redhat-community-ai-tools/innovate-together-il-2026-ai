# Contributing

Thanks for helping keep the Innovate Together IL 2026 takeaway pack accurate and useful.

## Speaker opt-in (LinkedIn / GitHub)

By default we list **name + talk title only**. To add a public LinkedIn and/or GitHub profile:

1. Open a PR that updates the right speakers file:
   - AI / morning: `skills/innovate-together-il-ai/references/speakers.md`
   - Infrastructure: `skills/innovate-together-il-infra/references/speakers.md`
2. Add only URLs you want published (no work email)
3. Mention your talk slug in the PR description

Or reply to the track lead with the exact URLs and they will land the PR for you.

## Adding / updating talk material

Preferred updates go in:

- `skills/innovate-together-il-ai/references/talks/<slug>.md` or `skills/innovate-together-il-infra/references/talks/<slug>.md` — canonical agent content
- `docs/talks/<slug>.md` — short human summary (keep in sync; do not fork long abstracts)

Useful additions:

- Public OSS repo links and “good first contribution” pointers
- Official product documentation URLs
- Slide **outline / takeaways** as markdown in the talk file (preferred — skill users have no Drive access)
- A **public** shareable PDF/recording URL only if the speaker/organizer has published one for everyone

### Organizers (private Drive)

Do **not** put access-controlled Drive or agenda-sheet links in skill/docs PRs. Keep them in local gitignored `host-notes/slides-drive-index.md` (create the file from your organizer notes if missing). When a deck changes, update that index locally, then refresh the public talk `.md` outline/takeaways so skill users stay current without needing Drive.

## What not to add

- Work emails or private phone numbers
- Sales scripts, discount codes, or account-team playbooks
- Secrets, internal-only URLs, private Drive/sheet links, or customer-confidential case details without clearance
- Executable skill scripts, hooks, or MCP server configs

## Security review

PRs that touch `skills/` should stay markdown-only. CI runs harness-eval security checks when configured.

## License

Contributions are under the Apache License 2.0.
