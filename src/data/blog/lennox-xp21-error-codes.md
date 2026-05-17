---
title: "Lennox XP21 Heat Pump Error Codes — iComfort Fault Code Guide"
description: "Complete guide to Lennox XP21 heat pump error codes displayed on the iComfort thermostat and control board, including common faults and step-by-step fixes."
pubDatetime: 2026-04-22T22:00:00Z
modDatetime: 2026-04-22T22:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - lennox
  - heat-pump
---

## Lennox XP21 Heat Pump Error Codes — What They Mean

The Lennox XP21 is a variable-capacity heat pump in the Elite series. It uses Lennox's Quantum Coil and a variable-speed scroll compressor for efficiency ratings up to 21 SEER. The XP21 communicates through the iComfort or Harmony III thermostat system, which displays fault codes and descriptions directly on the thermostat screen. Faults can also be read from the diagnostic LED on the outdoor control board.

[Jump to Fix](#fix)

## Lennox XP21 Common Fault Codes

| Code | Description |
|------|-------------|
| 104 | Low-pressure switch open |
| 107 | High-pressure switch open |
| 110 | Defrost sensor fault |
| 126 | Communication error between outdoor and indoor units |
| 204 | Discharge temperature sensor fault |
| 206 | Outdoor ambient temperature sensor fault |
| 227 | Compressor protection device tripped |
| 328 | Variable-speed compressor drive fault |
| 411 | Low-refrigerant charge detected |
| 512 | Outdoor fan motor fault |

## Common Causes by Code

- **Code 104 — Low pressure** — Low refrigerant charge is the most common cause. The XP21's variable-speed compressor unloads as pressure drops, which can mask a slow leak for months before the low-pressure switch opens. Also check the low-pressure switch itself.
- **Code 107 — High pressure** — Dirty condenser coil, failed outdoor fan motor, or refrigerant overcharge. The XP21 has a two-piece Quantum Coil that is difficult to clean from the inside — use a professional coil cleaner sprayed through the louvers.
- **Code 126 — Communication error** — The XP21 uses a two-wire communicating bus between the outdoor unit and the air handler. Check the two-wire connection at both units. A corroded terminal or shorted wire causes this code.
- **Code 328 — Compressor drive fault** — The XP21's variable-speed compressor uses an inverter drive in the outdoor unit. Drive faults indicate an electrical fault in the inverter, a refrigerant charge issue causing the drive to overload, or a failing compressor. This code requires professional diagnosis.
- **Code 411 — Low charge** — The XP21 has a refrigerant charge monitoring algorithm. Code 411 appears before Code 104 on newer firmware, giving an early warning of developing leaks.
- **Code 512 — Fan motor fault** — The ECM condenser fan motor has failed or has a communication error. Check the motor wiring, then test motor winding continuity.

## Step-by-Step Fix {#fix}

1. **Read fault history from iComfort** — Navigate to Menu > Diagnostics > Equipment Faults on the iComfort thermostat. The fault history shows codes, dates, and descriptions — far more useful than a single flash code.
2. **For Code 104 / 411** — Connect manifold gauges (R-410A; certified technician required). Check subcooling and superheat at multiple compressor speeds — the XP21 varies compressor speed to meet load, so measurements at full capacity are most representative.
3. **For Code 107** — Turn off the unit. Inspect the condenser coil from the outside. Clean with an approved coil cleaner. Confirm the outdoor fan is pulling air upward through the top of the unit.
4. **For Code 126** — Locate the two-wire communicating bus (usually blue and orange wires). Check connections at the outdoor unit terminal strip and the air handler board. Test for shorts or opens with a multimeter.
5. **For Code 328** — Do not attempt to bypass or ignore this code. The inverter drive can be damaged by running a low-charge system. Call an authorized Lennox dealer — the drive is a serviceable component but requires careful static-discharge procedures.
6. **For Code 512** — Power off the unit. Spin the fan blade by hand — it should rotate freely. Check the motor capacitor (if present) with a capacitor meter. If the motor hums but doesn't spin, the capacitor is likely failed.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Refrigerant charge (R-410A) | [Amazon](https://www.amazon.com/s?i=industrial&k=Refrigerant+charge+%28R-410A%29&tag=errorcodefixes-20) \| Requires EPA certification; fix leak first |
| Defrost sensor | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?tag=errorcodefixes-20) \| Clip-on type for outdoor coil |
| Communicating bus wire | [Amazon](https://www.amazon.com/s?i=industrial&k=Communicating+bus+wire&tag=errorcodefixes-20) \| 18-gauge two-wire; replace if damaged |
| ECM outdoor fan motor | [Amazon](https://www.amazon.com/dp/B0D2L5NSMM?tag=errorcodefixes-20) \| ECM type; confirm XP21 model compatibility |
| Compressor drive (inverter) | [Amazon](https://www.amazon.com/s?i=industrial&k=Compressor+drive+%28inverter%29&tag=errorcodefixes-20) \| Major part; Lennox dealer required for diagnosis |
| High/low pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?tag=errorcodefixes-20) \| Match to XP21 refrigerant circuit pressures |
## When to Call a Pro

The XP21's variable-speed inverter drive and communicating system require Lennox-specific diagnostic software to fully diagnose. Code 328 (drive fault) and repeated Code 411 (low charge) should not be serviced without certified refrigerant handling and inverter knowledge. Contact a Lennox Premier Dealer for advanced diagnostics.

## Related Articles

- [Lennox Error Code 292 — Ignition Failure Fix](/posts/lennox-292-error-code/)
- [Lennox EL296V Error Codes — Variable-Speed Furnace Diagnostic Guide](/posts/lennox-el296v-error-codes/)
- [Lennox Elite Series Furnace Error Codes — Fault Code Diagnostic Guide](/posts/lennox-elite-series-furnace-codes/)
- [Lennox 103 Error Code — Causes & Fix](/posts/lennox-error-code-103/)
- [Lennox Error Code 111 — Causes & Fix](/posts/lennox-error-code-111/)
