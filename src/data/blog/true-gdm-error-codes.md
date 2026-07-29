---
title: "True GDM Error Codes - What It Means and How to Fix It"
description: "True GDM merchandisers use error codes to flag sensor, defrost, fan, and controller problems before product warms up. This guide explains the common codes and the field checks that solve them fastest."
pubDatetime: 2026-04-25T00:00:00Z
author: "James Rutherford"
tags:
  - hvac
  - error-codes
---

True Manufacturing glass door merchandisers — the GDM series — are the most widely deployed reach-in refrigerated cases in commercial foodservice. Walk into any convenience store, gas station, or small grocery and you'll find a True GDM cooling beverages somewhere behind that glass door. When they fail, every minute of downtime puts product at risk.

This guide covers the complete True GDM error code system, what each code means, and what to do about it.

## What Does True GDM Error Codes Mean?

True GDM merchandisers with electronic temperature controllers display error codes on the digital temperature display when they detect a fault condition. The display normally shows the cabinet temperature. When an error occurs, the display flashes an alphanumeric code.

The error code system applies to GDM models equipped with the Ranco ETC or similar electronic controller. Older GDM models with mechanical thermostats don't display error codes — those fail silently (the cabinet temperature just rises).

**Models covered:** GDM-5, GDM-7, GDM-10, GDM-12, GDM-23, GDM-26, GDM-33, GDM-35, GDM-41, GDM-45, GDM-47, GDM-52, GDM-69, GDM-72 (and variants)

---

## How to Fix It — Error Code by Error Code

### E1 — Temperature Sensor Failure (Cabinet Sensor)

**What it means:** The electronic controller has lost communication with the cabinet temperature sensor (thermistor). Either the sensor has failed, the wiring has broken, or the connector has corroded.

**What you see:** "E1" flashing on the display. The compressor may continue to run in a failsafe mode on some models, or it may shut down.

**How to diagnose:**
1. Locate the cabinet temperature sensor — typically mounted on the evaporator coil or in the cabinet air return. On most GDM models, it's a small cylindrical probe with two wires.
2. Disconnect the sensor from the controller wiring harness
3. Using a multimeter set to resistance (ohms), test across the sensor terminals
   - At 32°F (0°C): sensor should read approximately **29,000 ohms** (29kΩ)
   - At 50°F (10°C): approximately **19,600 ohms** (19.6kΩ)
   - At 77°F (25°C): approximately **10,000 ohms** (10kΩ)
   - Open circuit (∞ ohms) or short circuit (0 ohms): sensor has failed — replace it
4. Also check the wiring for breaks, corrosion at connectors, or pinched wires

**Fix:** Replace the thermistor sensor. True part number for most GDM cabinet sensors: **True 800271** (NTC thermistor, 2-wire). Third-party universal NTC thermistors will work if rated to the same resistance values.

**Expected repair time:** 20–30 minutes

---

### E2 — Defrost Sensor / Evaporator Coil Sensor Failure

**What it means:** The defrost termination sensor (the sensor that tells the controller when the evaporator coil has reached defrost completion temperature, typically 50–55°F) has failed or is reading out of range.

**What you see:** E2 on display. If the defrost sensor fails, the controller can't properly terminate defrost cycles — the unit may run defrost too long (overheating the cabinet) or not long enough (leaving ice on the coil).

**How to diagnose:** Same process as E1, but locate the evaporator coil sensor (mounted directly on the evaporator coil fins). Test resistance values against the same table above.

**Fix:** Replace the defrost termination sensor. For most True GDM models, this is the same **True 800271** thermistor or a similar NTC 10kΩ probe. The defrost sensor is often distinguishable because it will have a clip to mount to the evaporator fin, while the cabinet sensor has a probe bracket.

---

### E3 — High Temperature Alarm

**What it means:** The cabinet temperature has exceeded the high-temperature alarm setpoint (typically 10°F above the setpoint, or 45–50°F for a beer cooler set to 35°F). The product is at risk.

