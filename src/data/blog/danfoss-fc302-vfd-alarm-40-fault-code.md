---
title: "Danfoss FC302 Alarm 40 - Causes & Fix"
description: "Alarm 40 on a Danfoss FC302 is a digital output overload on terminal 27. Check for shorts or excessive load on that terminal."
pubDatetime: 2026-06-03T10:48:37Z
modDatetime: 2026-06-03T10:48:37Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - danfoss
---

## Danfoss FC302 Alarm 40 — What It Means

Alarm 40 on a Danfoss FC302 VFD means overload of digital output terminal 27. The drive has detected that terminal 27 is sourcing or sinking more current than allowed, or the connected circuit is effectively shorted. This fault is tied to parameters 5-00 (Digital I/O Mode) and 5-01 (Terminal 27 Mode). The drive is protecting itself from damage to the output stage.

This is not a motor earth fault or a power-stage problem. It is strictly a digital I/O issue on terminal 27. The fault points to either external wiring or device problems connected to that terminal, or incorrect configuration of how the terminal is being used. In most cases, the issue is in the field wiring or the connected load, not inside the drive itself.

[Jump to Fix](#fix)

## Common Causes

- **Short circuit on terminal 27 wiring** A direct short in the wiring connected to terminal 27 will overload the output and trigger Alarm 40.
- **Excessive current draw from connected device** A device wired to terminal 27 that draws more current than the output can supply will cause the overload fault.
- **Incorrect parameter 5-00 or 5-01 configuration** The terminal mode settings do not match the external load or application, causing the output to operate outside its limits.
- **Damaged or pinched field wiring** Physical damage to the conductors connected to terminal 27 can create a short or fault condition.
- **Failed external relay or input device** An external component on the terminal 27 circuit that has internally shorted will overload the output.
- **Defective control card or I/O section** If the fault persists with terminal 27 unloaded and wiring removed, the drive's control card or output stage may be damaged.

## Step-by-Step Fix {#fix}

1. **Disconnect power to the drive** and wait for stored energy to discharge before working on any terminals.
2. **Remove the wiring and load from terminal 27** completely. Restore power and check if Alarm 40 clears.
3. **Inspect the removed wiring and external device** for shorts, pinched conductors, incorrect terminations, or signs of internal failure in the connected load.
4. **Check parameter 5-00 (Digital I/O Mode)** and parameter 5-01 (Terminal 27 Mode) in the drive menu. Verify both settings match the intended function and external circuit requirements for terminal 27.
5. **Reconnect the wiring to terminal 27** after repairs or verification. Power up the drive and test for normal operation without the alarm.
6. **Cycle power to the drive** if Alarm 40 persists with terminal 27 unloaded. If the alarm returns with no external load, the control card or I/O section may be defective.
7. **Replace the control card or contact Danfoss** if the fault remains after all external causes are ruled out and terminal 27 is disconnected.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Field wiring for terminal 27 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-40-fault-code&k=Field+wiring+for+terminal+27&tag=errorcodefixes-20) \| Replace if conductors are shorted, pinched, or damaged. |
| External relay or device connected to terminal 27 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-40-fault-code&k=External+relay+or+device+connected+to+terminal+27&tag=errorcodefixes-20) \| Replace if the connected load is internally shorted or draws excessive current. |
| Danfoss FC302 control card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-40-fault-code&k=Danfoss+FC302+control+card&tag=errorcodefixes-20) \| Required if Alarm 40 persists with terminal 27 unloaded and after power cycle. Consult Danfoss for part number specific to your drive model. |

## When to Call a Pro

Call a qualified technician or controls specialist if you are not comfortable working with VFD wiring or digital I/O circuits. If Alarm 40 continues after you have removed and checked all external wiring and loads on terminal 27, and the fault returns after a power cycle with nothing connected, the control card is likely defective and requires factory replacement or repair. VFD repairs involving internal boards should be done by trained personnel to avoid voiding warranties or creating safety hazards.

## See Also

- [Danfoss FC302 ALARM 35 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-35-fault-code/)
- [Danfoss FC302 ALARM 35 - Causes & Fix](/posts/danfoss-fc302-alarm-35-fault-code/)
- [Danfoss FC302 VFD ALARM 57 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-57-fault-code/)
- [Danfoss RX Controller Fault Codes — Troubleshooting Guide](/posts/danfoss-rx-controller-fault/)
