#!/usr/bin/env sh
# Install the design-skills collection into an agent's skills directory.
#
#   ./install.sh                      # auto-detect target (~/.dsh/skills or ~/.claude/skills)
#   ./install.sh ~/.claude/skills     # explicit target
#   ./install.sh -l                   # symlink instead of copy (dev mode)
#
# Each skill is a directory containing SKILL.md. Existing skills with the same
# name are replaced only when --force is passed.

set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
SOURCE_DIR="$SCRIPT_DIR/skills"

usage() {
  sed -n '2,9p' "$0" | sed 's/^# \{0,1\}//'
  exit "${1:-0}"
}

MODE=copy
FORCE=0
TARGET=""

while [ $# -gt 0 ]; do
  case "$1" in
    -h|--help) usage 0 ;;
    -l|--link) MODE=link ;;
    -f|--force) FORCE=1 ;;
    -*) echo "unknown option: $1" >&2; usage 1 ;;
    *) TARGET="$1" ;;
  esac
  shift
done

if [ -z "$TARGET" ]; then
  if [ -d "$HOME/.dsh/skills" ]; then
    TARGET="$HOME/.dsh/skills"
  elif [ -d "$HOME/.claude/skills" ]; then
    TARGET="$HOME/.claude/skills"
  else
    TARGET="$HOME/.dsh/skills"
  fi
fi

[ -d "$SOURCE_DIR" ] || { echo "error: $SOURCE_DIR not found" >&2; exit 1; }
mkdir -p "$TARGET"

echo "Installing into: $TARGET"
echo "Mode: $MODE"
echo

for dir in "$SOURCE_DIR"/*/; do
  name=$(basename "$dir")
  dest="$TARGET/$name"

  if [ -e "$dest" ] || [ -L "$dest" ]; then
    if [ "$FORCE" -eq 1 ]; then
      rm -rf "$dest"
    else
      echo "  skip   $name (exists; use --force to replace)"
      continue
    fi
  fi

  if [ "$MODE" = link ]; then
    ln -s "$dir" "$dest"
    echo "  link   $name"
  else
    cp -R "$dir" "$dest"
    echo "  copy   $name"
  fi
done

echo
echo "Done. Restart or reload your agent session to pick up the new skills."
