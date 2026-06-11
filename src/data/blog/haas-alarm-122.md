---
title: "Haas Alarm 122 — ATC Chain Fault"
description: "Haas Alarm 122 means the automatic tool changer chain or carousel failed to index correctly. Learn the causes and how to fix Haas Alarm 122."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - cnc
  - haas
  - atc
  - carousel
money_part: "Carousel proximity switch"
---

## Haas Alarm 122 — What It Means

**Alarm 122** on a Haas mill means the **ATC chain or carousel did not move to the commanded position**. The control expected the tool magazine to index and confirm position, but the position signal did not arrive in time.

[Jump to Fix](#fix)

## Common Causes

- **Carousel is jammed with chips or damaged toolholders**.
- **Low air pressure** on umbrella changer or side-mount tool changer systems.
- **Carousel motor or gearbox issue**. The chain may stall before reaching position.
- **Home / pocket sensor failure**. The magazine moves but the control never sees confirmation.
- **Tool pocket damage from a crash**. Bent pocket hardware causes drag or misindexing.

## Step-by-Step Fix {#fix}

1. **Inspect the carousel physically**. Look for chips, broken tools, or bent toolholders.
2. **Check air pressure** and air blast components if the magazine uses pneumatic assist.
3. **Run tool changer recovery** and jog the carousel slowly if the machine allows it.
4. **Watch the pocket sensor status** on diagnostics while the carousel moves.
5. **Check the carousel drive motor and gearbox** for binding, backlash, or overheating.
6. **Verify pocket alignment**. A misaligned tool pocket can stall the index cycle.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Carousel proximity switch | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-haas-alarm-122&k=Carousel+proximity+switch&tag=errorcodefixes-20) \| Replace if position is not detected |
| Tool pocket hardware | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-haas-alarm-122&k=Tool+pocket+hardware&tag=errorcodefixes-20) \| Bent pockets or dogs must be replaced |
| Carousel drive motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-haas-alarm-122&k=Carousel+drive+motor&tag=errorcodefixes-20) \| If weak or stalled under normal load |
| Air regulator parts | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-haas-alarm-122&k=Air+regulator+parts&tag=errorcodefixes-20) \| If pneumatic assist is weak |
## When to Call a Pro

If the carousel repeatedly stops between positions or the magazine is physically damaged, deeper alignment and changer timing work may be required.

## Related Articles

- [Haas CNC Alarm 101 — Emergency Stop Active Fix](/posts/haas-alarm-101-emergency-stop/)
- [Haas Alarm 102 — Servo Drive Fault Fix](/posts/haas-alarm-102/)
- [Haas Alarm 103 — Servo Overload Fix](/posts/haas-alarm-103/)
- [Haas Alarm 104 Feed Hold — Causes & Fix](/posts/haas-alarm-104-feed-hold/)
- [Haas Alarm 105 E-Stop — Causes & Fix](/posts/haas-alarm-105/)

## See Also

- [Haas Alarm 106 — Causes & Fix](/posts/haas-alarm-106/)
- [Haas Alarm 132 — Servo Amplifier Fault Fix](/posts/haas-alarm-132/)
- [Haas Alarm 103 Overheating — CNC Machine Thermal Fault Diagnosis and Fix](/posts/haas-alarm-103-overheating/)
- [Haas Alarm 118 — Spindle Orientation Fault Causes & Fix](/posts/haas-alarm-118/)
