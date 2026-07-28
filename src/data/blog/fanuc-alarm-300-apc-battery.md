---
title: "Fanuc Alarm 300: APC Battery Low — Absolute Encoder Battery Fix"
description: "Fanuc Alarm 300 means the absolute encoder battery is low or dead. Replace the 3V lithium battery fast — a dead battery wipes home position and forces re-homing."
pubDatetime: 2026-04-26T17:30:00Z
modDatetime: 2026-04-26T17:30:00Z
author: "Dana Kowalski"
slug: fanuc-alarm-300-apc-battery
featured: false
draft: false
tags:
  - fanuc
  - cnc
  - alarm-code
  - encoder
  - industrial-maintenance
---

## Fanuc Alarm 300: What It Means

**Fanuc Alarm 300** is an **APC (Absolute Pulse Coder) alarm** — specifically, the absolute encoder battery is low or dead. The full alarm text typically appears as **"300 APC ALARM: n AXIS BATTERY"** where n is the affected axis number.

Fanuc's absolute encoders remember the motor's position even when the machine is powered off. They do this by running a tiny internal circuit from a dedicated 3V lithium battery. When that battery drops below threshold — typically around 2.8V — the control throws alarm 300 to warn you. The encoder can still hold position for a short time, but the battery is dying.

**This is the most time-sensitive Fanuc alarm you will see.** Here is why: if the battery dies completely before you replace it, the absolute encoder loses all position data. The machine no longer knows where any axis is. You will see a **"304 APC ALARM: n AXIS ZERO POINT"** or similar, and the machine must be **manually re-homed** to re-establish the reference position before it can run production parts. On complex multi-axis machining centers, that re-homing process can take hours and requires a skilled operator or maintenance technician.

The moment Alarm 300 appears, treat it as urgent. The battery costs $5–$15. Losing home position can cost hours of downtime.

## Common Causes

- **Battery natural end of life.** Fanuc recommends replacing the APC battery every 2–3 years. Most shops do not have a preventive maintenance schedule for it, so the first sign of a problem is alarm 300.
- **Machine left unpowered for an extended period.** The battery drains faster when the machine is off. Machines stored during shutdowns, plant moves, or extended idle periods often wake up with a dead or dying battery.
- **High-temperature environment.** Batteries drain faster in hot electrical cabinets or near heat sources. A battery that should last 3 years in a climate-controlled environment may last 18 months in a hot shop.
- **Battery holder corrosion.** On older machines, the battery contact springs can corrode and create intermittent or high-resistance connections that drain the battery.
- **Multiple axes on one battery.** Some Fanuc configurations run several encoder batteries from a shared pack. If one axis trips alarm 300, all connected axes are at risk.

## Step-by-Step Diagnosis {#fix}

1. **Do not power off the machine if at all possible.** While the machine is powered on, the encoder draws power from the main 24VDC supply rather than the battery. Replacing the battery with the machine on is safe and preserves the absolute position data. Check your machine's maintenance manual to confirm this applies to your specific Fanuc series.

2. **Identify which axis is affected.** The alarm text will say "n AXIS BATTERY" — note the axis number. On most machines, each axis has its own battery in the drive cabinet or in a battery holder near the encoder.

3. **Locate the battery.** On most Fanuc Series 0, 16, 18, 21, 30i, 31i, and 32i systems, the encoder batteries are located in the servo amplifier cabinet. Look for a battery pack holder on the amplifier unit or a standalone battery box. The battery is typically a **3.0V lithium, size A or 2/3A**, such as an ER3V, CR17335, or A98L-0031-0025.

4. **Read the battery voltage before replacement.** A new battery reads 3.0–3.6V. Alarm 300 typically triggers below 2.8V. Use a multimeter to confirm you have the right battery to replace.

5. **Replace the battery with machine power ON when possible.** Insert the new battery, confirm it seats fully in the holder, then clear the alarm. If you must power off to replace it, do so with the machine in a safe, parked position and be prepared to re-home immediately after power-on.

6. **Clear the alarm and verify.** After replacement, clear the alarm from the MDI panel. Cycle power if required. The alarm should not return.

7. **Check position data is intact.** After restart, jog each axis and verify the machine's position display matches the known physical position. If position data was lost, a re-homing or reference point return procedure is required.

## How to Fix It

**Standard battery replacement (machine powered on):**
Locate the battery holder, note which battery type is installed, swap in the new battery, and clear the alarm. Done. This is a 5-minute job and costs under $15. Always keep a spare on the shelf.

**If position was already lost (Alarm 304 or axis position error after power-on):**
The machine must be re-referenced. This process varies by machine and Fanuc series, but generally involves:
1. Releasing the E-stop and resetting all alarms.
2. Using the reference point return (ZRN) function on each affected axis.
3. Jogging the axis toward its reference switch until the machine re-establishes the home position.

On complex machines with pallet systems, tool changers, or fixture offsets tied to absolute position, re-homing must be done carefully and verified before running any part. Involve the machine builder or a Fanuc-trained technician if you are uncertain.

**Preventive maintenance going forward:** Add a battery replacement task to your PM schedule — every 2 years is a safe interval for most Fanuc systems. Write the replacement date on the battery with a marker. Stock at least two spare batteries per machine.

## Parts You May Need

- [Fanuc encoder battery ER3V 3.6V lithium](https://www.amazon.com/s?ascsubtag=ecf-fanuc-alarm-300-apc-battery&k=Fanuc+encoder+battery+ER3V+3.6V&tag=errorcodefixes-20)
- [A98L-0031-0025 Fanuc battery replacement](https://www.amazon.com/s?ascsubtag=ecf-fanuc-alarm-300-apc-battery&k=A98L-0031-0025+Fanuc+battery&tag=errorcodefixes-20)
- [CR17335 3V lithium battery for CNC encoder](https://www.amazon.com/s?ascsubtag=ecf-fanuc-alarm-300-apc-battery&k=CR17335+3V+lithium+battery+CNC&tag=errorcodefixes-20)
- [Digital multimeter for battery voltage check](https://www.amazon.com/dp/B08ZJSN5X3?ascsubtag=ecf-fanuc-alarm-300-apc-battery&tag=errorcodefixes-20)

## When to Call a Technician

Call a Fanuc-certified technician if position data was lost and you are not confident in the re-homing procedure for your machine. An incorrect reference point on a machining center can result in a crash on the first program run. On high-precision machines or systems with complex fixture offsets, having a technician verify the re-homed position against a calibrated reference is worth the service call.

## Related Error Codes

- [Fanuc Alarm 414: Servo Alarm Axis Detect Error](/posts/fanuc-alarm-414/)
- [Fanuc Alarm 401: Servo Alarm V-Ready Off](/posts/fanuc-alarm-401/)
- [Fanuc Complete CNC Alarm Code Reference](/posts/fanuc-alarm-codes/)
