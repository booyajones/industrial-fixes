---
title: "Danfoss FC302 Alarm 14 - Causes & Fix"
description: "Danfoss FC302 Alarm 14 means earth (ground) fault. The drive detected current leakage from an output phase to ground in the motor or cable."
pubDatetime: 2026-05-29T09:40:07Z
modDatetime: 2026-05-29T09:40:07Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Shielded VFD-rated motor cable"
most_likely_cause: "Damaged motor cable insulation"
---

## Danfoss FC302 Alarm 14 — What It Means

Alarm 14 on the Danfoss VLT FC302 is an earth (ground) fault. The drive compares current leaving the inverter with current returning from the motor. If the difference is too large, it trips to protect the system. Danfoss service documentation describes this as a short to ground in the motor or motor wiring.

The fault indicates current leakage from an output phase to ground, either in the motor cable insulation or in the motor windings themselves. This is an output-side electrical insulation problem, not a drive input or supply issue.

[Jump to Fix](#fix)

## Common Causes

- **Damaged motor cable insulation** Cable insulation breakdown from physical wear, heat, or contamination creates a leakage path from phase to ground.
- **Motor winding insulation failure** Moisture, thermal aging, or contamination in the motor windings breaks down insulation and allows current to leak to the frame.
- **Loose or contaminated connections** Poor terminations in the motor junction box or drive output terminals create flashover paths to ground.
- **Drive current sensor offset or internal fault** If the alarm persists with all motor and output leads disconnected, the drive's current sensors or output power section may be faulty.

## Step-by-Step Fix {#fix}

1. **Remove power and inspect** all connections at the drive output terminals, motor cable ends, and motor junction box for loose, damaged, or contaminated terminations.
2. **Disconnect the motor leads** from the drive output terminals and reset the fault to isolate whether the problem is in the motor/cable or inside the drive.
3. **Megger test the motor cable and motor windings** to ground to locate insulation breakdown (field practice suggests below 2 MΩ indicates insulation problems, though manufacturer threshold is not published).
4. **Check for current sensor offset** by performing a manual initialization or complete AMA (Automatic Motor Adaptation) if the alarm appeared after a power-card change or component work.
5. **Replace the motor cable** if the insulation test fails or visible damage is found in the cable jacket or conductor insulation.
6. **Replace the motor** if winding-to-ground insulation is defective and cannot be repaired or dried out.
7. **Service or replace the drive** if the fault persists with all output wiring removed, indicating an internal current sensor or output power section fault.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Shielded VFD-rated motor cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-14-fault-code&k=Shielded+VFD-rated+motor+cable&tag=errorcodefixes-20) \| Use if insulation test fails or visible cable damage is found. |
| Replacement three-phase motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-14-fault-code&k=Replacement+three-phase+motor&tag=errorcodefixes-20) \| Required if motor winding insulation is defective and cannot be restored. |
| Danfoss FC302 current sensor or power card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-14-fault-code&k=Danfoss+FC302+current+sensor+or+power+card&tag=errorcodefixes-20) \| Needed if fault remains with motor and cable disconnected, indicating internal drive failure. |

## When to Call a Pro

Call a qualified technician if you are not trained in high-voltage isolation testing or VFD diagnostics. Megger testing requires skill to avoid further damage to the motor or drive. If the fault persists after disconnecting the motor and all output wiring, the drive has an internal problem that requires factory-trained service or component-level repair. If the motor winding insulation is defective, a motor shop should evaluate whether rewinding is cost-effective or if replacement is required.

## See Also

- [Danfoss RX Controller Fault Codes — Troubleshooting Guide](/posts/danfoss-rx-controller-fault/)
- [Danfoss FC302 Alarm AL 29 — Causes & Fix](/posts/danfoss-fc302-fault-al-29/)
- [Danfoss VFD Fault UL — Causes & Fix](/posts/danfoss-vfd-fault-ul/)
- [Danfoss FC-302 Alarm 12 — Overcurrent Fix](/posts/danfoss-fc302-alarm-12/)
