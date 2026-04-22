---
title: "Haas Alarm 122 — ATC Chain Fault"
description: "Haas Alarm 122 means the automatic tool changer chain or carousel failed to index correctly. Learn the causes and how to fix Haas Alarm 122."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - cnc
  - haas
  - atc
  - carousel
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
| Carousel proximity switch | Replace if position is not detected |
| Tool pocket hardware | Bent pockets or dogs must be replaced |
| Carousel drive motor | If weak or stalled under normal load |
| Air regulator parts | If pneumatic assist is weak |

## When to Call a Pro

If the carousel repeatedly stops between positions or the magazine is physically damaged, deeper alignment and changer timing work may be required.
