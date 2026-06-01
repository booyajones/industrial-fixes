---
title: "Danfoss FC302 ALARM 36 - Causes & Fix"
description: "ALARM 36 on the Danfoss FC302 VFD signals mains failure. Learn the common causes (fuses, breakers, supply loss) and repair steps."
pubDatetime: 2026-05-30T12:19:36Z
modDatetime: 2026-05-30T12:19:36Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - danfoss
---

## Danfoss FC302 ALARM 36 — What It Means

ALARM 36 on a Danfoss VLT FC 302 means mains failure. The drive has lost its supply voltage, and the alarm is active when parameter 14-10 Mains Failure is not set to No Function. This is almost always an external power-supply problem, not an internal drive fault. The drive is reporting that it no longer sees incoming AC line power at its input terminals.

[Jump to Fix](#fix)

## Common Causes

- **Blown input fuses** One or more fuses feeding the drive have opened, cutting off the supply voltage to the unit.
- **Tripped upstream breaker or disconnect** A circuit breaker or disconnect switch ahead of the drive has tripped or been opened, removing mains power.
- **Loose or open line power connections** Line-side terminal connections at the drive or upstream junction points have loosened, corroded, or failed, creating an open circuit.
- **Loss of upstream mains supply** The facility power source feeding the drive has been interrupted or lost entirely.
- **Parameter 14-10 configured to trigger alarm** The mains failure function is enabled in parameter 14-10, and the drive detects a supply disturbance or drop that meets the alarm threshold.

## Step-by-Step Fix {#fix}

1. Check upstream power supply and verify that the mains to the facility or panel are live and stable.
2. Inspect the circuit breaker or disconnect feeding the drive and reset or replace it if tripped or failed.
3. Examine the drive's input fuses for continuity and replace any that have blown.
4. Measure incoming line voltage at the drive input terminals using a multimeter and confirm the supply is present and within the rated input range for your specific FC 302 model (consult your model's nameplate and manual).
5. Inspect all line-side terminal connections at the drive and upstream junction boxes for tightness, heat damage, or corrosion, and re-torque or repair as needed.
6. Review parameter 14-10 Mains Failure in the drive programming and set it to No Function if the alarm is unwanted or verify the control logic if it is intentional.
7. Clear the alarm and cycle power to the drive after restoring the supply, then monitor for recurrence.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Input fuses for Danfoss FC 302 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-36-fault-code&k=Input+fuses+for+Danfoss+FC+302&tag=errorcodefixes-20) \| Match the fuse type and amperage rating to your drive's input voltage and frame size per the manual. |
| Circuit breaker or disconnect switch | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-36-fault-code&k=Circuit+breaker+or+disconnect+switch&tag=errorcodefixes-20) \| Replace if the upstream breaker has failed or will not hold after reset. |
| Line power wire or terminal lugs | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-36-fault-code&k=Line+power+wire+or+terminal+lugs&tag=errorcodefixes-20) \| Use if existing input wiring or terminals are damaged, burned, or corroded beyond repair. |

## When to Call a Pro

Call a qualified electrician or drive technician if you are not trained to work safely with live industrial AC power, if you cannot locate the source of the mains loss after checking the upstream supply and input fuses, or if the alarm persists even when you have confirmed that proper line voltage is present at the drive input terminals. A recurring ALARM 36 with good incoming power may indicate a configuration issue or an internal control fault that requires factory support or a field service engineer.
