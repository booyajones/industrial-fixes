---
title: "Amana Dryer F25 Error Code - Causes & Fix"
description: "F25 is a control fault on Amana dryers. Most common fix: power-cycle the breaker for 5 minutes. If it returns, check the inlet thermistor."
pubDatetime: 2026-06-10T18:33:44Z
modDatetime: 2026-06-10T18:33:44Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - appliance
  - dryer
  - amana
money_part: "Inlet thermistor / inlet temperature sensor"
most_likely_cause: "transient control glitch cleared by power reset"
likelihood: "the most common first step that resolves the code"
diy_or_pro: "diy"
---

## Amana Dryer F25 Error Code — What It Means

F25 is a manufacturer-defined control fault code on Amana dryers. Amana's official product-help system instructs you to power-cycle the unit as the first remedy but does not publish the full plain-English definition in publicly available documentation. Field service sources commonly associate F25 with a shorted inlet thermistor or inlet temperature sensor circuit problem, though this interpretation is not confirmed by visible Amana text. The safest manufacturer-grounded statement is that F25 signals a dryer control fault requiring a power reset and further component diagnosis if the code returns after the reset.

## Before You Replace Anything

Homeowners sometimes replace the main control board when the inlet thermistor is actually shorted. Measure thermistor resistance with a multimeter (disconnected from power) before ordering a board.

[Jump to Fix](#fix)

## Common Causes

- **Transient control glitch or software latch-up (~40%)** A temporary fault in the control board memory or microprocessor that clears after a full power cycle, per Amana's documented first step.
- **Shorted inlet thermistor or inlet temperature sensor (~35%)** The inlet temperature sensor develops an internal short or reads out of range, triggering a control fault that persists after reset.
- **Corroded or loose thermistor harness connection (~15%)** Oxidation, vibration, or heat damage at the sensor connector causes intermittent or shorted readings without the sensor itself failing.
- **Restricted airflow driving abnormal temperature behavior (~7%)** Lint blockage in the vent, blower wheel, or duct causes overheating that stresses thermal components and can accompany repeated temperature faults.
- **Failed main control board temperature-input circuit (~3%)** The sensing circuit on the control board itself shorts or drifts, generating the fault even when the thermistor tests good.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the F25 code clear and stay gone after you turn off both breakers for five minutes and restore power?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault was a transient glitch. Run a full heat cycle and monitor; if the code does not return, no further repair is needed.<br><strong>No:</strong> The fault is persistent. Proceed to test the inlet thermistor and check the harness for shorts or loose connections.</div>
</details>

<details class="dtree"><summary>With power disconnected, does the inlet thermistor measure close to 50,000 ohms at room temperature?</summary>
<div class="dtree-body"><strong>Yes:</strong> The sensor itself is probably good. Inspect the wiring harness and connector to the sensor and control board for corrosion or damage, then suspect the control board if wiring is clean.<br><strong>No:</strong> The thermistor is shorted or open. Replace the inlet temperature sensor and verify the code clears.</div>
</details>

<details class="dtree"><summary>Is your dryer vent duct clean, short, and free of kinks or crushed sections?</summary>
<div class="dtree-body"><strong>Yes:</strong> Airflow is adequate. Focus diagnostics on the thermistor circuit and control board.<br><strong>No:</strong> Clean the vent, lint screen, and blower wheel thoroughly. Restricted airflow can contribute to overheating and temperature-sensor stress, even if it is not the root cause of F25.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off both circuit breakers** feeding the dryer (most 240 V dryers use two breakers) and wait a full five minutes to allow the control board to discharge and reset, per Amana's documented procedure for F25.
2. **Restore power and start a normal cycle** to see whether the fault clears. If the code does not return, the issue was transient and no further repair is needed.
3. **If F25 returns immediately or within one cycle**, disconnect power again and locate the inlet thermistor or inlet temperature sensor, typically mounted on the blower housing or near the air inlet.
4. **Disconnect the thermistor connector** and use a multimeter set to resistance (ohms) to measure across the sensor terminals at room temperature. Field sources report about 50,000 ohms as a typical check point, though this is not confirmed as an Amana factory specification.
5. **Inspect the wiring harness and connector** to the thermistor and the main control board for loose pins, corrosion, heat damage, or any wire that has chafed through insulation and shorted to the frame.
6. **Replace the inlet thermistor** if it reads zero ohms (shorted), infinite ohms (open), or significantly off the expected value. If the sensor tests good, replace the main control board because the fault lies in the board's input circuit.
7. **Clean the lint screen, vent duct, and blower wheel** before reassembly. Restricted airflow can drive abnormal temperature behavior that stresses thermal components and contributes to recurring faults.
8. **Reconnect all harnesses, restore power, and run a full heat cycle** to verify that F25 does not reappear and that the dryer heats and dries normally.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Inlet thermistor / inlet temperature sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-amana-dryer-f25-error-code&k=Inlet+thermistor+%2F+inlet+temperature+sensor&tag=errorcodefixes-20) \| Match the part number on your original sensor or use your dryer's model number to order the correct Amana OEM or equivalent aftermarket sensor. |
| Main control board (electronic control board) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-amana-dryer-f25-error-code&k=Main+control+board+%28electronic+control+board%29&tag=errorcodefixes-20) \| Only replace if the thermistor tests good and wiring is intact. Verify your model number because control boards are not interchangeable across series. |

## When to Call a Pro

Call a professional if you are uncomfortable working with 240 V wiring or if you have completed the power-cycle and thermistor checks but the code persists and you do not want to invest in a control board without confirmation. A technician can measure the control-board input circuit under power, verify that the thermistor signal path is clean, and rule out less common faults such as a grounding issue or a failed high-limit thermostat that shares the same sensing harness. Also call a pro if your dryer still overheats or fails to dry properly after the fault clears, because that points to a secondary airflow or heating-element problem that needs a full diagnostic workup.

**Rough cost:** DIY runs about $30–80 in parts, 30–60 min. A pro service call runs about $150–250 service call and sensor replacement.
