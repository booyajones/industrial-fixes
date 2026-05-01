---
title: "Danfoss FC301 Fault AL 14 — Ground Fault Causes & Fix"
description: "What Danfoss FC301 alarm AL 14 means, why ground fault trips the drive, and how to fix it step by step."
pubDatetime: 2026-04-22T15:00:00Z
modDatetime: 2026-04-22T15:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - danfoss
---

## Danfoss FC301 Fault AL 14 — What It Means

Alarm 14 (Ground Fault) on a Danfoss FC301 drive means the drive has detected an abnormal current flow to earth ground on the motor output side. The FC301 is Danfoss's HVAC-optimized VLT drive, designed for pumps and fans in building automation systems. AL 14 fires when the vector sum of the three output phase currents is not zero — indicating current is leaking to ground through insulation breakdown, a wiring fault, or moisture ingress. The drive trips immediately to protect both equipment and personnel. This is the same alarm code as AL 14 on the FC302 and FC51 drives.

[Jump to Fix](#fix)

## Common Causes

- **Motor insulation failure** — Deteriorated motor winding insulation allows current to leak to the motor frame and ground. This is more common on older motors or motors exposed to moisture, thermal cycling, or corrosive environments.
- **Damaged output cable** — A cable with abraded insulation touching conduit or the machine frame creates a direct ground fault path. Cables routed through tight conduit bends are vulnerable.
- **Moisture in the motor terminal box** — Water ingress into the motor terminal box causes a temporary ground fault that may clear when dried but indicates a seal has failed.
- **EMC filter leakage current** — The FC301's built-in EMC filter (RFI filter) passes a small leakage current to ground by design. If the ground fault detection threshold is set very low, this can occasionally trigger AL 14. Use parameter 14-07 to adjust the ground fault detection level.

## Step-by-Step Fix {#fix}

1. **Cut power and isolate** — Disconnect the FC301 at the supply breaker and allow 4 minutes for DC bus discharge.
2. **Disconnect the motor cable at the drive** — Remove the U, V, W terminals at the drive output. Measure insulation resistance from each phase to ground using a 500 VDC megohmmeter. Values below 1 MΩ indicate a cable or motor insulation problem.
3. **Disconnect the motor cable at the motor** — Repeat the megohm test from the motor terminals. If the cable tests good but the motor tests bad, the insulation failure is in the motor.
4. **Inspect the motor terminal box** — Open the motor terminal box and check for moisture, condensation, or visible carbon tracking. Dry with compressed air and treat with a moisture-displacing spray if wet.
5. **Inspect the cable route** — Look for chafing, sharp bends, or conduit abrasion along the cable run. Replace any section of damaged cable.
6. **Check parameter 14-07 (Ground Fault Detection Level)** — If the motor and cable test clean, verify that EMC filter leakage is not causing false trips. Adjusting 14-07 from the default can filter legitimate leakage current.
7. **Reset and test** — Restore power, reset AL 14, and ramp the drive to full speed while monitoring output current balance.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor output cable | [Amazon](https://www.amazon.com/s?k=Motor+output+cable&tag=errorcodefixes-20) \| Replace fully if insulation damage is found |
| Motor (rewind or replace) | [Amazon](https://www.amazon.com/s?k=Motor+%28rewind+or+replace%29&tag=errorcodefixes-20) \| Required if winding insulation tests below 1 MΩ |
## When to Call a Pro

Megohmmeter testing and motor insulation diagnosis should be performed by a qualified electrician. A motor with insulation failure below 1 MΩ is a safety hazard and must not be operated until repaired or replaced.
