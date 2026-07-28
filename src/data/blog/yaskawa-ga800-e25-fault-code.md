---
title: "Yaskawa GA800 E25 Fault - Causes & Fix"
description: "E25 on a Yaskawa GA800 means main circuit power establishment error. Learn causes, diagnostic steps, and when to call support."
pubDatetime: 2026-05-30T12:34:33Z
modDatetime: 2026-05-30T12:34:33Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Input line fuses"
most_likely_cause: "Missing or unbalanced input phase"
---

## What this code means
E25 on the Yaskawa GA800 is a main circuit or power supply establishment error. The drive does not recognize that the DC bus or main circuit power has come up correctly, so it trips to protect itself. This fault means the inverter detected an abnormality during power-up or the internal main circuit failed to establish the correct operating condition.

The drive will not run until the root cause is found and corrected. This is not a nuisance trip. It points to either an input power problem or an internal failure in the power section of the drive.

## Common Causes

- **Missing or unbalanced input phase** One or more incoming line phases are absent, creating an undervoltage condition that prevents proper DC bus formation.
- **Blown fuse or tripped circuit protection** An upstream fuse or GFCI has opened due to a fault, cutting power before the drive's internal supply can establish.
- **Loose or damaged input wiring** Poor terminal connections, corroded lugs, or undersized wire create high resistance or intermittent contact at power-up.
- **Electrical noise or transient event** A voltage spike, surge, or EMI disturbance during energization interferes with the drive's power-up recognition logic.
- **Internal main circuit component failure** Damage to rectifier diodes, bus capacitors, or other power section hardware prevents the DC link from charging normally.
- **Peripheral device rating mismatch** An external contactor, reactor, or filter is wired incorrectly or exceeds the drive's design limits, causing a power-supply anomaly.

## Step-by-Step Fix {#fix}

1. **Disconnect all power** and wait the discharge time printed on the drive's warning label until all indicator lights are off.
2. **Inspect input fuses and circuit protection** for blown elements or tripped breakers, then check for evidence of short circuits or ground faults before proceeding.
3. **Verify incoming line voltage** at the drive's input terminals with a multimeter, confirming all three phases are present and within the drive's rated supply range.
4. **Examine all input and output wiring** for loose lugs, burned terminals, or damaged insulation, and re-torque connections to the values in the installation manual.
5. **Check for signs of electrical noise** by reviewing recent event logs or speaking with the customer about nearby equipment starts, lightning, or utility disturbances that coincided with the fault.
6. **Remove the cause of the fault**, correct any wiring or supply issues, then re-energize and reset the drive by cycling control power or pressing the reset button.
7. **If E25 returns immediately**, treat it as an internal main circuit failure and contact Yaskawa technical support or an authorized service center rather than replacing parts by trial.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Input line fuses | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-e25-fault-code&k=Input+line+fuses&tag=errorcodefixes-20) \| Replace with the amperage and speed rating shown in the drive's input schematic if blown. |
| Input terminal block | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-e25-fault-code&k=Input+terminal+block&tag=errorcodefixes-20) \| Order from Yaskawa if terminals are cracked, burned, or cannot hold torque. |

## When to Call a Pro

Call Yaskawa technical support or an authorized drive service center if the fault persists after you have confirmed good input power, tight wiring, and no external disturbances. E25 that returns after basic checks indicates an internal main circuit component failure. Yaskawa's maintenance documentation limits field repair to fans and control boards. Power-section faults require factory-level diagnostics and component replacement. Do not guess at internal parts or attempt circuit-board work without manufacturer authorization.
