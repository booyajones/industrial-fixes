#!/usr/bin/env bash
# Autonomous consumer-content ship loop for errorcodefixes.com.
#
# Each iteration: generate a wave from the consumer pool -> build gate (mojibake +
# astro) -> commit blog .md -> rebase onto origin (cloud pipeline) -> push -> IndexNow.
# Build-gated: a failing build STOPS the loop, so nothing broken ever deploys.
# Stops naturally when the pool is exhausted (nothing new to ship).
#
# Usage: scripts/ship-loop.sh [MAX_ITERS] [COUNT]
# Requires ANTHROPIC_API_KEY + PERPLEXITY_API_KEY in env.
set -uo pipefail
cd "$(dirname "$0")/.." || exit 1
MAX_ITERS="${1:-6}"
COUNT="${2:-180}"
ITER=0
while [ "$ITER" -lt "$MAX_ITERS" ]; do
  ITER=$((ITER + 1))
  echo "===== ITER $ITER / $MAX_ITERS  $(date -u +%H:%M:%S) ====="
  python scripts/generate-batch.py --topics-file scripts/.consumer-topics.txt --count "$COUNT" --jobs 3 2>&1 | tail -2
  UNCOMMITTED=$(git status --porcelain src/data/blog | wc -l | tr -d ' ')
  echo "iter $ITER: $UNCOMMITTED uncommitted blog files"
  if [ "$UNCOMMITTED" -le 0 ]; then echo "nothing new to ship; pool exhausted. stopping."; break; fi

  NODE_OPTIONS=--max-old-space-size=6144 npm run build > "/tmp/loop_build_$ITER.log" 2>&1
  if [ $? -ne 0 ]; then echo "BUILD FAILED iter $ITER:"; tail -6 "/tmp/loop_build_$ITER.log"; echo "STOPPING (no broken deploy)."; break; fi

  git add src/data/blog
  git commit -q -m "Consumer pivot auto-wave $ITER: +$UNCOMMITTED grounded appliance/HVAC guides" \
                 -m "Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
  # keep volatile, build-regenerated / state files out of the way of rebases
  # (search-index.json is rebuilt every build; failing to clean it blocks pull --rebase)
  git checkout -- scripts/.generated-articles.json scripts/.code-pool.json public/search-index.json 2>/dev/null || true
  git fetch origin --quiet
  if [ "$(git rev-list --count HEAD..origin/main 2>/dev/null || echo 0)" -gt 0 ]; then
    git pull --rebase origin main 2>&1 | tail -2 || { git rebase --abort 2>/dev/null; echo "rebase conflict; will retry next iter"; continue; }
  fi
  git push origin main 2>&1 | tail -2
  node scripts/indexnow-ping.mjs 2>&1 | head -1
  echo "iter $ITER shipped: $(git log -1 --oneline)"
done
echo "===== SHIP-LOOP DONE: blog count $(ls -1 src/data/blog/*.md | wc -l), HEAD $(git log -1 --oneline) ====="
