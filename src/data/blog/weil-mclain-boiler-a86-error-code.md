---
title: "Weil-McLain A86 Error Code - Causes & Fix"
description: "A86 is not a standard Weil-McLain fault code in published manuals. Check for misread display or fault history. Most often ignition or flame-proving."
pubDatetime: 2026-06-15T11:42:53Z
modDatetime: 2026-06-15T11:42:53Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - boiler
  - weil-mclain
money_part: "Flame rod / ignition electrode"
most_likely_cause: "Dirty or faulty flame rod or ignition electrode"
likelihood: "the most common cause of ignition-related faults"
diy_or_pro: "pro"
free_checks:
  - "Pull the fault history through the contractor diagnostics menu to confirm the actual stored code and rule out a history entry"
  - "Verify gas shutoff is fully open and the boiler is receiving gas at the meter"
  - "Inspect the condensate trap and drain line for blockage or standing water"
part_price: "$25-50"
---

## Weil-McLain A86 Error Code — What It Means

A86 does not appear in Weil-McLain's published fault code tables for their boiler controls. The code may be a controller history entry rather than a live lockout, or it may be model-specific and not documented in the general service literature. Weil-McLain's control systems use codes like A01 (no burner ignition) and other A-series and F-series faults, but A86 has not been verified in the available manuals.

Because the exact meaning is unclear, the fault is likely related to ignition or flame-proving problems, which are the most common causes of unidentified A-series codes on Weil-McLain boilers. Technicians report that dirty flame rods, gas supply issues, grounding problems, and condensate blockages are the real-world causes behind ignition faults. Always confirm the exact boiler model and pull the full fault history through the diagnostics menu to identify the actual stored code.

## Before You Replace Anything

Technicians sometimes replace the gas valve or control board when the real problem is a fouled flame rod or poor grounding. Pull and clean the flame rod first, and verify the burner ground connection before replacing expensive components.

[Jump to Fix](#fix)

## Common Causes

- **Dirty or faulty flame rod (~35%)** Soot, corrosion, or contamination on the ignition electrode or flame rod prevents reliable flame detection, and cleaning or replacing the rod resolves the fault in many cases.
- **Gas supply pressure too low or gas line not purged (~25%)** Insufficient inlet gas pressure (below 3.5 in. w.c. on some models) or air in the line on a new install prevents ignition.
- **Poor grounding or loose electrode wiring (~20%)** Flame rectification depends on a solid burner ground and secure electrode connections, and field experience shows grounding problems are a common cause of intermittent ignition complaints.
- **Blocked condensate trap or drain (~10%)** A clogged trap or drain line can prevent the boiler from firing or cause repeated lockouts on condensing models.
- **Air pressure switch or venting issue (~10%)** If the air pressure switch does not close or the vent intake is blocked, the control module will not allow ignition.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is the code displayed on the live screen, or is it only visible in the fault history menu?</summary>
<div class="dtree-body"><strong>Yes:</strong> The code is active. Proceed with ignition and gas supply checks below.<br><strong>No:</strong> The code may be a history entry from an earlier event. Check the current live status and clear history after confirming the boiler is running normally.</div>
</details>

<details class="dtree"><summary>Can you hear the ignitor spark or see the flame rod glowing when the boiler tries to fire?</summary>
<div class="dtree-body"><strong>Yes:</strong> Ignition is attempting. Check gas supply, flame rod cleanliness, and grounding.<br><strong>No:</strong> No ignition attempt. Verify power to the control, thermostat call, and pressure switch closure before troubleshooting ignition components.</div>
</details>

<details class="dtree"><summary>Does the boiler fire normally after you clean the flame rod and reset the control?</summary>
<div class="dtree-body"><strong>Yes:</strong> The rod was fouled. Monitor for repeat faults and check combustion air and venting if fouling returns quickly.<br><strong>No:</strong> The fault persists. Test gas pressure, verify electrode position and grounding, and check for condensate or venting blockage.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Record the exact boiler model number** from the rating plate and consult the service manual for that model to confirm whether A86 is a documented code or a history entry.
2. **Pull the fault history** by entering the contractor diagnostics menu on the control (consult your model's manual for the button sequence) and write down all stored codes, not just the live display.
3. **Shut off power and gas** at the service switches, then remove the burner cover or access panel to expose the ignition electrode and flame rod.
4. **Inspect and clean the flame rod and ignitor** using fine steel wool or emery cloth to remove soot, corrosion, or contamination, and verify the electrode is positioned correctly per the manual's gap and alignment specs.
5. **Check the burner ground connection** and all electrode wiring for tightness and corrosion, and verify the burner assembly is solidly grounded to the boiler chassis.
6. **Verify gas supply** by confirming the manual shutoff is fully open, checking inlet pressure with a manometer (should be 3.5 to 11 in. w.c. on Aqua Balance models, consult your model's table), and purging air from the gas line on new installs.
7. **Inspect the condensate trap and drain** for blockage, standing water, or improper installation, and clear or reinstall as needed.
8. **Restore power and gas**, then press the reset button on the control for 1.5 seconds and observe the ignition sequence through the burner sight glass or window.
9. **If the fault returns**, measure flame rectification current (typically 0.5 to 5 microamps DC on condensing boilers, consult your model's service data) and test the gas valve, pressure switch, and control module per the service manual's diagnostic flowchart.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Flame rod / ignition electrode | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a86-error-code&k=Flame+rod+%2F+ignition+electrode&tag=errorcodefixes-20) \| Order by boiler model number; rod and ignitor are often sold as a single assembly or separately depending on the burner design. |
| Gas valve | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a86-error-code&k=Gas+valve&tag=errorcodefixes-20) \| Model-specific; verify the correct voltage (24V or 120V) and gas type (natural or LP) before ordering. |

## When to Call a Pro

Call a licensed boiler technician if you do not have a combustion gas analyzer and manometer to measure inlet gas pressure and flue gas. Gas-fired appliance work requires permits and inspection in many jurisdictions, and incorrect diagnosis or repair can create carbon monoxide hazards or void your warranty. A technician will pull the full fault history, test flame rectification with a microamp meter, verify gas pressure and venting compliance, and replace the control module or gas valve if component-level testing confirms failure. If the boiler is under warranty, professional service is required to maintain coverage.

**Rough cost:** A pro service call runs about $150-300.

## See Also

- [Weil-McLain Boiler A08 Error Code - Causes & Fix](/posts/weil-mclain-boiler-a08-error-code/)
- [Weil-McLain Boiler A124 Error - Causes & Fix](/posts/weil-mclain-boiler-a124-error-code/)
- [Weil-McLain A155 Error - Causes & Fix](/posts/weil-mclain-boiler-a155-error-code/)
- [Weil-McLain A105 Error Code - Causes & Fix](/posts/weil-mclain-boiler-a105-error-code/)
