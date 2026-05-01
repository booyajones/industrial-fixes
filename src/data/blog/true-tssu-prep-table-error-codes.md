---
title: "True TSSU Prep Table Error Codes, Causes, and Fixes"
author: "Industrial Error Code Fixes"
pubDatetime: 2026-04-24T22:10:00Z
modDatetime: 2026-04-24T22:10:00Z
slug: true-tssu-prep-table-error-codes
featured: false
draft: false
tags:
  - "true"
  - prep-table
  - commercial-refrigeration
  - restaurant-equipment
  - error-codes
description: "True TSSU sandwich and salad prep table error codes explained. Diagnose E1, E2, E3, E4, high temperature alarms, and common no-cool faults on one of the most common restaurant prep refrigerators."
---

## Error Codes: True TSSU Prep Tables

**What it means:** True TSSU prep tables, including popular models like the TSSU-27-8, TSSU-48-12, and TSSU-60-16, use an electronic temperature controller that monitors the cabinet sensor, evaporator sensor, and defrost cycle. When the controller loses a sensor signal or sees unsafe temperatures, it shows an error code and may shut the compressor or fans down to protect the equipment.

These prep tables sit on the front line in sandwich shops, pizza kitchens, delis, and fast-casual restaurants. When one goes down, product warms up fast and the line slows down. That makes TSSU fault codes high-intent searches, especially during lunch or dinner rush.

---

## True TSSU Prep Table Fault Code Reference

### E1 — Cabinet Temperature Sensor Fault

The controller is not getting a valid signal from the cabinet air sensor.

**What it means:** The main sensor that tells the controller how cold the cabinet is has gone open, shorted, or drifted out of range.

**Common causes:**
- Failed 10k NTC cabinet thermistor
- Sensor wire rubbed through near the evaporator cover or controller housing
- Moisture in the connector causing unstable resistance
- Controller input failure, less common than a bad sensor

This is the same basic issue covered in the broader [True Refrigeration E1 guide](/posts/true-refrigeration-e1-error-code/), but prep tables see it more often because kitchen staff open the lid and doors constantly and wash the unit down more aggressively.

### E2 — Evaporator Sensor Fault

The evaporator coil sensor is open, shorted, or reading outside the expected range.

**What it means:** The controller cannot tell how cold the evaporator is, so it cannot manage defrost timing or prevent coil icing accurately.

**Common causes:**
- Failed evaporator thermistor clipped to the coil
- Sensor wire pinched during a prior service call
- Ice buildup pulling the sensor loose from the coil
- Corroded harness connector inside the evaporator section

### E3 — Condenser or Auxiliary Sensor Fault

On many True prep table controllers, E3 indicates a third probe fault, usually tied to condenser temperature, discharge temperature, or an auxiliary product sensor depending on controller version.

**What it means:** The controller has lost the extra sensor input it uses to monitor performance.

**Common causes:**
- Failed condenser probe on newer energy-efficient TSSU models
- Broken harness near the machine compartment
- Grease contamination in the connector block
- Wrong replacement sensor installed after prior repair

### E4 — Defrost Termination Fault

The controller did not see the evaporator reach the expected temperature during defrost, or the defrost sensor signal was invalid.

**What it means:** The unit cannot complete a normal defrost cycle, so frost builds on the coil and airflow drops.

**Common causes:**
- Failed defrost sensor
- Burned out defrost heater on freezer or low-temp variants
- Evaporator completely iced over from a door left open
- Defrost relay or controller failure

### HI or High Temperature Alarm

The cabinet stayed warmer than its setpoint for too long.

**Common causes:**
- Dirty condenser coil
- Door gasket leaking warm kitchen air
- Evaporator fan motor not running
- Lid left open during prep rush
- Low refrigerant charge
- Overloaded pans blocking airflow from the rail to the cabinet

### LO or Low Temperature Alarm

The cabinet dropped below the normal operating range.

**Common causes:**
- Sensor out of calibration
- Stuck contactor or welded relay keeping compressor on too long
- Product sensor placed incorrectly
- Controller settings changed during prior service

---

## Common Causes on True TSSU Prep Tables

- **Dirty condenser coil:** This is the number one real-world failure on TSSU units. Prep tables sit low to the floor and pull flour, grease, cardboard dust, and kitchen lint straight into the condenser. Once head pressure climbs, cooling capacity falls fast.
- **Blocked airflow from overfilled pans:** Staff often load pans above the fill line or leave rail openings uncovered. That dumps warm air into the cabinet and forces longer run times.
- **Door and drawer gasket leaks:** Prep tables get hit hard all day. Torn gaskets let humid air in, which causes frost on the evaporator and leads to E2, E4, and high temperature alarms.
- **Sensor damage during cleaning:** Staff pull pans, wipe aggressively, and sometimes snag or soak thermistor connections. That creates intermittent E1 and E2 faults.
- **Evaporator icing after long lid-open periods:** During busy shifts, the top stays open and fans pull kitchen humidity onto the coil. Once airflow drops, the table warms up and the controller begins logging faults.

---

## Step-by-Step Fix {#step-by-step-fix}

1. **Write down the code and the model number.** TSSU-27-8, TSSU-48-12, and TSSU-60-16 use similar logic, but parts can differ. Read the controller code before cycling power.

