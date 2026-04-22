---
title: "Trane XR14 Heat Pump Error Codes — Fault Code Diagnostic Guide"
description: "Complete guide to Trane XR14 heat pump error codes, flash sequences, common fault causes, and step-by-step fixes for the most common failures."
pubDatetime: 2026-04-22T22:00:00Z
modDatetime: 2026-04-22T22:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - trane
  - heat-pump
---

## Trane XR14 Heat Pump Error Codes — What They Mean

The Trane XR14 is a single-stage heat pump in the XR series — a straightforward, builder-grade unit without communicating controls. It uses a conventional thermostat wiring scheme (Y, W, G, O) and a control board in the outdoor unit that communicates faults through LED flash codes. Unlike Trane's XL or XV series, the XR14 does not support communicating thermostats.

[Jump to Fix](#fix)

## Trane XR14 Flash Code Reference

| [Flash Code](https://www.amazon.com/s?k=Flash%20Code&tag=errorcodefixe-20) | Meaning |
|------------|---------|
| [1 flash](https://www.amazon.com/s?k=1%20flash&tag=errorcodefixe-20) | Normal operation |
| [2 flashes](https://www.amazon.com/s?k=2%20flashes&tag=errorcodefixe-20) | High-pressure switch open |
| [3 flashes](https://www.amazon.com/s?k=3%20flashes&tag=errorcodefixe-20) | Low-pressure switch open |
| [4 flashes](https://www.amazon.com/s?k=4%20flashes&tag=errorcodefixe-20) | Outdoor ambient lockout (below 0°F) |
| [5 flashes](https://www.amazon.com/s?k=5%20flashes&tag=errorcodefixe-20) | Compressor overload or protection device |
| [6 flashes](https://www.amazon.com/s?k=6%20flashes&tag=errorcodefixe-20) | Control board fault |
| [7 flashes](https://www.amazon.com/s?k=7%20flashes&tag=errorcodefixe-20) | Discharge line temperature sensor fault |
| [8 flashes](https://www.amazon.com/s?k=8%20flashes&tag=errorcodefixe-20) | Defrost control fault |

## Common Causes by Code

- **Code 2 — High pressure** — In cooling mode: dirty outdoor coil, failed condenser fan, or refrigerant overcharge. In heating mode: dirty indoor coil, failed indoor blower, or refrigerant overcharge. The XR14's single-speed compressor cannot reduce output when conditions are extreme — a dirty coil causes pressures to spike quickly.
- **Code 3 — Low pressure** — Low refrigerant (leak), failed low-pressure switch, or operation in very cold weather without a low-ambient kit. The XR14 is rated for heating down to 0°F outdoor ambient; below that, low-pressure lockout is normal.
- **Code 5 — Compressor protection** — The XR14's compressor has an internal overload. If it trips from excessive discharge temperature or voltage issues, allow 30 minutes for thermal reset. Check supply voltage under load — both legs should be within 10% of nameplate.
- **Code 8 — Defrost fault** — The XR14 uses a time-temperature defrost board. If the defrost control fails or the outdoor coil temperature sensor fails, defrost cycles either don't happen (ice accumulation) or happen continuously (nuisance cycling). Check the sensor resistance at the known ambient temperature.

## Step-by-Step Fix {#fix}

1. **Read the LED** — Open the XR14 access panel (screws on the side of the cabinet near the controls). The LED is on the defrost/control board.
2. **For Code 2 in cooling** — Turn off unit, inspect condenser coil, flush with garden hose. Verify fan direction (air should exit the top). Measure discharge pressure with gauges — over 400 PSI on R-410A at 95°F ambient suggests blocked coil or overcharge.
3. **For Code 2 in heating** — Check the indoor coil and blower. A locked-up indoor blower on a frigid day will cause immediate high-pressure trip in heat pump heating mode.
4. **For Code 3** — Connect gauges. Suction pressure in cooling should be 105–120 PSI at 75°F indoor. Below 80 PSI = low charge or restricted system. In heating mode, suction is the outdoor coil side — normal suction pressure at 30°F ambient is roughly 58–70 PSI.
5. **For Code 5** — Let the unit rest for 30 minutes. Check supply voltage both legs at the disconnect under load (start two legs independently). Check the run capacitor with a capacitor meter.
6. **For Code 8** — Locate the defrost sensor (clipped to the outdoor coil U-bend). Confirm it is firmly clipped; a loose sensor reads ambient air temperature instead of coil temperature and causes defrost timing errors.
7. **Clear and test** — Cycle power at the outdoor disconnect. Run the unit in both heating and cooling for 15 minutes each and monitor for fault recurrence.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [Run capacitor](https://www.amazon.com/s?k=Run%20capacitor&tag=errorcodefixe-20) | Dual run cap for compressor and fan; high failure rate |
| [Contactor](https://www.amazon.com/s?k=Contactor&tag=errorcodefixe-20) | Pitted contacts cause voltage drop |
| [Defrost board](https://www.amazon.com/s?k=Defrost%20board&tag=errorcodefixe-20) | For Code 8; match to XR14 model number |
| [Defrost sensor](https://www.amazon.com/s?k=Defrost%20sensor&tag=errorcodefixe-20) | Clipped to outdoor coil |
| [Low-pressure switch](https://www.amazon.com/s?k=Low-pressure%20switch&tag=errorcodefixe-20) | For Code 3 with correct refrigerant charge |
| [High-pressure switch](https://www.amazon.com/s?k=High-pressure%20switch&tag=errorcodefixe-20) | For Code 2 with clean coil and correct charge |

## When to Call a Pro

Heat pump refrigerant diagnosis requires EPA 608 certification and a manifold gauge set. If the XR14 is 10+ years old and showing low refrigerant, a refrigerant leak search (electronic leak detector or UV dye) should be performed before recharging. Repeated recharging without leak repair is not an approved practice under EPA Section 608.
