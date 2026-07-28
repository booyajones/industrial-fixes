---
title: "Daikin H0 Error Code - Causes & Fix"
description: "H0 means compressor current sensor abnormality on the outdoor PCB. Most often a faulty sensor circuit or PCB component failure."
pubDatetime: 2026-06-30T09:52:53Z
modDatetime: 2026-06-30T09:52:53Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - hvac
  - mini-split
  - daikin
money_part: "Daikin outdoor unit PCB"
most_likely_cause: "Faulty current sensor circuit or PCB component failure"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Turn off power at the breaker for 5-10 minutes and restart to rule out a transient glitch"
  - "Inspect outdoor PCB for visible burnt components, cracked solder joints, or loose wires"
---

## What this code means
The H0 error code on a Daikin mini split signals a compressor system sensor abnormality, specifically a fault in the compressor current sensor circuit on the outdoor unit's PCB. This sensor monitors real-time current flow to the compressor. When the signal is out of range or missing, the system halts and displays H0.

This is not a refrigerant issue, a communication error, or a temperature thermistor problem. The fault lies in the electrical circuit that tracks how much current the compressor draws. The outdoor PCB expects a valid signal from the current sensor, and when it does not receive one, it throws H0 to protect the compressor.

## Before You Replace Anything

Homeowners sometimes replace the compressor itself when the real culprit is a bad current sensor circuit or a burnt IC on the outdoor PCB. A multimeter voltage check at the sensor output terminals will pinpoint the circuit fault before spending hundreds on a compressor.

## Common Causes

- **Faulty current sensor circuit (~40%)** Open or short circuit in the compressor current sensor winding or PCB wiring causes the signal to drop out or read invalid.
- **Damaged PCB component (~35%)** Burnt IC (such as M2904), failed resistor (like R304), or cracked solder joints on the outdoor PCB interrupt the sensor signal path.
- **Loose or corroded connections (~15%)** Bad contact between the current sensor terminals and the PCB creates intermittent or missing signal.
- **Transient voltage spike (~7%)** A power surge or lightning strike damages the sensor circuit components on the outdoor PCB.
- **Compressor electrical issue (~3%)** Abnormal current draw from a degrading compressor can confuse the sensor, though this is less common than circuit faults.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the error clear for more than a few hours after a full power reset (breaker off 10 minutes)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Likely a transient glitch or loose connection. Monitor for recurrence and inspect outdoor PCB connections.<br><strong>No:</strong> The fault is hardware-related. Proceed to PCB inspection and sensor circuit testing.</div>
</details>

<details class="dtree"><summary>Do you see any burnt or discolored components on the outdoor PCB (IC, resistors, solder joints)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Burnt components confirm PCB damage. Replace the failed IC or resistor, or swap the entire outdoor PCB if severely damaged.<br><strong>No:</strong> Fault may be in the current sensor winding or wiring. Test sensor output voltage and resistance with a multimeter.</div>
</details>

<details class="dtree"><summary>Does the current sensor output voltage measure between 0.5-2.5V DC during compressor operation?</summary>
<div class="dtree-body"><strong>Yes:</strong> Sensor circuit is working. Check for issues elsewhere (compressor current draw, PCB logic). Consult service manual.<br><strong>No:</strong> Sensor circuit fault confirmed. Replace the current sensor or repair the PCB circuit (IC, resistor, solder joints).</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off power** at the breaker to both indoor and outdoor units for 5-10 minutes, then restart to rule out a transient glitch.
2. **Open the outdoor unit** and remove the service panel to access the PCB.
3. **Visually inspect the PCB** for burnt components (M2904 IC, R304 resistor), cracked solder joints, or loose wires on the current sensor circuit.
4. **Test the current sensor output** with a multimeter in DC voltage mode. Measure the sensor output terminals during compressor operation (expected range is typically 0.5-2.5V DC, consult your model's service manual).
5. **Check resistance** of R304 on the PCB (should be around 2kΩ) and the current sensor winding (typically less than 10kΩ, verify with service manual).
6. **Replace faulty components** such as the M2904 IC, R304 resistor, or re-solder cracked joints. If the PCB is severely damaged, replace the entire outdoor PCB (use model-specific part number).
7. **Reassemble and power up** the system. Monitor compressor operation via the diagnostic mode to verify no abnormal current spikes or stalling, then clear the error code.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Daikin outdoor unit PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-mini-split-h0-error-code&k=Daikin+outdoor+unit+PCB&tag=errorcodefixes-20) \| Model-specific part number required. Swap if IC or circuit damage is severe. |
| M2904 IC | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-mini-split-h0-error-code&k=M2904+IC&tag=errorcodefixes-20) \| Common PCB component for current sensor circuit. Check your PCB layout before ordering. |
| R304 resistor (2kΩ) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-mini-split-h0-error-code&k=R304+resistor+%282k%CE%A9%29&tag=errorcodefixes-20) \| Small resistor in sensor circuit. Verify value with service manual or PCB diagram. |

## When to Call a Pro

Call a licensed HVAC technician if the H0 code returns after a power reset or if you are not comfortable working with high-voltage circuits and PCB-level diagnostics. Compressor current sensor faults require multimeter testing, soldering skills, and a working knowledge of refrigerant systems. If the outdoor PCB needs replacement or if the compressor itself is drawing abnormal current, the job demands refrigerant recovery, electrical safety procedures, and warranty compliance. Attempting PCB repairs without proper training can damage the board further or create a shock hazard.

**Rough cost:** A pro service call runs about $200-500.
