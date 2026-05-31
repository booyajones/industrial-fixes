---
title: "LG Mini-Split CH22 Error Code — Indoor Fan Motor Fix"
author: "Marcus Webb"
pubDatetime: 2026-04-26T18:15:00Z
modDatetime: 2026-04-26T18:15:00Z
slug: lg-mini-split-ch22-error-code
featured: false
draft: false
tags:
  - lg
  - mini-split
  - hvac
  - error-codes
description: "LG mini-split CH22 error code means indoor fan motor lock or overcurrent fault. Learn how to diagnose the fan motor, check wiring, and fix or replace the indoor blower."
---

## LG Mini-Split CH22 Error Code — Indoor Fan Motor Fault

The **LG mini-split CH22 error code** indicates an **indoor fan motor fault** — specifically, a locked rotor condition or overcurrent detected in the indoor unit's blower motor. When the control board detects that the fan motor is not spinning at the expected speed, drawing excessive current, or has stopped completely, it shuts down the system and displays CH22 to prevent motor burnout and protect the heat exchanger.

CH22 appears on LG Art Cool, DUALCOOL, Multi-V, and other LG mini-split indoor units.

---

## What CH22 Means

The indoor unit fan motor is responsible for pulling room air over the evaporator coil to deliver conditioned air into the space. When the motor locks up (fails to rotate), draws too much current (overcurrent), or the control board loses the motor's speed feedback signal, CH22 is triggered.

CH22 is different from:
- **CH21** — Indoor fan motor speed error (slow but not locked)
- **CH26** — Communication error between indoor and outdoor unit

If your unit is displaying CH21, see our CH21 guide. If displaying CH26, the issue is communication-related, not the fan motor.

---

## Common Causes of CH22

- **Fan motor bearing failure** — worn or seized bearings prevent the rotor from spinning freely; this is the most common cause on units 5–10+ years old
- **Foreign object in the fan wheel** — a screw, piece of debris, or hardened dust chunk has jammed the blower wheel
- **Fan wheel cracked or loose on the motor shaft** — the wheel can separate and contact the housing, causing a lockout
- **Motor winding failure** — open or shorted winding prevents the motor from developing torque
- **Motor run capacitor failed** (on PSC-type motors) — a dead capacitor causes the motor to hum without rotating
- **Control board failed** — the motor drive circuit on the indoor board has failed, sending no power or incorrect power to the motor
- **Connector loose or corroded** between the control board and the fan motor

---

## Step-by-Step Diagnosis {#step-by-step-fix}

### Step 1: Power down safely

Turn off the mini-split at the thermostat or remote control, then shut off the circuit breaker or disconnect for the indoor unit. Wait 2 minutes before opening the unit.

### Step 2: Remove the front panel and filter

Most LG indoor units have a front panel that lifts off after releasing two clips at the bottom. Remove the panel and the air filter(s) to access the interior.

### Step 3: Inspect for obstructions

Look into the fan wheel area with a flashlight. The indoor blower is a cylindrical "squirrel cage" wheel running the full width of the unit. Look for:
- Debris lodged between the wheel blades and the housing
- Ice accumulation on the wheel (can occur if the system ran with low refrigerant or poor airflow)
- Dust buildup so severe that the wheel is out of balance and contacts the housing

Remove any obstructions. If the wheel is iced, allow it to thaw completely before proceeding.

### Step 4: Test fan wheel rotation by hand

With power still OFF, try to spin the fan wheel by hand (reach in from the side or through the filter opening). The wheel should rotate smoothly with minimal resistance. If it is:
- **Completely seized** — bearing failure is likely; proceed to motor replacement
- **Stiff but rotates** — bearing wear or winding issue; continue diagnosis
- **Spins freely** — the motor itself may be electrically failed, or the control board is the issue

### Step 5: Check the motor wiring and connector

Locate the fan motor connector on the indoor unit control board. Check for:
- Loose connector (push firmly to seat)
- Corroded or burned pins
- Damaged wires from the connector to the motor

### Step 6: Measure motor winding resistance

