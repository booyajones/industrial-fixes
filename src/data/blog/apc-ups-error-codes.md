---
title: "APC UPS Fault Codes & Errors: F01-F09, Beeps, LEDs"
description: "APC UPS fault codes decoded: Back-UPS Pro F01-F09, Smart-UPS Replace Battery and Overload LEDs, Symmetra F-faults, plus beep patterns and real fixes."
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

## More Apc Ups fault codes

Compiled from manufacturer service manuals and authorized documentation.

| Code | What it means | Likely cause | How to fix |
| --- | --- | --- | --- |
| F03 | On-Battery Xcap Overload (APC Back-UPS Pro BR/BN models) | Internal fault detected during on-battery operation | Per APC's manual, F03 cannot be corrected by the user. Contact APC/Schneider Electric Technical Support for service. |
| F04 | Clamp Short (APC Back-UPS Pro BR/BN models) | Internal hardware fault | Per APC's manual, F04 cannot be corrected by the user. Contact APC/Schneider Electric Technical Support; the unit typically requires replacement or factory service. |
| F05 | Charge Fault (APC Back-UPS Pro BR/BN models) | Internal battery-charger circuit failure | Per APC's manual, F05 cannot be corrected by the user. Contact APC/Schneider Electric Technical Support. |
| F07 | Temperature (APC Back-UPS Pro BR/BN models) | Internal overtemperature detected | Per APC's manual, F07 cannot be corrected by the user. Confirm the unit is not overloaded and has clear ventilation, then contact APC/Schneider Electric Technical Support if it persists. |
| F08 | Fan Fault (APC Back-UPS Pro BR/BN models) | Internal cooling fan failure | Per APC's manual, F08 cannot be corrected by the user. Contact APC/Schneider Electric Technical Support. |
| F09 | Internal Fault (APC Back-UPS Pro BR/BN models) | General internal hardware failure | Per APC's manual, F09 cannot be corrected by the user. Contact APC/Schneider Electric Technical Support. |


## How to troubleshoot Apc Ups

## How to diagnose an APC UPS fault

APC units span three distinct families, and the same indicator can mean different things across them, so identify the model line first: **Back-UPS / Back-UPS Pro** (LED or small LCD, "F0x" fault codes), **Smart-UPS** (LCD text or icon LEDs), and **Symmetra / modular** (numbered module faults).

**Start with the obvious.** Most "faults" on APC hardware are not the electronics failing. In order of likelihood: an exhausted battery (VRLA cells last 3-5 years, and heat halves that life for every 10 C above 25 C), an overloaded output, or a building-wiring problem the UPS correctly detected. Check these before assuming an internal failure.

**Separate user-fixable from service-only.** On Back-UPS Pro BR/BN units, APC documents only **F01 (on-battery overload)** and **F02 (on-battery output short)** as user-correctable: power down, strip the battery-backup outlets, power back up, and reintroduce load one device at a time to isolate the culprit. Every other code (F03 through F09) is an internal hardware fault that APC says the user cannot correct, meaning the unit needs factory service or replacement. Do not open the enclosure chasing these.

**Isolate overload vs. short.** An overload clears when you remove enough load; a short circuit trips again the instant the offending device is reconnected, even with everything else unplugged. If the fault returns with nothing plugged into the backup outlets, the UPS itself is at fault.

**Respect the site-wiring warning.** A site/building wiring fault (missing ground, reversed polarity, or an overloaded neutral) is a real electrical hazard, not a UPS defect. Stop and bring in a licensed electrician rather than defeating the warning.

**When to call a pro.** Anything beyond battery swaps and load management on large or modular gear (Symmetra PX, Galaxy) requires an APC/Schneider-trained technician, especially bypass operations and capacitor service. For desktop Back-UPS and Smart-UPS units showing an internal F-code, the economical path is often replacement rather than board-level repair.


## Frequently asked questions

### What does F02 mean on my APC Back-UPS?

On a Back-UPS Pro BR/BN unit, F02 is an on-battery output short circuit. Turn the UPS off, unplug everything from the battery-backup outlets, then turn it on and reconnect devices one at a time to find the shorted load. If F02 returns with nothing connected, the UPS needs service.

### My APC shows F03 (or F04, F05, F07, F08, F09). Can I fix it myself?

No. APC's own manuals state that faults F03 through F09 cannot be corrected by the user. They indicate an internal hardware failure (capacitor, clamp, charger, thermal, fan, or general internal fault). Contact APC/Schneider Electric Technical Support. For an out-of-warranty desktop unit, replacement is usually cheaper than repair.

### How long do APC UPS batteries last and why do they fail so fast?

APC's sealed VRLA batteries typically last 3-5 years. Heat is the biggest killer: battery life roughly halves for every 10 C (18 F) above 25 C. A unit in a hot closet or on top of a warm server can trigger a Replace Battery warning in as little as two years.

### Why does my APC UPS beep even though the power is on?

Steady periodic beeps with the power on usually mean a failed battery self-test (Replace Battery) or a site wiring fault the UPS detected in your outlet. A red overload LED means your connected equipment exceeds the UPS rating. Check which indicator is lit before assuming the unit is broken.

### Is a Site Wiring Fault an APC UPS problem?

No. A site or building wiring fault means the UPS detected a missing safety ground, reversed polarity, or a neutral-to-ground issue in your outlet. That is an electrical hazard in the building, not a UPS defect. Have a licensed electrician inspect the circuit rather than bypassing the warning.

