---
title: "Yaskawa A1000 Er-05 Fault - Causes & Fix"
description: "Er-05 (No-Load Current Error) means auto-tuning failed because motor parameters don't match nameplate data. Verify T1 parameters first."
pubDatetime: 2026-06-28T10:20:42Z
modDatetime: 2026-06-28T10:20:42Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Motor power cable (shielded, 3-conductor)"
most_likely_cause: "Motor nameplate data entered in T1 parameters does not match the physical motor"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Compare every T1 parameter (T1-01 through T1-09) against the motor nameplate and correct any mismatches"
  - "Visually inspect motor terminal connections at U, V, W for tightness and corrosion"
  - "Disconnect the motor from the driven load if performing rotational auto-tuning"
no_buy_pct: "80%"
---

## Yaskawa A1000 Er-05 Fault — What It Means

The Er-05 fault code (No-Load Current Error) appears on Yaskawa A1000 drives during auto-tuning when the calculated no-load current value falls outside the acceptable range or is invalid. This happens when the drive cannot correctly learn motor parameters because the T1 group settings (motor nameplate data like voltage, current, frequency, speed, and power) do not match the actual motor connected to the drive. The fault also triggers if motor wiring is faulty, the load is too high during rotational tuning, or the tuning process is interrupted or takes too long.

This is strictly a tuning error that occurs when you run the auto-tune procedure (parameter A1-02). It does not indicate a drive hardware failure. The drive is telling you it cannot build an accurate motor model with the information and conditions provided. Fixing it requires matching your parameter entries to reality, checking physical connections, and running the tuning procedure under the right conditions.

## Before You Replace Anything

Technicians sometimes replace option cards or encoder cables when they see tuning errors, but Er-05 is not an encoder fault. Always verify T1 parameter entries and motor wiring continuity before ordering hardware.

[Jump to Fix](#fix)

## Common Causes

- **Incorrect T1 motor parameters (~50%)** Motor nameplate voltage, current, frequency, speed, or power entered in the T1 group does not match the physical motor connected to the drive.
- **Faulty motor wiring or terminations (~25%)** Open or shorted motor cable, loose terminal connections at the drive or motor, or unbalanced winding resistance stops the drive from reading current correctly.
- **Excessive load during rotational tuning (~15%)** Motor is coupled to a machine with more than 30% load or a mechanical brake is not fully lifted, preventing the drive from measuring true no-load current.
- **Encoder cable noise or poor termination (~10%)** PG cable interference or loose encoder connections cause signal errors that disrupt the tuning calculation when using closed-loop control.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Do the T1 parameter values (voltage, current, frequency, speed, power) exactly match every line on the motor nameplate?</summary>
<div class="dtree-body"><strong>Yes:</strong> Parameters are correct. Move to wiring inspection and measure motor winding resistance between U-V, V-W, and W-U for balance.<br><strong>No:</strong> Correct every mismatched T1 entry to match the nameplate, then restart auto-tuning. This resolves most Er-05 faults.</div>
</details>

<details class="dtree"><summary>Is the motor physically disconnected from the driven load (uncoupled) during rotational auto-tuning?</summary>
<div class="dtree-body"><strong>Yes:</strong> Load is not the problem. Check motor cable continuity and terminal tightness at both ends.<br><strong>No:</strong> Decouple the motor from the machine or switch to static auto-tuning mode to eliminate load interference.</div>
</details>

<details class="dtree"><summary>Are all three motor phase winding resistances within 5% of each other when measured with the drive powered off?</summary>
<div class="dtree-body"><strong>Yes:</strong> Windings are balanced. Check for encoder cable issues if using closed-loop control, or consult the manual for advanced tuning settings.<br><strong>No:</strong> The motor has an open or shorted winding. Repair or replace the motor before attempting tuning again.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power off the drive** and lockout/tagout the main disconnect before touching any wiring or terminals.
2. **Compare T1 parameters to the motor nameplate** line by line (rated voltage in T1-01, rated current in T1-02, rated frequency in T1-03, rated speed in T1-04, rated power in T1-05, poles in T1-06, and so on through T1-09). Correct every entry that does not match.
3. **Inspect motor terminal connections** at U, V, and W on both the drive output and the motor peckerhead. Tighten any loose lugs and look for signs of overheating, corrosion, or melted insulation.
4. **Measure motor winding resistance** with a multimeter between U-V, V-W, and W-U with the drive powered off. Values should be balanced within 5%. If one reading is open (infinite) or significantly different, the motor or cable is faulty.
5. **Decouple the motor from the load** if you are performing rotational auto-tuning. Disconnect the coupling or belt. If decoupling is not possible, set A1-02 to static auto-tuning mode instead.
6. **Restart the auto-tuning procedure** by setting A1-02 to the correct tuning method (rotational or static) and initiating the run. Monitor the drive display for completion or any new error codes.
7. **If Er-05 persists after correcting parameters and wiring**, check encoder cable termination at both the option card and the motor encoder if using closed-loop control. Replace the PG cable if you see damaged wires or loose pins inside the connector.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor power cable (shielded, 3-conductor) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-al-05-fault-code&k=Motor+power+cable+%28shielded%2C+3-conductor%29&tag=errorcodefixes-20) \| Replace if cable insulation is damaged, conductors are open, or resistance is unbalanced between phases. |
| PG encoder cable (shielded twisted-pair) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-al-05-fault-code&k=PG+encoder+cable+%28shielded+twisted-pair%29&tag=errorcodefixes-20) \| Replace if using closed-loop control and you suspect noise or physical damage to the encoder feedback cable. |

## When to Call a Pro

Call a qualified drive technician or electrician if you are not familiar with VFD parameter programming, if you cannot safely measure motor winding resistance with a multimeter, or if the motor wiring is inside a control panel requiring high-voltage lockout. A professional should also handle encoder alignment and option card installation if you are running closed-loop control. If the motor itself has a shorted or open winding, a motor shop will need to rewind or replace it. Most Er-05 faults are parameter entry mistakes that a technician can correct in minutes, so a service call is often faster and safer than trial and error.

**Rough cost:** A pro service call runs about $150-400 for a service call to verify parameters, check wiring, and complete tuning.

## See Also

- [Yaskawa GA800 oV Fault — DC Overvoltage Fix](/posts/yaskawa-ga800-error-ov/)
- [Yaskawa GA800 A.135 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-a-135-fault-code/)
- [Yaskawa GA800 E63 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-e63-fault-code/)
- [Yaskawa A1000 CPF06 - Causes & Fix](/posts/yaskawa-a1000-vfd-cpf06-fault-code/)
