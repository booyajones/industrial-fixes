---
title: "Yaskawa A1000 PF Fault - Causes & Fix"
description: "PF means input phase loss or severe voltage imbalance on the incoming AC supply. Check incoming line fuses and wiring first."
pubDatetime: 2026-06-12T10:06:17Z
modDatetime: 2026-06-12T10:06:17Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Input line fuses (class and amperage per drive nameplate)"
most_likely_cause: "Blown input fuse or open breaker pole"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Visually inspect all three incoming line fuses and circuit-breaker poles for a blown element or tripped pole"
  - "Check for any loose or discolored wiring at the drive input terminals and upstream disconnect"
part_price: "$5-25 per fuse"
---

## What this code means
The PF code on a Yaskawa A1000 drive indicates an input phase-loss or severe phase-voltage imbalance condition. The drive has detected that one of the three incoming AC supply phases is missing or that the voltages across the three phases are significantly unbalanced. This is a supply-side fault, not a motor-output problem. The drive shuts down to protect its internal circuitry from damage caused by unbalanced or missing input power.

In practical terms, the fault usually points to a problem upstream of the drive itself: a blown fuse, a failed breaker pole, a loose or burnt input terminal, or a utility supply issue. In some cases, aged main circuit capacitors inside the drive can contribute to nuisance PF faults, especially when the drive's maintenance-life indicator shows the capacitors are nearing end-of-life.

## Before You Replace Anything

Technicians sometimes replace the drive itself when the real fault is a loose input terminal or a single blown fuse upstream. Always measure line-to-line voltage at the drive input terminals and inspect upstream fuses and breaker contacts before condemning the drive.

## Common Causes

- **Blown input fuse or open breaker pole** A single failed fuse or breaker contact removes one phase and triggers the phase-loss detection.
- **Loose or overheated input wiring** High resistance at a terminal or lug creates voltage drop and imbalance that the drive reads as a phase loss.
- **Utility supply imbalance or fluctuation** Severe voltage imbalance or a utility-side phase outage upstream of the building can cause the drive to see a missing phase.
- **Failed contactor or disconnect contact** A single pole of an upstream line contactor or disconnect can fail open, removing one phase.
- **Aged main circuit capacitors** When the drive's DC-bus capacitors approach end-of-life, internal ripple and sensing errors can produce nuisance PF faults.
- **Defective line reactor or input filter** If a line reactor or filter is installed and one winding fails open, the drive will see an incomplete input.

## Step-by-Step Fix {#fix}

1. **Lock out and tag out** the incoming power at the disconnect or panel breaker. Verify zero voltage at the drive input terminals with a multimeter before opening any covers.
2. **Inspect all three input fuses** (or breaker poles) feeding the drive. Look for a blown fuse element, a discolored contact, or a tripped pole. Replace any failed fuse or breaker.
3. **Measure line-to-line voltage** at the drive input terminals (L1–L2, L2–L3, L3–L1) with power restored and the drive still locked out from starting. All three readings should be within a few volts of each other. A significant difference (more than 5–10 V on a 480 V system, for example) indicates a supply problem.
4. **Check terminal torque and heat damage** on the drive's main power terminals (R/L1, S/L2, T/L3) and at any upstream contactor, disconnect, or line reactor. Re-torque lugs to the manufacturer's specification and replace any burnt or damaged terminals or wire.
5. **Inspect the line contactor and disconnect** for one pole that is stuck open, pitted, or showing high resistance. Replace the contactor or disconnect if a single contact is defective.
6. **Review the drive's maintenance data** by checking parameter U4-05 (capacitor maintenance life, if available on your model). If the value approaches or exceeds 90 percent, plan for capacitor or drive replacement even if you fix the immediate supply fault.
7. **Clear the PF fault** from the drive's display or keypad, restore power, and attempt a test run. If the fault reappears with verified balanced input voltage and tight connections, the drive's internal sensing circuitry or power section may be faulty and the drive should be sent for repair or replaced.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Input line fuses (class and amperage per drive nameplate) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-pf-fault-code&k=Input+line+fuses+%28class+and+amperage+per+drive+nameplate%29&tag=errorcodefixes-20) \| Match the fuse type and interrupt rating to the drive input current and your local code. |
| Line contactor or disconnect switch | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-pf-fault-code&k=Line+contactor+or+disconnect+switch&tag=errorcodefixes-20) \| Replace if a single pole is burned, pitted, or stuck open. |
| Main circuit capacitors (factory service kit or drive replacement) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-pf-fault-code&k=Main+circuit+capacitors+%28factory+service+kit+or+drive+replacement%29&tag=errorcodefixes-20) \| Consult Yaskawa or an authorized repair center when capacitor life exceeds the recommended threshold. |
| Input line reactor (if installed and found defective) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-pf-fault-code&k=Input+line+reactor+%28if+installed+and+found+defective%29&tag=errorcodefixes-20) \| Match inductance and current rating to your drive model. |

## When to Call a Pro

Call a qualified electrician or automation technician any time you need to work inside an energized panel or drive enclosure. High-voltage three-phase power is deadly. A technician will lock out the supply, safely measure phase voltages, check fuse continuity, inspect terminals for heat damage, and determine whether the fault is in the upstream wiring or inside the drive. If the drive's capacitor maintenance life is high or if balanced input power still produces a PF fault, the drive may need factory-level repair or replacement. Do not attempt to open the drive's main power section or replace internal capacitors yourself unless you are factory-trained and the drive is fully discharged and locked out.
