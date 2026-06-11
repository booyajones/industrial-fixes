---
title: "Siemens Micromaster F0003 - Causes & Fix"
description: "Siemens Micromaster F0003 means undervoltage on the DC link. Learn the real causes, diagnostics, and repair steps technicians use."
pubDatetime: 2026-05-28T09:11:44Z
modDatetime: 2026-05-28T09:11:44Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Input fuses for Siemens Micromaster"
---

## Siemens Micromaster F0003 — What It Means

F0003 on a Siemens Micromaster drive indicates undervoltage on the DC link or main supply side. The drive has detected that the incoming supply voltage has dropped below the allowed threshold and has tripped to protect itself. This is not a motor overload or overcurrent fault. It means the drive is not receiving enough voltage from the mains to operate safely.

[Jump to Fix](#fix)

## Common Causes

- **Incoming mains loss or brownout** A utility outage, voltage sag, or temporary dip in the plant supply is causing the drive to see insufficient voltage.
- **Loose or overheated supply connections** Terminals, lugs, or contactors on the line side are corroded, loose, burned, or making intermittent contact.
- **Voltage dips from other plant loads** Large motors or equipment starting elsewhere in the facility are pulling the supply down temporarily.
- **Single-phasing or lost input leg** One phase of the three-phase supply is missing or weak, causing the DC link to droop below threshold.
- **Supply not within rated range** The incoming voltage does not match the drive rating plate or the limit set in parameter P0210.
- **Undersized wiring or upstream voltage drop** Long cable runs, small wire gauge, or upstream devices like line reactors or filters are causing excessive voltage drop under load.

## Step-by-Step Fix {#fix}

1. Verify incoming voltage at the drive input terminals. Use a multimeter to measure line-to-line voltage on all three phases and confirm it matches the rating plate and expected supply range.
2. Monitor the supply during operation. Observe the voltage while the drive attempts to start and under load to catch any sags, dips, or dropouts that trigger the fault.
3. Inspect all line-side connections. Check disconnects, contactors, fuses, terminal blocks, and lugs for tightness, discoloration, burn marks, or corrosion.
4. Check for single-phasing. Measure each input leg individually and compare voltages to confirm all three phases are present and balanced.
5. Review drive parameters and fault history. Check parameter P0210 for supply voltage limits and read fault records in r0947 or r0949 to see if the fault is repeating or isolated.
6. Isolate the drive from plant power disturbances. If possible, temporarily disconnect other large loads or run the drive from a dedicated clean supply to rule out external voltage issues.
7. Reset the fault after correcting the cause. Power cycle the drive, use the keypad reset function, or activate the configured digital input reset method.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Input fuses for Siemens Micromaster | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-f0003-fault-code&k=Input+fuses+for+Siemens+Micromaster&tag=errorcodefixes-20) \| Replace if blown or showing signs of heat damage or intermittent contact. |
| Line contactor or disconnect switch | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-f0003-fault-code&k=Line+contactor+or+disconnect+switch&tag=errorcodefixes-20) \| Replace if contacts are pitted, burned, or not closing fully on all three poles. |
| Supply wiring, terminals, and lugs | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-f0003-fault-code&k=Supply+wiring%2C+terminals%2C+and+lugs&tag=errorcodefixes-20) \| Replace damaged, undersized, or corroded conductors and hardware on the line side. |
| Line reactor or EMI filter | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-f0003-fault-code&k=Line+reactor+or+EMI+filter&tag=errorcodefixes-20) \| Replace only if installed, found defective by measurement, or confirmed as incorrectly sized for the installation. |

## When to Call a Pro

Call a qualified electrician or drive technician if you cannot safely measure or verify the incoming supply, if the fault persists after checking all line-side connections and supply conditions, or if you suspect internal drive damage to the DC link or power stage. Also call for help if the plant supply shows chronic instability or if the drive documentation and parameter settings are unclear for your specific model and voltage class.
