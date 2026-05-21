---
title: "Danfoss FC-302 Alarm 12 — Overcurrent Fix"
description: "Danfoss FC-302 Alarm 12 (Torque Limit) means the drive's output current has been at the torque-limit setting (parameter 4-16 Motor Mode Torque Limit,..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: danfoss-fc302-alarm-12
featured: false
draft: false
tags:
  - danfoss
  - vfd
  - industrial-maintenance
  - drives
  - overcurrent-torque-limit
---
## Quick answer

Danfoss FC-302 Alarm 12 (Torque Limit) means the drive's output current has been at the torque-limit setting (parameter 4-16 Motor Mode Torque Limit, default 110%) for longer than the timeout in parameter 14-25 (default 60 seconds). This is technically a "I tried to give the motor more torque and you wouldn't let me" alarm, not a hard overcurrent fault — that's Alarm 13. The most common field cause is a mechanical bind: a seized bearing, a jammed conveyor, a frozen mixer, or a motor pulley that lost a setscrew and is dragging. The second most common is an auto-tune (AMA) that was never run, leaving the drive's internal motor model wrong so the current regulator overshoots.

## What Danfoss FC-302 Alarm 12 means

The FC-302 has two distinct overcurrent-class alarms and you need to know the difference. **Alarm 12 (Torque Limit)** is an integrated-time alarm — the drive operated at or above the torque limit set in parameter 4-16 (motor mode) or 4-17 (generator mode) for longer than the warning timeout in 14-25. **Alarm 13 (Overcurrent)** is the hardware-level instantaneous trip when motor current exceeds approximately 200% of inverter rated current. Alarm 12 is the drive complaining you've been pushing too hard for too long. Alarm 13 is the drive saving its own IGBTs from a short circuit.

The FC-302 measures motor current with Hall-effect sensors on each of the three output phases, sampled at the PWM rate (parameter 14-01 Switching Frequency, default 4 kHz on 380–500V drives below 7.5 kW). The torque limit is enforced by reducing output frequency in real time when measured current would exceed parameter 4-16. If the drive cannot maintain the commanded speed within the torque limit for longer than 14-25, it trips Alarm 12 to protect the motor and signal that the application is malfunctioning.

The "right" response to Alarm 12 is almost never to raise 4-16 above 110%. Going to 160% or 200% just pushes the motor closer to thermal damage and the drive closer to Alarm 13. The right response is to find out *why* the load is demanding more torque than the application engineer designed for.

## Read the fault history first

The FC-302 stores its alarm log in parameter group 15-3X. Read it before pressing Reset on the LCP (Local Control Panel). On the LCP 102 graphical display or LCP 101 numerical display:

1. Press **[Main Menu]** to enter the parameter tree
2. Navigate to parameter group **15 Drive Information** → **15-3 Alarm Log**
3. Read these parameters in order:
   - **15-30** — Alarm Log: Error Code (most recent at index 0, oldest at index 9 — the FC-302 keeps 10 alarms deep)
   - **15-31** — Alarm Log: Value (the value associated with the alarm, e.g., motor current for Alarm 12)
   - **15-32** — Alarm Log: Time (the operating-hour timestamp when the alarm occurred)
   - **15-33** — Alarm Log: Date and Time (real-time clock if installed — most FC-302 drives ship with the RTC option)
4. Also read **15-00** Operating Hours, **15-01** Running Hours, and **15-04** Overtemps as context for whether this is a chronic problem
5. Cross-reference with **16-10** Power [kW], **16-11** Power [hp], **16-14** Motor Current — to see what the drive was outputting *just before* the trip. The Quick Menu → Drive Status display also shows recent operating snapshot

Danfoss documents this in the FC-300 Programming Guide MG33MJ22 section 5.3 (Parameter 15-3X) and the FC-302 Operating Instructions MG33AK22 chapter 7 (Troubleshooting).

**Field insight — the Alarm 12 history trap:** parameter 15-31 (Alarm Log Value) for an Alarm 12 records the *output current at the moment of trip* in amps. People misread this as the trip threshold — it's not. The trip threshold is parameter 4-16 expressed as a percentage of the motor's rated current (parameter 1-24 Motor Current). So if 1-24 = 10.0 A and 4-16 = 110%, the trip happens at sustained 11.0 A output. If 15-31 reads 12.4 A, the drive was at 124% of motor rated, well above 4-16, for the timeout duration. Compare 15-31 to 1-24 × (4-16/100) and you'll know whether the trip was textbook or anomalous.

## Common causes (ranked by frequency)

