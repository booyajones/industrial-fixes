---
title: "Siemens G120 F0003 - Causes & Fix"
description: "F0003 is an undervoltage fault on Siemens G120 drives. The DC-link voltage dropped too low. Check incoming supply voltage first."
pubDatetime: 2026-06-01T11:35:11Z
modDatetime: 2026-06-01T11:35:11Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Incoming line fuses or fuse holders"
---

## Siemens G120 F0003 — What It Means

F0003 on a Siemens G120 drive means undervoltage. The drive has detected that its supply or DC-link voltage fell below the acceptable threshold and tripped to protect itself. Siemens lists the fault reaction as OFF 2, triggered when the main supply fails or a shock load pulls voltage outside specified limits. The fault code is stored in parameter r0947 as code 3, and the associated error value appears in r0949. The drive will not run until you correct the supply problem and clear the fault.

[Jump to Fix](#fix)

## Common Causes

- **Main supply voltage loss or sag** Incoming power to the drive dropped below the minimum required level, either from utility issues or upstream equipment failure.
- **Input voltage below configured limit** The actual line voltage does not match the supply voltage setting in parameter p0210, causing the drive to fault on undervoltage.
- **Loose or failed line connections** Corroded terminals, loose wiring, or poor contact at the input side can create intermittent voltage drops that trigger the fault.
- **Shock load or abrupt load demand** Sudden acceleration, mechanical binding, or a heavy inrush current pulls the DC bus voltage down faster than the supply can recover.
- **Blown fuse or tripped breaker upstream** A failed fuse, breaker, or contactor in the feeder path interrupts or reduces voltage reaching the drive.
- **Weak or unstable utility supply** Low grid voltage, brownouts, or voltage sag during peak demand can drop the drive supply below the undervoltage threshold.

## Step-by-Step Fix {#fix}

1. **Isolate and lock out power** to the drive and control panel before beginning any inspection or repair work.
2. **Check the incoming line voltage** at the drive input terminals with a multimeter and verify it matches the required supply and the value configured in parameter p0210.
3. **Inspect the supply path** for loose connections, corrosion, overheating, or damage at disconnects, fuses, contactors, breakers, and terminal blocks.
4. **Measure voltage under load** by monitoring at the drive input during motor startup or operation to catch intermittent sags that only appear during acceleration or load changes.
5. **Review the load condition** for mechanical binding, shock loading, or sudden torque demands that could momentarily pull down the DC bus voltage.
6. **Repair or replace failed upstream components** such as loose terminals, blown fuses, tripped breakers, or damaged contactors, and restore proper utility voltage if the grid supply is low.
7. **Reset the fault** after correcting the supply issue by cycling power, pressing the OP button on the control panel, using a digital input, or sending the reset command via control word 1.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Incoming line fuses or fuse holders | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f0003-fault-code&k=Incoming+line+fuses+or+fuse+holders&tag=errorcodefixes-20) \| Replace if blown or showing signs of overheating or corrosion at the terminals. |
| Line contactor or breaker | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f0003-fault-code&k=Line+contactor+or+breaker&tag=errorcodefixes-20) \| Replace if contacts are pitted, coil has failed, or the device trips repeatedly under normal load. |
| Input terminal blocks | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f0003-fault-code&k=Input+terminal+blocks&tag=errorcodefixes-20) \| Replace if cracked, corroded, or mechanically damaged after repeated heating cycles. |

## When to Call a Pro

Call a qualified electrician or drives technician if you cannot locate the source of the undervoltage after checking the incoming supply and upstream components, if the fault recurs even with correct line voltage, or if you suspect internal damage to the drive's rectifier or power section. A professional can perform detailed DC-link measurements, review parameter settings, and test the drive's internal hardware to confirm whether the power module or control board needs replacement.

## See Also

- [Siemens G120 F01040 - Causes & Fix](/posts/siemens-g120-f01040-fault-code/)
- [Siemens Micromaster F0015 - Causes & Fix](/posts/siemens-micromaster-vfd-f0015-fault-code/)
- [Siemens Sinumerik Alarm 300204 — Causes & Fix](/posts/siemens-sinumerik-alarm-300204/)
- [Siemens G120 F0011 Fault Code - Causes & Fix](/posts/siemens-g120-vfd-f0011-fault-code/)
