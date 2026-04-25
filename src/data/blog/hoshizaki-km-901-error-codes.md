---
title: "Hoshizaki KM-901 Error Codes - What They Mean and How to Fix Them"
description: "The Hoshizaki KM-901 ice machine displays fault codes E1 through E8 when it detects a problem — this guide explains each code, how to diagnose the cause, and what parts to order."
pubDatetime: 2026-04-25T00:00:00Z
tags: [hvac, error-codes, hoshizaki, ice-machine, commercial-refrigeration]
---

## What Does a Hoshizaki KM-901 Error Code Mean?

The Hoshizaki KM-901 is a commercial modular ice machine that produces crescent-shaped ice using an evaporator plate and refrigerant system. When the control board detects an abnormal condition, it flashes an error code on the LED indicators and stops ice production.

The KM-901 uses a single-digit error system (E1–E8) displayed via LED blink codes on the control board, or on a remote display panel if one is installed. Understanding these codes is the difference between a 20-minute fix and an unnecessary service call.

The KM-901 produces approximately 901 lbs of ice per 24 hours under AHRI standard conditions (70°F ambient, 50°F water). Real-world output is lower in warmer kitchens. If the machine is producing less ice than expected without throwing an error code, that's a different set of diagnostics — this guide focuses on fault codes specifically.

---

## All KM-901 Error Codes: E1–E8

### E1 — Freeze Cycle Too Long (Freeze Timeout)
**What it means:** The machine couldn't complete a freeze cycle within the maximum allowed time (typically 60 minutes). Ice isn't forming fast enough on the evaporator.

**Common causes:**
- Low refrigerant charge (most common)
- Dirty air filter or condenser coil (on KM-901MAH air-cooled models)
- High ambient temperature in the equipment room
- Low water supply pressure or flow
- Failed expansion valve

**Fix:**
1. Check ambient temperature — KM-901 requires ambient temps below 100°F (air-cooled) or below 110°F (water-cooled).
2. Clean the air filter and condenser coil — use compressed air or a coil cleaning solution.
3. Verify water supply pressure is 20–80 PSI.
4. If environment and water are fine, the issue is likely refrigerant — call a technician.

### E2 — Harvest Cycle Too Long (Harvest Timeout)
**What it means:** The machine couldn't complete a harvest cycle (releasing ice from the evaporator) within the allowed time. Ice is stuck on the evaporator or the hot gas valve isn't opening fully.

