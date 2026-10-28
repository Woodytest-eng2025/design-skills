# Contributing

Thanks for wanting to add a skill. The bar is content quality, not volume.

## Adding a skill

1. Create `skills/<kebab-case-name>/SKILL.md`.
2. Copy the front matter shape from an existing skill.
3. Run `python3 scripts/validate.py` — it must pass.
4. Open a PR describing **what the agent can do after loading the skill that it could not do before**.

## What makes a good skill here

| Requirement | Why |
| --- | --- |
| A precise `description` with trigger words (EN + 中文) | The agent only loads a skill when the description matches the user's phrasing. |
| "When to use" **and** "when not to use" | A skill that always applies is a skill that gets applied badly. |
| Current, pinned versions in every code block | Stale APIs are worse than no skill: they fail silently. |
| Specific values, not adjectives | `roughness: 1.2`, `flat-square`, `step 11 for text` — not "make it look nice". |
| A ship checklist | Gives the agent a stopping condition. |
| `references/` for depth | Keeps `SKILL.md` scannable while preserving the long tail. |

## What to avoid

- Marketing copy, star counts as arguments, "revolutionary".
- Invented APIs, parameters or endpoints. If you are not sure, link the docs and say "verify".
- Skills that are a wrapper around `npm install` with no design guidance.
- Anything that requires a secret, a paid key or a running server to be useful.

## Local check

```bash
python3 scripts/validate.py
sh -n install.sh
```

Both run in CI on every push and pull request.
