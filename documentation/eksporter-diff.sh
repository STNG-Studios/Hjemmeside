#!/bin/bash
#
# Eksportér git diff og opsummering for en AI-session.
#
# Brug:
#   bash eksporter-diff.sh <session-nummer> <start-commit> <slut-commit>
#
# Eksempel:
#   bash eksporter-diff.sh 001 abc1234 def5678
#
# Output:
#   documentation/ai-aendringer/session-<NNN>_<DATO>.diff
#   documentation/ai-aendringer/session-<NNN>_<DATO>.md

set -e

if [ "$#" -lt 3 ]; then
    echo "Brug: bash eksporter-diff.sh <session-nummer> <start-commit> <slut-commit>"
    echo ""
    echo "Eksempel:"
    echo "  bash eksporter-diff.sh 001 abc1234 def5678"
    echo ""
    echo "Tip: Find commits med 'git log --oneline'"
    exit 1
fi

SESSION_NR="$1"
START_COMMIT="$2"
END_COMMIT="$3"
DATO=$(date +%Y-%m-%d)

# Find projektrod (der hvor .git er)
PROJECT_ROOT=$(git rev-parse --show-toplevel)
OUTPUT_DIR="$PROJECT_ROOT/documentation/ai-aendringer"
mkdir -p "$OUTPUT_DIR"

DIFF_FILE="$OUTPUT_DIR/session-${SESSION_NR}_${DATO}.diff"
MD_FILE="$OUTPUT_DIR/session-${SESSION_NR}_${DATO}.md"

echo "Eksporterer diff fra $START_COMMIT til $END_COMMIT..."

# Generér diff-fil
git diff "$START_COMMIT".."$END_COMMIT" > "$DIFF_FILE"
echo "Diff gemt: $DIFF_FILE"

# Generér læsbar opsummering
{
    echo "# AI-ændringer — Session $SESSION_NR ($DATO)"
    echo ""
    echo "**Commit-range:** \`$START_COMMIT\`..\`$END_COMMIT\`"
    echo ""

    # List commits i rangen
    echo "## Commits"
    echo ""
    echo '```'
    git log --oneline "$START_COMMIT".."$END_COMMIT"
    echo '```'
    echo ""

    # Vis ændrede filer
    echo "## Ændrede filer"
    echo ""
    echo '```'
    git diff --stat "$START_COMMIT".."$END_COMMIT"
    echo '```'
    echo ""

    # Vis fuld diff med syntax highlighting hint
    echo "## Fuld diff"
    echo ""
    echo '```diff'
    git diff "$START_COMMIT".."$END_COMMIT"
    echo '```'
} > "$MD_FILE"

echo "Opsummering gemt: $MD_FILE"
echo ""
echo "Antal ændrede filer: $(git diff --name-only "$START_COMMIT".."$END_COMMIT" | wc -l | tr -d ' ')"
echo "Tilføjede linjer:   $(git diff "$START_COMMIT".."$END_COMMIT" | grep -c '^+[^+]' || echo 0)"
echo "Fjernede linjer:    $(git diff "$START_COMMIT".."$END_COMMIT" | grep -c '^-[^-]' || echo 0)"
