---
title: "Frigidaire Range F92 Error Code - Causes & Fix"
description: "F92 means maximum oven door open time exceeded. Door lock motor or latch is stuck. Most cases need a new door lock assembly."
pubDatetime: 2026-06-13T05:38:51Z
modDatetime: 2026-06-13T05:38:51Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - appliance
  - oven
  - frigidaire
money_part: "Door lock assembly (motor and latch)"
most_likely_cause: "Failed door lock motor or latch motor"
likelihood: "the most common cause"
diy_or_pro: "diy"
free_checks:
  - "Power-cycle the range (flip breaker or unplug for 30 seconds) to clear temporary glitches."
  - "Inspect the door latch for debris, bent metal, or visible damage that would prevent smooth travel."
  - "Open and close the door manually to confirm the latch moves freely and engages the strike plate."
part_price: "$45-90"
---

## Frigidaire Range F92 Error Code — What It Means

The F92 error code means the oven's control system detected that the door lock mechanism remained in the open position for longer than the factory-preset safety limit (typically 120 seconds or 2 minutes). The code triggers when the system fails to confirm that the door has fully locked when a self-clean or lockout cycle is initiated, or when the latch does not return to the unlocked position within the allowed time. F92 is part of a family of door lock codes (F90 through F94) that all signal different timeout or failure conditions in the latch assembly.

This code does not mean the door is physically ajar. It means the electronic lock cannot complete its cycle. The control board sends power to the door lock motor to move the metal latch into the locked position, and a microswitch signals back to confirm the lock is engaged. If the board never receives that confirmation signal within the timeout window, it throws F92 and halts the oven cycle for safety.

## Before You Replace Anything

Many homeowners replace the main control board first, assuming an electronics fault. Always test the door lock motor resistance with a multimeter and inspect the latch for physical jams before swapping the board.

[Jump to Fix](#fix)

## Common Causes

- **Failed door lock motor (latch motor) (~45%)** The motor that physically moves the latch is worn out, has broken windings, or is internally stuck, preventing it from pulling the latch into the locked position or releasing it completely.
- **Obstructed or broken latch mechanism (~25%)** The metal latch hook is bent, jammed by debris, or the linkage connecting the motor to the latch is broken, preventing smooth movement.
- **Faulty door lock switch (microswitch) (~15%)** The switch that tells the control board the door is locked or unlocked is stuck open, shorted, or has lost contact, so the board never receives the confirmation signal and times out.
- **Wiring harness issues (~10%)** Broken wires, frayed connectors, or corroded terminals between the door lock motor, the microswitch, and the main control board prevent proper signal transmission.
- **Control board (ERC/main board) failure (~5%)** The logic board may be sending incorrect voltage to the motor or failing to read the microswitch signal correctly due to a failed relay or damaged component on the board.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the latch move smoothly by hand when you open and close the door?</summary>
<div class="dtree-body"><strong>Yes:</strong> The mechanical linkage is likely intact. The problem is electrical (motor, switch, or wiring). Proceed to multimeter testing of the motor and switch.<br><strong>No:</strong> The latch is obstructed or broken. Remove the door or inner panel to inspect the latch assembly for bent parts, debris, or broken linkage before testing electrical components.</div>
</details>

<details class="dtree"><summary>After a power reset (30 seconds unplugged), does the F92 code return immediately when you start a self-clean cycle?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is persistent hardware (motor, switch, or board). Begin resistance testing of the motor and switch.<br><strong>No:</strong> The code may have been a temporary glitch or a one-time event. Monitor the oven for a few cycles. If it does not return, no repair is needed.</div>
</details>

<details class="dtree"><summary>When you measure resistance across the door lock motor terminals, do you get a reading between 200 and 400 Ohms?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor windings are intact. Check the microswitch and wiring harness for continuity. If those pass, suspect the control board.<br><strong>No:</strong> A reading of 0 Ohms (short) or infinite/OL (open windings) confirms a failed motor. Replace the door lock assembly.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect power** to the range by unplugging it or flipping the circuit breaker off. Wait 30 seconds, then restore power and test if the code clears.
2. **Open the oven door** and manually inspect the latch assembly. Look for bent metal, debris in the latch track, or broken linkage. Clean any obstructions and confirm the latch slides freely.
3. **Remove the oven door** (if needed for access) by opening it fully, releasing the hinge locks, and lifting straight up. Set it aside on a protected surface.
4. **Access the door lock assembly** by removing the inner door panel or top control panel (consult your model's service manual for screw locations). Disconnect the wire harness from the motor and microswitch.
5. **Test the door lock motor** with a multimeter set to resistance (Ohms). Measure across the motor terminals. A healthy motor typically reads 200 to 400 Ohms. A reading of 0 Ohms (short) or infinite/OL (open) means the motor is failed.
6. **Test the door lock microswitch** for continuity. The switch should show continuity (closed circuit) in one position and open circuit in the other as you manually move the latch. No change indicates a stuck or failed switch.
7. **Replace the door lock assembly** if the motor or switch is defective. Install the new assembly, reconnect the wire harness, and reassemble the door or panel. Restore power and run a test cycle to confirm the code is cleared.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Door lock assembly (motor and latch) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-frigidaire-range-f92-error-code&k=Door+lock+assembly+%28motor+and+latch%29&tag=errorcodefixes-20) \| Verify your model number on the Frigidaire parts site. Many assemblies include motor, latch, and microswitch as one unit. |
| Door lock microswitch | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-frigidaire-range-f92-error-code&k=Door+lock+microswitch&tag=errorcodefixes-20) \| Available separately on some models if the motor tests good and only the switch is faulty. |

## When to Call a Pro

Call a professional if you are uncomfortable working with live voltage testing or disassembling the oven door and control panels. A technician has the wiring diagrams and can quickly isolate whether the fault is in the lock assembly, the harness, or the main control board. Also call a pro if you have replaced the door lock assembly and the F92 code persists, since that points to a control board or wiring fault that requires trace-level diagnostics and possibly a board swap under warranty.

**Rough cost:** DIY runs about $50-120 in parts, 45-90 min. A pro service call runs about $150-300.
