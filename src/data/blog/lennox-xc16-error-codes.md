---
title: "Lennox XC16 Air Conditioner Error Codes — Fault Code Diagnostic Guide"
description: "Complete guide to Lennox XC16 air conditioner error codes, alert codes, common fault causes, and step-by-step fixes for technicians and homeowners."
pubDatetime: 2026-04-22T23:00:00Z
modDatetime: 2026-04-22T23:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - lennox
  - air-conditioner
money_part: "Dual run capacitor"
---

## Lennox XC16 Air Conditioner Error Codes — What They Mean

The Lennox XC16 is a 16–21 SEER2 two-stage central air conditioner that uses the iComfort S30 or compatible communicating thermostat when installed in a full Dave Lennox Signature system. It communicates faults both through the thermostat display (when in communicating mode) and through a diagnostic LED on the outdoor unit board. The XC16 uses R-410A and features a two-stage scroll compressor for improved efficiency and dehumidification at part load.

## Lennox XC16 Error Code Reference

| Alert Code | Meaning |
|---|---|
| 103 | High-pressure switch open |
| 111 | Low-pressure switch open |
| 114 | Loss of charge — pressure too low |
| 125 | Outdoor fan motor fault |
| 204 | Compressor protection — thermal overload |
| 223 | Discharge temperature sensor fault |
| 225 | Outdoor ambient sensor fault |
| 231 | Communication fault — outdoor board |
| 327 | High-stage compressor fault |
| 332 | Contactor fault detected |
| 411 | Control board hardware fault |

## Common Causes by Code

- **Alert 103 — High pressure** — Dirty condenser coil or failed outdoor fan. The XC16's two-stage compressor pushes higher mass flow at first stage versus many single-stage units — a partially fouled coil can cause intermittent high-pressure trips only at first stage, making it harder to diagnose.
- **Alert 111/114 — Low pressure / loss of charge** — Refrigerant leak. Common leak points on XC16 units are the Schrader valve cores, flare fittings at the unit connections, and the evaporator coil (inspect with UV light after adding dye).
- **Alert 125 — Outdoor fan motor** — The XC16 uses a PSC condenser fan motor. Test the run capacitor (shared or dedicated depending on board version) before condemning the motor. Motor replacement requires the correct HP, RPM, and rotation direction.
- **Alert 204 — Compressor thermal overload** — Allow 30-minute cooldown. Check supply voltage, capacitor, and contactor contacts before suspecting the compressor itself.
- **Alert 231 — Communication** — Inspect the communication wire (4-conductor from thermostat to air handler to outdoor unit). A pinched or stapled wire is the most common cause.

## Step-by-Step Fix {#fix}

1. **Read the thermostat** — On iComfort S30 or iComfort Wi-Fi, navigate to System > Alerts to view the active alert code and a brief description. Record the code before clearing.
2. **For Alert 103 (high pressure)** — Turn off at thermostat. Clean the condenser coil using Nu-Calgon Coil-Brite or equivalent — spray from inside-out. Confirm fan rotation (counterclockwise from top, drawing air upward).
3. **For Alert 111/114 (low pressure/loss of charge)** — Connect manifold gauges. Note static pressure when the unit is off (should equalize to 120–200 PSI depending on ambient). If static pressure is 0, the unit has no refrigerant — do not operate the compressor.
4. **For Alert 125 (fan motor)** — Check the run capacitor with a capacitor meter. Measure voltage at the fan motor terminals with the unit calling for cooling. If voltage is present and the motor doesn't spin, the motor has failed.
5. **Clear and restart** — At the thermostat, clear the alert, set a cooling demand, and observe the first 5 minutes of operation. The XC16 starts in first stage (lower speed); confirm stage 2 engages after the demand is sustained.

## Parts Often Needed

| Part | Notes |
|---|---|
| Dual run capacitor | [View on Amazon](https://www.amazon.com/dp/B01M05L7B3?ascsubtag=ecf-lennox-xc16-error-codes&tag=errorcodefixes-20) \| Compressor and fan; most common single failure |
| Contactor | [View on Amazon](https://www.amazon.com/dp/B0CJFZQVPT?ascsubtag=ecf-lennox-xc16-error-codes&tag=errorcodefixes-20) \| Two-pole; check for pitting and coil resistance |
| Condenser fan motor | [View on Amazon](https://www.amazon.com/dp/B0D2L5NSMM?ascsubtag=ecf-lennox-xc16-error-codes&tag=errorcodefixes-20) \| Match HP, RPM, frame size |
| High-pressure switch | [View on Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-lennox-xc16-error-codes&tag=errorcodefixes-20) \| 610 PSIG cutout for R-410A |
| Low-pressure switch | [View on Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-lennox-xc16-error-codes&tag=errorcodefixes-20) \| 50 PSIG cutout; replace if code persists |
| Outdoor communication board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lennox-xc16-error-codes&k=Outdoor+communication+board&tag=errorcodefixes-20) \| For Alert 231 or 411 |
## When to Call a Pro

The XC16's two-stage compressor makes refrigerant charging more complex than a single-stage unit — the system must be checked at both low-stage and high-stage operation to confirm correct superheat and subcooling. Lennox requires iComfort-enabled service tools for advanced diagnostics. Contact a Lennox Premier Dealer for communicating system issues beyond basic troubleshooting.
