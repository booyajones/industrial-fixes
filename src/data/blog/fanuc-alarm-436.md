---
title: "Fanuc Alarm 436 — Causes & Fix"
description: "What Fanuc Alarm 436 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T14:00:00Z
modDatetime: 2026-04-22T14:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - cnc
  - fanuc
---

## Fanuc Alarm 436 — What It Means

Fanuc Alarm 436 indicates a servo following error on the Z-axis — the actual Z-axis position lagged behind the commanded position by more than the allowable error tolerance. The Z-axis carries the spindle on most vertical machining centers, making this alarm particularly impactful: any Z-axis fault stops all cutting. Alarm 436 is the Z-axis equivalent of 414 (X) and 435 (Y).

[Jump to Fix](#fix)

## Common Causes

- **Z-axis counterbalance or weight issue** — On VMCs, the Z-axis carries the spindle head. A failed counterbalance cylinder or compressed air system means the servo fights gravity constantly, causing following error under rapid moves.
- **Z-axis servo amplifier degraded** — Reduced drive torque output from a degraded amplifier can't keep up with commanded Z moves under load.
- **Ballscrew wear or contamination** — A worn Z-axis ballscrew creates variable resistance through the stroke, causing following error at specific positions.
- **Encoder feedback fault** — An intermittent Z-axis encoder signal causes sudden position error jumps that trigger Alarm 436.

## Step-by-Step Fix {#fix}

1. **Check counterbalance pressure** — On VMCs with pneumatic counterbalance, verify air pressure at the counterbalance cylinder. Low pressure forces the servo to carry full spindle head weight. Correct air pressure per machine specification.
2. **Test Z-axis servo amplifier** — Check the amplifier display for its own fault indicators. Test DC bus voltage under load — sagging bus voltage reduces torque output.
3. **Inspect Z-axis ballscrew** — Move Z to multiple positions and check for binding or rough spots. Clean and re-lubricate. Check ballscrew backlash compensation parameters.
4. **Check encoder cable** — Inspect from motor to amplifier for damage. Substitute a known-good cable if you suspect intermittent signal loss.
5. **Reset and test with slow feed** — Press RESET and jog Z slowly through full travel. If 436 appears only at speed, the torque or following error tolerance needs adjustment.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Counterbalance cylinder / seals | If air pressure drops due to seal wear |
| Z-axis encoder cable | Most common cause of intermittent 436 |
| Z-axis servo motor | If motor winding test shows fault |

## When to Call a Pro

Z-axis mechanical work on VMCs (ballscrew, guideway, counterbalance) requires precision re-leveling and accuracy verification. Fanuc-trained field service is recommended for any Z-axis mechanical repair.
