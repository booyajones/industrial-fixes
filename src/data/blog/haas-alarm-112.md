---
title: "Haas Alarm 112 — Motor Overtemp"
description: "What Haas CNC alarm 112 means, why a servo motor overtemperature occurs, and how to diagnose and fix it."
pubDatetime: 2026-04-22T11:00:00Z
modDatetime: 2026-04-22T11:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - cnc
  - haas
---

## Haas Alarm 112 — What It Means

Haas alarm 112 indicates that a servo motor has exceeded its temperature limit. The servo motor contains an embedded thermistor (thermal sensor) in the motor windings. When winding temperature exceeds the protection threshold — typically 150°C — the servo drive reads the thermistor signal and triggers alarm 112 to prevent motor winding insulation breakdown. The machine stops all motion and will not restart until the motor cools and the alarm is cleared.

[Jump to Fix](#fix)

## Common Causes

- **Mechanical overload on the axis** — A tight ball screw, binding linear guide, excessive friction, or a programmed feed rate that overworks the motor forces the motor to continuously draw high current, generating excessive heat.
- **Aggressive duty cycle** — A program with continuous rapid traverse moves, very short cycle times, or repeated high-acceleration sequences keeps the motor at high current draw without adequate cooling intervals.
- **Motor cooling obstruction** — The motor cooling fan (if equipped) is blocked, or the motor body is enclosed in a way that prevents convective cooling.
- **Failed thermistor** — The thermistor embedded in the motor windings has drifted out of spec or failed, causing the control to read a false over-temperature signal even when the motor is cool.

## Step-by-Step Fix {#fix}

1. **Allow the motor to cool** — With the machine in an alarm state, wait 20–30 minutes with the servo drives de-energized. The motor will cool by convection. Do not restart until the motor is cooler to the touch.
2. **Inspect for mechanical binding** — With power off and servo drives de-energized, manually push the affected axis. Check for excessive friction, tight spots, or unusual resistance. Inspect the ball screw, linear guides, and way covers for damage or contamination.
3. **Lubricate linear guides and ball screw** — Verify that the axis lubrication system is functioning and that the way lube oil reservoir is filled. Dry guides dramatically increase friction and motor load.
4. **Review the machining program** — Check the program for aggressive feed rates, rapid traverse moves in constrained spaces, or duty cycles that do not allow motor cooling time between passes.
5. **Check the thermistor** — Measure the thermistor resistance at the servo drive connector (motor cool). Compare to the expected cold resistance from the Haas service manual. An open or very low reading confirms a failed thermistor.
6. **Verify motor airflow** — Confirm the motor body has adequate space around it for air circulation. Check that motor fan covers are not blocked by chips, coolant hose routing, or enclosure panels.
7. **Reset the alarm and test** — After the motor has cooled, reset alarm 112 and run the axis at reduced feed rate. Monitor motor temperature in the Haas diagnostic screens if available.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Servo motor thermistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-haas-alarm-112&k=Servo+motor+thermistor&tag=errorcodefixes-20) \| OEM Haas part; replacement requires motor disassembly |
| Servo motor (complete) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-haas-alarm-112&k=Servo+motor+%28complete%29&tag=errorcodefixes-20) \| Replace if windings are damaged from repeated overtemperature events |
| Way lube pump / distributor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-haas-alarm-112&k=Way+lube+pump+%2F+distributor&tag=errorcodefixes-20) \| Replace if lubrication system is not delivering oil to guides |
| Ball screw support bearing | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-haas-alarm-112&k=Ball+screw+support+bearing&tag=errorcodefixes-20) \| Replace if ball screw is binding due to bearing failure |
## When to Call a Pro

Motor winding damage from repeated overtemperature events, and servo motor replacement, should be handled by a Haas Factory Outlet (HFO) service technician. Thermistor replacement requires motor disassembly and should be done with the correct motor parameters re-entered into the drive.

## Related Articles

- [Haas CNC Alarm 101 — Emergency Stop Active Fix](/posts/haas-alarm-101-emergency-stop/)
- [Haas Alarm 102 — Servo Drive Fault Fix](/posts/haas-alarm-102/)
- [Haas Alarm 103 — Servo Overload Fix](/posts/haas-alarm-103/)
- [Haas Alarm 104 Feed Hold — Causes & Fix](/posts/haas-alarm-104-feed-hold/)
- [Haas Alarm 105 E-Stop — Causes & Fix](/posts/haas-alarm-105/)

## See Also

- [Haas Alarm 131 — E-Stop Chain Fault Fix](/posts/haas-alarm-131/)
- [Haas Alarm 219 — X-Axis Servo Error Fix](/posts/haas-alarm-219/)
- [Haas Alarm 129: Spindle Orientation Error — Fix Guide](/posts/haas-alarm-129/)
- [Haas Alarm 122 — ATC Chain Fault](/posts/haas-alarm-122/)
