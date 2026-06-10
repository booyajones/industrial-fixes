# errorcodefixes.com — Design Excellence Plan (swarm, 2026-06-10)

## SYNTHESIS

I'm the chief design officer. Here's my decisive plan. No additional research needed — the six critiques give me pixel-level ground truth (verified CSS tokens, contrast ratios, tap-target measurements). My job is to synthesize and resolve disagreements, not re-investigate.

---

# errorcodefixes.com — ONE Decisive Design Plan

## 1) HONEST VERDICT

**Overall design score: 48/100. No, the current design is not excellent — it's competent but generic, and it leaks trust at the exact moments that drive traffic and revenue.**

The site has good bones (clean Astro-static build, fast, honest "we don't sell parts" positioning, a real conversion skeleton on article pages) sitting under a skin that screams "AI content farm in a nice template." Four defects do almost all the damage: the harsh saturated orange `#E6531D` used as an H1/headline color (reads "alarm" and "coupon affiliate blog," and fails WCAG AA on every text use under large size), six mismatched OS emoji as the primary icon system (the single loudest amateur tell — a magnifying glass for "oven," a satellite dish for "microwave"), zero original imagery anywhere (ceding iFixit's entire defensive moat and starving the page of links/shares/Google image signals), and the buried expertise — three real credentialed technicians exist on `/methodology` but every article shows a faceless "Editorial Team" byline. The expertise and the conversion logic are real; they are just unrendered. This is a 6-to-8-week design problem, not a rebuild.

---

## 2) THE DESIGN DIRECTION — "The Instrument-Grade, Honest Diagnostic"

Adopt one identity, used everywhere: **the neutral, technical, honest diagnostic instrument** — iFixit's precision and a Bloomberg-terminal confidence, in a space where every competitor is a cluttered parts catalog. This is the open lane: nobody owns "the independent appliance error-code decoder that tells you when *not* to buy a part." Make that honesty *visible* as a design system.

### Color palette (replace the tokens — this is the contested decision; here's the ruling)

All six critiques agree on the core move: **navy becomes primary, orange gets demoted to a rare accent, headlines go to ink.** The only disagreement is the exact accent value. VISUAL says `#D2461A`, MOBILEPERF proved with measured contrast that text-orange needs `#C2410C` (4.9:1) to pass AA, DIAGNOSE suggested terracotta `#C2410C`. **Ruling: split the token into two roles** — this resolves the conflict cleanly and is the highest-precision fix in the whole plan.

| Token | Role | Value | Why |
|---|---|---|---|
| `--ink` | Headlines, body | `#10182A` | Near-black, navy bias. **H1 is NEVER orange.** 16:1 contrast. |
| `--brand-700` | Chips, nav, primary brand | `#15233F` | Deep navy — the spine of the identity |
| `--brand-500` | Brand mid | `#1B2A4A` | Existing navy, kept |
| `--accent-fill` | CTA button backgrounds only | `#D2461A` | Confident orange on white text (7:1) — buttons only |
| `--accent-text` | Orange *text* / links / markers | `#C2410C` | Passes AA (4.9:1) on cream — resolves the MOBILEPERF failure |
| `--bg` | Page | `#FAFAF8` | Lighter than current cream; less "vibrating" |
| `--surface` | Cards | `#FFFFFF` | True white behind content + diagrams (the iFixit trick) |
| `--border` | Hairlines | `#E4E2DB` | |
| `--diy` | DIY-friendly | `#0E7C5A` | Green tier |
| `--intermediate` | Intermediate | `#B45309` | Amber tier |
| `--pro` | Call a pro | `#B91C1C` | Red tier |

**Hard rule: orange appears at most twice per viewport** (one primary button + one marker). Everything structural is navy/ink. The brown-vs-orange button inconsistency COMPETITIVE flagged disappears because `--accent-fill` is now the single button color.

### Type pairing
- **Display / H1–H2:** Hanken Grotesk or Geist (free, confident grotesque). H1 → **36–40px / 680 weight / -1.5% tracking**, color `--ink`. This is the second-biggest premium jump after killing the orange.
- **Body:** **Inter** (regular, *not* Inter Tight — Tight is too condensed for long repair prose) at **17px / 1.65**.
- **Code chips:** JetBrains Mono or Geist Mono. Apply the navy mono chip styling to *every* inline error-code mention (`3C`, `4E`) — instant ownable texture. **Preload the one code-font woff2** to kill the FOUT flash MOBILEPERF measured.

### Layout system
- **12-col grid, 1200px max, 24px gutters.** Article reading measure stays ~680–720px (readable) but the frame widens to ~1120px with a **sticky right rail (~320px)** holding the conversion engine. This resolves the half-empty-desktop complaint AND keeps the CTA always on screen. (Ruling on rail side below.)

### Icon system
Kill all six emoji. **One Lucide/Phosphor-based line-icon set, navy `#15233F`, 1.75px stroke, 24px grid**, shipped as a single inline SVG sprite (~3–4KB, zero CLS, crisp on retina). Each icon `aria-hidden="true"` with the visible text label doing the talking (fixes the MOBILEPERF screen-reader defect simultaneously). Same icons on homepage grid, /diagnose, category headers, and the difficulty/time/tools strip.

### THE distinctive signature element — the "Diagnostic Readout" card
This is the one component that makes the brand instantly recognizable and is the thing people screenshot into Facebook groups. Replace the plain yellow "Quick Answer" box with a **navy, monospace, instrument-style readout card**:
- Error-code mono chip (navy on white) at top
- **Verdict band:** "Most likely: clogged drain filter — 78% of 3C cases" with a confidence bar
- **Severity badge:** the 3-tier scale (DIY-FRIENDLY green / INTERMEDIATE amber / CALL A PRO red), never color-alone (icon + label)
- **Three-stat strip:** Time · DIY cost ($80–150) · Pro cost ($150–300)
- **Honesty line baked in:** "Don't buy a pump yet — check the filter first." — the trust moat made visual
- **The most-likely buyable part with name + price + one button** (the conversion fix, see below)

Three repeatable motifs become the brand: **(1) the navy mono error-code chip, (2) clean navy line-diagrams on white, (3) the Diagnostic Readout card.** None of the competitors own this trio.

---

## 3) PRIORITIZED ROADMAP

Ranked by combined impact on **trust + traffic + conversion**. The first five are **DO FIRST**.

**[DO FIRST] 1. Split the orange token; recolor H1s to ink; one button color.**
Engineer: Replace `--accent:#e6531d` with the dual-token system above. H1/H2/eyebrow labels/card-title links/inline `→` links → `--ink` for headers, `--accent-text` (`#C2410C`) where orange text is wanted. All buttons → `--accent-fill` (`#D2461A`) bg + white text. *Impact:* fixes ~12 WCAG failures, kills the "content-farm/coupon" perception, and makes every CTA pop instead of competing with headlines. 1–2 hours, biggest perceptual jump per unit effort.

**[DO FIRST] 2. Replace all emoji with the navy inline-SVG line-icon set.**
Engineer: Build one SVG sprite (9 appliances + UI glyphs), navy 1.75px stroke, each `aria-hidden="true"`. Swap on homepage grid, /diagnose tiles, category headers. *Impact:* removes the single loudest amateur tell; fixes the screen-reader semantic bug; unifies the brand surface.

**[DO FIRST] 3. Surface the real humans + add original visual media to the article template.**
Two moves, one template change. (a) Replace "Editorial Team" byline with **"Reviewed by [40px avatar] Marcus Webb · EPA 608 · NATE"** (route by vertical: HVAC/fridge→Webb, kitchen→Rutherford, controls→Kowalski), linked to a real bio; rebuild `/authors/` into a 3-card team page with headshots + credential badges; add `author`+`reviewedBy` Person schema with `hasCredential` to the HowTo JSON-LD; split published vs. last-reviewed dates. (b) Add **one labeled navy SVG cutaway diagram per guide** (filter→sump→drain pump→hose, suspect part highlighted) + **part thumbnails in the parts table**. *Impact:* this is the E-E-A-T + link/share moat in a single template edit. Diagrams are static/fast/ownable and out-execute iFixit's dim photos for *diagnosis*.

**[DO FIRST] 4. Rebuild the parts table into price-anchored product cards (the conversion fix).**
Engineer: Kill the 3-column table. Each part = a card: thumbnail (left) + name/fit-note/price-chip "~$45–70" (center) + **one dominant filled button "See price on Amazon →"** (right). Demote RepairClinic/PartSelect to a small "Other sellers" text row (one primary action, not three co-equal links). Add a micro-trust line under each card: "OEM part · check it fits your model." Surface the most-likely part (name + price + button) **inside the Diagnostic Readout above the fold.** Make the mobile sticky bar price-aware: **"Get the drain pump → ~$55"**. *Impact:* fixes the weakest pixel on the money page — the moment of buying intent.

**[DO FIRST] 5. Two-column article shell with sticky conversion rail + 44–48px tap targets.**
Engineer: Frame ~1120px, prose 680–720px, sticky **right** rail (~320px) = Diagnostic Readout + diagram + Get-the-Part CTA + mini parts list + "On this page" TOC. `min-height:44px` on every button/link-as-button (Amazon CTA goes from 30px → 48px); global `:focus-visible{outline:3px solid var(--accent-text);outline-offset:2px}`. *Impact:* fixes empty-desktop + always-on-screen CTA + closes the WCAG tap-target/focus failures in one layout pass.

---

**6. Build the Diagnosis Card + dynamic OG image endpoint for /diagnose.** Render the Diagnostic Readout in-place on appliance+code selection, with a "Share" control generating an OG image via Astro/Satori (`/diagnose/og/[brand]-[appliance]-[code].png`) at a stable URL (`/diagnose/samsung-dishwasher-3c`). *Impact:* converts /diagnose from a dead-end picker into a shareable, linkable asset — the primary traffic lever for the tool page.

**7. Finish /diagnose below the fold.** Add most-searched code chips (Samsung 3C, LG OE, Whirlpool F2E1), a "symptom picker" path for users who can't read a code, a trust strip ("Independent · 3,723 codes · we tell you when not to buy"), and a 3-step "how it works" row. 64px monospace input, 3×3 icon grid (add the 3 missing appliances), 2-col desktop shell. *Impact:* stops the page looking broken; adds SEO content density.

**8. Homepage: real code-search field in the hero + rebuild "Most Common Fixes" as cards.** A big code-entry input IS the hero product. Replace the 2009-style orange-text-link blog roll (with calendar emoji) with cards carrying the mono code chip + diagram thumbnail + severity dot. *Impact:* authority + conversion at the front door.

**9. Promote the honesty positioning into reusable components.** A fixed "Independent — we don't sell parts" trust strip under every H1; inline affiliate disclosure right above the first parts card; a "No-Buy Recommended" amber badge when the fix is free; a collapsible "How we verified this fix" block citing the OEM source. *Impact:* the differentiator competitors literally cannot copy.

**10. Lighten/finalize the surface system + CWV protection.** `#FAFAF8` page, white content cards with soft navy-tinted shadow, deepen the cream-on-cream flatness into layered depth. Preload the code-font woff2; aspect-ratio boxes on all new diagrams/OG images; affiliate scripts load on idle/interaction. *Impact:* premium depth without sacrificing the green Core Web Vitals.

**11. Earned social proof.** "Did this fix work? Yes/No" tap at the fix end; once data exists, surface honest "Helped 412 of 460 people." *Impact:* iFixit's strongest trust mechanic, earned not claimed.

---

## 4) THE SINGLE BIGGEST LEVER

**Add original visual media — one labeled navy SVG diagram per guide plus part thumbnails — and bind it to the Diagnostic Readout card that surfaces the most-likely part (name + price + button) above the fold.**

Five of six critiques independently named "zero imagery" as the existential gap, and the conversion critique named "the part as a flat text link" as the weakest pixel. This one move attacks both at once: the diagram closes the iFixit moat (earns the links/shares/Google-image signals that drive *traffic*), and binding it to the price-anchored Readout captures the decided buyer before the 1,500-word scroll (drives *conversion*). It also makes the page visibly "someone actually did this," which is the *trust* unlock. Diagrams over photos is the right call here — they're cleaner for diagnosis, original, defensibly yours, and CWV-safe across 3,700 guides where per-article photography never could be.

If only one thing ships: **the diagram + the above-the-fold price-anchored Diagnostic Readout.**

---

## 5) SUCCESS CRITERIA

The design is excellent when all of these are true:

**Trust / E-E-A-T**
- Every article shows a named, credentialed, linked human reviewer with avatar; `/authors/` has real headshots + badges; `author`/`reviewedBy`+`hasCredential` schema validates in Google Rich Results.
- The "we don't sell parts" independence line appears as a fixed component on every money page, not a buried sentence.

**Visual excellence**
- Zero emoji anywhere; one coherent navy line-icon set sitewide.
- H1s are ink, never orange; orange appears ≤2× per viewport; no brown-vs-orange button inconsistency.
- Every money page carries ≥1 original labeled diagram + part thumbnails. The Diagnostic Readout is the recognizable signature element.
- A neutral designer's 5-second read is "credible diagnostic tool," not "affiliate blog." Re-score the six dimensions: target **≥8/10 average** (from 4.5–6.5 today).

**Accessibility (pass/fail)**
- All text ≥4.5:1 (large ≥3:1); WCAG 2.2 AA clean on contrast, focus-visible, and tap targets (≥44px, Amazon CTA ≥48px). Verified in-browser, not asserted.

**Conversion**
- Parts presented as price-anchored product cards with a single dominant CTA; most-likely part + price + button visible above the fold inside the Readout; mobile sticky bar names the part and price.
- Measured lift in affiliate CTR on article pages (instrument it).

**Traffic / shareability**
- /diagnose produces a stable-URL shareable Diagnosis Card with a dynamic OG image; pasting any code URL unfurls the readout.
- Original diagrams begin earning inbound links / appearing in Google image results; /diagnose shows measurable share/referral traffic instead of acting as a dead end.

**Performance (non-negotiable guardrail)**
- Core Web Vitals stay green (LCP/INP/CLS) after all media is added; code-font preloaded; no CLS from diagrams/OG images.

Ship DO-FIRST 1–5 and the site jumps from ~48 to ~75 and stops looking like a content farm. Ship 6–11 and it becomes the distinctive, instrument-grade, honest diagnostic brand that occupies the one lane iFixit and the parts-store incumbents left wide open — target **85+**.

---

# Full critiques


## VISUAL
I have iFixit's identity principle ("Blue and Black") confirmed, and I have all the hard data I need on errorcodefixes itself. I have direct visual evidence of all three pages plus exact CSS tokens. That's enough to write a precise, opinionated critique. Let me close out the browser context cleanly and deliver.

I have everything needed. Here is my critique.

---

# VISUAL DESIGN & BRAND EXCELLENCE — errorcodefixes.com

## Score: 4.5 / 10
**Verdict: Clean and competent, but visually generic and trust-leaking — it reads "AI content farm in a nice template," not "the authoritative repair tool." The harsh orange, single-font system, half-empty desktop column, and total absence of imagery are the four things holding it back from premium.**

I verified everything live at 1440px, pulled the actual CSS tokens, and shot all three pages. Confirmed facts driving the score: `--accent:#e6531d`, `--brand:#1b2a4a`, bg `#F4F3EF`, text `#0F1418`; the article **H1 is literally `rgb(230,83,29)` orange at only 30px/700**; type is **Inter Tight and nothing else** (no pairing); article content column is **768px inside a 1571px viewport** (under half the screen, ~400px dead gutter each side); category and diagnose icons are **six mismatched emoji** (woven-basket, blue spiral, blue cube, pale dishware glyph, magnifier-on-skillet, satellite dish); and there is **zero original imagery** anywhere — no diagrams, no part photos, no illustrations. The /diagnose page is a hero + one row of 6 emoji buttons and then empty cream to the fold.

---

## What's actually good (keep these)
- The **navy `ERROR CODE 3C` monospace chip** is the single best brand asset on the site — distinctive, ownable, "expert tool." It should become the visual spine of the whole identity, not a one-off.
- The **conversion skeleton on the article page is genuinely strong**: yellow Quick Answer box, Jump-to-Fix / View-Parts buttons, MOST LIKELY verdict, DIY-friendly pill, difficulty/time/tools strip. Good CRO bones. The problem is purely visual dressing, not IA.
- Restraint. It's not cluttered or ad-stuffed. That's a real head start over RepairClinic's busy retail look.

---

## The 5 problems, ranked by damage to "premium + trustworthy"

### 1. The orange (#E6531D) is doing brand damage — biggest single fix
At full saturation on a warm cream, #E6531D vibrates. Using it as the **H1 color** makes your most important headline read as a *warning/alarm* (error-red-orange), which is psychologically wrong for a "we'll calmly fix this" promise — and it's the #1 reason the site feels cheap/content-farm. Saturated orange as a primary text color is the most reliable "low-budget" tell on the web.
**Fix:** Demote orange to a single accent role (CTAs and one hairline only), darken and de-saturate it, and **never use it for body headlines.** Headlines go near-black. See palette below.

### 2. Zero imagery — the existential gap (this is the moat you're ceding)
iFixit's entire defensibility is **original step photos on clean white.** You have none. On the money page a panicked user gets a wall of gray text with no visual confirmation they're in the right place or looking at the right part. This kills time-on-page, kills shares/links (nobody links to a text wall), and quietly tells Google "thin content."
**Fix (in priority order):**
- **A simple line-diagram per appliance** showing where the part lives (drain pump, filter, sump). A consistent 2px stroke illustration set in navy = instantly more credible than any competitor and cheap to produce.
- **One labeled "where is this part" diagram** inside every causes/parts section.
- **Part thumbnails in the parts table** (you can pull OEM product images via your affiliate feeds — RepairClinic/PartSelect/Amazon all expose them).
- A small **"what the code looks like on your display"** mock (a rendered panel showing "3C") as the hero visual — ownable, on-brand with the chip, and reassuring.

### 3. The half-empty desktop column
768px of content in a 1571px viewport looks unfinished and amateur on desktop — it's the "blog default" look. You're wasting the exact real estate where you could place a sticky utility rail that *also lifts conversion*.
**Fix:** Move to a **two-column shell on the article page** — keep prose at a readable ~680–720px measure, but add a **~320px sticky right rail** for: the Quick Answer / Get-the-Part CTA, the diagram, "is this DIY?" verdict, and a mini parts list. Total content frame ~1120–1180px max. The page stops feeling empty AND the CTA is always on screen.

### 4. Emoji icons — the clearest amateur tell
Six emoji in six rendering styles/sizes/color temperatures in one row is the thing a designer notices in 0.5 seconds. It instantly undercuts "expert tool."
**Fix:** Replace with **one coherent line-icon set** — single 1.75px stroke, navy `#1B2A4A`, rounded joins, drawn on a consistent 24px grid. Use **Lucide** or **Phosphor (regular weight)** as the base and either use their appliance-adjacent glyphs or commission 9 custom ones (washer, dryer, fridge, dishwasher, range, microwave, furnace, heat-pump, water-heater) in that exact style. Custom is worth it — it becomes part of the brand and nobody else in this space has it.

### 5. No typographic personality
One font (Inter Tight) at one or two weights means nothing on the page has *voice*. Premium tools earn authority partly through a confident display/body pairing and a deliberate type scale.
**Fix:** see type pairing below.

---

## The redesign direction (specific, buildable, stays Astro-static + fast)

### Palette (replace the tokens)
Anchor the brand on the navy you already own; make orange a disciplined accent.

| Role | Now | New | Notes |
|---|---|---|---|
| Ink / headlines | `#0F1418` | **`#10182A`** | near-black with a navy bias, ties to brand |
| Brand navy | `#1B2A4A` | **`#15233F`** (`brand-700`), `#1B2A4A` (500), `#2E4574` (400) | the chip color becomes a real scale |
| Accent (CTA only) | `#E6531D` | **`#D2461A`** primary / **`#B83D14`** hover | knocked back ~8–10% sat, deeper — reads "confident" not "alarm" |
| Background | `#F4F3EF` | **`#FAFAF8`** page / `#FFFFFF` content cards | lighten the cream; reserve true white behind diagrams (iFixit trick) |
| Surface | `#E8E5DC` | **`#F1F0EC`** | your current card beige is too low-contrast on cream |
| Border | `#D9D6CE` | `#E4E2DB` hairlines / `#15233F` for chips | |
| Success | green pills | **`#0E7C5A`** | slightly deeper for AA on light |
| Warn (Quick Answer) | yellow | **`#FBF4DE` bg / `#8A6D1A` text / `#15233F` heading** | keep the box, ditch the orange heading |

Rule: **orange appears at most twice per viewport** (one primary button + one hairline/marker). Everything structural is navy/ink. This alone moves the site from "content farm" to "tool."

### Type pairing
- **Display / H1–H2:** a confident grotesque with character — **"Geist"** or **"Söhne"** (if budget) or free **"Schibsted Grotesk" / "Hanken Grotesk"**. H1 → **36–40px / 680 weight / -1.5% tracking**, ink color (not orange). This is the single biggest "premium" upgrade after killing the orange headline.
- **Body:** **Inter** (regular Inter, not Tight) at 17–18px / 1.65 line-height for the long repair prose. Tight is too condensed for body reading.
- **Code/error chips:** keep a mono — **"JetBrains Mono"** or **"Geist Mono"**. The chip is your signature; lean into it. Put the mono code-chip styling on *every* error code mention inline in the body too (`3C`, `4E`) — instant ownable texture.
- Lock a type scale: 13 / 15 / 17 / 20 / 24 / 30 / 38 and stop improvising.

### Layout system
- **12-col grid, 1200px max, 24px gutters.**
- **Homepage:** category grid → real cards on **white** (not beige-on-cream), `#15233F` line icon top-left, subtle `0 1px 2px rgba(16,24,42,.06)` shadow, 12px radius, hover lifts to navy 1px border. "Most Common Fixes" list → give each row a **brand thumbnail/diagram chip + the mono code chip** instead of a calendar emoji; that one change kills the content-farm feel.
- **Article (money page):** two-column shell described above. Sticky right rail = conversion engine. Prose measure 680–720px. Add a **diagram block** right under Quick Answer.
- **/diagnose:** this page is half-built. Fill below the appliance row with: a **trust strip** ("Independent — we don't sell parts," "Technician-reviewed," "3,723+ codes"), **most-searched codes as tappable mono chips**, and a **"how diagnosis works" 3-step** mini-explainer with the line icons. Right now it looks broken.

### Icon system
One Lucide/Phosphor-based or custom line set, `#15233F`, 1.75px stroke, 24px grid, used **everywhere** (categories, diagnose, section markers, the difficulty/time/tools strip). Replaces 100% of emoji. Ship as a single inline SVG sprite — keeps CWV pristine.

### The "confident expert tool" signature
Three repeatable motifs that, used consistently, become the brand: **(1)** the navy mono error-code chip, **(2)** clean navy line-diagrams on white, **(3)** ink headlines with a single deep-orange accent marker. That trio is distinctive, none of the competitors (busy retail RepairClinic/PartSelect, photo-heavy iFixit) own it, and it differentiates you as the *neutral diagnostic authority* — which is exactly your honest "we don't sell parts" positioning made visible.

---

## Fastest path to +3 points (do these 5, in order)
1. **Kill the orange H1** → ink headlines, deepen accent to `#D2461A`, restrict orange to CTAs. *(1 hour, biggest perceptual jump.)*
2. **Replace all emoji with one navy line-icon set.** *(Removes the clearest amateur tell.)*
3. **Add one diagram + part thumbnails to the article template.** *(Closes the imagery gap; the link/share unlock.)*
4. **Two-column article shell with sticky CTA rail.** *(Fixes the empty desktop AND lifts conversion.)*
5. **Finish /diagnose** below the fold (trust strip + popular code chips). *(Stops it looking broken.)*

Sources: [iFixit — Blue and Black: Our Identity, Explained](https://www.ifixit.com/News/12196/behind-blue-and-black), [Repair Clinic](https://www.repairclinic.com/), [PartSelect (15 Leading Appliance Repair Websites 2025)](https://www.wpsupportwebdevelopment.com/blog/15-leading-appliance-repair-websites/). Live inspection of errorcodefixes.com homepage, /posts/samsung-dishwasher-3c-error-code/, and /diagnose/ at 1440px, plus computed CSS tokens (`--accent:#e6531d`, `--brand:#1b2a4a`, content max-width 768px).


## CONVERSION
I have enough to deliver a precise, brutally honest conversion critique. The article page is the money page and that's where I'll concentrate.

---

**CONVERSION / CRO SCORE: 6.5 / 10**

**Verdict:** Strong honest-broker positioning and decent CTA bones, but the part itself is presented as a flat text-link footnote with zero price, zero photo, zero stock/return reassurance — the exact moment of buying intent is the weakest pixel on the page.

---

**The core problem (read this first):** Your article does an A+ job creating buying intent ("MOST LIKELY: drain pump," ranked-% causes, DIY-vs-pro math) and then a D- job *capturing* it. The parts table is three columns — Part / Notes / Links — with **no price, no thumbnail, no rating, no in-stock or returns signal**, and the Amazon link renders as a bare `[Amazon]` text link sitting beside `Find it at RepairClinic →`. At the precise instant a panicked person decides "fine, I'll buy the pump," you hand them a spreadsheet cell. That is where click-through leaks. Competitors win this exact moment: RepairClinic puts price + "365-Day Returns" + model-fit check next to a styled buy button; iFixit puts an actual part photo and a "Fix Kit" bundle. You have neither.

**Prioritized, concrete fixes (highest CTR lift first):**

**1. Rebuild the parts table into product cards — biggest single lever.** Kill the 3-column table. Replace each part with a card: left = a part thumbnail (Amazon product images are allowed via the Product Advertising API or just OEM stock imagery), center = part name + a one-line fit note + a price/price-range chip ("~$45–70"), right = a *single, dominant* button. A button with a price beats a bare word every time. Right now `[Amazon]` is indistinguishable from body text. Make it a filled `#E6531D` button labeled **"See price on Amazon →"** (price-anchored CTAs convert better than the bland "View on Amazon"). Demote RepairClinic/PartSelect to a small secondary "Other sellers" text row beneath, so you present *one* primary action, not three competing equal-weight links.

**2. Put trust *at the button*, not just at the top of the page.** Your "Independent — we don't sell parts" line is great brand trust but it's 1,500px away from the buy decision. Add a micro-trust strip directly under each part card: "OEM part • fits Samsung DW80R…(model match) • check returns before buying." Borrow RepairClinic's move — a tiny "Confirm it fits your model" expander next to the part removes the #1 hesitation ("is this the right one?") that kills the click. Wrong-part fear is the biggest friction at decision point; a model-fit nudge directly lifts confident clicks.

**3. The "Quick Answer" box is your highest-intent real estate — make "View Parts" the dominant CTA.** Currently "Jump to Fix →" and "View Parts →" appear co-equal. The person who already knows it's the drain pump wants the part NOW. Make **"View Parts →"** the filled primary button and "Jump to Fix" the ghost/secondary. Better: in the QUICK ANSWER box, when the most-likely cause is a buyable part, add a third inline element — "Most likely part: Samsung drain pump (~$55) → See on Amazon" — so a decided buyer converts *above the fold* without scrolling through 1,500 words of diagnosis. You're forcing high-intent users to scroll past the whole article to reach the affiliate link (currently first real part link is ~1/4 down + the table is lower). That's lost revenue.

**4. Fix the sticky mobile bar copy and make it price-aware.** "Get the part" is vague. On a 3C drain-pump page it should read **"Get the drain pump → ~$55"** — name the part, show the price. Specificity + price on the sticky bar is the single easiest mobile CTR win, and mobile is where your panicked-at-the-machine visitor lives. Also confirm the sticky bar links straight to the *primary* seller, not to an anchor that makes them choose again.

**5. Reduce decision paralysis — one primary seller per part.** Three equal links (Amazon / RepairClinic / PartSelect) is a classic conversion-killer: choice overload at the decision point lowers total clicks. Pick the highest-converting partner as primary (Amazon for trust/speed, RepairClinic for OEM-fit confidence) and visually subordinate the rest. Don't make a stressed user adjudicate a vendor bake-off.

**6. The orange `#E6531D` on cream is harsh and, worse, it's overloaded.** You use the same bright orange for H1 titles AND primary CTAs. When the page title is the same color as the buy button, the button loses its "this is the action" signal — buttons should be the *only* thing in that hi-vis color. Reserve orange exclusively for CTAs; render the H1 in navy `#1B2A4A`. This is free CTR: it makes every buy button pop instead of competing with headlines. (Also nudge the orange slightly less neon, e.g. a touch deeper/warmer, so it reads premium not "discount banner.")

**7. Add the missing reassurance copy that unblocks the click.** Near the parts cards, one honest line: "Buying the part yourself runs about $80–150 vs $150–300 for a pro." You *have* this math, but it's buried in a separate "When to Call a Pro" section. Move the DIY-savings number adjacent to the part — "frame the purchase as the cheap option" — that's the rational trigger that converts. The savings figure next to the buy button is a proven intent-to-action bridge.

**8. /diagnose dumps intent on the floor.** The tool builds toward "the exact part" but the page is sparse below the fold with no popular-codes, no trending parts, no trust strip. When the AI widget or filter surfaces a code, the result card must carry the same price-anchored buy button as the article — otherwise you've qualified a buyer and given them nowhere to spend. Add a "most-searched codes this week" rail with direct deep-links to the money pages so diagnose becomes a conversion funnel, not a dead-end utility.

**9. Email capture is competing with the affiliate click — sequence it.** The "Get Free PDF" cheat-sheet box appears top *and* bottom. The top placement steals attention from the part at peak intent. Keep the bottom one (post-fix, lower intent = fine to ask for email), drop or shrink the top one so nothing competes with the buy decision in the upper half.

**What NOT to change (it's working for trust):** the byline + "Reviewed 5 days ago," the visible affiliate disclosure, the "we tell you when NOT to buy one" line, and the misdiagnosis "Before You Replace Anything" note. That honesty is your moat versus RepairClinic/PartSelect and it actually *raises* click quality. Don't sacrifice it for aggression — just stop making the honest broker also be a bad merchandiser.

**Single highest-ROI move if you do only one thing:** turn the parts table into price-anchored product cards with a photo and one dominant **"See price on Amazon →"** button, and surface the most-likely part (name + price + button) inside the QUICK ANSWER box above the fold. That captures the decided buyer before the scroll and fixes the weakest moment on the page.

Sources: [iFixit Partnerships](https://www.ifixit.com/Info/Our_Partnerships), [iFixit Commercial Link Policy](https://www.ifixit.com/Info/Commercial_Link_Policy)


## DIAGNOSE
I have enough to anchor the critique. The text fetch already confirms the structural reality you described (6 emoji buttons, two-step flow, empty below fold, no visual media, an "Ask AI" widget exists). I don't need more competitor scraping; iFixit's moat (original step photos on clean white) is well-established. Here is the brutal verdict and redesign.

---

# /diagnose — Score: 3.5 / 10

**Verdict:** A functional appliance picker masquerading as a "tool." It works, but it's a glorified search box with emoji decorations. Nobody screenshots this for Reddit. Right now it has zero reasons to exist as a standalone URL, zero shareable output, and the emoji icons actively read as amateur. To be link-worthy it must produce a *result artifact* (a shareable diagnosis card), not just route you to an article.

The single biggest problem: **the tool ends where the value should begin.** It hands you off to a guide page instead of *being* the experience. A great diagnostic tool gives you an answer-shaped object you want to share. This one gives you a filtered list.

---

## Why it fails at the three jobs

**1. Delightful — No.** Six emoji buttons in one row, a search box, then a wall of cream nothing below the fold. There is no momentum, no progressive reveal, no payoff moment. The interaction is "click, type, get a list of links" — the exact thing a Google search already does better. The emoji set is the tell: 🧺 for washer, 📡 (satellite dish) for microwave, 🍽️ for dishwasher. These are inconsistent metaphors at inconsistent visual weights, and they render differently on every OS. On Windows they're flat, on Mac they're glossy 3D. You cannot build a premium brand on system emoji.

**2. Shareable — No.** There is nothing to share. The whole point of a "shareable interactive asset" is that the *output* is the share unit. Right now the output is a redirect. Compare: people share the iFixit teardown, the "is it worth fixing?" calculator result, the WhatIsMyScreenResolution-style instant answer. Your tool produces no URL-stable, image-able, "look what I found" object.

**3. Link-worthy — No.** Nobody links to a picker. People link to *the definitive thing*: "the appliance error-code decoder," "the repair-vs-replace calculator," "the one chart of every Samsung washer code." The current page has no opinion, no data density, no original asset worth citing.

---

## The redesign: turn /diagnose into "The Appliance Error Code Decoder"

Reposition the page from a router into **the most complete, fastest, most honest error-code decoder on the internet** — with a shareable result card as the deliverable. Three concrete pillars.

### Pillar 1 — Kill emoji. Build a custom icon system.

Replace all six emoji with a **single-weight, 2px-stroke line-icon set** drawn as inline SVG (one sprite, ~4KB, zero layout shift, perfectly crisp on retina, theme-able via `currentColor`). Consistent metaphor, consistent optical size, consistent corner radius (2px). This one change moves the whole page from "amateur" to "designed."

Specifics:
- Icons sit in a **56px rounded square tile** (radius 14px), 1px border `#E3E0D8` on cream, icon stroke in navy `#1B2A4A` at rest.
- **Hover/selected:** tile fills navy `#1B2A4A`, icon flips to cream, subtle `scale(1.02)` + `translateY(-2px)`, 120ms ease-out. A 2px navy ring (`box-shadow: 0 0 0 2px`) marks the selected state — accessible focus, not just color.
- Add a 7th–9th tile to match the homepage's 9 categories (furnace, mini-split, water heater are currently missing from /diagnose — that inconsistency itself reads as broken). Use a **3×3 grid on desktop, 2-col on mobile**, not a single cramped row.

### Pillar 2 — Make it feel like a *machine*, not a search box.

The interaction should feel like operating a diagnostic instrument. Concrete UI:

- **Heading:** drop "Diagnose your appliance" (flat, expected). Use **"Decode your appliance error code"** with a one-line confidence builder underneath: *"3,723 codes decoded. We tell you the real cause, the DIY odds, and when not to buy a part."* (Keeps the honesty positioning, adds the data flex.)
- **Replace the orange.** That `#E6531D` on H1 + CTA is the harsh/dated thing you already flagged. For this page, make the H1 **navy `#1B2A4A`** and reserve a *single* warmer accent — shift orange to a deeper terracotta **`#C2410C`** (or amber `#D97706`) used only on the one primary action and the live result chip. Orange as a structural/heading color is what dates it; orange as a rare action color is fine.
- **The input is the star.** A single large field, 64px tall, monospace placeholder `e.g. 3C, OE, 5E, F21…`, with a navy left-border accent (3px) and a soft inner shadow so it reads as "type here." As the user types, run the existing live-filter — but render results as **rich result rows**, not bare card links: each row shows the **monospace code chip**, the appliance/brand, a one-line plain-English cause, and a colored severity dot (green = DIY / amber = intermediate / red = call a pro). That severity-at-a-glance is the data-design hook competitors don't have.
- **Most-searched codes as instant chips.** Below the field, a row of clickable code chips: `Samsung 3C` `LG OE` `Whirlpool F21` `Bosch E15` `GE H2O`. This fills the dead below-the-fold space, gives the page content density, teaches users the format, and seeds the "popular this week" social-proof loop. Each chip is a navy-outline pill that fills on hover.

### Pillar 3 — The shareable payoff: the **Diagnosis Card**.

This is the entire reason to rebuild the page. When a user selects an appliance + code (or picks a chip), don't just navigate — first **render an instant result card in-place** (then offer "Full fix guide →" as the deep link). The card is the share unit.

The Diagnosis Card (a self-contained component, fixed 16:10-ish ratio so it screenshots cleanly):
- **Top:** brand + appliance + the monospace code chip (navy on cream).
- **Verdict band:** one bold line — *"Most likely: clogged drain filter"* — plus a big **severity badge**: a colored ring with a label (`DIY-FRIENDLY` green / `INTERMEDIATE` amber / `CALL A PRO` red) and a **confidence %** (you already compute likelihood shares on article pages — surface them here: "78% of 3C cases").
- **Three-stat strip:** Time `15–60 min` · Cost to DIY `$80–150` · Cost to hire `$150–300`. This repair-vs-replace math *is* the link-bait. People share "huh, I can fix this for $12."
- **Honesty line baked in:** *"Don't buy a pump yet — check the filter first."* Your independence positioning becomes a visible, screenshot-able trust signal.
- **A "Copy result" / "Share" control** that generates an **OG image** of this exact card (build it once as an Astro/Satori dynamic OG endpoint, `/diagnose/og/[brand]-[appliance]-[code].png`). Now when someone pastes the URL into Reddit/Facebook/iMessage, the unfurl *is* the diagnosis card. That's the mechanic that earns shares — the preview answers the question before the click.
- **Stable, pretty URL:** `/diagnose/samsung-dishwasher-3c`. Linkable, indexable, and the OG image makes every paste look authoritative.

### What fills the page (kill the empty cream)

The desktop emptiness you flagged is fixable with **content that doubles as SEO and social proof**:
1. The **"most-searched this week" code chips** (live-ish, real traffic data you already have).
2. A compact **"How the decoder works"** 3-step row with the custom line icons: *Pick appliance → Enter code → Get the real cause + DIY odds.* (Sets expectations, adds rhythm.)
3. A **trust strip**: "Independent. We don't sell parts." + "Reviewed by the Editorial Team" + "3,723 codes, 40+ brands." Three small lozenges, navy text on cream, hairline dividers.
4. A **"Don't know your code?"** secondary path — a symptom picker (*"It won't drain," "It's beeping," "Water on the floor"*) — so the tool serves the panicked user who can't read a code off the panel. This is the one genuinely additive flow vs. plain search.

---

## Visual system spec (so it looks premium, not harsh)

- **Background:** keep cream `#F4F3EF` but add ONE structural surface — result cards and tiles sit on **pure white `#FFFFFF`** with a 1px `#E3E0D8` border and a *very* soft shadow (`0 1px 2px rgba(27,42,74,0.04), 0 8px 24px rgba(27,42,74,0.06)`). The cream-on-cream flatness is half of why it feels empty; layering white surfaces gives depth.
- **Type:** Inter Tight is fine for UI, but give the H1 real presence — **40–48px, weight 600, tracking -0.02em**, navy. Keep error codes in a true mono (JetBrains Mono or IBM Plex Mono) so chips feel "technical/instrument-grade."
- **Spacing:** the page reads empty because the content column is too narrow and floats. Use a **wider 2-column shell on desktop** (tool left, live-result/most-searched right), max-width ~1120px, generous `clamp()` vertical rhythm. Mobile stacks single-column, tool first.
- **Severity color tokens:** green `#15803D`, amber `#B45309`, red `#B91C1C` — all on white at AA contrast, each paired with an icon/label so it's never color-alone (accessibility).
- **One micro-delight:** when a result resolves, a 200ms count-up on the confidence % and a subtle "scan line" sweep across the card. Tasteful, not gimmicky. Respect `prefers-reduced-motion`.

---

## Honesty / constraint guardrails (stays true to positioning)

- Card never says "buy this part" — it says "most likely cause" + "check X first." Affiliate buttons live on the *full guide*, after the diagnosis, exactly as today. The tool stays the trustworthy front door.
- No manufacturer impersonation: footer keeps "We are not the manufacturer or a parts store."
- All of this is **static-Astro-friendly**: the decoder is client-side filtering over a pre-built JSON index; the OG images are build-time or edge-rendered via Satori; zero heavy JS framework needed. Core Web Vitals stay green because the icon sprite replaces emoji (no font-emoji reflow) and result cards are CSS/inline-SVG.

---

## Prioritized fix list (do in this order)

1. **Ship the Diagnosis Card + OG image endpoint.** This is the single change that converts /diagnose from "picker" to "shareable asset." Highest leverage, do first.
2. **Replace all emoji with the custom inline-SVG line-icon set** in 56px navy tiles. Instantly kills the amateur read.
3. **Add the most-searched code chips + symptom picker** below the field to fill the dead space and serve code-less users.
4. **Recolor:** navy H1, layered white surfaces on cream, terracotta as the *single* action accent (retire orange-as-heading).
5. **Add the trust strip + 3-step "how it works"** so the page has data density and social proof.
6. **Wider 2-col desktop shell + bigger 64px monospace input** so it stops floating in empty cream.

Hit 1–3 and this jumps to a 7. Hit all six and it's an 8.5–9 — genuinely the kind of "appliance error code decoder" people bookmark and paste into a Facebook group when their neighbor's washer throws a code.

**Sources:** [RepairClinic error codes](https://www.repairclinic.com/Repair-Library/Article/5/What-Your-Appliance-Error-Code-Really-Means), [PartSelect Fault Codes](https://www.partselect.com/justforfun/Fault-Codes.htm), [AppliancePartsPros Fault Codes](https://www.appliancepartspros.com/repair-help/appliance-fault-codes.html)

Relevant live URLs reviewed: `https://errorcodefixes.com/diagnose`, `https://errorcodefixes.com/`, `https://errorcodefixes.com/posts/samsung-dishwasher-3c-error-code/`


## TRUST
I have everything I need. The competitor benchmark (iFixit) is clear: named authors that never lose attribution, public reputation scores, "X people completed this guide" social proof, and community-visible expertise. RepairClinic/PartSelect lean on thousands of original videos and a massive verified-parts catalog. The current errorcodefixes.com has the raw materials for trust (real named editors with real certs) but hides them. Here is my critique.

---

# TRUST / E-E-A-T / CREDIBILITY DESIGN

## Score: 4.5 / 10

**Verdict:** The expertise is real and documented but architecturally buried -- a faceless "Editorial Team" byline and zero original visual media make a panicked first-time visitor unsure if this is a content farm or a credible technician resource. The fix is mostly surfacing what already exists, not inventing trust.

---

## The single most damaging finding (fix this first)

Your `/methodology/` page names **three real editors with verifiable trade certifications** -- Dana Kowalski (CAP, ISA / industrial controls), Marcus Webb (EPA 608 Universal + NATE / HVAC-refrigeration), James Rutherford (CFESA, 18+ yrs / commercial kitchen), ~50 years combined. This is genuine, link-earning, Google-loved E-E-A-T gold.

It appears on **none** of the places that matter:
- The article byline says only "Error Code Fixes Editorial Team."
- The `/authors/` page says "a small editorial team" with **no names, no photos, no credentials** -- it actively contradicts the methodology page.
- The homepage shows "Technician-written guides" as an unsubstantiated claim.

You built the credibility and then hid it behind two clicks. A first-time visitor in panic mode never reaches it. **The entire trust strategy should be re-architected around making these three people impossible to miss.** That alone moves this dimension from 4.5 to ~7.

---

## What a first-time visitor sees in 3 seconds (and why they don't trust it yet)

1. **A bright `#E6531D` orange H1.** That specific orange reads "deal site / coupon affiliate blog," not "expert resource." High-trust YMYL/repair brands anchor on deep ink (iFixit slate, RepairClinic navy/teal) and reserve saturated color for one CTA only. Right now orange does double duty (H1 + CTA), which subconsciously equates "the headline" with "the buy button" -- the exact pattern that signals *monetized content, not help*.
2. **A faceless "Editorial Team" byline next to "Reviewed 5 days ago."** No avatar, no name, no link. Human faces are the single fastest trust accelerant; their absence reads as auto-generated.
3. **Zero images anywhere in the article body.** This is your biggest credibility gap, not just an aesthetic one. iFixit's entire moat is *original step photos on clean white* -- it's proof a real human did the repair. A wall of text claiming "technician practice" with no photo of the part, the error display, or the access panel looks like it could have been written by anyone (or anything). Text-only = "they've never touched this machine."

---

## Prioritized, concrete fixes

### P0 -- Surface the real humans (highest trust-per-hour-of-work)

1. **Real author byline on every article.** Replace "Error Code Fixes Editorial Team" with: small circular avatar (40px) + **"Reviewed by Marcus Webb"** (or whoever owns that brand's vertical -- HVAC/fridge codes -> Webb, kitchen -> Rutherford) + a credential chip rendered in your navy `#1B2A4A`: `EPA 608 · NATE`. Make the name a link to a real bio. Pattern: `Reviewed by [avatar] Marcus Webb, EPA 608 Universal · NATE Certified` then on its own line `Last reviewed Jun 4, 2026 · Published Mar 2026`.
2. **Rebuild `/authors/` into a real team page with photos.** Three cards, each: real headshot (or, if anonymity is required, a consistent illustrated portrait -- *never* a generic silhouette), name, credential badges, one-line specialty, years, and the list of brands they own. This page should rank for "[site] editorial team" and be linkable as your E-E-A-T proof for Google. Add `Person` + `sameAs` schema (LinkedIn/credential-body profiles if they exist).
3. **Add visible `author` + `reviewedBy` to your Article/HowTo JSON-LD.** Google's quality systems read structured author data. A faceless byline plus empty author schema is a self-inflicted E-E-A-T wound. Each guide's HowTo schema should carry the reviewing editor's `Person` object with their `hasCredential`.
4. **Split published vs. last-reviewed dates visibly.** "Reviewed 5 days ago" is good but pair it with the original publish date so it doesn't read as a date-spoofing trick (Google penalizes fake freshness). Show both.

### P0 -- Add original visual media (the iFixit moat, your biggest gap)

5. **Even 2-3 original images per money-page closes most of the gap.** Priority order: (a) a photo/clean render of the **actual error display** showing "3C" on a Samsung panel, (b) a labeled diagram or photo of the part being inspected (drain hose / case heater), (c) a screenshot of the control-panel reset sequence. These don't need to be glossy -- iFixit's are utilitarian. They need to be *yours and consistent* (same lighting, same on-white treatment, same callout style). This is what converts "content farm" into "someone actually did this," and it's what earns the inbound links that Google reads as expertise.
6. **Build one reusable visual system** so it scales across 3,700 guides without per-article photography: a branded SVG diagram kit (appliance silhouettes, numbered callout pins in navy, a consistent "error display" component that renders any code in your monospace on a realistic LCD). A distinctive, recognizable diagram style becomes a brand asset competitors can't copy and a thing people screenshot and link.

### P1 -- Make the trust line and color system signal credibility instead of "affiliate blog"

7. **Promote the "we don't sell parts" independence line into a fixed trust component**, not an easy-to-miss sentence. A compact bordered strip under the H1: shield/scale icon + **"Independent. We don't sell parts -- so we'll tell you when *not* to buy one."** Same component echoed in the footer. This single line is your strongest differentiator vs. RepairClinic/PartSelect (who *are* the parts store and therefore always say "buy the part"). Lean into it hard -- it's the honest-positioning angle that earns trust *and* links.
8. **Demote the orange.** Move H1s to your navy `#1B2A4A` (or near-black ink). Reserve `#E6531D` for the **one** primary CTA per view (the part button). Right now the same orange on the headline and the buy button blurs the line between "editorial" and "commercial," which is precisely the trust tell. Also desaturate it slightly (toward `#D2481A`) -- the current value is the "harsh/dated" you already sensed.
9. **Affiliate disclosure inline at the first part link, not just footer.** A one-line muted note *right above the parts table* ("Affiliate links -- buying through them supports the site at no extra cost. Commission never changes which part we recommend.") is a *trust gain*, not a tax. It pre-empts the "they just want me to buy" reflex at the exact moment of doubt and reinforces the independence claim.

### P1 -- Surface the methodology on-page (don't make people hunt)

10. **Add a collapsible "How we verified this fix" block** at the article foot: a 1-line summary ("Built from Samsung service literature + field service-call history, reviewed by an EPA 608 / NATE editor") with a link to full methodology. The "if the only source is a forum post, the guide doesn't get drafted" line is excellent -- quote it on-page. Sourcing transparency on a YMYL page is a direct ranking and trust signal.
11. **Cite the manufacturer.** Even one line -- "Per Samsung's published fault-code reference, 3C indicates a circulation pump / wiring fault" -- with a link to (or named reference of) the OEM source instantly separates you from forum-scraper farms. You claim OEM sourcing in methodology; show it on the page.

### P2 -- Borrow competitors' social-proof mechanics, honestly

12. **Add lightweight "did this fix work?" feedback** (a Yes/No tap at the fix's end) and, once you have data, surface an honest "Helped 412 of 460 people" stat. This is iFixit's "X completed this guide" mechanic adapted -- it's the strongest trust signal of all (other real humans succeeded) and it's earned, not claimed.
13. **Fix the `/diagnose` emoji icons immediately.** Emoji (satellite-dish "microwave," laundry-basket "washer") is the loudest amateur tell on the whole site and it sits on a *tool* page where you're asking for trust before a recommendation. Replace with a single consistent line-icon set (Lucide/Phosphor or custom appliance glyphs) in navy. Add a "Popular codes this week" list and a one-line trust strip to kill the empty-below-the-fold problem.

---

## Why this also wins with Google (not just humans)

The same moves are the literal inputs to E-E-A-T scoring: a named author with `hasCredential` schema (Expertise), original photos/diagrams that get linked and screenshotted (Experience + earns backlinks), visible methodology + OEM citation (Trustworthiness), and inline disclosure (Trust/honesty). You already did the hard part -- you hired/assembled credentialed editors and wrote a real methodology. The failure is purely **information architecture and visual design hiding it.** Surface it and this dimension goes from 4.5 to a defensible 8+.

**Net:** keep the honesty positioning (it's your genuine moat against the parts-store competitors), kill the emoji and the orange-everywhere, put real faces and credentials on every page, and add a consistent original-diagram system. Trust isn't missing here -- it's just unrendered.

**Sources:** [iFixit Reputation](https://www.ifixit.com/Info/Reputation), [iFixit Guide Ownership](https://www.ifixit.com/Wiki/Guide_Ownership), [iFixit Parts of a Guide Page](https://about.ifixit.com/Wiki/Parts_of_a_Guide_Page), [iFixit Content Quality](https://www.ifixit.com/Info/content-quality)


## COMPETITIVE
I now have full pixel ground truth on all three pages. The diagnose page confirms the worst of it: the emoji icons are genuinely embarrassing (washer = wicker picnic basket, dryer = blue spiral/cyclone, range/oven = a purple magnifying glass which makes no sense, microwave = a satellite-dish-and-signal emoji), the page is 70% empty cream below a single row of cards, and there are no trust signals, no popular codes, no second step visible. I have everything I need. Writing the critique now.

---

**COMPETITIVE DESIGN BENCHMARK — errorcodefixes.com: 5.0 / 10**

Verdict: cleaner and more honest-feeling than the cluttered incumbents, but visually generic and under-built — it reads "tasteful Tailwind starter," not "the authoritative diagnostic brand," and the emoji icons + image-zero body actively undercut the credibility the copy is trying to earn.

---

**WHERE IT LOSES vs. THE INCUMBENTS (specific, observed live)**

1. **The orange is the single biggest brand liability — and it's worse rendered than spec'd.** On the article H1 ("Samsung Dishwasher 3C Error Code") the orange renders as a muddy brick/terracotta on the #F4F3EF cream, and the primary buttons ("Jump to Fix," "Get Free PDF," the Amazon chips) render as a dark *brown*, not bright orange. So you have three different oranges fighting: muddy-orange headlines, brown buttons, and bright-orange stat numbers on the homepage. It looks like an unresolved palette, not a decision. Worse, an orange H1 on cream is a low-contrast, dated "2015 affiliate blog" signal. RepairClinic/PartSelect own trustworthy blues; iFixit owns a confident blue (#0071CE-ish) on stark white. Orange on cream reads cheaper than all of them.

2. **Zero original visual media is the disqualifying gap.** iFixit's entire moat is original, evenly-lit step photography on white. Your article body has *not one image* — no photo of a clogged filter, no labeled diagram of the sump/drain path, no "this is the part, here's where it lives" shot. The "Parts Often Needed" table lists "Samsung dishwasher drain pump assembly" with a tiny brown Amazon button and **no product thumbnail**. A panicked visitor cannot visually confirm they're buying the right part. Every competitor shows the part. This is the #1 thing keeping you below 7.

3. **The desktop layout is ~65% empty cream.** Content is locked to ~48rem centered in a 1440px viewport, leaving roughly 470px of dead beige on each side of the article, and the /diagnose page is a single row of cards floating above an ocean of empty background. The incumbents fill the viewport (catalog facets, video rails, related parts). Your emptiness doesn't read "premium minimal" — it reads "unfinished," because nothing anchors the margins (no sticky TOC, no parts rail, no diagram).

4. **The emoji icons are genuinely amateurish — confirmed worse than described.** On /diagnose: Washer = a wicker picnic basket, Dryer = a blue cyclone/spiral, **Range/Oven = a purple magnifying glass** (literally the wrong concept), Microwave = a satellite-dish-with-signal emoji. These are OS-rendered emoji, so they look different on every device and several are simply incorrect. iFixit and RepairClinic use consistent line-icon or product-photo systems. This one detail signals "hobby project" louder than anything else on the site.

5. **"Most Common Fixes" is a 2009 blog roll.** It's a vertical stack of orange text links, each with a 📅 calendar emoji + gray date + gray description — no thumbnails, no card, no rank, no visual weight difference between items. It looks like a default RSS dump. PartSelect/RepairClinic present popular items as cards with imagery and price/rating chips.

6. **The hero is missing its promised search box.** The brief says the homepage has a search box; live, there is no visible input — only a text link "Not sure of your code? Use the guided diagnosis →". For a site whose core job is "type your code, get the fix," the absence of a big, obvious code-entry field at the top is a conversion and authority miss. A code lookup field IS your hero product.

---

**THE WHITE SPACE — HOW TO LOOK BETTER AND MORE AUTHORITATIVE THAN ALL OF THEM**

The incumbents are catalog-commerce sites that happen to have content. None of them looks like a *modern, neutral, instrument-grade diagnostic tool*. That's the open lane: position the design as the "Bloomberg terminal / iFixit-precision" of error codes — honest, technical, beautifully systematic. Specific moves:

**A. Re-anchor the palette to "trusted instrument," demote orange to an accent.**
- Make the **navy (#1B2A4A) the primary brand color** — headlines, nav, the error-code chip system. Navy on cream already looks more authoritative than any competitor's blue-on-white because the warm paper feels editorial, not e-commerce.
- Keep **one** orange, and make it a true confident orange only for the single primary CTA and the live error-code value. Pick `#D8431A`–`#E6531D`, use it *once per view*, and never as an H1 color. Headlines go near-black ink (`#15171A`) on cream.
- Add a **green-for-DIY / amber-for-call-a-pro semantic system** as a deliberate, named palette (you already have the green "DIY-friendly" pill — formalize it into a 3-tier severity scale shown consistently on every card and verdict).

**B. Build a signature "Diagnostic Readout" component — your iconic, screenshot-able element.**
Replace the plain yellow QUICK ANSWER box with a navy, monospace, terminal-style verdict card: error code chip, a confidence bar ("Most likely: 70% — drain blockage"), the DIY/Pro severity pill, est. cost range, and time/tools as a tight icon strip. Make it look like a *readout from an instrument*. This becomes the thing people screenshot and link to — earns the shares the brief wants, and instantly looks more authoritative than a yellow alert box.

**C. Commission/generate a consistent line-icon set and kill every emoji.**
Two-tone navy/orange stroke icons (washer, dryer, fridge, dishwasher, range, microwave, furnace, mini-split, water heater). Even a single afternoon with a consistent icon set (Lucide/Phosphor customized, or AI-generated SVGs) erases the #1 amateurish signal. Same icons on homepage grid, /diagnose, and category headers.

**D. Add the visual media moat — but do it the AI-honest way.**
You can't photograph every part, but you can out-execute on **labeled SVG diagrams**: a clean, branded cutaway of a dishwasher showing filter → sump → drain pump → hose, with the suspect part highlighted in orange. This is *better* than iFixit photos for diagnosis (clearer than a dim photo), it's original (link-bait), it's static/fast (CWV-safe), and it's defensibly yours. For the parts table, pull the Amazon/affiliate product image thumbnail so buyers can visually confirm the part. Diagrams + thumbnails is the single highest-ROI upgrade.

**E. Fill the dead margins with a sticky left rail (desktop).**
Article gets a sticky **"On this page" TOC + a mini diagnostic-readout + DIY/Pro cost summary** in the left margin, and a **related codes / "people also fixed"** rail on the right. Widen the reading column slightly to ~62–66rem. Now the screen looks engineered, not empty, and you add internal links (SEO) without touching the body.

**F. Make /diagnose feel like the product, not a placeholder.**
After the appliance row: show the **step-2 code input inline immediately** (don't hide it), add a row of **"Most-searched codes right now"** chips (Samsung 3C, LG OE, Whirlpool F2E1…), a small trust strip ("3,723 verified fixes · independent · we tell you when *not* to buy a part"), and a live result preview card. The honesty line is your best differentiator — put it ON the tool, big.

**G. Lean into the "AI-operated, independent, honest" identity as a visible design system.**
None of the incumbents can credibly say "we don't sell parts, so we'll tell you NOT to buy one." Turn that into a **recurring visual badge** — a small navy "Independent Verdict" seal / "No-Buy Recommended" amber callout that appears when the fix is free. That's a brand-defining, trust-building component the parts-sellers literally cannot copy because it's against their interest.

---

**PRIORITIZED FIX LIST (highest design-ROI first)**
1. Kill all emoji → consistent navy/orange line-icon set (homepage grid, /diagnose, categories).
2. Add labeled SVG cutaway diagrams to articles + product-image thumbnails in the parts table.
3. Fix the palette: navy primary + ink-black headlines on cream; one true orange used once per view; resolve the brown-vs-orange button inconsistency.
4. Build the "Diagnostic Readout" terminal-card to replace the yellow Quick Answer box (signature component).
5. Add the desktop sticky left rail (TOC + readout + cost) and right related-codes rail; widen column to ~64rem.
6. Put a real code-search field in the homepage hero; rebuild "Most Common Fixes" as image/severity cards, not a text blog roll.
7. Rebuild /diagnose: inline step-2 input, popular-code chips, trust strip, result preview.
8. Formalize the DIY-green / Pro-amber severity scale and the "Independent / No-Buy" honesty badge as reusable components.

If 1–4 ship, this jumps to ~7.5 and starts looking more distinctive and trustworthy than RepairClinic/PartSelect (catalog clutter) while occupying the one lane iFixit left open: the honest, instrument-grade, AI-operated diagnostic brand.

Sources: [RepairClinic](https://www.repairclinic.com), [PartSelect](https://www.partselect.com), [iFixit](https://www.ifixit.com)


## MOBILEPERF
Now I have ground-truth article data. Critical confirmed facts:

- **H1 = `rgb(230,83,29)` (#E6531D) at 30px on cream = 3.37:1.** The article H1 IS the harsh orange. At 30px/700 it's "large text" so it technically passes the 3:1 large-text threshold — but barely (3.37 vs 3.0), and the SAME orange on smaller link text (18px card titles, "Skip to content" 16px, the "QUICK ANSWER" label) FAILS 4.5:1. This is the central accessibility defect.
- **"Jump to Fix" and "Amazon" buttons are actually `rgb(146,64,14)` (a dark brown), NOT the bright orange** — contrast 7.09:1, which PASSES. So the primary CTAs are fine; the bright orange #E6531D is reserved for the H1 and link accents where it fails.
- **Buttons are 30–39px tall** — the Amazon button at **30px** and Jump-to-Fix at 39px are both **under the 44px minimum tap target**. 51 of 66 tappable elements are under 44px.
- **3 `<details>` decision-tree elements** (native, keyboard-accessible — good).
- **Only 2 images on the entire money page** (both logos). Zero diagrams/photos confirmed.
- The mobile sticky "get the part" bar is `display:none` at this width (didn't appear in fixed/sticky scan), so I can't measure it here, but the brief describes it.

I have a complete, evidence-backed picture. The window-width limitation doesn't affect any of my load-bearing measurements (colors, contrast ratios, font sizes, tap-target pixel dimensions, aria attributes, font-display, DOM size are all viewport-independent or measured at the rendered size). Here is the critique.

---

**SCORE: 6.5/10 — Mobile UX, Performance & Accessibility**

**Verdict:** Genuinely fast and clean with solid conversion bones, but it is NOT yet world-class on a phone — the signature orange fails WCAG AA on text, most links have no visible focus ring, tap targets are too small, the diagnose-page emoji are read aloud as semantic content, and there is zero original media. Fixable in about a week; none of it is architectural.

---

**THE EVIDENCE (measured in-browser, computed styles)**

- Accent orange is `--accent: #e6531d` = `rgb(230,83,29)`. On the cream page background `#F4F3EF` it computes to **3.37:1**.
- Body/headline ink is `rgb(15,20,24)` on cream = **16.68:1** (excellent — keep it).
- Primary CTAs ("Jump to Fix", "Amazon") are actually `rgb(146,64,14)` dark-rust, white text = **7.09:1 PASS**. Good. The bright orange is only used where it fails.
- Fonts: Inter Tight body, "Google Sans Code" / JetBrains Mono for code chips, all `font-display: swap`. 2 external CSS files + ~28KB inline `<style>`. Article DOM = 477 nodes. Truly lightweight.

---

**P0 — ACCESSIBILITY FAILURES (fix first, these are pass/fail)**

1. **Orange text fails WCAG 2.2 AA (1.4.3) at 3.37:1.** It appears on: every article-card title link (18px), the "QUICK ANSWER" eyebrow label, "Skip to content" (16px), inline "→" links, "See all Samsung error codes". All need 4.5:1; all fail. The H1 at 30px/700 is "large text" so 3.37 technically clears the 3:1 bar — but only just, and you're betting your whole brand on a 0.37 margin.
   **Fix:** darken the *text* orange to `#C2410C` (≈4.9:1 on cream, still unmistakably orange) or `#B23E12` (≈5.6:1). Keep the bright `#E6531D` ONLY for large fills/CTA backgrounds with white text, never for body-size text on cream. One token split: `--accent` (fills) vs `--accent-text` (text/links). This is a 1-line variable change that resolves ~12 of the failing elements at once.

2. **No visible focus indicator on most interactive elements.** Computed `outline-style: none` on the default card/nav link; only `.ps-link`, `.sp-cta`, and the chat widget have explicit `:focus-visible` rings. Card titles, "Jump to Fix", "Amazon", nav, and the diagnose appliance buttons have **nothing** when tabbed to (WCAG 2.4.7 fail, and 2.4.11 focus-not-obscured).
   **Fix:** one global rule — `:where(a,button,summary,[role=button],input):focus-visible{ outline:3px solid var(--accent); outline-offset:2px; border-radius:4px; }`. Make the ring `#C2410C` so it also passes 3:1 against cream.

3. **Emoji icons are exposed to the accessibility tree.** On the homepage grid and the /diagnose appliance row, the emoji spans have `aria-hidden=false`. A screen-reader user hears "laundry basket Washers", "satellite antenna Microwaves", "hot springs Water heaters". The washer/microwave/dishwasher emoji are also semantically wrong AND inconsistent across platforms (they render differently on iOS vs Android vs Windows).
   **Fix two birds:** replace emoji with a single inline-SVG icon set (one sprite, ~3KB, crisp, on-brand, consistent) and wrap each in `aria-hidden="true"` with the visible text label doing the talking. This also kills the "amateurish" look the brief flags.

---

**P1 — MOBILE UX / TAP TARGETS**

4. **Tap targets are too small (WCAG 2.5.8 AA, 24px min; Apple/Google guidance 44/48px).** Measured on the article: **51 of 66** tappable elements are under 44px. The **Amazon affiliate button is only 30px tall** — that is your single most important revenue click and it is the smallest button on the page. "Jump to Fix"/"View Parts" are 39px. Nav links are 32px.
   **Fix:** `min-height:44px` on all buttons/links-as-buttons, `padding:12px 16px` on the Amazon/part buttons (push to 48px — a panicked person at the machine is tapping one-handed), and `min-height:44px; display:flex; align-items:center` on nav items. Add `line-height` breathing room so the 44px isn't just an invisible hit area but looks tappable.

5. **The sticky "get the part" mobile bar — make it the hero of mobile, and QA it.** It was `display:none` at the widths I could test, so I couldn't measure its live contrast/height — **verify on a real 390px device** that: (a) it clears the iOS home-indicator with `padding-bottom: env(safe-area-inset-bottom)`, (b) its button is ≥48px, (c) it uses the dark-rust `#92400E` fill (7:1) not bright orange, (d) it doesn't cover the last paragraph / footer links, and (e) it has a dismissable affordance or doesn't trap the "When to call a pro" honesty content. A sticky affiliate bar that hides your "don't buy the part" trust line would undercut the whole honest-positioning play.

6. **/diagnose is too sparse and the emoji row is the worst offender.** One row of 6 inconsistent emoji buttons then a wall of empty space. On mobile this reads as "broken / unfinished."
   **Fix:** below the appliance picker add a "Popular codes right now" chip list (Samsung 3C, LG OE, Whirlpool F2E1…) as 44px chips, plus the trust line ("Independent — we tell you when NOT to buy a part") and a 1-line "How this works" so the page earns trust before asking for a tap.

---

**P1 — READABILITY & THE MISSING MEDIA MOAT**

7. **Zero original visual media is the biggest gap for both conversion AND links/shares.** 2 images on the money page, both logos. iFixit's entire moat is original step photos on white; you have text only. On a phone, an unbroken text column is fatiguing and gives Google nothing to rank in image/visual results.
   **Fix (mobile-first, CWV-safe):** add (a) one **simple labeled SVG diagram per code** ("where the drain filter is") — vector, tiny, sharp on retina, themeable for dark mode, zero CLS; (b) the error-code chip itself rendered as an OG/share image so social cards are distinctive. Every `<img>` must ship `width`/`height` (you already do on the logos — `noDims:0`, good) and `loading="lazy"` below the fold to protect LCP. This is the single change that most separates you from a generic affiliate blog.

8. **Body type / measure.** Body is 16px / 24px line-height Inter Tight on cream — fine. On mobile bump body to **17px** and line-height to ~1.6 for the long troubleshooting prose; constrain measure to ~68ch. Make the navy code chips (`ui-monospace`) at least 16px so they're legible when someone is comparing the chip to the blinking code on the panel.

---

**P2 — CORE WEB VITALS (you're fast; protect it)**

9. **You're in good shape and should stay there.** Astro static, 477 DOM nodes, `font-display:swap`, no hero raster image. Risks to watch:
   - **FOUT on the monospace code chip** — `swap` means the navy "3C" chip flashes in Courier then reflows to Google Sans Code. **Preload the one code-font woff2** (`<link rel=preload as=font crossorigin>`) — I found **zero font preloads**. That removes the flash on your most identity-defining element. INP/CLS stay green.
   - **~28KB inline CSS + 2 external sheets.** Fine, but ensure the external `index.*.css` is truly critical-path; consider inlining only above-the-fold and deferring the rest if LCP ever creeps.
   - **Set an explicit aspect-ratio box** for any new diagrams/OG images so adding media never reintroduces CLS.
   - Keep the affiliate/Skimlinks scripts `async` (they are) and ideally load them **on interaction/idle** so they never block INP on a low-end Android.

---

**WHAT'S ALREADY GOOD (keep):** dark-rust CTA at 7:1, near-black body ink at 16.68:1, native `<details>` decision tree (3 on the page — keyboard-accessible, no JS dependency), `width=device-width` viewport, lightweight static build, honest "we don't sell parts" trust line, `font-display:swap`, dimensioned logos.

**THE ONE-WEEK PATH TO ~9/10:** (1) split the orange token and darken text-orange to `#C2410C`; (2) one global `:focus-visible` ring; (3) `aria-hidden` + SVG-replace all emoji; (4) 44–48px min on every button incl. the 30px Amazon CTA; (5) preload the code font; (6) ship one labeled SVG diagram per guide + a code-chip OG image. Items 1–5 are CSS/markup changes measurable in an afternoon; item 6 is the moat.