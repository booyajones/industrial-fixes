---
title: "ABB ACS550 EFB 2 Fault - Causes & Fix"
description: "EFB 2 is a reserved communication fault code on the ACS550 drive. Most often caused by wrong control setup or fieldbus wiring issues."
pubDatetime: 2026-05-31T11:12:35Z
modDatetime: 2026-05-31T11:12:35Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - abb
money_part: "Fieldbus communication cable"
most_likely_cause: "Wrong control source or protocol setting"
---

## ABB ACS550 EFB 2 Fault — What It Means

The ACS550 EFB 2 fault (code 32) is a reserved embedded fieldbus fault code that ABB's documentation states is not actually used for the drive's standard embedded fieldbus diagnostics. It is protocol dependent and does not indicate a motor, DC bus, or inverter hardware failure. When this code appears, it usually points to a control or communication setup problem rather than a power stage fault. The drive is trying to report an issue with fieldbus communication or control source configuration, but because the code is reserved and protocol dependent, it does not have one universal meaning the way hardware faults do.

[Jump to Fix](#fix)

## Common Causes

- **Wrong control source or protocol setting** The drive is configured for fieldbus control but the actual control method does not match, or the communication protocol selection is incorrect for the installation.
- **Fieldbus wiring or connection fault** Loose connectors, open circuits, shorts, or poor terminations on the communication cable prevent proper data exchange between the drive and controller.
- **Electrical noise on the communication line** Inadequate shielding, improper grounding, or routing near power cables introduces interference that corrupts fieldbus signals.
- **Missing or invalid fieldbus command** The drive expects active communication from a fieldbus master but is not receiving valid data, triggering the reserved fault code.
- **Incorrect communication parameter settings** Baud rate, node address, timeout settings, or other fieldbus parameters in the drive do not match the rest of the system configuration.

## Step-by-Step Fix {#fix}

1. **Verify the exact fault code** displayed on the keypad or HMI to confirm it reads EFB 2 or fault 32, not a similar alarm or a completely different code like F0002.
2. **Check the active control method** in the drive parameters to confirm whether the drive is set for embedded fieldbus, panel control, hardwired I/O, or another communication module, and verify that matches your actual installation.
3. **Inspect all fieldbus wiring and connectors** for loose terminals, damaged cable, broken shields, and proper grounding at both the drive and controller ends of the communication link.
4. **Review communication parameters** in the drive, including protocol selection, node address, baud rate, and any comm fault action or timeout settings that could trigger this code when the link is not active.
5. **Power-cycle the drive** only after correcting any wiring or parameter issues, then clear the fault and observe whether the drive returns to ready status without the code reappearing.
6. **If the drive is not actually being commanded over fieldbus**, change the control source parameter to match your actual control method (panel, I/O, or other) so the drive stops expecting fieldbus data it will never receive.
7. **Test with a known-good communication cable** and verify shield continuity and ground connection if the fault persists after parameter corrections, to rule out cable or noise problems.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Fieldbus communication cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs550-vfd-efb2-fault-code&k=Fieldbus+communication+cable&tag=errorcodefixes-20) \| Shielded twisted-pair cable rated for your specific fieldbus protocol and installation length. |
| Cable shield grounding kit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs550-vfd-efb2-fault-code&k=Cable+shield+grounding+kit&tag=errorcodefixes-20) \| Clamps and hardware for proper 360-degree shield termination at drive and controller enclosures. |
| Communication connector or terminal block | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs550-vfd-efb2-fault-code&k=Communication+connector+or+terminal+block&tag=errorcodefixes-20) \| Replacement for damaged or corroded fieldbus connector pins or screw terminals on the drive. |

## When to Call a Pro

Call a qualified technician or ABB service partner if you have verified all wiring, confirmed the control source and communication parameters match your installation, and the EFB 2 fault still persists after power cycling. Because this is a reserved code with protocol-dependent meaning, a technician with access to ABB diagnostic tools and fieldbus protocol analyzers can isolate whether the issue is in the drive's control board, the fieldbus master, or a subtle configuration mismatch that is not obvious from the panel. Also call a pro if you are not familiar with fieldbus protocols or if the drive is part of a larger networked system where changes could affect other equipment.

## See Also

- [ABB ACS580 A2A1 Fault - Causes & Fix](/posts/abb-acs580-vfd-a2a1-fault-code/)
- [ABB ACS580 A5A0 Fault - Causes & Fix](/posts/abb-acs580-a5a0-fault-code/)
- [ABB ACS550 F0001 Fault — Causes & Fix](/posts/abb-acs550-f0001-overcurrent/)
- [ABB VFD Fault Codes — ACS550, ACS880, ACS310 Reference](/posts/abb-vfd-fault-codes/)
