---
title: "Weil-McLain Boiler A09 Error - Causes & Fix"
description: "A09 means gas valve fault. The control detected incorrect voltage or response from the gas valve. Usually the gas valve itself has failed."
pubDatetime: 2026-07-01T09:49:31Z
modDatetime: 2026-07-01T09:49:31Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - boiler
  - weil-mclain
money_part: "Gas valve (Weil-McLain OEM)"
most_likely_cause: "Failed gas valve"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify the gas shutoff valve is fully open and other gas appliances in the home are working"
  - "Check the fault history menu to confirm the code is persistent (hold WM logo, go to Contractor Menu, Diagnostics, Fault History)"
part_price: "$120-250"
---

## Weil-McLain Boiler A09 Error — What It Means

The A09 error code on a Weil-McLain boiler indicates a gas valve fault. The control module detected an incorrect operation, voltage, or response from the gas valve during the ignition sequence or run cycle. This means the control board cannot confirm the gas valve is opening or closing properly, or it detected an electrical anomaly such as a short circuit, open circuit, or implausible voltage on the gas valve circuit.

This is a critical safety lockout. Weil-McLain explicitly states technicians must not attempt to reset this code manually until the fault is diagnosed and repaired, as it prevents un-metered gas flow. The boiler will remain locked out until a qualified technician identifies and corrects the underlying problem.

## Before You Replace Anything

Some technicians replace the control board first, but the gas valve itself is far more often the culprit. Test the valve coil resistance (should be 20-100 Ω typical, not 0 or infinite) and verify 24V AC is reaching the valve terminals before replacing the board.

[Jump to Fix](#fix)

## Common Causes

- **Failed gas valve (~60%)** The internal solenoid or coil within the gas valve is defective (open or shorted), preventing the valve from responding to control signals.
- **Faulty wiring or connections (~25%)** Corroded, loose, or broken wires between the control module and the gas valve, or a poor ground connection, interrupt communication.
- **Control module failure (~10%)** The control board itself is failing to drive the gas valve correctly (less common than valve failure, but possible).
- **New installation issues (~5%)** Gas lines may not be purged, or the gas valve may not be receiving correct supply pressure (3.5 to 11 inches w.c. spec), though a stubborn valve issue can trigger A09.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Are other gas appliances in the home (stove, water heater) working normally?</summary>
<div class="dtree-body"><strong>Yes:</strong> The gas supply is likely fine. The problem is inside the boiler (valve or wiring).<br><strong>No:</strong> Check the main gas shutoff and call your gas utility to verify supply pressure before troubleshooting the boiler.</div>
</details>

<details class="dtree"><summary>Is this a brand-new installation or recent service?</summary>
<div class="dtree-body"><strong>Yes:</strong> The gas line may need purging, or the valve may have a wiring error. Call the installer to complete commissioning and purge air from the gas line.<br><strong>No:</strong> The gas valve or its wiring has likely failed and needs professional diagnosis and replacement.</div>
</details>

<details class="dtree"><summary>Did you hear the gas valve click when the boiler tried to fire before the A09 appeared?</summary>
<div class="dtree-body"><strong>Yes:</strong> The valve may be opening mechanically but has an electrical fault (coil short or open). A technician should test valve resistance.<br><strong>No:</strong> The valve is not responding at all. Check wiring first, then replace the valve if wiring is intact.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Do not reset the boiler.** Weil-McLain requires you to diagnose and repair the fault before clearing the lockout, as A09 prevents un-metered gas flow.
2. **Verify gas supply.** Confirm the gas shutoff valve is fully open and other gas appliances in the home are working to rule out a general supply issue.
3. **Inspect wiring and connections.** Disconnect power, then visually inspect the wires connecting the gas valve to the control module for damage, corrosion, or loose connections. Check for continuity in the wiring harness.
4. **Test gas valve resistance.** Disconnect the gas valve wires and measure the resistance across the coil terminals using a multimeter. Typical gas valve coils range from 20-100 Ω. If the reading is 0 Ω (short) or infinite Ω (open), the valve is defective.
5. **Test voltage at the gas valve.** Power the unit and enter the ignition sequence. Measure the voltage at the gas valve terminals. Weil-McLain typically drives gas valves with 24V AC. If the control board outputs 24V but the valve does not respond (no click or open), the valve is dead.
6. **Replace the gas valve** if resistance is out of spec or the valve does not open with 24V applied. If the valve checks out perfectly but the control board does not output voltage, replace the control module.
7. **Purge the gas line** (new installations only). If the boiler is new, purge the gas line to remove air before final testing and commissioning.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Gas valve (Weil-McLain OEM) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a09-error-code&k=Gas+valve+%28Weil-McLain+OEM%29&tag=errorcodefixes-20) \| Verify your boiler model and serial number to order the correct valve assembly. |
| Control module (Weil-McLain control board) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a09-error-code&k=Control+module+%28Weil-McLain+control+board%29&tag=errorcodefixes-20) \| Order only if the gas valve tests good and the board does not output 24V AC to the valve. |

## When to Call a Pro

Call a licensed HVAC or boiler technician immediately. The A09 code is a critical safety lockout involving the gas valve, and attempting to reset it without proper diagnosis can create a gas leak or fire hazard. The repair requires working with gas lines, testing live 24V AC circuits, and interpreting electrical measurements that are beyond typical homeowner tools and training. Weil-McLain explicitly requires professional diagnosis before clearing this fault. A qualified technician will test the gas valve coil resistance, verify control board output voltage, inspect wiring for shorts or opens, and replace the failed component safely. Do not attempt to bypass the lockout or replace parts based on guesswork.

**Rough cost:** A pro service call runs about $250-500.

## See Also

- [Weil-McLain A121 Error Code - Causes & Fix](/posts/weil-mclain-boiler-a121-error-code/)
- [Weil-McLain A82 Error Code - Causes & Fix](/posts/weil-mclain-boiler-a82-error-code/)
- [Weil-McLain A155 Error - Causes & Fix](/posts/weil-mclain-boiler-a155-error-code/)
- [Weil-McLain A117 Error Code - Causes & Fix](/posts/weil-mclain-boiler-a117-error-code/)
