---
title: "Carrier 58CVA Furnace Error Codes — Fault Code Diagnostic Guide"
description: "Complete guide to Carrier 58CVA furnace error codes, LED flash sequences, common fault causes, and step-by-step repair procedures for HVAC technicians."
pubDatetime: 2026-04-22T23:00:00Z
modDatetime: 2026-04-22T23:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - carrier
  - furnace
---

## Carrier 58CVA Furnace Error Codes — What They Mean

The Carrier 58CVA is a two-stage variable-speed gas furnace delivering 80% AFUE efficiency. It uses an ECM blower motor for variable airflow and a two-stage gas valve for improved comfort and dehumidification. The 58CVA communicates faults through a two-digit LED display on the control board — a more informative system than single-LED flash codes. Each code is a two-digit number that identifies both the fault category and specific condition.

[Jump to Fix](#fix)

## Carrier 58CVA Error Code Reference

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Fault |
|---|---|
| [11](https://www.amazon.com/s?k=11&tag=errorcodefixe-20) | No ignition — failed to light |
| [12](https://www.amazon.com/s?k=12&tag=errorcodefixe-20) | Blower on after delay (not a fault — status) |
| [13](https://www.amazon.com/s?k=13&tag=errorcodefixe-20) | Limit device lockout — exceeded 3 limit trips |
| [14](https://www.amazon.com/s?k=14&tag=errorcodefixe-20) | Ignition lockout — exceeded 3 ignition failures |
| [21](https://www.amazon.com/s?k=21&tag=errorcodefixe-20) | Gas heating lockout — control reset required |
| [22](https://www.amazon.com/s?k=22&tag=errorcodefixe-20) | Abnormal flame sense current |
| [23](https://www.amazon.com/s?k=23&tag=errorcodefixe-20) | Pressure switch stuck open |
| [24](https://www.amazon.com/s?k=24&tag=errorcodefixe-20) | Secondary voltage fuse blown |
| [25](https://www.amazon.com/s?k=25&tag=errorcodefixe-20) | Modulating gas valve fault |
| [31](https://www.amazon.com/s?k=31&tag=errorcodefixe-20) | Pressure switch stuck closed |
| [32](https://www.amazon.com/s?k=32&tag=errorcodefixe-20) | Pressure switch open during run |
| [33](https://www.amazon.com/s?k=33&tag=errorcodefixe-20) | Limit circuit open |
| [34](https://www.amazon.com/s?k=34&tag=errorcodefixe-20) | Igniter circuit open |
| [41](https://www.amazon.com/s?k=41&tag=errorcodefixe-20) | Blower motor fault |
| [42](https://www.amazon.com/s?k=42&tag=errorcodefixe-20) | Inducer motor fault |
| [43](https://www.amazon.com/s?k=43&tag=errorcodefixe-20) | Condensate system fault (if equipped) |
| [44](https://www.amazon.com/s?k=44&tag=errorcodefixe-20) | Flame sensed after gas valve closed |
| [45](https://www.amazon.com/s?k=45&tag=errorcodefixe-20) | Control board fault |
| [46](https://www.amazon.com/s?k=46&tag=errorcodefixe-20) | Incorrect line voltage (out of range) |
| [47](https://www.amazon.com/s?k=47&tag=errorcodefixe-20) | Low-stage pressure switch stuck open |

## Common Causes by Code

- **Code 13 — Limit lockout** — The 58CVA high-limit switch is tripping due to overheating. Most common cause: dirty air filter restricting airflow through the heat exchanger. Second cause: failed ECM blower motor running below rated speed.
- **Code 14 — Ignition lockout** — The furnace attempted to ignite three times and failed. Check the hot surface igniter (HSI) — silicon nitride igniter glow time should produce a visible orange glow within 17 seconds. Also check gas supply pressure at the manifold (should be 3.5" WC for natural gas at full fire).
- **Code 22 — Abnormal flame sense** — The flame sensor rod produces a DC microamp signal (1.5–4 µA normal). Below 1 µA causes this code. Clean the sensor with steel wool. A cracked flame sensor rod or an open circuit in the sensor wire causes complete failure.
- **Code 33 — Limit circuit open** — The high-limit or roll-out switch is open. Check the roll-out switch first — it's a manual-reset device mounted at the burner box and trips if flames roll out (blocked heat exchanger or gas pressure too high).
- **Code 41 — Blower motor fault** — ECM motor fault. Check motor connector at both the motor and board. ECM motors communicate with the board — a fault in the motor or communication circuit triggers this code.
- **Code 42 — Inducer motor fault** — The inducer motor failed to reach operating speed. Check for blocked flue, failed inducer capacitor (on PSC-type inductors), or a seized inducer bearing.

## Step-by-Step Fix {#fix}

1. **Read the code** — The 58CVA board displays the fault code as two digits on the LED display. If the board has a fault history, it cycles through recent codes. Record all codes before clearing.
2. **For Code 13/33 (limit)** — Replace the air filter first. Then check return air temperature — should not exceed 85°F. Measure static pressure across the filter (should be less than 0.1" WC). Check blower motor RPM if a tachometer is available.
3. **For Code 14 (ignition lockout)** — Confirm gas supply is on at the shutoff valve upstream of the furnace. Measure gas pressure at the manifold test port. Inspect the igniter — a cracked igniter glows unevenly or fails to reach temperature.
4. **For Code 22 (flame sense)** — Remove the flame sensor wire. Clean the sensor rod with fine steel wool. Reinstall and measure microamp signal with a meter set to DC microamps (probe in series with the flame sensor wire).
5. **For Code 41 (blower)** — Check the ECM motor hall-effect connector (5-pin) for corrosion. Measure 120VAC supply to the motor. Spin the blower wheel by hand — if it turns freely but the motor won't run, the motor module may have failed.

## Parts Often Needed

| Part | Notes |
|---|---|
| [Hot surface igniter](https://www.amazon.com/s?k=Hot%20surface%20igniter&tag=errorcodefixe-20) | Silicon nitride; handle carefully, avoid touching ceramic |
| [Flame sensor](https://www.amazon.com/s?k=Flame%20sensor&tag=errorcodefixe-20) | Clean first; replace if cracked or reading <0.5 µA |
| [ECM blower motor](https://www.amazon.com/s?k=ECM%20blower%20motor&tag=errorcodefixe-20) | Verify correct motor model; programmed to unit |
| [Inducer motor](https://www.amazon.com/s?k=Inducer%20motor&tag=errorcodefixe-20) | Match frame size and speed rating |
| [High-limit switch](https://www.amazon.com/s?k=High-limit%20switch&tag=errorcodefixe-20) | L170°F or L200°F depending on unit config |
| [Pressure switch](https://www.amazon.com/s?k=Pressure%20switch&tag=errorcodefixe-20) | Check tubing for blockage before replacing |

## When to Call a Pro

The 58CVA's two-stage gas valve and ECM motor require familiarity with Carrier's variable-speed control logic to diagnose correctly. If Code 45 (control board fault) appears, contact a Carrier authorized dealer — board replacement on a variable-speed furnace requires configuration matching the ECM motor and gas valve parameters.
