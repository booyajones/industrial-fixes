---
title: "Okuma CNC Alarm 1201 — Causes & Fix"
description: "What Okuma CNC alarm 1201 spindle overload means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T09:00:00Z
modDatetime: 2026-04-22T09:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - cnc
  - okuma
---

## Okuma CNC Alarm 1201 — What It Means

Okuma CNC alarm 1201 indicates a spindle overload — the spindle drive (OKUMA OSP spindle amplifier or third-party inverter) detected that the spindle motor was drawing current exceeding its continuous or peak rating. On Okuma OSP-P200/P300 series controls, alarm 1201 appears when the spindle amplifier's thermal or overcurrent protection trips due to sustained heavy cutting, stall, or mechanical binding at the spindle. The spindle shuts down immediately and the machine goes to feed hold. The spindle motor must cool before the alarm can be cleared.

[Jump to Fix](#fix)

## Common Causes

- **Aggressive cutting parameters** — Depth of cut, feed rate, and spindle speed combination is demanding too much torque from the spindle motor for the material and tooling. Common on high-volume programs with deep roughing passes.
- **Dull or incorrect tooling** — Worn or incorrect cutting tools require significantly more torque to maintain the programmed feed rate, pushing spindle current above the rated limit.
- **Spindle bearing wear or contamination** — Degraded spindle bearings or contamination in the spindle bearing races increase mechanical drag, requiring higher motor current to maintain speed.
- **Spindle drive cooling fault** — The spindle amplifier's internal cooling fan has failed, causing the amplifier to reach its thermal limit under load that was previously handled without issue.

## Step-by-Step Fix {#fix}

1. **Allow spindle motor and drive to cool** — Do not attempt to clear alarm 1201 immediately. The spindle motor thermal protection requires the winding temperature to drop below reset threshold. Allow 20–30 minutes before reset.
2. **Review cutting parameters** — Pull up the cutting program and review the depth of cut, chip load, and spindle speed for the operation that triggered the alarm. Compare against the tooling manufacturer's recommended parameters for the material.
3. **Inspect tooling condition** — Check the cutting edge of the offending tool for wear, chipping, or glazing. Dull inserts can double or triple the required cutting force. Replace worn tooling before resuming.
4. **Check spindle amplifier cooling** — Open the Okuma electrical cabinet and inspect the spindle drive cooling fan. Confirm it is running at full speed. Clean any dust accumulation from the drive heatsink.
5. **Monitor spindle load meter** — After resuming with revised parameters, watch the spindle load meter (displayed on the OSP control as a percentage or amperage). Keep it below 80% on continuous cuts to avoid thermal accumulation.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Spindle amplifier cooling fan | [Amazon](https://www.amazon.com/s?i=industrial&k=Spindle+amplifier+cooling+fan&tag=errorcodefixes-20) \| Match voltage and airflow; Okuma spindle drives use 24VDC fans typically |
| Cutting inserts / tooling | [Amazon](https://www.amazon.com/s?i=industrial&k=Cutting+inserts+%2F+tooling&tag=errorcodefixes-20) \| Replace any worn cutting edges before resuming operation |
| Spindle bearings | [Amazon](https://www.amazon.com/s?i=industrial&k=Spindle+bearings&tag=errorcodefixes-20) \| Replace if drag is confirmed via manual spindle rotation test |
## When to Call a Pro

If alarm 1201 returns at cutting parameters well within the tool manufacturer's recommendations and with confirmed good tooling, the spindle motor may have insulation degradation that reduces effective winding capacity. An Okuma service technician can measure motor efficiency and spindle bearing preload.

## Related Articles

- [CNC Alarm Reset Guide: How to Clear Alarms Safely](/posts/cnc-alarm-reset-guide/)
- [CNC Machine Error Codes: Complete Troubleshooting Guide](/posts/cnc-error-codes-guide/)
- [Doosan CNC Alarm Codes Guide — Fanuc / Fanuc i Series Controls](/posts/doosan-cnc-fault-codes/)
- [Fanuc 0i-MD Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-0i-md-alarm-codes/)
- [Fanuc 30i/31i/32i Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-30i-alarm-codes/)
