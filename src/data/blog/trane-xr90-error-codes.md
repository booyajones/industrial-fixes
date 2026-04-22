---
title: "Trane XR90 Furnace Error Codes — Fault Code Diagnostic Guide"
description: "Complete guide to Trane XR90 furnace error codes, LED flash sequences, common fault causes, and step-by-step repair procedures for HVAC technicians."
pubDatetime: 2026-04-22T23:00:00Z
modDatetime: 2026-04-22T23:00:00Z
author: "ErrorCodeFixes"
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

| [Flash Sequence](https://www.amazon.com/s?k=Flash%20Sequence&tag=errorcodefixe-20) | Fault |
|---|---|
| [1 flash](https://www.amazon.com/s?k=1%20flash&tag=errorcodefixe-20) | Normal — standby |
| [2 flashes](https://www.amazon.com/s?k=2%20flashes&tag=errorcodefixe-20) | Pressure switch stuck open |
| [3 flashes](https://www.amazon.com/s?k=3%20flashes&tag=errorcodefixe-20) | Pressure switch stuck closed |
| [4 flashes](https://www.amazon.com/s?k=4%20flashes&tag=errorcodefixe-20) | Open limit device |
| [5 flashes](https://www.amazon.com/s?k=5%20flashes&tag=errorcodefixe-20) | Flame sensed without gas valve call |
| [6 flashes](https://www.amazon.com/s?k=6%20flashes&tag=errorcodefixe-20) | 115V power reversed — hot and neutral swapped |
| [7 flashes](https://www.amazon.com/s?k=7%20flashes&tag=errorcodefixe-20) | Gas valve stuck open |
| [8 flashes](https://www.amazon.com/s?k=8%20flashes&tag=errorcodefixe-20) | Ignition failure — exceeded retry limit |
| [9 flashes](https://www.amazon.com/s?k=9%20flashes&tag=errorcodefixe-20) | Inducer motor fault |
| [Rapid flash](https://www.amazon.com/s?k=Rapid%20flash&tag=errorcodefixe-20) | Low voltage — check transformer |
| [Continuous](https://www.amazon.com/s?k=Continuous&tag=errorcodefixe-20) | Normal — blower running in cooling or fan mode |

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
| [Hot surface igniter](https://www.amazon.com/s?k=Hot%20surface%20igniter&tag=errorcodefixe-20) | Norton 601, silicon carbide; fragile — don't touch the ceramic |
| [Flame sensor](https://www.amazon.com/s?k=Flame%20sensor&tag=errorcodefixe-20) | Rod-type; clean with steel wool before replacing |
| [Inducer motor capacitor](https://www.amazon.com/s?k=Inducer%20motor%20capacitor&tag=errorcodefixe-20) | 5 or 7.5 µF; measure before replacing motor |
| [Pressure switch](https://www.amazon.com/s?k=Pressure%20switch&tag=errorcodefixe-20) | Two switches on some XR90 versions (high and low) |
| [High-limit switch](https://www.amazon.com/s?k=High-limit%20switch&tag=errorcodefixe-20) | L200°F on most XR90 configurations |
| [Blower capacitor](https://www.amazon.com/s?k=Blower%20capacitor&tag=errorcodefixe-20) | PSC blower motor; dedicated capacitor |

## When to Call a Pro

The XR90 heat exchanger is a clamshell design that can crack at the secondary (condensate-side) section. If you smell combustion gases in the conditioned air, suspect a cracked heat exchanger — this is a safety issue requiring professional inspection and likely furnace replacement. Do not operate a furnace with a suspected cracked heat exchanger.
