---
title: "Trane Rooftop Unit Fault 77 — High Pressure Cutout"
description: "Trane RTU Fault 77 means a high-pressure cutout on the refrigerant circuit. Learn the exact causes, diagnostic steps, and fixes for this commercial HVAC fault."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - trane
  - rooftop-unit
  - refrigerant
---

# Trane Rooftop Unit Fault 77 — High Pressure Cutout

**Fault 77** on Trane commercial RTUs (Precedent, YCD, and similar series) means the high-pressure safety switch has tripped, shutting down the compressor to prevent damage. The fault appears on the ComfortLink or Tracer zone sensor display.

## Jump to Fix

- [Most Likely Cause](#most-likely-cause)
- [Diagnosis Steps](#diagnosis)
- [Parts](#parts)

## What Triggers Fault 77

The high-pressure switch monitors refrigerant discharge pressure. For R-410A systems, the switch typically trips between 550–620 psig. When pressure exceeds this setpoint, the switch opens, the compressor shuts off, and Fault 77 is stored.

## Common Causes {#most-likely-cause}

| Cause | Likelihood |
|---|---|
| Dirty or blocked condenser coil | Very High |
| One or more condenser fan motors not running | Very High |
| Refrigerant overcharge | Medium |
| Failed condenser fan capacitor | Medium |
| Non-condensables in refrigerant circuit | Medium |
| Defective high-pressure switch | Low |
| Restricted liquid line or TXV | Low |

## Step-by-Step Diagnosis {#diagnosis}

**Step 1 — Inspect the condenser coil**
- Shut down the unit and visually inspect the condenser coil
- Dirt, cottonwood, leaves, or grease block airflow and spike head pressure
- Clean with Nu-Brite or similar alkaline coil cleaner, rinse from inside out

**Step 2 — Verify all condenser fans are running**
- With unit running in cooling, observe each condenser fan
- A stopped fan with the motor hot = failed run capacitor (most common)
- Test capacitor µF with a meter — replace if outside ±6% of rating
- If capacitor is good, check motor windings for open circuit

**Step 3 — Check refrigerant pressures**
- Connect gauges to the high and low side service ports
- Normal high-side pressure (R-410A, 95°F ambient): 280–320 psig
- High-side above 400 psig with fans running and coil clean = overcharge or non-condensables
- Calculate subcooling: if above 20°F, refrigerant may be overcharged

**Step 4 — Test the high-pressure switch**
- The switch should be closed at ambient pressure
- Open continuity at rest means a failed switch — replace
- Confirm correct switch part number (trip pressure varies by model)

**Step 5 — Check liquid line and TXV**
- Feel the liquid line — it should be warm, not hot
- A hot liquid line with high head pressure suggests a restriction
- Check TXV screen for debris if pressures remain abnormal after coil cleaning

## Fault 77 Reset Procedure

Trane RTUs require a manual reset for Fault 77 in most configurations:
1. Correct the root cause first
2. Access the ComfortLink/Tracer zone sensor menu
3. Navigate to Diagnostics > Reset Faults
4. Alternatively, cycle unit power at the disconnect for 30 seconds

## Replacement Parts {#parts}

| Part | Notes |
|---|---|
| Condenser fan run capacitor | Match µF and voltage — 370V or 440V AC |
| Condenser fan motor | Match HP, RPM, rotation direction |
| High-pressure switch | Trane part BRD05072 or equivalent — match trip pressure |
| TXV valve | Model-specific — match refrigerant type |

> **Pro tip:** On hot summer days, high head pressure is often entirely caused by a dirty condenser coil or a stopped condenser fan. Clean the coil and replace the capacitor before assuming refrigerant issues.
