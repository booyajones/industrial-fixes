---
title: "Sullair Compressor Fault Codes: Supervisor & VSD Guide"
description: "Sullair rotary screw fault codes for the Supervisor controller and VSD drive: numeric Drive Fault codes, named alarms, causes, and real fixes."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - compressor
  - sullair
  - industrial
money_part: "Air/oil separator element"
---

## Sullair Compressor Fault Codes - Quick Reference

Sullair rotary screw compressors use the Supervisor and Touch Panel controllers to display warning and shutdown alarms. Codes vary by model (S-Series, 900/1150 HH, ShopTek), but these are the most common alarm families.

| Fault | Meaning | Quick Fix |
|-------|---------|-----------|
| High Discharge Temperature | Outlet air/oil temp exceeds limit | Check coolers, oil level, ambient temp |
| Low Oil Pressure | Lubrication fault | Check oil level, filter, pump |
| High Oil Temperature | Oil overheating | Check oil cooler, oil quality |
| Motor Overload | Drive motor overcurrent | Check amps, voltage, load |
| E-Stop Active | Emergency stop tripped | Reset E-stop, inspect circuit |
| Service Required | PM interval reached | Perform scheduled service |
| Separator Differential High | Oil separator restricted | Replace separator element |
| High Sump Pressure | Sump pressure relief or blowdown fault | Check minimum pressure valve |
| Sensor Fault | Temp or pressure sensor out of range | Check wiring and sensor |
| Blowdown Fault | Blowdown valve not opening | Inspect blowdown valve |

## Most Common Faults

### High Discharge Temperature
The leading cause of Sullair shutdowns. Dirty oil cooler fins, low oil level, high ambient temperature, or a failed cooling fan all drive this fault. Start with cleaning the cooler with dry air blown against normal airflow. Check oil level when cool. Verify fan operation.

### Separator Differential High
A restricted oil separator causes high pressure drop and oil carryover into the discharge air. Replace the separator element at or before the rated service interval. On Sullair units this is typically 2,000–4,000 hours depending on model.

### Low Oil Pressure
Check the oil level first - if low, fill and reset. If oil level is correct, the oil filter may be bypassing or the scavenge line may be blocked. On older units, the oil pump pickup can become contaminated.

### Motor Overload
Verify incoming voltage balance on all three phases. Unbalanced voltage causes disproportionate current draw on one phase and will trip the overload even at normal load. Also check the inlet valve if the compressor loads too heavily on startup.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Air/oil separator element | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-sullair-compressor-fault-codes&k=Air%2Foil+separator+element&tag=errorcodefixes-20) \| Replace every 2,000–4,000 hours |
| Oil filter | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-sullair-compressor-fault-codes&k=Oil+filter&tag=errorcodefixes-20) \| Replace with separator service |
| Discharge temperature sensor | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-sullair-compressor-fault-codes&tag=errorcodefixes-20) \| Common on high-hour units |
| Inlet valve kit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-sullair-compressor-fault-codes&k=Inlet+valve+kit&tag=errorcodefixes-20) \| Common cause of motor overloads |
| Minimum pressure valve | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-sullair-compressor-fault-codes&k=Minimum+pressure+valve&tag=errorcodefixes-20) \| Fails open causing high sump pressure |
## When to Call a Pro
Repeated discharge temperature trips after cleaning, or loss of oil pressure with correct oil level, indicate internal airend wear or oil pump failure. These require disassembly and should be handled by a Sullair-trained technician.

## More Sullair Compressor fault codes

Compiled from manufacturer service manuals and authorized documentation.

