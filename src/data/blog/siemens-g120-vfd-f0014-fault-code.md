---
title: "Siemens G120 VFD F0014 - Causes & Fix"
description: "F0014 on a Siemens G120 VFD signals a motor overload or thermal overload condition. Check motor load, temperature sensor, and parameter settings."
pubDatetime: 2026-07-19T07:33:50Z
modDatetime: 2026-07-19T07:33:50Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - siemens
money_part: "Motor temperature sensor (PTC or KTY thermistor)"
most_likely_cause: "motor mechanical overload or blockage"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify the motor shaft turns freely by hand with power off and no unusual resistance or binding"
  - "Reset the drive and monitor if the fault returns immediately or only under load"
  - "Check the drive display for actual motor current compared to nameplate rating"
---

## Siemens G120 VFD F0014 — What It Means

The F0014 fault code on a Siemens G120 variable frequency drive indicates that the drive has detected an overload condition, typically related to motor thermal protection. The drive monitors motor current and temperature to protect the motor from damage due to excessive heat or prolonged overload. When the calculated thermal load exceeds the programmed threshold, the drive trips and displays F0014. This fault can be triggered by actual motor overload, incorrect parameter configuration, or a faulty temperature sensor if one is installed.

## Before You Replace Anything

Technicians sometimes replace the drive control board when F0014 appears, but the fault is usually caused by motor or load issues. Always check the motor freely turns and measure actual motor current under load before replacing any drive components.

[Jump to Fix](#fix)

## Common Causes

- **Motor mechanical overload (~40%)** The driven load has increased beyond the motor's rated capacity due to a jammed conveyor, seized bearing, or other mechanical fault that draws excessive current.
- **Incorrect motor parameters (~25%)** The drive's motor nameplate parameters (rated current, power, or thermal time constant) are set incorrectly, causing the drive to calculate false overload conditions.
- **Inadequate motor cooling (~15%)** The motor cooling fan has failed or airflow is blocked, causing the motor to overheat even at normal loads and triggering thermal protection.
- **Faulty temperature sensor (~10%)** If a motor temperature sensor (PTC or KTY) is installed and connected to the drive, a sensor fault or open circuit can falsely trigger the thermal overload alarm.
- **Drive output phase loss (~7%)** A loose connection or failed output contactor causes single-phase operation at the motor, which drastically increases current in the remaining phases and triggers overload protection.
- **Ambient temperature too high (~3%)** The motor or drive is operating in an environment that exceeds the rated ambient temperature, reducing thermal capacity and causing premature overload trips.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the motor shaft turn freely by hand with power off and no unusual resistance?</summary>
<div class="dtree-body"><strong>Yes:</strong> The mechanical load is likely normal. Check drive parameters and motor current readings.<br><strong>No:</strong> The load is mechanically bound or jammed. Inspect the driven equipment for seized bearings, blockages, or alignment problems before restarting.</div>
</details>

<details class="dtree"><summary>Does the fault occur immediately on startup or only after the motor runs for several minutes?</summary>
<div class="dtree-body"><strong>Yes:</strong> Immediate faults suggest a parameter mismatch or severe overload. Verify motor nameplate settings in the drive.<br><strong>No:</strong> Delayed faults point to thermal buildup. Check motor cooling fans, ventilation, and temperature sensor wiring if installed.</div>
</details>

<details class="dtree"><summary>Is the actual motor current (displayed on the drive) near or above the motor nameplate rating?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor is drawing excessive current due to mechanical load or supply issues. Reduce load or investigate motor condition.<br><strong>No:</strong> Current is normal but the fault still trips, indicating a parameter error or sensor fault. Review thermal overload settings and sensor connections.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive** and lock out the main disconnect, then verify zero voltage at the motor terminals with a multimeter.
2. **Inspect the motor and driven load** by rotating the motor shaft by hand to confirm it turns smoothly without binding, grinding, or unusual resistance.
3. **Check all motor and drive connections** at the drive output terminals and motor junction box for loose wires, burned contacts, or signs of overheating.
4. **Access the drive parameter menu** and verify that motor nameplate data (rated voltage, current, power, and frequency) match the actual motor nameplate and are entered correctly.
5. **Review the thermal overload parameters** (typically found in the motor protection function group) and confirm the thermal time constant and overload trip class are appropriate for the motor and application.
6. **Test the motor temperature sensor** (if installed) by measuring resistance at the drive terminals and comparing to the sensor type specification, or temporarily disconnect it to rule out sensor faults.
7. **Clear the fault** from the drive and restart under no-load or light-load conditions while monitoring motor current on the drive display to confirm it stays within rated limits.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor temperature sensor (PTC or KTY thermistor) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f0014-fault-code&k=Motor+temperature+sensor+%28PTC+or+KTY+thermistor%29&tag=errorcodefixes-20) \| Only if the existing sensor is confirmed faulty by resistance test or open circuit. |
| Motor cooling fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f0014-fault-code&k=Motor+cooling+fan&tag=errorcodefixes-20) \| Required if the motor has a separate cooling fan that has failed and caused thermal overload. |

## When to Call a Pro

Call a qualified electrician or drive technician if you are not familiar with VFD programming and parameter setup, as incorrect settings can damage the motor or create unsafe conditions. Professional help is necessary if the fault persists after verifying mechanical load and parameters, if motor current measurements are required under load, or if you need to perform insulation resistance testing on the motor windings. High-voltage work on three-phase industrial equipment requires proper training, PPE, and lockout-tagout procedures.

**Rough cost:** A pro service call runs about $200-600.

## See Also

- [Siemens G120 F01659 - Causes & Fix](/posts/siemens-g120-f01659-fault-code/)
- [Siemens Sinumerik Alarm 300204 — Causes & Fix](/posts/siemens-sinumerik-alarm-300204/)
- [Siemens Micromaster F0011 - Causes & Fix](/posts/siemens-micromaster-vfd-f0011-fault-code/)
- [Siemens Micromaster F0070 - Causes & Fix](/posts/siemens-micromaster-f0070-fault-code/)
