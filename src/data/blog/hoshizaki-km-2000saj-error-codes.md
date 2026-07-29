---
title: "Hoshizaki KM-2000SAJ Ice Machine Error Codes - Full Diagnostic Guide"
description: "Complete Hoshizaki KM-2000SAJ error codes E1 through E8, harvest fault diagnosis, and step-by-step repair guide for this high-capacity ice machine."
pubDatetime: 2026-04-25T00:00:00Z
author: "James Rutherford"
tags:
  - hvac
  - error-codes
---

The Hoshizaki KM-2000SAJ is a high-capacity crescent cube ice machine capable of producing up to 1,929 pounds of ice per day. It's the kind of unit that anchors a hotel bar, a large restaurant, or a hospital food service operation , when it goes down, you feel it immediately in operations. Hoshizaki built the KM-2000SAJ with comprehensive self-diagnostics that communicate failures through a seven-segment LED display on the control board. Understanding these codes cuts diagnosis time from hours to minutes.

## What Does a Hoshizaki KM-2000SAJ Error Code Mean?

The KM-2000SAJ's control board uses "E" codes displayed on the LED panel. The machine also uses indicator lights on the service panel , the combination of the code and the indicator status tells you exactly which component failed and in which operating phase (freeze cycle vs. harvest cycle).

**How to access codes:** Error codes display automatically when a fault is detected. The machine stops, and the code appears on the LED panel. To check stored faults after a power cycle, hold the clean/reset button for 3 seconds and cycle through the fault history using the mode button.

The KM-2000SAJ uses a harvest-by-time system with safety timers. If the freeze cycle or harvest cycle exceeds its time limit, a safety lockout fault activates regardless of whether refrigerant-side conditions look normal.

### Hoshizaki KM-2000SAJ Error Code Reference

**E1 , Ice Thickness Sensor Fault**
The ice thickness (or water level) sensor has either failed or is not detecting the proper ice slab thickness at the expected time in the freeze cycle. The sensor probe is located at the water inlet area and monitors freeze progress. Causes: mineral scale on the probe tip (most common), failed sensor, or wiring fault at the sensor connector.

**Fix:** Descale the sensor probe. Use Hoshizaki's recommended scale remover or a citric acid solution. If the probe is clean and the fault persists, measure resistance between the probe terminals , contact Hoshizaki service documentation for the specific resistance curve at operating temperature.

**E2 , Float Switch Fault (High Water Level)**
The float switch in the water reservoir has detected water above or below normal level for too long. The KM-2000SAJ maintains a precise water level in the sump , too much water dilutes the freeze cycle; too little causes dry-ice issues and pump cavitation. Causes: float switch stuck (scale buildup on float arm), water inlet valve leaking, or drain valve not seating.

**Fix:** Remove the float switch assembly and clean it thoroughly. Verify the water inlet valve closes fully when commanded (no drip). Check the drain valve for debris preventing full closure.

**E3 , High-Side Pressure Fault (High Pressure Lockout)**
The high-side refrigerant pressure has exceeded the safety threshold. On the KM-2000SAJ, this almost always means a condenser-side problem. For the self-contained air-cooled version: dirty condenser coil, failed condenser fan motor, or condenser coil fins blocked with grease (kitchen installations). For water-cooled configurations: inadequate water flow to condenser, water temperature too high, or water regulating valve stuck.

**Fix:** Clean the condenser coil thoroughly. On kitchen installations, use a degreaser safe for aluminum coils. Verify the condenser fan motor (check amperage draw , should be within nameplate specs). For water-cooled units, check condenser water pressure and temperature at inlet.

**E4 , Low-Side Pressure Fault (Low Pressure Lockout)**
The suction side refrigerant pressure dropped below the safety threshold during operation. Causes: low refrigerant charge (leak), expansion valve stuck closed, or extremely low ambient water temperature causing over-subcooling. On the KM-2000SAJ with its large refrigerant circuit, even a small leak causes this code.

**Fix:** This code requires a licensed refrigeration technician. Refrigerant pressure checking, leak detection, and charge adjustment on a commercial R-404A or R-448A system requires EPA Section 608 certification and professional equipment.

