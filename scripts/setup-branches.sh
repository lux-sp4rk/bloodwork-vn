#!/usr/bin/env bash
# setup-branches.sh — Enforce PR requirement for narrative files on digital-death-dolls
# Run from repo root or pass repo as arg: ./scripts/setup-branches.sh lux-sp4rk/digital-death-dolls

set -e

REPO="${1:-lux-sp4rk/digital-death-dolls}"
GAME_PATTERNS="'game/**/*.rpy','game/**/*.rnh'"

echo "=== Branch Protection Setup for $REPO ==="
echo ""
echo "NOTE: Branch protection via API requires GitHub Pro on private repos."
echo "      If this fails, configure manually at:"
echo "      https://github.com/$REPO/settings/branch_protection_rules/new"
echo ""
echo "Required settings:"
echo "  • Protect main branch"
echo "  • Require pull requests before merging"
echo "  • Under 'Branch protection rules > Apply to' add: main"
echo "  • Require status checks: optional (lint is best-effort)"
echo "  • DO NOT enable 'Require signed commits' (not yet enforced)"
echo ""

# Try to set branch protection
# This will 403 on free/proxy tier for private repos — expected.
PROTECTION_PAYLOAD=$(cat <<EOF
{
  "required_status_checks": null,
  "enforce_admins": false,
  "required_linear_history": false,
  "allow_force_pushes": false,
  "require_conversation_resolution": true,
  "required_signatures": false,
  "required_pull_request_reviews": {
    "dismiss_stale_reviews": true
  },
  "restrictions": null
}
EOF
)

echo "Attempting API-based branch protection (will fail gracefully on free tier)..."
RESPONSE=$(gh api repos/$REPO/branches/main/protection --method PUT \
  -H "Accept: application/vnd.github+json" \
  -f raw="$(printf '%s' "$PROTECTION_PAYLOAD")" 2>&1) && {
    echo "✓ Branch protection applied"
    echo "$RESPONSE" | gh api --jq '.message' 2>/dev/null || echo "$RESPONSE"
  } || {
    CODE=$?
    if echo "$RESPONSE" | grep -q "403"; then
      echo "✗ Branch protection requires GitHub Pro (expected for private repos)"
      echo "  → Set up manually at: https://github.com/$REPO/settings/branch_protection_rules/new"
    else
      echo "✗ Unexpected error:"
      echo "$RESPONSE"
      exit $CODE
    fi
}

echo ""
echo "=== Workflow files applied ==="
ls -la .github/workflows/
echo ""
echo "Next steps:"
echo "  1. Commit and push: git add .github/workflows/ && git commit -m 'add narrative check + lint workflows'"
echo "  2. Configure branch protection manually (link above)"
echo "  3. For Vercel deploy previews: connect repo at vercel.com → new project → import $REPO"
