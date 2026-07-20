---
title: "ABB ACS580 VFD E0029 Fault Code - Causes & Fix"
description: "E0029 signals an input phase loss or severe voltage imbalance on your ABB ACS580 drive. Check incoming power connections first."
pubDatetime: 2026-07-18T07:58:36Z
modDatetime: 2026-07-18T07:58:36Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - abb
money_part: "Three-phase input contactor"
most_likely_cause: "Loose or corroded connection at the drive input terminals"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Inspect the three incoming power conductors at the drive's L1, L2, and L3 terminals for loose screws or discolored wire"
  - "Check the upstream disconnect switch and contactor contacts for pitting or burns"
  - "Review the drive's event log to see if the fault occurred during a known power disturbance or storm"
no_buy_pct: "75%"
---

## ABB ACS580 VFD E0029 Fault Code — What It Means

The E0029 fault on an ABB ACS580 variable frequency drive indicates the controller has detected a loss of one or more input phases or a severe voltage imbalance on the incoming three-phase power supply. This fault protects the drive from operating under unstable power conditions that can damage internal components or cause erratic motor behavior.

The drive continuously monitors the three incoming power lines and trips when it sees one phase missing entirely, a phase voltage that has dropped too far below the others, or loose connections that create intermittent contact. The fault will latch and prevent motor operation until the supply issue is corrected and the drive is reset.

## Before You Replace Anything

Technicians sometimes replace the drive's input rectifier or main control board when E0029 appears, but the fault is almost always upstream in the building's electrical supply. Measure incoming line-to-line voltages at the drive terminals with a multimeter under load before ordering any drive components.

[Jump to Fix](#fix)

## Common Causes

- **Loose input terminal connection (~40%)** A screw-clamp terminal at L1, L2, or L3 that has vibrated loose or was never torqued properly will create intermittent contact and cause the drive to see a missing phase.
- **Failed upstream contactor or breaker (~25%)** A worn contactor with pitted contacts or a circuit breaker with internal damage can drop one leg of three-phase power before it reaches the drive.
- **Blown fuse in one phase (~15%)** If fused disconnect switches feed the drive, a single blown fuse will remove one phase and trigger the fault immediately.
- **Voltage imbalance in the building supply (~10%)** An unbalanced utility transformer, a lost neutral on a wye service, or a single-phasing condition elsewhere in the facility can present unequal voltages to the drive.
- **Damaged input power cable (~7%)** A cable that has been crushed, cut, or chewed by rodents may have one conductor severed internally while the jacket remains intact.
- **Drive input rectifier failure (~3%)** Internal rectifier diodes can short and cause the drive to misread phase voltages, though this is less common than supply-side problems.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Do all three incoming line-to-line voltages at the drive terminals measure within a few volts of each other with the drive disconnected?</summary>
<div class="dtree-body"><strong>Yes:</strong> The building supply is balanced. Inspect the drive's input terminal block for loose screws and corroded wire ends.<br><strong>No:</strong> The problem is upstream. Open the disconnect and check for blown fuses, damaged breaker contacts, or a failed contactor.</div>
</details>

<details class="dtree"><summary>Does the fault clear after power-cycling the drive and tightening all input terminals?</summary>
<div class="dtree-body"><strong>Yes:</strong> A loose connection was the cause. Monitor the drive for a few days to confirm the fault does not return.<br><strong>No:</strong> The fault is persistent. Measure voltage under load while the drive is running to see if one phase sags, or call an electrician to trace the supply back to the panel.</div>
</details>

<details class="dtree"><summary>Does the fault appear only when the motor is under heavy load or during startup?</summary>
<div class="dtree-body"><strong>Yes:</strong> Voltage drop under load points to undersized supply wiring, a weak transformer, or high resistance in a connection that heats up and opens.<br><strong>No:</strong> The fault is constant, which suggests a hard open circuit or a blown fuse rather than a marginal connection.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect power** to the drive at the upstream breaker or disconnect switch and verify zero voltage with a multimeter before touching any terminals.
2. **Remove the cover** from the drive's input terminal compartment and inspect the L1, L2, and L3 wire terminations for discoloration, burns, or loose hardware.
3. **Tighten each input terminal screw** to the torque specification listed on the drive's wiring label or in the installation manual, typically in the range of 1.5 to 2.5 Nm for this frame size.
4. **Measure incoming line-to-line voltages** at the drive terminals with the disconnect closed but the drive not yet powered. All three readings should be within about 2 percent of each other.
5. **Inspect the upstream disconnect** and contactor for pitted or welded contacts, and replace any blown fuses you find in the supply path.
6. **Restore power** and clear the fault from the drive's keypad or HMI by pressing the reset button or navigating to the fault-reset menu.
7. **Monitor the drive** during a test run under normal load to confirm all three phase voltages remain stable and the fault does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Three-phase input contactor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0029-fault-code&k=Three-phase+input+contactor&tag=errorcodefixes-20) \| Match the coil voltage and contact rating to your panel; replace if contacts are pitted or welded. |
| Fuse set for disconnect switch | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0029-fault-code&k=Fuse+set+for+disconnect+switch&tag=errorcodefixes-20) \| Use the amperage and interrupt rating specified on your existing fuse block; all three must match. |

## When to Call a Pro

Call a licensed electrician or industrial controls technician whenever E0029 appears. Diagnosing phase-loss faults requires working with live high-voltage three-phase power, measuring voltages under load, and tracing circuits back through panels and contactors. If tightening terminals and resetting the drive does not clear the fault, a professional will use a power-quality analyzer to capture voltage waveforms, check for transient imbalances, and verify that your supply meets the drive's input specifications. Attempting to swap internal drive components without confirming the supply is sound will waste money and leave the root cause unresolved.

**Rough cost:** A pro service call runs about $150-400.
