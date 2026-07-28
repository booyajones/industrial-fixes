---
title: "Yaskawa A1000 VFD Er-04 - Causes & Fix"
description: "Er-04 means line-to-line resistance error during auto-tuning. Most often caused by incorrect motor nameplate data entered into T1 parameters."
pubDatetime: 2026-06-28T10:19:45Z
modDatetime: 2026-06-28T10:19:45Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Motor cable (three-phase, properly rated for VFD use)"
most_likely_cause: "incorrect motor nameplate data entered in T1 parameters"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify T1 parameters match the motor nameplate exactly (resistance, voltage, rated current, horsepower)"
  - "Inspect motor terminals and drive output terminals for loose or corroded connections"
  - "Measure resistance between motor phases U-V, V-W, and W-U to confirm balanced values"
no_buy_pct: "60%"
---

## What this code means
The Er-04 fault (often misread as AL-04) indicates a line-to-line resistance error during the auto-tuning process on a Yaskawa A1000 variable frequency drive. The drive detected a discrepancy in the motor's measured resistance between phases (T1) that does not match the expected values or the tuning process exceeded parameter limits. This is strictly a motor resistance and tuning fault, not an encoder or feedback error.

The fault appears when the auto-tuning routine cannot validate the motor's electrical characteristics against the parameters you entered. It means either the motor nameplate data entered into the T1 parameters (resistance, voltage, rated current, horsepower) is incorrect, the motor wiring has a fault, or the motor itself has an internal problem causing resistance drift. The drive will not complete tuning until the mismatch is resolved.

## Before You Replace Anything

Do not replace the option card or control board for Er-04. This is a motor parameter and wiring fault. Verify the motor nameplate data and inspect all motor cable connections before replacing any drive components.

## Common Causes

- **Incorrect motor nameplate data (~50%)** The resistance, voltage, current, or horsepower values entered in T1 parameters do not match the actual motor nameplate, causing the tuning algorithm to fail validation.
- **Loose or broken motor cable connections (~25%)** Loose terminal screws, broken strands, or damaged insulation at the drive output or motor input create intermittent or high-resistance paths that skew the tuning measurements.
- **Motor wiring errors (~15%)** Open circuit in one phase, short to ground, or crossed wiring between motor phases prevents accurate resistance measurement during auto-tuning.
- **Motor overheated or mechanically unloaded (~7%)** Running auto-tuning on a hot motor or with the motor detached from the machine causes resistance values to drift outside expected limits.
- **Faulty motor windings (~3%)** Internal motor faults such as shorted turns or unbalanced winding resistance produce inconsistent line-to-line measurements that fail the tuning check.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Do the T1 parameter values (resistance, voltage, current, HP) exactly match the motor nameplate?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is likely wiring or motor related. Proceed to inspect motor cable connections and measure phase-to-phase resistance.<br><strong>No:</strong> Correct the T1 parameters to match the motor nameplate exactly, then restart auto-tuning. Most Er-04 faults clear after entering correct data.</div>
</details>

<details class="dtree"><summary>Are all motor cable connections tight and free of corrosion at both the drive output and motor terminal box?</summary>
<div class="dtree-body"><strong>Yes:</strong> Measure resistance between U-V, V-W, and W-U. If values are unbalanced or outside motor specs, replace the motor cable or check for internal motor faults.<br><strong>No:</strong> Tighten all terminal screws, clean corrosion, and inspect for broken wire strands. Re-run auto-tuning after repairs.</div>
</details>

<details class="dtree"><summary>Is the motor cool to the touch and mechanically coupled to the load during auto-tuning?</summary>
<div class="dtree-body"><strong>Yes:</strong> If parameters and wiring are correct but Er-04 persists, the motor may have internal winding faults. Test with a megohmmeter or replace the motor.<br><strong>No:</strong> Allow the motor to cool to ambient temperature and make sure it is coupled to the machine before running auto-tuning. Hot or unloaded motors can produce unstable resistance readings.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive** and lock out the disconnect. Wait for the DC bus capacitors to discharge (at least five minutes) before touching any terminals.
2. **Record the motor nameplate data** including rated voltage, frequency, horsepower (or kW), full-load current, and resistance (if listed). If resistance is not on the nameplate, consult the motor manufacturer's specification sheet.
3. **Access T1 parameters** in the drive menu (typically T1-01 through T1-06). Compare each value to the motor nameplate. Correct any mismatches, paying close attention to voltage and current ratings.
4. **Inspect motor cable connections** at both the drive output terminals (U, V, W) and the motor terminal box. Tighten all screws to the torque specified in the drive manual. Look for broken wire strands, cracked insulation, or corrosion.
5. **Measure phase-to-phase resistance** with a digital multimeter. Disconnect the motor from the drive first. Measure U-V, V-W, and W-U. Values should be balanced (within a few percent of each other) and match the motor nameplate or spec sheet if available.
6. **Restart auto-tuning** after verifying parameters and wiring. Follow the drive's auto-tuning procedure (usually accessed via the keypad menu). The drive will run the motor briefly and measure electrical characteristics.
7. **Monitor the tuning process** for completion. If Er-04 reappears, verify the motor is cool, mechanically coupled to the load, and not experiencing a fault. If all checks pass, replace the motor cable or test the motor windings with a megohmmeter for internal faults.
8. **Clear the fault** and run a test at low speed. If the drive operates normally, the tuning is complete. If faults persist, consult a qualified technician or contact Yaskawa technical support.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor cable (three-phase, properly rated for VFD use) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-al-04-fault-code&k=Motor+cable+%28three-phase%2C+properly+rated+for+VFD+use%29&tag=errorcodefixes-20) \| Only if existing cable is damaged, has broken strands, or shows high resistance. Must match drive output voltage and motor current rating. |
| Three-phase motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-al-04-fault-code&k=Three-phase+motor&tag=errorcodefixes-20) \| Only if internal winding faults are confirmed by megohmmeter testing or if phase-to-phase resistance is severely unbalanced and cable is verified good. |

## When to Call a Pro

Call a qualified electrician or automation technician if you are not familiar with VFD parameter programming, motor nameplate interpretation, or electrical testing with a multimeter. High-voltage work on the drive input (line power) or output (motor cable) requires lockout/tagout procedures and proper PPE. If the fault persists after verifying nameplate data and wiring, a technician can perform megohmmeter testing on the motor windings, check for grounding faults, and determine whether the motor or drive needs replacement. Auto-tuning requires understanding of motor control theory to interpret results and troubleshoot edge cases. Professional service typically costs $150 to $400 for diagnosis, parameter correction, and re-tuning.

**Rough cost:** A pro service call runs about $150-400 for wiring inspection, parameter correction, and re-tuning.
