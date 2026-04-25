---
title: "True T-49 Refrigerator Error Codes - What They Mean and How to Fix Them"
description: "True T-49 refrigerator error codes E1 through E6 indicate sensor and refrigeration system faults — this guide covers every code, what it means, and the exact steps to diagnose and fix each one."
pubDate: 2026-04-25
heroImage: /images/hvac-error-codes.jpg
category: hvac
tags: [hvac, error-codes, true-refrigeration, commercial-refrigerator]
---

## What Does a True T-49 Error Code Mean?

The True T-49 is a two-section commercial reach-in refrigerator — a staple in restaurant kitchens and food service operations. The T-49 series uses a microprocessor controller (the Ranco or True-branded ETC controller, depending on production year) that monitors temperature sensors throughout the cabinet.

When a sensor fails, reads out of range, or when the refrigeration system can't maintain temperature, the controller throws an error code on the digital display. In some T-49 models, the display alternates between the set point and the error code. In others, the error code replaces the temperature readout entirely.

**Not all T-49 units use the same controller.** True has used multiple controller generations. Older units may use simple setpoint controllers that don't display codes — they just show temperature. This guide covers T-49 units with the digital controller that displays E1–E6 (primarily units with ETC-200 and equivalent controllers).

---

## All T-49 Error Codes: E1–E6

### E1 — Cabinet Temperature Sensor Fault

**What it means:** The primary cabinet air temperature sensor (also called the box sensor or return air sensor) is reading outside its acceptable range or has an open/shorted circuit. The controller can't read cabinet temperature.

**Symptoms:** Display shows E1 or alternates between the set temperature and E1. The unit may continue running the compressor since it can't verify temperature, or it may shut down depending on the controller configuration.

**Fix:**
1. Locate the cabinet temperature sensor — it's typically clipped inside the cabinet, often at the return air duct near the evaporator.
2. Disconnect and test resistance with a multimeter. NTC thermistor sensors typically read approximately 10 kΩ at 77°F (25°C). At refrigerator temperature (35°F / 2°C), expect approximately 25–32 kΩ. Confirm against your controller's specification sheet.
3. Check the wiring connector at both the sensor and the controller board — corrosion and loose pins cause E1 far more often than actual sensor failure.
4. Replace if readings are out of spec. True part number for common cabinet sensor: **800441** (verify for your production year).

### E2 — Evaporator Coil Temperature Sensor Fault

**What it means:** The evaporator temperature sensor (coil sensor or defrost termination sensor) is out of range or has failed. This sensor tells the controller when the evaporator is fully defrosted.

