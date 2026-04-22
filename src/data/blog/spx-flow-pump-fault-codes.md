---
title: "SPX Flow Pump Fault Codes: Complete Guide"
description: "SPX Flow pump fault codes and diagnostics. Fault codes for Bran+Luebbe, Lightnin, and Delco pumps, causes, and technician-level troubleshooting."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-04-22T23:45:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - pumps
  - spx-flow
  - industrial
---

# SPX Flow Pump Fault Codes

SPX Flow (formerly incorporating Bran+Luebbe, Lightnin, Plenty Mirrlees, Delco) produces a wide range of industrial pumps for chemical processing, food/beverage, and utilities. Fault detection is typically through the associated motor protection relay or VFD — the pump itself does not generate electronic codes.

## SPX Flow Pump Fault Reference

| Fault Indication | Fault Description | Common Cause | Action |
|-----------------|------------------|--------------|--------|
| Motor trips/overload | Motor thermal trip | Overload, high viscosity fluid, worn impeller | Check FLA vs. nameplate |
| Vibration high | Excessive vibration | Cavitation, bearing, alignment | Check vibration levels |
| Pressure relief open | Relief valve venting | Discharge blockage, closed valve | Check discharge system |
| Seal leak | Mechanical seal failure | Worn seal or improper installation | Replace mechanical seal |
| No flow | Pump running, no output | Air lock, blocked suction, wrong rotation | Check suction and rotation |
| Noise (cavitation) | Cavitation damage | Insufficient NPSH | Check suction conditions |
| Bearing overtemp | High bearing temperature | Lubrication, overload, misalignment | Check lubrication schedule |
| Output low | Below rated output | Worn impeller, high viscosity | Inspect impeller wear rings |

## Most Common SPX Flow Faults

### Motor Overload
SPX Flow pumps handling high-viscosity fluids (such as Bran+Luebbe metering pumps on chemicals) are susceptible to overload if fluid viscosity increases. Check fluid temperature — colder, more viscous fluids draw higher current. Check the motor protection relay trip current setting matches the motor nameplate.

### Seal Leak
Most SPX Flow centrifugal and positive displacement pumps use mechanical seals. Seal failure is typically caused by excessive shaft runout, dry run, wrong seal material for the fluid, or abrasive particles in the fluid. Inspect the seal gland for liquid weepage or crystallized chemical deposits.

### No Flow — Air Lock
Centrifugal pumps require priming. If air enters the suction line, the pump continues to run but produces no flow or very low head. Install a foot valve on vertical suction lifts, verify suction pipe is fully submerged, and prime via the vent valve on the pump casing.

### Cavitation
Cavitation occurs when suction pressure drops below the fluid's vapor pressure. Required NPSH must exceed available NPSH. Check suction strainer for blockage (most common cause), reduce suction line length/fittings, or reduce pump speed.

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| Mechanical seal | Match shaft diameter and material |
| Impeller wear rings | Replace as sets |
| Bearing set | Match pump specification |
| Suction strainer basket | Clean or replace regularly |
| Motor protection relay | Match FLA and trip class |

> **Pro tip:** SPX Flow provides PumpView and other IIoT monitoring tools for their pumping equipment. For process-critical applications, condition-based monitoring with vibration and temperature sensors is more cost-effective than scheduled replacement of bearings and seals.
