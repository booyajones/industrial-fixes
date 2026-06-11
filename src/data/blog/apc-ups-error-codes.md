---
title: "APC UPS Error Codes and Fault Guide - Complete Reference"
description: "APC UPS error codes and fault indicators for Back-UPS, Smart-UPS, and Symmetra systems: beep patterns, LED codes, and fixes."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - apc
  - ups
  - power-systems
money_part: "Replacement battery (RBC)"
---

## APC UPS Error Codes - Quick Reference

APC UPS systems from Back-UPS RS/Pro, Smart-UPS, and Symmetra lines communicate faults via LED indicators, beep codes, LCD displays, and via APC PowerChute software or network management cards.

| Code / Fault | System | Meaning | Quick Fix |
|-------------|--------|---------|-----------|
| 4 beeps / On Battery | All | Utility power lost | Check power source |
| Continuous beep | All | Battery critically low | Connect load, charge battery |
| Battery Replace LED | Smart-UPS | Battery at end of life | Replace battery |
| Overload LED (red) | Back-UPS/Smart-UPS | Load exceeds UPS rating | Reduce load |
| F01 | Symmetra | Battery failure | Replace battery module |
| F02 | Symmetra | Intelligence module fault | Replace I/O module |
| F06 | Symmetra | Overload on output | Reduce connected load |
| Site Wiring Fault LED | Smart-UPS | Building wiring problem | Check building electrical |
| Replace Battery | Smart-UPS LCD | Battery test failed | Replace battery |
| Overcharge | Back-UPS | Battery overcharge condition | Check charger circuit |

## Most Common Faults

### Replace Battery
Battery Replace LED or LCD message on APC Smart-UPS indicates the internal battery self-test has failed. APC VRLA batteries typically last 3–5 years depending on temperature and discharge frequency. Hot environments dramatically shorten battery life - every 10°C above 25°C cuts battery life in half.

To replace: power down the UPS or use APC's "Battery Replace" procedure to hot-swap without dropping load (on Smart-UPS with HotSwap). Match the battery part number exactly - mixing battery chemistry or capacity causes charging problems.

### Overload
Red overload LED means connected load exceeds the UPS VA rating. Check the load with a watt meter. Common causes: added equipment, printer with large inrush, or a failed component drawing excessive current. Remove load until the overload clears, then add equipment incrementally.

### Site Wiring Fault
APC Smart-UPS checks building wiring and reports site wiring fault when it detects a missing safety ground or neutral-ground voltage issues. This is a building wiring problem - contact a licensed electrician. Running a UPS with a wiring fault can damage equipment and is a safety hazard.

### Symmetra F01 - Battery Failure
Symmetra battery modules include individual cell monitoring. F01 can indicate one or more dead cells in a battery frame. Replace the indicated battery module; Symmetra systems allow hot-swap of individual modules without dropping load.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Replacement battery (RBC) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-apc-ups-error-codes&k=Replacement+battery+%28RBC%29&tag=errorcodefixes-20) \| Size per UPS model - match RBC number |
| Symmetra battery module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-apc-ups-error-codes&k=Symmetra+battery+module&tag=errorcodefixes-20) \| Hot-swappable |
| Network management card (NMC) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-apc-ups-error-codes&k=Network+management+card+%28NMC%29&tag=errorcodefixes-20) \| Replace on network fault |
| Back-UPS output fuse | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-apc-ups-error-codes&k=Back-UPS+output+fuse&tag=errorcodefixes-20) \| Replace on output overload damage |
| Smart-UPS internal fuse | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-apc-ups-error-codes&k=Smart-UPS+internal+fuse&tag=errorcodefixes-20) \| Replace on no-output fault |
## When to Call a Pro
Symmetra PX and Galaxy-series UPS maintenance, including bypass switching and capacitor replacement, requires APC/Schneider-trained technicians. Do not attempt internal repairs on large UPS systems without proper training.

