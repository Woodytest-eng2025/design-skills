# Design Skills

**Eight agent skills that give AI-generated interfaces a sense of taste** — hand-drawn accents, a real
component system, a perceptually tuned palette, readable type, honest diagrams, consistent icons and a
README that does not look like everyone else's.

<p>
  <a href="https://github.com/Woodytest-eng2025/design-skills/actions/workflows/validate.yml"><img alt="validate" src="https://github.com/Woodytest-eng2025/design-skills/actions/workflows/validate.yml/badge.svg?branch=main"></a>
  <a href="LICENSE"><img alt="license: MIT" src="https://img.shields.io/badge/license-MIT-3DA639?style=flat-square&logo=opensourceinitiative&logoColor=white"></a>
  <img alt="skills: 8" src="https://img.shields.io/badge/skills-8-6366F1?style=flat-square&logo=readme&logoColor=white">
  <a href="https://github.com/Woodytest-eng2025/design-skills/stargazers"><img alt="stars" src="https://img.shields.io/github/stars/Woodytest-eng2025/design-skills?style=flat-square&color=F5B301&logo=github"></a>
  <img alt="works with" src="https://img.shields.io/badge/agents-DSH%20%C2%B7%20Claude%20Code%20%C2%B7%20Codex-0F172A?style=flat-square&logo=anthropic&logoColor=white">
</p>

Each skill is a self-contained `SKILL.md` plus optional `references/` — no runtime, no dependencies, no
build step. Drop it into an agent's skills directory and the agent gains both the API knowledge and the
design judgement to use the library well.

---

## The collection

| Skill | What it gives the agent | Upstream | ⭐ |
| --- | --- | --- | --- |
| [`roughjs-sketch`](skills/roughjs-sketch/SKILL.md) | Hand-drawn SVG/canvas shapes, hachure fills, annotation layers, sketch frames — and the restraint rules for using them | [Rough.js](https://github.com/rough-stuff/rough) | 21k |
| [`shadcn-ui`](skills/shadcn-ui/SKILL.md) | Owned component source, theming tokens, composition recipes that look designed instead of default | [shadcn/ui](https://github.com/shadcn-ui/ui) | 127k |
| [`radix-colors`](skills/radix-colors/SKILL.md) | The 12-step colour scale, step semantics, palette composition and dark-mode mapping | [Radix Colors](https://github.com/radix-ui/colors) | 1.7k |
| [`readme-stats`](skills/readme-stats/SKILL.md) | Stats, top-languages, pin and WakaTime cards — curated, themed, self-hosted when it matters | [GitHub Readme Stats](https://github.com/anuraghazra/github-readme-stats) | 80k |
| [`mermaid-diagrams`](skills/mermaid-diagrams/SKILL.md) | Text-to-diagram syntax, diagram-type selection, theming and a CLI export pipeline | [Mermaid](https://github.com/mermaid-js/mermaid) | 90k |
| [`simple-icons`](skills/simple-icons/SKILL.md) | 3200+ brand marks: slug discovery, three embedding paths, optical alignment rules | [Simple Icons](https://github.com/simple-icons/simple-icons) | 26k |
| [`fontsource`](skills/fontsource/SKILL.md) | Self-hosted fonts, variable axes, subsets, type scales and pairing by product tone | [Fontsource](https://github.com/fontsource/fontsource) | 6.1k |
| [`markdown-badges`](skills/markdown-badges/SKILL.md) | shields.io grammar, badge style discipline, a README header recipe | [Markdown Badges](https://github.com/Ileriayo/markdown-badges) | 17k |

---

## Install

```bash
git clone https://github.com/Woodytest-eng2025/design-skills.git
cd design-skills
./install.sh
```

`install.sh` auto-detects `~/.dsh/skills` (DeepSeek Harness) or `~/.claude/skills` (Claude Code) and
copies every skill in. Options:

```bash
./install.sh ~/.claude/skills     # explicit target
./install.sh --link               # symlink instead of copy (edit in place)
./install.sh --force              # overwrite skills that already exist
```

Manual install — copy any single skill:

```bash
cp -R skills/mermaid-diagrams ~/.dsh/skills/
```

### Where skills live

| Agent | Directory |
| --- | --- |
| DeepSeek Harness | `~/.dsh/skills/<name>/SKILL.md` |
| Claude Code | `~/.claude/skills/<name>/SKILL.md` |
| Most other SKILL.md-compatible agents | `<agent-config>/skills/<name>/SKILL.md` |

Reload or restart the session afterwards so the skill index is rebuilt.

---

## How a skill is structured

```
skills/mermaid-diagrams/
├── SKILL.md                 # front matter + when-to-use + API + recipes + pitfalls
└── references/
    └── syntax-cheatsheet.md # dense lookup material, loaded only when needed
```

```yaml
---
name: mermaid-diagrams
description: Text-to-diagram ... Trigger words: 流程图, diagram, sequence diagram ...
license: MIT
metadata:
  author: Woodytest2025
  version: "1.0.0"
  category: diagrams
  keywords: mermaid, flowchart, sequence, er, gantt
  source: https://github.com/mermaid-js/mermaid
  stars: "90k"
---
```

`description` is what the agent matches against, so it carries both the capability statement and the
trigger words (English and Chinese). `references/` keeps `SKILL.md` short enough to stay in context
while still making the deep detail available on demand.

---

## Design principles behind the collection

1. **Taste is a constraint, not a decoration.** Every skill states when *not* to use the library. Three
   sketch elements are charming; thirty are noise. One badge style is a system; four are a mess.
2. **Defaults are the design.** The skills bias toward the specific values that read as professional:
   muted strokes, `flat-square` badges, `hachure` over solid fills, 12-step colour roles, one accent.
3. **Ship-checkable.** Each skill ends with a checklist an agent (or a reviewer) can run before the work
   is considered done.

---

## Validate

```bash
python3 scripts/validate.py
```

Checks front matter keys, `name` ↔ directory agreement, kebab-case, description length, required
sections, and that every relative link resolves. CI runs the same script on push and pull request.

---

## Credits

All credit for the underlying work goes to the upstream projects above — this repository only packages
their APIs and design conventions into agent-readable form. Icons and fonts referenced by the skills
carry their own licences (CC0 for Simple Icons artwork, SIL OFL for Fontsource families); brand marks
remain subject to their owners' guidelines.

## License

MIT — see [LICENSE](LICENSE).
