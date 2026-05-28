---
title: "Fanuc Alarm 600 — Causes & Fix"
description: "What Fanuc Alarm 600 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T18:00:00Z
modDatetime: 2026-04-22T18:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - cnc
  - fanuc
---

## Fanuc Alarm 600 — What It Means

Fanuc Alarm 600 is an APC (Absolute Pulse Coder) alarm series — the absolute encoder battery has died or the APC has lost its position data. The Fanuc absolute encoder (built into the servo motor) stores the axis position even when machine power is off, relying on a small backup battery. When this battery fails, the encoder loses its absolute position reference and Alarm 600 series fires.

[Jump to Fix](#fix)

## Common Causes

- **Backup battery dead or low** — The most common cause. The lithium backup battery (typically 6V or 3V depending on system) has discharged. Battery life is typically 2-5 years.
- **Battery connector loose or corroded** — The battery lead connector at the battery holder or encoder PCB can loosen or corrode, causing intermittent position loss.
- **Encoder PCB failure** — The encoder board itself has failed, requiring replacement of the servo motor encoder.
- **Power was cut while encoder was active** — Certain Fanuc configurations can lose absolute position if main power and battery are both absent simultaneously during a replacement.

## Step-by-Step Fix {#fix}

1. **Replace the backup battery immediately** — Locate the encoder backup battery (usually a lithium 6V battery pack near the control cabinet or at the servo amplifier). Replace it with the correct Fanuc replacement battery. Do this while machine power is ON to preserve encoder data.
2. **Re-execute reference return** — After battery replacement, execute ZRN on all axes with Alarm 600 to re-establish absolute position reference.
3. **Inspect battery connector** — Check the battery lead connector for corrosion or loose fit. Clean and reseat.
4. **Verify alarm clears** — After reference return, confirm Alarm 600 no longer appears and all axis positions read correctly.
5. **Document battery replacement date** — Note the date for future maintenance scheduling.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Fanuc encoder backup battery | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-alarm-600&k=Fanuc+encoder+backup+battery&tag=errorcodefixes-20) \| Match to Fanuc system — A06B-6073-K001 (6V) or model-specific |
| Battery cable harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-alarm-600&k=Battery+cable+harness&tag=errorcodefixes-20) \| Replace if corroded |
## When to Call a Pro

If Alarm 600 persists after battery replacement and reference return, the encoder PCB inside the servo motor may have failed. Motor encoder replacement requires Fanuc-certified service.

## Related Articles

- [Fanuc 0i-MD Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-0i-md-alarm-codes/)
- [Fanuc 30i/31i/32i Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-30i-alarm-codes/)
- [Fanuc Alarm 1 Overtravel — Causes & Fix](/posts/fanuc-alarm-1-overtravel/)
- [Fanuc Alarm 10 Servo Alarm — Causes & Fix](/posts/fanuc-alarm-10-servo-alarm/)
- [Fanuc Alarm 2 — Overtravel Plus Causes & Fix](/posts/fanuc-alarm-2-overtravel/)

## See Also

- [Fanuc Alarm 411 — Causes & Fix](/posts/fanuc-alarm-411/)
- [Fanuc Alarm 800: APC Alarm — Causes and Fix](/posts/fanuc-alarm-800/)
- [Fanuc OT Alarm — Software Overtravel (All Series)](/posts/fanuc-ot-alarm-soft/)
- [Fanuc Alarm 2 — Overtravel Plus Causes & Fix](/posts/fanuc-alarm-2-overtravel/)
