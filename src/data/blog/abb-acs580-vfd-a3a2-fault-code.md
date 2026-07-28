---
title: "ABB ACS580 A3A2 Fault - Causes & Fix"
description: "A3A2 means DC link undervoltage: the drive's internal DC bus is too low. Most often a blown input fuse or missing phase."
pubDatetime: 2026-06-21T10:36:03Z
modDatetime: 2026-06-21T10:36:03Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - abb
money_part: "Input fuses (Class J or CC)"
most_likely_cause: "Blown input fuse or missing supply phase"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Measure AC voltage at L1, L2, and L3 input terminals with a multimeter to confirm all three phases are present and within 10% of the drive's rated voltage"
  - "Check parameter 95.01 (Supply voltage) on the drive's control panel and verify it matches the actual measured incoming voltage"
  - "Inspect input terminal connections for loose or corroded wiring"
no_buy_pct: "40%"
---

## What this code means
The A3A2 fault code on an ABB ACS580 variable frequency drive indicates DC link undervoltage. The drive has detected that the intermediate circuit DC voltage is too low while the drive is stopped or starting. The inverter cannot generate the required AC output voltage to the motor because the energy stored in the DC link capacitors is below the minimum operational threshold.

This is a critical power supply issue. The drive expects the rectifier bridge to convert incoming three-phase AC into a stable DC bus voltage (for example, around 680V DC on a 480V-rated drive). When that DC voltage drops below roughly 65% of the nominal value, the drive shuts down with A3A2 to protect itself and the motor from erratic operation.

## Before You Replace Anything

Technicians sometimes replace the rectifier bridge or control board before checking input fuses and wiring. Always measure AC voltage at the drive input terminals and verify fuse continuity first, both of which take minutes and cost nothing.

## Common Causes

- **Blown input fuse or missing phase** A blown fuse in the input switchgear or cabling creates a single-phase condition, starving the rectifier of the full three-phase power it needs to maintain DC bus voltage.
- **Low incoming utility voltage (brown-out)** The supply voltage is significantly below the drive's rating, for example a 480V drive receiving only 400V, so the rectifier cannot produce enough DC voltage.
- **Incorrect parameter 95.01 setting** Parameter 95.01 (Supply voltage) is set higher than the actual incoming voltage, causing the drive to expect a higher DC level than the rectifier can deliver.
- **Defective rectifier bridge** One or more diodes or thyristors in the input rectifier have failed, preventing proper conversion of AC to DC even when input power is good.
- **Loose or corroded input wiring** Poor connections at the drive input terminals or in the upstream switchgear create voltage drops or intermittent power, starving the DC link.

## Step-by-Step Fix {#fix}

1. **Lock out and tag out** all upstream power sources. Use a multimeter to measure AC line voltage at the drive's L1, L2, and L3 input terminals. Confirm all three phases are present and within 10% of the drive's rated voltage (for example, 432V to 528V on a 480V drive).
2. **Navigate to parameter 95.01** (Supply voltage) on the drive's keypad or control interface. Verify the setting matches the actual measured input voltage, not the nominal rating. Adjust if needed and reset the fault to see if it clears.
3. **Test input fuses** for continuity. De-energize the circuit, then use a multimeter to check each fuse in the input switchgear or disconnect. A blown fuse reads open (infinite resistance). Replace any blown fuses with the correct class and amperage.
4. **Inspect all input wiring** at the drive terminals and upstream connections. Look for loose terminal screws, cold solder joints, or corrosion. Tighten connections and clean corroded terminals.
5. **Measure DC bus voltage** with the drive stopped. Access the DC+ and DC- terminals (consult your model's manual for safe test points). With AC input present, you should read approximately 1.35 times the AC line-to-line voltage (for example, roughly 650V DC on a 480V AC supply). If the DC voltage is near zero, the rectifier bridge is faulty.
6. **Check parameter 95.04** (Control board supply) to confirm the internal logic power is stable. If the control board voltage is erratic, the fault may stem from a failing power supply module rather than the main rectifier.
7. **Replace the rectifier bridge** if diagnostics confirm no DC voltage with good AC input. Order the correct rectifier module for your drive frame size and rating. Follow the manufacturer's procedure to discharge capacitors before removing covers and swapping the module.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Input fuses (Class J or CC) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-a3a2-fault-code&k=Input+fuses+%28Class+J+or+CC%29&tag=errorcodefixes-20) \| Replace with fuses matching the drive's input current rating and interrupting capacity. |
| Rectifier bridge module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-a3a2-fault-code&k=Rectifier+bridge+module&tag=errorcodefixes-20) \| Order the exact replacement for your ACS580 frame size and voltage rating from ABB or an authorized distributor. |
| Input line reactor or choke | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-a3a2-fault-code&k=Input+line+reactor+or+choke&tag=errorcodefixes-20) \| If brown-out conditions are frequent, add a line reactor to stabilize incoming voltage and protect the rectifier. |

## When to Call a Pro

Call a qualified industrial electrician or VFD service technician if you are not trained to work on high-voltage equipment. The ACS580 operates at lethal voltages (240V to 690V AC, and DC bus voltages above 300V). Measuring the DC bus requires understanding how to safely discharge capacitors and access internal test points. If the rectifier bridge or control board needs replacement, the repair involves firmware configuration, torque specs for bus bars, and thermal compound application that require factory training. Always call a pro if you find a hardware failure inside the drive or if input voltage issues trace back to utility transformers or switchgear you are not authorized to service.
