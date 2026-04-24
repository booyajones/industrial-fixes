---
title: "Allen-Bradley PowerFlex 40 F3 Fault — Power Loss"
description: "PowerFlex 40 F3 fault means the drive detected an input power loss or phase loss condition. Learn the causes, diagnostics, and fix for AB PowerFlex 40 F3."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - allen-bradley
  - powerflex
  - power-loss
---

## Allen-Bradley PowerFlex 40 F3 Fault — What It Means

An **F3 fault** on an Allen-Bradley PowerFlex 40 means the drive detected an input power loss condition. On single-phase units this usually means low or unstable incoming voltage. On three-phase systems it commonly points to **phase loss**, a bad input connection, or blown upstream fuse.

[Jump to Fix](#fix)

## Common Causes

- **One input phase is missing**. A blown fuse or loose terminal on L1, L2, or L3 causes the DC bus to collapse and trips F3.
- **Low incoming voltage**. Brownouts or undersized wiring can pull voltage below the PowerFlex 40 trip threshold.
- **Loose line terminals**. Heat cycling loosens the input lug screws over time.
- **Failing contactor or disconnect**. Worn contacts create intermittent voltage drop under load.
- **Bad precharge / bus circuit inside the drive**. Less common, but possible if input power is stable and F3 persists.

## Step-by-Step Fix {#fix}

1. **Measure incoming voltage at the drive input**. Check L1-L2, L2-L3, and L1-L3 while the drive is powered. Voltage should be balanced within 2 to 3 percent.
2. **Check all upstream fuses and breakers**. Replace any blown fuse and investigate why it failed before restarting.
3. **Torque the input terminals**. Loose terminals are a very common cause of intermittent F3 faults.
4. **Inspect the line contactor**. Pitted contacts can drop voltage under load and mimic phase loss.
5. **Check the DC bus reading in the diagnostic menu**. If line voltage is normal but the bus is unstable, the drive may have an internal power section failure.
6. **Run the drive unloaded if possible**. If the fault disappears unloaded, the problem may be upstream voltage sag under motor load.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Input fuses | [Amazon](https://www.amazon.com/s?k=Input+fuses&tag=errorcodefixes-20) \| Match class and amp rating to the installation |
| Line contactor | [Amazon](https://www.amazon.com/s?k=Line+contactor&tag=errorcodefixes-20) \| Replace if contacts are burned or voltage drop is excessive |
| Terminal block hardware | [Amazon](https://www.amazon.com/s?k=Terminal+block+hardware&tag=errorcodefixes-20) \| Replace damaged lugs or screws |
| PowerFlex 40 drive | [Amazon](https://www.amazon.com/s?k=PowerFlex+40+drive&tag=errorcodefixes-20) \| If internal bus or rectifier section is failed |
## When to Call a Pro

If line voltage is stable and balanced but F3 still trips, the drive's rectifier or internal power supply may be failing. At that point, replacement is usually faster than board-level repair.
