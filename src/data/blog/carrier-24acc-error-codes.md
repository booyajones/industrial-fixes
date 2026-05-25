---
title: "Carrier 24ACC Air Conditioner Error Codes — Fault Code Diagnostic Guide"
description: "Complete guide to Carrier 24ACC central air conditioner error codes, flash sequences, common fault causes, and step-by-step fixes for the most common failures."
pubDatetime: 2026-04-22T22:00:00Z
modDatetime: 2026-04-22T22:00:00Z
author: "Marcus Webb"
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

| Flash Code | Meaning |
|------------|---------|
| 1 flash | Normal — unit running |
| 2 flashes | High-pressure switch open |
| 3 flashes | Low-pressure switch open |
| 4 flashes | Compressor protection fault |
| 5 flashes | Control board fault |
| 6 flashes | Outdoor ambient sensor fault |
| 7 flashes | Discharge temperature sensor fault |
| 8 flashes | Communication fault (if connected to Infinity system) |

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
| Run capacitor | [Amazon](https://www.amazon.com/dp/B01M05L7B3?ascsubtag=ecf-carrier-24acc-error-codes&tag=errorcodefixes-20) \| Dual run capacitor for compressor and fan; common failure |
| Contactor | [Amazon](https://www.amazon.com/dp/B0CJFZQVPT?ascsubtag=ecf-carrier-24acc-error-codes&tag=errorcodefixes-20) \| Pitted contacts cause voltage drop and Code 4 |
| Low-pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-carrier-24acc-error-codes&tag=errorcodefixes-20) \| Replace if Code 3 persists with correct charge |
| High-pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-carrier-24acc-error-codes&tag=errorcodefixes-20) \| Replace if Code 2 persists with clean coil |
| Condenser fan motor | [Amazon](https://www.amazon.com/dp/B0D2L5NSMM?ascsubtag=ecf-carrier-24acc-error-codes&tag=errorcodefixes-20) \| Check capacitor first before replacing |
| Control board | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?ascsubtag=ecf-carrier-24acc-error-codes&tag=errorcodefixes-20) \| For Code 5 or persistent unexplained faults |
## When to Call a Pro

Refrigerant handling requires EPA 608 certification. Any Code 3 investigation that goes beyond switch testing requires manifold gauges and refrigerant recovery equipment. If the compressor is failing to start (buzzing but not running), compressor replacement on a 24ACC is a major repair — get a cost estimate vs. full system replacement.

## Related Articles

- [Carrier 11 Error Code — Causes & Fix](/posts/carrier-11-error-code/)
- [Carrier 12 Error Code — Causes & Fix](/posts/carrier-12-error-code/)
- [Carrier 13 Error Code — Limit Switch Lockout Fix](/posts/carrier-13-error-code/)
- [Carrier 13 Soft Lockout — What's Different from Hard Lockout](/posts/carrier-13-soft-lockout/)
- [Carrier 14 Error Code — Causes & Fix](/posts/carrier-14-error-code/)

## See Also

- [Carrier 21 Error Code — Gas Heating Lockout Fix](/posts/carrier-21-error-code/)
- [Carrier 13 Soft Lockout — What's Different from Hard Lockout](/posts/carrier-13-soft-lockout/)
- [Carrier Error Code 61 — Rollout Switch Lockout](/posts/carrier-61-error-code/)
- [Carrier 46 Error Code — Check IFC: Board Self-Diagnosis Fault](/posts/carrier-46-error-code/)
