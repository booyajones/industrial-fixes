---
title: "Mazak Alarm 600 ATC — Automatic Tool Changer Fault Causes & Fix"
description: "What Mazak alarm 600 ATC means, why the automatic tool changer faults, and how to fix it step by step."
pubDatetime: 2026-04-22T15:00:00Z
modDatetime: 2026-04-22T15:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - cnc
  - mazak
money_part: "ATC proximity switch"
most_likely_cause: "ATC arm did not complete a phase within timeout"
---

## What this code means
Alarm 600 (ATC Alarm) on a Mazak CNC machining center (Nexus, Variaxis, Integrex series) indicates a fault in the Automatic Tool Changer system. The ATC is responsible for swapping tools between the magazine/drum and the spindle; a position, timing, or interlock fault during any phase of the tool change cycle triggers alarm 600. The CNC immediately halts all motion and requires the operator to investigate and clear the ATC fault before machining can resume. Because the ATC is a complex mechanical-pneumatic system, alarm 600 can have many sub-causes depending on which phase of the tool change failed.

## Common Causes

- **ATC arm did not complete a phase within timeout** — The ATC arm (swing arm or carousel) failed to reach its commanded position within the expected time. This can be caused by a jammed tool, a worn proximity switch, or low air pressure.
- **Proximity/limit switch failure** — The ATC's position sensing relies on multiple proximity switches that confirm each phase of the change cycle. A failed or misaligned switch causes the controller to wait indefinitely and eventually time out with alarm 600.
- **Low air pressure to ATC pneumatic actuators** — Many Mazak ATC mechanisms use pneumatic actuators for arm engagement and tool retention. Low shop air pressure or a faulty pressure regulator can prevent full actuation.
- **Tool retention / retention knob problem** — A missing or incorrect retention knob (pull stud), a damaged tool holder, or a contaminated pot in the magazine can cause the arm to fail to grip or release a tool.
- **ATC arm mechanical jam or collision** — A chip or chip-encrusted tool lodged in the ATC path, or a tool holder that has come loose, can physically prevent the arm from completing its travel.

## Step-by-Step Fix {#fix}

1. **Do not force or manually move the ATC arm** — Alarm 600 locks out the ATC. Do not attempt to manually cycle the arm until the CNC indicates it is safe. Consult the Mazak maintenance manual for the safe manual recovery procedure.
2. **Identify the ATC phase from the sub-alarm or diagnosis screen** — Mazak Mazatrol and Fusion CNC controls show a sub-alarm or diagnostic status alongside alarm 600. This sub-code identifies exactly which phase of the tool change failed.
3. **Inspect for physical obstruction** — Visually inspect the ATC arm and magazine for jammed tools, mis-seated holders, or foreign objects.
4. **Check air pressure** — Verify shop air is within the required range for the Mazak model (typically 80–100 PSI). Check the ATC-specific pressure regulator and filter.
5. **Inspect proximity switches** — Identify the switch associated with the failed phase (from the diagnostic screen). Verify the switch face is clean and the cam or target is within the specified sensing distance. Swap the switch if suspect.
6. **Check tool holder retention** — Verify all tools in the magazine have the correct retention knob (pull stud) for the machine's spindle taper, and that no holders are damaged.
7. **Execute the manual recovery procedure** — Follow the Mazak manual recovery procedure (typically in Maintenance mode) to return the ATC to a safe home position before resetting alarm 600.

## Parts Often Needed

| Part | Notes |
|------|-------|
| ATC proximity switch | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mazak-alarm-600-atc&k=ATC+proximity+switch&tag=errorcodefixes-20) \| Match the Mazak machine model and switch thread/body size |
| Retention knob (pull stud) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mazak-alarm-600-atc&k=Retention+knob+%28pull+stud%29&tag=errorcodefixes-20) \| Must match the spindle taper (CAT40, BT40, HSK-A63, etc.) |
| ATC pneumatic solenoid valve | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mazak-alarm-600-atc&k=ATC+pneumatic+solenoid+valve&tag=errorcodefixes-20) \| Replace if actuator does not respond to commanded position |
## When to Call a Pro

Mazak ATC recovery after a mid-cycle jam — especially on swing-arm or double-arm changers — requires the machine's maintenance manual and often a Mazak service technician. An improper manual recovery can damage the spindle, the arm, or the magazine.
