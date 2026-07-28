# Growth Plan — From 59 to 10,000 Monthly Visitors

Honest diagnosis followed by a channel-by-channel plan with the math behind each choice. Paid social ads addressed at the end with a recommendation.

## The actual bottleneck

| Reality | Number |
|---|---|
| Articles in catalog | 1,288 |
| Visitors last 30 days | 59 |
| Google organic visitors last 30 days | 5 |
| Bounce rate | 91% |
| Pageviews per visitor | 2.07 |
| Top traffic source | Direct (49 visitors, mostly attribution-stripped bot + referral noise) |

**This is not a content problem.** You have more content than 95% of competitors. The bottleneck is one of these:

1. **Indexation lag.** Google has not yet indexed most of the catalog. Sitemap has 2,086 URLs, but only 5 Google visitors / 30d means almost nothing is ranking.
2. **Domain authority.** No backlinks → Google can't trust the site enough to rank competing pages.
3. **Distribution.** Zero referral traffic from Reddit, Pinterest, YouTube, LinkedIn, or newsletter activity.

Indexation will compound naturally over the next 60-90 days from the work shipped today (Skimlinks live, 178 internal links, 131 new articles, IndexNow already pinged Bing/Yandex). Authority and distribution are the levers we can pull now.

---

## Channel-by-channel ROI math

### 1. Organic SEO — already compounding (KEEP)
- Time to impact: 60-180 days
- Effort: 5-10 hours/week on content + link building
- Expected ramp: 50 → 500 → 5,000 → 20,000 monthly visitors over 12 months
- Cost: zero direct, but slow

The work shipped today (131 new articles, 178 internal links, Skimlinks for monetization) is exactly the right SEO investment. Nothing more to do here this week beyond letting Google crawl.

### 2. YouTube Shorts — the council's chosen distribution channel (PRIORITIZE)
- Time to impact: 30-90 days for first viral hits
- Effort: 5 hours/week to film + edit + publish 3-5 shorts/week
- Expected ramp: 0 → 5,000 monthly views → 500 monthly site visitors (10% CTR from bio link)
- Cost: $0 (DIY) or $200/month for a tech-on-camera contractor

You have the Reddit Intel demand signal pipeline already producing YouTube Shorts candidates. You just need someone with a face and a phone. Each Short script is a 30-60 second answer to a specific high-intent question.

**What I'm shipping today:** a script-generator that turns the Reddit Intel JSON output directly into camera-ready scripts (hook, problem statement, fix, call-to-action) with bio-link instructions, hashtags, and thumbnail copy. See `scripts/shorts-script-gen.py`.

### 3. Pinterest — sleeper hit for residential repair (PRIORITIZE)
- Time to impact: 60-120 days  
- Effort: 1-2 hours/week for 10 pins
- Expected ramp: 0 → 500 monthly site visitors within 90 days
- Cost: zero
- Why it works: Pinterest indexes pins fast, pins compound for years, residential appliance audience does NOT mind clicking out, and most pins are saved into "DIY home" boards that re-surface for years.

**What I'm shipping today:** a pin-description batch for the 50 highest-traffic residential appliance posts. You sign up at pinterest.com/business/create, build 10 image templates in Canva (30 min once), batch-create pins via Tailwind (or schedule manually).

### 4. Beehiiv newsletter — already plumbed, needs cadence (ACTIVATE)
- Time to impact: immediate
- Effort: 1 hour/week to write + schedule
- Expected ramp: each send drives 100-500 click-backs once list passes 1,000
- Cost: Beehiiv free tier covers up to 2,500 subscribers

Email capture is live on every post and the PDF is delivering. What's missing is the broadcast cadence — sending the list anything at all. A weekly digest of new articles + one "deep dive" piece earns trust and drives repeat visits.

**What I'm shipping today:** a script that reads the last 7 days of new articles + assembles a 4-section newsletter draft (HVAC / Refrigeration / Drives & CNC / Buying Guides) ready to paste into Beehiiv composer.

### 5. Backlink outreach — slow but durable (RAMP)
- Time to impact: 30-90 days per earned link
- Effort: 30 min per outreach email, 5-20% reply rate
- Expected ramp: 2-5 backlinks/month from DR 30+ sites within 90 days
- Cost: zero direct

The site needs links from HVAC trade schools, contractor blogs, manufacturer resource pages. We have the outreach templates from earlier (parts-town, johnstone, automation-direct). The same playbook works for trade schools and "useful resources" pages.

**What I'm shipping today:** a prospect-list generator using DuckDuckGo to find HVAC trade school resource pages + a personalized outreach template tied to specific Reddit threads where you helped first.

### 6. LinkedIn — niche B2B for industrial controls content (LOW PRIORITY)
- Time to impact: 30-90 days
- Effort: 2 hours/week
- Expected ramp: small but high-intent (50-200 monthly visitors at maturity)
- Cost: zero

Only worth doing for the VFD/CNC/industrial vertical. Residential HVAC content doesn't fit LinkedIn audiences. Worth setting up if you have 15 min, skip otherwise.

### 7. Paid social ads — DO NOT, YET (DEFER)
Read the math:
- HVAC-related CPCs on Meta/Google: $1-5
- Current visitor conversion to affiliate click: unknown but call it 10% generously
- Current avg affiliate commission: $0.50 (Skimlinks pass-through) or $2 (Amazon at 4%)
- Break-even CPC: $0.05-0.20

You'd be paying $1-5 to earn back $0.20. The math literally cannot work yet.

