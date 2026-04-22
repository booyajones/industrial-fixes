---
title: "Lennox Error Code 292 — Ignition Failure Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-03-10T08:00:00Z
modDatetime: 2024-03-10T08:00:00Z
slug: lennox-292-error-code
featured: false
draft: false
tags:
  - hvac
  - lennox
  - furnace
  - ignition
  - gas
description: "Lennox error code 292 means the furnace went into soft lockout after repeated ignition failures. This guide covers every cause and fix for the 292 fault code."
---

## Error Code: Lennox 292

**What it means:** Error code 292 on a Lennox furnace indicates a soft lockout caused by repeated failed ignition attempts. The control board tries to light the burners — the hot surface igniter glows, the gas valve opens — and the flame sensor never detects a flame. After three failed ignition trials, the board goes into soft lockout and displays code 292. A soft lockout means the furnace will automatically attempt to restart after about an hour, but will keep locking out until the root cause is fixed.

This code does not mean the furnace is permanently broken. It means the ignition sequence failed, and the board is protecting the system from flooding the heat exchanger with unburned gas.

## Common Causes

- **Failed hot surface igniter** — The igniter glows orange to light the gas. Over time (typically 3–7 years), the igniter element cracks or loses efficiency and stops reaching the 1,800°F threshold needed to ignite gas reliably. This is the most common cause of code 292.
- **Dirty or coated flame sensor** — The flame sensor rod detects the flame via electrical conductivity through the flame. A thin layer of oxide or residue on the sensor rod reduces conductivity enough that the board can't confirm ignition, even when a flame is present.
- **Gas supply problem** — Low gas pressure, a partially closed manual shutoff valve, or a momentarily interrupted gas supply causes ignition failure with a healthy igniter and sensor.
- **Failed gas valve** — If the gas valve solenoid doesn't open during the ignition trial (no click, no gas flow), the igniter will glow but no flame can form.
- **Weak or intermittent igniter** — Sometimes the igniter works sometimes but can't sustain reliable ignition, especially in cold weather when the furnace is most stressed.
- **Control board fault** — Rarely, the board itself fails to send the correct voltage to the igniter or gas valve during the ignition sequence.

## Step-by-Step Fix {#step-by-step-fix}

1. **Reset the lockout first.** Turn the thermostat to OFF, then cut power to the furnace at the disconnect switch or breaker for 30 seconds. Restore power. This clears the soft lockout and lets you observe the ignition sequence in real time on the next call for heat.

2. **Watch the ignition sequence.** Turn the thermostat up to call for heat. Watch through the furnace sight glass: you should see the inducer spin up, then the igniter glow bright orange within about 30–45 seconds, then the gas valve click and burners light. Identify exactly where the sequence stops.

3. **Inspect the hot surface igniter.** Cut power before touching anything. Remove the burner access panel. Visually inspect the igniter element — look for cracks, fractures, or a dull element that doesn't glow uniformly. If you see any cracking, replacement is required regardless of other findings. Lennox igniter part number **44W93** is the correct replacement for most G61MP and SLP98 series furnaces (~$45 at Repair Clinic).

4. **Clean the flame sensor.** Locate the flame sensor — a metal rod with a ceramic insulator, positioned so the rod tip sits in the burner flame path. Disconnect the sensor wire. Remove the single mounting screw. Using fine steel wool or a clean dollar bill (not sandpaper), lightly buff the metal rod to remove oxidation. Reinstall and reconnect. This takes 5 minutes and fixes a significant percentage of 292 codes.

5. **Verify gas supply.** Confirm the manual gas shutoff valve on the supply line to the furnace is fully open (handle parallel to pipe). If you have a gas pressure gauge, verify inlet pressure is between 5–7 inches W.C. for natural gas or 11–14 inches W.C. for propane. If pressure is low, the issue is upstream of the furnace.

6. **Test the igniter resistance.** With power off, disconnect the igniter leads and use a multimeter set to resistance. Lennox SiC igniters should read between 40–90 ohms when cold. A reading of OL (open circuit) confirms a failed igniter even if it looks intact.

7. **Monitor the flame sensor voltage during operation.** If you have a multimeter with a microamp mode, reconnect everything and clip the leads to measure current through the flame sensor during operation. A reading below 1.5 µA (microamps) indicates a weak signal — clean the sensor or replace it. A reading of 2–6 µA is normal.

8. **Replace components and retest.** If the igniter tests failed or the sensor cleaning doesn't resolve the issue, replace the suspect component and run the furnace through 3–4 full heat cycles to confirm the 292 code is gone.

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Part Number | Typical Cost | [Where to Buy](https://www.amazon.com/s?k=Where%20to%20Buy&tag=errorcodefixe-20) |  |------|------------|-------------|-------------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Hot surface igniter | 44W93 | [$40–$55](https://www.amazon.com/s?k=%2440%E2%80%93%2455&tag=errorcodefixe-20) | Repair Clinic / Amazon |
| [Flame sensor](https://www.amazon.com/s?k=Flame%20sensor&tag=errorcodefixe-20) | 51W06 | $20–$30 | [Repair Clinic / Amazon](https://www.amazon.com/s?k=Repair%20Clinic%20%2F%20Amazon&tag=errorcodefixe-20) |  | Gas valve (G60DF-1) | [LB-100523P](https://www.amazon.com/s?k=LB-100523P&tag=errorcodefixe-20) | $180–$250 | HVAC Distributors / Amazon | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Control board | 103116-01 | [$220–$350](https://www.amazon.com/s?k=%24220%E2%80%93%24350&tag=errorcodefixe-20) | Repair Clinic |

## When to Call a Professional

If you've replaced the igniter and cleaned the flame sensor and the 292 code persists, the problem is likely the gas valve, gas pressure, or control board. Gas valve replacement involves working with live gas lines — this requires a licensed technician in most jurisdictions and should not be a DIY repair. Similarly, if you smell gas at any point during diagnosis, shut off the gas supply immediately and leave the building before calling your gas utility.

> **Pro tip:** Before buying a new igniter, measure its resistance first. A cracked igniter can still read within spec on a multimeter but fail under operating temperature. If the igniter looks cracked even slightly, replace it — cracks propagate and the furnace will lock out again within weeks.
