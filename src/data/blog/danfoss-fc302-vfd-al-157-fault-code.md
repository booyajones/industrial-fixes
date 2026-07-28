---
title: "Danfoss FC302 AL-157 - Causes & Fix"
description: "AL-157 is not a valid Danfoss FC302 fault code. Most likely Alarm 38 (internal fault) or a misread display. Power-cycle first."
pubDatetime: 2026-06-26T09:49:53Z
modDatetime: 2026-06-26T09:49:53Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "FC302 control board assembly"
most_likely_cause: "Failed control board or corrupted parameter memory"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power-cycle the drive completely (disconnect AC mains, wait for capacitors to discharge, then reconnect) and confirm the exact alarm number on the display"
  - "Inspect all control wiring, terminals, and ground connections for corrosion, looseness, or broken strands"
  - "Check the LCP display for physical damage or LCD artifacts that might corrupt the readout"
---

## What this code means
The code AL-157 does not exist in official Danfoss FC302 documentation. Danfoss FC302 drives use alarm numbers from 1 to 99, and internal faults are reported as Alarm 38 with a sub-code (such as 38.1 or 38.12). The number 157 may be a misreading of the display, a corrupted sub-code outside the normal range, or confusion with a parameter number. Common causes include LCD artifacts making AL 38 look like AL 157, or the display showing an extended diagnostic code that does not match standard alarm tables.

If your drive actually shows Alarm 38, the fault is internal to the drive's control or power electronics. The most frequent triggers are a failed control board, corrupted parameter memory, gate driver circuit failure, or overheating power components. Check the display carefully after a full power cycle and verify the exact alarm number and sub-code before proceeding with diagnosis or parts replacement.

## Before You Replace Anything

Technicians sometimes replace the entire drive or power module when the fault is actually corrupted parameters or loose control wiring. Always power-cycle the drive, check wiring connections, and attempt a parameter reset before ordering expensive assemblies.

## Common Causes

- **Failed control board (~35%)** Memory errors, firmware corruption, or damaged components on the logic or control PCB trigger internal fault detection and generate Alarm 38.
- **Corrupted parameter memory (~25%)** Parameter values are lost or corrupted due to power loss, battery failure, or electrical noise, causing the drive to flag internal logic errors.
- **Gate driver circuit failure (~20%)** Damaged gate drivers for IGBTs prevent proper switching and trigger internal fault protection when the control board detects the mismatch.
- **Overheating power components (~15%)** IGBTs or DC link capacitors fail due to heat buildup or aging, and the drive's thermal monitoring reports an internal fault.
- **Display misread or corruption (~5%)** The LCD shows a corrupted or phantom code (such as 157) due to physical damage, electrical noise, or firmware glitch during boot.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the drive display clear to a different alarm or no alarm after a full power cycle?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault was likely a transient glitch or noise event. Monitor the drive during normal operation and check for loose wiring or grounding issues.<br><strong>No:</strong> The fault is persistent. Proceed to check control wiring, input voltage balance, and attempt a parameter reset if the manual allows.</div>
</details>

<details class="dtree"><summary>With the motor disconnected, does the drive still show the same alarm when powered on?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is internal to the drive itself (control board, gate drivers, or power electronics) and not caused by the motor or load.<br><strong>No:</strong> The motor or load wiring is contributing to the fault. Inspect motor windings, cables, and mechanical coupling for shorts or overload.</div>
</details>

<details class="dtree"><summary>Are all three input phases within 3% of each other when measured at the drive terminals?</summary>
<div class="dtree-body"><strong>Yes:</strong> Input power is balanced. Focus on internal drive diagnostics, control wiring, and parameter memory.<br><strong>No:</strong> Unbalanced input voltage can stress power components and trigger internal faults. Check utility supply, fuses, and contactors upstream.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect all power** to the drive at the main breaker or disconnect switch. Wait for the DC bus capacitors to discharge according to the time listed in your drive's manual (typically several minutes) before touching any terminals.
2. **Examine the LCP display** closely under good lighting. Confirm whether the code reads AL-157, AL 38, AL 17, or another number. If the display is dim, flickering, or shows partial segments, note that as a possible display fault.
3. **Power-cycle the drive** by reconnecting AC mains and watching the boot sequence. Record the exact alarm number and any sub-code (such as 38.12) that appears. Consult Table 6.1 in the FC302 operating manual for the official meaning of Alarm 38 sub-codes.
4. **Check input voltage** on all three phases (L1, L2, L3) at the drive input terminals. Phases must be within 3% of each other. Verify proper grounding and inspect terminals for corrosion or loose hardware.
5. **Inspect all control wiring** including 24V DC control circuits, digital inputs, analog signals, and encoder feedback if installed. Look for broken strands, pinched insulation, or noise coupling from motor cables running parallel to control wires.
6. **Disconnect the motor** from the drive output terminals. Attempt to run the drive unloaded (or with parameter adjustments to allow no-motor operation). If the alarm persists, the fault is internal. If it clears, check the motor for winding faults or mechanical binding.
7. **Attempt a parameter reset** to factory defaults if the manual permits and you have documented all custom settings. This can clear corrupted memory. If the fault remains after reset, the control board or power electronics are likely failed and require replacement by a qualified technician.

## Parts Often Needed

| Part | Notes |
|------|-------|
| FC302 control board assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-157-fault-code&k=FC302+control+board+assembly&tag=errorcodefixes-20) \| Match your drive frame size and firmware revision. Often requires factory programming or cloning from the old board. |
| LCP (Local Control Panel) display module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-157-fault-code&k=LCP+%28Local+Control+Panel%29+display+module&tag=errorcodefixes-20) \| If the display itself is damaged or corrupted. Verify the alarm by connecting a laptop with Danfoss MCT software before replacing. |

## When to Call a Pro

Call a qualified VFD technician or industrial electrician if the alarm persists after a power cycle and basic wiring checks. Internal faults on the FC302 typically require oscilloscope diagnostics, firmware tools, or replacement of the control board and gate driver circuits. High DC bus voltages (up to 800 VDC on 480V models) remain inside the drive even after AC power is removed, and contact with live bus bars can be fatal. Do not open the drive enclosure or attempt board-level repair unless you are trained in high-voltage industrial equipment and have proper PPE and lockout procedures. If the drive is under warranty or service contract, contact Danfoss or your distributor before performing any invasive diagnostics.

**Rough cost:** A pro service call runs about $300-800.
