---
title: "Florida Heat Pump (FHP) Fault Codes: UPM Blink Code Guide"
description: "Florida Heat Pump (FHP) fault codes explained: UPM board blink codes 1-6 for high pressure, low pressure, freeze and brownout, with causes, fixes and reset steps."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - florida-heat-pump
  - geothermal
  - heat-pump
---

# Florida Heat Pump Error Codes: Complete Technician Guide

Florida Heat Pump (FHP), now part of Bosch Thermotechnology, manufactures water-source and geothermal heat pumps used in commercial and residential applications. FHP units display fault codes on the DDC (digital display controller) or communicate via the optional ECA (extended control accessory) board.

## FHP Fault Code Table

| Code | Description | Common Cause |
|---|---|---|
| E1 | High-pressure lockout | High loop/water temp, low airflow, dirty coil |
| E2 | Low-pressure lockout | Low refrigerant, low airflow, low loop flow |
| E3 | Freeze protection — refrigerant | Low refrigerant temp — airside issue |
| E4 | Freeze protection — water coil | Low entering water temperature |
| E5 | High discharge temperature | Low refrigerant, restricted TXV |
| E6 | Compressor overload | High amps — check compressor and supply voltage |
| E7 | Low voltage lockout | Supply voltage below minimum |
| E8 | Communication fault | Check wiring between control boards |
| E9 | Condensate overflow | Clogged drain pan or condensate pump |
| F1 | Entering water sensor fault | Check sensor wiring and resistance |
| F2 | Leaving water sensor fault | Check sensor at water outlet |
| F3 | Entering air sensor fault | Check sensor at return air |
| F4 | Leaving air sensor fault | Check sensor at supply air |
| H1 | Hard lockout | 3 fault trips — manual reset required |

## Most Common FHP Faults

### E1 — High Pressure Lockout
The most common FHP commercial fault, especially in summer:
1. Check entering water temperature — above 90°F causes high head pressure
2. Inspect air filter and blower motor
3. Check refrigerant charge (subcooling)
4. Verify cooling tower or loop system operation

### E2 — Low Pressure Lockout
1. Check air filter and blower
2. Check loop pump operation and flow rate
3. Check refrigerant charge with gauges
4. Inspect TXV for restriction

### E3 / E4 — Freeze Protection
- E3: Air-side issue — dirty filter or low airflow in cooling
- E4: Water-side issue — low loop water temperature (below 40°F entering)
- Check antifreeze concentration in loop (propylene glycol recommended)

### F1 / F2 / F3 / F4 — Sensor Faults
FHP temperature sensors are typically 10K ohm NTC thermistors. Check:
- Sensor resistance at known temperature (10K ohm at 77°F)
- Wiring continuity
- Sensor position and mounting

## FHP vs Bosch Branding Note

FHP units manufactured after 2015 may show Bosch Thermotechnology branding. The fault codes and diagnostic procedures are identical. Service manuals reference both FHP and Bosch part numbers.

## FHP Parts Reference

