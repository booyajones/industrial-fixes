---
title: "Yaskawa A1000 Uv4 Fault - Causes & Fix"
description: "Uv4 means gate drive board undervoltage. The drive shuts down to protect the IGBTs. Most common fix: replace the gate drive board."
pubDatetime: 2026-06-11T10:02:47Z
modDatetime: 2026-06-11T10:02:47Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Yaskawa A1000 Gate Drive Board"
most_likely_cause: "gate drive board failure"
likelihood: "the most common cause"
diy_or_pro: "pro"
---

## What this code means
The Uv4 fault code stands for Gate Drive Board Undervoltage. The internal voltage supply to the gate drive board (the circuit that controls the IGBTs or transistors) has dropped below the specified threshold. The drive cannot properly switch the output transistors when this happens, which creates a risk of uneven switching and potential short circuits. The A1000 immediately shuts down and displays Uv4 to protect the hardware from catastrophic failure.

This code is distinct from Uv1 (DC Bus Undervoltage), Uv2 (Control Power Undervoltage), or Uv3 (Soft Charge Circuit Fault). Uv4 is specific to the gate drive circuitry. The fault indicates low voltage reaching the gate drive, but the root causes are typically hardware failures or supply issues rather than a simple power dip.

## Before You Replace Anything

Technicians sometimes replace the main power board first, but a simple voltage measurement at the gate drive board supply pins will show whether the power board is delivering correct voltage or the gate board itself has failed.

## Common Causes

- **Gate drive board failure (~55%)** Capacitors on the gate drive board have leaked or the voltage regulator circuit has failed, causing the board to no longer maintain proper voltage.
- **Main power board degradation (~25%)** The transformer or regulator on the main power board that supplies voltage to the gate drive has failed, starving the gate board of power.
- **Loose internal connections (~10%)** Poor contact between the gate drive board and the main power board or control board leads to voltage drops at the connector.
- **Insufficient input power (~7%)** The main input voltage to the drive is low or a phase is missing, reducing the downstream supply to the gate drive board.
- **Transient power loss (~3%)** A momentary spike or drop in the main input power caused the gate drive supply to dip briefly and trigger the fault.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault clear after cycling power and waiting five minutes?</summary>
<div class="dtree-body"><strong>Yes:</strong> The issue may have been a transient power event. Monitor the drive under load and check for recurring faults.<br><strong>No:</strong> The fault is hardware-related. Proceed with internal inspection and board replacement.</div>
</details>

<details class="dtree"><summary>Is the main input voltage to the drive within the specified range for your A1000 model?</summary>
<div class="dtree-body"><strong>Yes:</strong> Input power is not the problem. Focus on the gate drive board and internal power supply circuits.<br><strong>No:</strong> Correct the input voltage issue or resolve the phase loss before diagnosing further.</div>
</details>

<details class="dtree"><summary>After reseating all internal connectors, does the Uv4 fault still appear immediately on startup?</summary>
<div class="dtree-body"><strong>Yes:</strong> A board has failed. Replace the gate drive board first, then the main power board if needed.<br><strong>No:</strong> A loose connection was the cause. Verify the drive runs normally under load.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Cycle power completely.** Turn off the input to the drive, wait for the display to blank, then wait five minutes for internal capacitors to discharge before turning it back on.
2. **Observe fault behavior.** If Uv4 clears and the drive runs normally, it may have been a transient issue. If the fault returns immediately, proceed with internal diagnostics.
3. **Open the drive enclosure and inspect connections.** Check all connectors between the control board, main power board, and gate drive board. Reseat any loose cards and look for bent pins.
4. **Verify main input voltage.** Measure the input voltage at the drive terminals and confirm it is within the specified range for your A1000 model. Check for phase loss.
5. **Replace the gate drive board.** If input power is correct and connections are tight, replace the gate drive board. This is the most common fix for Uv4.
6. **Replace the main power board if needed.** If the new gate drive board does not resolve the fault, the transformer or regulator on the main power board has likely failed.
7. **Test under load.** After replacement, cycle power and run the drive under no load, then under increasing load. Monitor for any recurring faults or abnormal behavior.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa A1000 Gate Drive Board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-uv4-fault-code&k=Yaskawa+A1000+Gate+Drive+Board&tag=errorcodefixes-20) \| Match the part number to your specific A1000 frame size and voltage rating. |
| Yaskawa A1000 Main Power Board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-uv4-fault-code&k=Yaskawa+A1000+Main+Power+Board&tag=errorcodefixes-20) \| Required if the gate drive board replacement does not clear the fault. |

## When to Call a Pro

Call a qualified technician or industrial electrician for all Uv4 diagnostics and repair. The work requires opening the drive enclosure, which exposes high-voltage DC bus capacitors and power circuits. Even after the drive is powered down, capacitors can hold a lethal charge for several minutes. A technician will follow lockout-tagout procedures, discharge capacitors safely, and use proper test equipment to isolate the failed board. Replacing the gate drive board or main power board also requires knowledge of the drive architecture and proper ESD handling. Incorrect installation can destroy the new board or cause a fault at startup. Only attempt this repair if you are trained on high-voltage VFD service.

**Rough cost:** A pro service call runs about $400-900.
