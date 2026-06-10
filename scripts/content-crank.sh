#!/usr/bin/env bash
# Continuous content crank: deepen consumer code pages to Command Center depth in
# revenue order, shipping each wave so pages go live progressively. Idempotent
# (skips already-deep pages), so re-launches just pick up the backlog.
# Caller must export ANTHROPIC_API_KEY (+ PERPLEXITY_API_KEY) before running.
set -uo pipefail
cd /c/Users/chris/industrial-fixes || exit 1
WAVES="${1:-10}"
COUNT="${2:-50}"
JOBS="${3:-2}"
[[ "$WAVES$COUNT$JOBS" =~ ^[0-9]+$ ]] || { echo "numeric args only: waves count jobs"; exit 2; }
# Per-user, 0600 log (response bodies can land here; keep it off a shared /tmp path).
LOG="${TMPDIR:-/tmp}/ecf-crank-$(id -u).log"
( umask 077; : >> "$LOG" )

ship() {
  git checkout -- public/search-index.json 2>/dev/null
  git add src/data/blog 2>/dev/null
  git diff --cached --quiet && { echo "  (nothing to ship)" >> "$LOG"; return 0; }
  git -c commit.gpgsign=false commit -q -m "Content crank: deepened consumer code pages (revenue order) [crank]" 2>>"$LOG"
  git fetch -q origin main 2>>"$LOG"
  if [ "$(git rev-list --count HEAD..origin/main 2>/dev/null)" -gt 0 ]; then
    git rebase -q origin/main >>"$LOG" 2>&1 || { git rebase --abort 2>>"$LOG"; echo "  rebase aborted" >> "$LOG"; }
  fi
  git push -q origin main >>"$LOG" 2>&1 && echo "  pushed wave" >> "$LOG"
}

echo "=== CRANK START $(date) waves=$WAVES count=$COUNT jobs=$JOBS ===" >> "$LOG"
# Revenue-first: finish the money-map targets before broadening.
if [ -f .planning/money-targets.txt ]; then
  echo "=== money targets $(date) ===" >> "$LOG"
  python scripts/money-gen.py --file .planning/money-targets.txt --jobs "$JOBS" >> "$LOG" 2>&1
  ship
fi
# Broaden: deepen the consumer code-page backlog wave by wave.
for i in $(seq 1 "$WAVES"); do
  echo "=== wave $i/$WAVES $(date) ===" >> "$LOG"
  python scripts/regen-deep.py --count "$COUNT" --jobs "$JOBS" >> "$LOG" 2>&1
  ship
done
echo "=== CRANK DONE $(date) ===" >> "$LOG"
