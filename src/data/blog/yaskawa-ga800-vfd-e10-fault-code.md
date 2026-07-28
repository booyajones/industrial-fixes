---
title: "Yaskawa GA800 E10 Fault - Causes & Fix"
description: "E10 on Yaskawa GA800 means external fault input active. Check interlock wiring, overload relays, and external safety contacts."
pubDatetime: 2026-06-04T09:26:55Z
modDatetime: 2026-06-04T09:26:55Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Motor overload relay"
most_likely_cause: "Open external interlock or safety contact"
---

## What this code means
E10 on a Yaskawa GA800 VFD indicates an external fault input has been triggered. This is not an internal drive hardware failure. Instead, the drive has detected an open contact or active signal from an external protective device or interlock circuit, causing it to shut down. The fault comes from outside the VFD itself, such as a motor overload relay, pressure switch, thermal protector, safety relay, or other customer-supplied protective equipment in the control circuit.

The GA800 is responding to a condition in your external wiring or a device telling it to stop, not reporting a problem with its own power section or control boards. Diagnosis starts with the machine schematic and the external input chain, not the drive internals. You need to identify which external device or wiring issue opened the fault input circuit and restore normal operating conditions before clearing the fault.

## Common Causes

- **Open external interlock or safety contact** A pressure switch, flow switch, overload relay auxiliary contact, thermal protector, or safety relay in the stop chain has opened and is actively tripping the drive.
- **Loose or broken control wiring** Control circuit wiring to the external fault input terminal is disconnected, broken, or poorly terminated, creating an open circuit the drive reads as a fault.
- **Failed external protective device** The motor overload relay, process switch, or other protective device in the fault input chain is defective and falsely signaling a trip condition.
- **Incorrect parameter or wiring configuration** The external fault input terminal is wired or programmed incorrectly, causing the drive to misinterpret the control signal and register a false trip.
- **Option card or communication fault path** If an option card or networked control is used, a communication condition or poor card connection can activate the external fault input logic.

## Step-by-Step Fix {#fix}

1. **Obtain the machine schematic and terminal plan** to identify which external devices are wired into the GA800 fault input circuit and where they are physically located.
2. **Inspect all external protective devices** one by one, including motor overload relay contacts, pressure switches, flow switches, thermal protectors, and safety relay contacts, to determine if any have tripped or opened.
3. **Check control circuit wiring and terminal connections** at the drive's external fault input terminals for loose screws, broken wires, open circuits, or missing control voltage.
4. **Verify drive parameter settings** match the intended control method and confirm the external fault input is configured correctly for your wiring scheme and logic type.
5. **Reseat option cards and inspect connectors** if the E10 is part of a networked or option-based control system, checking for bent pins or poor contact.
6. **Restore the external trip circuit to normal** by correcting the open contact, repairing wiring, or resetting the protective device, then clear the E10 fault from the drive keypad or control interface.
7. **Test-run the system** and monitor for fault recurrence. If E10 returns immediately with all external wiring and devices proven good, suspect a drive input board issue or contact Yaskawa technical support for board-level diagnostics.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor overload relay | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e10-fault-code&k=Motor+overload+relay&tag=errorcodefixes-20) \| Replace if contacts are burned, stuck open, or mechanically failed after tripping. |
| Pressure or flow switch | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e10-fault-code&k=Pressure+or+flow+switch&tag=errorcodefixes-20) \| Replace if defective or falsely tripping the external fault input. |
| Control wiring and terminal blocks | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e10-fault-code&k=Control+wiring+and+terminal+blocks&tag=errorcodefixes-20) \| Replace damaged conductors or terminals in the external fault input circuit. |
| GA800 option card or I/O board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e10-fault-code&k=GA800+option+card+or+I%2FO+board&tag=errorcodefixes-20) \| Only if all external devices check good and fault persists after reseating. Consult Yaskawa support for part number. |

## When to Call a Pro

Call a qualified electrician or controls technician if you are not trained to read machine schematics, trace control circuits, or work safely with industrial control voltage. If you have verified all external wiring, contacts, and protective devices are in good condition and the E10 fault returns immediately after clearing, the issue may be in the drive's input board or require factory-level diagnostics. Contact Yaskawa technical support or an authorized service center for board replacement and advanced troubleshooting. Do not attempt to bypass safety interlocks or jumper the external fault input to clear the code, as this can create a hazardous operating condition.
