---
title: "Trane 3 Flash Pressure Switch Fault — Detailed Diagnosis Guide"
description: "Trane 3 flashes specifically indicating a pressure switch fault. This guide covers differential pressure switch testing, hose tracing, condensate drain diagnosis, and inducer verification."
pubDatetime: 2026-04-22T18:00:00Z
modDatetime: 2026-04-22T18:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - trane
  - furnace
  - hvac
  - pressure-switch
  - error-code
---

## Trane 3 Flashes — Pressure Switch Fault (Deep Dive)

On most Trane furnaces, **3 flashes** from the diagnostic LED means a **pressure switch fault** — either the switch didn't close when it should have (inducer running, draft established) or it failed to open when it should have (before inducer starts). This guide goes deeper than basic troubleshooting.

## The Two Types of Trane Pressure Switch Faults

| [Scenario](https://www.amazon.com/s?k=Scenario&tag=errorcodefixe-20) | What It Means |
|---|---|
| [Switch won't close (stuck open)](https://www.amazon.com/s?k=Switch%20won't%20close%20(stuck%20open)&tag=errorcodefixe-20) | Inducer running but no/low draft — most common |
| [Switch won't open (stuck closed)](https://www.amazon.com/s?k=Switch%20won't%20open%20(stuck%20closed)&tag=errorcodefixe-20) | Welded contacts or condensate in switch — less common |

Both cause 3 flashes but require different repairs.

## Pressure Switch Stuck Open — Full Diagnosis

This is the most common scenario. The inducer is running but draft isn't being sensed.

### Check the Condensate System First

High-efficiency Trane furnaces (90%+ AFUE) generate significant condensate. This water drains through a trap and can:
- **Block the pressure switch port** if the drain is backed up
- **Fill the inducer housing** with water, reducing suction
- **Freeze in cold attics** or unconditioned spaces

Action: Disconnect the condensate drain at the trap. If water pours out under pressure, the drain is clogged. Clean the trap with warm water. Check the drain line all the way to the floor drain.

### Inspect All Pressure Switch Hoses

Trane 2-stage and modulating furnaces may have **2–3 pressure switches** with multiple hose connections. Trace each hose:

1. From the inducer housing outlet port
2. From the inducer housing inlet port (negative pressure side on some)
3. From the secondary heat exchanger (on condensing models)

Look for: cracks, splits at the barb fittings, hoses kinked around corners, hoses that have come off entirely. Replace with 3/16" ID vinyl tubing from any hardware store.

### Test the Switch with a Manometer

For definitive testing, connect a digital manometer to the inducer port while the inducer is running. A properly operating inducer should produce:
- Negative pressure (suction) of typically **-0.5 to -1.5" WC** on the draft side
- The pressure switch closes at its rated setpoint (usually -0.2 to -0.5" WC)

If inducer suction is low, the problem is draft (blocked flue, inducer wear) not the switch itself.

## Pressure Switch Stuck Closed — Full Diagnosis

When the IFC detects the pressure switch is closed at startup (before inducer starts), it throws a fault because this shouldn't happen.

Causes:
- **Condensate inside the switch** — water bridges the contacts
- **Welded contacts** from previous arcing
- **Wrong replacement switch installed** — setpoint too low, closes at atmospheric pressure

Test: With the furnace powered off, measure continuity across the pressure switch terminals. If it reads closed (continuity) at rest with no hoses connected, the switch is defective — replace it.

## Inducer Motor Performance

Even if the switch and hoses are good, a worn inducer motor may not generate enough draft to close the switch. Signs of inducer wear:
- Motor hums but doesn't spin
- Squealing bearing noise before startup
- Motor runs but spins slow (measure RPM with tachometer if possible)
- Housing is cracked, allowing air bypass

## Pressure Switch Reference Values (Common Trane Models)

| [Model Series](https://www.amazon.com/s?k=Model%20Series&tag=errorcodefixe-20) | Switch Rating | Switch Part | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | --- |---|---|
| TUD/TDX 80% | [-0.45" WC](https://www.amazon.com/s?k=-0.45%22%20WC&tag=errorcodefixe-20) | SWT2641, SWT02641 |
| [XR95 (condensing)](https://www.amazon.com/s?k=XR95%20(condensing)&tag=errorcodefixe-20) | -0.20" WC, -1.75" WC | Multiple switches | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | XV95 (2-stage) | Dual switch assembly | [CNT04784](https://www.amazon.com/s?k=CNT04784&tag=errorcodefixe-20) |  | XC95M (modulating) | [3 switches](https://www.amazon.com/s?k=3%20switches&tag=errorcodefixe-20) | Multiple |

*Always verify on the IFC board label or tech spec sheet for your specific model.*

## Parts List

| Part | Typical Cost |
|---|---|
| [Pressure switch (generic)](https://www.amazon.com/s?k=Pressure%20switch%20(generic)&tag=errorcodefixe-20) | $15–45 |
| [OEM Trane pressure switch](https://www.amazon.com/s?k=OEM%20Trane%20pressure%20switch&tag=errorcodefixe-20) | $40–90 |
| [Inducer motor assembly](https://www.amazon.com/s?k=Inducer%20motor%20assembly&tag=errorcodefixe-20) | $150–400 |
| [Condensate trap kit](https://www.amazon.com/s?k=Condensate%20trap%20kit&tag=errorcodefixe-20) | $15–30 |
| [Drain line tubing (per foot)](https://www.amazon.com/s?k=Drain%20line%20tubing%20(per%20foot)&tag=errorcodefixe-20) | $1–2 |

## When Code 3 Becomes Code 4 or Code 6

If you see 3 flashes that escalate to 4 flashes (open limit) or 6 flashes (rollout), the pressure switch issue has caused secondary overheating. Fix the pressure switch fault first before addressing secondary codes.
