---
title: "Carrier 24ACC Air Conditioner Error Codes — Fault Code Diagnostic Guide"
description: "Complete guide to Carrier 24ACC central air conditioner error codes, flash sequences, common fault causes, and step-by-step fixes for the most common failures."
pubDatetime: 2026-04-22T22:00:00Z
modDatetime: 2026-04-22T22:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - carrier
  - air-conditioner
---

## Carrier 24ACC Air Conditioner Error Codes — What They Mean

The Carrier 24ACC is a Comfort series central air conditioner (condensing unit only). It uses a single-speed scroll compressor and a conventional contactor-based control system. Unlike Infinity-series units, the 24ACC communicates fault status through a diagnostic LED on the outdoor control board rather than through a communicating thermostat. The LED flash code identifies the active fault.

[Jump to Fix](#fix)

## Carrier 24ACC Flash Code Reference

| [Flash Code](https://www.amazon.com/s?k=Flash%20Code&tag=errorcodefixe-20) | Meaning |
|------------|---------|
| [1 flash](https://www.amazon.com/s?k=1%20flash&tag=errorcodefixe-20) | Normal — unit running |
| [2 flashes](https://www.amazon.com/s?k=2%20flashes&tag=errorcodefixe-20) | High-pressure switch open |
| [3 flashes](https://www.amazon.com/s?k=3%20flashes&tag=errorcodefixe-20) | Low-pressure switch open |
| [4 flashes](https://www.amazon.com/s?k=4%20flashes&tag=errorcodefixe-20) | Compressor protection fault |
| [5 flashes](https://www.amazon.com/s?k=5%20flashes&tag=errorcodefixe-20) | Control board fault |
| [6 flashes](https://www.amazon.com/s?k=6%20flashes&tag=errorcodefixe-20) | Outdoor ambient sensor fault |
| [7 flashes](https://www.amazon.com/s?k=7%20flashes&tag=errorcodefixe-20) | Discharge temperature sensor fault |
| [8 flashes](https://www.amazon.com/s?k=8%20flashes&tag=errorcodefixe-20) | Communication fault (if connected to Infinity system) |

## Common Causes by Code

- **Code 2 — High pressure** — Dirty condenser coil is the most common cause. The 24ACC coil must be clean on all sides — a garden hose flush from inside-out dislodges debris that compressed air only pushes deeper. Also check condenser fan motor: if the fan is spinning backward, high-pressure faults occur immediately.
- **Code 3 — Low pressure** — Low refrigerant charge (leak) or a failed low-pressure switch. On a 24ACC, low pressure can also occur in very cold ambient temperatures (below 45°F) — the unit has a low-ambient kit available to prevent nuisance trips.
- **Code 4 — Compressor protection** — The 24ACC compressor has an internal thermal overload. If the compressor has been running in high-pressure or high-ambient conditions, the overload trips and won't reset for 20–30 minutes. The code also appears when supply voltage is low (below 208V on a 240V unit).
- **Code 5 — Control board** — Rare. Usually caused by a lightning strike, power surge, or moisture intrusion into the control box. Check for corroded terminals or burnt traces on the board.
- **Code 6 — Ambient sensor** — The outdoor ambient temperature sensor is on the control board. If the sensor reads out of range, the board will not operate in low-ambient or high-ambient protection modes. Check the sensor resistance vs. the temperature-resistance chart in the service manual.

## Step-by-Step Fix {#fix}

1. **Read the LED** — Open the side access panel on the 24ACC outdoor unit. The control board LED is visible near the contactor. Record the flash code.
2. **For Code 2 (high pressure)** — Turn off the unit. Inspect the condenser coil from outside — debris, cottonwood seeds, or pet hair often block the coil base. Flush the coil with water from inside-out. Confirm the fan blade is spinning in the correct direction (should draw air up through the top of the unit).
3. **For Code 3 (low pressure)** — Connect refrigerant gauges (R-410A; EPA certification required). Check suction pressure — should be approximately 100–110 PSI at 70°F ambient. Below 80 PSI suggests low charge. Also check low-pressure switch continuity (should be closed above 40 PSI on R-410A).
4. **For Code 4 (compressor protection)** — Let the unit sit off for 30 minutes. Check supply voltage at the disconnect — both legs should read within 10% of nameplate voltage. Check capacitor (start and run) before condemning the compressor.
5. **For Code 5** — Inspect the control board for burn marks, corroded terminals, or shorted components. Check fuse on the board (if present). Measure 24VAC from the transformer.
6. **Clear and test** — After any repair, restore power, confirm the contactor pulls in cleanly, and monitor system pressures for the first 10 minutes of operation.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [Run capacitor](https://www.amazon.com/s?k=Run%20capacitor&tag=errorcodefixe-20) | Dual run capacitor for compressor and fan; common failure |
| [Contactor](https://www.amazon.com/s?k=Contactor&tag=errorcodefixe-20) | Pitted contacts cause voltage drop and Code 4 |
| [Low-pressure switch](https://www.amazon.com/s?k=Low-pressure%20switch&tag=errorcodefixe-20) | Replace if Code 3 persists with correct charge |
| [High-pressure switch](https://www.amazon.com/s?k=High-pressure%20switch&tag=errorcodefixe-20) | Replace if Code 2 persists with clean coil |
| [Condenser fan motor](https://www.amazon.com/s?k=Condenser%20fan%20motor&tag=errorcodefixe-20) | Check capacitor first before replacing |
| [Control board](https://www.amazon.com/s?k=Control%20board&tag=errorcodefixe-20) | For Code 5 or persistent unexplained faults |

## When to Call a Pro

Refrigerant handling requires EPA 608 certification. Any Code 3 investigation that goes beyond switch testing requires manifold gauges and refrigerant recovery equipment. If the compressor is failing to start (buzzing but not running), compressor replacement on a 24ACC is a major repair — get a cost estimate vs. full system replacement.
