#!/usr/bin/env bash
# Autonomous content factory loop. Runs each content-type generator wave, then
# build-gates and ships it (push retries past the racing cloud pipeline). A
# failing build STOPS the loop so nothing broken deploys. Paced: one wave at a
# time. Requires ANTHROPIC_API_KEY + PERPLEXITY_API_KEY in env.
set -uo pipefail
cd "$(dirname "$0")/.." || exit 1
JOBS="${JOBS:-3}"
UNI="scripts/.content-universe.json"

# label|generator command  (highest-money first: parts -> models -> symptom fill)
WAVES=(
  "parts|python scripts/generate-parts.py --topics-file $UNI --count 200 --jobs $JOBS"
  "models|python scripts/generate-models.py --topics-file $UNI --count 125 --jobs $JOBS"
  "symptoms-fill|python scripts/generate-symptoms.py --count 230 --jobs $JOBS"
  "parts2|python scripts/generate-parts.py --topics-file $UNI --count 280 --jobs $JOBS"
)

for entry in "${WAVES[@]}"; do
  label="${entry%%|*}"; cmd="${entry#*|}"
  echo "===== WAVE: $label  $(date -u +%H:%M:%S) ====="
  eval "$cmd" 2>&1 | tail -3
  UNCOMMITTED=$(git status --porcelain src/data/blog | wc -l | tr -d ' ')
  echo "$label: $UNCOMMITTED uncommitted blog files"
  if [ "$UNCOMMITTED" -le 0 ]; then echo "nothing new for $label; continuing"; continue; fi

  NODE_OPTIONS=--max-old-space-size=6144 npm run build > "/tmp/cf_build_$label.log" 2>&1
  if [ $? -ne 0 ]; then echo "BUILD FAILED ($label):"; tail -6 "/tmp/cf_build_$label.log"; echo "STOPPING (no broken deploy)."; break; fi

  git add src/data/blog
  git commit -q -m "Content factory: $label wave (+$UNCOMMITTED grounded consumer pages)" \
                 -m "Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
  ok=0
  for i in $(seq 1 8); do
    git fetch origin --quiet
    # clean build-regenerated / engine-state tracked files so they can't block rebase
    git checkout -- public/search-index.json scripts/.generated-articles.json scripts/.code-pool.json 2>/dev/null
    # only rebase when actually behind; a plain push fast-forwards otherwise
    if [ "$(git rev-list --count HEAD..origin/main 2>/dev/null || echo 0)" -gt 0 ]; then
      git rebase -X theirs origin/main > /tmp/cf_rb.log 2>&1 || { git rebase --abort 2>/dev/null; continue; }
    fi
    if git push origin main 2>&1 | grep -q 'main -> main'; then ok=1; break; fi
  done
  if [ "$ok" = 1 ]; then
    echo "$label SHIPPED: $(git log -1 --oneline)"
    node scripts/indexnow-ping.mjs 2>&1 | head -1
  else
    echo "$label push failed after retries (commit kept; next wave will carry it)"
  fi
done
echo "===== CONTENT FACTORY DONE: blog $(ls -1 src/data/blog/*.md | wc -l), HEAD $(git log -1 --oneline) ====="
