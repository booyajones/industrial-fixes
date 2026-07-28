---
title: "Yaskawa GA800 Fault 030 - Causes & Fix"
description: "Fault 030 means DC bus overvoltage. Most common cause: motor decelerating too fast. Increase deceleration time or add brake resistor."
pubDatetime: 2026-06-27T11:48:14Z
modDatetime: 2026-06-27T11:48:14Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Yaskawa brake resistor for GA800"
most_likely_cause: "Excessive motor deceleration generating back-EMF"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Check parameter F010 (Deceleration Time 1) and increase it to 5-10 seconds to reduce back-EMF"
  - "Measure input line voltage at drive terminals to verify it is within rated range (380-460V for 400V-class)"
  - "Verify motor cable length is within drive specifications and check for damaged insulation"
part_price: "$80-250 for brake resistor"
no_buy_pct: "60%"
---

## What this code means
Fault 030 (OV) indicates the DC bus voltage inside the GA800 drive has exceeded the overvoltage detection threshold, typically above 800 VDC for 400V-class drives or above 750 VDC for 200V-class drives depending on the model. The drive shuts down output to protect IGBTs and capacitors from damage. Note that F030 is a parameter name (Acceleration Time 1), not a fault code. The actual fault code is 030, which corresponds to overvoltage.

## Before You Replace Anything

Technicians often replace the drive power board when the real cause is simply deceleration time set too short. Check and increase parameter F010 (Deceleration Time 1) and verify brake resistor sizing before replacing any electronics.

## Common Causes

- **Motor decelerating too quickly (~45%)** When deceleration time is set too short, the motor acts as a generator and pushes energy back into the DC bus faster than the drive can dissipate it, causing overvoltage.
- **Missing or undersized brake resistor (~30%)** Without a properly sized brake resistor, the drive cannot dissipate regenerative energy during deceleration or when a heavy load is being lowered.
- **Input voltage too high (~15%)** Line voltage above nominal (for example above 480V on a 400V drive) directly raises the DC bus voltage beyond the overvoltage threshold.
- **Faulty DC bus capacitors (~6%)** Degraded or failing DC link capacitors cause voltage instability and can trigger overvoltage faults during normal operation.
- **Long motor cable with high capacitance (~4%)** Excessive cable capacitance can cause voltage spikes during PWM switching and contribute to DC bus overvoltage events.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault occur only during motor deceleration or stopping?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor is generating back-EMF. Increase parameter F010 (Deceleration Time 1) to 5-10 seconds or install a brake resistor.<br><strong>No:</strong> Check input line voltage and DC bus capacitors. Measure line voltage at drive input terminals and verify it is within rated range.</div>
</details>

<details class="dtree"><summary>Is input line voltage above 480V (for a 400V-class drive)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Excessive supply voltage is the cause. Install a line reactor or step-down transformer, or correct the supply voltage issue at the panel.<br><strong>No:</strong> Check for brake resistor presence and sizing. Consult the GA800 manual for required brake resistor wattage and resistance for your motor size.</div>
</details>

<details class="dtree"><summary>Does the drive have a brake resistor installed and connected to terminals B1-B2?</summary>
<div class="dtree-body"><strong>Yes:</strong> Verify brake resistor is not open or damaged by measuring resistance (typically 20-100 ohms depending on drive size). Replace if open.<br><strong>No:</strong> Install a brake resistor if the application involves frequent deceleration, high-inertia loads, or regenerative braking.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Reset the fault** by pressing the Stop/Reset button or cycling drive power, then monitor for recurrence during normal operation.
2. **Measure input voltage** at the drive's L1, L2, L3 terminals with a multimeter and verify it is within the rated range (typically 380-460V for 400V-class drives).
3. **Check parameter F010** (Deceleration Time 1) in the drive menu. If set below 3 seconds, increase it to 5-10 seconds to reduce back-EMF during stopping.
4. **Inspect brake resistor** if installed. Verify the resistor is connected to terminals B1 and B2, measure its resistance with a multimeter, and check for physical damage or discoloration.
5. **Calculate brake resistor requirements** using the GA800 manual's brake resistor selection table if no resistor is present and the application involves frequent stopping or high inertia.
6. **Test DC bus capacitors** by measuring DC bus voltage ripple during operation (requires oscilloscope). Excessive ripple (above 10% of nominal) indicates capacitor failure.
7. **Replace faulty components** such as the brake resistor, DC link capacitors, or control board only after confirming failure through measurement and diagnostic testing.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa brake resistor for GA800 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f030-fault-code&k=Yaskawa+brake+resistor+for+GA800&tag=errorcodefixes-20) \| Select wattage and resistance using the drive manual's brake resistor selection table based on motor horsepower and deceleration time. |
| DC bus electrolytic capacitors | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f030-fault-code&k=DC+bus+electrolytic+capacitors&tag=errorcodefixes-20) \| Original equipment capacitors from Yaskawa or equivalent industrial-grade capacitors rated for 450VDC minimum and 105°C. |

## When to Call a Pro

Call a qualified drives technician or industrial electrician if you are not trained in VFD programming and high-voltage DC systems. Work inside the GA800 involves DC bus voltages above 600V that remain present for several minutes after power-off. A professional can safely measure DC bus voltage, test capacitors with proper discharge procedures, program deceleration parameters, and size and install brake resistors according to the application's regenerative energy requirements. If the fault persists after adjusting parameters and adding a brake resistor, the drive may have failed power electronics or control circuitry that requires factory-trained repair.

**Rough cost:** A pro service call runs about $200-500 for service call and parameter adjustment or brake resistor installation.
