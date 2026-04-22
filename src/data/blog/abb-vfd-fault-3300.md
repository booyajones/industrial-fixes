---
title: "ABB VFD Fault 3300 — Causes & Fix"
description: "What ABB VFD fault code 3300 means, why earth leakage trips the drive, and how to fix it."
pubDatetime: 2026-04-22T10:00:00Z
modDatetime: 2026-04-22T10:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - abb
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
| Motor cable (XLPE, screened) | Use VFD-rated cable with continuous shield; correct cross-section for ampacity |
| Motor (rewind or replacement) | If insulation resistance is below 1 MΩ at 500VDC |
| Cable glands and conduit fittings | Replace if water entry point identified |

## When to Call a Pro

Motor rewinding or replacement is specialized work. If the insulation test confirms a failed motor, coordinate motor removal with a qualified electrician or motor shop. Working inside drive output circuits requires lockout/tagout procedures.
