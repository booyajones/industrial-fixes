---
title: "Johnson Controls HVAC VFD Fault Codes — Common Faults and Fixes"
description: "Guide to Johnson Controls variable frequency drive fault codes used in HVAC systems, what each fault means, and how to fix the most common problems."
pubDatetime: 2026-04-22T14:00:00Z
modDatetime: 2026-04-22T14:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - johnson-controls
---

## Johnson Controls HVAC VFD Fault Codes — What They Mean

Johnson Controls uses variable frequency drives from multiple OEM manufacturers (primarily York-branded drives and rebranded Hitachi and other OEM drives) in air handling units, cooling towers, and chiller plant auxiliaries. The fault codes displayed on these drives follow the conventions of the underlying OEM but are sometimes relabeled with Johnson Controls part numbers. The most common JCI HVAC VFDs are found in Built Environment (BE) air handling units and central plant equipment managed by Metasys BAS. The faults below cover the most frequently encountered issues on field-installed JCI VFDs.

[Jump to Fix](#fix)

## Most Common JCI VFD Fault Codes

| Code | Meaning |
|------|---------|
| OC / OCA | Overcurrent — motor drawing excess amps |
| OV | Overvoltage — DC bus voltage too high |
| UV | Undervoltage — DC bus voltage too low |
| OH | Overheat — drive heat sink temperature exceeded |
| GF | Ground fault — current path to ground detected |
| OL / OLT | Motor overload — thermal model exceeded |
| LF | Input phase loss — single-phasing on supply |
| EF | External fault — remote fault input activated |

## Common Causes

- **OC (Overcurrent)** — Motor winding short, mechanical overload on the fan or pump, excessive acceleration ramp (too fast for the load inertia), or a failing output IGBT in the drive. Check the motor insulation and mechanical load before assuming the drive is faulty.
- **OV (Overvoltage)** — Regenerative braking with no braking resistor (deceleration too fast for a high-inertia fan), incoming utility voltage spike, or a drive deceleration ramp set too aggressively. Lengthen the deceleration ramp or add a dynamic braking resistor.
- **OH (Overheat)** — Drive cabinet ventilation is blocked, cooling fan inside the drive has failed, ambient temperature exceeds drive rating, or drive is oversized for a very lightly loaded application (light-load operation reduces internal cooling). Clean cabinet filters and verify cooling fan operation.
- **GF (Ground Fault)** — Deteriorated motor winding insulation, water intrusion into motor terminal box, or damaged motor cable. Megger the motor and cable with the drive disconnected.
- **LF (Phase Loss)** — One of the three incoming supply phases has been lost or is significantly unbalanced. Check all three supply voltages at the drive input terminals. Phase loss on HVAC VFDs is often caused by a blown input fuse or a loose connection in the panel.
- **EF (External Fault)** — A remote interlock (fire/smoke damper, differential pressure switch, or Metasys BAS point) has de-energized the drive's enable input. Check the BAS and field interlock status before assuming the drive is faulty.

## Step-by-Step Fix {#fix}

1. **Record the fault and check drive fault history** — Most JCI VFDs have a fault log accessible from the keypad. Review the last 3–5 faults and their timestamps. A pattern (e.g., OH faults only in summer) points to an environmental cause.
2. **For OC faults** — Disconnect the motor from the drive. Run the drive in no-load test mode (if available) — if OC persists with no motor connected, the drive IGBT output stage is failing. If no-load test is clean, megger the motor (500V DC megger; expect >100MΩ phase-to-ground on a healthy motor).
3. **For OH faults** — Inspect the drive's cooling fans — all fans inside the drive enclosure must be spinning. Clean the heat sink fins with compressed air. Measure ambient temperature at the drive; it should not exceed the drive's rated ambient (usually 40–50°C/104–122°F).
4. **For LF faults** — Measure all three incoming supply voltages at the drive input with the drive powered. Phase imbalance >3% or a missing phase indicates a supply problem. Check the input fuses (often inside the drive at the L1/L2/L3 terminals).
5. **For EF faults** — Navigate to the drive's I/O status screen and identify which digital input is de-energized. Trace that input back to the field device or Metasys point that controls it and resolve the interlock condition.
6. **Reset and test** — After repairs, reset the fault from the keypad (usually STOP + RESET or a dedicated RESET key). Run the drive in manual mode through a slow ramp to confirm no fault recurrence before returning to automatic BAS control.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Drive cooling fan (internal) | [Amazon](https://www.amazon.com/s?k=Drive+cooling+fan+%28internal%29&tag=errorcodefixes-20) \| Match voltage and airflow to original; JCI part number cross-references to Hitachi or other OEM |
| Input fuse set | [Amazon](https://www.amazon.com/s?k=Input+fuse+set&tag=errorcodefixes-20) \| Match voltage and amp rating from drive nameplate |
| Dynamic braking resistor | [Amazon](https://www.amazon.com/s?k=Dynamic+braking+resistor&tag=errorcodefixes-20) \| For OV faults on high-inertia fans without adequate deceleration ramp |
| Replacement VFD | [Amazon](https://www.amazon.com/s?k=Replacement+VFD&tag=errorcodefixes-20) \| For output IGBT failure confirmed by no-load OC test |
## When to Call a Pro

Ground fault diagnosis (GF code) requires a megger (insulation resistance tester) and comfort working with motor circuits. Drive output IGBT replacement requires VFD-specific training — most HVAC contractors replace the entire drive rather than attempting board-level repair. Johnson Controls has a building products service line and authorized contractors for Metasys-integrated equipment.

## Related Articles

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS310 Fault 3130 — Causes & Fix](/posts/abb-acs310-fault-3130/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)
