---
title: "Yaskawa GA800 E58 Fault - Causes & Fix"
description: "E58 is a soft-charge answerback fault: the drive's precharge bypass relay did not confirm correct operation. Replace the control board or drive."
pubDatetime: 2026-06-06T11:44:06Z
modDatetime: 2026-06-06T11:44:06Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
most_likely_cause: "Failed soft-charge bypass relay or contact in the drive power section"
likelihood: "the most common cause"
diy_or_pro: "pro"
money_part: "Yaskawa GA800 control board (model-specific)"
---

## Yaskawa GA800 E58 Fault — What It Means

The E58 fault on a Yaskawa GA800 VFD is a soft-charge answerback fault. During power-up, the drive uses a precharge circuit to safely charge the DC bus capacitors through a resistor, then bypasses that resistor with a relay or contactor. The drive expects an answerback signal confirming the bypass relay has closed correctly. If that confirmation is missing or inconsistent, the drive trips E58. This is a power-up and DC bus precharge circuit problem, not a motor overload or output-phase fault.

The fault indicates that the soft-charge bypass relay or contact has failed, the control board circuitry that monitors or commands the relay is damaged, or the entire drive power section has degraded. Yaskawa's maintenance counter U4-06 (PreChargeRelayMainte) tracks relay life. If the counter is over 90%, the drive or board should be replaced.

## Before You Replace Anything

Technicians sometimes replace the entire drive without first checking the U4-06 maintenance counter and attempting a simple power cycle. Check the counter and re-energize the drive before ordering a replacement.

[Jump to Fix](#fix)

## Common Causes

- **Failed soft-charge bypass relay** The relay or contactor that bypasses the precharge resistor has failed mechanically or electrically and cannot provide the expected answerback signal.
- **Damaged control board circuitry** The control board that monitors or commands the relay has a fault in the relay driver or feedback circuit.
- **Precharge relay end-of-life** The maintenance counter U4-06 (PreChargeRelayMainte) is over 90%, indicating the relay has reached its rated life and should be replaced.
- **Power section failure** Broader degradation in the drive power section prevents the precharge circuit from operating correctly.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault clear after removing power for 30 seconds and re-energizing the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault may have been transient. Monitor the drive and check the U4-06 counter for relay life. If the counter is below 90%, continue normal operation.<br><strong>No:</strong> The fault is persistent. Proceed to check the U4-06 maintenance counter and prepare for control board or drive replacement.</div>
</details>

<details class="dtree"><summary>Is the U4-06 (PreChargeRelayMainte) maintenance counter reading over 90%?</summary>
<div class="dtree-body"><strong>Yes:</strong> The soft-charge bypass relay has reached end-of-life. Replace the control board or the entire drive per Yaskawa guidance.<br><strong>No:</strong> The relay life is acceptable, so the fault is likely due to a failed relay contact or control board circuitry. Inspect the relay path and control board.</div>
</details>

<details class="dtree"><summary>Does the fault recur immediately on every power-up after inspection?</summary>
<div class="dtree-body"><strong>Yes:</strong> The soft-charge bypass relay or control board has failed. Replace the control board or drive.<br><strong>No:</strong> The fault may be intermittent. Collect model number, serial number, failure information, application details, and runtime history, then contact Yaskawa technical support.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Remove power** from the drive and wait 30 seconds for the DC bus capacitors to discharge, then re-energize the drive and observe whether the E58 fault clears.
2. **Check the U4-06 maintenance counter** (PreChargeRelayMainte) in the drive's monitoring menu to evaluate the soft-charge bypass relay life percentage.
3. **If the counter is over 90%**, prepare to replace the control board or the entire drive per Yaskawa's guidance, as the relay has reached end-of-life.
4. **If the fault persists and the counter is below 90%**, inspect the soft-charge bypass relay and contact circuit in the drive power section for visible damage or loose connections.
5. **Test the control board circuitry** that monitors and commands the relay using a multimeter, checking for proper voltage signals and continuity in the relay coil and feedback paths (consult your model's schematic for test points).
6. **Replace the control board** if the relay circuit tests show control board faults, or replace the entire drive if the power section is degraded.
7. **Collect detailed information** (model/spec number, serial number, failure details, application, and runtime history) and contact Yaskawa technical support if the fault remains unresolved after these steps.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 control board (model-specific) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e58-fault-code&k=Yaskawa+GA800+control+board+%28model-specific%29&tag=errorcodefixes-20) \| Required if U4-06 counter is over 90% or control board circuitry is damaged. Match your drive's model and spec code. |
| Yaskawa GA800 VFD (complete replacement unit) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e58-fault-code&k=Yaskawa+GA800+VFD+%28complete+replacement+unit%29&tag=errorcodefixes-20) \| Required if the fault persists after control board replacement or if the power section has broader degradation. |

## When to Call a Pro

Call a qualified technician or VFD specialist immediately. The E58 soft-charge answerback fault involves the drive's internal power section, high-voltage DC bus circuitry, and control board diagnostics that require specialized test equipment and knowledge of VFD precharge circuits. Attempting to open the drive or probe high-voltage circuits without proper training and lockout/tagout procedures can result in lethal electric shock, even after disconnecting input power, because the DC bus capacitors store dangerous voltages. A technician will safely verify the precharge relay operation, check the U4-06 maintenance counter, and determine whether control board replacement or full drive replacement is needed. If your facility does not have in-house VFD expertise, contact Yaskawa technical support or an authorized distributor to arrange service or return for repair.

**Rough cost:** A pro service call runs about $500-2000 depending on whether control board replacement or full drive replacement is needed.

## See Also

- [Yaskawa A1000 rH Fault Code - Causes & Fix](/posts/yaskawa-a1000-vfd-rh-fault-code/)
- [Yaskawa A1000 oPr Fault Code - Causes & Fix](/posts/yaskawa-a1000-vfd-opr-fault-code/)
- [Yaskawa GA800 E72 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-e72-fault-code/)
- [Yaskawa GA800 VFD E60 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-e60-fault-code/)
