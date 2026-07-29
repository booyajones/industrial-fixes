---
title: "Lennox G60UHV Furnace Error Codes — Flash Code Diagnostic Guide"
description: "Complete guide to Lennox G60UHV variable-speed furnace error codes, flash sequences, fault causes, and step-by-step repairs for the most common failures."
pubDatetime: 2026-04-22T22:00:00Z
modDatetime: 2026-04-22T22:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - lennox
  - furnace
money_part: "SureLight ignitor"
---

## Lennox G60UHV Furnace Error Codes — What They Mean

The Lennox G60UHV is a variable-speed, 80% AFUE gas furnace that uses an ECM blower motor for quiet, efficient operation. It reports faults through a flashing LED on the control board (SureLight integrated furnace control). The LED flashes a code number, pauses, then repeats. The G60UHV also supports Lennox iComfort and Harmony III communicating thermostat systems, which can display readable fault descriptions.

## Lennox G60UHV Flash Code Reference

| Flash Code | Meaning |
|------------|---------|
| 1 flash | Normal — call for heat satisfied |
| 2 flashes | Inducer motor not at speed |
| 3 flashes | Pressure switch stuck open |
| 4 flashes | High-limit switch open |
| 5 flashes | Flame sensed — no call for heat |
| 6 flashes | AC power fault (115V) |
| 7 flashes | Gas valve circuit fault |
| 8 flashes | Ignition lockout (failed to prove flame) |
| 9 flashes | Rollout limit switch open |
| 10 flashes | Pressure switch stuck closed |
| 11 flashes | Blower motor fault |
| 12 flashes | Limit device fault (repeated trips) |
| 13 flashes | Control board failure |

## Common Causes by Code

- **Code 2 — Inducer not at speed** — Unique to the G60UHV, the control board monitors inducer RPM via a Hall-effect sensor. If the inducer motor bearing is worn, the motor may start but not reach full speed. Also check for a dirty inducer wheel clogged with lint.
- **Code 3 — Pressure switch open** — The G60UHV uses two pressure switches in some configurations (for two-stage operation). Check both hoses and both switch contacts. A plugged condensate trap inside the unit is a common culprit.
- **Code 4 — High limit** — ECM blower failure is a major cause on the G60UHV. The ECM module is mounted to the rear of the motor — when the module fails, the motor runs at reduced speed or not at all, causing limit trips.
- **Code 8 — Ignition lockout** — SureLight ignitor (Norton/Saint-Gobain) is Lennox-specific. Do not substitute with generic ignitors — the resistance and wattage must match exactly.
- **Code 9 — Rollout limit** — Rollout switches are manually resetting. On the G60UHV, the rollout switches are located on the burner manifold brackets. Manual reset required after trip; do not reset without inspecting for crack in primary heat exchanger.
- **Code 11 — Blower motor fault** — ECM module fault or communication error between control board and motor. Try power-cycling the furnace (off 60 seconds) before replacing the motor.

## Step-by-Step Fix {#fix}

1. **Read the code** — The G60UHV LED is on the lower control board. Open the lower door and note flash count.
2. **For Code 2** — Listen to the inducer motor during startup. It should reach full speed in 15–20 seconds. If it spins slowly or makes noise, check the inducer wheel for debris and confirm the capacitor (if present) is functional.
3. **For Code 3** — Check the condensate trap — it's integrated into the cabinet on the G60UHV. Remove and flush with water. Check both pressure switch hoses (if two-stage model) for kinks or cracks.
4. **For Code 4 and 12** — Replace the filter. Measure duct static pressure; anything over 0.8" W.C. is too high for the G60UHV. Verify ECM blower speed by confirming full airflow at all registers.
5. **For Code 8** — Confirm SureLight ignitor is glowing during the ignition trial. If no glow, check ignitor resistance (40–90 ohms). If glowing but no flame, check gas valve coil continuity and inlet gas pressure.
6. **For Code 11** — Power cycle the furnace completely. If blower doesn't run on the next cycle, check the ECM communication connection between the control board and motor. The 5-wire communications plug is a common failure point on early G60UHV units.

## Parts Often Needed

| Part | Notes |
|------|-------|
| SureLight ignitor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lennox-g60uhv-error-codes&k=SureLight+ignitor&tag=errorcodefixes-20) \| Lennox-specific; use OEM part number |
| Condensate trap | [View on Amazon](https://www.amazon.com/dp/B077J4Y763?ascsubtag=ecf-lennox-g60uhv-error-codes&tag=errorcodefixes-20) \| Integrated into G60UHV cabinet; replace if cracked |
| ECM blower module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lennox-g60uhv-error-codes&k=ECM+blower+module&tag=errorcodefixes-20) \| Mounts to rear of motor; test before replacing motor |
| Pressure switch | [View on Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-lennox-g60uhv-error-codes&tag=errorcodefixes-20) \| Confirm correct rating for single or two-stage |
| Inducer motor | [View on Amazon](https://www.amazon.com/dp/B00FDZ90B2?ascsubtag=ecf-lennox-g60uhv-error-codes&tag=errorcodefixes-20) \| Replace bearing or full motor assembly |
| Control board | [Amazon](https://www.amazon.com/s?k=Control+board&tag=errorcodefixes-20) \| For Code 13 or communication errors |
## When to Call a Pro

The G60UHV's ECM motor requires specialized diagnosis. Lennox sells a motor tester tool (L0409MOTORTOOL) used by authorized dealers to identify whether the fault is in the motor, module, or control board. If you're seeing Code 11 or 13 without an obvious cause, an authorized Lennox dealer can connect diagnostic tools for a definitive diagnosis.
