---
title: "ABB ACS355 Fault 3130 — Input Phase Loss Fix"
description: "What ABB ACS355 fault 3130 means, why input phase loss triggers, and how to fix it step by step."
pubDatetime: 2026-04-22T14:00:00Z
modDatetime: 2026-04-22T14:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - abb
---

## ABB ACS355 Fault 3130 — What It Means

The ABB ACS355 is a general-purpose variable frequency drive designed for pump, fan, compressor, and conveyor applications. Fault 3130 (INPUT PHASE LOSS) means the drive has detected a missing or severely unbalanced phase on its three-phase supply input. The ACS355 monitors the DC bus ripple — when one input phase is lost, the bus ripple increases dramatically because the drive is now rectifying only two phases. When ripple exceeds the fault threshold, the drive trips on 3130 to prevent damage to the rectifier bridge and bulk capacitors.

[Jump to Fix](#fix)

## Common Causes

- **Blown input fuse** — A fuse in the upstream panel has blown on one of the three supply phases. This is the most common cause. Fuses blow from a transient fault (motor short, surge) or from reaching end of life.
- **Loose or corroded input power terminal** — A loose L1, L2, or L3 terminal connection at the drive creates a high-resistance path that appears as a missing phase under load. Vibration environments are particularly prone to this.
- **Failed upstream contactor or disconnect** — A contactor with a failed contact or a disconnect switch with a damaged blade can drop one phase under load even though it appears closed.
- **Utility phase loss** — One phase of the utility supply has actually been lost at the service entrance, the transformer, or the panel. Check voltages at the panel before suspecting the drive.
- **Single-phase input on a three-phase drive** — If someone wired a single-phase supply to a three-phase ACS355, fault 3130 appears immediately. The ACS355 is a three-phase-input drive (there is a separate ACS355 single-phase input variant).

## Step-by-Step Fix {#fix}

1. **Measure all three input voltages at the drive** — With the drive powered (and faulted), use a multimeter to measure L1-L2, L2-L3, and L1-L3 at the drive's input terminal block. All three should read within ±3% of each other. A missing phase reads 0V or significantly lower.
2. **Check upstream fuses** — Open the upstream panel and test each input fuse with a multimeter or fuse tester. Replace any blown fuse. Investigate why it blew before assuming it was a fluke.
3. **Inspect the drive input terminals** — With power off and capacitors discharged (wait 5 minutes after power off), check L1, L2, L3 terminal connections inside the drive. Tighten any loose screws. Clean any corroded terminal contacts.
4. **Inspect the upstream contactor or disconnect** — If fuses are good, check the contactor contacts with a multimeter for continuity when energized. A contact with high resistance under load causes voltage drop that appears as phase loss.
5. **Check drive parameter 30.17** — On the ACS355, parameter 30.17 controls the phase loss detection sensitivity. If fault 3130 appears intermittently under heavy load, the sensitivity may be set too high for the application's supply quality. Verify the supply voltage balance and adjust only if supply quality is confirmed acceptable.
6. **Reset and restart** — After restoring all three phases and confirming input voltages are balanced, press RESET on the ACS355 keypad. Monitor the DC bus voltage (parameter 01.11) at startup — it should rise smoothly without excessive ripple.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [Input fuses](https://www.amazon.com/s?k=Input%20fuses&tag=errorcodefixe-20) | Match voltage and amp rating; ABB specifies fuse type in the ACS355 hardware manual |
| [Upstream contactor](https://www.amazon.com/s?k=Upstream%20contactor&tag=errorcodefixe-20) | Replace if one contact shows high resistance |
| [ACS355 rectifier bridge](https://www.amazon.com/s?k=ACS355%20rectifier%20bridge&tag=errorcodefixe-20) | Only if input fuse and terminal checks are clean but 3130 persists — rare |

## When to Call a Pro

If all three supply phases are confirmed present and balanced at the panel but fault 3130 still appears at the drive, the rectifier input section of the drive may be damaged. This requires an ABB-certified technician or drive repair shop to diagnose and repair at the board level.
