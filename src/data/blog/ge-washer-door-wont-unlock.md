---
title: "GE Washer Door Won't Unlock - Causes & Fix"
description: "Usually the door lock assembly has failed or the control is still waiting to drain. Unplug for 30 seconds, then run forced test 13."
pubDatetime: 2026-06-01T15:05:05Z
modDatetime: 2026-06-01T15:05:05Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - appliance
  - washer
  - ge
  - symptom
---

## GE Washer Door Won't Unlock — What's Happening

A GE washer door that won't unlock means the control has not released the door lock assembly after a pause, end-of-cycle drain, or fault condition. On GE front-loaders the door should unlock when you pause the washer, though some cycles drain first before releasing the lock. The lock is a safety device that automatically engages when the washer starts and should release after the machine finishes draining or you press pause.

If the panel shows a scrolling "door" message, that typically indicates the door is not properly latched rather than a separate unlock code. A door that stays locked is treated as a door lock system problem in GE repair guidance. The control may be commanding unlock, but the lock, harness, or main board may not be responding.

[Jump to Fix](#fix)

## Most Likely Causes

- **Failed door lock assembly** The lock does not respond to the unlock command and should be replaced if resistance readings are out of spec.
- **Control still waiting to unlock** The cycle has not fully drained or completed its unlock sequence, so the door remains locked as a safety measure.
- **Door not fully latched or striker misaligned** A loose latch, misaligned striker, or object preventing full closure keeps the lock from engaging or releasing properly.
- **Damaged wiring harness** Broken or corroded wires between the main board and the lock prevent the unlock signal from reaching the assembly.
- **Failed main control board** The board does not send the unlock command voltage to the lock, so the door stays locked even when commanded to open.

## How to Diagnose and Fix {#fix}

1. Unplug the washer and wait 30 seconds to let the control reboot, then plug it back in.
2. Press Start/Pause to pause the washer and wait a few seconds for the door to unlock (some cycles will drain first before releasing).
3. Enter forced diagnostic mode by holding Start/Pause while turning the selector eight clicks counter-clockwise until the display flashes 0 and the LEDs blink.
4. Run forced test 13 for the door lock to command the lock to open.
5. If the door opens in the test, the problem is likely intermittent. If it stays locked, inspect the door latch and striker alignment, then use manual access procedures to release the door safely.
6. With power disconnected, test door lock resistance at the lock harness: with the striker removed you should read OL across all three pins, and with the striker inserted and locking button pressed you should measure about 118 to 127 ohms between pins 2 and 3.
7. If resistance is out of spec, replace the door lock assembly. If the lock tests good, check harness continuity end-to-end.
8. If the harness is good, measure AC voltage from the control board during a forced lock command: a healthy board supplies about 120 volts at J513 pins 2 and 3. If the board does not send that voltage, replace the control board.

## Parts You Might Need

| Part | Notes |
|------|-------|
| GE washer door lock assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-ge-washer-door-wont-unlock&k=GE+washer+door+lock+assembly&tag=errorcodefixes-20) \| Includes the latch and striker mechanism. |
| GE washer main control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-ge-washer-door-wont-unlock&k=GE+washer+main+control+board&tag=errorcodefixes-20) \| Model-specific, supplies unlock command voltage. |
| Door lock wiring harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-ge-washer-door-wont-unlock&k=Door+lock+wiring+harness&tag=errorcodefixes-20) \| Connects the lock to the main board. |

## Related GE Error Codes

Seeing a code on the display? These match this problem:

- [Ge Washer E23 error code](/posts/ge-washer-e23-error-code/)

## When to Call a Pro

If you are not comfortable working with live 120-volt circuits or accessing internal harnesses, call a qualified appliance tech. Testing the control board output voltage and safely releasing a locked door on a pressurized or water-filled washer require experience. A pro can also verify model-specific lock resistance values and board pinouts, since these specs vary by GE platform and may differ from the general guidance here.
