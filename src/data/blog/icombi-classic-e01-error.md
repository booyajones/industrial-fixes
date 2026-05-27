---
title: "Rational iCombi Classic E01 - Causes & Fix"
description: "E01 on the Rational iCombi Classic signals a calibration step failure. Learn common causes and the repair steps technicians follow."
pubDatetime: 2026-05-25T00:00:39Z
modDatetime: 2026-05-25T00:00:39Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - appliance
  - rational
---

## Rational iCombi Classic E01 — What It Means

E01 on the Rational iCombi Classic is not a single fixed fault. It appears in the calibration error family, where the number identifies the calibration step that failed rather than pointing to one broken part. The exact meaning depends on which self-test or manual calibration step the unit reached when the fault occurred.

Common underlying problems include the unit being too hot during calibration (sensors above 40°C), a faulty or loose differential pressure sensor, fan motor rpm detection faults, and steam heating failures. Because the number is tied to a specific step, you need to verify the unit state and work through the relevant circuits in order.

[Jump to Fix](#fix)

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
