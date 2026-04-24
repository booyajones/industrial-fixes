---
title: "Fujitsu Mini Split E3 Error Code — Causes & Fix"
description: "What Fujitsu mini split E3 error code means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T09:00:00Z
modDatetime: 2026-04-22T09:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - fujitsu
---

## Fujitsu Mini Split E3 Error Code — What It Means

Fujitsu mini split error code E3 indicates a fan motor fault on the indoor unit. The indoor unit's fan motor has either failed to start, stalled, or the control board detected an abnormal fan speed signal from the Hall effect sensor integrated into the motor. Fujitsu uses DC brushless fan motors on most current models, and these motors report speed feedback directly to the PCB. When the reported speed is zero or outside the expected range, the system shuts down to prevent operating without indoor airflow — which would cause the evaporator coil to ice over.

[Jump to Fix](#fix)

## Common Causes

- **Failed indoor fan motor (DC brushless)** — The motor winding, driver integrated circuit, or Hall sensor fails. The motor may hum without turning, run at reduced speed, or be completely dead.
- **Obstructed fan wheel** — Ice, debris, or a foreign object jammed in the fan wheel prevents rotation. The motor runs at high current and the board sees zero speed feedback.
- **Loose or damaged motor wiring connector** — The connector between the PCB and the fan motor can work loose over time, particularly on units that vibrate or where the harness routing pulls on the connector.
- **Failed indoor PCB fan driver circuit** — The PCB's motor driver output fails, sending incorrect PWM signals to the motor. This is distinguishable from motor failure by substituting the motor.

## Step-by-Step Fix {#fix}

1. **Inspect the fan wheel for obstructions** — Remove the indoor unit's front panel and filter cover. Manually rotate the fan wheel (cylindrical fan, also called a squirrel cage or cross-flow fan). It should spin freely without binding or grinding.
2. **Check the motor connector at the PCB** — Shut off the unit and remove the access panel. Locate the fan motor connector on the indoor PCB. Inspect for bent pins, corrosion, or loose seating. Reseat firmly.
3. **Test motor windings** — With the connector unplugged, test resistance across the motor winding leads per the service manual schematic. An open circuit indicates a failed winding. Check the Hall sensor leads separately if specified in the manual.
4. **Verify PCB fan output voltage** — With the unit energized and calling for operation, measure the voltage on the motor drive output from the PCB. No voltage when the unit should be running indicates a PCB driver fault rather than a motor fault.
5. **Replace fan motor and reset** — Install the correct replacement motor (match motor model number exactly — CFM, voltage, and connector pinout vary). Restore power and confirm E3 clears.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Indoor DC fan motor | [Amazon](https://www.amazon.com/s?k=Indoor+DC+fan+motor&tag=errorcodefixes-20) \| Fujitsu uses several motor variants; order by indoor unit model number |
| Fan wheel (cross-flow fan) | [Amazon](https://www.amazon.com/s?k=Fan+wheel+%28cross-flow+fan%29&tag=errorcodefixes-20) \| Replace if blades are cracked, warped, or contaminated with heavy debris |
| Indoor PCB | [Amazon](https://www.amazon.com/s?k=Indoor+PCB&tag=errorcodefixes-20) \| Replace only if motor driver output is confirmed dead |
## When to Call a Pro

On multi-zone systems with combined indoor/outdoor PCBs, E3 diagnosis may require Fujitsu service software to isolate the specific zone. If the fan motor replacement doesn't clear the fault, a Fujitsu-authorized technician with diagnostic tools can read live sensor data to confirm the PCB is the cause.