2. **Clean the condenser first.** Remove the front grille. Brush and vacuum the condenser coil completely. On kitchen prep tables, this fixes a large share of HI alarms and performance complaints.

3. **Check actual cabinet temperature.** Put a calibrated thermometer in a cup of glycol or water inside the cabinet for 10 minutes. Compare that reading to the controller display. If they disagree badly, suspect E1 or a drifting cabinet sensor.

4. **Test the cabinet and evaporator sensors.** Disconnect each thermistor and measure resistance with a multimeter. Most True sensors are 10k NTC at 77°F. If one reads open, shorted, or far off compared to the temperature chart, replace it.

5. **Inspect the sensor routing.** Look for rubbed insulation where the harness passes through metal panels or near the evaporator cover. Moisture and vibration kill these wires over time.

6. **Open the evaporator cover if you have E2 or E4.** If the coil is packed in ice, thaw it fully before further diagnosis. A solid block of ice points to a failed sensor, gasket leak, fan issue, or defrost problem.

7. **Check evaporator fan operation.** Fans should run during the cooling cycle on most configurations. If the fan is stalled or noisy, airflow across the coil drops and the table warms even if the compressor still runs.

8. **Inspect door gaskets and rail practices.** Replace torn gaskets. Make sure staff keep pan covers on when possible and do not overfill ingredient pans above the rail line.

9. **Check for low refrigerant only after airflow and sensor issues are ruled out.** A clean condenser, working fans, and good sensors with weak cooling usually point to a leak, weak compressor, or restricted metering device.

10. **Replace the controller last.** Controller failures happen, but bad sensors and dirty condensers are far more common. Confirm the inputs before you buy an electronic board.

---

## Parts Often Needed {#parts-often-needed}

| Part | Notes | Typical Cost | Where to Buy |
|------|-------|--------------|--------------|
| Cabinet temperature sensor | Verify controller family and sensor curve | $20–$45 | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?tag=errorcodefixes-20) \| Parts Town |
| Evaporator sensor | Clips to coil, common E2 fix | $20–$45 | [Amazon](https://www.amazon.com/s?k=True+evaporator+sensor+prep+table&tag=errorcodefixes-20) \| Parts Town |
| Evaporator fan motor | Common after icing or washdown damage | $65–$140 | [Amazon](https://www.amazon.com/dp/B01N0J3ZEH?tag=errorcodefixes-20) \| Parts Town |
| Door gasket | Match exact TSSU model and door size | $55–$110 | [Amazon](https://www.amazon.com/dp/B0FPF84HQP?tag=errorcodefixes-20) \| Parts Town |
| Condenser fan motor | Needed when head pressure runs high | $70–$150 | [Amazon](https://www.amazon.com/dp/B0D2L5NSMM?tag=errorcodefixes-20) \| Parts Town |
| Replacement controller | Use exact OEM cross-reference | $140–$260 | [Amazon](https://www.amazon.com/s?k=True+refrigeration+controller+prep+table&tag=errorcodefixes-20) \| Parts Town |
| Coil cleaning brush and condenser cleaner | Low-cost first repair step | $15–$35 | [Amazon](https://www.amazon.com/s?k=commercial+refrigerator+coil+cleaner+brush&tag=errorcodefixes-20) |

---

## When to Call a Professional

Call a refrigeration technician if the prep table still runs warm after you clean the condenser, confirm the fans work, and test the sensors. At that point the likely causes shift to refrigerant leaks, a restricted cap tube, or compressor problems. Any sealed-system repair requires EPA 608 certification, proper recovery equipment, and leak testing. You should also call for service if product temperature rises above food-safe levels, because a prep table can drift out of compliance fast during a busy shift.

> **Pro tip:** If your TSSU table cools fine overnight but warms up during service, look at workflow before you condemn parts. Overfilled pans, a lid that stays open, and a condenser packed with flour create that exact pattern.

---

## See Also

- [True Refrigeration E1 Error Code](/posts/true-refrigeration-e1-error-code/)
- [True Refrigeration E2 Error Code](/posts/true-refrigeration-e2-error-code/)
- [True Refrigeration E3 Error Code](/posts/true-refrigeration-e3-error-code/)
- [True Refrigeration E4 Error Code](/posts/true-refrigeration-e4-error-code/)
- [True T-23 Error Codes](/posts/true-t-23-error-codes/)
- [True T-49 Error Codes](/posts/true-refrigeration-t49-error-codes/)
- [Commercial Refrigerator Error Codes](/posts/commercial-refrigerator-error-codes/)

## Related Articles

- [True Refrigeration E1 Error Code — Causes & Fix](/posts/true-refrigeration-e1-error-code/)
- [True Refrigeration E2 Error Code — Causes & Fix](/posts/true-refrigeration-e2-error-code/)
- [True Refrigeration E3 Error Code — Causes & Fix](/posts/true-refrigeration-e3-error-code/)
- [True Refrigeration E4 Error Code — Causes & Fix](/posts/true-refrigeration-e4-error-code/)
- [True Refrigeration E5 Error Code — Defrost Sensor Causes & Fix](/posts/true-refrigeration-e5-error-code/)
