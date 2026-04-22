---
title: "Burnham Series 2 Boiler Error Codes: Complete Guide"
description: "Burnham Series 2 boiler error codes and fault diagnostics. Fault codes, lockout causes, and technician-level troubleshooting for Series 2 cast iron boilers."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-04-22T23:45:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - burnham
  - boiler
---

# Burnham Series 2 Boiler Error Codes

Burnham Series 2 boilers use a Honeywell or Beckett primary control that displays fault codes via LED or LCD. Controls vary by burner type (gas or oil). Gas units typically use a Honeywell S8610 or S9201 control; oil units use a Beckett AFG or Riello burner with cad cell relay.

## Series 2 Fault Code Table

| Code | Fault Description | Common Cause | Action |
|------|------------------|--------------|--------|
| E1 | Ignition lockout | No flame detected after 3 trials | Check gas/oil supply and igniter |
| E2 | Gas valve fault | Failed gas valve or wiring | Check 24 VAC at valve terminals |
| E3 | Pressure switch fault | Blocked inducer or failed switch | Measure flue pressure |
| E4 | High-limit lockout | Boiler overtemperature | Check pump, thermostat, and system |
| E5 | Flame sensor fault | Dirty or failed flame rod | Clean or replace flame sensor |
| E6 | Inducer fault | Failed inducer motor | Check inducer amps and rotation |
| E7 | Low water cutoff | Low water in boiler | Check system fill and pressure |
| Flashing Red | Hard lockout | Manual reset required | Diagnose and reset |
| Steady Red | Soft lockout | Auto-reset after cooling | Find cause before it repeats |

## Most Common Series 2 Faults

### E1 — Ignition Lockout (Gas)
Burnham Series 2 gas units require 3.5 in. w.c. natural gas pressure at the manifold. Check gas pressure with a manometer. Inspect igniter electrode for cracks and carbon — replace if cracked. Clean flame sensor rod with emery cloth.

### E4 — High-Limit Lockout
Burnham Series 2 boilers set the high-limit at 200°F (factory). Lockout occurs when aquastat contacts open. Check for a failed or seized circulator pump. Verify all zone valves are operational. Check thermostat anticipator setting.

### E7 — Low Water Cutoff
The LWCO (low water cutoff) is a critical safety device. If the boiler loses water pressure, it locks out to prevent dry-fire damage. Check system pressure (residential: 12–18 PSI hot), look for leaks, and test the LWCO annually.

### Ignition Lockout (Oil)
On oil-fired Series 2 units with Beckett burner: check oil tank level, oil filter condition, and nozzle condition. Beckett AFG primary has a reset button — push once. If it locks out again, check cad cell resistance (should be < 1600 Ω in flame, > 100,000 Ω no flame).

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| Flame sensor (gas) | Clean first — measure µA |
| Oil burner nozzle | Replace annually |
| Ignition transformer | Check spark at electrode |
| Circulator pump | Check for seized impeller |
| Low water cutoff | Test annually — replace if suspect |
| Aquastat | Match temperature rating |

> **Pro tip:** Burnham Series 2 cast iron boilers require annual maintenance. Clean the heat exchanger passages with a boiler brush — accumulated soot significantly reduces efficiency and can cause overtemperature faults.
