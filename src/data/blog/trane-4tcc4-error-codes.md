---
title: "Trane 4TCC4 Mini Split Error Codes — Causes & Fix"
description: "Trane 4TCC4 mini split error codes explained — what each code means, why it happens, and how to fix it."
pubDatetime: 2026-04-22T15:00:00Z
modDatetime: 2026-04-22T15:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - mini-split
  - trane
---

## Trane 4TCC4 Mini Split Error Codes — What They Mean

The Trane 4TCC4 series is Trane's single-zone ductless mini-split indoor unit, typically paired with 4TXK4 or 4TXK6 outdoor units. These units display fault codes on the front panel LED when the control system detects an abnormal condition. The 4TCC4 platform is part of Trane's ductless product line (developed in partnership with Mitsubishi's OEM manufacturing partners) and uses alphanumeric codes that align broadly with Trane's comfort system diagnostic standard.

[Jump to Fix](#fix)

## Common Error Codes and Causes

- **E1 — Communication Fault** — Indoor and outdoor units have lost communication on the S-wire. Most often a loose terminal or a damaged wire in the line set bundle.
- **E2 — Room Temperature Sensor Fault** — The indoor ambient thermistor is open, shorted, or disconnected. Check the sensor connector on the indoor PCB.
- **E3 — Evaporator Coil Sensor Fault** — The indoor coil (T2) thermistor is faulty. Check connection and measure resistance (~10 kΩ at 25°C for standard NTC).
- **E4 — Outdoor Coil/Ambient Sensor Fault** — An outdoor-side thermistor has failed or its connector has corroded. More common in humid or coastal environments.
- **H6 — Indoor Fan Motor Fault** — The indoor blower motor is not operating within spec. Check for blockage, a failed motor, or a failed motor drive circuit on the indoor PCB.
- **P0 — Refrigerant Leak or Low Charge** — The system has detected low refrigerant conditions. Check pressures; do not operate the compressor with a confirmed leak.
- **P5 — Outdoor Fan Motor Fault** — The outdoor fan motor has stopped or is running out of spec. Check for debris, a seized motor, or a failed capacitor.
- **LC — Communication Lockout** — Repeated E1 faults have locked the system. Power cycle and address the root communication fault.

## Step-by-Step Fix {#fix}

1. **Record the fault code** — Note the exact code before power-cycling so you can trace the root cause.
2. **Power cycle for communication faults (E1/LC)** — Cut breaker power for 2 minutes, then restore. If the fault returns, inspect the S-wire at both terminal blocks for corrosion or looseness.
3. **Test thermistors for sensor faults (E2/E3/E4)** — Disconnect the thermistor and measure resistance at ambient temperature. Replace any sensor outside the 9–11 kΩ range at 25°C.
4. **Inspect fan motors (H6/P5)** — Manually spin the indoor blower or outdoor fan (with power off) — it should turn freely. A seized or dragging motor requires replacement.
5. **Check refrigerant charge (P0)** — Connect manifold gauges and compare readings to the R-410A pressure curve at the current ambient. Low suction pressure indicates undercharge.
6. **Reset and test** — Power cycle after any repair. Run a full 30-minute cooling cycle and confirm the code does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Indoor ambient thermistor | [Amazon](https://www.amazon.com/s?k=Indoor+ambient+thermistor&tag=errorcodefixes-20) \| Trane 4TCC4 OEM; verify resistance curve |
| Indoor coil thermistor | [Amazon](https://www.amazon.com/s?k=Indoor+coil+thermistor&tag=errorcodefixes-20) \| Often sold as a kit with the ambient sensor |
| Outdoor fan motor | [Amazon](https://www.amazon.com/dp/B0D2L5NSMM?tag=errorcodefixes-20) \| Match nameplate HP, RPM, and shaft size |
| Communication wire | [Amazon](https://www.amazon.com/s?k=Communication+wire&tag=errorcodefixes-20) \| 18 AWG, length to match installation |
## When to Call a Pro

P0 refrigerant codes require gauge sets and EPA 608 certification. H6 and P5 motor replacements are straightforward but require a comfort with ductless system wiring — call a Trane-authorized technician if unsure.

## Related Articles

- [Trane 1 Flash Error Code — Causes & Fix](/posts/trane-1-flash-error-code/)
- [Trane Error Code 126 — Ignition Lockout Fix](/posts/trane-126-error-code/)
- [Trane 2 Flashes Error Code — Causes & Fix](/posts/trane-2-flashes-error-code/)
- [Trane 3 Flashes Error Code — Pressure Switch Fault Fix](/posts/trane-3-flashes-error-code/)
- [Trane 3 Flash Pressure Switch Fault — Detailed Diagnosis Guide](/posts/trane-3-flashes-pressure-switch/)