**Common causes:**
- Failed hot gas solenoid valve
- Low refrigerant charge (too little hot gas to warm the evaporator)
- Harvest thermostat not reading correctly
- Water curtain stuck or damaged (ice can't slide off properly)

**Fix:**
1. Inspect the water curtain — it should swing freely. A stuck or cracked curtain causes E2.
2. Check the harvest thermostat. Part number: **443-3501-01**. It should open at approximately 48°F and close at 32°F.
3. Listen for the hot gas solenoid valve clicking when the harvest cycle starts. If silent, the valve or its coil may have failed.
4. If the evaporator appears clear of ice but E2 persists, the refrigeration system needs a technician.

### E3 — High Refrigerant Pressure
**What it means:** The high-pressure switch opened, indicating excessive discharge pressure.

**Common causes:**
- Dirty condenser coil or air filter
- Condenser fan motor failure
- High ambient temperature
- Refrigerant overcharge (less common)

**Fix:**
1. Clean condenser coil thoroughly with Nu-Brite or equivalent coil cleaner.
2. Check condenser fan — it should spin freely and run during the freeze cycle.
3. Replace condenser fan motor if failed. Common part: **Hoshizaki 622-2041-01** (verify against your specific model suffix — MAH, MRH, etc.).

### E4 — Low Refrigerant Pressure / Suction Pressure Too Low
**What it means:** The low-pressure safety switch opened. Low suction pressure typically indicates low refrigerant charge (a leak) or a failed metering device.

**Fix:** Stop here. Refrigerant diagnosis requires EPA 608 certification and manifold gauges. Call a certified commercial refrigeration technician.

### E5 — Evaporator Thermistor Fault
**What it means:** The thermistor monitoring evaporator temperature is reading out of range or has an open/shorted circuit.

**Fix:**
1. Locate the evaporator thermistor — it's clipped to the evaporator surface.
2. Disconnect and test resistance with a multimeter: at 32°F it should read approximately 16.3 kΩ; at 77°F approximately 7.5 kΩ.
3. Replace if readings are outside spec. Part number: **Hoshizaki 443-3501-02** (confirm with model).
4. Check the connector at the control board — corrosion on the thermistor connector is a common cause of E5.

### E6 — Drain or Water System Fault
**What it means:** A drain or water level issue — the sump may not be draining correctly or the float valve is stuck.

**Fix:**
1. Check the drain hose for kinks or blockages.
2. Inspect the float valve and clean scale buildup — scale is the #1 cause of E6.
3. Run a cleaning cycle (see below) if the machine has heavy mineral scale.
4. Check the water inlet valve — if scale has plugged the screen, water flow drops and E6 can result.

### E7 — Communication Error (for units with remote display or multiple evaporators)
**What it means:** Communication lost between the main control board and a secondary module or remote display.

**Fix:** Check all wiring connectors between the main control board and any secondary boards or remote panels. Re-seat connectors. If the error persists, the control board or secondary module may have failed.

### E8 — Control Board Fault
**What it means:** The control board has detected an internal fault.

**Fix:**
1. Power cycle the machine — disconnect power for 30 seconds, then restore.
2. If E8 returns immediately, the control board needs replacement.
3. Control board part number varies by model year — check the board itself for a part number label. Common KM-901 control board: **Hoshizaki 2A4334G01** (verify for your suffix).

---

## How to Run a Cleaning Cycle on the KM-901

Scale buildup causes more service calls on the KM-901 than any component failure. Run a cleaning cycle every 6 months (more often in hard water areas).

1. Press and hold the **CLEAN** button for 5 seconds until the cleaning mode light illuminates.
2. Add **Hoshizaki Scale Away** (part **946-2101-04**) or equivalent ice machine cleaner to the water trough.
3. The machine will run a rinse and clean cycle automatically (approximately 70 minutes).
4. Press the **POWER** button at the end of the cycle, then press **ICE** to return to ice production.
5. Discard the first two batches of ice after cleaning.

---

## Parts You May Need

| Part | Why | Approx. Cost |
|------|-----|-------------|
| [Harvest thermostat — Hoshizaki 443-3501-01](https://www.amazon.com/s?k=Harvest+thermostat+%E2%80%94+Hoshizaki+443-3501-01&tag=errorcodefixes-20) | E2 — harvest timeout (stuck ice) | $35–$55 |
| [Evaporator thermistor — Hoshizaki 443-3501-02](https://www.amazon.com/s?k=Evaporator+thermistor+%E2%80%94+Hoshizaki+443-3501-02&tag=errorcodefixes-20) | E5 — thermistor fault | $25–$45 |
| [Water curtain assembly](https://www.amazon.com/s?k=Water+curtain+assembly&tag=errorcodefixes-20) | E2 — ice not releasing (cracked/stuck curtain) | $40–$70 |
| [Condenser fan motor — Hoshizaki 622-2041-01](https://www.amazon.com/s?k=Condenser+fan+motor+%E2%80%94+Hoshizaki+622-2041-01&tag=errorcodefixes-20) | E3 — high pressure from failed fan | $120–$200 |
| [Hot gas solenoid valve — Hoshizaki 422-3541-01](https://www.amazon.com/s?k=Hot+gas+solenoid+valve+%E2%80%94+Hoshizaki+422-3541-01&tag=errorcodefixes-20) | E2 — harvest won't complete | $80–$150 |
| [Control board — Hoshizaki 2A4334G01](https://www.amazon.com/s?k=Control+board+%E2%80%94+Hoshizaki+2A4334G01&tag=errorcodefixes-20) | E8 — internal board fault | $300–$550 |
| [Scale Away cleaner — Hoshizaki 946-2101-04 (1 qt)](https://www.amazon.com/s?k=Scale+Away+cleaner+%E2%80%94+Hoshizaki+946-2101-04+%281+qt%29&tag=errorcodefixes-20) | Preventive cleaning, E6 | $15–$25 |
| [Float valve assembly](https://www.amazon.com/s?k=Float+valve+assembly&tag=errorcodefixes-20) | E6 — water level fault | $30–$60 |
| [Water inlet valve](https://www.amazon.com/s?k=Water+inlet+valve&tag=errorcodefixes-20) | E6 — restricted water flow | $40–$80 |

Always verify part numbers against your specific KM-901 model suffix (KM-901MAH, KM-901MRH, etc.) before ordering. Hoshizaki parts are available through authorized distributors including Parts Town, Wasserstrom, and KaTom.

---

## When to Call a Pro

- **E4 (low pressure) or E1/E2 persisting after cleaning and environment check:** These require manifold gauge readings — refrigerant work is EPA-regulated.
- **E8 (control board fault) that doesn't clear on power cycle:** Board replacement is straightforward, but diagnosing what caused the failure requires a technician — a failed component downstream can blow a new board.
- **Any refrigerant-related diagnosis:** KM-901 uses R-404A or R-448A depending on manufacture date. Both require EPA 608 certification to handle.
- **Health-critical situations:** Commercial ice machines are food service equipment. If there's any chance of contamination (mold, unusual odors, discolored ice), stop production and call a pro — this is a food safety issue, not just a repair.

---

## Frequently Asked Questions

**Q: How do I clear an error code on the Hoshizaki KM-901?**

Most error codes clear automatically once the machine is power cycled and the underlying issue is resolved. Press the power button to turn the machine off, wait 30 seconds, then press ICE to restart. If the code returns within one cycle, the problem is still active.

**Q: My KM-901 shows E2 on every harvest cycle in summer but not in winter. Why?**

This is almost always a refrigerant or high ambient temperature issue. As ambient temperature rises in summer, the refrigerant system works harder. If charge is marginally low, the system copes in winter but can't complete harvest in summer because there isn't enough hot gas to warm the evaporator. Have a technician check refrigerant charge.

**Q: How often should I clean the KM-901?**

Hoshizaki recommends every 6 months, but in areas with hard water (above 10 grains per gallon), every 3–4 months is better. Scale buildup is the single biggest cause of reduced ice output and E6 faults. Nickel-plated evaporator models are more scale-resistant but still need regular cleaning.

**Q: What's the difference between the KM-901MAH and KM-901MRH?**

MAH = air-cooled head, MRH = remote condenser (condensing unit is installed remotely, often on the roof). The fault codes are the same, but E3 (high pressure) diagnostics differ — on the MRH, you're inspecting a remote condenser, not an integral one. The hot gas valve and harvest thermostat are the same across both configurations.

**Q: Can I use generic ice machine cleaner instead of Hoshizaki Scale Away?**

Yes, as long as it's nickel-safe. Hoshizaki's evaporators are nickel-plated, and some aggressive cleaners can damage the plating and void the warranty. Check that any cleaner you use is labeled safe for nickel-plated evaporators. Hoshizaki's own 946-2101-04 is the safest choice.

## Related Articles

- [Hoshizaki C-101BAH / C-201BAH Countertop Ice Maker Error Codes — Full Fault Guide](/posts/hoshizaki-c-101bah-error-codes/)
- [Hoshizaki DKM-500 Cube Dispenser Error Codes — Fault Code Diagnostic Guide](/posts/hoshizaki-dkm-500-error-codes/)
- [Hoshizaki Ice Machine E1 Error Code — Water Inlet Fix](/posts/hoshizaki-e1-error-code/)
- [Hoshizaki E2 Error Code — Harvest Fault Fix](/posts/hoshizaki-e2-error-code/)
- [Hoshizaki E3 Error Code — Causes & Fix](/posts/hoshizaki-e3-error-code/)