**E5 , Freeze Cycle Safety Timeout**
The freeze cycle exceeded the maximum allowed time without completing. The KM-2000SAJ has a programmed time limit for the freeze cycle (typically around 60 minutes depending on production settings). If the slab doesn't reach the required thickness within that window, E5 activates. Causes: low refrigerant charge (slow freeze), water temperature too high (incoming water above 90°F slows freezing), dirty evaporator plate, or failing compressor.

**Fix:** Check incoming water temperature , it should be below 90°F for rated production. Clean the evaporator plate of scale deposits. If freeze cycle consistently runs near the time limit even with clean components and proper water temp, suspect refrigerant charge.

**E6 , Harvest Cycle Safety Timeout**
The harvest cycle (where hot gas or water is used to release the ice slab from the evaporator) exceeded the maximum allowed time. The KM-2000SAJ uses a hot gas harvest. Causes: harvest gas valve stuck or slow to open, low hot gas pressure (low refrigerant), harvest water valve issue (on water-cooled harvest assist models), or ice slab bonded to evaporator from water quality issues.

**Fix:** Check that the harvest gas valve responds (you should hear a click and feel the hot gas line warm up within 30 seconds of harvest initiation). Check water quality , very hard water creates a strong bond between the ice slab and the stainless evaporator plate; increase cleaning frequency.

**E7 , Evaporator Temperature Sensor Fault**
The thermistor monitoring evaporator temperature has failed or reads out of range. On the KM-2000SAJ, the evaporator sensor plays a role in freeze cycle management and harvest initiation timing. A failed E7 sensor causes the machine to run on timer-only logic, which reduces efficiency and ice quality.

**Fix:** Locate the evaporator sensor clipped to the back of the evaporator plate. Inspect the sensor wiring for pinch damage or connector corrosion. Test resistance at ambient temperature , Hoshizaki thermistors are typically 10K NTC type.

**E8 , Inlet Water Temperature Too High / Condenser Water Temperature Too High**
This code activates when the water entering the ice machine (or the condenser cooling water on water-cooled units) is above 90°F. Rated production figures assume 70°F inlet water and 70°F ambient air. At 90°F inlet water, production drops significantly. At temperatures above 90°F, the machine protects itself with E8.

**Fix:** Address the root cause of hot incoming water. Check if the water supply line runs near a heat source. Confirm the building's cold water temperature. For water-cooled units, increase cooling tower efficiency or check for a stuck water regulating valve.

### Quick-Reference Error Code Table

| Code | Fault | Priority |
|------|-------|----------|
| E1 | Ice thickness sensor | Medium , clean probe first |
| E2 | Float switch / water level | Medium , clean float assembly |
| E3 | High refrigerant pressure | High , coil/fan issue |
| E4 | Low refrigerant pressure | High , call technician |
| E5 | Freeze cycle timeout | High , multiple causes |
| E6 | Harvest cycle timeout | High , valve or water quality |
| E7 | Evaporator sensor fault | Medium , sensor replacement |
| E8 | Water too hot | High , source problem |

## How to Fix It

1. **Document the code before resetting.** The KM-2000SAJ stores fault history. Note the code, time of occurrence, and cycle phase (freeze or harvest) before clearing.
2. **Perform a full cleaning.** Many E1, E2, E5, and E6 faults are directly caused by scale and biological buildup. Follow Hoshizaki's recommended cleaning procedure: run Hoshizaki's scale remover, then a sanitizer, per the frequency in the manual (every 6 months minimum, more often in hard water areas).
3. **Check condenser airflow (E3).** The KM-2000SAJ requires minimum clearances around the unit (typically 6 inches on sides, 12 inches on top for the condenser exhaust). Verify the condenser fan runs and verify there's no hot air recirculation (hot condenser exhaust being pulled back into the condenser air inlet).
4. **Verify water supply conditions (E5, E8).** Measure incoming water temperature with a thermometer. Measure water pressure , the KM-2000SAJ requires 20–80 PSI water pressure.
5. **Inspect harvest valve operation (E6).** With the machine in harvest mode, feel the hot gas line leaving the compressor toward the harvest valve , it should feel warm within 30–45 seconds. A cold harvest line means the valve is not opening.
6. **Reset and observe one full cycle.** After any repair, reset the machine and watch one complete freeze-to-harvest cycle. A full cycle on the KM-2000SAJ takes 20–40 minutes. Verify the slab forms, harvests cleanly, and ice drops into the bin.

