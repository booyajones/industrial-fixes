---
title: "ABB ACS580 A2B3 Fault Code - Causes & Fix"
description: "ABB ACS580 A2B3 means earth leakage detected. Learn the causes, diagnostic steps, and parts to fix load unbalance faults."
pubDatetime: 2026-05-27T10:32:13Z
modDatetime: 2026-05-27T10:32:13Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - abb
money_part: "Motor cable (shielded VFD-rated)"
---

## ABB ACS580 A2B3 Fault Code — What It Means

The A2B3 fault code on an ABB ACS580 drive indicates earth leakage. The drive has detected load unbalance, typically caused by an earth fault in the motor or motor cable. This is a diagnostic fault in ABB's fault list that points to a current path to ground somewhere in the motor circuit.

ABB specifically identifies power factor correction capacitors or surge absorbers in the motor cable as common triggers, along with insulation breakdown in the motor windings or cable. The drive is protecting itself and the motor from continued operation with a ground fault present.

[Jump to Fix](#fix)

## Common Causes

- **Earth fault in the motor cable** Damaged, crushed, or aged cable insulation allows current to leak to ground, especially at terminations, sharp bends, or areas exposed to moisture.
- **Earth fault in the motor windings** Insulation breakdown inside the motor or at the terminal box creates a path to the motor frame and triggers the earth leakage detection.
- **Power factor correction capacitors in the motor circuit** Capacitors connected in the motor cable path create unbalanced currents that the drive interprets as earth leakage.
- **Surge absorbers on the motor cable** Surge suppression devices installed between the drive and motor can cause load unbalance and false earth fault detection.
- **Loose or corroded motor terminal connections** Poor connections at the motor terminal box or cable lugs can create intermittent ground paths or unbalanced current flow.
- **Water ingress in the motor or cable** Moisture in conduit, junction boxes, or the motor itself provides a conductive path to ground and degrades insulation resistance.

## Step-by-Step Fix {#fix}

1. **Disconnect power** and lock out the drive at the upstream disconnect, then verify zero voltage at the drive output terminals and motor connections.
2. **Remove or isolate any power factor correction capacitors or surge absorbers** from the motor cable circuit, as ABB identifies these as common triggers for A2B3 faults.
3. **Inspect the motor cable** along its entire run for physical damage, crushed insulation, rubbing against sharp edges, loose cable glands, water in conduit or junction boxes, and correct routing away from heat sources.
4. **Disconnect the motor cable at both the drive output and motor terminals**, then use a megohmmeter to test insulation resistance between each phase conductor and ground, and between phases, following your site's insulation test procedure.
5. **Inspect the motor terminal box** for moisture, corrosion, loose connections, damaged insulation, and signs of arcing or tracking to the motor frame.
6. **Test the motor windings** for insulation resistance to ground with the cable disconnected, comparing results to acceptable values for your motor voltage class and consulting the motor nameplate data.
7. **Reconnect the system and test run** the drive only after all insulation tests pass and any damaged cable or faulty components have been replaced, then monitor for fault recurrence. If A2B3 persists after these checks, contact ABB service support or your local ABB representative for drive-level diagnostics.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor cable (shielded VFD-rated) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-a2b3-fault-code&k=Motor+cable+%28shielded+VFD-rated%29&tag=errorcodefixes-20) \| Replace if insulation resistance tests fail or physical damage is found along the cable run. |
| Three-phase AC motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-a2b3-fault-code&k=Three-phase+AC+motor&tag=errorcodefixes-20) \| Required if winding insulation to ground tests below acceptable limits and cannot be dried or repaired. |
| Motor terminal box gasket and cable glands | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-a2b3-fault-code&k=Motor+terminal+box+gasket+and+cable+glands&tag=errorcodefixes-20) \| Needed when water ingress or poor sealing is found during inspection of the motor termination area. |

## When to Call a Pro

Call a qualified electrician or ABB service technician if insulation resistance tests on the motor and cable all pass but the A2B3 fault continues to appear, or if you lack a megohmmeter and the training to safely perform insulation testing on VFD motor circuits. Also call a professional if the fault appeared after a recent installation or drive commissioning, as parameter settings or grounding configuration may need expert review. ABB's official guidance is to escalate to your local ABB representative when external motor-circuit causes have been ruled out.

## See Also

- [ABB ACS580 A2A1 - Causes & Fix](/posts/abb-acs580-a2a1-fault-code/)
- [ABB VFD Fault 5010 — Causes & Fix](/posts/abb-vfd-fault-5010/)
- [ABB VFD Fault 4110 — Causes & Fix](/posts/abb-vfd-fault-4110/)
- [ABB ACS580 FA81 Fault - Safe Torque Off 1 Active](/posts/abb-acs580-fa81-fault-code/)
