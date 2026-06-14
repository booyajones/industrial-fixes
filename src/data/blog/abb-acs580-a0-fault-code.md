---
title: "ABB ACS580 A0 Fault Code - Causes & Fix"
description: "ABB ACS580 A0 is likely a misread of A5A0 or 5091, meaning Safe Torque Off is active. Learn causes, diagnosis, and reset steps."
pubDatetime: 2026-05-27T10:33:18Z
modDatetime: 2026-05-27T10:33:18Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - abb
money_part: "ABB ACS580 STO terminal jumper kit"
most_likely_cause: "Open or missing STO jumper"
---

## ABB ACS580 A0 Fault Code — What It Means

The ACS580 does not have a standard fault code labeled 'A0' in ABB's official fault lists. The code you are seeing is most likely A5A0 or fault 5091, which both mean Safe Torque Off (STO) is active. This is a safety function that cuts torque to the motor when the STO circuit opens. It is not a motor or power fault. It indicates the safety chain has removed the enable signal, either intentionally through an E-stop or safety device, or unintentionally due to wiring or jumper issues.

This is different from fault 5090, which ABB defines as an STO hardware failure inside the drive itself. If your display shows 5090 instead of 5091 or A5A0, the drive has detected an internal safety hardware problem and you should contact ABB. For the STO active condition (5091/A5A0), the fix involves restoring the external safety circuit and resetting the drive.

[Jump to Fix](#fix)

## Common Causes

- **Open or missing STO jumper** If the drive is not connected to an external safety device, the STO terminals require a jumper to close the safety loop, and a loose or missing jumper will activate the STO function.
- **External safety device triggered** An E-stop button, safety relay, door interlock, or other safety device in the STO circuit has opened and needs to be reset or closed.
- **Loose or broken STO terminal wiring** Poor connection or broken wire at the STO terminals can interrupt the safety circuit and cause the drive to read STO as active.
- **STO indication parameter set to fault** Parameter 31.22 (STO indication) may be configured to treat STO activation as a fault rather than a warning, stopping the drive even if the condition is temporary.
- **Misread display** The code may have been misread on the keypad or HMI, and verifying the exact alphanumeric code is necessary before troubleshooting.

## Step-by-Step Fix {#fix}

1. **Verify the exact fault code** displayed on the drive keypad or HMI to confirm whether it reads A5A0, 5091, 5090, or something else entirely.
2. **Inspect the STO terminals** on the drive and check for the presence and tightness of the STO jumper if no external safety device is installed.
3. **Check the external safety circuit** including E-stop buttons, safety relays, door switches, and interlocks to confirm all devices are closed and functioning.
4. **Test for continuity** through the entire STO safety chain using a multimeter to locate any open circuit or faulty wiring.
5. **Reset the drive** after restoring the safety circuit by cycling power or using the reset function on the keypad, then verify normal operation resumes.
6. **Review parameter 31.22** (STO indication) if the fault recurs and consider changing the setting from Fault to Warning if appropriate for your application.
7. **Contact ABB** if the display shows fault 5090 (STO hardware failure) or if the STO active condition persists with correct external wiring and jumpers in place.

## Parts Often Needed

| Part | Notes |
|------|-------|
| ABB ACS580 STO terminal jumper kit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-a0-fault-code&k=ABB+ACS580+STO+terminal+jumper+kit&tag=errorcodefixes-20) \| Required if original jumper is missing or damaged and no external safety device is used. |
| Safety relay or interlock switch | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-a0-fault-code&k=Safety+relay+or+interlock+switch&tag=errorcodefixes-20) \| Replace if an external safety device in the STO circuit is faulty or not closing properly. |
| ABB ACS580 control unit or STO interface board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-a0-fault-code&k=ABB+ACS580+control+unit+or+STO+interface+board&tag=errorcodefixes-20) \| Only needed for fault 5090 (STO hardware failure). Contact ABB for diagnosis and part number before ordering. |

## When to Call a Pro

Call a qualified electrician or ABB service technician if you cannot locate the cause of the STO activation after checking all external wiring and jumpers, if the drive displays fault 5090 indicating internal STO hardware failure, or if you are unfamiliar with safety circuit wiring and testing. Work on STO circuits involves machine safety systems and incorrect handling can create serious hazards. If the drive will not reset after restoring the safety chain, or if you need to modify parameter 31.22 and are uncertain about the safety implications, professional support is the correct choice.

## See Also

- [ABB Inverter Fault Code F0001 - Causes & Fix](/posts/abb-inverter-fault-code-f0001/)
- [ABB VFD Fault 3130 — Input Phase Loss Fix](/posts/abb-vfd-fault-3130/)
- [ABB VFD Fault 0001 Overcurrent — Causes & Fix](/posts/abb-vfd-fault-0001-overcurrent/)
- [ABB ACS550 AI1 LOSS - Causes & Fix](/posts/abb-acs550-ai1-loss-fault-code/)