## Parts You May Need

| Part | Use | Buy on Amazon |
|------|-----|---------------|
| Hoshizaki Scale Remover (32 oz) | Clear scale from E1 sensor, evaporator, float switch | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-hoshizaki-km-2000saj-error-codes&k=hoshizaki+scale+remover+ice+machine+cleaner&tag=errorcodefixes-20) |
| Hoshizaki Sanitizer (Ice Machine Safe) | Sanitize after scale treatment, reduce biological fouling | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-hoshizaki-km-2000saj-error-codes&k=hoshizaki+ice+machine+sanitizer&tag=errorcodefixes-20) |
| Ice Machine Nickel Safety Plate (Evaporator Treatment) | Reduce ice-to-evaporator bonding in hard water areas | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-hoshizaki-km-2000saj-error-codes&k=nickel+safety+plate+ice+machine+evaporator&tag=errorcodefixes-20) |
| 10K NTC Thermistor Sensor | Replace E7 evaporator sensor | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-hoshizaki-km-2000saj-error-codes&k=10k+ntc+thermistor+sensor+commercial+refrigeration&tag=errorcodefixes-20) |
| Ice Machine Float Switch (Universal) | Replace failed float switch for E2 | [Search on Amazon](https://www.amazon.com/s?ascsubtag=ecf-hoshizaki-km-2000saj-error-codes&k=Ice+Machine+Float+Switch+%28Universal%29&tag=errorcodefixes-20) |
| Commercial Condenser Coil Cleaner (Foam) | Deep-clean condenser for E3 faults | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-hoshizaki-km-2000saj-error-codes&k=commercial+condenser+coil+cleaner+foam+hvac&tag=errorcodefixes-20) |

## When to Call a Pro

- **E4 (low pressure)** always requires a licensed commercial refrigeration technician. Refrigerant leak detection and charge adjustment on a commercial R-404A or R-448A system requires specialized equipment.
- **E3 that returns after thorough condenser cleaning.** A failed condenser fan motor, malfunctioning water regulating valve (water-cooled units), or compressor issues require professional service.
- **E5 or E6 that return after cleaning and water quality checks.** Persistent timeout faults after eliminating environmental causes indicate refrigerant circuit or compressor performance issues.
- **Any fault on a unit under Hoshizaki warranty.** Attempting your own repair on a covered unit without authorization can void the warranty.

## FAQ

**Q: How often should I clean the Hoshizaki KM-2000SAJ?**
A: Hoshizaki recommends cleaning every 6 months minimum. In hard water areas (above 15 grains per gallon hardness), clean every 3 months. The KM-2000SAJ produces nearly a ton of ice per day , scale accumulates rapidly at this production level. A water softener or inline scale filter dramatically extends cleaning intervals.

**Q: My KM-2000SAJ shows E5 but the ice looks normal and the machine seems to be producing at normal rates. Should I be concerned?**
A: Yes. E5 means the freeze cycle is just barely completing within the allowed window , you're operating near the edge of the safety envelope. This often means something is marginal: low refrigerant charge, slightly above-normal water temperature, or partial evaporator fouling. Address the root cause before the machine starts consistently failing to complete cycles.

**Q: The KM-2000SAJ produced "soft" or slushy ice before showing E5. What does that indicate?**
A: Soft or slushy ice suggests the freeze cycle is not completing fully , the ice slab isn't fully frozen when harvest initiates. This can precede E5 by days or weeks. It's most commonly caused by low refrigerant charge or incoming water above 85°F. Have refrigerant charge checked by a technician.

**Q: Can I replace the KM-2000SAJ control board myself?**
A: The control board is field-replaceable on the KM-2000SAJ. However, the replacement board may require parameter configuration to match the unit's production settings, refrigerant type, and harvest mode. Hoshizaki-authorized service technicians have the service tool to configure replacement boards. An unconfigured board will produce error codes or incorrect operation.
