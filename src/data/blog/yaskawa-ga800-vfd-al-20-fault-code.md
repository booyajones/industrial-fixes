---
title: "Yaskawa GA800 VFD AL-20 Fault - Causes & Fix"
description: "AL-20 signals an analog input error on the Yaskawa GA800 drive. Check wiring connections and input scaling in parameters first."
pubDatetime: 2026-07-21T07:43:12Z
modDatetime: 2026-07-21T07:43:12Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "Analog input terminal block or connector kit"
most_likely_cause: "loose or damaged wiring at the analog input terminals"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Inspect all analog input terminal wiring for loose connections, corrosion, or broken strands and tighten or clean as needed"
  - "Review the analog input scaling parameters in the drive menu to confirm they match the actual input signal type and range"
  - "Power-cycle the drive to clear any transient fault conditions"
---

## Yaskawa GA800 VFD AL-20 Fault — What It Means

The AL-20 fault code on a Yaskawa GA800 variable frequency drive indicates an analog input signal problem. The drive has detected that one or more analog input channels (voltage or current) are outside the expected range or that the signal being received does not match the parameter configuration.

This alarm typically appears when the drive cannot properly read a speed reference, feedback signal, or process control input. The fault protects the drive and connected equipment by preventing operation until the input signal is corrected. The exact threshold and behavior depend on how the analog inputs are configured in your drive's parameter settings.

## Before You Replace Anything

Technicians sometimes replace the control board when the real problem is incorrect parameter scaling or a failed external sensor. Always verify the analog input signal with a multimeter and review the scaling parameters before swapping circuit boards.

[Jump to Fix](#fix)

## Common Causes

- **Loose or corroded wiring at analog input terminals (~35%)** Vibration, heat cycling, or environmental contamination can loosen terminal screws or corrode the connection points, causing intermittent or out-of-range signals.
- **Incorrect analog input parameter scaling (~25%)** The drive parameters may be set for a different input range (for example 0-10V when the sensor outputs 4-20mA), causing the drive to see the signal as invalid.
- **Failed external sensor or signal source (~20%)** A potentiometer, transducer, or PLC analog output that feeds the drive may drift out of range or fail completely, sending a signal the drive rejects.
- **Noise or interference on the analog input cable (~15%)** Unshielded or improperly routed signal wiring can pick up electrical noise from motors or power lines, corrupting the analog signal and triggering the fault.
- **Damaged drive analog input circuit (~5%)** A voltage spike, ESD event, or component failure on the drive's input board can prevent it from reading analog signals correctly.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is the analog input signal wiring fully seated and free of visible damage or corrosion?</summary>
<div class="dtree-body"><strong>Yes:</strong> Wiring is likely intact. Measure the signal voltage or current at the drive terminals with a multimeter to confirm it is within the expected range.<br><strong>No:</strong> Clean corroded terminals, re-terminate any damaged wires, and tighten all screws. Test the drive again before proceeding.</div>
</details>

<details class="dtree"><summary>Does the measured signal voltage or current fall within the range configured in the drive parameters?</summary>
<div class="dtree-body"><strong>Yes:</strong> Signal is correct. The drive's analog input circuit or internal wiring may be damaged. Consider calling a technician to test the input board.<br><strong>No:</strong> Either the external sensor is faulty or the drive parameters are set incorrectly. Verify the sensor output specification and adjust the drive's input scaling parameters to match.</div>
</details>

<details class="dtree"><summary>Does the fault clear after you disconnect the analog input signal and set the drive to run from the keypad or digital input?</summary>
<div class="dtree-body"><strong>Yes:</strong> The problem is in the external wiring or sensor, not the drive itself. Troubleshoot or replace the signal source.<br><strong>No:</strong> The drive may have a fault in its analog input circuitry. Professional diagnosis and possible board replacement are needed.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive** and lock out the upstream disconnect or breaker to prevent accidental energization during inspection.
2. **Remove the terminal cover** and visually inspect all analog input terminal blocks for loose screws, broken wire strands, corrosion, or signs of overheating.
3. **Tighten all analog input terminal screws** to the torque specification in your drive manual and re-seat any removable connectors.
4. **Measure the analog input signal** at the drive terminals using a multimeter set to the appropriate voltage or current range and compare the reading to the expected signal from your sensor or controller.
5. **Access the drive parameter menu** and verify that the analog input type, scaling, and range parameters match the actual signal being supplied (consult your model's parameter table for the correct settings).
6. **Check for noise** by inspecting the analog signal cable routing. Separate signal wiring from power cables and verify that shielded cable is used with the shield grounded at one end only.
7. **Clear the fault** from the drive keypad or parameter menu, restore power, and test operation. If the fault returns immediately, measure the signal again to confirm it remains stable and within range.
8. **Replace the external sensor or signal source** if measurements show the output is out of specification or drifting, or contact a qualified technician if the drive input circuit is suspect.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Analog input terminal block or connector kit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-al-20-fault-code&k=Analog+input+terminal+block+or+connector+kit&tag=errorcodefixes-20) \| Use only genuine Yaskawa replacement parts to match terminal pitch and ratings. |
| Shielded twisted-pair signal cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-al-20-fault-code&k=Shielded+twisted-pair+signal+cable&tag=errorcodefixes-20) \| Select cable rated for industrial environments and appropriate for the signal type (voltage or current). |

## When to Call a Pro

Call a qualified electrician or automation technician if you are not trained to work with industrial control equipment or if measurements confirm the drive's internal analog input circuit is damaged. VFD troubleshooting involves live high-voltage DC bus capacitors that can remain charged even after input power is removed, and incorrect wiring or parameter changes can damage connected machinery. A professional can safely diagnose board-level faults, verify proper grounding and shielding practices, and reprogram parameters to match your process requirements.

**Rough cost:** A pro service call runs about $200-500.
