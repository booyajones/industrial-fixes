---
title: "Siemens Micromaster F0035 - Causes & Fix"
description: "F0035 means the drive exceeded its auto-restart limit (P1211). Reset the fault and find the underlying trip cause to fix it."
pubDatetime: 2026-06-03T10:33:52Z
modDatetime: 2026-06-03T10:33:52Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Siemens Micromaster 440 replacement drive"
most_likely_cause: "Recurring motor or load fault"
---

## What this code means
On a Siemens Micromaster 440 VFD, fault code F0035 indicates 'Auto restart after n.' The drive tried to automatically restart after a trip but exceeded the number of attempts allowed by parameter P1211. This is not a wiring or component fault on its own. It means the inverter kept hitting the same problem over and over until the restart counter ran out. The underlying trip condition is still present, so the drive gave up and locked into F0035. You need to reset the fault and then hunt down whatever keeps causing the repeated trips in the first place.

## Common Causes

- **Recurring motor or load fault** The drive keeps restarting because an unresolved motor overload, stall, or mechanical jam keeps tripping the inverter.
- **Unstable supply voltage** Repeated under-voltage, over-voltage, or power loss events trigger auto-restart until the limit in P1211 is reached.
- **Control signal or parameter mismatch** An application logic error or incorrect run command keeps forcing the drive into a trip-restart loop.
- **Auto-restart enabled without fixing root cause** P1211 allows auto-restart, but the original fault (overload, ground, etc.) was never corrected, so the drive exhausts its attempts.
- **Intermittent process condition** A transient process issue (temporary jam, surge, or loss of feedback) keeps re-triggering trips faster than the drive can recover.

## Step-by-Step Fix {#fix}

1. **Confirm the fault code** on the BOP or AOP display by scrolling through active faults and verify it is F0035 on a Micromaster 440.
2. **Reset the fault** by cycling power to the drive, pressing the reset button on the BOP/AOP, or using Digital Input 3 if configured for fault reset.
3. **Check parameter P1211** to see how many auto-restart attempts are configured and whether auto-restart is appropriate for your application (disable if not needed).
4. **Review the fault history** in the drive's fault memory to identify the original trip code that triggered the restart loop (overload, undervoltage, overcurrent, etc.).
5. **Inspect motor and mechanical load** for binding, excessive load, locked rotor, or wiring faults that would cause repeated trips.
6. **Verify supply voltage** at the drive input terminals under load to rule out intermittent power dips, surges, or phase loss.
7. **Clear the fault memory** after correcting the root cause, then run a controlled start-stop test to confirm stable operation without further restarts.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens Micromaster 440 replacement drive | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-vfd-f0035-fault-code&k=Siemens+Micromaster+440+replacement+drive&tag=errorcodefixes-20) \| Only if internal diagnostics confirm drive hardware failure after all parameter and wiring checks pass. |
| Motor overload relay or sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-vfd-f0035-fault-code&k=Motor+overload+relay+or+sensor&tag=errorcodefixes-20) \| If the root cause is genuine motor overload or intermittent thermal trips. |

## When to Call a Pro

Call a qualified electrician or controls technician if you cannot safely identify the original fault from the drive's fault history, if the motor or load inspection reveals no obvious mechanical problem, or if the fault returns immediately after a proper reset and parameter review. A technician with a Siemens commissioning tool can log real-time parameters, verify power quality, and trace the restart loop back to the true source. Also call a pro if the drive hardware itself is suspect (internal fault, damaged control board) or if your process requires tuning of auto-restart logic and advanced parameters beyond P1211.
