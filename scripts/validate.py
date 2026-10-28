#!/usr/bin/env python3
"""Validate every skill in ./skills against the collection's conventions.

Checks:
  - skills/<dir>/SKILL.md exists and starts with a YAML front matter block
  - the front matter parses as strict YAML
  - required keys: name, description, license, metadata
  - metadata keys: author, version, category, keywords, source, stars
  - name == directory name, kebab-case
  - description is 60..700 chars
  - body has "## " sections, a checklist, and at least 60 lines
  - relative links inside the body resolve to existing files

Exit code 1 on any error. Run from the repository root:
    python3 scripts/validate.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - CI installs PyYAML
    print("error: PyYAML is required (pip install pyyaml)", file=sys.stderr)
    raise SystemExit(2)

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"

REQUIRED_TOP = {"name", "description", "license", "metadata"}
REQUIRED_META = {"author", "version", "category", "keywords", "source", "stars"}
KEBAB = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK = re.compile(r"\]\((?!https?://|#|mailto:)([^)]+)\)")


def split_front_matter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("missing leading '---'")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("unterminated front matter")
    return text[4:end], text[end + 5 :]


def check(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    name = skill_dir.name
    path = skill_dir / "SKILL.md"

    if not path.is_file():
        return [f"{name}: missing SKILL.md"]

    try:
        block, body = split_front_matter(path.read_text(encoding="utf-8"))
    except ValueError as exc:
        return [f"{name}: {exc}"]

    try:
        meta_all = yaml.safe_load(block)
    except yaml.YAMLError as exc:
        detail = str(exc).replace("\n", " ")[:160]
        return [f"{name}: front matter is not valid YAML ({detail})"]

    if not isinstance(meta_all, dict):
        return [f"{name}: front matter is not a mapping"]

    missing = REQUIRED_TOP - meta_all.keys()
    if missing:
        errors.append(f"{name}: missing front-matter keys {sorted(missing)}")

    meta = meta_all.get("metadata") or {}
    if not isinstance(meta, dict):
        errors.append(f"{name}: 'metadata' must be a mapping")
        meta = {}
    missing_meta = REQUIRED_META - meta.keys()
    if missing_meta:
        errors.append(f"{name}: missing metadata keys {sorted(missing_meta)}")

    declared = str(meta_all.get("name", ""))
    if declared != name:
        errors.append(f"{name}: front-matter name '{declared}' != directory '{name}'")
    if not KEBAB.match(declared):
        errors.append(f"{name}: name is not kebab-case")

    desc = str(meta_all.get("description", ""))
    if not 60 <= len(desc) <= 700:
        errors.append(f"{name}: description length {len(desc)} not in 60..700")

    if "## " not in body:
        errors.append(f"{name}: body has no '## ' sections")
    if "checklist" not in body.lower():
        errors.append(f"{name}: body has no checklist section")
    if len(body.splitlines()) < 60:
        errors.append(f"{name}: body is shorter than 60 lines")

    for link in LINK.findall(body):
        target = link.split("#")[0].strip()
        if target and not (skill_dir / target).exists():
            errors.append(f"{name}: broken relative link '{link}'")

    return errors


def main() -> int:
    if not SKILLS.is_dir():
        print(f"error: {SKILLS} not found", file=sys.stderr)
        return 1

    dirs = sorted(d for d in SKILLS.iterdir() if d.is_dir())
    if not dirs:
        print("error: no skills found", file=sys.stderr)
        return 1

    all_errors: list[str] = []
    print(f"{'skill':22} {'files':>5} {'lines':>6}  status")
    for d in dirs:
        errs = check(d)
        files = [p for p in d.rglob("*") if p.is_file()]
        lines = sum(len(p.read_text(encoding="utf-8").splitlines()) for p in files)
        status = "ok" if not errs else "FAIL"
        print(f"{d.name:22} {len(files):5} {lines:6}  {status}")
        all_errors.extend(errs)

    print()
    if all_errors:
        for e in all_errors:
            print(f"  - {e}", file=sys.stderr)
        print(f"{len(all_errors)} problem(s) across {len(dirs)} skill(s)", file=sys.stderr)
        return 1

    print(f"All {len(dirs)} skills valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
