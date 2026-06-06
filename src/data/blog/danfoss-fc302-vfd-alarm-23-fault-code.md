---
title: "Danfoss FC302 VFD Alarm 23 - Causes & Fix"
description: "Alarm 23 means the internal cooling fan is not running or has failed. Check the fan, wiring, soft-charge fuses, and control card."
pubDatetime: 2026-06-02T10:47:05Z
modDatetime: 2026-06-02T10:47:05Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - danfoss
---

## Danfoss FC302 VFD Alarm 23 — What It Means

Alarm 23 (or Warning 23) on a Danfoss VLT AutomationDrive FC 302 indicates an internal fan fault. The drive's fan-monitoring function has detected that the internal cooling fan is not running, is not mounted correctly, or its monitoring circuit has reported a problem. This is an extra protective function that checks whether the fan is functioning properly and installed as required. The alarm is tied to the drive's internal cooling system, not the motor or load side. If the fan cannot cool the drive electronics, the VFD may overheat and shut down to protect itself.

[Jump to Fix](#fix)

## Common Causes

- **Failed internal fan or worn bearings** The cooling fan itself has failed mechanically or the fan bearings are worn out and the fan cannot spin.
- **Loose, disconnected, or damaged fan wiring** The fan connector is loose, the wiring to the fan is broken, or the connection has corroded or pulled apart.
- **Defective soft-charge fuses** One or more soft-charge fuses affecting the fan supply path have blown or failed, cutting power to the fan circuit.
- **Defective control card** The control card or its fan-monitoring circuit is defective, even if the fan itself is working correctly.
- **Defective or poorly seated option card** If an option card is installed, it may be defective or not seated properly, interfering with the fan monitoring circuit.

## Step-by-Step Fix {#fix}

1. **Power down safely** and follow lockout/tagout procedures before opening the drive enclosure to prevent shock or arc flash.
2. **Inspect the fan physically** by confirming it is installed correctly, the mounting is secure, no obstructions block the blades, and the fan rotor can rotate freely by hand.
3. **Check the fan resistance** according to the Danfoss procedure for Warning 23 (consult your model's documentation for the expected resistance value).
4. **Check the soft-charge fuses** for continuity and replace any that have blown or show signs of failure.
5. **Verify 24 V DC supply power** if your drive configuration uses a 24 V DC circuit associated with the fan monitoring function.
6. **Check the control card** for visible damage, corrosion, or defect if the fan and fuses check out but the alarm persists.
7. **Check the option card** (if fitted) for proper seating in its connector and for any signs of defect or damage, and reseat or replace if necessary.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 internal fan assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-23-fault-code&k=Danfoss+FC302+internal+fan+assembly&tag=errorcodefixes-20) \| Replacement cooling fan for your FC302 frame size |
| Danfoss FC302 control card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-23-fault-code&k=Danfoss+FC302+control+card&tag=errorcodefixes-20) \| Main control PCB if fan monitoring circuit is defective |
| Danfoss soft-charge fuse | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-23-fault-code&k=Danfoss+soft-charge+fuse&tag=errorcodefixes-20) \| Check your drive's parts list for correct fuse rating |

## When to Call a Pro

Call a qualified drives technician or an electrical contractor with VFD experience if you are not trained in high-voltage electrical work or if the alarm persists after replacing the fan and fuses. Working inside a VFD involves potentially lethal DC bus voltages that can remain even after mains power is disconnected. If the control card or option card needs replacement, a technician can also verify proper configuration and parameter settings after the repair.

## See Also

- [Danfoss FC302 Alarm 20 - Causes & Fix](/posts/danfoss-fc302-alarm-20-fault-code/)
- [Danfoss FC302 VFD Alarm 46 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-46-fault-code/)
- [Danfoss FC302 Alarm 24 - Causes & Fix](/posts/danfoss-fc302-alarm-24-fault-code/)
- [Danfoss FC302 Alarm 49 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-49-fault-code/)
