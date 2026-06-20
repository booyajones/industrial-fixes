---
title: "Yaskawa A1000 Uv1 Fault - Causes & Fix"
description: "Uv1 means DC bus undervoltage detected while running. Most often caused by loose input terminals or incoming power phase loss."
pubDatetime: 2026-06-11T09:58:31Z
modDatetime: 2026-06-11T09:58:31Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Main circuit magnetic contactor"
most_likely_cause: "loose input terminals or incoming power phase loss"
likelihood: "the most common real-world causes"
diy_or_pro: "pro"
---

## Yaskawa A1000 Uv1 Fault — What It Means

Uv1 on a Yaskawa A1000 drive signals DC bus undervoltage: the internal DC bus voltage dropped below the drive's threshold while running, or stayed below it longer than the programmed trip delay. For 200 V class drives the threshold is approximately 190 V (160 V for single-phase 200 V models), and for 400 V class drives it is approximately 380 V (350 V when parameter E1-01 is set below 400). The drive shuts down to protect itself from damage when it cannot maintain stable DC voltage.

This fault family is most often triggered by external supply problems rather than internal drive failure. Input power phase loss, loose or undersized input wiring, abnormal incoming line voltage, undersized upstream transformers, and faulty upstream contactors all appear in Yaskawa's diagnostic guidance. Internal aging of main-circuit capacitors or power-section circuitry can also cause Uv1, particularly on older drives or those approaching the end of their capacitor service life.

## Before You Replace Anything

Technicians sometimes replace the entire drive when the real cause is a loose terminal block connection or a failing upstream contactor. Always measure incoming line voltage under load and retorque all main-circuit terminals to specification before condemning the drive.

[Jump to Fix](#fix)

## Common Causes

- **Loose input terminals (~35%)** Poor connections at the drive's main input block create intermittent contact and voltage sag under load, triggering undervoltage detection.
- **Incoming power phase loss (~30%)** A blown fuse, open phase in upstream wiring, or failing utility supply drops one or more phases and collapses the DC bus.
- **Undersized or sagging line voltage (~15%)** An undersized transformer, long wire runs, or low utility voltage cannot deliver the drive's rated input voltage, especially during motor acceleration.
- **Main circuit magnetic contactor failure (~10%)** Worn or chattering upstream contactor contacts interrupt power delivery or create voltage dips each time the drive starts.
- **Aged main-circuit capacitors (~7%)** Worn electrolytic capacitors lose capacitance and cannot buffer the DC bus against transients, allowing voltage to droop below the trip threshold.
- **Internal power-section defect (~3%)** Failed rectifier diodes, damaged circuit boards, or defective CHARGE indicator circuitry prevent the drive from building or maintaining DC bus voltage.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the incoming line voltage measure within specification at the drive input terminals while the drive is running under load?</summary>
<div class="dtree-body"><strong>Yes:</strong> The supply is healthy so the fault is likely inside the drive: check input terminal torque, then inspect internal capacitors and power sections or call for service.<br><strong>No:</strong> The supply is inadequate: trace back through upstream disconnects, contactors, fuses, and wiring to find the phase loss, voltage sag, or loose connection.</div>
</details>

<details class="dtree"><summary>Are all three phases present and balanced at the input terminals when measured under load?</summary>
<div class="dtree-body"><strong>Yes:</strong> No phase loss detected, so confirm voltage level is within the drive's input specification and check for loose terminals or undersized transformer.<br><strong>No:</strong> Phase loss confirmed: inspect upstream fuses, disconnects, contactor contacts, and branch-circuit wiring for opens or poor connections.</div>
</details>

<details class="dtree"><summary>Is the drive's capacitor life monitor (parameter U4-05 if available) below 90 percent?</summary>
<div class="dtree-body"><strong>Yes:</strong> Capacitors are within service life so focus on external supply issues, terminal connections, and upstream contactor health.<br><strong>No:</strong> Capacitor wear is approaching replacement threshold: plan for drive replacement or capacitor service per the manufacturer's service manual.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Confirm the exact fault code** by reviewing the drive display or parameter history to distinguish Uv1 (undervoltage while running) from Uv2 or other alarms.
2. **Measure incoming line voltage** at the drive's input terminals with a true-RMS multimeter while the drive is starting and while running under load, watching for dips below specification or phase imbalance.
3. **Inspect and retorque all main-circuit input terminals** at the drive, verifying each connection matches the torque specification in the installation manual and that no conductors show signs of arcing or overheating.
4. **Check upstream power components** including the main disconnect, magnetic contactor, fuses, and all line-side connections for loose hardware, burned contacts, or blown fuses that could cause intermittent phase loss.
5. **Verify the supply matches the drive voltage class** and that incoming voltage stays within the drive's input-power specification, accounting for voltage drop under load if the transformer is undersized or wire runs are long.
6. **Review capacitor service-life data** by checking parameter U4-05 or consulting the drive's service history; if capacitor life exceeds 90 percent or the drive is very old, plan for replacement.
7. **Test or replace the drive** if all external supply and wiring checks pass but the Uv1 fault persists, consulting Yaskawa service or a qualified technician to diagnose internal power-section failures or replace worn components.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Main circuit magnetic contactor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-uv1-fault-code&k=Main+circuit+magnetic+contactor&tag=errorcodefixes-20) \| Replace if contacts are worn, pitted, or chattering and causing intermittent power interruption. |
| Yaskawa A1000 VFD replacement drive | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-uv1-fault-code&k=Yaskawa+A1000+VFD+replacement+drive&tag=errorcodefixes-20) \| Match the exact frame size and voltage class; required if internal capacitors or power section are worn beyond service life. |

## When to Call a Pro

Call a qualified electrician or drive technician if you are not trained to work on high-voltage three-phase equipment, if incoming line voltage measurements are outside specification and require utility or transformer work, or if all external wiring and supply checks pass but the Uv1 fault persists. Internal inspection of the drive's DC bus capacitors, rectifier section, and power boards requires lockout/tagout procedures, high-voltage safety training, and access to the service manual. A technician can also measure DC bus voltage directly, interpret capacitor-life monitors, and determine whether board-level repair or full drive replacement is the most economical path for your installation.

**Rough cost:** A pro service call runs about $150-600 depending on whether the fix is wiring, a contactor, or drive replacement.

## See Also

- [Yaskawa GA800 E02 Fault - Causes & Fix](/posts/yaskawa-ga800-e02-fault-code/)
- [Yaskawa A1000 oL2 Fault - Causes & Fix](/posts/yaskawa-a1000-vfd-ol2-fault-code/)
- [Yaskawa GA800 A.124 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-a-124-fault-code/)
- [Yaskawa A1000 Fault UV1, DC Bus Undervoltage Causes & Fix](/posts/yaskawa-a1000-fault-uv1/)
