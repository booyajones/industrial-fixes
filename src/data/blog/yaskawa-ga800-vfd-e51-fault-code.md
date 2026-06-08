---
title: "Yaskawa GA800 E51 Fault - Causes & Fix"
description: "E51 on a Yaskawa GA800 means input phase loss or incoming power failure. Most often caused by a missing phase from the supply or a blown input fuse."
pubDatetime: 2026-06-06T11:38:35Z
modDatetime: 2026-06-06T11:38:35Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
most_likely_cause: "One input phase missing from the supply or an open upstream protection device"
likelihood: "the most common real-world cause"
diy_or_pro: "pro"
---

## Yaskawa GA800 E51 Fault — What It Means

The E51 fault on a Yaskawa GA800 variable frequency drive signals an input power abnormality or phase-loss condition on the incoming supply side. The drive has detected that one or more of the three-phase input lines (L1, L2, or L3) has disappeared or dropped below acceptable levels. This is not a motor-side overload or output problem. The fault protects the drive from operating with unbalanced or incomplete incoming power, which would damage the input rectifier section.

Yaskawa's troubleshooting approach for this code focuses on the power path from the utility supply to the drive terminals. The drive's input monitoring circuit has flagged a condition where the incoming voltage pattern no longer matches normal three-phase operation, either because a phase is completely missing or the imbalance is severe enough to trigger the protection logic.

## Before You Replace Anything

Technicians sometimes replace the drive's control board or rectifier section when the real problem is a blown input fuse, loose line terminal, or upstream contactor dropping one phase. Always verify all three incoming line voltages at the drive input terminals before replacing any drive components.

[Jump to Fix](#fix)

## Common Causes

- **Missing input phase from utility or breaker** One of the three supply lines has opened upstream due to a tripped breaker, failed disconnect, or utility service problem.
- **Blown input fuse** An input fuse protecting one phase has opened, cutting power to that leg of the drive.
- **Loose or damaged input terminal** A connection on L1, L2, or L3 at the drive has loosened, overheated, or oxidized, causing intermittent or complete loss of that phase.
- **Faulty line-side contactor** A contactor or other switching device feeding the drive is dropping one phase under load due to worn contacts or coil problems.
- **Severe incoming voltage imbalance** The supply voltages are present but unbalanced or sagging enough to be interpreted as a phase-loss condition by the drive.
- **Drive input rectifier damage** If supply-side components test good, the drive's input power conversion section may have failed and is falsely signaling a phase loss.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Do all three line-to-line voltages measure equal and match the nameplate rating at the drive input terminals with the upstream disconnect closed?</summary>
<div class="dtree-body"><strong>Yes:</strong> The supply is good. The problem is likely inside the drive's input section or a wiring connection at the terminals. Inspect terminals for loose screws or heat damage, then contact Yaskawa support if connections are solid.<br><strong>No:</strong> One or more phases are missing or low. The problem is upstream. Check the breaker, disconnect, fuses, and contactor in the feeder before the drive.</div>
</details>

<details class="dtree"><summary>Does the fault clear immediately after you reset it, or does it return as soon as you power up?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault returns right away, indicating a persistent problem. The missing phase or connection fault is still present. Recheck all upstream devices and line-side terminals.<br><strong>No:</strong> The fault was intermittent. Look for loose terminals, a contactor with worn contacts, or a supply problem that comes and goes under load.</div>
</details>

<details class="dtree"><summary>Are any input fuses open or any upstream protective devices tripped?</summary>
<div class="dtree-body"><strong>Yes:</strong> Replace the open fuse or reset the device, then investigate why it opened (short circuit, overload, or drive fault). Do not simply replace and re-energize without finding the root cause.<br><strong>No:</strong> Fuses and breakers are intact. Move on to checking line voltage balance and terminal connections at the drive.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Lock out and tag out** the disconnect feeding the drive, following your facility's electrical safety procedures.
2. **Inspect the upstream path** from the supply panel to the drive: check the breaker, disconnect switch, any input fuses, line-side contactor, and line reactor or filter if installed.
3. **Measure all three line-to-line voltages** (L1-L2, L2-L3, L3-L1) at the drive input terminals with the disconnect closed and compare them to the supply nameplate. All three should be present and within a few volts of each other.
4. **Tighten all input terminal screws** on L1, L2, and L3 at the drive and inspect for signs of overheating, discoloration, or oxidation. Replace any damaged conductors or terminal lugs.
5. **Replace any open fuse** or reset any tripped upstream device. If a fuse blew, investigate the cause (check for a short or a drive internal fault) before re-energizing.
6. **Re-energize the drive** and observe the keypad. If E51 does not return, the supply-side issue has been corrected. If it returns immediately, the drive's input section may be damaged.
7. **Reset the fault** from the keypad using the documented reset method. Monitor the drive under load to confirm the fault does not recur.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Input fuses (sized per GA800 installation manual) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e51-fault-code&k=Input+fuses+%28sized+per+GA800+installation+manual%29&tag=errorcodefixes-20) \| Replace if any are open. Confirm amperage and type match the drive's input rating before ordering. |
| Line-side contactor or disconnect components | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e51-fault-code&k=Line-side+contactor+or+disconnect+components&tag=errorcodefixes-20) \| If one phase is being dropped by worn contacts or a failed auxiliary, repair or replace the upstream switching device. |
| Input terminal lugs and conductors | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e51-fault-code&k=Input+terminal+lugs+and+conductors&tag=errorcodefixes-20) \| Replace any heat-damaged, oxidized, or loose terminal hardware and re-land with proper torque. |

## When to Call a Pro

Call a licensed electrician or drive technician if you are not trained and authorized to work on three-phase industrial power systems. Diagnosing E51 requires measuring live line voltages and working inside electrical enclosures under lockout/tagout. If the upstream supply and all terminals test good but the fault persists, contact Yaskawa support or an authorized service center. The drive's input rectifier or power conversion section may be damaged, and replacing internal assemblies requires manufacturer training and proper part identification. Do not attempt to repair or replace drive internal components without consulting Yaskawa's maintenance documentation and verifying the correct part numbers for your frame size and voltage rating.

**Rough cost:** A pro service call runs about $150-500.
