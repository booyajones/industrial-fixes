---
title: "Yaskawa GA800 VFD AL-21 Fault - Causes & Fix"
description: "AL-21 signals a momentary power loss or interruption. Check incoming power connections and line voltage stability before replacing parts."
pubDatetime: 2026-07-21T07:43:57Z
modDatetime: 2026-07-21T07:43:57Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "Yaskawa GA800 power supply module"
most_likely_cause: "Loose or corroded incoming power connections"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Inspect all incoming power terminals (L1, L2, L3) for tightness and corrosion"
  - "Check the disconnect switch and upstream breaker contacts for pitting or wear"
  - "Review the facility for other equipment tripping or voltage sags at the same time"
---

## Yaskawa GA800 VFD AL-21 Fault — What It Means

The AL-21 fault code on a Yaskawa GA800 variable frequency drive typically indicates a momentary power loss or interruption to the drive's control circuit. This alarm is triggered when the drive detects that incoming AC power dipped below the minimum threshold or was briefly interrupted, even for a few milliseconds. The drive flags this condition to alert the operator that a loss of power occurred, which may have caused the drive to reset or drop out.

Unlike a critical fault that shuts down the drive immediately, AL-21 is often a warning that the drive experienced an input power disturbance. The drive may continue to operate or require a manual reset depending on your parameter settings. Repeated AL-21 faults point to an unstable power supply, loose wiring, or issues upstream in the electrical distribution system.

## Before You Replace Anything

Technicians sometimes replace the drive's internal power supply board or control card when the real cause is a loose terminal or a failing upstream contactor. Always verify incoming voltage stability and connection torque before swapping circuit boards.

[Jump to Fix](#fix)

## Common Causes

- **Loose or corroded power terminals (~35%)** High resistance at L1, L2, or L3 input terminals causes intermittent voltage drops that the drive reads as power loss.
- **Worn upstream contactor or breaker (~25%)** A contactor with pitted contacts or a breaker with internal arcing can momentarily interrupt power to the drive during switching or under load.
- **Utility voltage sag or brownout (~20%)** Grid disturbances, transformer loading, or nearby equipment starting can pull line voltage below the drive's minimum operating threshold.
- **Undersized or aging supply wiring (~10%)** High impedance in long or undersized feeder cables drops voltage under load, especially during motor acceleration.
- **Faulty drive power supply module (~7%)** Internal components in the drive's rectifier or control power supply may be failing and dropping out under marginal conditions.
- **Incorrect input voltage parameter (~3%)** If the drive's voltage range parameter is set incorrectly, it may falsely detect normal voltage dips as power loss.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the AL-21 fault occur at the same time each day or when other equipment starts?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is likely caused by a utility voltage sag or shared transformer loading. Monitor incoming voltage with a power quality meter and consider adding line reactors or a dedicated feeder.<br><strong>No:</strong> The fault is probably due to wiring or hardware issues at the drive or upstream disconnect. Proceed to check all connections and contactors.</div>
</details>

<details class="dtree"><summary>Can you measure incoming line voltage at L1, L2, and L3 while the drive is running?</summary>
<div class="dtree-body"><strong>Yes:</strong> Record voltage continuously during normal operation and when the fault occurs. Dips below the drive's minimum spec (consult your model's table) confirm a supply problem.<br><strong>No:</strong> Call a qualified electrician or technician with a multimeter or power analyzer to perform voltage measurements under load.</div>
</details>

<details class="dtree"><summary>Are the incoming power terminal screws torqued to specification?</summary>
<div class="dtree-body"><strong>Yes:</strong> Connections are secure. Next, inspect the upstream disconnect, contactor, and breaker for worn contacts or signs of arcing.<br><strong>No:</strong> Tighten all power terminals to the torque values listed in the drive's installation manual. Loose connections are a leading cause of intermittent power loss.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive** and open the upstream disconnect. Lock out and tag out the power source following NFPA 70E or local electrical safety standards.
2. **Inspect the incoming power terminals** (L1, L2, L3) for signs of discoloration, corrosion, or loose hardware. Remove each wire, clean the terminal and lug with a wire brush, and reinstall with the correct torque per the installation manual.
3. **Check the upstream contactor or breaker** for pitted or burned contacts. Open the enclosure and visually inspect the contact surfaces. Replace any contactor showing signs of arcing or excessive wear.
4. **Measure incoming line voltage** at the drive's input terminals using a true-RMS multimeter or power quality analyzer. Verify that all three phases are balanced within a few volts and that voltage remains stable under load.
5. **Monitor voltage during a fault event** if possible. Use a data-logging meter or oscilloscope to capture transient dips or interruptions that occur when the AL-21 alarm triggers.
6. **Review drive parameters** related to input voltage range and power loss detection. Consult the GA800 manual to confirm that the drive's voltage settings match your actual supply.
7. **Test the drive under no-load** after tightening connections and verifying voltage. If the AL-21 fault persists with stable incoming power, the internal power supply or control board may need replacement by a qualified technician.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 power supply module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-al-21-fault-code&k=Yaskawa+GA800+power+supply+module&tag=errorcodefixes-20) \| Factory replacement for internal rectifier or control power supply; requires factory part number matching your drive's voltage and frame size. |
| Upstream magnetic contactor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-al-21-fault-code&k=Upstream+magnetic+contactor&tag=errorcodefixes-20) \| Select a contactor rated for the drive's input current and voltage; consult your electrical drawings for the correct coil voltage. |

## When to Call a Pro

Call a licensed electrician or industrial automation technician if you are not trained in high-voltage AC power systems. Work inside a VFD or upstream electrical panel involves lethal voltages and requires proper lockout-tagout procedures, personal protective equipment, and knowledge of arc flash hazards. A professional can perform voltage monitoring, torque verification, and drive parameter adjustments safely. If the fault persists after tightening connections and verifying stable incoming power, a technician with factory training should diagnose the drive's internal power supply and control circuitry.

**Rough cost:** A pro service call runs about $150-400.
