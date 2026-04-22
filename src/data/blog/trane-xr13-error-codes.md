---
title: "Trane XR13 Air Conditioner Error Codes — Fault Code Diagnostic Guide"
description: "Complete guide to Trane XR13 central air conditioner error codes, LED flash sequences, common fault causes, and step-by-step repair procedures."
pubDatetime: 2026-04-22T23:00:00Z
modDatetime: 2026-04-22T23:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - trane
  - air-conditioner
---

## Trane XR13 Air Conditioner Error Codes — What They Mean

The Trane XR13 is a 13 SEER single-stage central air conditioner in Trane's value-line residential series. It uses R-410A refrigerant and a single-speed scroll compressor. Like most entry-level condensing units, the XR13 relies on a diagnostic LED on the control board to report faults via flash sequences rather than communicating through a smart thermostat. The LED is visible through the access panel on the outdoor unit.

[Jump to Fix](#fix)

## Trane XR13 LED Flash Code Reference

| [Flash Sequence](https://www.amazon.com/s?k=Flash%20Sequence&tag=errorcodefixe-20) | Fault |
|---|---|
| [Continuous ON](https://www.amazon.com/s?k=Continuous%20ON&tag=errorcodefixe-20) | Normal operation |
| [2 flashes](https://www.amazon.com/s?k=2%20flashes&tag=errorcodefixe-20) | High-pressure switch open |
| [3 flashes](https://www.amazon.com/s?k=3%20flashes&tag=errorcodefixe-20) | Low-pressure switch open |
| [4 flashes](https://www.amazon.com/s?k=4%20flashes&tag=errorcodefixe-20) | Open circuit — compressor protection device |
| [5 flashes](https://www.amazon.com/s?k=5%20flashes&tag=errorcodefixe-20) | Control board fault |
| [6 flashes](https://www.amazon.com/s?k=6%20flashes&tag=errorcodefixe-20) | Outdoor thermistor fault |
| [7 flashes](https://www.amazon.com/s?k=7%20flashes&tag=errorcodefixe-20) | Loss of charge (pressure switch) |
| [8 flashes](https://www.amazon.com/s?k=8%20flashes&tag=errorcodefixe-20) | Anti-short cycle delay active |
| [9 flashes](https://www.amazon.com/s?k=9%20flashes&tag=errorcodefixe-20) | Communication fault (if connected to ComfortLink thermostat) |

## Common Causes by Code

- **2 flashes — High pressure** — Restricted condenser coil, failed condenser fan motor, or refrigerant overcharge. The XR13 does not have an inverter-driven fan — if the capacitor fails, the fan stops and high-pressure faults follow within minutes.
- **3 flashes — Low pressure** — Refrigerant leak or low ambient temperature. The XR13 has no factory low-ambient kit and will trip the low-pressure switch below about 45°F outdoor temperature.
- **4 flashes — Compressor protection** — The XR13 compressor has an internal overload protector. A hard start kit reduces start current and can extend compressor life when supply voltage is marginal.
- **5 flashes — Control board** — Usually traced to power surge damage. Check the 5A fuse on the board and the 24V transformer secondary voltage (should be 24–28VAC at full load).
- **8 flashes — Anti-short cycle** — Normal behavior after a compressor shutdown; the board delays restart for 5 minutes to protect the compressor from liquid slugging. Not a fault — just wait.

## Step-by-Step Fix {#fix}

1. **Locate the LED** — Open the service access panel on the XR13 outdoor unit. The control board is mounted near the contactor. The LED flashes the fault code continuously until cleared.
2. **For 2 flashes (high pressure)** — Shut down the unit. Inspect the condenser coil on all four sides — the XR13's coil can accumulate debris between the fins where visual inspection misses it. Use a fin comb for badly bent fins. Verify the fan is spinning (capacitor test with a capacitor meter is more reliable than a visual check).
3. **For 3 flashes (low pressure)** — Connect manifold gauges. R-410A suction pressure should be 100–115 PSI at 70°F ambient. If pressure is low, locate the leak before recharging — UV dye injection or an electronic leak detector at all joints and the service ports.
4. **For 4 flashes (compressor protection)** — Allow 30 minutes for thermal overload reset. Measure supply voltage at both legs of the disconnect — should be within ±10% of nameplate voltage. Test the dual run capacitor with a capacitor meter.
5. **Restart and monitor** — After any repair, power up the unit and monitor suction and discharge pressures for the first 10 minutes. A properly operating XR13 should have suction around 105–120 PSI and discharge around 280–320 PSI at standard conditions.

## Parts Often Needed

| Part | Notes |
|---|---|
| [Dual run capacitor](https://www.amazon.com/s?k=Dual%20run%20capacitor&tag=errorcodefixe-20) | Most common failure on XR13 outdoor units |
| [Contactor](https://www.amazon.com/s?k=Contactor&tag=errorcodefixe-20) | Replace if contacts are pitted or discolored |
| [Condenser fan motor](https://www.amazon.com/s?k=Condenser%20fan%20motor&tag=errorcodefixe-20) | Confirm rotation direction (counterclockwise from top) |
| [High-pressure switch](https://www.amazon.com/s?k=High-pressure%20switch&tag=errorcodefixe-20) | Replace if Code 2 persists after coil cleaning |
| [Low-pressure switch](https://www.amazon.com/s?k=Low-pressure%20switch&tag=errorcodefixe-20) | Replace if Code 3 persists with correct charge |
| [Control board](https://www.amazon.com/s?k=Control%20board&tag=errorcodefixe-20) | For Code 5; check fuse before replacing board |

## When to Call a Pro

Any investigation of low-pressure or high-pressure faults that goes beyond visual inspection and switch testing requires refrigerant manifold gauges and EPA 608 certification. If the compressor hums but won't start, test the capacitor first — a failed run capacitor is the most common cause of compressor no-start on XR13 units.
