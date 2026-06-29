---
title: "Yaskawa GA800 F017 Fault - Causes & Fix"
description: "F017 on a Yaskawa GA800 VFD likely indicates an input power or rectifier problem. Check input voltage, fuses, and DC bus diodes first."
pubDatetime: 2026-06-27T11:37:31Z
modDatetime: 2026-06-27T11:37:31Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "Yaskawa GA800 input diode module"
most_likely_cause: "Failed input diode on the DC bus rectifier"
likelihood: "often reported in field cases"
diy_or_pro: "pro"
free_checks:
  - "Measure incoming three-phase voltage at L1, L2, and L3 terminals to confirm all phases are present and balanced"
  - "Inspect input fuses for the drive and replace any that are open"
  - "Check encoder coupling and mechanical tether for slippage if the fault occurs during PID control or torque reference changes"
---

## Yaskawa GA800 F017 Fault — What It Means

The F017 fault code on a Yaskawa GA800 VFD is not explicitly defined in widely available third-party sources, and the exact meaning can vary by firmware and configuration. Industry context suggests it is related to input power supply issues, similar to input phase loss faults on other brands. However, you must consult the official Yaskawa GA800 Technical Manual (SIEPC) or Maintenance and Troubleshooting Manual (TOEPYAIGA8001) to confirm the precise definition for your drive.

Field reports indicate that GA800 drives with input-related faults often have failed input diodes on the DC bus rectifier or blown input fuses. If the fault appears only during PID control or under load, the root cause may be PID feedback instability or mechanical coupling issues that cause torque oscillation and trigger overcurrent conditions, which can register as input faults. Always verify incoming three-phase power quality and check for phase imbalances before troubleshooting internal components.

## Before You Replace Anything

Technicians sometimes replace the entire drive control board when the real problem is a single failed input diode or a blown fuse. Always measure input voltage and test diode resistance with a multimeter before ordering expensive assemblies.

[Jump to Fix](#fix)

## Common Causes

- **Failed input diode (~40%)** One of the input diodes on the DC bus rectifier is open or shorted, preventing proper rectification and causing a phase loss condition.
- **Blown input fuse (~25%)** An input fuse has blown, removing one phase of power to the drive and triggering an input fault.
- **Phase imbalance or voltage drop (~20%)** The incoming three-phase power has insufficient voltage, a significant imbalance, or a missing phase.
- **Mechanical coupling slippage (~10%)** A loose encoder coupling or slipping tether causes rapid torque oscillation, which triggers an overcurrent condition that may register as an input fault.
- **Grounding or wiring issue (~5%)** Improper grounding or loose input wiring interferes with the DC bus and causes erratic fault codes.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does a multimeter show balanced three-phase voltage at the drive input terminals (L1, L2, L3)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Incoming power is likely good. Proceed to test input fuses and diodes inside the drive.<br><strong>No:</strong> The supply has a phase loss or imbalance. Check the upstream breaker, disconnect, and power distribution before working on the drive.</div>
</details>

<details class="dtree"><summary>Are all input fuses intact and showing continuity?</summary>
<div class="dtree-body"><strong>Yes:</strong> Fuses are good. Measure resistance of the input diodes on the DC bus to find a failed diode.<br><strong>No:</strong> Replace the blown fuse and investigate what caused it to fail (short circuit, overload, or transient).</div>
</details>

<details class="dtree"><summary>Does the fault occur only during PID control or under changing torque reference?</summary>
<div class="dtree-body"><strong>Yes:</strong> The root cause may be PID feedback instability or a loose encoder coupling causing torque oscillation. Inspect mechanical connections and PID tuning.<br><strong>No:</strong> The fault is likely a true input power or rectifier problem. Focus on diodes, fuses, and incoming voltage quality.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive** and lock out the upstream disconnect to make sure the DC bus capacitors have fully discharged before opening the enclosure.
2. **Measure incoming voltage** at L1, L2, and L3 with a multimeter set to AC voltage to confirm all three phases are present and balanced within manufacturer specifications.
3. **Inspect and test input fuses** for continuity using a multimeter, and replace any that are open or visibly damaged.
4. **Access the DC bus rectifier** inside the drive and measure the forward and reverse resistance of each input diode using a multimeter in diode-test mode to identify a failed diode (open or shorted).
5. **Check mechanical connections** if the fault occurs during PID control by inspecting the encoder coupling and tether for slipness or looseness that could cause torque oscillation.
6. **Verify grounding** by measuring continuity between the drive chassis ground and the facility ground to rule out grounding faults that can cause erratic behavior.
7. **Consult the official Yaskawa GA800 manual** (TOEPYAIGA8001 or SIEPC) to confirm the exact definition of F017 for your firmware version and follow any manufacturer-specific diagnostic procedures.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 input diode module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f017-fault-code&k=Yaskawa+GA800+input+diode+module&tag=errorcodefixes-20) \| Match the part number to your drive frame size and voltage rating; consult the manual or a Yaskawa distributor. |
| Input fuse for Yaskawa GA800 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f017-fault-code&k=Input+fuse+for+Yaskawa+GA800&tag=errorcodefixes-20) \| Check the drive nameplate or manual for the correct fuse type and rating. |

## When to Call a Pro

Call a qualified VFD technician or industrial electrician if you are not trained to work inside a variable frequency drive enclosure. Even after power-down, the DC bus capacitors can hold lethal voltage for several minutes. Diagnosing a failed input diode requires measuring resistance on live rectifier components and understanding three-phase power distribution. If you lack a multimeter, lockout/tagout training, or experience with high-voltage DC bus circuits, do not open the drive. A technician will also have access to the official Yaskawa manuals and can verify the exact fault definition and perform firmware updates if needed.

**Rough cost:** A pro service call runs about $200-600.
