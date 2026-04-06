---
title: "Allen-Bradley PowerFlex VFD Fault F7 — Motor Stalled Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-03-15T08:00:00Z
modDatetime: 2024-03-15T08:00:00Z
slug: allen-bradley-powerflex-fault-7-motor-stalled
featured: false
draft: false
tags:
  - electrical
  - vfd
  - allen-bradley
  - powerflex
description: "Allen-Bradley PowerFlex VFD Fault F7 means motor stalled — here's how to diagnose and fix it on PowerFlex 4, 40, and 400 series drives."
---

## Error Code: Allen-Bradley PowerFlex Fault F7

**What it means:** Fault F7 (Motor Stalled) on Allen-Bradley PowerFlex 4, 40, and 400 series variable frequency drives indicates that the drive applied output voltage but detected no motor rotation or detected that motor current exceeded the stall current threshold for longer than the programmed stall timeout. The drive shuts down to protect both itself and the motor from thermal damage caused by locked-rotor current.

PowerFlex drives are among the most common VFDs in industrial applications — conveyors, pumps, fans, compressors, mixers — so F7 appears on a wide range of equipment. The fault must be manually cleared (or auto-restarted if configured) after addressing the root cause.

## Common Causes

- **Mechanical binding or seized load** — The driven equipment (conveyor, pump, fan, gearbox) has jammed, seized, or is overloaded beyond the motor's torque capability. This is the most common cause.
- **Acceleration ramp too short** — The programmed acceleration time (parameter P041 on PowerFlex 4, Parameter 140 on PowerFlex 40) is too aggressive for the connected load's inertia. The drive pushes too much frequency too fast, the motor can't keep up, and current spikes to the stall threshold.
- **Motor overloaded** — The process load has increased beyond the motor's rated capacity. Common after conveyor belt loading changes, pump discharge pressure increases, or fan damper modification.
- **Stall timeout parameter too sensitive** — Parameters P036 (Motor Stall Enable) and P037 (Motor Stall Fault Time) on the PowerFlex 4 may be set too aggressively for the application's startup profile.
- **Motor winding fault** — An internal winding fault causes one phase to draw disproportionately high current, tripping the stall detection logic.
- **Drive output phase loss** — A broken wire or blown fuse between the drive output and motor terminal box causes single-phase operation, which produces high current and triggers F7.

## Step-by-Step Fix {#step-by-step-fix}

1. **Do NOT repeatedly reset and re-run without investigation.** Repeated forced restarts into a stall condition will thermally damage the motor windings. Identify the root cause before clearing the fault.

2. **Attempt to rotate the load shaft manually.** Lock out/tag out the drive and the motor. Try to rotate the driven equipment by hand. A conveyor, pump impeller, or fan that won't rotate freely has a mechanical problem — jammed product, seized bearing, broken coupling, or locked brake. Fix the mechanical issue before proceeding.

3. **Verify the load is within the motor's torque rating.** Check whether the process load has changed since the drive was commissioned (heavier product, higher back-pressure, denser medium). If the load has increased, you may need a larger motor/drive combination or a gearbox ratio change.

4. **Check the acceleration time parameter.** On PowerFlex 4: navigate to Parameter Group P041 (Accel Time 1). On PowerFlex 40: Parameter 140. On PowerFlex 400: Parameter 140. Increase the acceleration time by 25–50% and test. High-inertia loads (large fans, centrifuges, loaded conveyors) often need 10–30 seconds of ramp time to avoid stall conditions.

5. **Verify motor wiring at the drive output terminals and motor terminal box.** With LOTO in place, inspect T1/T2/T3 output terminals on the drive for loose connections or corrosion. At the motor terminal box, confirm all three phase leads are terminated correctly and none have pulled out. Use a clamp meter to verify balanced three-phase current during a brief run attempt if wiring is visually good.

6. **Measure motor winding resistance.** Disconnect the motor leads from the drive. Using a multimeter, measure resistance between T1-T2, T2-T3, and T1-T3. Readings should be equal (within 2% of each other) and match the expected resistance for the motor's winding type. Unbalanced or open readings indicate a winding fault.

7. **Review fault parameters and adjust stall protection if load is verified good.** On PowerFlex 4: Parameter P036 (Motor Stall Enable) and P037 (Motor Stall Fault Time). Increasing the stall time slightly can prevent nuisance trips on loads with legitimate slow acceleration profiles. Do not disable stall protection entirely.

8. **Clear the fault and test.** On PowerFlex 4/40/400: press the Stop/Reset button once to clear F7 after addressing the root cause. If the drive is configured for auto-restart (Parameter P040 on PowerFlex 4), confirm the restart delay is adequate. Monitor motor current during the next start with a clamp meter.

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Part Number | Typical Cost | Where to Buy |
|------|------------|-------------|-------------|
| Replacement PowerFlex 4 Drive (if damaged) | 22A-D2P3N104 (varies by HP) | $350–$900 | Automation Direct / Rockwell dealer |
| Motor Coupling (if sheared) | Application-specific | $20–$150 | Grainger / McMaster-Carr |
| Replacement Motor Bearings | Match motor frame size | $15–$80 | Grainger / bearing supply |

## When to Call a Professional

If mechanical checks, wiring verification, and parameter adjustments don't resolve F7, have a qualified electrician or drive technician perform a full motor insulation resistance test (megger test) and verify the drive output with an oscilloscope or power quality analyzer. A drive producing an asymmetrical output waveform due to a failed IGBT can cause F7 even with a healthy motor. IGBT module replacement requires component-level drive repair skills. Also note: Allen-Bradley PowerFlex drives require authorized access to certain parameter groups — if your drive's parameter access level is set to "Basic," you may not be able to see or modify the stall parameters without entering the drive's configuration password.

> **Pro tip:** On conveyor applications, F7 faults that happen every Monday morning but never mid-week are usually caused by cold-temperature grease in gearboxes or bearings making the load stiffer than normal at startup. Increasing the acceleration ramp time for cold-start conditions — or using a timer to run the conveyor briefly unloaded before full production — eliminates this class of F7 entirely.
