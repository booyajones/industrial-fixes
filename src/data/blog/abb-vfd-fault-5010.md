---
title: "ABB VFD Fault 5010 — Causes & Fix"
description: "What ABB VFD fault 5010 means, why Safe Torque Off activates, and how to fix it."
pubDatetime: 2026-04-22T10:00:00Z
modDatetime: 2026-04-22T10:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - abb
---

## ABB VFD Fault 5010 — What It Means

Fault 5010 on ABB ACS drives (ACS580, ACS880, ACH580) indicates that the Safe Torque Off (STO) function has been activated. STO is a safety function per IEC 61800-5-2 that removes the gate drive signals from the output IGBTs, preventing the drive from producing torque — without removing main power from the drive. Fault 5010 means the STO circuit has interrupted motor output, either intentionally (safety system request) or due to a wiring or component problem.

[Jump to Fix](#fix)

## Common Causes

- **Safety relay or safety PLC opened the STO circuit** — The most common cause is intentional. An e-stop button, light curtain, safety mat, or safety relay opened the STO input circuit as designed.
- **Loose or broken STO wiring** — The STO inputs on ABB drives (terminals STO1+ / STO1- and STO2+ / STO2- on ACS880, or the STO connector on smaller drives) are 24VDC logic signals. A loose wire or connector vibration causes an unintended STO trip.
- **Failed safety relay or STO card** — The safety relay supplying the STO signal can fail in the open state, permanently activating STO. On ACS880 drives with an STO option card, the card itself can fail.
- **Power supply to STO circuit lost** — The 24VDC supply powering the safety relay or STO logic is required; loss of this supply removes the STO enable signal.

## Step-by-Step Fix {#fix}

1. **Identify why the STO was activated** — Check the machine's safety system. If an e-stop or guard door is open, close it and reset the safety relay before attempting to restart the drive.
2. **Check STO input wiring** — With drive control power on (main power off), verify 24VDC is present on the STO input terminals (STO1+ and STO2+ on ACS880). No voltage = safety relay de-energized or wiring fault.
3. **Inspect STO circuit wiring** — Trace the wiring from the safety relay output to the drive STO inputs. Look for broken conductors, damaged insulation, or loose terminal connections.
4. **Test the 24VDC safety supply** — Confirm the 24VDC power supply feeding the safety relay is operational. Replace if output voltage is absent or out of tolerance (should be 22–26VDC).
5. **Reset the drive** — After correcting the STO condition, perform a fault reset on the drive (via keypad or digital input). If STO has cleared, the drive should be ready to run.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Safety relay (24VDC) | [Amazon](https://www.amazon.com/s?k=Safety+relay+%2824VDC%29&tag=errorcodefixes-20) \| Match safety relay series (Pilz, Schmersal, Sick, etc.) |
| ABB STO option card (FSIO) | [Amazon](https://www.amazon.com/s?k=ABB+STO+option+card+%28FSIO%29&tag=errorcodefixes-20) \| ACS880 drives with separate STO option module |
| 24VDC control power supply | [Amazon](https://www.amazon.com/s?k=24VDC+control+power+supply&tag=errorcodefixes-20) \| Replace if STO supply is failed |
| STO wiring (24VDC, shielded) | [Amazon](https://www.amazon.com/s?k=STO+wiring+%2824VDC%2C+shielded%29&tag=errorcodefixes-20) \| Replace any damaged conductors in the STO circuit |
## When to Call a Pro

Modifying or bypassing STO safety circuits is a machinery safety violation and must never be done to get a machine running. Fault 5010 without an obvious safety trigger requires a certified safety engineer and/or ABB service technician to diagnose the STO circuit.

## Related Articles

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS310 Fault 3130 — Causes & Fix](/posts/abb-acs310-fault-3130/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)
