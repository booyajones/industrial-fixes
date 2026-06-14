---
title: "Danfoss FC302 ALARM 37 - Causes & Fix"
description: "ALARM 37 on a Danfoss FC302 means phase imbalance between power units. Learn the causes, diagnostic steps, and parts to fix it."
pubDatetime: 2026-05-30T12:20:07Z
modDatetime: 2026-05-30T12:20:07Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 power card / power unit"
most_likely_cause: "Motor overheating or mechanical overload"
---

## Danfoss FC302 ALARM 37 — What It Means

ALARM 37 on the Danfoss VLT AutomationDrive FC 302 indicates a phase imbalance fault. This means there is a current imbalance between the power units inside the drive. Unlike a simple motor overload alarm, this is an internal drive-side fault condition. The drive has detected that current is not flowing evenly through its power sections, which can stem from load problems, incorrect configuration, or a failing drive component. Danfoss directs technicians to check motor condition, mechanical load, and the motor current parameter as first steps, then investigate the drive hardware if the fault persists.

[Jump to Fix](#fix)

## Common Causes

- **Motor overheating or mechanical overload** Danfoss specifically instructs technicians to check for motor overheating and mechanical overload when ALARM 37 appears, because excessive load stress can create current imbalance conditions.
- **Incorrect motor current setting in parameter 1-24** If parameter 1-24 Motor Current does not match the motor nameplate current rating, the drive may misinterpret normal operation as an imbalance and trigger the fault.
- **Faulty power card or power unit** A defective power card or power unit inside the drive can cause uneven current distribution between phases, leading to the imbalance alarm even when the motor and load are healthy.
- **Defective control card** Danfoss troubleshooting guidance for internal drive faults points to the control card as a potential source of current measurement or regulation errors that manifest as ALARM 37.
- **Wiring or connection issues at the motor terminals** Loose, corroded, or damaged wiring between the drive and motor can introduce resistance imbalances that show up as unequal current draw across the power units.

## Step-by-Step Fix {#fix}

1. Check the motor for overheating by measuring winding temperature or looking for discoloration, burnt insulation smell, or hot bearing housings.
2. Inspect the mechanical load for binding, jamming, or excessive friction that could overload the motor and create uneven current demand.
3. Verify parameter 1-24 Motor Current matches the motor nameplate current rating exactly, and correct it if needed.
4. Inspect all power wiring and motor terminals for loose connections, corrosion, or damaged insulation that could introduce phase imbalance.
5. Cycle power to the drive after correcting load, wiring, or parameter issues, then monitor for recurrence of ALARM 37.
6. If the fault persists with a healthy motor and correct settings, inspect the drive's power card and control card for signs of damage, overheating, or component failure.
7. Replace the faulty power unit or control card if internal drive hardware is confirmed defective.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 power card / power unit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-37-fault-code&k=Danfoss+FC302+power+card+%2F+power+unit&tag=errorcodefixes-20) \| Replacement power section module when current imbalance originates inside the drive. |
| Danfoss FC302 control card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-37-fault-code&k=Danfoss+FC302+control+card&tag=errorcodefixes-20) \| Main control board if fault tracing points to the drive logic or current sensing circuitry. |

## When to Call a Pro

Call a qualified drive technician or certified Danfoss service partner if you are not trained to work inside VFD cabinets, if the fault returns after correcting motor current settings and load issues, or if you lack the tools to safely test and replace power or control cards. Internal drive component replacement requires working with high-voltage DC bus capacitors and precise firmware configuration. If the motor itself shows signs of winding damage or insulation failure during inspection, bring in a motor shop for rewind or replacement evaluation.

## See Also

- [Danfoss FC302 ALARM 35 - Causes & Fix](/posts/danfoss-fc302-alarm-35-fault-code/)
- [Danfoss FC302 ALARM 26 - Causes & Fix](/posts/danfoss-fc302-alarm-26-fault-code/)
- [Danfoss FC302 Alarm 22 - Hoist Brake Fault Fix](/posts/danfoss-fc302-vfd-alarm-22-fault-code/)
- [Danfoss FC302 ALARM 27 - Causes & Fix](/posts/danfoss-fc302-alarm-27-fault-code/)
