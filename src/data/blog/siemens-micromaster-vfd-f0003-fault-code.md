---
title: "Siemens Micromaster F0003 - Causes & Fix"
description: "F0003 means undervoltage: the DC link voltage dropped below the safe limit. Most often fixed by checking incoming power supply."
pubDatetime: 2026-06-01T11:42:35Z
modDatetime: 2026-06-01T11:42:35Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Input line fuses"
most_likely_cause: "Incoming supply loss or sag"
---

## Siemens Micromaster F0003 — What It Means

F0003 on a Siemens Micromaster drive (MM420, MM440, and similar models) is an undervoltage fault. The drive detected that the DC link voltage or supply voltage fell below the permissible limit and tripped to protect itself. This fault is directly tied to low or unstable line voltage feeding the drive. Siemens documentation lists the main causes as main supply failure or shock load outside specified limits.

[Jump to Fix](#fix)

## Common Causes

- **Incoming supply loss or sag** A phase drop, low utility voltage, or temporary power interruption can cause the DC link to fall below the trip threshold.
- **Loose or corroded line connections** Poor contact on the input terminals, fuses, breakers, or cabling creates intermittent voltage drop under load.
- **Shock load or heavy transient** Abrupt acceleration or a sudden large load step pulls supply voltage down below the drive's allowable limit.
- **Weak upstream supply** Undersized feeders, long cable runs, or instability in the distribution system can cause sustained or repeated undervoltage events.
- **Internal drive power-stage fault** If supply voltage is confirmed stable and in-spec, the drive's own DC link circuit or power section may be damaged.

## Step-by-Step Fix {#fix}

1. **Verify the fault code** on the drive display or in the fault memory (parameter r0947 for MM440) to confirm it is F0003.
2. **Measure incoming line voltage** at the drive input terminals with a true-RMS multimeter and compare to the voltage range on the drive nameplate.
3. **Inspect all line-side connections** including input terminals, fuses, disconnect switches, and breakers for looseness, corrosion, or signs of overheating.
4. **Monitor voltage during operation** with a data logger or scope if the fault is intermittent, watching for dips during motor start or load changes.
5. **Check for shock loads** in the application and reduce abrupt acceleration rates or large load steps if the fault occurs during those events.
6. **Reset the drive** only after correcting the supply issue by power cycling, pressing the Fn key on the operator panel, or using a configured digital input if applicable.
7. **Consult Siemens or a qualified technician** if the supply is verified stable and within spec but the fault persists, as internal DC-link or power-stage repair may be required.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Input line fuses | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-vfd-f0003-fault-code&k=Input+line+fuses&tag=errorcodefixes-20) \| Replace if blown or showing signs of overheating due to loose connections. |
| Input terminals and hardware | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-vfd-f0003-fault-code&k=Input+terminals+and+hardware&tag=errorcodefixes-20) \| Upgrade or replace corroded or damaged terminal blocks and connection hardware. |
| Siemens Micromaster drive unit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-vfd-f0003-fault-code&k=Siemens+Micromaster+drive+unit&tag=errorcodefixes-20) \| Replacement or factory repair if internal DC-link circuitry is confirmed faulty after supply is ruled out. |

## When to Call a Pro

Call a qualified electrician or drive technician if you are not trained to measure three-phase power or work inside energized industrial control panels. If you confirm the incoming supply is stable and within the drive's rated voltage range but the F0003 fault keeps recurring, the drive likely has an internal power-section defect that requires factory repair or replacement. Siemens drive faults should always be investigated by someone familiar with VFD commissioning and the specific parameter structure of the Micromaster series.

## See Also

- [Siemens G120 F0007 Fault Code - Causes & Fix](/posts/siemens-g120-vfd-f0007-fault-code/)
- [Siemens G120 F01034 - Causes & Fix](/posts/siemens-g120-f01034-fault-code/)
- [Siemens Micromaster F0085 - Causes & Fix](/posts/siemens-micromaster-f0085-fault-code/)
- [Siemens SENTRON 3WL/3VA Fault Codes — Troubleshooting Guide](/posts/siemens-sentron-fault-codes/)
