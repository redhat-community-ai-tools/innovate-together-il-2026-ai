#!/usr/bin/env python3
"""Structural smoke checks for the public AI + Infra skills. Exit 0 = pass."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AI = ROOT / "skills/innovate-together-il-ai"
INFRA = ROOT / "skills/innovate-together-il-infra"
DOCS_TALKS = ROOT / "docs/talks"
EXTERNAL_SLUGS = (
    "smaller-models-smarter-systems",
    "agentic-ai-intel-xeon",
    "customer-case-study",
    "zero-to-fully-compliant",
    "infinidat-csi",
)
errors: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)


def talk_slugs_from_agenda(agenda: Path) -> list[str]:
    text = agenda.read_text(encoding="utf-8")
    return re.findall(r"\]\(talks/([a-z0-9-]+)\.md\)", text)


def check_no_private_links() -> None:
    """Public pack must not mention GitLab or carry Drive/Docs links."""
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.name == "smoke_check.py":
            continue
        if path.suffix.lower() not in {".md", ".yml", ".yaml", ".json", ".py"}:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        low = text.lower()
        rel = path.relative_to(ROOT)
        if "gitlab" in low:
            fail(f"{rel}: mentions GitLab")
        if "drive.google.com" in low or "docs.google.com" in low:
            fail(f"{rel}: has a Google Drive or Docs link")


def check_skill(skill_dir: Path, name: str) -> None:
    agenda = skill_dir / "references/agenda.md"
    talks = skill_dir / "references/talks"
    if not (skill_dir / "SKILL.md").is_file():
        fail(f"{name}: missing SKILL.md")
        return
    if not agenda.is_file():
        fail(f"{name}: missing agenda.md")
        return
    slugs = talk_slugs_from_agenda(agenda)
    if not slugs:
        fail(f"{name}: no talk links in agenda")
    for slug in slugs:
        path = talks / f"{slug}.md"
        if not path.is_file():
            fail(f"{name}: agenda links missing talk {slug}.md")
            continue
        body = path.read_text(encoding="utf-8")
        if "**Materials:**" not in body:
            fail(f"{name}/{slug}: missing Materials field")
        doc = DOCS_TALKS / f"{slug}.md"
        if not doc.is_file():
            fail(f"{name}/{slug}: missing docs/talks/{slug}.md")


def check_external_withheld() -> None:
    for slug in EXTERNAL_SLUGS:
        matches = list(ROOT.glob(f"skills/**/talks/{slug}.md"))
        if not matches:
            fail(f"missing external talk {slug}")
            continue
        body = matches[0].read_text(encoding="utf-8")
        if "**Materials:** slides-not-in-pack" not in body:
            fail(f"{slug}: external deck must stay slides-not-in-pack")


def check_public_wording() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "github.com/redhat-community-ai-tools/innovate-together-il-2026-ai" not in readme:
        fail("README: missing public GitHub repo URL")
    if "innovate-together-il-infra" not in readme:
        fail("README: missing infra skill install")
    plugin = (ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8")
    if '"name": "innovate-together-il-ai"' not in plugin:
        fail("plugin.json: public plugin id must stay innovate-together-il-ai")
    agenda = (INFRA / "references/agenda.md").read_text(encoding="utf-8")
    if "innovate-together-il-ai/references/talks/opening-keynote.md" not in agenda:
        fail("infra agenda: missing link-out to AI opening-keynote")
    if "innovate-together-il-ai/references/talks/ai-ready-enterprise.md" not in agenda:
        fail("infra agenda: missing link-out to AI ai-ready-enterprise")


def main() -> int:
    check_no_private_links()
    check_skill(AI, "ai")
    check_skill(INFRA, "infra")
    check_external_withheld()
    check_public_wording()
    infra_slugs = talk_slugs_from_agenda(INFRA / "references/agenda.md")
    if len(infra_slugs) < 8:
        fail(f"infra: expected >=8 talks in agenda, got {len(infra_slugs)}")
    if errors:
        print("FAIL")
        for err in errors:
            print(f"  - {err}")
        return 1
    print("PASS: structural smoke checks OK")
    print(f"  AI talks: {len(talk_slugs_from_agenda(AI / 'references/agenda.md'))}")
    print(f"  Infra talks: {len(infra_slugs)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
