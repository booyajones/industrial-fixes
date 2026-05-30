---
title: "ABB ACS580 A2B4 Fault Code - Causes & Fix"
description: "ABB ACS580 A2B4 means output-stage short circuit in motor cable or motor. Step-by-step troubleshooting and repair guide."
pubDatetime: 2026-05-27T10:32:43Z
modDatetime: 2026-05-27T10:32:43Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - abb
---

## ABB ACS580 A2B4 Fault Code — What It Means

The A2B4 fault on your ABB ACS580 drive indicates a short-circuit condition on the output side, typically in the motor cable or the motor itself. The drive detects this problem and trips to protect the IGBT power transistors in the output stage from damage.

ABB flags this fault because a sustained short circuit can stress or destroy the drive's output module. The short may be between motor cable phases, from a phase to ground, inside the motor windings, or caused by wiring errors at the motor terminals.

[Jump to Fix](#fix)

## Common Causes

- **Shorted motor cable** Damaged insulation between phase conductors or a phase shorted to ground in the cable run.
- **Motor winding failure** Internal insulation breakdown or a short circuit inside the motor itself.
- **Wiring errors** Incorrect phasing, reversed connections, or delta/star configuration mistakes at the motor terminals.
- **Earth fault or insulation breakdown** Low insulation resistance in the motor or cable allowing current to leak to ground.
- **Damaged terminations or moisture ingress** Crushed conduit, water in junction boxes, or failed cable lugs creating an unintended short.

## Step-by-Step Fix {#fix}

1. **Power down and lock out** the drive before any inspection or testing to prevent shock and further damage.
2. **Inspect the motor cable and terminals** for visible damage, crushed insulation, burn marks, loose strands, moisture, or contamination at both the drive and motor ends.
3. **Verify phasing and motor connection type** at the motor junction box and drive output terminals to rule out wiring errors or incorrect delta/star configuration.
4. **Measure insulation resistance** of the motor and motor cable using a megohmmeter to check for earth faults or insulation breakdown.
5. **Disconnect the motor cable from the drive output terminals** and attempt to reset the fault to isolate whether the problem is in the motor/cable or the drive itself.
6. **If the fault clears with the motor disconnected**, replace or repair the motor cable, motor, or terminations as needed and retest insulation resistance before reconnecting.
7. **If the fault persists with the motor disconnected** or the drive output stage shows visible damage, contact ABB service or a qualified technician to inspect and possibly replace the IGBT power module.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor cable assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-a2b4-fault-code&k=Motor+cable+assembly&tag=errorcodefixes-20) \| Replace if insulation is damaged or shorted between phases or to ground. |
| Motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-a2b4-fault-code&k=Motor&tag=errorcodefixes-20) \| Replace or rewind if internal winding insulation has failed or shows a short circuit. |
| Cable termination lugs and connectors | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-a2b4-fault-code&k=Cable+termination+lugs+and+connectors&tag=errorcodefixes-20) \| Replace damaged or poorly crimped terminals that may cause intermittent shorts. |
| IGBT power module or drive output section | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-a2b4-fault-code&k=IGBT+power+module+or+drive+output+section&tag=errorcodefixes-20) \| Contact ABB for replacement if the drive output stage is damaged after a severe short. |

## When to Call a Pro

Call a qualified electrician or ABB-authorized service technician if insulation testing and visual inspection do not reveal an obvious motor or cable fault, if the fault persists after disconnecting the motor, or if you find visible damage to the drive's output stage. Professional help is also recommended if you are not trained in high-voltage isolation testing or VFD output-module replacement, as misdiagnosis can lead to repeat failures or safety hazards.

## See Also

- [ABB VFD Fault 5010 — Causes & Fix](/posts/abb-vfd-fault-5010/)
- [ABB ACS580 B1 Fault Code - Causes & Fix](/posts/abb-acs580-b1-fault-code/)
- [ABB ACS580 A2B3 Fault Code - Causes & Fix](/posts/abb-acs580-a2b3-fault-code/)
- [ABB VFD Fault 0001 Overcurrent — Causes & Fix](/posts/abb-vfd-fault-0001-overcurrent/)
