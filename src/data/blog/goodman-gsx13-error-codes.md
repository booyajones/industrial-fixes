---
title: "Goodman GSX13 Air Conditioner Error Codes — Fault Code Diagnostic Guide"
description: "Complete guide to Goodman GSX13 air conditioner error codes, LED flash sequences, fault causes, and step-by-step fixes for the most common failures."
pubDatetime: 2026-04-22T23:00:00Z
modDatetime: 2026-04-22T23:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - goodman
  - air-conditioner
---

## Goodman GSX13 Air Conditioner Error Codes — What They Mean

The Goodman GSX13 is a 13 SEER single-stage residential central air conditioner using R-410A refrigerant. It is one of Goodman's most widely installed entry-level units and uses a standard contactor-based control system. Fault codes are reported by a diagnostic LED on the outdoor control board — the same LED-based flash code system used across Goodman's Comfort and Performance series. The GSX13 does not have a communicating control system.

[Jump to Fix](#fix)

## Goodman GSX13 LED Flash Code Reference

| [Flash Sequence](https://www.amazon.com/s?k=Flash%20Sequence&tag=errorcodefixe-20) | Fault |
|---|---|
| [1 flash](https://www.amazon.com/s?k=1%20flash&tag=errorcodefixe-20) | Normal / standby |
| [2 flashes](https://www.amazon.com/s?k=2%20flashes&tag=errorcodefixe-20) | High-pressure switch open |
| [3 flashes](https://www.amazon.com/s?k=3%20flashes&tag=errorcodefixe-20) | Low-pressure switch open |
| [4 flashes](https://www.amazon.com/s?k=4%20flashes&tag=errorcodefixe-20) | Open circuit in compressor protection (overload or internal protection) |
| [5 flashes](https://www.amazon.com/s?k=5%20flashes&tag=errorcodefixe-20) | Outdoor control board fault |
| [6 flashes](https://www.amazon.com/s?k=6%20flashes&tag=errorcodefixe-20) | Outdoor ambient thermistor fault |
| [7 flashes](https://www.amazon.com/s?k=7%20flashes&tag=errorcodefixe-20) | Discharge thermistor fault |
| [Rapid flash](https://www.amazon.com/s?k=Rapid%20flash&tag=errorcodefixe-20) | Low voltage — check transformer |

## Common Causes by Code

- **2 flashes — High pressure** — Dirty or blocked condenser coil is the most common cause on GSX13 units installed in tight side-yard locations. Also check that the refrigerant charge hasn't been overcharged during a previous service call.
- **3 flashes — Low pressure** — Refrigerant leak or low ambient temperature. GSX13 units don't have a low-ambient kit — expect nuisance low-pressure trips if the unit is run when outdoor temps fall below 45°F.
- **4 flashes — Compressor protection** — Internal thermal overload is the primary suspect. Also check the dual run capacitor (compressor leg) and verify supply voltage is within 10% of nameplate. A weak capacitor causes hard starts that overheat the windings.
- **5 flashes — Control board** — Power surge is the most common cause. Check the fuse on the board before ordering a replacement board.
- **6 flashes — Ambient thermistor** — The thermistor is mounted on the control board in some GSX13 versions and externally in others. Resistance should read approximately 10kΩ at 77°F (25°C).
- **Rapid flash — Low voltage** — Measure 24VAC at the control board. Low voltage (below 19VAC) indicates a failing transformer, loose connection, or excessive control circuit load.

## Step-by-Step Fix {#fix}

1. **Count the flashes** — Observe the LED cycle through the fault code (pause, then flash count, then pause). Count flashes carefully — some codes are easy to misread between 3 and 4.
2. **For 2 flashes (high pressure)** — Power off the outdoor unit at the disconnect. Inspect the coil on all sides. Flush with water from inside-out. Confirm the fan spins freely — a seized bearing will cause the fan motor to trip thermal and stop.
3. **For 3 flashes (low pressure)** — Connect manifold gauges. Do not add refrigerant without locating the leak. Common leak points: service port Schrader valves, flare fittings at the unit, and brazed joints at the metering device.
4. **For 4 flashes (compressor protection)** — Power off, wait 30 minutes for thermal reset. Test the dual run capacitor — the compressor leg should test within ±6% of the rating on the label. Check supply voltage at the disconnect with the unit running (voltage under load should not sag more than 10% below nameplate).
5. **For rapid flash (low voltage)** — Measure secondary voltage at the transformer (R and C terminals on the control board). If below 19VAC, check for transformer overload (shorted control devices) or replace the transformer.

## Parts Often Needed

| Part | Notes |
|---|---|
| [Dual run capacitor](https://www.amazon.com/s?k=Dual%20run%20capacitor&tag=errorcodefixe-20) | Single most common GSX13 failure |
| [Contactor](https://www.amazon.com/s?k=Contactor&tag=errorcodefixe-20) | Check for pitting; replace if contacts are burned |
| [Control board](https://www.amazon.com/s?k=Control%20board&tag=errorcodefixe-20) | For Code 5; check fuse first (usually 5A) |
| [Run capacitor (fan only)](https://www.amazon.com/s?k=Run%20capacitor%20(fan%20only)&tag=errorcodefixe-20) | Some GSX13 boards use separate fan capacitor |
| [High-pressure switch](https://www.amazon.com/s?k=High-pressure%20switch&tag=errorcodefixe-20) | For persistent Code 2 after coil service |
| [Low-pressure switch](https://www.amazon.com/s?k=Low-pressure%20switch&tag=errorcodefixe-20) | For persistent Code 3 with correct charge |

## When to Call a Pro

Refrigerant work requires EPA 608 certification. If the GSX13 compressor is buzzing but not starting after capacitor replacement, the compressor may need a hard-start kit (potential relay + start capacitor) or may be mechanically seized. A technician with manifold gauges and a clamp meter is needed to distinguish between a slugged compressor and a failed one.
