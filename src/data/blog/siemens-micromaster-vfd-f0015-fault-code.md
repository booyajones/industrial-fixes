---
title: "Siemens Micromaster F0015 - Causes & Fix"
description: "F0015 means motor temperature sensor signal lost (open or short circuit). Most often a broken wire or loose connection at the PTC sensor."
pubDatetime: 2026-06-01T11:46:26Z
modDatetime: 2026-06-01T11:46:26Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Motor PTC temperature sensor"
most_likely_cause: "Broken or open circuit in sensor wiring"
---

## Siemens Micromaster F0015 — What It Means

F0015 on a Siemens Micromaster indicates the drive has lost valid motor temperature feedback from the motor sensor circuit. This is categorized as an open or short circuit of the motor temperature sensor. When the fault occurs, the drive automatically switches to its internal motor thermal model for temperature protection and triggers an OFF2 shutdown. The drive expects a believable signal from the motor's PTC or thermistor temperature sensor and will fault when that signal disappears or falls outside normal range.

[Jump to Fix](#fix)

## Common Causes

- **Broken or open circuit in sensor wiring** Damaged, cut, or broken conductors in the cable between the motor temperature sensor and the drive input.
- **Short circuit in the sensor loop** Shorted wires or terminals in the motor temperature sensor circuit causing the drive to see invalid resistance.
- **Loose or corroded sensor connections** Poor contact at motor junction box terminals, drive input terminals, or intermediate terminal strips.
- **Failed motor temperature sensor** The PTC or thermistor itself has failed open or shorted internally.
- **Moisture or contamination in sensor circuit** Water, oil, or debris in junction boxes or connectors creating erratic sensor readings.
- **Incorrect drive parameterization for sensor type** Drive is configured to expect a motor temperature sensor that is not actually installed or wired.

## Step-by-Step Fix {#fix}

1. **Lock out and tag out the drive** and verify it is safe to work on before touching any wiring.
2. **Identify the motor temperature sensor type** from the motor nameplate or wiring diagram (PTC, thermistor, or other) to know what you are diagnosing.
3. **Inspect all sensor wiring end-to-end** from the motor terminals to drive terminals 14/PTCA and 15/PTCB, checking for loose terminals, broken wires, crushed cable, or moisture in junction boxes.
4. **Disconnect the sensor circuit and measure resistance** across the sensor leads to check for an open circuit (infinite resistance) or short circuit (near-zero resistance) that matches the fault description.
5. **Verify the sensor is installed and correctly wired** for your control scheme, and check that drive parameters match the physical sensor hardware present.
6. **Repair or replace faulty wiring or sensor** based on your resistance measurements and visual inspection, making sure all connections are clean and tight.
7. **Clear the fault and retest the drive** after completing repairs, and if the fault returns with known-good wiring and sensor, inspect the drive's I/O board seating and condition for internal faults.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor PTC temperature sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-vfd-f0015-fault-code&k=Motor+PTC+temperature+sensor&tag=errorcodefixes-20) \| Replacement thermistor or PTC sensor matching your motor manufacturer specs. |
| Shielded sensor cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-vfd-f0015-fault-code&k=Shielded+sensor+cable&tag=errorcodefixes-20) \| Two-conductor cable for motor temperature sensor connections between motor and drive. |
| Siemens Micromaster I/O board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-vfd-f0015-fault-code&k=Siemens+Micromaster+I%2FO+board&tag=errorcodefixes-20) \| Only if sensor circuit tests good and fault persists, indicating internal drive fault. |

## When to Call a Pro

Call a qualified electrician or drive technician if you are not comfortable working with locked-out industrial equipment, if you cannot safely access the motor or drive wiring, or if the fault persists after you have verified good sensor wiring and resistance. Also call a pro if the drive I/O board appears damaged or if you lack the test equipment to measure sensor continuity and resistance accurately. Internal drive faults on the temperature input circuit require specialized diagnostic tools and replacement boards that are best handled by experienced technicians.

## See Also

- [Siemens Sinumerik Alarm 300204 — Causes & Fix](/posts/siemens-sinumerik-alarm-300204/)
- [Siemens Micromaster F0015 - Causes & Fix](/posts/siemens-micromaster-f0015-fault-code/)
- [Siemens Micromaster F0221 - Causes & Fix](/posts/siemens-micromaster-f0221-fault-code/)
- [Siemens Micromaster F0060 - Causes & Fix](/posts/siemens-micromaster-f0060-fault-code/)
