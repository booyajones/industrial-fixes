---
title: "Yaskawa GA800 A.137 Fault - Causes & Fix"
description: "A.137 is not a standard GA800 code in published manuals. Check for misread display or machine-specific parameter fault; reset and verify wiring."
pubDatetime: 2026-06-09T11:27:18Z
modDatetime: 2026-06-09T11:27:18Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "GA800 control board (IGBT driver / logic board)"
most_likely_cause: "Misread or non-standard display code"
diy_or_pro: "pro"
---

## What this code means
A.137 does not appear in the published Yaskawa GA800 fault code lists, which typically use short alphanumeric codes like oC (overcurrent), Uv (undervoltage), or CPF (control power failure). The code may be misread from the keypad display, may belong to a host machine (elevator controller, CNC, HVAC system) that sends custom faults to the drive, or may be an internal diagnostic message not documented in the standard operator manual. If you see A.137 on a GA800 keypad, first confirm the exact characters displayed, then check whether the drive is part of a larger system that generates its own alarm codes.

Without a verified meaning from Yaskawa documentation, the safest approach is to treat A.137 as a generic parameter or communication fault. Record the operating condition when the alarm appeared, inspect all wiring and control terminals for loose connections or damage, verify that motor parameters match the motor nameplate, and attempt a fault reset by cycling power or pressing the keypad reset. If the alarm persists after wiring checks and a reset, consult the GA800 technical manual for your exact firmware revision or contact Yaskawa support with the drive serial number and the complete alarm history to obtain the specific meaning for your installation.

## Before You Replace Anything

Technicians sometimes replace the control board or main power module when the real issue is a loose control terminal, incorrect parameter setting, or a fault code forwarded from the host PLC. Always verify wiring, check parameter C1-01 through C1-06 for motor nameplate match, and review the alarm history log before ordering boards.

## Common Causes

- **Misread or non-standard display code** The characters may be similar to a documented code (such as A.137 being A1.37 or A-137 in a different format) or the display may be partially obscured by dust or a failing LCD segment.
- **Host machine or PLC-generated alarm** Many industrial systems send custom fault codes to the VFD keypad over a fieldbus or analog input, and A.137 may originate from the elevator controller, CNC, or HVAC system rather than the drive itself.
- **Parameter configuration mismatch** Incorrect motor parameters (especially motor rated current, voltage, or frequency in C1-01 through C1-06) or tuning settings can trigger undefined or undocumented alarms during autotuning or under load.
- **Loose or damaged control wiring** A poor connection at terminals S1 through S7, or a break in the control cable between the drive and external keypad or network module, can produce spurious codes.
- **Firmware or keypad incompatibility** An aftermarket or replacement keypad running different firmware may display codes in a non-standard format, or an older GA800 firmware revision may use internal diagnostics not listed in later manuals.

## Step-by-Step Fix {#fix}

1. **Record the complete alarm display** by photographing the keypad or writing down every character, including spacing and punctuation, to confirm the exact code.
2. **Check the drive model label** on the front or side cover and note the firmware revision (visible in the drive's parameter H1-01 or H1-02) to cross-reference against the correct technical manual.
3. **Inspect all control terminals S1 through S7** for loose screws, broken wires, or corrosion, and verify that shield drains on control cables are properly grounded.
4. **Review motor parameters C1-01 through C1-06** on the keypad and compare them to the motor nameplate; incorrect rated voltage, current, or frequency can trigger parameter faults during operation or autotuning.
5. **Attempt a fault reset** by pressing the keypad reset button or cycling power to the drive; if the alarm reappears immediately, note the exact operating condition (speed command, load, ambient temperature) when it triggers.
6. **Check the alarm history** in the drive menu (typically parameter H3-01 through H3-08) to see if other codes appeared before A.137, which can help identify the root cause.
7. **Contact Yaskawa technical support** with the drive serial number, firmware revision, and a photo of the alarm display if the code is not found in the published manual; they can confirm whether A.137 is specific to your firmware or application and provide the correct meaning and corrective action.

## Parts Often Needed

| Part | Notes |
|------|-------|
| GA800 control board (IGBT driver / logic board) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-137-fault-code&k=GA800+control+board+%28IGBT+driver+%2F+logic+board%29&tag=errorcodefixes-20) \| Only replace if Yaskawa support confirms a board fault; verify wiring and parameters first to avoid unnecessary expense. |
| GA800 operator keypad (remote keypad or replacement LCD) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-137-fault-code&k=GA800+operator+keypad+%28remote+keypad+or+replacement+LCD%29&tag=errorcodefixes-20) \| Needed if the display is physically damaged or if Yaskawa confirms the keypad firmware is incompatible with your drive revision. |

## When to Call a Pro

Call a qualified drive technician or Yaskawa-certified integrator if the alarm persists after you have verified wiring, checked motor parameters, and attempted a reset. VFD diagnostics often require specialized tools such as an oscilloscope to check gate-driver signals, a megohmmeter to test motor insulation, or a laptop with Yaskawa DriveWizard Plus software to read extended alarm logs and internal fault registers. A technician can also contact Yaskawa support on your behalf with detailed drive information to decode non-standard alarm messages and determine whether the control board, power module, or external network interface needs replacement. Do not attempt to open the drive enclosure or probe high-voltage terminals without proper lockout/tagout and high-voltage safety training.
