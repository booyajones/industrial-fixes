---
title: "Honeywell VisionPRO / T6 FC Fault — Fan Control Error"
description: "Honeywell FC fault code on VisionPRO and T6 thermostats means a fan control error. Here's what triggers it and how to restore normal operation."
pubDatetime: 2026-04-22T18:00:00Z
modDatetime: 2026-04-22T18:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - honeywell
  - thermostat
  - hvac
  - fan-control
  - error-code
---

## Honeywell FC Fault — Fan Control Error

The **FC fault code** on Honeywell VisionPRO (8000, TH8320) and T6 Pro thermostats means a **fan control error** — the thermostat sent a fan signal but detected an unexpected condition in response. This code appears when the thermostat's fan monitoring circuit doesn't see expected feedback.

## What FC Monitors

Honeywell's communicating and zone-control-capable thermostats monitor the G (fan) terminal output. FC can trigger when:
- The thermostat sends a G signal and detects no response
- The fan output is drawing unexpected current (short)
- A communicating fan coil or AHU fails to acknowledge a fan command

## Common Causes of FC Fault

| Cause | Notes |
|---|---|
| [G terminal wire shorted to chassis or other terminal](https://www.amazon.com/s?k=G+terminal+wire+shorted+to+chassis+or+other+terminal&tag=errorcodefixes-20) | Most common electrical cause |
| [Failed indoor blower relay or control board](https://www.amazon.com/dp/B0CNZGZ1HS?tag=errorcodefixes-20) | Relay coil shorted |
| [Wrong wiring configuration](https://www.amazon.com/s?k=Wrong+wiring+configuration&tag=errorcodefixes-20) | G wire on wrong terminal |
| [Accessory (humidifier, UVCO light) wired into G](https://www.amazon.com/s?k=Accessory+%28humidifier%2C+UVCO+light%29+wired+into+G&tag=errorcodefixes-20) | Causes excessive load |
| [Thermostat firmware bug](https://www.amazon.com/s?k=Thermostat+firmware+bug&tag=errorcodefixes-20) | Some early T6 Pro units had fan monitoring issues |
| [Failed thermostat output circuit](https://www.amazon.com/s?k=Failed+thermostat+output+circuit&tag=errorcodefixes-20) | Rare hardware failure |

## Step-by-Step Fix

**Step 1 — Check the G terminal wiring.** Remove the thermostat from its base. Inspect the G terminal wire:
- The wire should not be touching the W, Y, or R terminals
- The wire insulation should be intact — no bare copper touching the base or wall plate
- Confirm it's connected at the air handler/furnace on the G terminal (fan relay input)

**Step 2 — Check fan operation at the air handler.** Go to the furnace or air handler. Disconnect the G wire from the control board terminal. Briefly jump G to R (or C to G terminal if that's the fan relay input) — the fan should come on immediately. If it does, the AHU fan circuit is fine and the problem is in the wiring or thermostat.

**Step 3 — Inspect the wiring between thermostat and AHU.** If there's a zone controller, humidifier, or EAC (electronic air cleaner) inline on the G wire, disconnect them one at a time to see if the FC fault clears.

**Step 4 — Factory reset the thermostat.** On VisionPRO 8000: System → Equipment → Reset. On T6 Pro: hold MENU for 5 seconds, navigate to Reset. A reset clears error history and may clear a spurious FC flag.

**Step 5 — Update firmware (Wi-Fi models).** If the thermostat is connected to Wi-Fi, check for a firmware update through the Honeywell Home app. Some FC faults on T6 Pro were firmware bugs corrected in later releases.

## When FC Appears on Non-Communicating Systems

On standard 24V wired systems (not communicating/iComfort), FC usually means a wiring problem, not a system communication issue. Focus on the G terminal wiring and relay.

## Wiring Reference

| [Terminal](https://www.amazon.com/s?k=Terminal&tag=errorcodefixes-20) | Function |
|---|---|
| R | 24V power |
| C | Common (return) |
| G | Fan (indoor blower) |
| [W / W2](https://www.amazon.com/s?k=W+%2F+W2&tag=errorcodefixes-20) | Heat stage 1 / 2 |
| [Y / Y2](https://www.amazon.com/s?k=Y+%2F+Y2&tag=errorcodefixes-20) | Cool stage 1 / 2 |
| O/B | Reversing valve (heat pumps) |

## Replace vs. Repair

If FC persists after checking wiring and performing a factory reset, the thermostat's output circuit has likely failed. Honeywell VisionPRO units are typically 10–15 years old at this point — replacement with a T6 Pro ($50–80) or T9 Smart ($100–140) is usually more cost-effective than chasing an internal board fault.