1. **Mechanical bind on the driven load** — seized bearing, jammed material in a conveyor, frozen mixer paddle, gummed-up pump seal, broken gearbox tooth dragging
2. **AMA (Automatic Motor Adaptation) never performed or done wrong** — parameter 1-29 was never executed, drive's motor model is the default not the actual motor
3. **Motor nameplate parameters entered wrong** — 1-20 Power, 1-22 Voltage, 1-23 Frequency, 1-24 Current, 1-25 Nominal Speed do not match the motor on the shaft
4. **Acceleration ramp too short for load inertia** — parameter 3-41 (Ramp 1 Ramp-up Time) too aggressive, drive can't accelerate inside the torque limit
5. **Drive undersized for application** — someone replaced a 10 HP motor with a 15 HP motor but kept the original 10 HP drive
6. **Torque limit set too low** — parameter 4-16 was reduced to 80% or 90% by someone trying to "protect" the motor, but the application legitimately needs 100%
7. **Long motor cable with no output reactor** — reflected-wave standing voltage at the motor causes excess motor heating and apparent current draw

## Step-by-step diagnosis

Lock and tag the upstream disconnect on the drive's input contactor. Wait the FC-302 capacitor discharge time — Danfoss specifies a minimum of **4 minutes** for frame sizes A1 through A3, **15 minutes** for B and C frames, and **20 minutes** for D, E, and F frames. Verify zero DC bus at terminals 88 (-) and 89 (+) with a CAT-IV meter rated 1000 VDC. Stay outside the NFPA 70E arc-flash boundary on the cabinet label until you've confirmed zero energy and you are in the proper PPE.

1. **Read the alarm log before clearing.** Capture parameters 15-30 (the alarm code, should read 12), 15-31 (output current at trip), 15-32 (operating-hour timestamp), and 15-33 (real-time clock timestamp if equipped). Compare 15-31 to your motor's rated current in parameter 1-24.

2. **Manually rotate the load.** With the drive de-energized and confirmed dead, uncouple the load from the motor if possible. Rotate the load by hand and feel for resistance, binding, or grinding. A normal load should rotate freely or with smooth resistance proportional to the application (a pump has water in it, a fan has air, a conveyor has belt tension — but no clunks, no hard spots). This single step catches more Alarm 12s than any electrical test.

3. **Verify motor nameplate parameters are correctly entered.** Read parameter 1-20 (Motor Power [kW]), 1-22 (Motor Voltage), 1-23 (Motor Frequency), 1-24 (Motor Current), 1-25 (Motor Nominal Speed), and 1-39 (Motor Poles). Every one of these must match the motor nameplate on the shaft, not the original motor that was replaced two years ago. The drive's torque calculation depends on these values being correct.

4. **Run AMA — Automatic Motor Adaptation.** With motor stopped and at ambient temperature, set parameter **1-29 = [1] Enable Complete AMA** (or [2] Enable Reduced AMA if you cannot decouple the load). Press [Hand On] to start. The drive will inject test currents for 1–3 minutes — it does not rotate the shaft on a complete AMA. When done, parameter 1-29 returns to [0] Off and stator resistance (1-30), rotor resistance (1-31), main reactance (1-35), and leakage reactances (1-33, 1-34) populate automatically. If AMA fails with an error code, the motor model is genuinely wrong and you have a winding problem.

5. **Verify torque limit and timeout.** Read parameter **4-16 Torque Limit Motor Mode** (default 110%) and **14-25 Trip Delay at Torque Limit** (default 60 sec). If 4-16 was reduced to 90% by someone, that's your fault. If 14-25 was reduced to 1 sec, that's also your fault — restore both to defaults and re-test.

6. **Check the ramp times.** Parameter **3-41 Ramp 1 Ramp-up Time** and **3-42 Ramp 1 Ramp-down Time** should be sized for the load inertia. A high-inertia centrifugal fan typically needs 30–60 seconds. A pump 5–15 seconds. A jammed-up ramp time forces the drive to demand torque past 4-16.

7. **Inspect motor cable and connections.** With drive de-energized, check torque on the U/T1, V/T2, W/T3 output lugs against the FC-300 design guide — frame A3 spec is 1.8 Nm (16 in-lb) for the M5 motor terminals. A loose lug causes arcing and apparent overcurrent.

8. **Megger the motor.** Disconnect the cable at the drive's motor terminals. Use a 1000V megger phase-to-ground on each motor lead. Acceptable: above 100 megohms when cold. Below 5 megohms means moisture or insulation damage; below 1 megohm is a definite ground fault. A motor with a turn-to-turn fault will pass megger but fail AMA.

9. **If still tripping after all of the above:** install an output reactor on long cable runs (50 m or longer), or replace the drive with one frame size larger if the application is at the edge of the drive's rating. Don't keep raising 4-16 — at some point you'll trip Alarm 13 instead and that means melted IGBTs.

## Parts that may need replacement

