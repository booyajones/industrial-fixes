---
title: "Yaskawa GA800 F002 Fault - Causes & Fix"
description: "F002 on Yaskawa GA800 VFD means Input Phase Loss: one incoming power phase is missing or severely unbalanced. Check input terminals first."
pubDatetime: 2026-06-27T11:34:31Z
modDatetime: 2026-06-27T11:34:31Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Input fuse (appropriate voltage and current rating)"
most_likely_cause: "Loose or corroded connections at the L1, L2, or L3 input terminals"
likelihood: "the most frequent cause"
diy_or_pro: "pro"
free_checks:
  - "Power down the drive and visually inspect the L1, L2, and L3 input terminals for loose wires or corrosion"
  - "Check the input fuses and breakers in the power distribution panel for any that are blown or tripped"
  - "Measure voltage between all three phase pairs (L1-L2, L2-L3, L3-L1) with a multimeter to verify all three phases are present and balanced"
no_buy_pct: "75%"
---

## Yaskawa GA800 F002 Fault — What It Means

The F002 fault code on the Yaskawa GA800 variable frequency drive indicates **Input Phase Loss**. The drive has detected that one or more phases of the incoming AC power supply are absent, or that the voltage between phases is unbalanced beyond the allowable threshold. This occurs when the input power voltage is changing too much, a phase is physically lost, or wiring at the input terminals (L1, L2, or L3) is loose or disconnected.

The drive's internal monitoring circuit continuously checks the three-phase input power. When it sees a missing phase or an imbalance (typically greater than 10% difference between phases), it shuts down to protect itself and the connected motor. The fault can be intermittent if a connection is loose or if external power supply components are failing.

## Before You Replace Anything

Technicians sometimes replace the drive itself when the actual problem is a blown fuse or faulty contactor on the input side. Always measure input voltage and check external power components before condemning the VFD.

[Jump to Fix](#fix)

## Common Causes

- **Loose or corroded input wiring (~45%)** The most frequent cause is loose connections at the L1, L2, or L3 input terminals, leading to intermittent contact or a complete break in one phase.
- **External power supply issues (~30%)** A blown fuse, tripped breaker, or open contactor on one leg of the incoming power distribution panel interrupts power to the drive.
- **Voltage imbalance (~15%)** Severe unbalance in the utility power (greater than 10% difference between phases) can trigger the fault even if all phases are present.
- **Faulty input contactor (~8%)** A contactor with pitted or welded contacts on one phase can create an intermittent or open circuit that the drive sees as a phase loss.
- **Drive internal monitoring circuit failure (~2%)** If input voltage is balanced and stable but the fault persists, the drive's internal phase loss detection circuit may be faulty.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>With power on (drive disconnected), do you measure voltage between all three phase pairs (L1-L2, L2-L3, L3-L1) and are all readings within 5% of each other?</summary>
<div class="dtree-body"><strong>Yes:</strong> The incoming power is good. The fault is likely caused by loose input terminal connections or a failing internal monitoring circuit in the drive. Tighten all input terminals and retest.<br><strong>No:</strong> One phase is missing or severely low. The problem is upstream of the drive. Check fuses, breakers, and contactors in the power distribution panel.</div>
</details>

<details class="dtree"><summary>Are any of the input terminal screws at L1, L2, or L3 loose or showing signs of arcing or heat damage?</summary>
<div class="dtree-body"><strong>Yes:</strong> Tighten the loose terminals to the manufacturer's specified torque and clean any corrosion. This is likely the root cause.<br><strong>No:</strong> The wiring is secure. Move to checking external power components and measuring voltage under load.</div>
</details>

<details class="dtree"><summary>Does the fault occur only during motor operation or PID control, not at startup?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault may be triggered by voltage sag under load or by noise from the PID feedback sensor. Check the feedback wiring and perform a megger test on the motor leads.<br><strong>No:</strong> The fault appears at startup or randomly, indicating a persistent wiring or external power issue. Focus on input connections and external components.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down and lock out** the main input power to the VFD. Verify zero voltage at the L1, L2, and L3 terminals using a multimeter before touching any wiring.
2. **Inspect input terminals** at L1, L2, and L3 for loose wires, burn marks, or corrosion. Look for discoloration on the terminal blocks or wire insulation that indicates overheating.
3. **Tighten all input connections** to the manufacturer's specified torque. Consult the GA800 Maintenance Manual for exact torque values (typically 15 to 20 in-lb for terminal screws on this model).
4. **Restore power** (keep the drive off) and measure voltage between L1-L2, L2-L3, and L3-L1 using a true RMS multimeter. All three readings should be within 5% of each other. If one is missing or significantly lower, the issue is external to the drive.
5. **Check external power components** including fuses, breakers, and contactors on the input side. Replace any blown fuse or faulty contactor. Test contactors under load if intermittent faults are suspected.
6. **Review the drive's fault log** by navigating to F2, then Menu, then Modified Parameter or Fault Log. Check the exact voltage reading recorded at the time of the fault to confirm whether the phase loss was real or a detection error.
7. **Test under load** by running the drive and monitoring input voltage. If the fault reappears during motor operation, check for voltage sag or imbalance that only occurs under load. Consider installing a line reactor or checking the utility supply.
8. **If the fault persists** with balanced input voltage and tight connections, the drive's internal phase loss detection circuit may be faulty. Consult a qualified VFD technician or contact Yaskawa support for further diagnostics.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Input fuse (appropriate voltage and current rating) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f002-fault-code&k=Input+fuse+%28appropriate+voltage+and+current+rating%29&tag=errorcodefixes-20) \| Replace if blown. Match the fuse type and rating to your power distribution panel specifications. |
| Input contactor (appropriate coil voltage and contact rating) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f002-fault-code&k=Input+contactor+%28appropriate+coil+voltage+and+contact+rating%29&tag=errorcodefixes-20) \| Replace if contacts are pitted, welded, or not closing on all three phases. Verify coil voltage matches your control circuit. |

## When to Call a Pro

Call a qualified electrician or VFD technician if you are not comfortable working with three-phase power or if you cannot safely perform voltage measurements and terminal inspections. Professional help is needed if the fault persists after you have verified that input voltage is balanced, all connections are tight, and external components are good. The drive may require internal diagnostics or replacement of the monitoring circuit. Also call a pro if the fault appears intermittently during PID operation and you suspect noise or ground faults in the motor or feedback wiring, as this requires a megger test and signal-level troubleshooting.

**Rough cost:** A pro service call runs about $150-400.
