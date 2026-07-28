# Claude Code Review Handoff

Date: 2026-04-24

## What I prepared
- Created `CLAUDE_CODE_SITE_REVIEW_PROMPT.md`
- Structured it for an independent, skeptical review of `errorcodefixes.com`
- Included the repo path, live URLs, files to read, review criteria, required commands, and required output files
- Pointed Claude Code to local credential references through `TOOLS.md`

## What I did not do
I did not paste raw API keys, private keys, JSON credentials, OAuth tokens, or security secrets into a markdown file.

That would create a concentrated secret dump and is a bad operating pattern.
The prompt instead tells Claude Code to use existing local credentials on the machine if needed, and to reference paths without echoing secret contents.

## Files created
- `C:\Users\Administrator\.openclaw\workspace\industrial-fixes\CLAUDE_CODE_SITE_REVIEW_PROMPT.md`
- `C:\Users\Administrator\.openclaw\workspace\industrial-fixes\CLAUDE_CODE_SITE_REVIEW_HANDOFF.md`

## Suggested use
1. Open `CLAUDE_CODE_SITE_REVIEW_PROMPT.md`
2. Paste it into Claude Code
3. Let Claude Code produce the three requested markdown outputs
4. Compare its conclusions against `REVENUE_FIRST_CONTENT_PLAN.md`

## Notes
If you want, I can next create a second version tuned for implementation instead of review. That version would tell Claude Code to take the top 10 actions and ship them in priority order.
