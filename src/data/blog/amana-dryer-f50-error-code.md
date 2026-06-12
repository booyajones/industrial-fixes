---
title: "Amana Dryer F50 Error Code - Causes & Fix"
description: "F50 means the control board can't detect motor spin. Most often the rotor position sensor has failed. Replace the sensor or motor assembly."
pubDatetime: 2026-06-10T22:07:23Z
modDatetime: 2026-06-10T22:07:23Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - appliance
  - dryer
  - amana
money_part: "Rotor Position Sensor (RPS)"
most_likely_cause: "Failed Rotor Position Sensor (RPS)"
likelihood: "the most common cause"
diy_or_pro: "diy"
---

## Amana Dryer F50 Error Code — What It Means

The F50 error code signals a communication failure between the Motor Control Unit (MCU) and the Main Control Board. The main board is trying to monitor the motor's operation through the Rotor Position Sensor (RPS), but it is not receiving the expected feedback signal. This means the system cannot confirm the motor is spinning correctly, or the sensor is not detecting the spin.

The RPS sensor generates voltage pulses as the motor turns. When those pulses don't reach the main board, the F50 error appears and the dryer stops. This is different from airflow errors or simple power failures. It points directly to the motor-sensor-control loop.

## Before You Replace Anything

Many people replace the entire main control board first. Before ordering any board, test the RPS sensor resistance with an ohmmeter. If it reads outside the 150-250Ω range (often infinite or zero when failed), the sensor is the problem and costs far less than a control board.

[Jump to Fix](#fix)

## Common Causes

- **Failed Rotor Position Sensor (RPS) (~45%)** The sensor embedded in or near the motor has failed internally and no longer generates the voltage pulses needed to confirm rotation.
- **Failed Motor Control Unit (MCU) (~25%)** The board that drives the motor and processes the RPS signal has failed, so it cannot read or relay the feedback even if the sensor is good.
- **Loose or Corroded Wiring Connections (~15%)** The wires connecting the MCU to the main board, or the MCU to the RPS sensor, are disconnected, frayed, or have high resistance from corrosion.
- **Mechanical Motor Lockup (~10%)** The motor bearings are seized or the drum is jammed by a foreign object, preventing the motor from spinning and the RPS from registering a signal.
- **Failed Main Control Board (~5%)** The main board has a fault in the input circuit where it receives the RPS signal, though this is less common than the other causes.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the drum spin freely by hand when you open the door and rotate it?</summary>
<div class="dtree-body"><strong>Yes:</strong> The drum is not jammed. The fault is likely electrical (sensor, wiring, or control board). Proceed to testing the RPS sensor resistance.<br><strong>No:</strong> The drum is jammed or the motor bearings are seized. Remove any foreign objects from the drum and blower housing. If still locked, the motor or bearing may need replacement.</div>
</details>

<details class="dtree"><summary>When you unplug the dryer, open the motor housing, and measure the RPS sensor resistance, does it read between 150-250Ω?</summary>
<div class="dtree-body"><strong>Yes:</strong> The sensor is within spec. Check all wiring connections for continuity and inspect the MCU and main board for visible damage or burn marks.<br><strong>No:</strong> The RPS sensor is failed (infinite or zero resistance). Replace the sensor or the motor assembly that includes the sensor.</div>
</details>

<details class="dtree"><summary>After replacing the RPS sensor, does the F50 error clear and the dryer run normally?</summary>
<div class="dtree-body"><strong>Yes:</strong> The sensor was the cause. The repair is complete.<br><strong>No:</strong> The MCU or main control board is likely failed. Test continuity between the MCU and main board, then replace the faulty control component.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off power at the circuit breaker** for five minutes, then restore power and attempt a Time Dry cycle to see if the error clears (this rules out a transient fault).
2. **Open the dryer door** and spin the drum by hand to confirm it rotates freely without binding or scraping sounds (foreign objects or bad bearings will prevent rotation).
3. **Unplug the dryer** and remove the top panel or front panel to access the motor and Motor Control Unit (consult your model's service manual for panel removal steps).
4. **Locate the Rotor Position Sensor connector** on the MCU (often labeled P5 or similar) and disconnect it, then use an ohmmeter to measure resistance across the sensor pins (a good sensor reads 150-250Ω; infinite or zero means failed).
5. **Inspect all wiring** between the MCU, RPS sensor, and main control board for loose connectors, broken wires, or corrosion (use a continuity test to confirm each wire path is intact).
6. **Replace the failed component**: if the RPS sensor is out of spec, order a new sensor or motor assembly that includes the sensor; if the sensor and wiring are good, replace the MCU or main control board.
7. **Reassemble the dryer**, restore power, and run a test cycle to confirm the F50 error is cleared and the drum spins normally.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Rotor Position Sensor (RPS) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-amana-dryer-f50-error-code&k=Rotor+Position+Sensor+%28RPS%29&tag=errorcodefixes-20) \| Often sold as part of the motor assembly; verify your model number before ordering. |
| Motor Control Unit (MCU) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-amana-dryer-f50-error-code&k=Motor+Control+Unit+%28MCU%29&tag=errorcodefixes-20) \| The small board mounted on or near the motor; match the part number from your dryer's wiring diagram. |
| Main Control Board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-amana-dryer-f50-error-code&k=Main+Control+Board&tag=errorcodefixes-20) \| Only needed if testing confirms the board cannot receive the RPS signal; most expensive option, so test everything else first. |

## When to Call a Pro

Call a technician if you are uncomfortable working with electrical connections or removing panels to access the motor. If you have tested the RPS sensor and wiring and both check out, isolating whether the MCU or main board has failed requires advanced diagnostics and component swapping. A pro can bring spare boards to test on-site and avoid unnecessary parts orders. Also call if the drum will not spin by hand and you suspect a seized motor bearing, since motor replacement on some models requires special tools or disassembly of the entire cabinet.

**Rough cost:** DIY runs about $30-80 in parts, 45-90 min. A pro service call runs about $150-280.