**This is a warning, not necessarily a component failure.** E3 can trigger from:
- Heavy customer traffic leaving the doors open
- Blocked evaporator coil (ice buildup from failed defrost)
- Failed condenser fan motor
- Failed evaporator fan motor
- Low refrigerant charge
- Dirty condenser coil
- Compressor failure

**Diagnosis sequence:**
1. Is the condenser fan (outdoor/back of unit) running? If not, check the condenser fan motor and capacitor (if equipped).
2. Is the evaporator fan (inside the cabinet) running? On most True GDM units, you can hear the evaporator fan if you open the door and listen. If it's not running — check the evaporator fan motor.
3. Is the evaporator coil iced over? Open the back panel (if accessible) or remove the interior back panel to inspect the coil. Heavy ice means the defrost system has failed.
4. Is the condenser coil (rear of cabinet) clean? A dirty condenser coil is one of the most common causes of high-temp problems. Clean it with compressed air or coil cleaner.

---

### E4 — Defrost Cycle Duration Exceeded

**What it means:** The defrost cycle has run longer than the maximum allowed time (typically 30–60 minutes, depending on controller settings) without the defrost sensor reaching termination temperature.

**What this indicates:** The defrost heater(s) may have failed and the coil isn't actually defrosting. Alternatively, the coil has so much ice buildup that even a working defrost heater can't reach termination temperature in time.

