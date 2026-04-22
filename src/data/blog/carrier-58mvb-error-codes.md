---
title: "Carrier 58MVB Furnace Error Codes — Variable-Speed Furnace Fault Guide"
description: "Complete guide to Carrier 58MVB variable-speed furnace error codes, flash sequences, what each fault means, and how to diagnose and fix the most common failures."
pubDatetime: 2026-04-22T22:00:00Z
modDatetime: 2026-04-22T22:00:00Z
author: "ErrorCodeFixes"
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

| [Flash Code](https://www.amazon.com/s?k=Flash%20Code&tag=errorcodefixe-20) | Meaning |
|------------|---------|
| [1 flash](https://www.amazon.com/s?k=1%20flash&tag=errorcodefixe-20) | Normal — furnace call satisfied |
| [2 flashes](https://www.amazon.com/s?k=2%20flashes&tag=errorcodefixe-20) | System lockout — retry limit reached |
| [3 flashes](https://www.amazon.com/s?k=3%20flashes&tag=errorcodefixe-20) | Pressure switch stuck open or failed |
| [4 flashes](https://www.amazon.com/s?k=4%20flashes&tag=errorcodefixe-20) | Open high-limit switch |
| [5 flashes](https://www.amazon.com/s?k=5%20flashes&tag=errorcodefixe-20) | Flame detected with no call for heat |
| [6 flashes](https://www.amazon.com/s?k=6%20flashes&tag=errorcodefixe-20) | 115V power issue at control board |
| [7 flashes](https://www.amazon.com/s?k=7%20flashes&tag=errorcodefixe-20) | Gas valve circuit fault |
| [8 flashes](https://www.amazon.com/s?k=8%20flashes&tag=errorcodefixe-20) | Low flame signal (weak or dirty flame sensor) |
| [9 flashes](https://www.amazon.com/s?k=9%20flashes&tag=errorcodefixe-20) | Reversed pressure switch hose |
| [11 flashes](https://www.amazon.com/s?k=11%20flashes&tag=errorcodefixe-20) | Ignitor circuit open |
| [13 flashes](https://www.amazon.com/s?k=13%20flashes&tag=errorcodefixe-20) | Limit switch cycle lockout (>3 trips in one hour) |
| [14 flashes](https://www.amazon.com/s?k=14%20flashes&tag=errorcodefixe-20) | Ignition lockout (3 failed ignition attempts) |
| [23 flashes](https://www.amazon.com/s?k=23%20flashes&tag=errorcodefixe-20) | Pressure switch stuck closed before inducer |
| [24 flashes](https://www.amazon.com/s?k=24%20flashes&tag=errorcodefixe-20) | Secondary pressure switch (two-stage units) |
| [31 flashes](https://www.amazon.com/s?k=31%20flashes&tag=errorcodefixe-20) | High-limit switch open |
| [33 flashes](https://www.amazon.com/s?k=33%20flashes&tag=errorcodefixe-20) | Pressure switch opens during run cycle |
| [34 flashes](https://www.amazon.com/s?k=34%20flashes&tag=errorcodefixe-20) | Ignition proving failed |
| [45 flashes](https://www.amazon.com/s?k=45%20flashes&tag=errorcodefixe-20) | Control board or gas valve fault |

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
| [Flame sensor](https://www.amazon.com/s?k=Flame%20sensor&tag=errorcodefixe-20) | Most common cause of Code 8; clean or replace |
| [Hot surface ignitor](https://www.amazon.com/s?k=Hot%20surface%20ignitor&tag=errorcodefixe-20) | For Code 11 or 14; confirm correct wattage for 58MVB |
| [Pressure switch](https://www.amazon.com/s?k=Pressure%20switch&tag=errorcodefixe-20) | For persistent Code 3 or 33 after drain is clear |
| [High-limit switch](https://www.amazon.com/s?k=High-limit%20switch&tag=errorcodefixe-20) | For persistent Code 4/31 with adequate airflow |
| [Control board](https://www.amazon.com/s?k=Control%20board&tag=errorcodefixe-20) | For Code 45 or board damage; match to furnace serial |
| [Condensate trap](https://www.amazon.com/s?k=Condensate%20trap&tag=errorcodefixe-20) | Replace if cracked or plugged; specific to 58MVB design |

## When to Call a Pro

Gas pressure testing and gas valve diagnosis require a calibrated manometer and knowledge of proper manifold pressure settings for the 58MVB. ECM blower motor troubleshooting also requires specialized test equipment — a failed ECM module can mimic several different fault codes. If you've cleared the drain, replaced the filter, and the furnace still faults on every cycle, call a Carrier-authorized technician.
