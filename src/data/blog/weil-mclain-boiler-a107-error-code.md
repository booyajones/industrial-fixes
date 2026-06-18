---
title: "Weil-McLain Boiler A107 Error - Causes & Fix"
description: "A107 typically indicates a temperature sensor or thermistor fault. Most often fixed by reseating wiring or replacing the sensor."
pubDatetime: 2026-06-16T11:16:51Z
modDatetime: 2026-06-16T11:16:51Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - boiler
  - weil-mclain
money_part: "Thermistor / temperature sensor (OEM or equivalent for your Weil-McLain model)"
most_likely_cause: "loose or corroded sensor wiring and connectors"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power-cycle the boiler (switch off, wait 30 seconds, restart) and check if the fault clears"
  - "Inspect the sensor wiring harness and connector for visible corrosion, moisture, or loose pins"
part_price: "$25-60"
---

## Weil-McLain Boiler A107 Error — What It Means

The A107 error code on Weil-McLain boilers is most commonly described by service sources as a thermistor or temperature sensor fault, indicating loss of sensor contact or a failed sensing circuit. On some hybrid hot-water products the same code may refer to a heat-pump communication error, so the exact meaning depends on your specific model and control platform. The boiler's control board cannot read accurate temperature data, which prevents safe operation and triggers a lockout.

Because Weil-McLain publishes fault-code definitions specific to each boiler series (CGa, Ultra, Evergreen, WM97+), you should consult your model's installation and service manual to confirm the A107 definition for your unit. In the field, this code most often points to a wiring issue, a failed thermistor, or less commonly a control-board fault.

## Before You Replace Anything

Many people replace the control board first, but most A107 faults are wiring or sensor problems. Test the thermistor resistance with a multimeter and inspect all connectors before ordering a new PCB.

[Jump to Fix](#fix)

## Common Causes

- **Loose or corroded sensor wiring (~40%)** Vibration, moisture, or age causes pins and terminals to lose contact, interrupting the temperature signal to the control board.
- **Failed thermistor or temperature sensor (~30%)** The sensing element itself drifts out of specification or fails open, so the board reads no valid temperature.
- **Control board fault (~15%)** The PCB's sensor input circuit or communication logic fails, misreading or ignoring a good sensor signal.
- **Power or voltage irregularity (~10%)** Low line voltage, a weak transformer, or a poor ground can cause intermittent communication faults that register as sensor errors.
- **Moisture intrusion or scale buildup (~5%)** Water infiltration around the sensor well or heavy scale deposits can short the thermistor leads or insulate the probe tip.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault clear after you power-cycle the boiler and stay off for at least five minutes of run time?</summary>
<div class="dtree-body"><strong>Yes:</strong> The problem is intermittent, likely a marginal connector or voltage sag. Monitor for a few days and inspect wiring closely during the next occurrence.<br><strong>No:</strong> The fault is persistent. Proceed to test the sensor resistance and wiring continuity with a multimeter.</div>
</details>

<details class="dtree"><summary>When you disconnect the thermistor connector and measure the sensor's resistance at room temperature, is the reading within the range shown in your boiler's service manual (often 8-12 kΩ near 70°F, but consult your model's table)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The sensor itself is good. Check wiring continuity from the sensor plug all the way to the control board, then test board input voltage if wiring is intact.<br><strong>No:</strong> The thermistor has failed. Replace it with the correct OEM or equivalent part for your boiler model.</div>
</details>

<details class="dtree"><summary>After replacing the sensor or repairing wiring, does the A107 fault return immediately on the next call for heat?</summary>
<div class="dtree-body"><strong>Yes:</strong> The control board's sensor input circuit is faulty. Replace the PCB or call a qualified technician to confirm the diagnosis.<br><strong>No:</strong> The repair is successful. Clear the fault history from the boiler's diagnostic menu and monitor normal operation.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off power** to the boiler at the service switch and the circuit breaker, then turn off the gas supply valve.
2. **Retrieve the fault history** using your boiler's diagnostic menu (consult the manual for button sequence) to confirm A107 and check for additional codes.
3. **Locate the thermistor** or temperature sensor, typically mounted in the supply or return manifold or in a well on the heat exchanger. Refer to your service manual's wiring diagram.
4. **Disconnect the sensor connector** and inspect both halves for corrosion, bent pins, or moisture. Clean with electrical contact cleaner and reseat firmly.
5. **Measure sensor resistance** at room temperature with a multimeter set to ohms. Compare the reading to the resistance table in your boiler's manual (typical range 8-12 kΩ near 70°F, but varies by model).
6. **Test wiring continuity** from the sensor plug back to the control board if the sensor reads correctly. Look for breaks, shorts to ground, or high resistance in the harness.
7. **Replace the thermistor** if resistance is out of spec or infinite, using the exact OEM part number from your boiler's parts list or a verified equivalent.
8. **Restore power and gas**, clear the fault code per the manual's instructions, and run the boiler through a full heat cycle to verify the repair.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Thermistor / temperature sensor (OEM or equivalent for your Weil-McLain model) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a107-error-code&k=Thermistor+%2F+temperature+sensor+%28OEM+or+equivalent+for+your+Weil-McLain+model%29&tag=errorcodefixes-20) \| Match the part number in your service manual or on the original sensor body. |
| Sensor wiring harness or connector repair kit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a107-error-code&k=Sensor+wiring+harness+or+connector+repair+kit&tag=errorcodefixes-20) \| Use if the plug is damaged or corroded beyond cleaning. |
| Control board / PCB (model-specific) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a107-error-code&k=Control+board+%2F+PCB+%28model-specific%29&tag=errorcodefixes-20) \| Only after confirming sensor and wiring test good and the fault persists. |

## When to Call a Pro

Call a licensed heating technician if you are not comfortable working with 120 V power, gas piping, or boiler controls. A pro should also diagnose the fault if you have already tested the sensor and wiring and both check out, since board-level troubleshooting often requires specialized meters and access to OEM service bulletins. If the A107 code appears alongside other faults, or if your boiler has a sealed combustion system or integrated heat-pump module, professional diagnosis is the safest path to avoid misdiagnosis and wasted parts.

**Rough cost:** A pro service call runs about $150-350.
