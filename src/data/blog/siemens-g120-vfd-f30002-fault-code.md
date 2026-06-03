---
title: "Siemens G120 F30002 - DC Link Overvoltage Causes & Fix"
description: "F30002 means DC link overvoltage on your Siemens G120 VFD. Most often caused by regenerative braking without a working braking resistor."
pubDatetime: 2026-06-01T11:34:38Z
modDatetime: 2026-06-01T11:34:38Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - siemens
---

## Siemens G120 F30002 — What It Means

The F30002 fault on a Siemens SINAMICS G120 indicates that the drive detected DC link overvoltage. The intermediate-circuit voltage exceeded the safe limit, and the power unit shut down to protect its electronics. This is a power-unit protection fault, not a generic alarm.

In practical terms, energy has built up on the DC bus faster than the drive can handle. This typically happens when the motor acts as a generator during deceleration or braking, feeding power back into the drive, or when the incoming supply voltage spikes above the drive's rating. The drive cannot absorb or dissipate the excess energy, so it trips.

[Jump to Fix](#fix)

## Common Causes

- **Regenerative braking without proper dissipation** The motor decelerates quickly or is driven by the load, generating energy that the drive cannot handle without a braking resistor or module.
- **Braking resistor failure or incorrect connection** The braking resistor is missing, open circuit, undersized, or wired incorrectly, so regenerated energy cannot be burned off.
- **Incoming line overvoltage or supply disturbance** The mains supply voltage is above the drive's rated range or experiences transients that push the DC link voltage too high.
- **Aggressive deceleration ramp settings** The drive is programmed to stop too quickly for the application, creating excessive regenerative power during every stop cycle.
- **Load driving the motor as a generator** An overhauling load (such as a descending conveyor or high-inertia flywheel) constantly forces energy back into the drive.
- **Faulty DC link capacitors or power module** Internal power-section components have degraded and cannot buffer or regulate voltage correctly, leading to repeated overvoltage trips.

## Step-by-Step Fix {#fix}

1. **Stop the drive and clear the fault**, then verify that the fault log confirms F30002 before restarting or troubleshooting further.
2. **Inspect the braking resistor and wiring** for burn marks, loose connections, open circuits, or physical damage. Use a multimeter to measure the resistor's resistance and compare it to the specification for your power module.
3. **Check the incoming supply voltage** with a true-RMS meter during normal operation and during the fault condition to confirm the line voltage is within the drive's rated range and not spiking.
4. **Review deceleration and braking parameters** in the drive's parameter list. Look for ramp-down times that are too short, excessive braking demand, or settings that do not match the mechanical inertia of the load.
5. **Use the drive's diagnostic tools** to monitor DC link voltage in real time while running the machine. Watch for voltage spikes during deceleration, coasting, or when the load drives the motor.
6. **Correct the root cause**: extend deceleration ramps to reduce regenerative energy, install or upgrade the braking resistor and chopper module, stabilize the incoming supply, or adjust parameters to match the application.
7. **Test the drive under load** after repairs, running several complete start-stop cycles, and confirm the DC link voltage remains stable without tripping F30002.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Braking resistor for Siemens G120 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f30002-fault-code&k=Braking+resistor+for+Siemens+G120&tag=errorcodefixes-20) \| Match resistance and power rating to your specific power module. Consult Siemens tables for correct sizing based on deceleration duty. |
| Braking chopper module (if not integrated) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f30002-fault-code&k=Braking+chopper+module+%28if+not+integrated%29&tag=errorcodefixes-20) \| Required if your G120 power module does not have a built-in braking circuit and you need dynamic braking capability. |
| G120 power module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f30002-fault-code&k=G120+power+module&tag=errorcodefixes-20) \| Replace only if internal DC link components or power section is damaged and the fault persists after fixing external causes. |
| Line reactor or input choke | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f30002-fault-code&k=Line+reactor+or+input+choke&tag=errorcodefixes-20) \| Install if the supply is noisy or voltage transients are present. Helps buffer the DC link from line-side disturbances. |

## When to Call a Pro

Call a qualified drives technician or Siemens-authorized service provider if you are not familiar with high-voltage DC circuits, if the fault returns after you have verified and corrected braking components and parameters, or if you need help sizing braking resistors or performing parameter optimization. Also call a professional if the incoming supply voltage is unstable and requires power-quality analysis or if the power module itself is suspected to be damaged. Working inside a VFD enclosure involves lethal voltages, and incorrect braking-circuit installation can cause fire or component destruction.
