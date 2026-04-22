---
title: "Danfoss VFD Fault Codes — FC301, FC302, FC102 Reference"
description: "Danfoss VFD fault codes: all alarm codes for VLT FC301, FC302, and FC102 drives including AL-14, AL-29, OC, OL, and trip faults."
pubDatetime: 2026-04-22T16:00:00Z
modDatetime: 2026-04-22T16:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - danfoss
---

## Danfoss VFD Fault Codes — Quick Reference

Danfoss VLT drives (FC51 Micro, FC101, FC102 HVAC, FC202 Aqua, FC301, FC302) display fault codes as "AL" (alarm) numbers on the LCP keypad. Alarms stop the drive; warnings display without stopping. Retrieve fault history via Main Menu > Alarm Log (parameter 15-30 group).

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Meaning | Common Fix | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------ |---------|-----------|
| AL-14 | [Ground fault](https://www.amazon.com/s?k=Ground%20fault&tag=errorcodefixe-20) | Megger motor and cable |
| [AL-29](https://www.amazon.com/s?k=AL-29&tag=errorcodefixe-20) | Heatsink overtemperature | Clean fan; check ambient | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | OC / AL-13 | Overcurrent | [Check motor and acceleration](https://www.amazon.com/s?k=Check%20motor%20and%20acceleration&tag=errorcodefixe-20) |  | OL / AL-9 | [Inverter overloaded](https://www.amazon.com/s?k=Inverter%20overloaded&tag=errorcodefixe-20) | Reduce load; check motor current |
| [UL / AL-3](https://www.amazon.com/s?k=UL%20%2F%20AL-3&tag=errorcodefixe-20) | Undervoltage | Check input power | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | W30 / AL-30 | Motor phase missing | [Check motor connection](https://www.amazon.com/s?k=Check%20motor%20connection&tag=errorcodefixe-20) |  | AL-35 | [Input phase imbalance](https://www.amazon.com/s?k=Input%20phase%20imbalance&tag=errorcodefixe-20) | Check supply phases |
| [AL-47](https://www.amazon.com/s?k=AL-47&tag=errorcodefixe-20) | 24V supply low | Check 24V control supply | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | AL-69 | Drive board temperature | [Check fan and airflow](https://www.amazon.com/s?k=Check%20fan%20and%20airflow&tag=errorcodefixe-20) |  | AL-74 | [Thermistor fault (motor)](https://www.amazon.com/s?k=Thermistor%20fault%20(motor)&tag=errorcodefixe-20) | Check motor thermistor wiring |
| [OCL](https://www.amazon.com/s?k=OCL&tag=errorcodefixe-20) | Overcurrent limit (HVAC) | Reduce setpoint or load | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | E-Trip | Electronic trip (current) | [Check load and current settings](https://www.amazon.com/s?k=Check%20load%20and%20current%20settings&tag=errorcodefixe-20) | ## Most Common Codes

### AL-14: Ground Fault
The drive detected a current imbalance indicating a path to ground. On Danfoss FC302, AL-14 trips at relatively low ground current levels — it's a sensitive trip. Disconnect the motor, megger test each phase to ground at 500V DC (should be >1 MΩ). Also check for water ingress in outdoor junction boxes and motor terminal boxes. Long cable runs on unshielded cables can trigger AL-14 due to capacitive charging current — if cable is over 100 meters, ensure cable capacitance doesn't exceed drive rating.

### AL-29: Heatsink Overtemperature
The IGBT heatsink temperature exceeded limit. Check: (1) the cooling fan (inside the drive) is spinning and moving air, (2) heatsink fins are free of dust, (3) ambient temperature is within spec (typically 40–45°C max), (4) drive isn't mounted directly against hot surfaces or other heat sources. On Danfoss compact drives (FC51, FC101), the fan draws air through the bottom — ensure 100mm clearance at the bottom.

### AL-13 / OC: Overcurrent
Motor or cable overcurrent. Follow the same diagnosis as other VFD overcurrent faults: check motor FLA setting (parameter 1-24), test motor insulation, verify no mechanical jam, and check acceleration ramp (parameter 3-41). On Danfoss HVAC drives (FC102), also verify the motor control mode is set correctly — VVC+ mode works for most applications; Flux Vector Control requires motor data input.

### AL-9 / OL: Inverter Overload
The drive's internal thermal model calculated that the drive has been running at too high a load for too long. Either (1) the drive is undersized for the application, (2) the carrier frequency is set too high (increasing drive losses), or (3) there's a mechanical issue causing sustained high load. Check parameter 16-33 (Inverter Temp) to see the thermal state. Reduce carrier frequency (parameter 14-01) if set above default.

### W30: Motor Phase Missing
One motor phase is open. Check motor terminal box connections and the cable between the drive and motor. On FC302 drives, W30 can also appear if the "Load = no motor" detection feature (parameter 4-58) is enabled and there's a light-load condition.

### OCL (FC101/FC102 HVAC Drives)
The output current exceeded the current limit setting (parameter 4-18). Unlike a hardware overcurrent trip (AL-13), OCL is a software limit that clamps current and limits motor torque. If the application needs more torque, increase the current limit carefully. If OCL persists, the pump or fan load is higher than designed — check for blocked impellers or oversized resistance.

## Retrieving Fault Details

Navigate to Main Menu → Alarm Log (parameter group 15-3x). Each stored alarm entry shows:
- Alarm number
- Drive state at time of alarm (running/stopping)
- DC bus voltage
- Output frequency
- Output current

This data is valuable for diagnosing intermittent faults.

## Parts Often Needed | Part | [Notes](https://www.amazon.com/s?k=Notes&tag=errorcodefixe-20) |  |------|-------|
| Braking resistor | [Danfoss BRT series or equivalent, size per catalog](https://www.amazon.com/s?k=Danfoss%20BRT%20series%20or%20equivalent%2C%20size%20per%20catalog&tag=errorcodefixe-20) |  | Cooling fan | [FC302: 132B0093; drive-specific](https://www.amazon.com/s?k=FC302%3A%20132B0093%3B%20drive-specific&tag=errorcodefixe-20) |  | LCP remote panel | LCP-102 graphical or LCP-11 numeric |

## When to Call a Pro
AL-14 (ground fault) that persists after motor/cable testing, and any alarm related to a hardware trip (drive output damage, burnt smell), requires authorized Danfoss service. Field-level IGBT replacement is possible on larger FC302 frames but requires ESD training and proper procedures.
