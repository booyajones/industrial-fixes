---
title: "Yaskawa GA800 VFD AL-12 Fault - Causes & Fix"
description: "AL-12 signals an undervoltage condition on the DC bus. Most often caused by low incoming power or a blown fuse. Check supply voltage first."
pubDatetime: 2026-07-21T07:34:36Z
modDatetime: 2026-07-21T07:34:36Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "Yaskawa GA800 input fuse set"
most_likely_cause: "Low incoming supply voltage or poor connection"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify incoming line voltage at the drive terminals with a multimeter during the fault condition"
  - "Inspect all line and load connections for tightness and signs of arcing or corrosion"
  - "Check that the drive's voltage rating matches the supply (200V, 400V, or 600V class)"
part_price: "$15-40"
---

## Yaskawa GA800 VFD AL-12 Fault — What It Means

The AL-12 fault on a Yaskawa GA800 variable frequency drive indicates an undervoltage trip. The drive has detected that the DC bus voltage has fallen below the acceptable threshold for safe operation and has shut down to protect itself and the motor. This can happen during normal operation or at startup.

Undervoltage faults typically occur when the incoming AC supply voltage drops too low, when there is a wiring problem reducing available voltage, or when internal components such as fuses or the rectifier section fail. The drive monitors the DC bus continuously and will trip immediately when voltage sags below the programmed trip level. Consult your model's manual for the exact threshold value, as it varies with the drive's voltage rating.

## Before You Replace Anything

Technicians sometimes replace the main control board or power card when the real issue is a blown input fuse or loose line connection. Always measure incoming AC voltage and check fuses with a multimeter before ordering circuit boards.

[Jump to Fix](#fix)

## Common Causes

- **Low or sagging incoming AC supply voltage (~35%)** Utility brownouts, undersized branch circuits, or voltage drop in long cable runs can cause the DC bus to fall below the trip threshold.
- **Blown input fuse (~25%)** The drive's internal line fuses can fail due to inrush current, short circuits, or age, cutting power to the rectifier section and collapsing the DC bus.
- **Loose or corroded line connections (~20%)** Poor contact at the L1, L2, L3 terminals or at upstream breakers increases resistance and reduces voltage reaching the drive.
- **Failed rectifier diode or bridge (~10%)** A shorted or open diode in the input rectifier reduces DC bus voltage and may blow fuses repeatedly.
- **Incorrect parameter settings (~5%)** If the drive's rated voltage parameter does not match the actual supply, the undervoltage trip level may be set too high.
- **Weak or failing DC bus capacitor (~5%)** Capacitors that have lost capacity cannot maintain bus voltage during load transients, causing nuisance trips.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does your multimeter show incoming line voltage within 10% of the drive's rated voltage during the fault?</summary>
<div class="dtree-body"><strong>Yes:</strong> The supply is adequate. Focus on internal components such as fuses, the rectifier bridge, or bus capacitors.<br><strong>No:</strong> The supply voltage is too low. Check for utility problems, breaker sizing, or excessive voltage drop in the feed wiring.</div>
</details>

<details class="dtree"><summary>Can you see or smell any burned components, discolored PCBs, or blown fuses inside the drive enclosure?</summary>
<div class="dtree-body"><strong>Yes:</strong> A component failure is likely. Replace the blown fuse or damaged power card and investigate the root cause to prevent recurrence.<br><strong>No:</strong> The fault may be intermittent or caused by external wiring. Verify all connections and monitor voltage over time.</div>
</details>

<details class="dtree"><summary>Does the fault appear immediately at power-up or only under load?</summary>
<div class="dtree-body"><strong>Yes:</strong> If at power-up, suspect a wiring issue, wrong voltage rating, or failed rectifier. If under load, check for voltage sag or undersized supply.<br><strong>No:</strong> Intermittent faults often point to loose connections, thermal issues, or marginal supply voltage during peak demand.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect all power** to the drive and verify zero voltage with a multimeter before opening the enclosure or touching terminals.
2. **Measure incoming line voltage** at the L1, L2, and L3 terminals with the drive powered and compare to the drive's nameplate rating (200V, 400V, or 600V class).
3. **Inspect all line and load connections** for tightness, corrosion, or signs of overheating and retorque to the manufacturer's specification.
4. **Check the internal input fuses** by removing them and testing continuity with a multimeter; replace any open fuses with the correct type and amp rating.
5. **Review drive parameter settings** to confirm the voltage rating parameter matches the actual supply and that undervoltage trip thresholds are appropriate for your installation.
6. **Test the rectifier bridge** by measuring forward voltage drop across each diode with a diode-test multimeter function; replace the power card or bridge assembly if any diode is shorted or open.
7. **Clear the fault** using the keypad or parameter reset and monitor operation under load to verify the issue is resolved; log the fault history for future reference.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 input fuse set | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-al-12-fault-code&k=Yaskawa+GA800+input+fuse+set&tag=errorcodefixes-20) \| Match the fuse type and current rating to your drive's voltage class and horsepower. |
| GA800 power supply board or rectifier module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-al-12-fault-code&k=GA800+power+supply+board+or+rectifier+module&tag=errorcodefixes-20) \| Required if the rectifier bridge or capacitor bank has failed; consult Yaskawa for the exact part number for your frame size. |

## When to Call a Pro

Call a qualified electrician or industrial technician if you are not comfortable working with high-voltage three-phase power, if you lack the tools to safely measure line voltage and test internal components, or if the fault persists after checking fuses and connections. VFD troubleshooting requires knowledge of power electronics and the ability to interpret drive parameters and fault logs. Professional service is also recommended when the rectifier bridge or DC bus capacitors need replacement, as these involve desoldering and handling components that store lethal voltage even after shutdown.

**Rough cost:** A pro service call runs about $200-500.
