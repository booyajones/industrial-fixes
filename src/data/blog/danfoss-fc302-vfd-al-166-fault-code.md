---
title: "Danfoss FC302 AL-166 - Causes & Fix"
description: "AL-166 on a Danfoss FC302 VFD means catastrophic internal short circuit. The IGBT power module has failed and needs replacement."
pubDatetime: 2026-06-26T09:57:06Z
modDatetime: 2026-06-26T09:57:06Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 IGBT Power Module"
most_likely_cause: "IGBT power module catastrophic failure"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify Parameter 1-24 (Nominal Motor Current) matches the actual motor nameplate rating, not higher"
  - "Inspect motor cable and terminal box for visible burn marks or damage before replacing drive components"
part_price: "$600-1800"
---

## Danfoss FC302 AL-166 — What It Means

AL-166 is a catastrophic instantaneous overcurrent fault on the Danfoss FC302 VFD. This code signals that the drive's IGBT (Insulated Gate Bipolar Transistor) power module has suffered a complete semiconductor junction breakdown, creating a direct short circuit across the internal DC bus. The drive cuts power in microseconds to protect surrounding components, but the IGBT module itself is destroyed. This is distinct from a standard overcurrent alarm (AL-13), which indicates external load problems. AL-166 is an internal drive failure that cannot be cleared by a simple reset.

The fault means the power section of your VFD is no longer functional. In rare cases, a phase-to-phase short in the motor cable or motor terminal box can trigger this alarm, but the vast majority of AL-166 faults point to internal damage. Running the drive repeatedly after this fault appears will cause cascading damage to other expensive components.

## Before You Replace Anything

Do not replace the entire VFD without first disconnecting the motor and testing the drive unloaded. Some AL-166 faults are caused by a shorted motor cable or motor winding, which is much cheaper to repair than the drive itself.

[Jump to Fix](#fix)

## Common Causes

- **IGBT module semiconductor junction breakdown (~70%)** The power transistors in the IGBT module have failed internally, creating a direct short across the DC bus that triggers instantaneous shutdown.
- **Thermal overload of the power module (~15%)** Prolonged operation in high ambient temperatures or blocked cooling fans causes the IGBT to overheat and fail catastrophically.
- **Motor cable or motor winding short circuit (~10%)** A phase-to-phase short in the output cable or motor terminal box can mimic an internal IGBT fault and trigger AL-166.
- **Incorrect motor parameter settings (~5%)** Setting Nominal Motor Current (Parameter 1-24) significantly higher than the actual motor rating can cause false triggering of the instantaneous overcurrent protection.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the AL-166 fault persist when you disconnect the motor and run the drive unloaded?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is internal to the VFD. The IGBT power module has failed and the drive needs professional repair or replacement of the power section.<br><strong>No:</strong> The fault is external. Inspect the motor cable for shorts and test the motor windings with a megohmmeter before replacing any drive components.</div>
</details>

<details class="dtree"><summary>Is Parameter 1-24 (Nominal Motor Current) set higher than the motor nameplate current rating?</summary>
<div class="dtree-body"><strong>Yes:</strong> Correct the parameter to match the motor nameplate exactly. An oversized setting can cause false instantaneous trips. Reset and test the drive.<br><strong>No:</strong> The parameter is correct. Proceed with isolating the motor to test whether the fault is internal or external to the drive.</div>
</details>

<details class="dtree"><summary>Are there visible burn marks, scorching, or a burning smell inside the VFD enclosure?</summary>
<div class="dtree-body"><strong>Yes:</strong> The IGBT module has suffered catastrophic thermal failure. The drive requires replacement of the entire power section or a new VFD.<br><strong>No:</strong> Physical damage may not be visible. Professional testing of the IGBT module and current sensors is required to confirm internal failure.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect AC mains power and all DC-link sources** (including UPS or battery backups) to the VFD. Wait for the minimum capacitor discharge time specified in Table 2.1 of the FC302 manual before touching any terminals.
2. **Verify zero voltage** at the DC bus and AC input terminals using a multimeter before proceeding. Do not rely on LED indicators alone.
3. **Disconnect the motor** from the VFD output terminals U, V, and W. Label all three motor leads for reconnection.
4. **Attempt to run the drive unloaded** with no motor connected. If AL-166 reappears immediately, the fault is internal to the drive and the IGBT module has failed.
5. **If the drive runs unloaded**, inspect the motor cable for visible damage or shorts. Use a megohmmeter to test motor winding insulation and phase-to-phase shorts.
6. **Verify Parameter 1-24** (Nominal Motor Current) matches the motor nameplate rating exactly. Also check Parameters 1-20 and 1-21 (Motor Voltage and Frequency) for correctness.
7. **If the fault is internal**, disassemble the VFD to access the heatsink and power section. Look for scorch marks, burnt components, or visible IGBT damage. Professional IGBT module replacement or VFD replacement is required.
8. **Test current sensor continuity** if you have access to the power section. Replace any sensors showing open circuits or out-of-range resistance values per the service manual.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 IGBT Power Module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-166-fault-code&k=Danfoss+FC302+IGBT+Power+Module&tag=errorcodefixes-20) \| Must match the exact frame size and voltage rating of your VFD. Consult the serial number label and service manual for the correct part number. |
| Danfoss FC302 Current Sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-166-fault-code&k=Danfoss+FC302+Current+Sensor&tag=errorcodefixes-20) \| Only needed if sensor testing shows open or short circuit. Order by frame size and part number from the service manual. |

## When to Call a Pro

Call a qualified VFD technician or industrial electrician immediately when AL-166 appears. This fault involves high-voltage DC bus components and catastrophic internal failure that requires specialized diagnostic equipment and high-voltage safety training. Do not attempt repeated resets, as each power-on cycle risks cascading damage to the DC bus capacitors, gate driver boards, and other expensive components. A professional can test the IGBT module with proper tools, isolate whether the fault is internal or external, and replace the power section safely. Attempting DIY repair on a failed IGBT module without proper discharge procedures and high-voltage training poses serious risk of electric shock from the DC bus capacitors, which can hold lethal voltage for minutes after power-down.

**Rough cost:** A pro service call runs about $800-2500.

## See Also

- [Danfoss FC302 Alarm 34 - Causes & Fix](/posts/danfoss-fc302-alarm-34-fault-code/)
- [Danfoss FC302 AL-69 - Causes & Fix](/posts/danfoss-fc302-vfd-al-69-fault-code/)
- [Danfoss FC302 AL-134 - Causes & Fix](/posts/danfoss-fc302-vfd-al-134-fault-code/)
- [Danfoss FC302 AL-100 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-100-fault-code/)
