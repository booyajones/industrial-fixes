---
title: "Navien NPE-240S Tankless Water Heater Error Codes - Full Fault Guide"
description: "Complete error code guide for the Navien NPE-240S condensing tankless water heater. Covers all fault codes, scale sensor alerts, secondary heat exchanger issues, and step-by-step fixes."
pubDatetime: 2026-04-25T00:00:00Z
author: "James Rutherford"
tags:
  - hvac
  - error-codes
---

The Navien NPE-240S is the flagship model in Navien's NPE-S series of condensing tankless water heaters. With a 199,900 BTU maximum input and a 0.97 UEF rating, it's designed to provide whole-home hot water for large households. It also includes Navien's NaviLink Wi-Fi module, a built-in recirculation pump, and — critically for this guide — a sophisticated diagnostic system with detailed error codes.

The NPE-240S is more technically complex than entry-level tankless units. When something goes wrong, the error codes are specific enough to point directly at the failed component. This guide walks through every code and what to do about each.

## What Does Each NPE-240S Error Code Mean?

### E001 — Ignition Failure

The unit attempted to ignite and could not establish a stable flame within the required time window. It retried the specified number of times and locked out.

**Common causes:** Gas valve not fully open, air in the gas line, low gas pressure, dirty or failed igniter electrode, fouled flame sensor, blocked venting.

### E003 — Ignition Failure During Operation (Flame Loss)

Flame was established but lost during normal operation.

**Common causes:** Low gas supply pressure under load, venting backdraft, failing gas valve that sticks shut mid-cycle, dirty flame sensor causing intermittent signal dropout.

### E004 — False Flame

A flame signal is present when the gas valve should be closed. This is a lockout for safety.

**Common causes:** Shorted flame sensor lead, leaking gas valve, control board fault.

### E010 — Abnormal Air Pressure

The combustion air fan is running but the differential pressure switch indicates incorrect pressure — either too high or too low.

**Common causes:** Blocked intake or exhaust vent, failed inducer motor, disconnected or cracked pressure switch hose, failed pressure switch.

### E011 — Fan Motor Fault

The fan is running but the RPM feedback is out of specification.

**Common causes:** Worn fan bearing, damaged impeller, faulty tachometer signal wire.

### E012 — Exhaust Over-Temperature

Exhaust gases are hotter than the maximum threshold. This usually means venting is restricted or the heat exchanger is scaled.

### E016 — Hot Water Outlet Over-Temperature

The domestic hot water outlet temperature has exceeded the safety limit (typically 185°F).

**Common causes:** Very low flow rate, failed outlet thermistor reading falsely low, heavy scale in the primary heat exchanger.

### E021 — Cold Water Inlet Thermistor Fault

The inlet temperature sensor has failed or is out of range.

### E022 — Hot Water Outlet Thermistor Fault

The outlet temperature sensor has failed or is out of range.

### E046 — Scale Sensor Alert (Secondary Heat Exchanger)

This is unique to condensing Navien models like the NPE-240S. The unit has a scale detection sensor on the secondary (condensing) heat exchanger. E046 fires when scale buildup has reached a threshold that affects efficiency.

**This code means it's time to descale — not that the unit is failed.** However, if ignored, it will progress to E047 or heat exchanger damage.

### E047 — PCB Internal Fault

The main control board has detected an internal error. Can sometimes be cleared with a power cycle; persistent E047 usually means board replacement.

### E060 — Gas Valve Fault

The gas valve circuit has returned an abnormal signal. The valve driver or the valve itself has failed.

### E110 — Domestic Hot Water Temperature Sensor Fault (Outlet High Limit)

The high-limit sensor on the outlet has failed. This is a secondary safety sensor separate from E022.

### E351 — Low Water Pressure

The unit detects water pressure below the minimum threshold (about 15 PSI). The flow switch will not activate.

---

## How to Fix It

### Fixing E001 / E003 — Ignition and Flame Loss

1. **Check gas supply.** Confirm the shut-off valve on the gas line to the unit is fully open. Test another gas appliance in the home. If they work, the supply is likely fine.

2. **Check gas pressure at the unit.** The NPE-240S requires a minimum inlet gas pressure of 3.5 inches WC (natural gas) or 8 inches WC (propane). Use a manometer on the inlet test port. Low pressure under firing demand is a common cause of E003.

3. **Clean the flame sensor.** The sensor rod should be bright metal. Lightly polish it with fine steel wool (do not use sandpaper — too abrasive). A thin oxide layer is enough to block the microamp flame signal.

4. **Inspect and clean the igniter electrode.** Check for cracking in the ceramic insulator, carbon tracking, and proper gap (3–4mm).

5. **Inspect venting.** Check both the PVC intake and exhaust at the exterior termination. Clear any debris, ice, or nesting material.

### Fixing E010 / E011 — Fan Issues

1. Check vent termination for obstruction first.
2. Locate the pressure switch hose (small rubber tubing from the blower housing). Inspect for cracks or disconnection. Reconnect or replace if damaged.
3. Test the pressure switch with a multimeter — it should close when the fan is at full speed. An open switch at full speed = failed switch.
4. If the fan motor is running rough, grinding, or won't reach full RPM, the motor or its bearing is failing. Order by part number from the unit's data label.

### Fixing E046 — Scale Sensor (Descaling Required)

