---
title: "Carrier Error Code 51 — Control Fault (Secondary)"
description: "Carrier furnace error code 51: what it means, causes, and how to fix the secondary control fault on Carrier Performance and Infinity series furnaces."
pubDatetime: 2026-04-22T19:00:00Z
modDatetime: 2026-04-22T19:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - carrier
  - furnace
---

## Carrier Error Code 51 — What It Means

Carrier furnace error code **51** indicates a secondary control fault. This code appears on Carrier Performance and Infinity series furnaces that use two-stage or modulating control boards. Code 51 specifically signals that the secondary (stage 2) control circuit has detected a fault condition — separate from the primary ignition or limit circuits.

On Carrier furnaces, codes are displayed by counting LED blinks: the LED flashes a number, pauses, then repeats. Code 51 = five slow blinks followed by one fast blink.

## Causes of Carrier Code 51

| Cause | Likelihood | Test |
|-------|-----------|------|
| [Secondary pressure switch fault](https://www.amazon.com/s?k=Secondary+pressure+switch+fault&tag=errorcodefixes-20) | High | Inspect pressure switch hose; test switch |
| [Two-stage gas valve fault](https://www.amazon.com/s?k=Two-stage+gas+valve+fault&tag=errorcodefixes-20) | Medium | Verify 24VAC to valve stage 2 coil |
| [IFC control board fault](https://www.amazon.com/s?k=IFC+control+board+fault&tag=errorcodefixes-20) | Medium | Check board for burn marks; swap to test |
| [Inducer motor at second stage](https://www.amazon.com/s?k=Inducer+motor+at+second+stage&tag=errorcodefixes-20) | Medium | Verify inducer RPM at high fire |
| [Wiring fault in secondary circuit](https://www.amazon.com/s?k=Wiring+fault+in+secondary+circuit&tag=errorcodefixes-20) | Lower | Inspect all secondary circuit connections |

## Step-by-Step Diagnosis

**Step 1: Note the operating conditions**
Code 51 typically appears when the furnace attempts to switch from first-stage to second-stage operation. If the furnace runs fine at low fire but faults on second stage, focus on the components that only activate at high fire.

**Step 2: Check the secondary pressure switch**
Two-stage furnaces have two pressure switches — one that closes at low fire and another that requires the higher negative pressure at high fire to close. Inspect the rubber hose connecting the inducer housing to the secondary pressure switch. A cracked or obstructed hose will prevent the secondary switch from closing.

**Step 3: Test the gas valve stage 2 coil**
With the furnace calling for heat and running on first stage, measure 24VAC across the stage 2 terminals on the gas valve when the furnace tries to ramp to second stage. No voltage = control board issue. Voltage present but valve doesn't open = faulty gas valve.

**Step 4: Verify inducer motor performance**
At high fire, the inducer motor must spin faster to develop sufficient negative pressure to close the secondary pressure switch. A weak inducer motor that can maintain first-stage pressure but not second-stage pressure will cause code 51. Listen for the inducer to speed up when the furnace calls for second stage.

**Step 5: Inspect the IFC control board**
If all external components test correctly, the Integrated Furnace Control (IFC) board may be misdiagnosing the secondary circuit or failing to send the proper signal. Look for burn marks, swollen capacitors, or heat damage on the board.

## Quick Fixes

- **Most common fix:** Replace the cracked secondary pressure switch hose (under $5 part)
- **Second most common:** Clean inducer wheel — a dirty wheel reduces high-fire pressure
- **If a code 51 follows a recent repair:** Recheck all wiring connections made during the repair

## When to Call a Pro
Gas valve replacement and detailed pressure switch diagnostics require a licensed HVAC technician. If the furnace runs safely at first stage but faults at second stage, you can disable second-stage operation temporarily (by adjusting the stat's second-stage delay settings) while you arrange service.
