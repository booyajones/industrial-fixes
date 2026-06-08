---
title: "Yaskawa GA800 E45 Fault - Causes & Fix"
description: "E45 signals input phase loss or severe voltage instability on the GA800 VFD. Most often it's a blown input fuse or loose power terminal."
pubDatetime: 2026-06-06T11:33:51Z
modDatetime: 2026-06-06T11:33:51Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
most_likely_cause: "Blown input fuse or tripped upstream breaker"
likelihood: "the most common field cause"
diy_or_pro: "pro"
---

## Yaskawa GA800 E45 Fault — What It Means

The E45 fault on a Yaskawa GA800 variable frequency drive indicates input phase loss or input power loss. The drive has detected a missing phase, severe voltage imbalance, or unstable incoming supply on the main AC power input. This is a protective trip that prevents the drive from operating on damaged or incomplete power, which would cause internal component failure or unsafe motor operation.

The fault can also appear when input power voltage is changing too much, pointing to line-side instability or fluctuation. Before suspecting internal drive failure, verify that all three incoming phases are present, balanced, and stable at the drive input terminals.

## Before You Replace Anything

Technicians sometimes replace the entire VFD when E45 appears, assuming internal failure. Always measure incoming voltage at the drive input terminals first. A missing phase or loose wire is far more common than a failed drive.

[Jump to Fix](#fix)

## Common Causes

- **Blown input fuse** One or more fuses on the line side of the drive has opened, removing a phase from the input.
- **Tripped or open upstream disconnect or breaker** The protection device feeding the VFD has tripped or is not fully closed, cutting power to one or more phases.
- **Loose or overheated input terminals** Poor connections at the drive input or upstream terminal blocks create high resistance and intermittent phase loss.
- **True utility phase loss** The building or facility supply has lost one phase due to transformer, service entrance, or utility failure.
- **Severe voltage imbalance or fluctuation** Large swings in incoming voltage or phase imbalance exceed the drive's tolerance and trigger the fault.
- **Damaged upstream conductors or contactors** A broken wire, failed contactor pole, or corroded connection upstream of the drive produces the same phase-loss symptom.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is the upstream disconnect switch fully closed and the breaker not tripped?</summary>
<div class="dtree-body"><strong>Yes:</strong> The protective devices are set. Move to inspecting fuses and wiring.<br><strong>No:</strong> Reset or close the device and test. If it trips again immediately, you have a short circuit or overload upstream that must be corrected first.</div>
</details>

<details class="dtree"><summary>Do you measure balanced three-phase voltage at the drive input terminals with all power off, then re-energized?</summary>
<div class="dtree-body"><strong>Yes:</strong> Line power is good. Clear the fault and monitor. If E45 returns with verified good power, the drive may need service.<br><strong>No:</strong> You have a supply-side problem. Trace backward through fuses, disconnect, breaker, and wiring to find the open or weak phase.</div>
</details>

<details class="dtree"><summary>Are any input fuses blown or showing discoloration?</summary>
<div class="dtree-body"><strong>Yes:</strong> Replace the blown fuse with the correct rating and investigate what caused it to blow before re-energizing.<br><strong>No:</strong> Check for loose terminals, oxidized connections, or damaged wire insulation at every termination point from the panel to the drive.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Lock out and tag out** all upstream power sources to the VFD following your facility safety procedures.
2. **Inspect the upstream disconnect, breaker, and contactor** for tripped or open contacts. Reset or close if necessary, but do not re-energize yet.
3. **Check all input fuses** on the line side of the drive. Look for blown elements, blackened housings, or discoloration. Replace any blown fuse with the manufacturer-specified rating.
4. **Examine every input terminal** at the drive and upstream terminal blocks. Tighten all connections and look for heat damage, corrosion, or broken strands.
5. **Measure incoming three-phase voltage** at the drive input with a true-RMS multimeter. Compare all phase-to-phase readings. A missing phase or imbalance greater than a few volts indicates a supply problem.
6. **Repair the line-side issue** you found. Replace fuses, tighten or replace damaged wiring, or coordinate with your utility if the phase loss is at the service entrance.
7. **Clear the E45 fault** per the GA800 manual, re-energize, and run the drive under no load, then normal load. If the fault returns with verified good incoming power, contact Yaskawa technical support with the drive serial number, fault code, and your voltage measurements.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Input line fuses (Class J or T, matching drive rating) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e45-fault-code&k=Input+line+fuses+%28Class+J+or+T%2C+matching+drive+rating%29&tag=errorcodefixes-20) \| Consult the GA800 nameplate for correct amperage and interrupting rating. |
| Input terminal lugs or connectors | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e45-fault-code&k=Input+terminal+lugs+or+connectors&tag=errorcodefixes-20) \| Replace if damaged, overheated, or corroded. Match wire gauge and torque specification. |
| Upstream breaker or disconnect | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e45-fault-code&k=Upstream+breaker+or+disconnect&tag=errorcodefixes-20) \| If a pole is failed or the device will not hold, replace with the same frame size and rating. |

## When to Call a Pro

Call a qualified electrician or industrial controls technician immediately if you are not trained and authorized to work on three-phase power systems. High-voltage AC power is lethal. A professional should perform lockout/tagout, voltage measurements, terminal inspection, and fuse replacement. If the fault persists after all line-side issues are corrected and incoming power is verified as stable and balanced, contact Yaskawa technical support or an authorized drive repair center. The GA800 offers limited field repair beyond fan and control board replacement, so internal faults typically require factory service or module exchange.

**Rough cost:** A pro service call runs about $150–400 depending on whether the fix is a fuse, breaker, or wiring repair.
