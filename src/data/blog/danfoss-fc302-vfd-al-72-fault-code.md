---
title: "Danfoss FC302 AL-72 Fault - Causes & Fix"
description: "AL-72 means dangerous heatsink temperature forcing emergency shutdown. Most often caused by failed cooling fans or blocked airflow."
pubDatetime: 2026-06-22T10:24:24Z
modDatetime: 2026-06-22T10:24:24Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Heatsink cooling fan"
most_likely_cause: "Failed cooling fan"
likelihood: "the most frequent cause"
diy_or_pro: "pro"
free_checks:
  - "Visually inspect all cooling fans to verify they are spinning and not damaged"
  - "Check the heatsink fins for dirt buildup or blockage and clear any obstructions"
  - "Verify ambient temperature around the drive is within specification"
no_buy_pct: "40%"
---

## Danfoss FC302 AL-72 Fault — What It Means

Alarm 72 on the Danfoss FC302 VFD indicates Dangerous Temperature, meaning the heatsink has reached critical emergency levels that force an immediate shutdown to prevent component destruction. This is more severe than Alarm 29 (Overtemperature) and often means component damage may have already begun by the time the fault occurs. The drive trips with a Trip Lock (STO), requiring a power cycle and fault clearance to reset.

## Before You Replace Anything

Technicians often replace the entire power board assuming failed IGBTs when the actual cause is a dead cooling fan or clogged heatsink. Always verify fan operation and inspect airflow paths before condemning internal semiconductors.

[Jump to Fix](#fix)

## Common Causes

- **Failed cooling fans (~35%)** The most frequent cause is a failed heatsink fan, and on larger frame sizes multiple fans work together so loss of one significantly reduces cooling capacity.
- **Dirt or clogged airflow (~25%)** Excessive dirt on the heatsink fins or blocked air flow paths prevent proper heat dissipation.
- **Drive overload (~15%)** Operating the drive at currents significantly higher than the motor rating for extended periods generates excessive heat.
- **Short deceleration times (~12%)** Short deceleration ramps on high-inertia loads cause rapid energy dissipation that overheats the heatsink.
- **High input voltage (~8%)** Incoming line voltage running high (above 10% of nominal) can push the DC bus voltage into fault territory and increase heat generation.
- **Failing IGBTs (~5%)** Internal problems such as failing IGBTs that run hot even at moderate current levels, even if the load appears normal.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Are all cooling fans spinning when the drive is powered on?</summary>
<div class="dtree-body"><strong>Yes:</strong> Fans are running, so check for clogged heatsink fins or blocked airflow paths next.<br><strong>No:</strong> Replace the failed fan immediately, as this is the most common cause of AL-72.</div>
</details>

<details class="dtree"><summary>Is the heatsink clean and free of dust or debris?</summary>
<div class="dtree-body"><strong>Yes:</strong> Airflow is clear, so review load parameters and check for high-inertia loads with short decel times.<br><strong>No:</strong> Clean the heatsink thoroughly and verify airflow is unobstructed before restarting.</div>
</details>

<details class="dtree"><summary>Does the fault occur during normal load or only during high-current events?</summary>
<div class="dtree-body"><strong>Yes:</strong> Fault during normal load suggests failing IGBTs or a defective heatsink temperature sensor, requiring power board diagnosis.<br><strong>No:</strong> Fault only during high load suggests overload or short deceleration ramps, so extend Parameters 3-41/3-42.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive safely** and lock out the incoming power supply before performing any inspection.
2. **Inspect all cooling fans** immediately and verify they are spinning freely and not damaged or blocked.
3. **Clean the heatsink fins** thoroughly to remove dirt, dust, or any obstructions blocking airflow paths.
4. **Review the load profile** and motor parameter settings (Parameters 1-20 to 1-25) to verify the motor nominal current is set correctly and the drive is not overloaded.
5. **Extend deceleration ramps** (Parameters 3-41 and 3-42) if the application involves high-inertia loads or short stopping times that cause rapid energy dissipation.
6. **Measure incoming line voltage** at the drive input terminals to confirm it is within nominal limits and not exceeding 10% above rated voltage.
7. **Test the heatsink temperature sensor** for continuity and resistance values if the fault persists after clearing airflow and load issues, and replace the sensor if the circuit is open or resistance is out of spec.
8. **Inspect internal semiconductors** (IGBTs and rectifiers) if the fault occurs during normal load conditions, as this suggests component failure requiring power board replacement.
9. **Clear the trip lock** by cycling power after completing repairs and verify the drive operates normally under load.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Heatsink cooling fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-72-fault-code&k=Heatsink+cooling+fan&tag=errorcodefixes-20) \| Match the frame size and fan model to your FC302 unit |
| Heatsink temperature sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-72-fault-code&k=Heatsink+temperature+sensor&tag=errorcodefixes-20) \| Check continuity and resistance before replacing |
| Power board assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-72-fault-code&k=Power+board+assembly&tag=errorcodefixes-20) \| Required only if IGBTs or rectifiers have failed |

## When to Call a Pro

Call a qualified VFD technician or controls specialist for AL-72 faults. This alarm indicates a severe overtemperature condition that may have already damaged internal semiconductors, and diagnosis requires high-voltage electrical testing, access to the power section, and specialized knowledge of IGBT and heatsink sensor circuits. If cleaning the heatsink and verifying fan operation does not clear the fault, internal component testing and potential power board replacement are required, and incorrect diagnosis can result in expensive parts replacement or further damage to the drive.

**Rough cost:** A pro service call runs about $200-800.

## See Also

- [Danfoss FC302 AL-62 - Causes & Fix](/posts/danfoss-fc302-vfd-al-62-fault-code/)
- [Danfoss FC302 Alarm 11 - DC Voltage Too Low Causes & Fix](/posts/danfoss-fc302-vfd-al-110-fault-code/)
- [Danfoss FC302 Alarm 32 - Causes & Fix](/posts/danfoss-fc302-alarm-32-fault-code/)
- [Danfoss FC302 AL-160 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-160-fault-code/)
