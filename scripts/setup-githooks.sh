#!/usr/bin/env bash
# setup-githooks.sh — symlink githooks/ into .git/hooks/
#
# Run once after cloning, or re-run after githooks/ updates:
#   ./scripts/setup-githooks.sh

set -e

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
HOOKS_DIR="$REPO_ROOT/.git/hooks"

echo "Linking githooks into $HOOKS_DIR..."

for hook in "$REPO_ROOT/githooks"/*; do
  name=$(basename "$hook")
  target="$HOOKS_DIR/$name"

  if [[ -L "$target" ]]; then
    echo "  ✓ $name (already linked)"
  elif [[ -f "$target" ]]; then
    echo "  ~ $name (existing hook — backing up)"
    mv "$target" "$target.local"
    ln -s "../../githooks/$name" "$target"
    echo "  ✓ $name (linked, old hook saved as .local)"
  else
    ln -s "../../githooks/$name" "$target"
    echo "  ✓ $name (linked)"
  fi
done

echo ""
echo "Done. Hooks will run on:"
echo "  pre-push  — blocks direct push to main for narrative files"
echo "  pre-commit — lints staged .rpy/.rnh files"
