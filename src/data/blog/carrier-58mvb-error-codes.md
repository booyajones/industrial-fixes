---
title: "Carrier 58MVB Furnace Error Codes — Variable-Speed Furnace Fault Guide"
description: "Complete guide to Carrier 58MVB variable-speed furnace error codes, flash sequences, what each fault means, and how to diagnose and fix the most common failures."
pubDatetime: 2026-04-22T22:00:00Z
modDatetime: 2026-04-22T22:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - carrier
  - furnace
---

## Carrier 58MVB Furnace Error Codes — What They Mean

The Carrier 58MVB is a variable-speed, multi-position gas furnace that uses an ECM blower motor and communicates status through a diagnostic LED on the control board. Faults are displayed as flash sequences — count the fast flashes, then the slow flashes, to get the code. For example, 3 fast + 3 slow = Code 33. The LED is visible through the sight glass on the lower door without opening the furnace.

[Jump to Fix](#fix)

## Carrier 58MVB Flash Code Reference

| Flash Code | Meaning |
|------------|---------|
| 1 flash | Normal — furnace call satisfied |
| 2 flashes | System lockout — retry limit reached |
| 3 flashes | Pressure switch stuck open or failed |
| 4 flashes | Open high-limit switch |
| 5 flashes | Flame detected with no call for heat |
| 6 flashes | 115V power issue at control board |
| 7 flashes | Gas valve circuit fault |
| 8 flashes | Low flame signal (weak or dirty flame sensor) |
| 9 flashes | Reversed pressure switch hose |
| 11 flashes | Ignitor circuit open |
| 13 flashes | Limit switch cycle lockout (>3 trips in one hour) |
| 14 flashes | Ignition lockout (3 failed ignition attempts) |
| 23 flashes | Pressure switch stuck closed before inducer |
| 24 flashes | Secondary pressure switch (two-stage units) |
| 31 flashes | High-limit switch open |
| 33 flashes | Pressure switch opens during run cycle |
| 34 flashes | Ignition proving failed |
| 45 flashes | Control board or gas valve fault |

## Common Causes by Code

- **Code 3 / 33 — Pressure switch** — Clogged condensate drain, cracked inducer housing, kinked pressure switch tubing, or weak inducer motor. The 58MVB is a high-efficiency furnace; a plugged condensate drain is the #1 cause of pressure switch faults.
- **Code 4 / 31 — High limit** — Dirty filter, blocked return air, or failed ECM blower motor. The variable-speed ECM can fail in ways that reduce airflow without stopping entirely — check actual CFM, not just whether the motor spins.
- **Code 8 — Weak flame signal** — Dirty or cracked flame sensor rod. On the 58MVB, the sensor is near the burner assembly. Normal flame signal is 1.5–5 µA DC; below 1.0 µA causes nuisance lockouts.
- **Code 14 — Ignition lockout** — Failed hot surface ignitor, gas pressure too low, or valve not opening. Check ignitor resistance (should be 40–90 ohms cold), then check gas pressure at the valve inlet.
- **Code 45 — Control board fault** — Often a failed gas valve relay on the board. If you confirm 24V at the valve but no gas flow, the valve itself may be failed. Control boards on the 58MVB are model-specific — confirm exact part before ordering.

## Step-by-Step Fix {#fix}

1. **Read the flash code** — With the furnace off, remove the upper door and observe the LED through the lower sight glass during the next startup attempt. Count flashes carefully; write down the sequence.
2. **For pressure switch codes (3, 23, 33)** — Inspect the condensate trap and drain line. Blow gently into the pressure switch tubing to confirm it is not plugged. Disconnect the hose at the switch and apply 1–2 inches of water column pressure with a manometer to confirm switch actuation.
3. **For limit switch codes (4, 13, 31)** — Replace the air filter first. Confirm all supply and return registers are open. Let the furnace cool 30 minutes, then retry. If limit trips again within minutes, the ECM blower motor may have a failed winding — measure actual airflow or check blower RPM against the control board tap settings.
4. **For ignition/flame codes (8, 11, 14)** — Measure ignitor resistance with the power off. Inspect flame sensor and clean with steel wool if coated. Confirm 24V AC reaches the gas valve during the ignition trial period.
5. **Clear lockout** — For codes 2 and 14, turn the thermostat off for 30 seconds, then back on to reset. Some lockouts require cycling the 115V power at the disconnect.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Flame sensor | [Amazon](https://www.amazon.com/dp/B0CZ7M9V4D?tag=errorcodefixes-20) \| Most common cause of Code 8; clean or replace |
| Hot surface ignitor | [Amazon](https://www.amazon.com/dp/B00BTLLJ40?tag=errorcodefixes-20) \| For Code 11 or 14; confirm correct wattage for 58MVB |
| Pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?tag=errorcodefixes-20) \| For persistent Code 3 or 33 after drain is clear |
| High-limit switch | [Amazon](https://www.amazon.com/dp/B0BN3TRG9R?tag=errorcodefixes-20) \| For persistent Code 4/31 with adequate airflow |
| Control board | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?tag=errorcodefixes-20) \| For Code 45 or board damage; match to furnace serial |
| Condensate trap | [Amazon](https://www.amazon.com/dp/B077J4Y763?tag=errorcodefixes-20) \| Replace if cracked or plugged; specific to 58MVB design |
## When to Call a Pro

Gas pressure testing and gas valve diagnosis require a calibrated manometer and knowledge of proper manifold pressure settings for the 58MVB. ECM blower motor troubleshooting also requires specialized test equipment — a failed ECM module can mimic several different fault codes. If you've cleared the drain, replaced the filter, and the furnace still faults on every cycle, call a Carrier-authorized technician.

## Related Articles

- [Carrier 11 Error Code — Causes & Fix](/posts/carrier-11-error-code/)
- [Carrier 12 Error Code — Causes & Fix](/posts/carrier-12-error-code/)
- [Carrier 13 Error Code — Limit Switch Lockout Fix](/posts/carrier-13-error-code/)
- [Carrier 13 Soft Lockout — What's Different from Hard Lockout](/posts/carrier-13-soft-lockout/)
- [Carrier 14 Error Code — Causes & Fix](/posts/carrier-14-error-code/)
