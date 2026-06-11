---
title: "Danfoss FC302 ALARM 35 - Causes & Fix"
description: "ALARM 35 on a Danfoss FC302 VFD signals an option module fault. Most often fixed by reseating or replacing the option card."
pubDatetime: 2026-06-04T09:11:50Z
modDatetime: 2026-06-04T09:11:50Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC 302 option card or module"
---

## Danfoss FC302 ALARM 35 — What It Means

ALARM 35 on a Danfoss VLT AutomationDrive FC 302 means an option fault. The drive has detected a problem with an installed option module or an option-related communication or power-up condition. Danfoss states this alarm is option-specific, meaning it points to a particular option card or module that did not initialize correctly, lost communication, or failed during startup. It does not indicate a general motor, power supply, or mains fault. The most common causes are poor option card seating, a power-up handshake failure between the control card and the option, or a communication fault between the option and its external network or device.

[Jump to Fix](#fix)

## Common Causes

- **Option card not seated correctly** The installed option module has loose board edge connectors, bent pins, or is not fully engaged in the slot after installation or service.
- **Power-up fault on the option** The drive does not successfully initialize the option during startup, often due to a handshake failure or incompatible hardware or firmware combination.
- **Communication fault between control card and option** Loose wiring, damaged cable, poor shield termination, or a broken communication path between the drive's control card and the option module.
- **Incorrect or incompatible option for the drive model** The option card installed is not designed for this FC 302 model or is running firmware incompatible with the drive.
- **Failed option board or module** The option card itself is defective and cannot communicate or power up correctly, even when properly seated and wired.

## Step-by-Step Fix {#fix}

1. **Power down and lock out** the FC 302 drive, wait for all DC bus capacitors to discharge, and verify zero voltage at the motor terminals and control circuits.
2. **Identify which option card or module** is installed in the drive by inspecting the option slots and noting the model number, and check the LCP display for any additional alarm context or option-specific fault text.
3. **Inspect and reseat the option module** by removing it from the slot, checking for bent pins or contamination on the board edge connector, and reinstalling it firmly until all retaining clips or screws are fully engaged.
4. **Check all option wiring and communication cables** for loose terminals, damaged insulation, broken shield connections, and correct termination, and verify any external power supply connections if the option requires separate DC or AC power.
5. **Cycle power to the drive** and observe the startup sequence to see whether the alarm returns during initialization, because Danfoss identifies power-up faults as a leading cause of ALARM 35.
6. **Remove the option temporarily** (if the application permits) and start the drive without the option installed to confirm whether the fault is isolated to the option or to the drive's control card.
7. **Replace the option card** if reseating, wiring checks, and power-cycle tests do not clear the fault, or replace the control card if Danfoss-style isolation testing shows the control side is defective rather than the option itself.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC 302 option card or module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-35-fault-code&k=Danfoss+FC+302+option+card+or+module&tag=errorcodefixes-20) \| Match the exact option type and part number to your drive model and application, such as fieldbus, I/O, or encoder modules. |
| Danfoss FC 302 control card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-35-fault-code&k=Danfoss+FC+302+control+card&tag=errorcodefixes-20) \| Replace only if diagnostic isolation confirms the control card side is at fault rather than the option module. |
| Option communication cable and connectors | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-35-fault-code&k=Option+communication+cable+and+connectors&tag=errorcodefixes-20) \| Use shielded cable and connectors rated for your option's protocol if external communication wiring is damaged or missing. |

## When to Call a Pro

Call a qualified VFD technician or Danfoss-certified service partner if you are not trained in safe high-voltage lockout, option module installation, or industrial drive diagnostics. A professional can perform Danfoss-specific isolation tests, verify firmware compatibility between the drive and the option, and safely handle control card replacement or advanced communication troubleshooting. Always call for support if the alarm persists after reseating and wiring checks, or if your application requires continuous uptime and you cannot afford trial-and-error part replacement.

## See Also

- [Danfoss FC302 ALARM 22 - Causes & Fix](/posts/danfoss-fc302-alarm-22-fault-code/)
- [Danfoss FC302 ALARM 33 - Causes & Fix](/posts/danfoss-fc302-alarm-33-fault-code/)
- [Danfoss VFD Fault UL — Causes & Fix](/posts/danfoss-vfd-fault-ul/)
- [Danfoss AKC Controller Fault Codes - Complete Guide](/posts/danfoss-akc-controller-fault/)
