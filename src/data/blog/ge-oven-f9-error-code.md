---
title: "GE Oven F9 Error Code - Causes & Fix"
description: "F9 on most GE ovens means door latch/lock fault. Most often a dirty or binding lock mechanism. Clean and test the latch first."
pubDatetime: 2026-06-12T18:13:06Z
modDatetime: 2026-06-12T18:13:06Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - appliance
  - oven
  - ge
money_part: "Door latch / door lock assembly"
most_likely_cause: "Sticking, dirty, or mechanically bound latch/lock assembly"
likelihood: "the most common cause"
diy_or_pro: "diy"
free_checks:
  - "Power off at the breaker, wait 60 seconds, then restore power to clear any transient control fault and retest"
  - "Inspect the door latch area for debris, grease, or visible binding and clean thoroughly with a damp cloth"
  - "Manually cycle the lock/unlock mechanism and listen for grinding, sticking, or incomplete travel"
part_price: "$50-90"
no_buy_pct: "40%"
---

## What this code means
On most GE ovens and ranges, F9 is a door latch or door lock fault. The appliance believes the door-lock system is in the wrong state, most commonly because the lock-sensing switch is reporting unlocked when it should be locked during self-clean or high-temperature operation, or locked when it should not be during normal cooking. The control expects the latch to move between locked and unlocked positions correctly and the switches to confirm that position.

Some GE Monogram and other specific models use different F9 logic tied to the cooling fan, reed switch, or fan-speed sensing instead of the door lock. Always verify the exact meaning against your model's technical sheet or wiring diagram before ordering parts, because F9 is not universal across every GE platform.

## Before You Replace Anything

Many people replace the electronic control board first. Test the latch motor windings (should be about 3 kΩ) and check switch continuity in both locked and unlocked positions before replacing any board.

## Common Causes

- **Sticking, dirty, or binding latch/lock assembly (~35%)** Grease, spills, or debris prevent the lock cam and motor from moving smoothly between locked and unlocked positions, so the switch cannot signal the correct state to the control.
- **Damaged latch hook, cam, or lock mechanism (~25%)** Broken plastic tabs, bent metal hooks, or worn slots stop the latch from traveling fully, leaving the switch in the wrong position.
- **Faulty lock switch contacts (~20%)** The micro-switch inside the latch assembly is burned, pitted, or stuck and no longer shows continuity in the locked position or opens in the unlocked position.
- **Loose, damaged, or burned wiring to the latch (~10%)** Frayed wires, pinched connectors, or burned terminals between the latch assembly and the control board cause intermittent or missing signals.
- **Faulty lock motor windings (~7%)** The motor inside the latch assembly has open or shorted windings and will not drive the cam, or the winding resistance is far from the normal 3 kΩ spec.
- **Electronic control board fault (~3%)** After the latch mechanism, switches, motor, and wiring all test good, a failed input circuit or processor on the board is the remaining cause.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the latch mechanism move smoothly and completely when you manually push or pull the lock cam with power off?</summary>
<div class="dtree-body"><strong>Yes:</strong> The mechanical parts are likely okay. Inspect wiring and connectors for damage, then test the motor resistance (should be about 3 kΩ) and switch continuity in both locked and unlocked positions.<br><strong>No:</strong> The latch is binding or broken. Clean debris from the slots and cam, check for cracked tabs or bent hooks, and lubricate lightly if needed. If still stuck, replace the latch assembly.</div>
</details>

<details class="dtree"><summary>With the latch manually set to the locked position and power off, do the locked switch contacts show continuity on a multimeter?</summary>
<div class="dtree-body"><strong>Yes:</strong> The switch is working. Measure the lock motor winding resistance (should be about 3 kΩ). If the motor is good, check wiring and connectors or replace the control board.<br><strong>No:</strong> The lock switch contacts are faulty. Replace the entire door latch assembly, because the switch is not sold separately on most GE models.</div>
</details>

<details class="dtree"><summary>Did the error clear after a power cycle at the breaker and the oven is operating normally now?</summary>
<div class="dtree-body"><strong>Yes:</strong> A transient glitch or one-time mechanical stick caused the fault. Monitor for the next few cycles. If F9 returns, proceed with full latch and wiring diagnostics.<br><strong>No:</strong> The fault is persistent. Follow the full diagnostic sequence: verify model meaning, inspect and clean the latch, test motor and switch, check wiring, then replace the failed part.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify your exact model number** and consult the wiring diagram or tech sheet to confirm F9 means door latch fault, because some GE Monogram and other models define F9 as a cooling fan or reed switch fault instead.
2. **Turn off power at the circuit breaker** and wait at least 60 seconds, then restore power and test whether the error clears and the oven operates normally, because a transient control fault can sometimes resolve with a reset.
3. **Remove the inner door panel** (usually four to six screws around the frame) to expose the latch assembly and wiring, and inspect for debris, grease, broken plastic tabs, bent hooks, or damaged slots that would prevent smooth travel.
4. **Clean the latch cam, slots, and motor shaft** with a damp cloth and cycle the lock mechanism by hand to confirm it moves fully from unlocked to locked without binding, grinding, or incomplete travel.
5. **Disconnect the latch connector** and use a multimeter to measure motor winding resistance (should be about 3 kΩ) and to check switch continuity: with the latch manually locked the locked contacts should show continuity, and with the latch unlocked the unlocked contacts should show continuity.
6. **Inspect wiring and connectors** from the latch assembly to the control board for frayed insulation, pinched wires, burned terminals, or loose pins, and repair or replace any damaged harness sections.
7. **Replace the door latch assembly** if the motor resistance is wrong, the switches do not change state, or the mechanism is broken, and reassemble the door panel and restore power to test, or replace the electronic control board if all latch components and wiring test good.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Door latch / door lock assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-ge-oven-f9-error-code&k=Door+latch+%2F+door+lock+assembly&tag=errorcodefixes-20) \| Includes motor, cam, and micro-switches; verify your model number for the correct GE part. |
| Electronic control board (oven control) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-ge-oven-f9-error-code&k=Electronic+control+board+%28oven+control%29&tag=errorcodefixes-20) \| Replace only after verifying latch, motor, switches, and wiring all test good. |

## When to Call a Pro

Call a professional if you are not comfortable working with 240-volt wiring or removing the oven door and inner panel. Also call a pro if your model's tech sheet identifies F9 as a cooling fan or reed switch fault rather than a door lock fault, because diagnosing fan-speed sensors and control-board inputs requires specialized tools and knowledge. If you have replaced the latch assembly and verified wiring but the error persists, a technician with a service manual and multimeter can trace control-board inputs and confirm whether the board itself has failed.

**Rough cost:** DIY runs about $50-120 in parts, 45-90 min. A pro service call runs about $150-300.
