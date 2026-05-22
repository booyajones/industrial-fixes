# AdSense activation — what's done and what Chris needs to do

**Status:** Infrastructure deployed 2026-05-22. Awaiting Chris's manual signup.

## What's already wired

- `Layout.astro` reads `PUBLIC_ADSENSE_CLIENT` env var (format
  `ca-pub-XXXXXXXXXXXXXXXX`) and injects the AdSense auto-ads script
  into every page when present.
- `astro.config.ts` declares `PUBLIC_ADSENSE_CLIENT` as an optional
  client env var (so it builds cleanly without it set).
- Privacy Policy page exists at `/privacy/` — required by AdSense.
- Terms of Use page exists at `/terms/` — required by AdSense.
- Affiliate Disclosure already exists at `/disclosure/`.
- Footer links to all three legal pages.

## What Chris needs to do (10 min)

1. Sign in at https://adsense.google.com/ with the Google account that
   owns the Search Console property (the same account that owns
   `errorcodefixes.com` in GSC — likely info@errorcodefixes.com or
   chris.a.wyatt@gmail.com).
2. Add `errorcodefixes.com` as a new site.
3. Get the `ca-pub-XXXXXXXXXXXXXXXX` publisher ID from the AdSense
   dashboard.
4. Add it to Cloudflare Pages env vars:
   - Settings → Environment variables → Add variable
   - Name: `PUBLIC_ADSENSE_CLIENT`
   - Value: `ca-pub-XXXXXXXXXXXXXXXX`
   - Environment: Production
   - Save.
5. Trigger a deploy. The AdSense crawler picks up the script tag and
   begins the review process.

## Review timeline

- Initial review: 14 days typical, up to 4 weeks.
- During review, the site must stay live with the script tag present.
- Once approved, Auto Ads start serving immediately. No further code
  changes needed unless we want manual ad placements.

## Revenue expectations

At current organic traffic (~30 visitors/30d) AdSense earnings will be
trivial (~$0.50-$3/month). The point of activating now is:

1. **Start the 14-day clock today** so we're ready when traffic scales.
2. **No code lock-in.** Removing AdSense is a one-line env-var change.
3. **Compound effect.** Once approved, every new article also serves
   ads from day one without extra setup.

## Compliance pages shipped

| Page | URL | Required by |
|---|---|---|
| Privacy Policy | /privacy/ | AdSense, GDPR, CCPA |
| Terms of Use | /terms/ | AdSense, general legal |
| Affiliate Disclosure | /disclosure/ | FTC, AdSense |
| About | /about/ | AdSense quality review |

## After approval — optional optimizations

- Disable Auto Ads on the homepage (typically performs poorly for ad
  revenue versus article pages). Set in AdSense dashboard.
- Add manual ad slots in high-CTR positions (after H2, end of article,
  sidebar). Higher RPM than Auto Ads at scale.
- Enable **Ad Balance** at ~80% to surface only highest-RPM ads (small
  impression loss, often higher total revenue).
