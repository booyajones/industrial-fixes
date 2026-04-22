---
title: "Peerless Boiler Code 1 — Causes & Fix"
description: "What Peerless boiler code 1 means, why the boiler locks out, and how to diagnose and restore operation."
pubDatetime: 2026-04-22T11:00:00Z
modDatetime: 2026-04-22T11:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - boiler
  - peerless
---

## Peerless Boiler Code 1 — What It Means

Code 1 on a Peerless boiler (displayed on the Peerless IQ control or equivalent digital control) indicates a lockout condition. Depending on the Peerless model and control generation, Code 1 typically means the boiler has locked out due to a failed ignition sequence — the burner did not light within the trial-for-ignition period, or the control could not confirm a stable flame. Some older Peerless models display Code 1 as a general safety lockout requiring investigation and manual reset.

[Jump to Fix](#fix)

## Common Causes

- **Ignition failure** — The most common cause. The spark igniter did not generate a reliable spark, or the flame sensor did not confirm combustion within the required window.
- **Flame sensor fouling** — The flame sensor rod has oxidized and cannot produce the microamp flame rectification current required by the control.
- **Gas supply issue** — Low gas pressure, a closed manual shutoff, or a gas valve that did not open during the trial period resulted in no flame.
- **Draft or venting problem** — Insufficient draft pressure caused by a blocked vent, weak inducer, or improper vent sizing prevented proper combustion and caused the flame to extinguish immediately after lighting.

## Step-by-Step Fix {#fix}

1. **Reset the boiler** — Press the reset button on the Peerless control panel. This clears Code 1 and initiates a new ignition attempt. Watch the sequence carefully from pre-purge through ignition.
2. **Clean the flame sensor** — Remove the flame sensor rod from the burner area. Polish the sensing rod lightly with fine steel wool or a light emery cloth to remove oxidation. Reinstall securely.
3. **Verify the gas supply** — Confirm the gas shutoff valve upstream of the boiler is fully open. If the boiler shares a gas line with other appliances, confirm those appliances have normal gas pressure as a baseline check.
4. **Inspect the spark electrode** — Check the spark electrode gap (approximately 1/8") and look for cracks in the ceramic insulator. A cracked insulator allows the spark to ground out rather than jumping the gap to light the gas.
5. **Check the flue and combustion air** — Inspect the flue pipe for blockages. Confirm the combustion air intake (on direct-vent models) is unobstructed. Listen for the draft inducer (if present) during pre-purge.
6. **Measure gas valve voltage** — During the ignition sequence, use a multimeter to verify 24V AC appears at the gas valve terminals. No voltage indicates a control board output issue; voltage with no valve click indicates a failed gas valve.
7. **Reset and monitor** — After repairs, reset the boiler and observe a full heat cycle. Confirm Code 1 does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Flame sensor | OEM for Peerless model; clean before replacing |
| Spark electrode | Match to burner assembly; check gap |
| Gas valve | Replace only after control voltage and supply pressure confirmed |
| Peerless IQ control board | Replace if all field components test good and lockout persists |

## When to Call a Pro

If Code 1 returns after resetting and cleaning the flame sensor, call a licensed HVAC/boiler technician. Gas valve diagnosis, combustion analysis, and draft pressure measurement require specialized equipment and should not be performed by unqualified personnel.