| Part | Notes |
|---|---|
| [High/low pressure switch](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-florida-heat-pump-error-codes&tag=errorcodefixes-20) | Match refrigerant and trip pressure |
| [Temperature sensor](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-florida-heat-pump-error-codes&tag=errorcodefixes-20) | 10K NTC thermistor — FHP part 02531-016 |
| [TXV assembly](https://www.amazon.com/s?ascsubtag=ecf-florida-heat-pump-error-codes&k=TXV+assembly&tag=errorcodefixes-20) | Match capacity and refrigerant type |
| [DDC control board](https://www.amazon.com/s?k=DDC+control+board&tag=errorcodefixes-20) | FHP/Bosch part — match model number |
| [ECA accessory board](https://www.amazon.com/s?ascsubtag=ecf-florida-heat-pump-error-codes&k=ECA+accessory+board&tag=errorcodefixes-20) | For advanced controls and monitoring |

> **Note:** FHP/Bosch geothermal units have a hard lockout after 3 consecutive fault trips. After correcting the root cause, reset via the DDC controller or by cycling power at the breaker for 60 seconds.

## More Florida Heat Pump fault codes

Compiled from manufacturer service manuals and authorized documentation.

| Code | What it means | Likely cause | How to fix |
| --- | --- | --- | --- |
| 5 blinks (LED) | Air Coil Freeze condition (Freeze 2) | Refrigerant temperature at the air coil has fallen below the freeze limit (below 30 F for 30 seconds). Usually low airflow: dirty filter, failed blower, closed dampers, or low charge. | Replace the air filter, verify blower/ECM operation and duct airflow, and check refrigerant charge. Freeze 2 sensor is mounted on the air-coil (evaporator) side. Soft-lock on trip, hard-lock on repeated trips. |
| 6 blinks (LED) | Brown Out (low voltage) fault | Control voltage has fallen below 18 VAC. Undersized/failing transformer, loose 24 VAC wiring, or a supply brownout. | Measure 24 VAC control voltage under load, inspect transformer and low-voltage connections, and check building supply voltage. Compressor is held off until voltage recovers. |
| EM015 code 3 | Freeze Sensor fault (older EM015 board) | On FHP units using the older EM015 diagnostic control, code 3 is a freeze/temperature sensor fault. The EM015 scheme is 1=High Pressure Switch, 2=Low Pressure Switch, 3=Freeze Sensor, 4=Condensate Overflow, 5=Brown-out. | Check the freeze thermistor wiring, mounting and resistance, and confirm loop flow/temperature. Reset by cycling power to the board or unit. |

## How to troubleshoot Florida Heat Pump

## How to diagnose a Florida Heat Pump (FHP) water-source unit

FHP water-source and geothermal units protect the compressor through a board-mounted safety module and report faults by counting **LED blinks**, not by displaying an E-code. Two control generations are common in the field: the older **EM015** (numeric codes 1-5) and the current **UPM (Unit Protection Module)** used on LV, SV and similar series (blink codes 1-6). Note that some newer UPM boards renumber freeze/leak faults (for example 6 = evaporator freeze, 7 = refrigerant leak detection), so always read the blink count at the board and match it to the correct table for that exact unit before condemning any part.

**Check the water side first.** Because these are water-source machines, the single most common root cause of nuisance lockouts is water flow and water temperature, not the refrigerant circuit. Before touching gauges, confirm the loop pump is running, the flow rate is within spec, strainers are clean, and entering water temperature is in range. High entering water temperature in cooling drives high head pressure (blink 1); low loop flow or low loop temperature drives freeze and low-pressure trips (blinks 2 and 3). FHP recommends a flow switch so the unit will not run on lost flow.

**Then check airflow and condensate.** A dirty filter, failed blower, or closed damper starves the air coil and produces air-coil freeze (blink 5) or low pressure (blink 2). A clogged drain or dead condensate pump triggers condensate overflow (blink 4), which on FHP boards typically drives a lockout rather than a simple soft retry.

**Understand the lockout logic before you reset.** The UPM runs a 5-minute anti-short-cycle delay and an intelligent reset: on a fault it waits out the delay and restarts if the condition cleared. If the same fault recurs enough times within an hour (the count is set by the lockout DIP switch), the unit goes to **hard lockout** and needs a manual reset, done by cycling the thermostat off/on (RESET DIP = Y) or the breaker (RESET DIP = R). Repeatedly resetting without fixing the root cause accelerates compressor wear.

**When to call a pro.** Homeowners and facilities staff can safely check filters, condensate drains, loop pump operation and thermostat resets. Anything requiring refrigerant gauges, pressure-switch or TXV replacement, freeze-sensor resistance testing, or antifreeze correction is EPA-certified refrigerant work and should go to a qualified water-source/geothermal technician. Because a compressor is the most expensive component in the box, a persistent high-pressure or low-pressure lockout is worth professional diagnosis rather than repeated hard resets.

## Frequently asked questions

### What does 1 blink (or code 1) mean on my Florida Heat Pump?

One LED blink is a High Pressure fault: discharge pressure exceeded 600 PSIG. In cooling this is usually high entering water temperature or lost loop flow; also check for a dirty air coil/filter and overcharge. Repeated trips within an hour force a hard lockout requiring a manual reset.

### Why does my FHP unit lock out on a condensate fault?

By design. On the UPM board a condensate overflow fault (4 blinks) drives the unit into lockout rather than a simple retry. Clear the drain line, trap and condensate pump, then manually reset by cycling the thermostat off and on, or the breaker, depending on the RESET DIP switch.

### How do I reset a hard lockout on a Florida Heat Pump?

Fix the root cause first, then reset. If the RESET DIP switch is set to Y, turn the thermostat off and back on. If it is set to R, shut power off at the breaker and restore it. Cycling power on the older EM015 board clears its codes the same way. Resetting without correcting the fault will just re-lock and wear the compressor.

### What are the freeze faults (3 blinks and 5 blinks) telling me?

Both are freeze-protection trips: refrigerant temperature has fallen below the freeze limit (about 30 F) for 30 seconds. Three blinks is a water-coil freeze, usually low loop flow, low loop temperature, or too little antifreeze. Five blinks is an air-coil freeze, usually low airflow from a dirty filter or failed blower. On a fresh-water system with no antifreeze the Freeze1 R30 resistor is set to 26 F.

### Does my FHP use E1/E2 error codes like an air-source heat pump?

No. FHP water-source and geothermal units count LED blinks on the control board (blink codes 1-6 on the UPM, or codes 1-5 on the older EM015). E-code style displays (A/E/F codes) belong to Bosch air-source and IDS split systems, which are a different product line with different controls.
