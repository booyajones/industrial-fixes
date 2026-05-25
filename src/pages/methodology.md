---
layout: ../layouts/AboutLayout.astro
title: "Editorial Methodology"
---

## How we research, write, and verify every fix guide

We publish 1,288+ brand-and-code-specific guides on errorcodefixes.com.
Each one passes through the same editorial pipeline. This page documents
the pipeline in detail because trust matters more than traffic.

### Step 1 — OEM source sweep

Before drafting a guide, our editor for the relevant equipment category
collects the authoritative sources:

- **Manufacturer service literature** (service manuals, technical bulletins,
  installation manuals, parts catalogs).
- **Field service bulletins** that update or correct the original docs.
- **Authorized service-provider training materials** (when available).
- **OEM parts database** to confirm currently available SKUs.

If the only source for a code is a forum post or an unattributed blog,
the guide doesn't get drafted. Anecdotal codes get a placeholder in our
backlog until we can corroborate against OEM material.

### Step 2 — Field corroboration

Our editors collectively have ~50 years of field experience across HVAC,
commercial refrigeration, CNC controls, VFDs, and commercial kitchen
equipment. Before publication, the diagnostic steps in each guide are
cross-checked against:

- Their own service-call history for that code.
- Patterns we see across the industry (e.g. "Carrier code 13 is almost
  always a dirty filter and an over-rated MERV upgrade" before it
  becomes anything else).
- Wear-out patterns specific to the platform.

### Step 3 — Specific over generic

A common failure mode of internet repair guides is to fill space with
generic advice ("check the wiring"). We require every step to be
specific and measurable:

- **Voltage and resistance test ranges** for sensors and switches
  (e.g. "verify the flame rod measures 0.5–2.0 microamps in steady flame").
- **OEM part numbers** for the parts that fail (e.g. "ignitor: OEM
  P/N 60M0000").
- **Decision criteria** for next step (e.g. "if the reading is below
  0.5 µA, replace the flame rod; if at 0 µA verify the wire harness
  before condemning the rod").

If a step can't be made specific, it doesn't make the guide.

### Step 4 — Safety boundaries

Every guide that touches gas lines, refrigerant, or high-voltage work
includes an explicit "stop and call a licensed pro" line at the point
the work crosses jurisdictional licensure rules. We do not pretend a
homeowner can pull a panel and reseat a heat exchanger.

### Step 5 — Affiliate independence

When a guide recommends a replacement part, the recommendation is
editorial. Parts are chosen because:

1. They're the OEM-spec replacement for the specific failure.
2. They're readily available through major suppliers.
3. They have honest user reviews on the source we link to.

Affiliate tracking parameters are added so we can sustain the site.
Commission structure does not influence which part appears in the
guide. If RepairClinic and Amazon both stock the same OEM ignitor, we
link to whichever ships faster from the reader's typical location;
we do not bias toward whichever pays the higher commission.

See our [Affiliate Disclosure](/disclosure/) for the full list of
networks we participate in.

### Step 6 — Review and re-publish

Every guide carries a publish date and an editor byline. When OEM
service bulletins update a diagnostic procedure, or when a new
platform supersedes the original equipment, the guide is updated and
the `modDatetime` reflects the change. Major changes get a clear
revision note inline.

## What we don't do

- We don't republish or paraphrase manufacturer manuals. Where the
  manual is the authoritative source, we cite it; we don't pretend
  to be one ourselves.
- We don't write generic "10 reasons your furnace won't start"
  filler content. Every guide is brand-and-code-specific.
- We don't accept payment from manufacturers to write or rank their
  brand favorably. There is no "sponsored content" tier.
- We don't gate diagnostic content behind paywalls, account creation,
  or email signups. The guide loads as you arrive.

## Who's behind this

Three credentialed editors lead the editorial work. Full bios + the
guides they've authored are at the [Editorial Team page](/authors/).

| Editor | Trade | Credentials |
|---|---|---|
| Dana Kowalski | Industrial controls, VFD, CNC | Certified Automation Professional (CAP), ISA |
| Marcus Webb | HVAC, refrigeration | EPA 608 Universal, NATE Certified |
| James Rutherford | Commercial kitchen | CFESA Certified, 18+ years field |

For corrections, partnership, or press: [info@errorcodefixes.com](mailto:info@errorcodefixes.com)
