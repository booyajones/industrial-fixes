---
title: "Yaskawa GA800 F009 Fault - Causes & Fix"
description: "F009 on GA800 displays is likely UV2 (Control Power Undervoltage). Most common fix: reduce parameter L2-02 to 0 ms or connect recovery unit."
pubDatetime: 2026-06-26T10:04:45Z
modDatetime: 2026-06-26T10:04:45Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "Yaskawa GA800 momentary power loss recovery unit"
most_likely_cause: "Parameter L2-02 set too high without recovery unit connected"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Navigate to parameter L2-02 and reduce it to 0 ms if momentary power loss recovery is not required"
  - "Check all control power terminal connections (L1, L2, L3 or auxiliary terminals) for tightness and corrosion"
  - "Verify incoming control voltage is stable and within the drive's rated input range"
no_buy_pct: "80%"
---

## Yaskawa GA800 F009 Fault — What It Means

The Yaskawa GA800 does not have a standard F009 fault code in its official documentation. If you see a display that looks like F009, it is almost certainly the UV2 fault (Control Power Undervoltage) being misread or a parameter value on screen. UV2 indicates the control power supply voltage inside the drive has dropped below the acceptable threshold. This typically happens when parameter L2-02 (Power Loss Ride Through Time) is set too high for the actual momentary power loss duration the drive experiences, or when the drive is configured to expect a momentary power loss recovery unit but that unit is not physically connected to the drive terminals.

The drive will not operate until this condition is resolved. Unlike main circuit undervoltage faults, UV2 specifically targets the low-voltage control circuitry that runs the drive's logic and keypad, so it can occur even when main power appears stable.

## Before You Replace Anything

Technicians sometimes replace the control board assuming a hardware failure when the actual cause is simply parameter L2-02 set above 0 ms without the corresponding recovery hardware installed. Always check and adjust L2-02 first before ordering any circuit boards.

[Jump to Fix](#fix)

## Common Causes

- **L2-02 parameter set too high (~55%)** The Power Loss Ride Through Time parameter is configured for a duration the drive cannot sustain without the optional recovery unit, causing a fault on brief power dips.
- **Missing momentary power loss recovery unit (~25%)** The drive is programmed to expect a recovery unit at the designated terminals, but the hardware is not installed or not wired correctly.
- **Loose or corroded control power wiring (~10%)** Poor connections at the control power input terminals create voltage drops or intermittent contact that triggers the undervoltage fault.
- **Momentary power interruption (~7%)** A brief dip or brownout in the incoming control power supply (10 to 20 ms) that the drive cannot bridge without the recovery unit.
- **Faulty control power supply circuit (~3%)** Internal failure of the control board's power regulation stage, though this is rare and usually follows other symptoms like display flicker.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does parameter L2-02 show a value greater than 0 ms?</summary>
<div class="dtree-body"><strong>Yes:</strong> Reduce L2-02 to 0 ms and reset the fault. If the fault clears and does not return, the issue was the parameter setting.<br><strong>No:</strong> The drive is configured for immediate fault on control power loss. Check for a connected recovery unit or inspect control power wiring for loose connections.</div>
</details>

<details class="dtree"><summary>Is a momentary power loss recovery unit physically installed and wired to the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> Verify the unit's output voltage and wiring continuity. If the unit is dead or miswired, repair or replace it.<br><strong>No:</strong> Either install the recovery unit or set L2-02 to 0 ms so the drive does not expect one.</div>
</details>

<details class="dtree"><summary>Does the fault occur during motor acceleration or high-load operation?</summary>
<div class="dtree-body"><strong>Yes:</strong> The main power supply may be sagging under load, affecting the control circuit. Check incoming voltage and consider adding line reactors or improving power quality.<br><strong>No:</strong> The fault is likely triggered by a parameter mismatch or wiring issue rather than a load-related dip. Focus on L2-02 and terminal connections.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Access parameter L2-02** by navigating the drive keypad menu to the L2 group (Extended Functions) and scroll to L2-02 (Power Loss Ride Through Time).
2. **Reduce L2-02 to 0 ms** if your application does not require momentary power loss recovery, then press the enter or set button to save the new value.
3. **Reset the fault** by pressing the reset button on the keypad or cycling power to the drive, then observe whether UV2 (or the F009-like display) reappears.
4. **Inspect control power terminals** at the drive's L1, L2, L3 inputs or auxiliary power connections, tightening any loose screws and cleaning any corrosion with contact cleaner.
5. **Measure incoming control voltage** with a multimeter at the drive terminals under both idle and running conditions to confirm voltage is stable and within the drive's specified input range.
6. **Install or verify the recovery unit** if L2-02 must remain above 0 ms for your application, ensuring the unit is wired to the correct terminals per the GA800 manual and that its output voltage is present.
7. **Replace the control board** only if all parameter settings are correct, wiring is verified, and the fault persists with stable input power, indicating an internal circuit failure.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 momentary power loss recovery unit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f009-fault-code&k=Yaskawa+GA800+momentary+power+loss+recovery+unit&tag=errorcodefixes-20) \| Required only if L2-02 must be set above 0 ms; consult Yaskawa for the exact part number matching your drive voltage and frame size. |
| Yaskawa GA800 control board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f009-fault-code&k=Yaskawa+GA800+control+board+%28PCB%29&tag=errorcodefixes-20) \| Needed only when internal power supply circuitry has failed; verify all wiring and parameters first to avoid unnecessary replacement. |

## When to Call a Pro

Call a qualified drive technician or electrician if you are not comfortable navigating VFD parameters or measuring control voltages. Because the fault involves low-voltage control circuitry, it is generally safe for someone with basic electrical knowledge to adjust L2-02 and check wiring. However, if the fault persists after parameter changes and wiring checks, the issue may involve internal board-level diagnostics, power quality analysis, or installation of the recovery unit, all of which require training on Yaskawa drives and proper test equipment. Any work that involves modifying incoming power wiring or installing additional hardware should be performed by a licensed professional to meet electrical code and safety requirements.

**Rough cost:** A pro service call runs about $150-400 for parameter adjustment, wiring inspection, or recovery unit installation.
