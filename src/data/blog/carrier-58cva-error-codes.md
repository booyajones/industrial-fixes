---
title: "Carrier 58CVA Furnace Error Codes — Fault Code Diagnostic Guide"
description: "Complete guide to Carrier 58CVA furnace error codes, LED flash sequences, common fault causes, and step-by-step repair procedures for HVAC technicians."
pubDatetime: 2026-04-22T23:00:00Z
modDatetime: 2026-04-22T23:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - carrier
  - furnace
money_part: "Hot surface igniter"
---

## Carrier 58CVA Furnace Error Codes — What They Mean

The Carrier 58CVA is a two-stage variable-speed gas furnace delivering 80% AFUE efficiency. It uses an ECM blower motor for variable airflow and a two-stage gas valve for improved comfort and dehumidification. The 58CVA communicates faults through a two-digit LED display on the control board — a more informative system than single-LED flash codes. Each code is a two-digit number that identifies both the fault category and specific condition.

[Jump to Fix](#fix)

## Carrier 58CVA Error Code Reference

| Code | Fault |
|---|---|
| 11 | No ignition — failed to light |
| 12 | Blower on after delay (not a fault — status) |
| 13 | Limit device lockout — exceeded 3 limit trips |
| 14 | Ignition lockout — exceeded 3 ignition failures |
| 21 | Gas heating lockout — control reset required |
| 22 | Abnormal flame sense current |
| 23 | Pressure switch stuck open |
| 24 | Secondary voltage fuse blown |
| 25 | Modulating gas valve fault |
| 31 | Pressure switch stuck closed |
| 32 | Pressure switch open during run |
| 33 | Limit circuit open |
| 34 | Igniter circuit open |
| 41 | Blower motor fault |
| 42 | Inducer motor fault |
| 43 | Condensate system fault (if equipped) |
| 44 | Flame sensed after gas valve closed |
| 45 | Control board fault |
| 46 | Incorrect line voltage (out of range) |
| 47 | Low-stage pressure switch stuck open |

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
| Hot surface igniter | [Amazon](https://www.amazon.com/dp/B00BTLLJ40?ascsubtag=ecf-carrier-58cva-error-codes&tag=errorcodefixes-20) \| Silicon nitride; handle carefully, avoid touching ceramic |
| Flame sensor | [Amazon](https://www.amazon.com/s?k=Flame+sensor&tag=errorcodefixes-20) \| Clean first; replace if cracked or reading <0.5 µA |
| ECM blower motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-carrier-58cva-error-codes&k=ECM+blower+motor&tag=errorcodefixes-20) \| Verify correct motor model; programmed to unit |
| Inducer motor | [Amazon](https://www.amazon.com/dp/B00FDZ90B2?ascsubtag=ecf-carrier-58cva-error-codes&tag=errorcodefixes-20) \| Match frame size and speed rating |
| High-limit switch | [Amazon](https://www.amazon.com/dp/B0BN3TRG9R?ascsubtag=ecf-carrier-58cva-error-codes&tag=errorcodefixes-20) \| L170°F or L200°F depending on unit config |
| Pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-carrier-58cva-error-codes&tag=errorcodefixes-20) \| Check tubing for blockage before replacing |
## When to Call a Pro

The 58CVA's two-stage gas valve and ECM motor require familiarity with Carrier's variable-speed control logic to diagnose correctly. If Code 45 (control board fault) appears, contact a Carrier authorized dealer — board replacement on a variable-speed furnace requires configuration matching the ECM motor and gas valve parameters.

## Related Articles

- [Carrier 11 Error Code — Causes & Fix](/posts/carrier-11-error-code/)
- [Carrier 12 Error Code — Causes & Fix](/posts/carrier-12-error-code/)
- [Carrier 13 Error Code — Limit Switch Lockout Fix](/posts/carrier-13-error-code/)
- [Carrier 13 Soft Lockout — What's Different from Hard Lockout](/posts/carrier-13-soft-lockout/)
- [Carrier 14 Error Code — Causes & Fix](/posts/carrier-14-error-code/)

## See Also

- [Carrier Infinity 24VNA6 Heat Pump Error Codes - Greenspeed Fault Reference](/posts/carrier-24vna6-error-codes/)
- [Carrier WeatherMaker RTU Error Code 23 — Fix](/posts/carrier-weathermaster-rtu-error-code-23/)
- [Carrier Rooftop Unit Error Codes: Common Faults Guide](/posts/carrier-rooftop-unit-error-codes/)
- [Carrier 48 Error Code — Induced Draft Motor Lockout](/posts/carrier-48-error-code/)