| Part | Catalog Number | Typical Cost | Where to Buy |
|---|---|---|---|
| FC-302, 480V, 5.5kW (7.5HP) | 131F0036 | $1,950–$2,350 | [AutomationDirect](https://www.automationdirect.com?aff=PLACEHOLDER-ADI), [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO) |
| FC-302, 480V, 11kW (15HP) | 131F0058 | $2,850–$3,400 | [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO), [Wolf Automation](https://www.wolfautomation.com?aff=PLACEHOLDER-WOLF) |
| FC-302, 480V, 22kW (30HP) | 131F0073 | $4,200–$5,100 | [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO), [Wolf Automation](https://www.wolfautomation.com?aff=PLACEHOLDER-WOLF) |
| LCP 102 graphical display | 130B1107 | $385–$485 | [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO), [Wolf Automation](https://www.wolfautomation.com?aff=PLACEHOLDER-WOLF) |
| LCP 101 numerical display | 130B1124 | $215–$285 | [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO), [AutomationDirect](https://www.automationdirect.com?aff=PLACEHOLDER-ADI) |
| Danfoss output reactor 22 kW | 130B2304 | $625–$795 | [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO), [Wolf Automation](https://www.wolfautomation.com?aff=PLACEHOLDER-WOLF) |
| Danfoss du/dt filter 11 kW | 130B2440 | $890–$1,150 | [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO) |
| Fluke 87V industrial multimeter | FLUKE-87-5 | $480–$580 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20), [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO) |
| Megger MIT420/2 1000V tester | MIT420/2 | $1,250–$1,500 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20), [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO) |
| Wiha torque screwdriver 1.0–5.0 Nm | Wiha 28503 | $215–$285 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |

The FC-302 power stage is not field-serviceable. If AMA fails and motor and cable check out, the drive itself has a current sensor or gate-drive problem and gets replaced. Danfoss offers a 24-month manufacturer warranty.

## When to call a controls engineer

Bring in senior support when: Alarm 12 trips happen only at specific output frequencies (suggests mechanical resonance — torsional vibration in the driveline you can address with parameter 4-61 Bypass Speed From and 4-62 Bypass Speed To); the drive is in flux vector mode (1-01 = [1]) and AMA fails repeatedly on a known-good motor; the application involves a high-inertia load with regenerative behavior on decel and you need to coordinate Alarm 12 (motoring) with Alarm 13 (overcurrent on regen); or when Alarm 12 only happens after the drive has been running for hours, suggesting thermal drift in the current measurement circuit.

## FAQs

**Can I just raise parameter 4-16 to 160% to get past Alarm 12?** You can, but you're masking a real problem. The motor will overheat at sustained torque above its design point (T-class insulation typically 110% for 1 minute, 150% for 30 seconds, no more). Find and fix the mechanical cause instead.

**Why does my drive trip Alarm 12 only on startup, never during steady-state?** Acceleration ramp is too short. The motor needs to overcome breakaway torque to start rotation — usually 1.5–2× running torque. Extend parameter 3-41 (Ramp 1 Ramp-up Time) and consider setting parameter 1-71 (Start Delay) and 1-72 (Start Function) to provide a brief DC injection before ramp.

**Difference between Alarm 12 and Alarm 13?** Alarm 12 is the integrated torque limit alarm — drive ran at limit for longer than 14-25 timeout. Alarm 13 is the instantaneous hardware overcurrent trip when motor current exceeds approximately 200% of inverter rating. Alarm 12 is "stop pushing so hard," Alarm 13 is "I'm protecting my IGBTs."

**Does AMA require disconnecting the load?** A complete AMA (1-29 = [1]) injects high-frequency test currents but does not rotate the shaft, so a coupled load is acceptable. A reduced AMA (1-29 = [2]) is for situations where motor is in a hazardous area and you cannot allow even high-frequency excitation. Run complete AMA whenever possible.

**Should I enable Smart Logic Controller to auto-reset Alarm 12?** No. Auto-reset on Alarm 12 will eventually let a binding mechanical load damage the motor or driveline. Use parameter 14-20 (Reset Mode) = [0] Manual Reset on torque-class alarms.

## Related guides

- [Danfoss FC-302 Alarm 13 — DC Link Overvoltage Fix](/danfoss-fc302-alarm-13/)
- [Yaskawa GA800 oC Fault — Overcurrent Fix](/yaskawa-ga800-error-oc/)
- [Allen-Bradley PowerFlex F012 Fault — HW Overcurrent Fix](/allen-bradley-powerflex-f012-fault/)
- [ABB ACS580 Fault 2310 — Overcurrent Fix](/abb-acs580-2310-fault/)
- [Allen-Bradley PowerFlex F070 Fault — Motor Overload Fix](/allen-bradley-powerflex-f070-fault/)
