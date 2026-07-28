---
title: "Siemens Micromaster F0021 Fault - Causes & Fix"
description: "F0021 on Siemens Micromaster 440 drives means earth fault: current is leaking to ground. Check motor cable insulation and windings first."
pubDatetime: 2026-06-02T10:32:43Z
modDatetime: 2026-06-02T10:32:43Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Motor cable (shielded VFD-rated)"
most_likely_cause: "Damaged motor cable insulation"
---

## What this code means
F0021 is an earth fault code on Siemens Micromaster 440 variable frequency drives. The drive has detected that the sum of the phase currents is greater than 5% of the inverter's nominal current, which means current is leaking to ground somewhere in the motor circuit. This fault applies only to inverters with three current sensors, specifically frame sizes D to F and FX/GX.

The fault indicates an imbalance consistent with output-to-earth leakage. It is not a simple overload. The drive is seeing evidence that current is flowing to ground through damaged insulation, a grounded motor winding, or contamination in the cable or motor. The fault history is stored in parameter P0947.

## Common Causes

- **Damaged motor cable insulation** The motor cable jacket or insulation has been nicked, crushed, or worn through, allowing current to leak to ground or a conduit.
- **Motor winding insulation breakdown** One or more motor windings have broken down internally and are conducting to the motor frame or earth.
- **Moisture or contamination in motor or cable** Water, oil, dust, or other conductive contamination creates a leakage path between the windings or cable conductors and ground.
- **Poor or corroded grounding connections** Loose, corroded, or improperly sized ground conductors can contribute to nuisance earth-fault behavior or measurement errors.
- **Drive output stage fault** If the fault persists with the motor and all field wiring disconnected, the inverter's output stage or current sensors may be defective.

## Step-by-Step Fix {#fix}

1. **Lock out and tag out** all power to the drive and motor before beginning any diagnostics or repairs.
2. **Inspect the motor cable** along its entire run for physical damage, pinch points, sharp edges, or signs of insulation wear or contamination.
3. **Disconnect the motor from the drive** at the output terminals (U, V, W) and reset the fault to see if it clears when the motor and field wiring are isolated.
4. **Test motor winding insulation to ground** using a megohmmeter (megger) on each motor lead to verify that insulation resistance is acceptable and the motor is not shorted to frame.
5. **Check continuity from drive output terminals to ground** with all external wiring disconnected to confirm there is no internal short in the inverter output stage.
6. **Inspect and re-terminate all grounding points** at the motor, cable, and drive to remove corrosion, tighten connections, and verify proper ground continuity.
7. **If the fault persists with motor and cables disconnected**, the drive output section is likely defective and the inverter should be serviced or replaced per Siemens guidance.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor cable (shielded VFD-rated) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-vfd-f0021-fault-code&k=Motor+cable+%28shielded+VFD-rated%29&tag=errorcodefixes-20) \| Replace if insulation is damaged or worn through to ground. |
| Three-phase AC motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-vfd-f0021-fault-code&k=Three-phase+AC+motor&tag=errorcodefixes-20) \| Replace if winding insulation has broken down and megohmeter test fails. |
| Siemens Micromaster 440 drive unit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-vfd-f0021-fault-code&k=Siemens+Micromaster+440+drive+unit&tag=errorcodefixes-20) \| Replace or send for repair if fault persists with all external wiring disconnected. |

## When to Call a Pro

Call a qualified industrial electrician or VFD technician if you are not trained in lockout/tagout procedures, high-voltage insulation testing, or variable frequency drive diagnostics. If megohmmeter testing and cable inspection do not locate the fault, or if the fault remains after disconnecting all external wiring, the drive output stage likely requires factory service or replacement. Siemens recommends consulting the full fault history in parameter P0947 and verifying frame size and sensor configuration before ordering parts.
