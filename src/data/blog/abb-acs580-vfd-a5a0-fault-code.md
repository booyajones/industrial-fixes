---
title: "ABB ACS580 A5A0 Fault - Causes & Fix"
description: "A5A0 means Safe Torque Off is active because the safety circuit signal at the STO connector is lost. Check the e-stop and wiring first."
pubDatetime: 2026-06-21T10:39:11Z
modDatetime: 2026-06-21T10:39:11Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - abb
money_part: "ABB ACS580 internal 24V power supply board"
most_likely_cause: "Open safety circuit component"
likelihood: "the most frequent cause"
diy_or_pro: "pro"
free_checks:
  - "Check that all emergency stop buttons are released and safety doors are fully closed"
  - "Inspect the XSTO connector for loose wires or unseated jumper pins"
  - "Measure continuity across the safety circuit with a multimeter to confirm the loop is closed"
no_buy_pct: "60%"
---

## ABB ACS580 A5A0 Fault — What It Means

The A5A0 fault code on an ABB ACS580 variable frequency drive indicates that the Safe Torque Off (STO) function is active. This means the drive has detected that the external safety circuit signal connected to the STO connector (XSTO) has been lost or interrupted. The drive stops delivering torque to the motor as a safety precaution.

The STO function is triggered by external safety devices such as emergency stop buttons, safety door interlocks, or machine safety relays. When any of these devices open the circuit, the drive enters a safe state and logs the A5A0 fault. This is a normal protective response, not necessarily a drive failure. The fault is linked to parameter 31.22 (STO diagnostics) in the drive's programming.

## Before You Replace Anything

Technicians sometimes replace the control board when the real issue is simply a loose jumper pin inside the XSTO connector or an accidentally pressed emergency stop button. Always verify continuity across the entire safety loop with a multimeter before ordering any boards.

[Jump to Fix](#fix)

## Common Causes

- **Open safety circuit component (~45%)** An emergency stop button is pressed, a safety door is open, or a safety relay is de-energized, breaking the STO signal path.
- **Loose or disconnected STO wiring (~30%)** Poor connections at the XSTO terminals, broken wires, or jumper pins that have become loose inside the connector interrupt the 24VDC signal.
- **Internal 24VDC supply failure (~15%)** The drive's internal 24VDC power supply that feeds the STO circuit is unstable, blown, or disconnected, causing a false loss-of-signal.
- **Incorrect parameter 31.22 setting (~8%)** Parameter 31.22 (STO diagnostics) is set to trigger a fault when no external safety circuit is installed, or it is configured incorrectly for the application.
- **Electrical noise on STO line (~2%)** Transient electrical noise momentarily breaks the STO signal, causing the drive to register a fault.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Are all emergency stop buttons released and safety doors fully closed?</summary>
<div class="dtree-body"><strong>Yes:</strong> The external safety devices are in the correct state. Proceed to inspect the drive's STO connector and wiring.<br><strong>No:</strong> Release the e-stop or close the door. The fault should clear when the safety circuit is restored and the drive is reset.</div>
</details>

<details class="dtree"><summary>Does a multimeter show continuity (less than 1 ohm) across the entire safety loop?</summary>
<div class="dtree-body"><strong>Yes:</strong> The external circuit is intact. The problem is likely inside the drive (loose connector, failed 24V supply, or control board).<br><strong>No:</strong> There is an open in the external safety wiring or a faulty safety component. Trace the circuit to find the break.</div>
</details>

<details class="dtree"><summary>Is the drive's internal 24VDC present at the STO terminals?</summary>
<div class="dtree-body"><strong>Yes:</strong> The power supply is working. Check for loose jumpers, incorrect parameter settings, or a faulty control board.<br><strong>No:</strong> The internal 24V supply board has failed and needs replacement.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Check all external safety devices** by walking through the machine and verifying that every emergency stop button is released and every safety door or gate is fully closed.
2. **Inspect the XSTO connector** by opening the drive control panel and examining the STO terminal block for loose wires, unseated jumper pins, or signs of corrosion.
3. **Measure continuity** across the safety circuit using a multimeter set to resistance mode, confirming the loop reads less than 1 ohm when all devices are closed.
4. **Verify internal 24VDC supply** by measuring voltage at the STO terminals with a multimeter. The drive should provide 24VDC when powered and the safety circuit is closed.
5. **Review parameter 31.22** by navigating to the drive's parameter group 31 and checking the STO diagnostics setting. If no external safety circuit is used, set it to Disabled or None.
6. **Reset the fault** by cycling power to the drive or using parameter 96.08 (Control board boot) to clear the A5A0 code.
7. **Test run the drive** under normal operating conditions to confirm the fault does not return and the motor runs smoothly.

## Parts Often Needed

| Part | Notes |
|------|-------|
| ABB ACS580 internal 24V power supply board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-a5a0-fault-code&k=ABB+ACS580+internal+24V+power+supply+board&tag=errorcodefixes-20) \| Replace if 24VDC is missing at the STO terminals and all external wiring is correct. |
| ABB ACS580 control board (main PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-a5a0-fault-code&k=ABB+ACS580+control+board+%28main+PCB%29&tag=errorcodefixes-20) \| Replace only if the STO circuit, wiring, and power supply are confirmed good but the fault persists. |

## When to Call a Pro

Call a qualified industrial electrician or controls technician if you are not familiar with VFD safety circuits, 24VDC measurements, or parameter programming. Safe Torque Off is a critical safety function, and incorrect troubleshooting can create hazards. A professional should handle any work that involves replacing internal power supply boards or control boards, diagnosing electrical noise issues, or integrating the drive with machine safety systems. If the fault returns intermittently or you cannot locate the open circuit, a technician with a scope and wiring diagrams can trace the signal path and identify the root cause.

**Rough cost:** A pro service call runs about $150-400 depending on whether the fix is wiring or a board replacement.
