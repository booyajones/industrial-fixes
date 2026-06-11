---
title: "Danfoss RX Controller Fault Codes — Troubleshooting Guide"
description: "Danfoss RX refrigeration controller fault codes and alarms: probe failures, defrost faults, communication issues, and step-by-step fixes."
pubDatetime: 2026-04-22T21:00:00Z
modDatetime: 2026-04-22T21:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - refrigeration
  - danfoss
  - controller
  - walk-in
money_part: "Room probe"
---

## Danfoss RX Controller Fault Codes — Quick Reference

Danfoss refrigeration controllers use short alarm codes for sensor, temperature, defrost, and communication problems. The exact code list varies by controller family, but these are the alarms technicians see most often on RX-style walk-in and case controls.

| Code | Meaning | Quick Fix |
|------|---------|-----------|
| E1 | Room sensor fault | Check room probe and wiring |
| E2 | Evaporator sensor fault | Check coil probe location and resistance |
| HA | High temperature alarm | Check box temp, airflow, and refrigerant system |
| LA | Low temperature alarm | Check setpoint and sensor calibration |
| dEF | Defrost fault / defrost overdue | Check heaters, termination probe, and timer settings |
| DO | Door open alarm | Check door switch and wiring |
| Com | Communication fault | Check network cable and addressing |

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
| Room probe | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-rx-controller-fault&k=Room+probe&tag=errorcodefixes-20) \| Replace on E1 alarms |
| Evaporator probe | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-rx-controller-fault&k=Evaporator+probe&tag=errorcodefixes-20) \| Replace on E2 or defrost alarms |
| Defrost heater | [Amazon](https://www.amazon.com/dp/B07FVP4CY6?ascsubtag=ecf-danfoss-rx-controller-fault&tag=errorcodefixes-20) \| Replace if open on ohm check |
| Door switch | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-rx-controller-fault&k=Door+switch&tag=errorcodefixes-20) \| Replace on repeated DO alarms |
## Jump to Fix

- **E1** → Check probe connection → Measure resistance → Replace sensor
- **E2** → Check probe placement → Measure resistance → Replace sensor
- **dEF** → Force defrost → Check heater or hot gas → Check termination sensor

## When to Call a Pro
If the controller alarms after sensor replacement, the real problem may be refrigerant flow, hot gas piping, or a failed solenoid. A refrigeration technician should check the full system.

## See Also

- [Danfoss FC-302 Alarm 13 — DC Link Overvoltage Fix](/posts/danfoss-fc302-alarm-13/)
- [Danfoss VFD Fault W30 — Brake Resistor Overtemperature Fix](/posts/danfoss-vfd-fault-w30/)
- [Danfoss VFD Fault OL — Causes & Fix](/posts/danfoss-vfd-fault-ol/)
- [Danfoss FC102 VLT HVAC Drive Fault Codes — Complete Diagnostic Reference](/posts/danfoss-fc102-fault-codes/)