| Code | What it means | Likely cause | How to fix |
| --- | --- | --- | --- |
| VSD Param Lim Fault | Supervisor-reported drive setup mismatch. | Incorrect model, HP, or voltage selected in Factory & VSD Setup. | Make the proper selections in the Factory & VSD Setup menus to match the drive rating. |
| VSD Com Error | The Supervisor lost communications with the VSD. | Broken connection to the VSD, loss of VSD control power, or a board fault. | Check the connections to the VSD, verify VSD control power, and check for board faults. |
| P3 Oil Pressure Low / dP3 Oil Pressure Low | Measured oil pressure is low. | Oil pump failure or clogged oil filter (the manual's listed causes for this alarm). | Replace the oil filter; if pressure is still low, consult the Sullair service department (possible oil pump failure). |
| P1 Sump Pressure High | Sump pressure is too high (poppet, Sullicon, spiral, blowdown, or pneumatic valve failed). | A control valve failed to open/vent, a solenoid valve issue, a misadjusted pressure regulator, or a stuck minimum-pressure check valve. | Check the valves and Sullicon adjustment, verify solenoid valve operation and wiring, check the pressure regulator adjustment, and inspect the minimum-pressure check valve. |
| Power Interruption | The Supervisor lost the expected starter/brownout signal at input D8. | Motor starter not working / no contact to input D8, or intermittent control power. | Check the starter controls and wiring, verify the wiring to the input, and check line voltage and connections. |
| Factory Setup Error | The Supervisor's factory setup information needs to be reviewed for correct values. | Corrupted or incorrect factory configuration data. | Review the factory setup values; if the problem persists, replace the Supervisor controller. |

## How to troubleshoot Sullair Compressor

## How to diagnose a Sullair rotary screw shutdown

**Read the actual message first, and know which controller you have.** Many Sullair units use the Supervisor controller (later units use a Touch Screen controller). The controller shows a named message (for example, T2 Discharge High or P1 Sump Pressure High) and separately shows numeric **Drive Fault** codes that come from the variable speed drive (VSD). A warning lets the machine keep running while a fault (shutdown) stops the machine until the condition clears. Before you touch anything, open the fault log; the Supervisor stores the last 16 faults, plus a sensor log of the readings leading up to a fault, which usually tells you whether the trip was temperature, pressure, or drive related.

**Work the most common failure modes in order.** Overheating trips (high discharge or oil temperature) are among the most frequent causes of Sullair shutdowns, so start there: check the coolant/fluid level when the unit is cool, clean the cooler fins and fan (blow dry air against normal airflow), confirm the thermal/thermostatic valve is working, and on water-cooled units verify water flow and temperature. For low oil pressure, check level and the oil filter before suspecting the pump. Rising separator differential (dP1) or oil carryover points to a plugged separator element. Repeated motor overloads warrant checking three-phase voltage balance and the inlet valve.

**Isolate drive faults from mechanical faults.** A numeric "Drive Fault xx" is reported by the VSD, not the airend. Plug a keypad service tool into the drive to read the fault name behind the number. Communication messages (VSD Com Error, VSD Com Fault, VSD Param Lim Fault) are wiring, control-power, or setup problems, not compressor damage, so check the bus cable, drive control power, and the model/HP/voltage setup selections first. Sensor Fail messages usually mean a failed sensor, loose connector, or corroded contact rather than a genuine over-limit condition.

**Safety and when to call a pro.** Always lock out and depressurize the sump before opening any pressurized component; a Sullair sump holds pressure even after shutdown. Confirm the emergency stop is released and its wiring is intact before assuming an electrical fault. Call a Sullair-trained technician when: high-temperature trips repeat after cleaning and correct fluid level (possible internal airend wear), oil pressure stays low with correct level and a fresh filter (possible oil pump failure), or the drive throws Saturation trip (Fault 7) or System fault (Fault 8), which the manual says may require leaving power off and contacting service. Internal airend, oil pump, and power-electronics work is not a field DIY repair.

## Frequently asked questions

### What does a numbered 'Drive Fault' mean on my Sullair Supervisor display?

It is a fault reported by the variable speed drive, shown by the Supervisor as 'Drive Fault' plus a code number. Plug a keypad service tool into the drive to see the fault name behind the number (for example, 1 = Overcurrent, 2 = Overvoltage, 3 = Ground/Earth Fault, 14 = Over-temperature). These are drive/electrical faults, not necessarily airend damage.

### Why does my Sullair keep tripping on high discharge or oil temperature?

It is one of the most common Sullair shutdowns. Check the coolant/fluid level when cool, clean the cooler fins and fan (blow dry air against normal airflow), verify the thermal valve operates, and confirm ambient is not above about 105F (41C) with poor ventilation. On water-cooled units, check for low water flow, high water temperature, or plugged cooler tubes.

### How do I clear a VSD Com Error or VSD Com Fault?

These mean the Supervisor lost communication with the drive, not that the compressor is damaged. Check the bus/control wiring and connectors to the VSD, verify the drive has control power, set the Supervisor VSD setting to 'Serial' if applicable, and look for board faults. If wiring and power are correct, contact Sullair service.

### What does P1 Sump Pressure High mean and how do I fix it?

Sump pressure is above limit, typically because a control valve failed to vent: the poppet, Sullicon, spiral, blowdown, or pneumatic valve. Check those valves and the Sullicon adjustment, verify solenoid valve operation and wiring, check the pressure regulator, and inspect the minimum pressure check valve.

### When should I replace the air/oil separator element?

Replace it when the separator differential (dP1 Separator High) climbs or you see oil carryover into the discharge air, and at or before the model's rated service interval. A restricted separator causes high pressure drop and oil in the air. Replacing the oil filter at the same time is good practice.
