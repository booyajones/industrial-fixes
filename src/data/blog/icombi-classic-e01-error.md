---
title: "Rational iCombi Classic Fault Codes & E01 Error Fix"
description: "E01 on the Rational iCombi Classic usually means a self-test or calibration step stopped. See the real Service (E) fault codes, likely causes, and technician fixes."
pubDatetime: 2026-05-25T00:00:39Z
modDatetime: 2026-05-25T00:00:39Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - appliance
  - rational
money_part: "Differential pressure sensor"
most_likely_cause: "Unit too hot during calibration"
---

## What this code means
E01 on the Rational iCombi Classic is not a single fixed fault. It appears in the calibration error family, where the number identifies the calibration step that failed rather than pointing to one broken part. The exact meaning depends on which self-test or manual calibration step the unit reached when the fault occurred.

Common underlying problems include the unit being too hot during calibration (sensors above 40°C), a faulty or loose differential pressure sensor, fan motor rpm detection faults, and steam heating failures. Because the number is tied to a specific step, you need to verify the unit state and work through the relevant circuits in order.

## Common Causes

- **Unit too hot during calibration** If sensors B1, B2, or B4 are above 40°C when calibration starts, the step will fail and throw E01.
- **Differential pressure sensor fault or loose cables** A faulty sensor or poor connection in the differential pressure circuit will cause the calibration step to abort.
- **Fan motor rpm detection fault** If the control cannot read accurate rpm feedback from the fan motor, the self-test step tied to airflow will fail.
- **Steam heating does not work** Problems with voltage supply, the SSR, plug X20, or gas supply (on gas models) prevent the steam step from completing.
- **Heating time too long** If the unit takes excessive time to heat, often caused by a missing or dry odor trap in the drain, the calibration step will time out.

## Step-by-Step Fix {#fix}

1. {'text': '**Verify whether the fault occurred during self-test or manual calibration** and note which step number appeared, because the displayed E01 is tied to that specific step.'}
2. {'text': '**Check if the cabinet is too hot.** Allow sensors to cool below 40°C before retrying calibration, then switch the unit off and on.'}
3. {'text': '**Inspect the differential pressure sensor and its wiring** for loose connectors, damaged cables, or sensor failure.'}
4. {'text': '**Test the fan motor rpm feedback circuit** and verify the fan motor assembly is operating correctly and sending valid rpm signals to the control.'}
5. {'text': '**Check steam heating components** if the failure is in a steam step: verify supply voltage, inspect the SSR, check plug X20 for secure connection, and confirm gas supply on gas models.'}
6. {'text': '**Inspect the drain arrangement** and verify the odor trap is installed and filled with water if heating time is excessive.'}
7. {'text': '**Switch the unit off and on after correcting the likely cause**, then re-run the calibration or self-test to confirm the fault is cleared.'}

## Parts Often Needed

| Part | Notes |
|------|-------|
| Differential pressure sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-icombi-classic-e01-error&k=Differential+pressure+sensor&tag=errorcodefixes-20) \| Match the sensor to your model's specification sheet and verify connector compatibility. |
| Fan motor assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-icombi-classic-e01-error&k=Fan+motor+assembly&tag=errorcodefixes-20) \| Order by model and serial number if rpm detection circuit tests point to motor failure. |
| Solid state relay (SSR) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-icombi-classic-e01-error&k=Solid+state+relay+%28SSR%29&tag=errorcodefixes-20) \| Used in the steam heating circuit, replace if voltage tests confirm SSR failure. |
| X20 plug / connector | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-icombi-classic-e01-error&k=X20+plug+%2F+connector&tag=errorcodefixes-20) \| Inspect for burn marks or loose pins, replace if damaged during steam circuit testing. |

## When to Call a Pro

Call a Rational-certified technician if you are not trained in commercial combi oven calibration or if initial checks (unit temperature, visible wiring faults) do not resolve the code. Steam heating and rpm detection circuits require specific test equipment and knowledge of the control architecture. Because E01 is step-specific, misdiagnosis can lead to unnecessary part replacement. If you work on gas models, a qualified gas technician must verify supply and safety interlocks.

## More Icombi Classic E01 Error fault codes

Compiled from manufacturer service manuals and authorized documentation.

