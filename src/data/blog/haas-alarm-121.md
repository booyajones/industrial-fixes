---
title: "Haas Alarm 121 — ATC Arm Fault"
description: "Haas Alarm 121 means the automatic tool changer arm failed to complete its motion correctly. Learn the causes and how to fix Haas Alarm 121."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - cnc
  - haas
  - atc
  - tool-changer
---

## Haas Alarm 121 — What It Means

**Alarm 121** on a Haas mill means the **automatic tool changer arm did not reach the expected position** during a tool change. The arm may be blocked, mis-timed, or failing to actuate completely.

[Jump to Fix](#fix)

## Common Causes

- **ATC arm is out of alignment**. After a crash or jam, timing can shift.
- **Low air pressure**. Haas tool changers rely heavily on clean, stable air supply.
- **Dirty or sticky tool changer mechanism**. Chips and dried grease create drag.
- **Failed proximity switch or sensor**. The control doesn't see the arm in the correct position.
- **Damaged arm or gripper fingers**. Physical interference prevents full travel.

## Step-by-Step Fix {#fix}

1. **Check shop air pressure**. Haas machines generally want clean, dry air around 100 psi.
2. **Inspect the ATC arm for chips or crash damage**. Remove any debris around the arm pocket and grippers.
3. **Run tool changer recovery** from the Haas service menu if the machine supports it.
4. **Check arm sensors / prox switches**. Confirm each switch changes state when the arm moves.
5. **Inspect timing marks** on the arm and gearbox. Mis-timed arms must be realigned to Haas procedure.
6. **Lubricate the mechanism** if dry or sticky.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Proximity switch | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-haas-alarm-121&k=Proximity+switch&tag=errorcodefixes-20) \| Common if the control never sees arm position |
| ATC arm gripper fingers | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-haas-alarm-121&k=ATC+arm+gripper+fingers&tag=errorcodefixes-20) \| Replace if bent or worn |
| Air regulator / filter parts | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-haas-alarm-121&k=Air+regulator+%2F+filter+parts&tag=errorcodefixes-20) \| Low air causes incomplete actuation |
| ATC gearbox components | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-haas-alarm-121&k=ATC+gearbox+components&tag=errorcodefixes-20) \| If timing will not hold |
## When to Call a Pro

If the arm is visibly out of time or the changer jammed during a crash, the safest path is a proper Haas recovery and alignment procedure. Forcing the changer can bend the arm or damage the carousel.

## Related Articles

- [Haas CNC Alarm 101 — Emergency Stop Active Fix](/posts/haas-alarm-101-emergency-stop/)
- [Haas Alarm 102 — Servo Drive Fault Fix](/posts/haas-alarm-102/)
- [Haas Alarm 103 — Servo Overload Fix](/posts/haas-alarm-103/)
- [Haas Alarm 104 Feed Hold — Causes & Fix](/posts/haas-alarm-104-feed-hold/)
- [Haas Alarm 105 E-Stop — Causes & Fix](/posts/haas-alarm-105/)