**When paid ads start to make sense:**
1. Once email list passes 1,000 subscribers (you can retarget warm audiences)
2. Once site has 10K+ monthly visitors (enough conversion data to optimize)
3. Once you've identified your top 10 highest-EPC products via Skimlinks dashboard (you optimize for those, not all traffic)

Realistic timeline: **revisit paid ads in 90 days.** Until then, the same dollars are better spent on:
- $200/month for a YouTube Shorts-on-camera contractor
- $100/month for a Canva Pro + Tailwind Pinterest scheduler
- $300/month for a Beehiiv paid plan that unlocks audience segmentation (once you cross 2,500 subs)

---

## 90-day execution plan

### Days 1-7 (this week)
- [ ] **Skimlinks dashboard: exclude amazon.com / amzn.to / amazon.co.uk** (2 min, only thing protecting your existing 100% Amazon commission)
- [ ] **Pinterest business account signup** (5 min at pinterest.com/business/create)
- [ ] **First Beehiiv weekly digest** (drafted by the script I'm shipping)
- [ ] **Add UTM tracking to outbound affiliate links** (so Plausible attribution works for which posts/sources drive clicks)
- [ ] **Decide on YouTube Shorts on-camera talent**: yourself, a hired contractor at $50/video, or skip

### Days 8-30
- [ ] **Ship first 10 YouTube Shorts** from the Reddit Intel demand signals (already classified for you)
- [ ] **Ship first 20 Pinterest pins** from the batch I'm generating
- [ ] **Send Beehiiv digest weekly** (Tuesdays 10am Eastern is the proven slot for B2B technical)
- [ ] **Send 10 backlink outreach emails** to HVAC trade schools
- [ ] **Check Plausible numbers** at day 30 — expect 100-200 visitors, organic should be 15+

### Days 31-60
- [ ] Continue YouTube Shorts at 3-5/week, scaling whichever performs
- [ ] Continue Pinterest at 5 pins/week  
- [ ] **Re-evaluate paid ads** once email list passes 250 subscribers
- [ ] **Apply for direct affiliate programs that beat Skimlinks pass-through** (ShareASale + AutomationDirect, RepairClinic, Impact pending applications)
- [ ] Plausible target: 500 monthly visitors

### Days 61-90
- [ ] Identify top 10 Pinterest pins by saves, double down with more like those
- [ ] Identify top 3 YouTube Shorts by retention, double down
- [ ] **Apply for Mediavine Journey** once at 10K monthly sessions (ad network — direct CPM income on top of affiliate)
- [ ] Plausible target: 2,000 monthly visitors
- [ ] **Now revisit paid ads** with a $500 test budget on Meta retargeting your email list

---

## Honest assessment on automation

What can be automated end-to-end:
- ✅ Article generation (already automated via your existing pipeline)
- ✅ Internal linking (just shipped)
- ✅ Schema injection (Layout.astro does it)
- ✅ Sitemap + IndexNow pings (existing postbuild script)
- ✅ Newsletter draft generation (shipping today)
- ✅ YouTube Shorts script generation (shipping today)
- ✅ Pinterest pin description batch (shipping today)
- ✅ Backlink prospect list (shipping today)

What CANNOT be automated (platform TOS forbids or quality demands human):
- ❌ Posting to YouTube (you upload, but the script is ready)
- ❌ Posting to Pinterest (manual or via paid Tailwind tool, but the descriptions are ready)
- ❌ Sending the newsletter (you click Send in Beehiiv composer, draft is ready)
- ❌ Recording the videos (face on camera)
- ❌ Sending the outreach emails (sent from your address)

The 80/20 here: I do the work where automation works, you do the publishing.

---

## What I'm shipping right now

After this doc, the next commits add:

1. **`scripts/shorts-script-gen.py`** — turns Reddit Intel output (or any error-code thread) into a 30-60 second YouTube Shorts script with hook, fix, CTA, hashtags, thumbnail copy
2. **`scripts/pinterest-pin-batch.py`** — generates pin descriptions for the 50 highest-traffic residential appliance posts
3. **`scripts/newsletter-digest.py`** — assembles last-7-days articles into a Beehiiv-ready weekly digest with link tracking
4. **`scripts/backlink-prospects.py`** — generates a CSV of HVAC trade school + contractor resource pages worth outreach
5. **`scripts/utm-on-affiliate-links.py`** — adds UTM tracking to outbound merchant URLs across the catalog so Plausible can show conversion attribution

All idempotent, all run-on-demand, all push outputs to a `growth-pipeline/` directory at the repo root that you check before each cadence step.

---

## On paid advertising specifically

You asked whether to run social advertising. **My straight answer: not for at least 60 days.** Here's the trigger criteria for when:

| Trigger | Why |
|---|---|
| Email list crosses 1,000 subscribers | You can run retargeting ads to warm audiences at $0.10-0.30 CPC, which IS profitable |
| Plausible shows 5,000+ monthly visitors | You have enough conversion data to find which articles are worth amplifying |
| Direct affiliate programs activated (ShareASale, Impact, CJ) | Higher commission rates make paid economics workable |
| At least one product/article hitting $50+/month affiliate revenue solo | You amplify the winner instead of broad-spraying |

Until then, every dollar you spend is better placed on:
- A YouTube Shorts contractor ($50/video × 4 = $200/month, compounds for years)
- Canva Pro ($15/month) for higher-quality pins
- Beehiiv paid plan IF list grows past 2,500 subscribers

Total recommended monthly spend right now: **$215** on production help, **$0** on ads.

Re-check this calculus on 2026-07-20.
