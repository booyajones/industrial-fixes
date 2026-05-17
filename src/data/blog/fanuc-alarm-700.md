---
title: "Fanuc Alarm 700 — Causes & Fix"
description: "What Fanuc CNC alarm 700 means, why the spindle overheats, and how to diagnose and fix it."
pubDatetime: 2026-04-22T10:00:00Z
modDatetime: 2026-04-22T10:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - cnc
  - fanuc
---

## Fanuc Alarm 700 — What It Means

Alarm 700 on a Fanuc CNC (FS0i, FS16i, FS18i, FS21i, FS30i series) is a spindle overheat alarm. The spindle drive detected that the spindle motor temperature exceeded the threshold set in the spindle amplifier or the thermal sensor in the spindle motor reported an overtemperature condition. Fanuc 700-series alarms all relate to the spindle drive system; 700 specifically indicates motor overheat.

[Jump to Fix](#fix)

## Common Causes

- **Excessive spindle load or duty cycle** — Continuous heavy cuts without adequate dwell time cause the spindle motor to accumulate heat faster than it can dissipate.
- **Blocked or failed spindle motor cooling fan** — Most Fanuc spindle motors have an integral cooling fan (or separate blower) on the non-drive end. A seized fan or blocked duct stops airflow over the windings.
- **Spindle drive operating in ambient temperatures above rated** — If the control cabinet or the machine is in an ambient environment above 40°C (104°F), derating is required and overtemperature trips occur at lower loads.
- **Failing motor thermistor** — The thermistor embedded in the spindle motor windings can drift high and report overtemperature when actual winding temperature is normal.
- **Worn spindle bearings** — Preloaded or worn bearings increase mechanical friction, adding heat to the spindle motor at any speed.

## Step-by-Step Fix {#fix}

1. **Check the spindle motor cooling** — With the machine powered and the spindle stationary, confirm the cooling fan on the spindle motor is running. Listen for airflow and visually confirm the fan blade is spinning. Check the fan duct for debris blockage.
2. **Allow the spindle to cool** — Alarm 700 will not clear until the motor thermistor cools below the reset threshold. Allow 20–30 minutes with the spindle idle (and cooling fan running) before attempting to reset.
3. **Test the spindle thermistor** — Access the thermistor wiring at the spindle drive amplifier (THR terminals). With the spindle at room temperature, measure resistance. Fanuc spindle motors typically use 120Ω thermistors at ambient; values significantly higher indicate a drifting thermistor. Refer to the Fanuc spindle motor parameter manual for the specific motor type.
4. **Review spindle duty cycle and cutting parameters** — Reduce the depth of cut, feedrate, or continuous run time to lower the thermal load on the motor. Allow dwell time between heavy cuts.
5. **Check spindle bearings** — At low RPM (300–500), monitor spindle motor current. Elevated current at low speed indicates bearing drag. Bearing replacement is a machine shop task.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Spindle motor cooling fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-alarm-700&k=Spindle+motor+cooling+fan&tag=errorcodefixes-20) \| Match motor frame size and voltage; Fanuc OEM or equivalent |
| Motor thermistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-alarm-700&k=Motor+thermistor&tag=errorcodefixes-20) \| Fanuc OEM; 120Ω PTC type; match motor model |
| Spindle bearings | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-alarm-700&k=Spindle+bearings&tag=errorcodefixes-20) \| Matched pair; angular contact; require precision installation |
## When to Call a Pro

Spindle bearing replacement requires precision preload setting and alignment and should be performed by a qualified machine tool technician or Fanuc-authorized service engineer. Improper bearing installation causes rapid bearing failure and spindle damage.

## Related Articles

- [Fanuc 0i-MD Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-0i-md-alarm-codes/)
- [Fanuc 30i/31i/32i Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-30i-alarm-codes/)
- [Fanuc Alarm 1 Overtravel — Causes & Fix](/posts/fanuc-alarm-1-overtravel/)
- [Fanuc Alarm 10 Servo Alarm — Causes & Fix](/posts/fanuc-alarm-10-servo-alarm/)
- [Fanuc Alarm 2 — Overtravel Plus Causes & Fix](/posts/fanuc-alarm-2-overtravel/)
