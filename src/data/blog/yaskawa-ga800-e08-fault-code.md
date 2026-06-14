---
title: "Yaskawa GA800 E08 Fault Code - Causes & Fix"
description: "Yaskawa GA800 E08 (EF8) external fault on terminal S8. Learn the 4 most common wiring and input causes, plus 6 repair steps."
pubDatetime: 2026-05-30T12:24:57Z
modDatetime: 2026-05-30T12:24:57Z
author: "James Rutherford"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "GA800 control board"
most_likely_cause: "Open or broken wiring on S8"
---

## Yaskawa GA800 E08 Fault Code — What It Means

The GA800 E08 code (also labeled EF8 in some displays) indicates an external fault trip on MFDI terminal S8. This is not an internal drive failure. Instead, the drive has received a fault signal from an outside device or circuit connected to that terminal. The fault occurs when S8 is configured for external fault monitoring (typically through parameter H1-01 set to 2C through 2F) and the input sees an open or active trip condition. If S8 is wired to a safety interlock, emergency stop, or process sensor, any of those devices opening its contact will generate this fault and stop the drive.

Because this is an externally triggered event, the drive itself is usually not damaged. The task is to locate the device or wiring problem that is asserting the fault signal on S8, correct that condition, then clear the trip and restart.

[Jump to Fix](#fix)

## Common Causes

- **Open or broken wiring on S8** A loose, broken, or incorrectly landed wire at terminal S8 causes the input to float and register a fault condition even when no external device is actually tripping.
- **External safety or interlock device is open** An emergency stop button, door switch, temperature switch, or process sensor wired to S8 has opened its contact, sending the fault signal to the drive.
- **Parameter mismatch with unused terminal** Parameter H1-01 assigns S8 to external fault (2C to 2F) but the terminal is not actually connected to any device, leaving the input in an undefined or open state that the drive interprets as a fault.
- **Incorrect terminal function assignment** S8 is configured for external fault when it should be assigned to a different function, causing the drive to monitor a signal that was never intended as a fault input.

## Step-by-Step Fix {#fix}

1. {'lead': 'Record the displayed fault code and drive information', 'text': 'Write down the exact code shown (E08 or EF8), the drive model and serial number, and the application details, then reset the fault to see if it returns immediately or only under certain conditions.'}
2. {'lead': 'Inspect terminal S8 wiring and connections', 'text': 'Open the drive terminal cover and visually check S8 for loose conductors, incorrect wire landing, broken strands, or any sign of physical damage or poor contact.'}
3. {'lead': 'Trace the external fault circuit back to the source device', 'text': 'Follow the wire from S8 to the external interlock, safety relay, or sensor and verify that the device contact is closed and functioning correctly, then check for continuity through the entire circuit.'}
4. {'lead': 'Review parameter H1-01 and input function assignments', 'text': 'Access the drive parameters and confirm whether H1-01 is set to 2C through 2F (external fault on S8), then decide if that assignment matches your wiring and application intent.'}
5. {'lead': 'Remove or reassign S8 if the terminal is unused', 'text': 'If S8 is not connected to any external device, change the parameter assignment so the terminal is not configured for external fault, or jumper it to common through a closed contact if your control design requires the input to be active.'}
6. {'lead': 'Clear the fault and test drive operation', 'text': 'Once the wiring or parameter issue is corrected, reset the fault using the keypad or control input, then run the drive through a normal start cycle to verify the external fault does not return.'}
7. {'lead': 'Contact Yaskawa technical support if the fault persists', 'text': 'If the fault continues after wiring and parameter checks, gather the model number, serial number, fault code, application description, and time in service, then call Yaskawa support for further diagnosis.'}

## Parts Often Needed

| Part | Notes |
|------|-------|
| GA800 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-e08-fault-code&k=GA800+control+board&tag=errorcodefixes-20) \| Only required if the S8 input circuit itself is damaged after lightning strike or power surge, verify with Yaskawa before ordering. |
| External fault relay or interlock device | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-e08-fault-code&k=External+fault+relay+or+interlock+device&tag=errorcodefixes-20) \| Replace the safety relay, emergency stop, or sensor that is incorrectly opening the S8 circuit if the device itself has failed. |

## When to Call a Pro

Call a qualified technician or Yaskawa support if you cannot locate the external device sending the fault signal to S8, if the wiring trace is complex or undocumented, or if the fault returns after correcting all visible wiring and parameter issues. Also seek professional help if you are not familiar with VFD parameter programming or if your application involves safety interlocks that must meet regulatory standards. Yaskawa requires model number, serial number, failure details, application type, and service history before providing advanced troubleshooting, so have that information ready when you call.

## See Also

- [Yaskawa VFD Fault UV1 — Causes & Fix](/posts/yaskawa-vfd-fault-uv1/)
- [Yaskawa VFD Fault OH — Causes & Fix](/posts/yaskawa-vfd-fault-oh/)
- [Yaskawa GA800 E21 Fault - Causes & Fix](/posts/yaskawa-ga800-e21-fault-code/)
- [Yaskawa GA800 E25 Fault - Causes & Fix](/posts/yaskawa-ga800-e25-fault-code/)
