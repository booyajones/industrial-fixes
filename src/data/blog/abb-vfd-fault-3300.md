---
title: "ABB VFD Fault 3300 — Causes & Fix"
description: "What ABB VFD fault code 3300 means, why earth leakage trips the drive, and how to fix it."
pubDatetime: 2026-04-22T10:00:00Z
modDatetime: 2026-04-22T10:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - abb
money_part: "Motor cable (XLPE, screened)"
---

## ABB VFD Fault 3300 — What It Means

Fault 3300 on an ABB ACS series drive (ACS580, ACS880, ACS310, etc.) indicates an earth fault — the drive's output current monitoring detected an unbalanced current to ground. ABB drives measure the vector sum of all output phase currents; in a healthy three-phase system, these sum to zero. When current leaks to ground through damaged motor winding insulation or cable insulation, the sum is non-zero and the drive trips on earth fault 3300 to prevent IGBT damage and operator hazard.

[Jump to Fix](#fix)

## Common Causes

- **Degraded motor winding insulation** — Moisture ingress, thermal cycling, or contamination in the motor causes insulation resistance to drop, allowing current to flow to the motor frame (earth).
- **Damaged motor cable insulation** — A cable pinched by conduit, cut by equipment, or degraded from heat or UV exposure allows phase conductors to contact ground.
- **Wet or contaminated motor terminal box** — Water pooling in the motor terminal box creates a conductive path from winding terminals to the grounded motor frame.
- **Drive IGBT or output filter failure** — Rarely, a failed IGBT or output EMC filter capacitor in the drive itself causes a false earth fault detection.

## Step-by-Step Fix {#fix}

1. **Isolate the motor and cable** — Disconnect the motor cable at the drive output terminals (U2, V2, W2) and at the motor terminal box. This separates the motor from the cable for individual testing.
2. **Test motor insulation resistance** — Use a 500V or 1000V insulation resistance (IR) tester (Megger). Measure between each phase (U, V, W) and the motor frame (PE). Healthy motors read >100 MΩ at 500VDC. Values below 1 MΩ indicate degraded insulation.
3. **Test cable insulation resistance** — With the cable disconnected at both ends, test each conductor to the cable shield/armor. Values below 10 MΩ indicate damaged cable insulation — replace the cable.
4. **Inspect the motor terminal box** — Open the terminal box and look for water, corrosion, or carbon tracks between terminals and the box body. Clean, dry, and reseal.
5. **Reconnect and test** — After confirming cable and motor insulation resistance is acceptable, reconnect the cable and run the drive. If fault 3300 clears and does not return, the repair was successful.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor cable (XLPE, screened) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-vfd-fault-3300&k=Motor+cable+%28XLPE%2C+screened%29&tag=errorcodefixes-20) \| Use VFD-rated cable with continuous shield; correct cross-section for ampacity |
| Motor (rewind or replacement) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-vfd-fault-3300&k=Motor+%28rewind+or+replacement%29&tag=errorcodefixes-20) \| If insulation resistance is below 1 MΩ at 500VDC |
| Cable glands and conduit fittings | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-vfd-fault-3300&k=Cable+glands+and+conduit+fittings&tag=errorcodefixes-20) \| Replace if water entry point identified |
## When to Call a Pro

Motor rewinding or replacement is specialized work. If the insulation test confirms a failed motor, coordinate motor removal with a qualified electrician or motor shop. Working inside drive output circuits requires lockout/tagout procedures.

## Related Articles

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS310 Fault 3130 — Causes & Fix](/posts/abb-acs310-fault-3130/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [PowerFlex vs SINAMICS VFD compared](/posts/powerflex-vs-sinamics-vfd/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [PowerFlex F004 undervoltage fix](/posts/allen-bradley-powerflex-f004-fault/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [PowerFlex F012 hardware overcurrent](/posts/allen-bradley-powerflex-f012-fault/)

## See Also

- [ABB ACS880 Complete Fault Code Guide — All Faults and Fixes](/posts/abb-acs880-complete-guide/)
- [ABB VFD Fault 2310 — Causes & Fix](/posts/abb-vfd-fault-2310/)
- [ABB ACS550 AF10 Fault — Causes & Fix](/posts/abb-acs550-af10-heatsink/)
- [ABB VFD Fault 0001 Overcurrent — Causes & Fix](/posts/abb-vfd-fault-0001-overcurrent/)
