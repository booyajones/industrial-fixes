---
title: "Trane XR90 Furnace Error Codes — Fault Code Diagnostic Guide"
description: "Complete guide to Trane XR90 furnace error codes, LED flash sequences, common fault causes, and step-by-step repair procedures for HVAC technicians."
pubDatetime: 2026-04-22T23:00:00Z
modDatetime: 2026-04-22T23:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - trane
  - furnace
---

## Trane XR90 Furnace Error Codes — What They Mean

The Trane XR90 is a single-stage 90% AFUE gas furnace with a PSC (permanent split capacitor) blower motor. It is one of Trane's long-running mid-efficiency residential furnaces designed for reliability and straightforward service. The XR90 uses a control board with a status LED that reports fault codes via flash sequences. The board also includes a fault history LED window on some revisions that displays the last five fault codes as sticky memory.

[Jump to Fix](#fix)

## Trane XR90 LED Flash Code Reference

| Flash Sequence | Fault |
|---|---|
| 1 flash | Normal — standby |
| 2 flashes | Pressure switch stuck open |
| 3 flashes | Pressure switch stuck closed |
| 4 flashes | Open limit device |
| 5 flashes | Flame sensed without gas valve call |
| 6 flashes | 115V power reversed — hot and neutral swapped |
| 7 flashes | Gas valve stuck open |
| 8 flashes | Ignition failure — exceeded retry limit |
| 9 flashes | Inducer motor fault |
| Rapid flash | Low voltage — check transformer |
| Continuous | Normal — blower running in cooling or fan mode |

## Common Causes by Code

- **2 flashes — Pressure switch open** — Blocked condensate drain line (the XR90 is a 90% unit with a condensate system), cracked pressure switch tubing, or failed inducer motor not creating sufficient draft. Check the condensate trap for blockage first — this is the most common cause on XR90s over 5 years old.
- **3 flashes — Pressure switch stuck closed** — A pressure switch that closes before the inducer starts indicates a failed switch or a stuck switch from condensate in the switch. Disconnect the tubing from the pressure switch and blow it out.
- **4 flashes — Open limit** — Airflow restriction causing heat exchanger overtemperature. Replace the air filter. Check for closed supply registers or a blocked return air path.
- **5 flashes — Flame without call** — The flame sensor is detecting signal when the gas valve is off. This indicates a shorted or contaminated flame sensor creating a leakage current, or a failed gas valve that isn't fully closing.
- **8 flashes — Ignition failure** — The XR90 uses a hot surface igniter. Confirm gas supply is on, igniter glows red-orange (not dim yellow), and gas valve opens on ignition call (listen for the click of the valve solenoid).
- **9 flashes — Inducer fault** — Inducer motor failed or speed too low. Check inducer capacitor (usually 5–7.5 µF) with a capacitor meter. A seized bearing is the other common cause — spin by hand with power off.

## Step-by-Step Fix {#fix}

1. **Count the LED flashes** — The XR90 LED flashes a code, pauses, then repeats. Count the flashes in one cycle (from pause to pause). The code is the flash count.
2. **For 2 flashes (pressure switch open)** — Check the condensate drain trap. On the XR90, the trap is usually a U-shaped PVC assembly under the secondary heat exchanger. Remove and flush with water. Also check the condensate hose from the secondary heat exchanger to the trap for kinks.
3. **For 4 flashes (limit)** — Replace the filter immediately. If filters were just changed, check for a blocked or partially collapsed return air duct. Measure blower wheel RPM if possible — a failing PSC capacitor drops blower speed and reduces airflow.
4. **For 8 flashes (ignition failure)** — Observe the ignition sequence: inducer starts (verify), igniter heats (glow visible through sight glass), gas valve opens, flame appears. If the flame lights then goes out within 5 seconds, the flame sensor needs cleaning.
5. **For 9 flashes (inducer)** — Measure supply voltage to the inducer motor (115VAC). Check the capacitor. If voltage is present, capacitor is good, and the motor won't spin, the motor windings have failed.

## Parts Often Needed

| Part | Notes |
|---|---|
| Hot surface igniter | [Amazon](https://www.amazon.com/dp/B00BTLLJ40?ascsubtag=ecf-trane-xr90-error-codes&tag=errorcodefixes-20) \| Norton 601, silicon carbide; fragile — don't touch the ceramic |
| Flame sensor | [Amazon](https://www.amazon.com/s?k=Flame+sensor&tag=errorcodefixes-20) \| Rod-type; clean with steel wool before replacing |
| Inducer motor capacitor | [Amazon](https://www.amazon.com/dp/B01M05L7B3?ascsubtag=ecf-trane-xr90-error-codes&tag=errorcodefixes-20) \| 5 or 7.5 µF; measure before replacing motor |
| Pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-trane-xr90-error-codes&tag=errorcodefixes-20) \| Two switches on some XR90 versions (high and low) |
| High-limit switch | [Amazon](https://www.amazon.com/dp/B0BN3TRG9R?ascsubtag=ecf-trane-xr90-error-codes&tag=errorcodefixes-20) \| L200°F on most XR90 configurations |
| Blower capacitor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-trane-xr90-error-codes&k=Blower+capacitor&tag=errorcodefixes-20) \| PSC blower motor; dedicated capacitor |
## When to Call a Pro

The XR90 heat exchanger is a clamshell design that can crack at the secondary (condensate-side) section. If you smell combustion gases in the conditioned air, suspect a cracked heat exchanger — this is a safety issue requiring professional inspection and likely furnace replacement. Do not operate a furnace with a suspected cracked heat exchanger.

## Related Articles

- [Trane 1 Flash Error Code — Causes & Fix](/posts/trane-1-flash-error-code/)
- [Trane Error Code 126 — Ignition Lockout Fix](/posts/trane-126-error-code/)
- [Trane 2 Flashes Error Code — Causes & Fix](/posts/trane-2-flashes-error-code/)
- [Trane 3 Flashes Error Code — Pressure Switch Fault Fix](/posts/trane-3-flashes-error-code/)
- [Trane 3 Flash Pressure Switch Fault — Detailed Diagnosis Guide](/posts/trane-3-flashes-pressure-switch/)

## See Also

- [Trane XR80 Blinking Yellow Light Codes: Full Flash-Code Fix Guide](/posts/trane-xr80-error-codes/)
- [Trane ComfortLink II Communicating Thermostat Fault Codes - What They Mean and How to Fix Them](/posts/trane-communicating-thermostat-fault-codes/)
- [Trane XR17 Heat Pump Error Codes - Fault Code and Flash Code Guide](/posts/trane-xr17-error-codes/)
- [Trane 8 Flashes Error Code — Causes & Fix](/posts/trane-8-flashes-error-code/)