| Code | What it means | Likely cause | How to fix |
| --- | --- | --- | --- |
| Service (E) 10 | SC-automatic failed (steam generator side) | The SC (steam generator refill/drain) mechanism is faulty; commonly a high water level in the SC pump or a blocked pump-off path. | Cooking is limited until resolved. Have a RATIONAL Service Partner inspect the SC pump, level electrode, and steam generator water path; descaling or pump replacement is common. |
| Service (E) 11 | Water supply steam generator failed | The steam generator's water inlet is faulty; can also stem from the level electrode or CDS flow reading. | Confirm the water shut-off valve is open and supply pressure is adequate, then have a Service Partner check the inlet solenoid and hose for blockage or scale. |
| Service (E) 12 | Water volume measurement failed | The measurement of the water quantity is incorrect (CDS / flow measurement fault), often blocked signal or low pressure. | Verify water supply and pressure, then have a technician check the CDS flow sensor and its wiring for signal or scale issues. |
| Service (E) 13 | Water detection failed | The water level in the steam generator is not recognized correctly, typically a calcified or failed level electrode. | Have a Service Partner inspect and descale or replace the level electrode. |
| Service (E) 20.1 | Cabinet sensor failed (B1 thermocouple) | The cabinet temperature probe (B1) is defective. | Let the unit cool, then have a technician test and replace the B1 cabinet thermocouple. |
| Service (E) 20.8 | Steam generator sensor failed (B5 thermocouple) | The steam generator temperature probe (B5) is defective. | Have a Service Partner test and replace the B5 steam generator thermocouple. |
| Service (E) 25 | Water volume cleanjet too low | The water quantity required during automatic cleaning is too low; low pressure, blocked inlet, nozzle, or sensor. | Cooking is blocked until cleared. Check supply pressure, the water inlet, spray nozzle, and CDS sensor; abort/complete the rinse program, then have a technician verify flow. |
| Service (E) 26 | Drain valve does not open | The ball valve cannot find the open position. | Cooking is blocked. Have a Service Partner inspect the drain ball-valve motor/actuator and replace the drain valve assembly if it is stuck. |
| Service (E) 27 | Drain valve does not close | The ball valve cannot find the closed position during initialization. | Cooking is still possible. Start/abort a rinse program; if it recurs, have a technician service the drain valve actuator. |
| Service (E) 28.2 | Cooking cabinet too hot | The temperature limit of the cooking cabinet has been exceeded. | Cooking is not possible until it cools. Let the cabinet drop below the limit; if it recurs, have a technician check the cabinet sensor and heating control. |
| Service (E) 32.1 | Check gas supply (gas units) | The gas burner is faulty / ignition not detected. | Close the shut-off valve on the gas line. A qualified gas technician must verify gas supply, the ignition box, and safety interlocks before returning to service. |
| Service (E) 33.1 | Gas burner failed - close gas supply (gas units) | The gas burner is faulty. | Close the gas line shut-off valve and call a qualified gas technician to inspect the burner, ignition box, gas valve, and wiring. |
| Service (E) 47.1 | Pump failed (CleanJet drain/waste water pump) | The CleanJet drain (waste water) pump is defective. | Cooking is blocked. Have a Service Partner inspect the pump and drain hose for blockage, then repair or replace the pump. |
| Service (E) 110 | CleanJet failed | An error occurred during the automatic clean, commonly traced to the SC pump or level electrode. | Complete/abort the clean program. Have a technician check the pump and level electrode for scale or failure. |
| Service (E) 120 | CleanJet failed | An error occurred during the automatic clean, commonly traced to the care/level pump or level electrode. | Complete/abort the clean program. Have a technician inspect and descale or replace the level electrode and check the pump. |

## How to troubleshoot Icombi Classic E01 Error

On a commercial combi oven like the Rational iCombi Classic, work the fault in a fixed order: read the exact code, note the unit state, then check the simple external causes before opening the unit. Confirm the water supply shut-off valve is open and pressure is adequate, the drain is clear, and the gas line (on gas models) is on. Many "faults" are really a starved water inlet, a blocked drain, or a hot cabinet, not a failed part.

Temperature-related codes are the most common false alarm. If a self-test or calibration is involved, let the unit cool so the cabinet (B1), quenching (B2), and moisture (B4) probes are well below their limits, then switch the unit off and back on before re-running the routine. Running a self-test on a hot or dry unit will fail the step and throw a code that looks like a hardware fault.

The next tier is water-side wear. Scale build-up drives a large share of steam generator, level-electrode, CDS flow, and CleanJet codes on hard-water sites. Descaling, checking the level electrode, and verifying flow through the SC/waste-water pump resolve many of these before any board or sensor is replaced. Sensor codes (the 20.x family) point to a specific thermocouple by suffix, so test the identified probe rather than swapping parts blindly.

Know when to stop. Rational's own guidance is that all error messages should go to a certified RATIONAL Service Partner, and the steam, gas, ignition, and rpm-detection circuits need model-specific test equipment and knowledge of the control architecture. Anything involving gas supply, ignition, or high-voltage steam heating is a licensed-technician job. Have the unit serial number ready before you call.

## Frequently asked questions

### Is E01 a standard Rational iCombi Classic fault code?

The iCombi Classic displays faults as Service (E) messages (for example Service (E) 10, 20.1, 25) rather than a simple E01. An E01-style display usually means the unit stopped on a calibration or self-test step, where the number identifies the step that failed. Note the exact wording on screen and the step it stopped on, then match it to the Service code list.

### Why does my iCombi calibration or self-test keep failing?

A common reason is that the unit is still too hot when the routine starts. Let it cool fully, switch the unit off and on, then re-run the test. A loose or failed differential pressure sensor and a missing or dry drain odor trap are the next things to check.

### What causes steam generator and CleanJet water errors on the iCombi Classic?

Scale is the usual culprit on hard-water sites. Codes tied to the steam generator, level electrode, water volume/CDS measurement, and CleanJet (for example Service (E) 11, 12, 13, 25, 110, 120) often trace back to a calcified level electrode, a starved water inlet, or a worn SC/waste-water pump. Confirm the water is on and at pressure first, then have the level electrode and pump inspected and descaled.

### Can I fix an iCombi Classic fault code myself?

You can safely handle the basics: verify water and gas supply, clear the drain, clean the air filter, let the unit cool, and power-cycle it. Rational's official guidance is that all error messages should go to a certified RATIONAL Service Partner, and steam, gas, ignition, and fan rpm circuits need model-specific test equipment. Gas-model faults must be handled by a qualified gas technician.

### What information should I have ready before calling for service?

Have the exact Service (E) code and on-screen wording, the unit serial number and software version (available in the unit data menu), and whether the fault appeared during cooking, a self-test/calibration, or a CleanJet cycle. That lets the technician arrive with the right probe, pump, valve, or board and avoids unnecessary part swaps.

## Related guides

- [Hobart Dishwasher Error Codes](/posts/hobart-dishwasher-error-codes/)
- [Frymaster Fryer Error Codes](/posts/frymaster-fryer-error-codes/)
- [Manitowoc Indigo Nxt Complete Guide](/posts/manitowoc-indigo-nxt-complete-guide/)
- [Rational Combi Oven Error Codes](/posts/rational-combi-oven-error-codes/)
