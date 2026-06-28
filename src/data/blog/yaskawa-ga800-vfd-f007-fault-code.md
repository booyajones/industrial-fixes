---
title: "Yaskawa GA800 F007 Fault - Causes & Fix"
description: "F007 is not a standard GA800 code. You likely have PF (Phase Loss), meaning input power is unstable or a phase is missing. Check wiring."
pubDatetime: 2026-06-26T10:02:55Z
modDatetime: 2026-06-26T10:02:55Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "Input terminal block or wiring harness"
most_likely_cause: "Loose or corroded input wiring at L1, L2, or L3 terminals"
likelihood: "the most frequent cause"
diy_or_pro: "pro"
free_checks:
  - "Check that all upstream breakers and disconnects are fully closed and not tripped"
  - "Inspect the input terminal block (L1, L2, L3) for loose screws, discoloration, or signs of arcing"
  - "Measure AC voltage between all three phase pairs at the drive input terminals to confirm all phases are present and balanced"
no_buy_pct: "60%"
---

## Yaskawa GA800 F007 Fault — What It Means

The Yaskawa GA800 does not use an F007 fault code in its standard fault library. The code you are seeing is most likely PF (Phase Loss), which indicates the drive has detected that one or more phases of the incoming AC power are missing, unstable, or experiencing excessive voltage fluctuation. This triggers a protective shutdown to prevent damage to the drive's internal components.

The PF fault means the drive input power voltage is changing too much or there is input phase loss due to a lost phase or loose wiring at the input terminals. This is a power-quality issue, not a motor or mechanical problem, though it can prevent the drive from running the motor safely.

## Before You Replace Anything

Technicians sometimes replace the drive board or rectifier section when the real issue is simply loose input terminal screws or a blown fuse upstream. Always measure and tighten input connections and verify upstream power first before ordering internal drive components.

[Jump to Fix](#fix)

## Common Causes

- **Loose or corroded input terminals (~40%)** The most frequent cause is loose connections at the drive's input terminals (L1, L2, L3), leading to intermittent contact or phase loss.
- **Upstream power component failure (~30%)** Blown fuses, tripped breakers, or a failed contactor in the upstream power distribution supplying the drive.
- **Unbalanced input voltage (~20%)** Severe voltage imbalance (often greater than 3 to 5 percent) between phases can trigger this fault even if all phases are present.
- **Utility power fluctuation (~10%)** External utility grid voltage sags, surges, or brownouts that cause the drive to see unstable input power.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Do you measure balanced three-phase voltage (within 3 percent) at the drive input terminals L1, L2, and L3?</summary>
<div class="dtree-body"><strong>Yes:</strong> Input power is present and balanced, so inspect terminal tightness and the drive's internal input monitoring settings or sensors.<br><strong>No:</strong> You have an upstream power issue. Check fuses, breakers, contactors, and transformer connections feeding the drive.</div>
</details>

<details class="dtree"><summary>Are all input terminal screws tight and free of corrosion or discoloration?</summary>
<div class="dtree-body"><strong>Yes:</strong> Wiring is good, so the fault may be due to utility voltage fluctuation or a drive parameter setting. Review the fault log and consult the manual.<br><strong>No:</strong> Loose or corroded terminals are causing intermittent phase loss. De-energize, clean, re-torque, and test.</div>
</details>

<details class="dtree"><summary>Does the fault occur immediately on power-up or only during motor operation?</summary>
<div class="dtree-body"><strong>Yes:</strong> If it trips on power-up, the issue is with the input power supply. If it trips during run, check for voltage drop under load or upstream contactor chatter.<br><strong>No:</strong> If the fault does not trip consistently, you may have an intermittent connection or a transient utility voltage event.</div>
</details>

## Step-by-Step Fix {#fix}

1. **De-energize the system** and lock out the upstream disconnect or breaker supplying the drive.
2. **Measure AC voltage** at the drive input terminals (L1-L2, L2-L3, L3-L1) using a calibrated multimeter to confirm all phases are present and within 3 percent of each other.
3. **Open the drive cover** and inspect the input terminal block (L1, L2, L3) for loose screws, corrosion, discoloration, or signs of arcing.
4. **Re-torque input terminals** to the manufacturer's specification (typically 2.5 to 3.5 Nm for GA800 drives, though verify in the manual) and clean any corrosion.
5. **Check upstream fuses, breakers, and contactors** for blown or failed components and replace as needed.
6. **Reset the fault** using the keypad and restore power, then monitor the drive for stable input voltage and current during operation.
7. **Review the fault log** in the drive's Modified Parameter or Fault Log menu to confirm the code is PF and check for any recent parameter changes that might affect input monitoring.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Input terminal block or wiring harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f007-fault-code&k=Input+terminal+block+or+wiring+harness&tag=errorcodefixes-20) \| Only if terminals are damaged, burned, or corroded beyond cleaning. |
| Upstream fuses or breaker | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f007-fault-code&k=Upstream+fuses+or+breaker&tag=errorcodefixes-20) \| Replace any blown fuses or failed breakers in the power distribution feeding the drive. |
| Contactor or disconnect switch | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f007-fault-code&k=Contactor+or+disconnect+switch&tag=errorcodefixes-20) \| If the upstream contactor is chattering or failing to close all three phases reliably. |

## When to Call a Pro

Call a qualified electrician or drive technician if you are not comfortable working with high-voltage three-phase power, if you cannot safely measure and verify input voltages, or if the fault persists after you have tightened terminals and verified upstream power. A professional can perform a megger test on the motor and cables, check for ground faults, review drive parameters, and replace internal drive components if the input stage has been damaged by phase loss. Do not attempt to open or service the drive while it is energized or if you lack the proper test equipment and lockout procedures.

**Rough cost:** A pro service call runs about $150-400 depending on whether the fix is tightening terminals or replacing upstream components.
