---
title: "Danfoss FC302 VFD Alarm 33 - Causes & Fix"
description: "Alarm 33 means inrush fault from too many power-ups. Let the drive cool, check for rapid power cycling, and reset once."
pubDatetime: 2026-06-03T10:44:03Z
modDatetime: 2026-06-03T10:44:03Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 precharge/inrush circuit board"
---

## Danfoss FC302 VFD Alarm 33 — What It Means

Alarm 33 on the Danfoss FC302 VFD is an inrush fault. The drive has detected too many power-ups in a short time, so the DC-link precharge circuit is not completing normally or the unit is being cycled too rapidly. This is a startup and precharge fault, not a motor overload problem.

In practical terms, the drive's inrush protection has tripped because it did not have enough time to reset between power cycles, or there is an internal fault in the precharge path or DC-link circuit. If the alarm returns after proper cooldown and normal supply conditions, the cause is more likely an internal drive or power section issue than an external wiring or motor problem.

[Jump to Fix](#fix)

## Common Causes

- **Repeated power cycling** The drive was turned on and off multiple times in a short interval, which trips the inrush protection before the precharge circuit can complete.
- **Insufficient cooldown time** The drive was re-energized before internal capacitors and thermal components returned to operating temperature.
- **DC-link fault to ground** A ground fault or leakage in the DC bus prevents the precharge circuit from functioning correctly.
- **Internal precharge circuit failure** The inrush or precharge relay, resistor, or associated circuitry inside the drive has failed and cannot complete the startup sequence.
- **Incoming power interruptions** Unstable mains supply or momentary power loss causes the drive to restart repeatedly in a short window.
- **Power section or DC-link component fault** Internal damage to DC-link capacitors or related power section components prevents normal inrush operation.

## Step-by-Step Fix {#fix}

1. **Remove power and allow the drive to cool** to operating temperature before attempting any reset or troubleshooting.
2. **Check the power-cycling history** by reviewing operator logs or control system records to confirm the drive has not been energized and de-energized multiple times in a short period.
3. **Inspect incoming power supply** for stability, correct voltage, and verify there are no interruptions or control circuit faults causing unintended restarts.
4. **Test for DC-link fault to ground** using a megohmmeter on the DC bus and motor output terminals with power off and the drive fully discharged.
5. **Reset the alarm** through the keypad or control interface after confirming adequate cooldown time and correcting any external power-cycling or supply issues.
6. **Monitor the drive through a full startup cycle** and observe for any repeated Alarm 33 or unusual precharge behavior during power-on.
7. **If Alarm 33 returns after proper cooldown and normal supply conditions**, treat it as an internal drive fault in the precharge or inrush circuitry and contact a drive service center or prepare for replacement rather than continuing to reset.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 precharge/inrush circuit board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-33-fault-code&k=Danfoss+FC302+precharge%2Finrush+circuit+board&tag=errorcodefixes-20) \| Verify with Danfoss service whether your specific model and power rating uses a replaceable precharge module before ordering. |
| Danfoss FC302 DC-link capacitor bank | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-33-fault-code&k=Danfoss+FC302+DC-link+capacitor+bank&tag=errorcodefixes-20) \| If internal DC-link fault is confirmed, consult factory service for the correct capacitor assembly for your drive frame size. |

## When to Call a Pro

Call a qualified VFD technician or Danfoss service partner if Alarm 33 returns after you have allowed proper cooldown time, corrected any rapid power-cycling, and verified stable incoming power. Persistent inrush faults usually indicate an internal failure in the precharge relay, DC-link circuit, or power section that requires factory-level diagnostics and component replacement. Do not continue to reset and re-energize the drive if the fault repeats, as this can cause further damage to internal components.

## See Also

- [Danfoss FC302 Alarm 26 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-26-fault-code/)
- [Danfoss FC302 Alarm 24 - Causes & Fix](/posts/danfoss-fc302-alarm-24-fault-code/)
- [Danfoss VFD Fault OL — Causes & Fix](/posts/danfoss-vfd-fault-ol/)
- [Danfoss AKC Controller Fault Codes - Complete Guide](/posts/danfoss-akc-controller-fault/)
