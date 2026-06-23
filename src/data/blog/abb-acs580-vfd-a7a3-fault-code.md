---
title: "ABB ACS580 A7A3 Fault - Causes & Fix"
description: "A7A3 means current sensor calibration failed. Most common fix: re-run parameter 99.13 calibration or clean control board connections."
pubDatetime: 2026-06-21T10:42:14Z
modDatetime: 2026-06-21T10:42:14Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - abb
money_part: "ABB ACS580 Control Board"
most_likely_cause: "Failed auto-calibration routine due to incorrect motor parameters or noise"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power cycle the drive (turn off, wait 5 minutes, turn on) and check if the fault clears"
  - "Verify parameter 99.06 (Motor nominal current) is less than parameter 30.17 (Maximum current)"
  - "Navigate to parameter 99.13 and execute the Current measurement calibration routine"
no_buy_pct: "60%"
---

## ABB ACS580 A7A3 Fault — What It Means

The A7A3 fault code on an ABB ACS580 drive indicates that the internal current sensor calibration has failed or is invalid. The drive's firmware could not successfully calibrate the current measurement sensors, typically during startup or when the auto-calibration routine runs. Because the drive cannot accurately measure motor current, which is a critical safety parameter for overcurrent protection and torque control, it throws this fault to prevent unsafe operation.

This is not the same as an overcurrent fault (F0001). Instead, the drive is reporting that it cannot trust the current measurement itself, not that the current is simply too high. The fault usually appears as A7A3 FILT or A7A3 FLTR on the display. It means the calibration logic detected noise, an incorrect parameter, a broken sensor connection, or an internal hardware issue that prevents reliable current sensing.

## Before You Replace Anything

Technicians sometimes replace the entire drive power board when only the control board connections are loose or dirty. Always re-run the current calibration routine (parameter 99.13) and inspect ribbon-cable connectors between the control unit and power unit before ordering new boards.

[Jump to Fix](#fix)

## Common Causes

- **Failed auto-calibration routine (~40%)** The drive could not complete parameter 99.13 calibration due to power instability, noise, or incorrect motor nominal current and torque values in parameters 99.06 and 99.12.
- **Loose or dirty control board connections (~25%)** Ribbon cables or plugs connecting the Control Unit (CU) to the Power Unit (PU) are loose, dusty, or have poor contact, preventing sensor initialization.
- **Incorrect motor parameter configuration (~15%)** Parameter 99.06 (Motor nominal current) is set higher than parameter 30.17 (Maximum current), or parameter 99.12 (Motor nominal torque) exceeds the maximum torque limit, blocking calibration logic.
- **Unstable internal 24V control supply (~10%)** The internal 24V power supply for the control board is failing or noisy, preventing sensors from initializing correctly during calibration.
- **Dust or corrosion on current sensors (~5%)** Dust accumulation or corrosion on the current sensor terminals or drive board vents interferes with accurate measurement.
- **Defective control board or current sensor (~5%)** The current sensor or the main control board has a hardware failure and cannot perform calibration even when all parameters and connections are correct.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault clear after a full power cycle (off for 5 minutes, then on)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault was likely transient noise or a one-time calibration glitch. Monitor the drive during normal operation to see if it recurs.<br><strong>No:</strong> The fault is persistent. Proceed to check motor parameters and run the calibration routine.</div>
</details>

<details class="dtree"><summary>Is parameter 99.06 (Motor nominal current) less than parameter 30.17 (Maximum current)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Motor current parameters are correctly configured. Move to step 3 and run the calibration routine.<br><strong>No:</strong> Adjust parameter 30.17 to be greater than 99.06, then re-run the calibration routine at parameter 99.13.</div>
</details>

<details class="dtree"><summary>Does the fault persist immediately after running parameter 99.13 calibration?</summary>
<div class="dtree-body"><strong>Yes:</strong> The issue is hardware related. Inspect control board connections, clean dust, and check the internal 24V supply. If the fault remains, a control board or current sensor is likely defective.<br><strong>No:</strong> The calibration succeeded and the fault should be cleared. Restart the drive and verify normal operation.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify motor parameters** by checking that parameter 99.06 (Motor nominal current) is lower than parameter 30.17 (Maximum current), and that parameter 99.12 (Motor nominal torque) is within the maximum torque limits in group 30.
2. **Run the calibration routine** by navigating to parameter 99.13 (Current measurement calibration), selecting the calibration option, and executing it. Wait for the drive to complete the routine.
3. **Power cycle the drive** if the calibration fails. Turn off the drive, wait 5 minutes for the DC bus to discharge, then power it back on and check if the fault clears.
4. **Inspect internal connections** by powering down the drive completely, opening the enclosure, and checking the ribbon cables and plugs between the Control Unit and Power Unit for loose connections or dust.
5. **Clean dust and debris** from the vents, fans, and around the control board and current sensor terminals to remove any interference with sensor readings.
6. **Check the 24V control supply** by verifying that the internal 24V supply is stable. If parameter 95.04 is set to external 24V, confirm the external supply is present and within spec.
7. **Replace the control board or current sensor** if the fault persists after re-calibration, cleaning, and connection checks. This indicates a hardware failure in the sensor or control circuitry.

## Parts Often Needed

| Part | Notes |
|------|-------|
| ABB ACS580 Control Board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-a7a3-fault-code&k=ABB+ACS580+Control+Board&tag=errorcodefixes-20) \| Only needed if calibration and connector cleaning do not resolve the fault; verify your drive frame size and part number before ordering. |
| ABB ACS580 Power Board with Current Sensors | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-a7a3-fault-code&k=ABB+ACS580+Power+Board+with+Current+Sensors&tag=errorcodefixes-20) \| Required if the current sensor itself is defective; consult ABB or a certified distributor for the correct power unit replacement. |

## When to Call a Pro

Call a qualified VFD technician or an ABB-certified service partner if the fault persists after you have verified motor parameters, run the calibration routine at parameter 99.13, and inspected control board connections. Working inside a variable frequency drive involves high-voltage DC bus capacitors that can remain charged for minutes after power-down, and incorrectly replacing boards or sensors can damage the drive or void warranties. A technician has the tools to measure the internal 24V supply, safely test current sensor circuits, and access ABB diagnostic software. If your facility does not have personnel trained in VFD repair, a service call is the safer and faster route to restoring operation.

**Rough cost:** A pro service call runs about $200-500 for service call and board replacement if needed.