1. Shut off the cold water inlet and hot water outlet valves (or install isolation valves if not present).
2. Connect a submersible pump descaler kit to the service ports.
3. Use 1–2 gallons of undiluted white vinegar or a commercial descaling solution (Calci-Free, Nu-Calgon).
4. Circulate for 45–60 minutes minimum. The secondary heat exchanger on condensing units accumulates calcium carbonate faster than the primary.
5. Flush with clean water for 10 minutes.
6. Restore water flow and power. E046 should clear.

**Note:** If E046 returns within 3–6 months, you have very hard water (above 12 GPH). Install a whole-house water softener or at minimum a dedicated scale inhibitor cartridge on the cold inlet.

### Fixing E021 / E022 — Thermistor Replacement

1. Power off at the breaker.
2. Locate the failed thermistor (inlet thermistor is on the cold manifold; outlet thermistor is on the hot manifold).
3. Test with multimeter — at 68°F, resistance should be approximately 10,000–12,000 ohms. An open or short circuit confirms failure.
4. Disconnect the wiring connector, unscrew the sensor, and install the replacement. Navien uses a standardized NTC sensor; order by Navien part number for a reliable fit.

---

## Parts You May Need

| Part | What It Fixes | Amazon Link |
|------|--------------|-------------|
| Navien NPE Flame Sensor Rod | E001 / E003 ignition/flame issues | [View on Amazon](https://www.amazon.com/s?k=Navien+NPE+Flame+Sensor+Rod&tag=errorcodefixes-20) |
| Navien Igniter Electrode Assembly | E001 ignition failure | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-navien-npe-240s-error-codes&k=navien+npe+igniter+electrode+assembly&tag=errorcodefixes-20) |
| NTC Inlet/Outlet Thermistor (Navien) | E021 / E022 thermistor faults | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-navien-npe-240s-error-codes&k=navien+npe+thermistor+inlet+outlet&tag=errorcodefixes-20) |
| Tankless Descaling Kit with Pump | E046 scale sensor alert | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-navien-npe-240s-error-codes&k=tankless+water+heater+descaler+pump+kit&tag=errorcodefixes-20) |
| Calci-Free Descaling Solution | E046 scale buildup | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-navien-npe-240s-error-codes&k=calci-free+descaling+solution+tankless&tag=errorcodefixes-20) |
| Scale Inhibitor Cartridge (Polyphosphate) | Prevent recurring E046 | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-navien-npe-240s-error-codes&k=polyphosphate+scale+inhibitor+tankless+water+heater&tag=errorcodefixes-20) |
| Navien Condensing Tankless Air Pressure Switch | E010 pressure switch fault | [View on Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-navien-npe-240s-error-codes&tag=errorcodefixes-20) |

---

## Secondary Heat Exchanger — The NPE-240S Differentiator

The NPE-240S and other condensing models in the NPE-S line include a secondary (condensing) heat exchanger that extracts additional heat from exhaust gases. This is what gives the unit its 97% efficiency — but it comes with a maintenance requirement.

The secondary heat exchanger operates at lower temperatures, which means condensate forms inside it constantly. In hard water areas, calcium and magnesium dissolved in that condensate precipitate and coat the heat exchanger fins. This is exactly what the E046 scale sensor detects.

**Signs the secondary heat exchanger is scaling:**
- E046 error code
- Reduced hot water output at full demand
- Longer time to reach set temperature
- Unit running longer burner cycles than usual

Annual descaling prevents these issues entirely. The NPE-240S has service ports specifically for flush descaling — Navien designed it to be serviced without disassembly.

---

## When to Call a Pro

- **E001 persists after cleaning igniter and flame sensor** — gas valve or control board requires licensed gas technician.
- **E060 (gas valve fault)** — gas valve replacement on a condensing unit requires proper commissioning, leak testing, and combustion analysis.
- **E047 (PCB fault) that won't clear** — control board replacement and commissioning require specialized knowledge.
- **Water visible inside cabinet** — condensing units produce significant condensate, but free water near the gas valve or control board is not normal and can be a safety hazard.
- **Unit is producing yellow or orange flame** — shut off the gas and call a technician immediately. This indicates combustion air issues or a heat exchanger crack.

---

## FAQ

**Q: How do I reset the Navien NPE-240S?**
A: Press the Reset button on the front panel. For persistent codes, cycle the breaker off for 60 seconds. The NaviLink app can also send remote resets if Wi-Fi is configured.

**Q: How is the NPE-240S different from the NPE-240A?**
A: The NPE-240S includes a built-in recirculation pump, a scale detection sensor, and a NaviLink Wi-Fi module. The NPE-240A is the standard (non-S) model without these features. Error code systems are similar but the S model has the unique E046 scale code.

**Q: My NPE-240S shows E046 every 6 months. Is this normal?**
A: It means you have hard water. Annual descaling is the manufacturer recommendation. If you're descaling twice a year, install a scale inhibitor on the cold inlet or a whole-house softener.

**Q: Can I use the recirculation pump without a dedicated return line?**
A: Yes — the NPE-240S supports comfort flow (recirculation through the cold water line) using the built-in pump. Set it to demand mode to minimize energy use.

**Q: What is the warranty on the NPE-240S?**
A: Navien provides a 15-year heat exchanger warranty, 5-year parts warranty, and 1-year labor warranty when installed by a licensed contractor and registered within 30 days.

## See Also

- [Navien Error Code E016 — Causes & Fix](/posts/navien-error-code-e016/)
- [Navien NPE Series Error Codes — Tankless Water Heater Fault Guide](/posts/navien-npe-error-codes/)
- [Navien Error Code E010 — Causes & Fix](/posts/navien-error-code-e010/)
- [Navien E009 Error Code — Causes & Fix](/posts/navien-error-code-e009/)
