---
title: "Siemens Micromaster F0002 - Causes & Fix"
description: "F0002 is a DC-link overvoltage trip. Most often caused by too-fast deceleration on high-inertia loads. Increase ramp-down time or check braking."
pubDatetime: 2026-06-01T11:42:01Z
modDatetime: 2026-06-01T11:42:01Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Braking resistor"
most_likely_cause: "Deceleration ramp too short"
---

## What this code means
F0002 on Siemens MICROMASTER drives (420, 440, and others) means the DC-link voltage exceeded the drive's overvoltage trip threshold. The drive monitors the DC bus voltage (parameter r0026) and trips when it climbs above the level set in P2172. This almost always happens during deceleration or when a high-inertia load or overhauling load drives the motor and pushes regenerated energy back into the drive faster than the drive can dissipate it.

You'll typically see F0002 when stopping or slowing down quickly. The DC link charges up from regenerative braking energy. If your deceleration ramp is too short, your incoming mains voltage is too high, or your braking resistor and chopper are missing or broken, the bus voltage spikes and the drive protects itself by shutting down.

## Common Causes

- **Deceleration ramp too short** High-inertia loads or overhauling applications generate energy faster than the DC link can handle when ramp-down time (P1121) is set too aggressively.
- **Incoming supply voltage too high** Mains voltage outside the drive's permitted range directly raises the DC-link voltage above the trip threshold.
- **DC-link voltage controller disabled or misconfigured** Parameter P1240 (Vdc controller) is not enabled or not tuned correctly to regulate bus voltage during regeneration.
- **Braking resistor or brake chopper not working** The external braking resistor may be open, disconnected, or undersized, or the internal brake chopper transistor may be defective.
- **Overhauling load drives the motor** Applications such as downhill conveyors or lowering hoists continuously feed energy back into the drive even at constant speed.
- **Supply voltage spikes or transients** Lightning strikes, capacitor switching, or other line disturbances can briefly push the DC link over the trip level.

## Step-by-Step Fix {#fix}

1. **Measure the incoming supply voltage** at the drive terminals with the drive off and confirm it is within the voltage range printed on the rating plate.
2. **Monitor DC-link voltage in real time** by viewing parameter r0026 on the keypad while running the drive through a typical start and stop cycle to see when the voltage spikes.
3. **Increase the deceleration ramp-down time** in parameter P1121 to allow the load's kinetic energy to dissipate more slowly and reduce regenerative current into the DC link.
4. **Check and enable the DC-link voltage controller** by setting parameter P1240 according to the parameter manual for your MICROMASTER model so the drive actively regulates bus voltage.
5. **Inspect braking resistor connections and resistance** if a brake resistor is installed, verify all terminals are tight and measure the resistor's ohms to confirm it is not open or damaged.
6. **Test or replace the brake chopper circuit** if the drive has an internal or external chopper, consult the service manual to verify chopper operation or swap the chopper module if accessible.
7. **Reset the fault and re-test under load** by cycling power or pressing the reset button, then run the same deceleration profile that caused the trip to confirm the fix.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Braking resistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-vfd-f0002-fault-code&k=Braking+resistor&tag=errorcodefixes-20) \| Must match the drive's voltage class and power rating. Consult the MICROMASTER selection guide for correct ohms and wattage. |
| Brake chopper module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-vfd-f0002-fault-code&k=Brake+chopper+module&tag=errorcodefixes-20) \| Internal or external unit depending on drive model. Verify part number in the drive's manual before ordering. |
| Input line reactor or filter | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-vfd-f0002-fault-code&k=Input+line+reactor+or+filter&tag=errorcodefixes-20) \| Can help dampen supply voltage spikes if the mains are noisy or if transient overvoltages are suspected. |

## When to Call a Pro

Call a qualified drive technician or Siemens service partner if you are not familiar with high-voltage DC bus work, if the fault persists after lengthening ramp times and verifying supply voltage, or if you suspect internal damage to the brake chopper or DC-link capacitors. Measuring live DC-link voltage and working inside the drive cabinet requires lockout/tagout and appropriate PPE. If your application involves continuous regeneration (downhill conveyors, hoists, centrifuges), a professional can size and install an external braking resistor or configure advanced Vdc control parameters to prevent repeated trips.