Disconnect the motor connector from the board. Using a multimeter, measure resistance across each motor winding terminal:
- A healthy motor winding typically reads 10–100 Ω depending on motor size and winding type
- An open winding (OL/infinite resistance) indicates a burned-out winding
- A winding that reads zero ohms indicates a short

If any winding is open or shorted, replace the motor.

### Step 7: Check the run capacitor (if applicable)

Some LG indoor fan motors use a run capacitor. If present, test it with a capacitance meter. A failed capacitor reads zero or very low capacitance. Replace with the same value and voltage rating.

### Step 8: Check board motor output

If the motor tests electrically healthy and spins freely by hand, reconnect power briefly and use a multimeter to verify the control board is sending voltage to the motor connector when the unit should be running. No voltage = control board motor drive circuit failed.

---

## How to Fix CH22

| Root Cause | Fix |
|-----------|-----|
| Debris in fan wheel | Remove obstruction and clean the wheel |
| Fan motor bearing failure | Replace the indoor fan motor |
| Motor winding open/shorted | Replace the indoor fan motor |
| Run capacitor failed | Replace the capacitor |
| Loose connector | Re-seat connector firmly |
| Control board failed | Replace the indoor control board |

---

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Typical Cost | Where to Buy |
|------|-------------|-------------|
| LG Indoor Fan Motor (blower motor) | $80–$180 | [Amazon](https://www.amazon.com/dp/B0D2L5NSMM?ascsubtag=ecf-lg-mini-split-ch22-error-code&tag=errorcodefixes-20) |
| Indoor Unit Control Board | $120–$280 | [Amazon](https://www.amazon.com/s?k=Indoor+Unit+Control+Board&tag=errorcodefixes-20) |
| Fan Motor Run Capacitor | $10–$25 | [Amazon](https://www.amazon.com/dp/B01M05L7B3?ascsubtag=ecf-lg-mini-split-ch22-error-code&tag=errorcodefixes-20) |
| LG Fan Wheel / Squirrel Cage | $40–$100 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-mini-split-ch22-error-code&k=LG+mini+split+indoor+fan+wheel+squirrel+cage&tag=errorcodefixes-20) |

---

## When to Call a Technician

If diagnosis points to the control board (no motor output voltage despite healthy motor), or if the motor replacement does not clear CH22, have an LG-authorized HVAC technician inspect the unit. An incorrectly diagnosed CH22 that is actually caused by a refrigerant pressure fault interfering with motor control is uncommon but possible on some LG platform versions — a technician can connect LG's service tool (LG LGMV) for detailed diagnostics.

> **Pro tip:** CH22 faults on LG mini-splits in humid climates often follow a pattern: the unit runs fine in summer, sits unused in winter, and comes up CH22 the following cooling season. The cause is usually rust or corrosion on the motor shaft causing the bearing to seize after sitting idle. Running the fan mode periodically through the off-season prevents this.

## Related Articles

- [LG Mini-Split CH21 Error Code — Fan Speed Error](/posts/lg-mini-split-ch21-error-code/)
- [LG Mini-Split CH10 Error Code — Indoor Coil Sensor](/posts/lg-mini-split-ch10-error-code/)
- [LG Mini-Split CH26 Error Code — Communication Error](/posts/lg-mini-split-ch26-error-code/)

<!-- INTERNAL-LINK-AUTO -->
**Related:** [LG washer error codes (complete guide)](/posts/lg-washer-error-codes/)

<!-- INTERNAL-LINK-AUTO -->
**Related:** [LG washer error code 31 (pressure / suspension fault)](/posts/lg-washer-error-code-31/)

## See Also

- [LG Refrigerator Error ER RF — Evap Fan Motor Fix](/posts/lg-refrigerator-error-er-rf/)
- [LG Mini Split CH01 Error Code — Causes & Fix](/posts/lg-mini-split-ch01-error-code/)
- [LG Washer Error Codes — Complete Fix Guide](/posts/lg-washer-error-codes/)
- [LG Mini Split CH02 Error Code — Causes & Fix](/posts/lg-mini-split-ch02-error-code/)
