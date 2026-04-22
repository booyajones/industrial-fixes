---
title: "Danfoss RX Controller Fault Codes — Troubleshooting Guide"
description: "Danfoss RX refrigeration controller fault codes and alarms: probe failures, defrost faults, communication issues, and step-by-step fixes."
pubDatetime: 2026-04-22T21:00:00Z
modDatetime: 2026-04-22T21:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - refrigeration
  - danfoss
  - controller
  - walk-in
---

## Danfoss RX Controller Fault Codes — Quick Reference

Danfoss refrigeration controllers use short alarm codes for sensor, temperature, defrost, and communication problems. The exact code list varies by controller family, but these are the alarms technicians see most often on RX-style walk-in and case controls.

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Meaning | Quick Fix | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------ |---------|-----------|
| E1 | [Room sensor fault](https://www.amazon.com/s?k=Room%20sensor%20fault&tag=errorcodefixe-20) | Check room probe and wiring |
| [E2](https://www.amazon.com/s?k=E2&tag=errorcodefixe-20) | Evaporator sensor fault | Check coil probe location and resistance | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | HA | High temperature alarm | [Check box temp, airflow, and refrigerant system](https://www.amazon.com/s?k=Check%20box%20temp%2C%20airflow%2C%20and%20refrigerant%20system&tag=errorcodefixe-20) |  | LA | [Low temperature alarm](https://www.amazon.com/s?k=Low%20temperature%20alarm&tag=errorcodefixe-20) | Check setpoint and sensor calibration |
| [dEF](https://www.amazon.com/s?k=dEF&tag=errorcodefixe-20) | Defrost fault / defrost overdue | Check heaters, termination probe, and timer settings | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | DO | Door open alarm | [Check door switch and wiring](https://www.amazon.com/s?k=Check%20door%20switch%20and%20wiring&tag=errorcodefixe-20) |  | Com | [Communication fault](https://www.amazon.com/s?k=Communication%20fault&tag=errorcodefixe-20) | Check network cable and addressing |

## Most Common Faults

### E1 — Room Sensor Fault
The controller cannot read the box temperature sensor. Check the probe resistance against the Danfoss temperature chart. A damaged probe wire near the door frame is common in walk-ins.

### E2 — Evaporator Sensor Fault
The coil sensor controls defrost termination and fan restart. If the probe is loose, hanging in free air, or failed, the controller may over-defrost or short-cycle defrost.

### dEF — Defrost Fault
If the controller does not see the coil warm up during defrost, it alarms on defrost. Check electric heater continuity, hot gas solenoid operation, and the termination sensor.

## Defrost Checklist

1. Start a manual defrost.
2. Verify heaters or hot gas energize.
3. Watch coil temperature rise on the controller.
4. Confirm defrost terminates before max time.
5. Confirm fan delay ends and fans restart.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [Room probe](https://www.amazon.com/s?k=Room%20probe&tag=errorcodefixe-20) | Replace on E1 alarms |
| [Evaporator probe](https://www.amazon.com/s?k=Evaporator%20probe&tag=errorcodefixe-20) | Replace on E2 or defrost alarms |
| [Defrost heater](https://www.amazon.com/s?k=Defrost%20heater&tag=errorcodefixe-20) | Replace if open on ohm check |
| [Door switch](https://www.amazon.com/s?k=Door%20switch&tag=errorcodefixe-20) | Replace on repeated DO alarms |

## Jump to Fix

- **E1** → Check probe connection → Measure resistance → Replace sensor
- **E2** → Check probe placement → Measure resistance → Replace sensor
- **dEF** → Force defrost → Check heater or hot gas → Check termination sensor

## When to Call a Pro
If the controller alarms after sensor replacement, the real problem may be refrigerant flow, hot gas piping, or a failed solenoid. A refrigeration technician should check the full system.
