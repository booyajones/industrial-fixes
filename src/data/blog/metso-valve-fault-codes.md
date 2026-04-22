---
title: "Metso Automation Valve Fault Codes — Neles ND9000 / NDX Guide"
description: "Metso Automation (Neles) valve positioner fault codes for ND9000 and NDX series: alarms, diagnostics, and troubleshooting steps for industrial control valves."
pubDatetime: 2026-04-22T21:00:00Z
modDatetime: 2026-04-22T21:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - valve
  - metso
  - neles
  - positioner
  - industrial
---

## Metso Valve Positioner Fault Codes — Quick Reference

Metso Automation (now Neles) ND9000 and NDX intelligent valve controllers report faults over HART, Foundation Fieldbus, or Profibus DP. Alarms are classified as process (F), maintenance (M), or advisory (A).

| [Fault Code](https://www.amazon.com/s?k=Fault%20Code&tag=errorcodefixe-20) | Meaning | Quick Fix | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ----------- |---------|-----------|
| F01 — Position Sensor | [Position sensor signal out of range](https://www.amazon.com/s?k=Position%20sensor%20signal%20out%20of%20range&tag=errorcodefixe-20) | Check sensor and harness |
| [F02 — Pressure Sensor](https://www.amazon.com/s?k=F02%20%E2%80%94%20Pressure%20Sensor&tag=errorcodefixe-20) | Internal pressure sensor fault | Replace instrument | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | F03 — Drive Current | Output current high or low | [Check I/P converter and supply](https://www.amazon.com/s?k=Check%20I%2FP%20converter%20and%20supply&tag=errorcodefixe-20) |  | F04 — Supply Pressure | [Supply pressure below minimum](https://www.amazon.com/s?k=Supply%20pressure%20below%20minimum&tag=errorcodefixe-20) | Check supply regulator |
| [F05 — Valve Deviation](https://www.amazon.com/s?k=F05%20%E2%80%94%20Valve%20Deviation&tag=errorcodefixe-20) | Valve not at setpoint | Check actuator and process | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | M01 — Travel Accumulation | Travel limit reached | [Schedule packing and seat inspection](https://www.amazon.com/s?k=Schedule%20packing%20and%20seat%20inspection&tag=errorcodefixe-20) |  | M02 — Cycle Counter | [Cycle limit reached](https://www.amazon.com/s?k=Cycle%20limit%20reached&tag=errorcodefixe-20) | Inspect valve internals |
| [A01 — Temperature](https://www.amazon.com/s?k=A01%20%E2%80%94%20Temperature&tag=errorcodefixe-20) | Internal temperature out of range | Check ambient temperature | [## Most Common Faults

### F01 — Position Sensor Fault
The Hall-effect or potentiometer position sensor signal is out of calibrated range. Check the sensor connector for corrosion or vibration damage. If the sensor is mechanically misaligned after maintenance, re-run the auto-calibration routine in FieldCare or Metso DNA.

### F05 — Valve Deviation
The positioner commanded the valve to move but measured travel does not match setpoint within the tolerance window. This points to high friction from tight packing, actuator problems, or excessive process differential pressure. Run the partial stroke test to observe response characteristics.

### F04 — Supply Pressure Low
Metso positioners require clean, dry instrument air typically at 35–100 psi. Confirm the supply pressure regulator is upstream and set correctly. Check supply tubing for leaks.

## Diagnostic Features

- **Auto-calibration** — learns travel limits and positions
- **Partial stroke testing** — safety valve verification without full closure
- **Step response** — measures valve response speed and gain
- **Torque profile** — identifies packing friction and seat load

## Parts Often Needed](https://www.amazon.com/s?k=%23%23%20Most%20Common%20Faults%0A%0A%23%23%23%20F01%20%E2%80%94%20Position%20Sensor%20Fault%0AThe%20Hall-effect%20or%20potentiometer%20position%20sensor%20signal%20is%20out%20of%20calibrated%20range.%20Check%20the%20sensor%20connector%20for%20corrosion%20or%20vibration%20damage.%20If%20the%20sensor%20is%20mechanically%20misaligned%20after%20maintenance%2C%20re-run%20the%20auto-calibration%20routine%20in%20FieldCare%20or%20Metso%20DNA.%0A%0A%23%23%23%20F05%20%E2%80%94%20Valve%20Deviation%0AThe%20positioner%20commanded%20the%20valve%20to%20move%20but%20measured%20travel%20does%20not%20match%20setpoint%20within%20the%20tolerance%20window.%20This%20points%20to%20high%20friction%20from%20tight%20packing%2C%20actuator%20problems%2C%20or%20excessive%20process%20differential%20pressure.%20Run%20the%20partial%20stroke%20test%20to%20observe%20response%20characteristics.%0A%0A%23%23%23%20F04%20%E2%80%94%20Supply%20Pressure%20Low%0AMetso%20positioners%20require%20clean%2C%20dry%20instrument%20air%20typically%20at%2035%E2%80%93100%20psi.%20Confirm%20the%20supply%20pressure%20regulator%20is%20upstream%20and%20set%20correctly.%20Check%20supply%20tubing%20for%20leaks.%0A%0A%23%23%20Diagnostic%20Features%0A%0A-%20**Auto-calibration**%20%E2%80%94%20learns%20travel%20limits%20and%20positions%0A-%20**Partial%20stroke%20testing**%20%E2%80%94%20safety%20valve%20verification%20without%20full%20closure%0A-%20**Step%20response**%20%E2%80%94%20measures%20valve%20response%20speed%20and%20gain%0A-%20**Torque%20profile**%20%E2%80%94%20identifies%20packing%20friction%20and%20seat%20load%0A%0A%23%23%20Parts%20Often%20Needed&tag=errorcodefixe-20) | Part | Notes | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------ |-------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Position sensor module | Replaces if F01 persists | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Supply pressure regulator | Replaces on F04 faults | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | I/P converter | Replaces on F03 faults | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Packing set | Replace on high friction diagnostics |

## Jump to Fix

- **F01 sensor fault** → Check connector → Re-calibrate → Replace sensor
- **F05 deviation** → Run partial stroke → Check actuator → Inspect packing
- **F04 supply** → Verify supply pressure → Check regulator

## When to Call a Pro
Metso/Neles positioners require FieldCare or Metso DNA for full diagnostic access. Authorized service partners provide calibration and on-site repair.
