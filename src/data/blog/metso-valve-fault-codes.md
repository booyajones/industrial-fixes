---
title: "Metso Automation Valve Fault Codes — Neles ND9000 / NDX Guide"
description: "Metso Automation (Neles) valve positioner fault codes for ND9000 and NDX series: alarms, diagnostics, and troubleshooting steps for industrial control valves."
pubDatetime: 2026-04-22T21:00:00Z
modDatetime: 2026-04-22T21:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - valve
  - metso
  - neles
  - positioner
  - industrial
money_part: "Position sensor module"
---

## Metso Valve Positioner Fault Codes — Quick Reference

Metso Automation (now Neles) ND9000 and NDX intelligent valve controllers report faults over HART, Foundation Fieldbus, or Profibus DP. Alarms are classified as process (F), maintenance (M), or advisory (A).

| Fault Code | Meaning | Quick Fix |
|-----------|---------|-----------|
| F01 — Position Sensor | Position sensor signal out of range | Check sensor and harness |
| F02 — Pressure Sensor | Internal pressure sensor fault | Replace instrument |
| F03 — Drive Current | Output current high or low | Check I/P converter and supply |
| F04 — Supply Pressure | Supply pressure below minimum | Check supply regulator |
| F05 — Valve Deviation | Valve not at setpoint | Check actuator and process |
| M01 — Travel Accumulation | Travel limit reached | Schedule packing and seat inspection |
| M02 — Cycle Counter | Cycle limit reached | Inspect valve internals |
| A01 — Temperature | Internal temperature out of range | Check ambient temperature |

## Most Common Faults

### F01 — Position Sensor Fault
The Hall-effect or potentiometer position sensor signal is out of calibrated range. Check the sensor connector for corrosion or vibration damage. If the sensor is mechanically misaligned after maintenance, re-run the auto-calibration routine in FieldCare or Metso DNA.

### F05 — Valve Deviation
The positioner commanded the valve to move but measured travel does not match setpoint within the tolerance window. This points to high friction from tight packing, actuator problems, or excessive process differential pressure. Run the partial stroke test to observe response characteristics.

### F04 — Supply Pressure Low
Metso positioners require clean, dry instrument air typically at 35–100 psi. Confirm the supply pressure regulator is upstream and set correctly. Check supply tubing for leaks.

## Diagnostic Features

- **Auto-calibration** — learns travel limits and positions
- **Partial stroke testing** — safety valve verification without full closure
- **Step response** — measures valve response speed and gain
- **Torque profile** — identifies packing friction and seat load

## Parts Often Needed

| Part | Notes |
|------|-------|
| Position sensor module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-metso-valve-fault-codes&k=Position+sensor+module&tag=errorcodefixes-20) \| Replaces if F01 persists |
| Supply pressure regulator | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-metso-valve-fault-codes&k=Supply+pressure+regulator&tag=errorcodefixes-20) \| Replaces on F04 faults |
| I/P converter | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-metso-valve-fault-codes&k=I%2FP+converter&tag=errorcodefixes-20) \| Replaces on F03 faults |
| Packing set | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-metso-valve-fault-codes&k=Packing+set&tag=errorcodefixes-20) \| Replace on high friction diagnostics |
## Jump to Fix

- **F01 sensor fault** → Check connector → Re-calibrate → Replace sensor
- **F05 deviation** → Run partial stroke → Check actuator → Inspect packing
- **F04 supply** → Verify supply pressure → Check regulator

## When to Call a Pro
Metso/Neles positioners require FieldCare or Metso DNA for full diagnostic access. Authorized service partners provide calibration and on-site repair.