**How to diagnose:**
1. Check if the defrost heater is energized during defrost. During a defrost cycle (usually 2–4 AM on preset schedules), the heater should be warm to the touch (accessible through the evaporator panel). If it's cold, it has failed.
2. Manually initiate a defrost cycle on the controller (check your model's service manual for the procedure) and monitor.
3. Measure heater resistance with a multimeter (with power off). GDM defrost heaters are typically glass-tube or calrod heaters with resistances of **10–30 ohms** depending on wattage. Open circuit = failed heater.

**Fix:** Replace the defrost heater. Common True GDM defrost heater part: **True 800270** or **True 993289** (varies by model — verify with the serial plate).

---

### E5 — Low Temperature Alarm

**What it means:** The cabinet temperature has dropped below the low-temperature alarm setpoint (typically 10°F below setpoint, or 25°F for a unit set at 35°F). Product may be freezing.

**Causes:**
- Thermostat or controller setpoint is set too low
- Temperature controller has failed and is holding the compressor on continuously
- Defrost control has failed and the unit isn't defrosting, causing ice to block the thermistor and give a false low reading

**Fix:** Check the controller setpoint first. If the setpoint is correct and the cabinet is genuinely too cold, the controller may be failed or the expansion valve may be stuck open. This typically requires a refrigeration technician.

---

### E6 — Controller Communication Fault / EEPROM Error

**What it means:** The temperature controller has detected an internal memory error or communication fault. On networked GDM units, this can also indicate a communication failure with a centralized monitoring system.

**Fix:** First, perform a controller reset: disconnect power for 5 minutes, then restore. If E6 returns immediately, the controller board has failed and needs replacement. True temperature controller replacement part: **True 843009** (Ranco ETC-211000) or the equivalent model-specific controller.

---

## Common Non-Code Failures

### Evaporator Fan Motor Failure

The evaporator fan circulates cold air inside the cabinet. When it fails, the cabinet temperature rises even with a working compressor. You'll often hear the unit run normally but notice the interior feels warm and air isn't moving over the product.

True GDM evaporator fan motors are typically shaded-pole AC motors or EC (electronically commutated) motors on newer models. Common True replacement evaporator fan motor: **True 800452** (multi-speed shaded pole, fits many GDM models).

### Condenser Fan Motor Failure

The condenser fan exhausts heat from the condenser coil. On most True GDM units, it's a small axial fan mounted behind the unit (or underneath on some models). A failed condenser fan causes the unit to run hot, eventually triggering E3 high-temp alarm and potentially the condensing unit high-pressure cutout.

### Door Gasket Failure

A deteriorated door gasket allows warm, humid air to infiltrate the cabinet constantly, overworking the refrigeration system and causing accelerated coil icing. Inspect by running a dollar bill around the door perimeter — it should grip firmly at every point. True GDM door gaskets are model-specific; order by model number.

---

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|--------------|
| [True 800271 NTC Thermistor Sensor](https://www.amazon.com/s?ascsubtag=ecf-true-gdm-error-codes&k=True+800271+thermistor+sensor+refrigerator&tag=errorcodefixes-20) | E1/E2 errors — cabinet or defrost sensor failure | $15–$30 |
| [True GDM Evaporator Fan Motor](https://www.amazon.com/s?ascsubtag=ecf-true-gdm-error-codes&k=True+GDM+Evaporator+Fan+Motor&tag=errorcodefixes-20) | Failed evaporator fan causes high cabinet temperature | $35–$75 |
| [True GDM Condenser Fan Motor](https://www.amazon.com/s?ascsubtag=ecf-true-gdm-error-codes&k=True+GDM+Condenser+Fan+Motor&tag=errorcodefixes-20) | Failed condenser fan causes E3 high-temp and compressor lockout | $30–$65 |
| [True 800270 Defrost Heater](https://www.amazon.com/s?ascsubtag=ecf-true-gdm-error-codes&k=True+800270+Defrost+Heater&tag=errorcodefixes-20) | E4 defrost fault — heater failure causes coil to ice up | $25–$55 |
| [Ranco ETC-211000 Temperature Controller](https://www.amazon.com/s?ascsubtag=ecf-true-gdm-error-codes&k=Ranco+ETC-211000+temperature+controller&tag=errorcodefixes-20) | E6 controller fault or failed temperature control | $45–$85 |
| [Coil Cleaner Commercial No-Rinse](https://www.amazon.com/s?ascsubtag=ecf-true-gdm-error-codes&k=commercial+coil+cleaner+no+rinse+foam&tag=errorcodefixes-20) | Dirty condenser causes E3 high temp alarm and efficiency loss | $15–$25 |

---

## When to Call a Pro

Call a commercial refrigeration technician when:

- The unit has lost refrigerant charge (E3 high-temp with clean condenser, running compressor, and working fans)
- The compressor is not running or is running continuously without cooling
- You need to replace refrigerant, repair a leak, or service refrigerant components
- The unit is under warranty (True provides a 3-year parts, 5-year compressor warranty on new GDM units)

For commercial operators, also consider a refrigeration service contract — proactive maintenance on condenser cleaning, gasket inspection, and controller verification prevents the emergencies.

---

## Frequently Asked Questions

**Q: My True GDM is running but the temperature is higher than the setpoint. No error code is showing. What's wrong?**

A: The most common cause is a dirty condenser coil. The condenser coil is the black heat-rejection coil at the back (or bottom) of the unit. In high-traffic convenience store environments, these get coated with dust and debris rapidly. Clean it with compressed air or coil cleaner every 60–90 days. If the condenser is clean and the unit still won't hold temperature, check the evaporator fan, door gaskets, and refrigerant charge.

**Q: How do I manually initiate a defrost cycle on a True GDM?**

A: The procedure varies by controller. On units with the Ranco ETC controller: press and hold the SET button for 5+ seconds. The display will show "dF" and the defrost cycle starts. On other controllers, check the label inside the control box. Manual defrost is useful for diagnosing whether the defrost heater works and for quickly clearing an iced coil.

**Q: Can I replace the temperature controller myself?**

A: Yes — on most True GDM models, the controller is accessible in the control box (typically at the top of the unit inside the door frame). Disconnect power, note the wiring connections (photograph them), remove the old controller, and install the new one. The Ranco ETC-211000 is a common replacement and comes with wiring instructions. Verify you're ordering the correct controller for your model — GDM-23 and GDM-33 use different controllers.

**Q: My True GDM door sweats on the outside. Is this a refrigeration problem?**

A: Usually not. Condensation on the outside of glass doors is typically a door heater or anti-sweat heater issue. True GDM units have electric anti-sweat heaters built into the door frame to keep the glass above the dew point. If a door heater fails, that section of glass will sweat. On many newer GDM models, these are LED door heaters that are energy-efficient. Check the door heater circuit if only one door is sweating while adjacent doors are clear.