**Symptoms:** E2 code on display. The unit may get stuck in defrost mode (if the controller can't confirm defrost completion, it may run defrost indefinitely) or skip defrost entirely.

**Fix:**
1. Find the evaporator sensor — it's clipped directly to the evaporator coil fins, often near the center of the coil.
2. Test resistance same as E1. At 32°F (0°C), evaporator sensors typically read 16–20 kΩ.
3. Check for ice bridging on the coil — a coil heavily iced over can push the sensor out of position or hold it against ice instead of the coil surface.
4. If the coil is iced up, run a manual defrost first. On most T-49 controllers: press and hold the defrost button for 5 seconds.
5. Replace sensor if readings are out of spec. Part number varies — common evaporator sensor: **800442** (verify).

### E3 — Condenser Temperature Sensor Fault

**What it means:** The condenser temperature sensor (if equipped) is reading out of range. Not all T-49 models have a condenser sensor — older units and simpler configurations may not use one.

**Fix:**
1. Verify your T-49 has a condenser sensor — check the wiring diagram on the inside of the service panel.
2. If the sensor is present: locate it (typically mounted on the condenser coil or discharge line), disconnect, and test resistance.
3. Check wiring for damage from the condenser fan or any heat sources.
4. Replace if faulty.

### E4 — High Temperature Alarm

**What it means:** The cabinet temperature has risen above the high-temperature alarm threshold (set in the controller, often 50°F or the set point plus 10°F). This is a temperature alarm, not necessarily a sensor fault — the cabinet is genuinely too warm.

**Common causes:**
- Door gaskets failing or doors left open
- Dirty condenser coil restricting airflow
- Failed condenser fan motor
- Failed evaporator fan motor
- Low refrigerant charge
- High ambient temperature overloading the system

**Fix:**
1. Check door gaskets — press a dollar bill between the door and the frame and pull. If it slides out easily, the gasket has failed.
2. Clean the condenser coil — pull the unit from the wall, remove the condenser cover, and clean the coil with compressed air or a vacuum.
3. Verify both the evaporator fan and condenser fan are running.
4. If fans are running and the coil is clean, check refrigerant charge — call a tech.

### E5 — Low Temperature Alarm

**What it means:** Cabinet temperature dropped below the low-temperature alarm threshold. Less common than E4, but it happens when the unit is overcooling — usually a thermostat or controller calibration issue, a stuck open expansion valve, or a refrigerant overcharge.

**Fix:**
1. Verify the set point is correct — make sure it's set for the intended temperature (typically 35–38°F for a refrigerator).
2. If the set point is correct and the cabinet is actually below freezing, check the expansion valve and refrigerant charge. Call a tech.

### E6 — Defrost Fault / Defrost Timer Fault

**What it means:** The defrost cycle failed to complete within the allowed time, or the defrost heater circuit has a fault. The evaporator is likely heavily iced up.

**Common causes:**
- Failed defrost heater
- Failed defrost thermostat (hi-limit thermostat)
- Failed defrost timer or control board
- Evaporator heavily iced from a prior defrost system failure

**Fix:**
1. Check whether the evaporator coil is visibly iced over — if yes, run a manual defrost.
2. Test the defrost heater: disconnect and measure resistance. A glass tube heater should read 20–100 ohms depending on wattage. An open circuit means the heater is burned out.
3. Test the defrost thermostat (hi-limit). It should be closed (continuity) at normal operating temperatures and open above approximately 140°F. If it's stuck open, defrost current can't flow.
4. Replace heater or thermostat as needed.

---

## How to Access Manual Defrost on the T-49

To manually initiate defrost: **press and hold the SET button for 5 seconds** on most ETC-200 controllers. The display will show "dEF" or similar. The unit will run a defrost cycle and automatically return to normal operation when the evaporator sensor signals completion.

If manual defrost won't terminate (the unit stays in defrost indefinitely), the evaporator sensor (E2) or hi-limit thermostat is the likely cause.

---

## Parts You May Need

| Part | Why | Approx. Cost |
|------|-----|-------------|
| [Cabinet temperature sensor — True 800441](https://www.amazon.com/s?k=Cabinet+temperature+sensor+%E2%80%94+True+800441&tag=errorcodefixes-20) | E1 fault — primary box sensor | $20–$40 |
| [Evaporator temperature sensor — True 800442](https://www.amazon.com/s?k=Evaporator+temperature+sensor+%E2%80%94+True+800442&tag=errorcodefixes-20) | E2 fault — defrost termination sensor | $20–$40 |
| [Defrost heater (model-specific)](https://www.amazon.com/s?k=Defrost+heater+%28model-specific%29&tag=errorcodefixes-20) | E6 — burned out heater | $40–$90 |
| [Defrost hi-limit thermostat — True 800239](https://www.amazon.com/s?k=Defrost+hi-limit+thermostat+%E2%80%94+True+800239&tag=errorcodefixes-20) | E6 — stuck open thermostat | $15–$30 |
| [Door gasket (per door)](https://www.amazon.com/s?k=Door+gasket+%28per+door%29&tag=errorcodefixes-20) | E4 — warm cabinet from bad seal | $35–$75 |
| [Condenser fan motor — True 800267](https://www.amazon.com/s?k=Condenser+fan+motor+%E2%80%94+True+800267&tag=errorcodefixes-20) | E4 — condenser not rejecting heat | $60–$120 |
| [Evaporator fan motor — True 800258](https://www.amazon.com/s?k=Evaporator+fan+motor+%E2%80%94+True+800258&tag=errorcodefixes-20) | E4 — no airflow through evaporator | $40–$80 |
| [ETC-200 controller](https://www.amazon.com/s?k=ETC-200+controller&tag=errorcodefixes-20) | Control board failure | $80–$150 |

True Manufacturing parts are available through Parts Town, KaTom, and Wasserstrom. Always verify part numbers against your T-49's serial number and production date — True has made the T-49 since the 1990s and component specifications have changed across generations.

---

## When to Call a Pro

- **E4 with clean condenser and working fans:** Refrigerant leak or charge issue — requires manifold gauges and EPA 608 certification.
- **E5 (overcooling) that doesn't resolve with set point adjustment:** Expansion valve or refrigerant system issue.
- **E6 recurring after defrost heater replacement:** If the heater keeps failing, something is wrong with the defrost control logic or the refrigeration system is creating more ice than the heater can clear.
- **Any refrigerant-related diagnosis:** True T-49 uses R-290 (propane refrigerant) in newer units and R-134a in older units — always verify before servicing. R-290 requires specific safety training and approved tools.

---

## Frequently Asked Questions

**Q: What refrigerant does the True T-49 use?**

It depends on the production year. T-49s built after approximately 2014 use R-290 (propane) refrigerant. Older units use R-134a. Check the data plate on the back of the unit or inside the compressor compartment. R-290 is highly flammable and requires specially trained technicians — don't attempt to service the refrigerant circuit on an R-290 unit without proper training.

**Q: My True T-49 shows a temperature number, then briefly flashes E1. Is that bad?**

Yes — that alternating display pattern means the controller is detecting a sensor fault but is still able to run based on the last known reading or a default value. The sensor is marginal — either failing or has a loose connection. Don't wait for it to fail completely. Check the sensor connection now.

**Q: How do I reset the error codes on a True T-49?**

Most error codes clear automatically once the underlying problem is fixed and the sensor reads correctly. For temperature alarms (E4, E5), the alarm clears once the cabinet returns to normal temperature range. If a code persists after repair, power cycle the unit: unplug for 30 seconds, then plug back in.

**Q: True T-49 showing E4 but the cabinet feels cold. What's happening?**

The cabinet may be warm near the top or in dead-air zones even if it feels cold near the center. Also, E4 can be triggered by a sensor that's not properly positioned — if the cabinet sensor is sitting against the coil instead of in the return air stream, it reads too cold while the actual cabinet air is warm. Verify sensor placement.

**Q: Can I replace the ETC-200 controller with a universal temperature controller?**

You can, but it's not recommended for a commercial unit that needs to meet health code. The ETC-200 is configured for True's specific sensor types and defrost parameters. A universal controller requires reconfiguration and may not support the same alarm features. If cost is a concern, an OEM ETC-200 replacement from True's parts suppliers runs $80–$150 — comparable to a quality universal controller but plug-and-play.
