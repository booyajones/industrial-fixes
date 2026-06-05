---
title: "Danfoss FC302 Alarm 31 - Causes & Fix"
description: "Alarm 31 means motor phase V missing. Most often a loose wire or bad connection on phase V between drive and motor. Check wiring."
pubDatetime: 2026-06-03T10:42:10Z
modDatetime: 2026-06-03T10:42:10Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - danfoss
---

## Danfoss FC302 Alarm 31 — What It Means

Alarm 31 on a Danfoss FC302 VFD indicates a missing motor phase V. The drive has detected that the V output phase between the frequency converter and the motor is open or absent while the motor is running. This alarm does not appear at start-up but triggers during operation when the drive's phase-loss detection is active. The drive is specifically reporting a problem on the V phase output side, not the incoming supply.

[Jump to Fix](#fix)

## Common Causes

- **Loose or disconnected V-phase motor lead** The most common field cause is a loose, open, or disconnected wire on phase V at the drive terminals, motor terminals, or junction box.
- **Broken or damaged motor cable conductor** The phase V conductor in the motor cable may be broken, nicked, or damaged internally even if insulation looks intact.
- **Corroded or overheated terminal or connector** A corroded, burnt, or overheated terminal on phase V can create an open circuit under load.
- **Open motor winding or internal connection** If wiring checks good, the motor itself may have an open winding or internal lead connection on phase V.
- **Failed drive output stage or inverter component** If the motor and all wiring test good, the drive's output power stage or IGBT section for phase V may have failed internally.

## Step-by-Step Fix {#fix}

1. **Remove power** from the drive and lock out all sources before any inspection or resistance testing.
2. **Inspect and tighten all V-phase connections** at the drive output terminals, motor terminal box, and any junction boxes or intermediate connectors.
3. **Check motor cable continuity** on phase V using a multimeter, and visually inspect the cable for heat damage, cuts, or worn insulation.
4. **Test the motor winding** for continuity on phase V if the cable tests good, and compare resistance across all three phases to check for an open or imbalanced winding.
5. **Inspect all terminals and connectors** on phase V for corrosion, overheating, discoloration, or loose hardware that could cause an open circuit under load.
6. **If wiring and motor are confirmed good**, suspect the drive's output stage on phase V and test or replace the inverter power module or power card for that phase according to service procedures for your frame size.
7. **Reset the drive** and run the motor under normal load to verify the alarm does not return and all three phases are balanced.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor cable assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-31-fault-code&k=Motor+cable+assembly&tag=errorcodefixes-20) \| Replacement cable if phase V conductor is broken or damaged. |
| Motor terminal connectors or crimp lugs | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-31-fault-code&k=Motor+terminal+connectors+or+crimp+lugs&tag=errorcodefixes-20) \| For repairing corroded or burnt terminals on phase V. |
| Drive output power module or inverter power board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-31-fault-code&k=Drive+output+power+module+or+inverter+power+board&tag=errorcodefixes-20) \| Frame-size-specific replaceable assembly if internal drive fault is confirmed. |

## When to Call a Pro

Call a qualified electrician or drive technician if you are not trained in VFD service, if the wiring and motor test good but the alarm persists (indicating an internal drive fault), or if you need to replace the drive's output power stage. Work on VFD output circuits and inverter components requires lockout procedures, high-voltage safety knowledge, and diagnostic tools. If the motor winding is open, call a motor shop or electrician to evaluate whether repair or replacement is more cost-effective.
