---
title: "Trane XV80 Furnace Error Codes — Flash Code Diagnostic Guide"
description: "Complete guide to Trane XV80 furnace error codes, flash sequences, common fault causes, and step-by-step repairs for pressure switch, ignition, and limit faults."
pubDatetime: 2026-04-22T22:00:00Z
modDatetime: 2026-04-22T22:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - trane
  - furnace
---

## Trane XV80 Furnace Error Codes — What They Mean

The Trane XV80 is an 80% AFUE, variable-speed gas furnace using an ECM blower motor for precise airflow control. It communicates faults through a diagnostic LED on the integrated furnace control (IFC) board. Flash codes appear as a pattern of rapid blinks — the number of blinks before a pause identifies the fault condition.

[Jump to Fix](#fix)

## Trane XV80 Flash Code Reference

| Flash Code | Meaning |
|------------|---------|
| 1 flash | Normal operation — call satisfied |
| 2 flashes | System lockout (exceeded retry count) |
| 3 flashes | Pressure switch open — inducer or draft issue |
| 4 flashes | Open high-limit device |
| 5 flashes | Flame sensed — gas valve not energized |
| 6 flashes | 115V wiring fault or reversed polarity |
| 7 flashes | Gas valve circuit problem |
| 8 flashes | Low flame signal — dirty flame sensor |
| 9 flashes | Rollout switch open |
| 13 flashes | Limit cycle lockout — excessive trips |
| 14 flashes | Ignition lockout — failed 3 consecutive attempts |
| 34 flashes | Ignition proving failed |

## Common Causes by Code

- **Code 3 — Pressure switch** — The XV80 is an 80% unit so it uses a metal flue pipe rather than PVC condensate drain. On the XV80, pressure switch faults often trace to a restricted vent pipe (birds' nests, ice blockage at the exterior termination), a cracked inducer housing gasket, or a failed pressure switch. Check the exterior flue cap in winter — ice buildup is a common field problem.
- **Code 4 — High limit** — Dirty air filter, blocked return, failed ECM blower module. The XV80's variable-speed ECM can develop a failed capacitor or module, reducing airflow to levels that trip the limit even with a clean filter.
- **Code 8 — Weak flame signal** — Flame sensor is mounted in the burner compartment. Normal µA reading is 1.5–5.0. Below 1.0 µA causes nuisance lockouts. Clean the sensor rod; check for a cracked ceramic insulator that causes the rod to ground intermittently.
- **Code 9 — Rollout switch** — Rollout trips on the XV80 are serious. Causes include cracked heat exchanger, gas valve sticking open, or blocked burner orifices. Do not simply reset the rollout and restart without inspection.
- **Code 13 — Limit cycle lockout** — More than three limit trips in one hour triggers lockout. Often caused by the ECM blower running below its commanded speed — check the blower motor's tap selection on the control board.
- **Code 14 — Ignition lockout** — No flame proven in three ignition trials. Check the ignitor (silicon nitride, 120V), the gas valve, and incoming gas pressure.

## Step-by-Step Fix {#fix}

1. **Read the code** — Open the lower access panel and observe the LED. Record the flash sequence before resetting.
2. **For Code 3** — Inspect the exterior flue termination for obstruction. Check pressure switch tubing for cracks or disconnection. Confirm inducer turns on and reaches full speed within 30 seconds of a call for heat.
3. **For Code 4 / 13** — Replace the filter. Check all registers for obstruction. Measure the blower speed by listening for proper airflow; if the blower sounds weak, use a blower door test or anemometer.
4. **For Code 8** — Remove the flame sensor (1/4-inch hex screw), clean with fine emery cloth, reinstall, and measure µA through a multimeter in series with the sensor wire.
5. **For Code 9** — Locate the rollout switches on the burner box. Check continuity. If tripped (open), investigate cause fully — look at the heat exchanger for cracks via flashlight and mirror before resetting.
6. **For Code 14** — Watch the ignitor during startup: it should glow orange-white at 90 seconds. If it glows but flame doesn't ignite, gas supply or valve is the issue. If no glow, ignitor circuit or board is the issue.
7. **Reset** — Cycle the disconnect or breaker to clear a lockout. For Code 13, the lockout clears after one hour with power on.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Flame sensor | [Amazon](https://www.amazon.com/s?k=Flame+sensor&tag=errorcodefixes-20) \| Common; cost ~$15–25 |
| Hot surface ignitor | [Amazon](https://www.amazon.com/s?k=Hot+surface+ignitor&tag=errorcodefixes-20) \| Silicon nitride, 120V; confirm part for XV80 |
| ECM blower module | [Amazon](https://www.amazon.com/s?k=ECM+blower+module&tag=errorcodefixes-20) \| Fits behind the motor; test before replacing motor |
| Pressure switch | [Amazon](https://www.amazon.com/s?k=Pressure+switch&tag=errorcodefixes-20) \| Match to inducer model and tubing port |
| Rollout switch | [Amazon](https://www.amazon.com/s?k=Rollout+switch&tag=errorcodefixes-20) \| Investigate cause before replacing |
| Control board (IFC) | [Amazon](https://www.amazon.com/s?k=Control+board+%28IFC%29&tag=errorcodefixes-20) \| For repeated unexplained lockouts |
## When to Call a Pro

A cracked heat exchanger in the XV80 is a carbon monoxide hazard. If the rollout switch has tripped, do not operate the furnace until a licensed technician inspects the heat exchanger. ECM motor troubleshooting also benefits from Trane's proprietary diagnostic tools available to authorized dealers.

## Related Articles

- [Trane 1 Flash Error Code — Causes & Fix](/posts/trane-1-flash-error-code/)
- [Trane Error Code 126 — Ignition Lockout Fix](/posts/trane-126-error-code/)
- [Trane 2 Flashes Error Code — Causes & Fix](/posts/trane-2-flashes-error-code/)
- [Trane 3 Flashes Error Code — Pressure Switch Fault Fix](/posts/trane-3-flashes-error-code/)
- [Trane 3 Flash Pressure Switch Fault — Detailed Diagnosis Guide](/posts/trane-3-flashes-pressure-switch/)
