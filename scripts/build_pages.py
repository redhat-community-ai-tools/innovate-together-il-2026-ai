#!/usr/bin/env python3
"""Build a static GitLab/GitHub-style preview site from docs/ into public/."""

from __future__ import annotations

import html as html_lib
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUT = ROOT / "public"

CSS = """
:root { color-scheme: light; }
* { box-sizing: border-box; }
body { margin: 0; font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 16px; line-height: 1.5; color: #606c71; background: #fff; }
a { color: #1e6bb8; text-decoration: none; }
a:hover { text-decoration: underline; }
.page-header { color: #fff; text-align: center; background-color: #159957; background-image: linear-gradient(120deg, #155799, #159957); padding: 3rem 1rem; }
.project-name { margin: 0; font-size: 2.25rem; font-weight: 700; color: #fff; }
.project-tagline { margin: 0.5rem 0 0; opacity: 0.85; font-weight: normal; font-size: 1.15rem; }
.main-content { max-width: 64rem; padding: 2rem 1.5rem; margin: 0 auto; font-size: 1.1rem; }
.main-content h1 { color: #159957; margin-top: 0; font-size: 1.8rem; }
.main-content h2 { color: #159957; margin-top: 2rem; border-bottom: 1px solid #eaecef; padding-bottom: 0.3rem; font-size: 1.35rem; }
table { width: 100%; border-collapse: collapse; margin: 1rem 0; display: block; overflow-x: auto; }
th, td { border: 1px solid #e9ebec; padding: 0.5rem 0.75rem; text-align: left; vertical-align: top; }
th { background: #f3f6fa; }
.site-footer { padding: 2rem 1rem; text-align: center; font-size: 0.85rem; color: #819198; border-top: 1px solid #eee; }
pre, code { font-family: Consolas, "Liberation Mono", Menlo, Courier, monospace; font-size: 0.9em; }
pre { background: #f3f6fa; padding: 1rem; overflow-x: auto; border-radius: 3px; }
nav.top { text-align: center; padding: 0.75rem; background: #f8f9fa; border-bottom: 1px solid #eee; font-size: 0.95rem; }
nav.top a { margin: 0 0.6rem; }
ul { padding-left: 1.4rem; }
"""


def strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[2].lstrip("\n")
    return text


def md_inline(s: str) -> str:
    s = html_lib.escape(s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r'href="([^"]+)\.md"', r'href="\1.html"', s)
    return s


def render_md(md: str) -> str:
    lines = md.splitlines()
    out: list[str] = []
    i = 0
    in_code = False
    code_buf: list[str] = []
    table_buf: list[str] = []

    def flush_table() -> None:
        nonlocal table_buf
        if not table_buf:
            return
        rows = [[c.strip() for c in row.strip("|").split("|")] for row in table_buf]
        body_rows = [r for r in rows if not all(re.match(r"^:?-+:?$", c or "") for c in r)]
        table_buf = []
        if not body_rows:
            return
        header, *rest = body_rows
        html = ["<table><thead><tr>"]
        html += [f"<th>{md_inline(c)}</th>" for c in header]
        html.append("</tr></thead><tbody>")
        for r in rest:
            html.append("<tr>")
            html += [f"<td>{md_inline(c)}</td>" for c in r]
            html.append("</tr>")
        html.append("</tbody></table>")
        out.append("".join(html))

    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            if in_code:
                out.append("<pre><code>" + html_lib.escape("\n".join(code_buf)) + "</code></pre>")
                code_buf = []
                in_code = False
            else:
                flush_table()
                in_code = True
            i += 1
            continue
        if in_code:
            code_buf.append(line)
            i += 1
            continue
        if "|" in line and line.strip().startswith("|"):
            table_buf.append(line)
            i += 1
            continue
        flush_table()
        if not line.strip():
            i += 1
            continue
        if line.startswith("# "):
            out.append(f"<h1>{md_inline(line[2:])}</h1>")
        elif line.startswith("## "):
            out.append(f"<h2>{md_inline(line[3:])}</h2>")
        elif line.startswith("- "):
            items = [line]
            i += 1
            while i < len(lines) and lines[i].startswith("- "):
                items.append(lines[i])
                i += 1
            out.append("<ul>" + "".join(f"<li>{md_inline(x[2:])}</li>" for x in items) + "</ul>")
            continue
        else:
            out.append(f"<p>{md_inline(line)}</p>")
        i += 1
    flush_table()
    return "\n".join(out)


def page(title: str, tagline: str, body_html: str, rel_prefix: str = "") -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{html_lib.escape(title)}</title>
  <style>{CSS}</style>
</head>
<body>
  <nav class="top">
    <a href="{rel_prefix}index.html">Agenda</a>
    <a href="{rel_prefix}speakers.html">Speakers</a>
    <a href="{rel_prefix}skill.html">Skill handoff</a>
    <a href="https://gitlab.cee.redhat.com/qe-ds/innovate-together-il-2026-ai/-/blob/main/README.md">GitLab README</a>
    <a href="https://gitlab.cee.redhat.com/qe-ds/innovate-together-il-2026-ai/-/blob/main/README.md#install-the-skill">Install</a>
  </nav>
  <section class="page-header">
    <h1 class="project-name">Innovate Together IL 2026 — AI Track</h1>
    <h2 class="project-tagline">{html_lib.escape(tagline)}</h2>
  </section>
  <main class="main-content">
{body_html}
  </main>
  <footer class="site-footer">Innovate Together IL 2026 — AI track takeaway pack</footer>
</body>
</html>
"""


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "talks").mkdir(parents=True)

    pages = {
        "index.md": ("AI Track Agenda", "Agenda, talk summaries, and agent-skill handoff for the AI track."),
        "speakers.md": ("Speakers", "Speaker LinkedIn and GitHub (when opted in)."),
        "skill.md": ("Agent skill handoff", "Share this with developers after the conference."),
    }
    for name, (title, tagline) in pages.items():
        md = strip_frontmatter((DOCS / name).read_text(encoding="utf-8"))
        (OUT / f"{Path(name).stem}.html").write_text(
            page(title, tagline, render_md(md)), encoding="utf-8"
        )

    for talk in sorted((DOCS / "talks").glob("*.md")):
        md = strip_frontmatter(talk.read_text(encoding="utf-8"))
        (OUT / "talks" / f"{talk.stem}.html").write_text(
            page(talk.stem.replace("-", " ").title(), "Talk summary", render_md(md), rel_prefix="../"),
            encoding="utf-8",
        )

    # GitLab Pages serves public/index.html
    print(f"Built {OUT} ({len(list(OUT.rglob('*.html')))} html files)")


if __name__ == "__main__":
    main()
