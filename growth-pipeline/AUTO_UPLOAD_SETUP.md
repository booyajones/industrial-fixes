# Auto-Upload Setup — the last mile to fully autonomous distribution

All three uploader scripts are built and tested in `--dry` mode. Each one
is gated by a single credential. The moment that credential lands in
`~/.claude/secrets/ecf.env`, the matching cron activates and content
starts posting on its own.

## Status

| Channel | Script | Credential needed | Blocker |
|---|---|---|---|
| Pinterest | `scripts/pinterest-upload.py` | `PINTEREST_ACCESS_TOKEN` | App-creation form has a reCAPTCHA — Chris must click "I'm not a robot" + Submit, then I finish OAuth |
| Beehiiv | `scripts/beehiiv-publish.py` | `BEEHIIV_API_KEY` | Just needs the key from app.beehiiv.com → Settings → Integrations |
| YouTube | `scripts/youtube-upload.py` | `YOUTUBE_CLIENT_ID/_SECRET/_REFRESH_TOKEN` | Google Cloud OAuth client + one consent flow |

## Pinterest — 90% done

App form is fully filled in the browser (name, company, website, privacy
link, purpose, use case = Pin creation & scheduling, audience = Creators).
**The only remaining step is the reCAPTCHA + Submit, which I'm not
permitted to click.**

Once submitted:
1. Pinterest shows app ID + secret on the app detail page
2. I run the OAuth flow: `https://www.pinterest.com/oauth/?client_id=<id>&redirect_uri=https://errorcodefixes.com/&response_type=code&scope=pins:write,boards:read,user_accounts:read`
3. Capture the `code`, exchange for an access token
4. Save `PINTEREST_ACCESS_TOKEN` to ecf.env
5. `scripts/pinterest-upload.py --count 2` posts the first pins

Then `ECF-Pinterest-Upload` cron (daily 11am ET) posts 2 pins/day from
the 55 PNGs + everything the daily content pipeline produces.

## Beehiiv — 1 step

1. app.beehiiv.com → Settings → Integrations → API → Create New API Key
2. Paste it here, I store as `BEEHIIV_API_KEY`
3. `scripts/beehiiv-publish.py --status draft` creates the weekly digest as
   a draft for review (or `--status confirmed` to send straight to the list)

The `BEEHIIV_PUBLICATION_ID_V2` is already in ecf.env.

## YouTube — most setup

1. console.cloud.google.com → new project "errorcodefixes-yt"
2. Enable "YouTube Data API v3"
3. OAuth consent screen → External → add scope `.../auth/youtube.upload`
4. Credentials → Create OAuth client ID → Desktop app
5. Copy client ID + secret
6. Run the one-time consent flow (I drive Chrome, you click Allow)
7. Capture refresh token → save all three to ecf.env
8. `scripts/youtube-upload.py --count 1` uploads the first Short + thumbnail

Then `ECF-YouTube-Upload` cron (daily 12pm ET) posts 1 Short/day from the
11 MP4s + every new one the weekly video batch renders.

## Pacing rationale (built into every uploader)

- Pinterest: 2/day — Pinterest flags accounts that bulk-post; 1-2/day is the
  sweet spot for a new account building trust.
- YouTube: 1/day — Shorts algorithm rewards consistency over volume; daily
  cadence keeps the channel "active" without tripping spam heuristics.
- Beehiiv: weekly — matches the digest cadence; no daily email fatigue.

All three track posted items in a `posted.json` so re-running never
double-posts and the queue drains predictably.
