---
title: "Yaskawa A1000 CPF35 (AL-35) - Causes & Fix"
description: "CPF35 (often mistyped AL-35) means control circuit hardware failure on your Yaskawa A1000 VFD. Replace the control board."
pubDatetime: 2026-06-29T10:52:10Z
modDatetime: 2026-06-29T10:52:10Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Yaskawa A1000 Control Board (Main PCB)"
most_likely_cause: "damaged control board"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Cycle power off for 5 minutes then restart to see if the fault clears temporarily"
  - "Check input voltage with a voltmeter to confirm stable power within the drive's rated range"
  - "Inspect all wiring terminals between control board and power section for corrosion or looseness"
part_price: "$300-800"
---

## Yaskawa A1000 CPF35 (AL-35) — What It Means

CPF35 is a Control Circuit Error indicating that the drive's internal hardware has failed. The microprocessor on the control board has detected an internal error it cannot resolve, such as memory corruption, ADC failure, or logic circuit damage. This fault is often mistyped or misheard as AL-35 or AL35, but the official Yaskawa code is CPF35. The fault means irreversible hardware damage has occurred, typically to the control board or power board. Unlike software faults that reset with a parameter change, CPF35 requires physical hardware replacement to restore function.

## Before You Replace Anything

Some technicians replace the entire drive when only the control board has failed. Always check input voltage and connections first, then replace the control board alone if the power section tests good.

[Jump to Fix](#fix)

## Common Causes

- **Damaged control board (~50%)** Physical hardware failure of the main PCB due to age, voltage spikes, or thermal stress causes the microprocessor to detect an unrecoverable internal error.
- **Power supply instability (~20%)** Undervoltage or unstable input power causes the control circuit to malfunction and trigger a hardware fault.
- **Loose or corroded connections (~15%)** Poor wiring between the control board and power section creates intermittent signals that the processor interprets as hardware failure.
- **Environmental degradation (~10%)** High ambient temperature, dust, or moisture corrodes internal components on the control board over time.
- **Cumulative damage from prior faults (~5%)** Previous undervoltage events or other faults may have weakened the control board, leading to eventual failure.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault clear after cycling power off for 5 minutes?</summary>
<div class="dtree-body"><strong>Yes:</strong> The control board may be marginally functional but failing. Monitor closely and prepare to replace the board if the fault returns.<br><strong>No:</strong> The control board has suffered permanent damage. Proceed with input voltage checks and plan for hardware replacement.</div>
</details>

<details class="dtree"><summary>Is the input voltage stable and within the drive's rated range (e.g., 200-240V AC for 230V models)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Power supply is not the root cause. Focus on inspecting connections and preparing to replace the control board.<br><strong>No:</strong> Correct the power supply issue first. Unstable or low voltage may have damaged the control board already, so replacement may still be needed.</div>
</details>

<details class="dtree"><summary>Are all connections between the control board and power section tight and free of corrosion?</summary>
<div class="dtree-body"><strong>Yes:</strong> Wiring is not the issue. The control board itself has failed and needs replacement.<br><strong>No:</strong> Clean and tighten all connections, then cycle power. If CPF35 persists, the control board is damaged.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off all power** to the drive and lock out the disconnect for at least 5 minutes to allow capacitors to discharge.
2. **Restore power** and check if CPF35 clears. If it does, monitor the drive closely for recurrence and proceed with diagnostics.
3. **Measure input voltage** at the drive terminals with a voltmeter. For 230V models, confirm voltage is between 200 and 240V AC and stable. If voltage is low or erratic, correct the power supply issue.
4. **Inspect all wiring** between the control board and power section. Look for loose terminals, corroded connections, or damaged insulation. Tighten and clean any suspect connections.
5. **Review the fault log** on the drive display to check for prior undervoltage (Uv1) or other faults that may indicate a pattern of power-related stress on the control board.
6. **Verify control board seating** by opening the drive enclosure and ensuring the control board is fully inserted in its slot with no bent pins or missing connections.
7. **Replace the control board** if CPF35 persists after power cycling and connection checks. If the control board is unavailable or damage extends to the power section, replace the entire drive.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa A1000 Control Board (Main PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-al-35-fault-code&k=Yaskawa+A1000+Control+Board+%28Main+PCB%29&tag=errorcodefixes-20) \| Match the exact model and voltage rating of your drive. The control board is the primary component to replace for CPF35. |
| Yaskawa A1000 VFD (Complete Drive Replacement) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-al-35-fault-code&k=Yaskawa+A1000+VFD+%28Complete+Drive+Replacement%29&tag=errorcodefixes-20) \| If the control board alone is not available or if the power board is also damaged, replace the full drive unit. |

## When to Call a Pro

Call a qualified technician or an industrial controls specialist for CPF35. This fault requires working inside the drive enclosure with high-voltage DC bus capacitors present even after input power is removed. Replacing the control board demands careful handling of static-sensitive components, proper grounding, and verification that the power section is not also damaged. If you lack experience with VFD repair or do not have the tools to safely discharge and test high-voltage circuits, professional service is the safer and faster route. A technician can also review your facility's power quality and recommend surge protection if voltage spikes contributed to the failure.

**Rough cost:** A pro service call runs about $400-1200 for control board replacement or drive swap.

## See Also

- [Yaskawa A1000 oFA34 Fault - Causes & Fix](/posts/yaskawa-a1000-vfd-al-34-fault-code/)
- [Yaskawa A1000 AL-08 - Causes & Fix](/posts/yaskawa-a1000-vfd-al-08-fault-code/)
- [Yaskawa A1000 oL1 Fault - Causes & Fix](/posts/yaskawa-a1000-vfd-ol1-fault-code/)
- [Yaskawa GA800 E29 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-e29-fault-code/)
