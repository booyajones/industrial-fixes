---
title: "LG CH23 Error Code - Causes & Fix"
description: "CH23 means the inverter DC link isn't charging. Usually caused by low voltage or loose connections. Check power supply first."
pubDatetime: 2026-05-31T00:52:46Z
modDatetime: 2026-05-31T00:52:46Z
author: "Dana Kowalski"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - lg
money_part: "LG outdoor unit inverter PCB (IPM board)"
most_likely_cause: "Low or unstable incoming voltage"
---

## LG CH23 Error Code — What It Means

CH23 appears on LG mini split systems when the inverter DC link in the outdoor unit fails to charge to its normal operating voltage after power is applied. The display alternates between CH and 23 on the indoor unit, outdoor unit, or wired remote. This fault tells you the DC bus capacitor bank is not reaching the threshold needed to run the compressor, usually because of a problem in the incoming power path or the rectifier and charging circuit on the outdoor unit's inverter board.

[Jump to Fix](#fix)

## Common Causes

- **Low or unstable incoming voltage** Utility supply below the rated range (220 V ±10% single-phase or 380 V ±10% three-phase) or unstable generator power prevents the DC link from charging fully.
- **Loose power or harness connections** Poorly seated connectors between the outdoor unit's main board, reactor harness, or inverter PCB interrupt the charging path.
- **Power surge or line transient** A voltage spike or electrical disturbance can damage the bridge rectifier or DC link capacitors and stop normal charging.
- **Faulty reactor or noise filter** A reactor coil with an open winding or a failed input filter stage drops the voltage before it reaches the rectifier.
- **Failed bridge diode or inverter PCB** An open or shorted diode in the rectifier bridge or a damaged IPM module on the inverter board prevents DC link voltage from building.
- **Main outdoor unit PCB defect** Faulty control logic or a damaged power-supply section on the main board can fail to enable the DC charging circuit correctly.

## Step-by-Step Fix {#fix}

1. **Turn off power at the breaker** and wait 60 seconds, then restore power to see if the fault clears after a single reset.
2. **Measure input voltage** at the outdoor unit terminal block with a multimeter while the system is off, confirming it falls within 220 V ±10% (single-phase) or 380 V ±10% (three-phase) per your model rating.
3. **Inspect and reseat all harness connectors** on the outdoor unit, paying special attention to the reactor harness and the plug to the inverter PCB.
4. **Measure DC link voltage** at the inverter board test points (consult your service manual for locations) with power on, checking that it reads more than 1.4 times the input voltage (around 310 V for 220 V supply).
5. **Check the noise filter output voltage** with your meter to confirm the filter stage is passing full voltage to the rectifier input.
6. **Test the bridge diode** in diode-check mode or resistance mode with power off, looking for normal forward and reverse readings in each leg (refer to your model's service data for thresholds).
7. **Replace the inverter PCB or main outdoor PCB** if upstream power and connections are confirmed good and the DC link still will not charge above 250 V, then clear the fault and test run the system.

## Parts Often Needed

| Part | Notes |
|------|-------|
| LG outdoor unit inverter PCB (IPM board) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-mini-split-ch23-error-code&k=LG+outdoor+unit+inverter+PCB+%28IPM+board%29&tag=errorcodefixes-20) \| Match your model and serial number on the original label. |
| LG outdoor unit main control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-mini-split-ch23-error-code&k=LG+outdoor+unit+main+control+board&tag=errorcodefixes-20) \| Verify board revision code matches your unit. |
| Reactor coil and harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-mini-split-ch23-error-code&k=Reactor+coil+and+harness&tag=errorcodefixes-20) \| Order as an assembly if the reactor tests open or the harness is damaged. |
| Bridge rectifier module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-mini-split-ch23-error-code&k=Bridge+rectifier+module&tag=errorcodefixes-20) \| Some units use a discrete module rather than board-mounted diodes. |

## When to Call a Pro

Call a licensed HVAC technician if you are not comfortable working with live line voltage or if your multimeter readings confirm normal input voltage but the DC link still reads below threshold. Diagnosing and replacing inverter boards, reactors, or bridge diodes requires understanding high-voltage DC circuits and proper discharge procedures. A pro will also have the factory service manual with your model's exact test-point locations, voltage tables, and component resistance specifications. If the unit is still under warranty, professional service may be required to preserve coverage.
