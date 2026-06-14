---
title: "Yaskawa GA800 E33 Fault Code - Causes & Fix"
description: "E33 fault meaning varies by GA800 model. Check your manual for the exact definition, then verify wiring and power connections."
pubDatetime: 2026-06-05T10:02:58Z
modDatetime: 2026-06-05T10:02:58Z
author: "Marcus Webb"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "Yaskawa GA800 Control Board"
most_likely_cause: "Misread or transposed fault code"
---

## Yaskawa GA800 E33 Fault Code — What It Means

The exact meaning of an E33 fault code on the Yaskawa GA800 VFD is not documented in standard Yaskawa troubleshooting materials for this series. Yaskawa drives typically display fault codes in formats like UV3, EF3, or bUS. The code you see may be a misread display, a diagnostic parameter entry, or a code specific to a custom configuration or older firmware version. Before proceeding, verify the exact alphanumeric code shown on the keypad display or in the drive's fault history menu.

Because the GA800 service documentation directs technicians to start with the elementary diagram and the specific fault definition for that model and serial number, the safest approach is to consult your drive's manual or contact Yaskawa technical support with your model number, serial number, and the exact fault text. General troubleshooting for undefined or ambiguous codes includes checking input power quality, control wiring integrity, and recent parameter changes that may have triggered a soft fault.

[Jump to Fix](#fix)

## Common Causes

- **Misread or transposed fault code** The display may show a similar code like E3, UV3, or another alphanumeric string that was noted incorrectly.
- **Custom parameter or firmware-specific fault** Some drive configurations or older firmware versions use fault codes not listed in current standard documentation.
- **Input power disturbance or phase loss** Voltage sags, phase imbalance, or missing phases can trigger unspecified or generic fault conditions.
- **Control board communication or memory error** Internal communication faults or corrupted parameter memory can produce non-standard fault codes.
- **Recent parameter change or keypad entry error** An incorrectly set parameter or accidental keypad input can cause the drive to enter a fault state with an unusual code.
- **Soft-charge or pre-charge relay failure** If the code is actually UV3 or similar, the soft-charge bypass relay or contactor may have failed to close on startup.

## Step-by-Step Fix {#fix}

1. **Verify the exact fault code** by pressing the alarm/history key on the keypad and recording the full alphanumeric string and any accompanying text description.
2. **Consult the GA800 manual** for your specific model and serial number to find the fault definition, or call Yaskawa technical support with the drive nameplate data and fault code.
3. **Power-cycle the drive** by switching off the main disconnect, waiting 60 seconds, then re-energizing to see if the fault clears or returns immediately.
4. **Inspect incoming power** with a multimeter, checking for balanced three-phase voltage within the drive's rated range and verifying that all three phases are present and stable.
5. **Review recent parameter changes** in the drive's parameter list or programming history, and restore factory defaults if a recent edit preceded the fault.
6. **Check control wiring and I/O connections** for loose terminals, damaged cables, or shorted analog/digital inputs that could generate a fault condition.
7. **Contact Yaskawa technical support or an authorized service center** with your model number, serial number, exact fault code, and elementary diagram if the fault persists or you cannot locate the code definition in your manual.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 Control Board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e33-fault-code&k=Yaskawa+GA800+Control+Board&tag=errorcodefixes-20) \| Required if internal communication or memory fault is confirmed by technical support. |
| Soft-Charge Bypass Relay/Contactor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e33-fault-code&k=Soft-Charge+Bypass+Relay%2FContactor&tag=errorcodefixes-20) \| Needed if the fault is actually UV3 or another pre-charge related code and the relay has failed. |

## When to Call a Pro

Call a qualified VFD technician or Yaskawa authorized service provider if you cannot locate the E33 fault definition in your drive manual, if the fault returns after a power cycle, or if you are unfamiliar with three-phase power systems and drive parameter programming. Yaskawa GA800 troubleshooting requires access to the elementary diagram, parameter tables, and sometimes oscilloscope or power-quality analysis tools. Incorrect wiring changes or parameter edits can damage the drive or connected motor. Professional support is also recommended if the drive is part of a critical process or if you need to verify warranty coverage before opening the enclosure or replacing boards.
