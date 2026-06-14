---
title: "Danfoss FC302 VFD ALARM 15 - Causes & Fix"
description: "ALARM 15 on a Danfoss FC302 means hardware mismatch. Most often a wrong or poorly seated option card. Record parameters 15-40 and 15-41."
pubDatetime: 2026-06-02T10:43:19Z
modDatetime: 2026-06-02T10:43:19Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC 302 compatible option card"
most_likely_cause: "Wrong or incompatible option card installed"
---

## Danfoss FC302 VFD ALARM 15 — What It Means

ALARM 15 on the Danfoss FC 302 VFD signals a hardware mismatch. The drive has detected that a fitted option card or module is not operational with the present control board hardware or software. This is not a motor fault or overload. It specifically points to an installed option that does not match the drive's configuration. Danfoss service instructions direct you to record parameter 15-40 (FC Type) and parameter 15-41 (Power Section) before taking any action, then to contact Danfoss support with those values if the mismatch is not easily resolved.

[Jump to Fix](#fix)

## Common Causes

- **Wrong or incompatible option card installed** The option card or module fitted to the drive is not supported by that FC 302 hardware or software variant.
- **Option card not seated correctly** The installed option has a poor connection or is not fully inserted into the option interface slot.
- **Control board hardware or software limitation** The drive's control board revision does not support the fitted option.
- **Hardware revision mismatch** The base drive and the option assembly are from incompatible hardware revisions.
- **Drive configured or serviced with mismatched parts** A previous repair or configuration change left the drive with an option that does not match the rest of the assembly.

## Step-by-Step Fix {#fix}

1. **Record parameter values** 15-40 (FC Type) and 15-41 (Power Section) from the drive display or keypad before you change anything. Danfoss requires these values for this alarm.
2. **Verify the exact FC 302 model and variant** against the installed option card. Check the drive nameplate and the option card label to confirm compatibility.
3. **Power down the drive and lock out** the supply. Wait for the DC bus to discharge fully before opening any covers.
4. **Inspect the option card or module** for correct seating, bent pins, contamination, or missing retention hardware. Remove and reseat the option carefully.
5. **If the option is known to be correct**, clear the alarm and power cycle the drive. Check that the alarm does not reappear.
6. **If the alarm persists**, replace the option with the correct approved part for your FC 302 variant or restore the drive to factory option configuration.
7. **Contact Danfoss support** with the recorded parameters if the alarm remains after verifying and replacing the option. This alarm often requires factory escalation.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC 302 compatible option card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-15-fault-code&k=Danfoss+FC+302+compatible+option+card&tag=errorcodefixes-20) \| Confirm the exact model and hardware revision of your drive before ordering. Danfoss does not publish a universal part number for this alarm. |
| FC 302 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-15-fault-code&k=FC+302+control+board&tag=errorcodefixes-20) \| Only required if Danfoss support determines the mismatch is due to a control board hardware or software limitation. Not a first-line field repair. |

## When to Call a Pro

Call a qualified VFD technician or contact Danfoss directly if you are not familiar with option card removal and reseating, or if the alarm returns after you have verified the option and configuration. Danfoss explicitly requests escalation with the recorded parameter values for this alarm. If the drive is under warranty or part of a critical process, professional support will prevent downtime and make sure the correct option and control board combination.

## See Also

- [Danfoss FC302 Alarm 24 - Causes & Fix](/posts/danfoss-fc302-alarm-24-fault-code/)
- [Danfoss VFD Fault OL — Causes & Fix](/posts/danfoss-vfd-fault-ol/)
- [Danfoss FC302 Alarm 32 - Causes & Fix](/posts/danfoss-fc302-alarm-32-fault-code/)
- [Danfoss FC302 Alarm 39 - Causes & Fix](/posts/danfoss-fc302-alarm-39-fault-code/)
