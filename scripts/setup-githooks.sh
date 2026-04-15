#!/usr/bin/env bash
# setup-githooks.sh — copy githooks/ into .git/hooks/
#
# Run once after cloning, or re-run after githooks/ updates:
#   ./scripts/setup-githooks.sh

set -e

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
HOOKS_DIR="$REPO_ROOT/.git/hooks"

echo "Copying hooks into $HOOKS_DIR..."

for hook in "$REPO_ROOT/githooks"/*; do
  name=$(basename "$hook")
  target="$HOOKS_DIR/$name"

  if [[ -f "$target" && ! -L "$target" ]]; then
    echo "  ~ $name (existing hook — backing up)"
    mv "$target" "$target.local"
  fi

  cp "$hook" "$target"
  chmod +x "$target"
  echo "  ✓ $name"
done

echo ""
echo "Done. Hooks active:"
echo "  pre-push  — blocks direct push to main for narrative files"
echo "  pre-commit — lints staged .rpy/.rnh files"
echo ""
echo "Note: hooks live directly in .git/hooks/ (not symlinks). To update,"
echo "      edit githooks/ and re-run this script."