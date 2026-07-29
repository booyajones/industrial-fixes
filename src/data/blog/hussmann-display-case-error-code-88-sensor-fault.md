---
title: "Hussmann Refrigeration Display Case Error Code 88 — Sensor Fault Fix"
author: "Marcus Webb"
pubDatetime: 2024-03-15T08:00:00Z
modDatetime: 2024-03-15T08:00:00Z
slug: hussmann-display-case-error-code-88-sensor-fault
featured: false
draft: false
tags:
  - refrigeration
  - hussmann
  - display-case
  - grocery
description: "Hussmann refrigeration display case error code 88 means a temperature sensor open circuit fault — here's how to diagnose and replace the NTC sensor."
---

## Error Code: Hussmann Display Case Error Code 88

**What it means:** Error code 88 on Hussmann refrigerated display cases indicates a temperature sensor open circuit fault. The case controller has lost communication with one of its NTC thermistor sensors — most commonly the discharge air temperature sensor, return air sensor, or defrost termination sensor — and cannot read a valid temperature. The display reads "88" (or "- - -" on some controller versions) and the case may continue running in a default mode or alarm continuously.

Hussmann display cases (the P series, R series, and I series merchandisers found in grocery stores and convenience stores) use NTC thermistors throughout the control system. Code 88 is one of the most common service calls in grocery refrigeration because these sensors are exposed to repeated freeze/thaw cycles, moisture, and the vibration of decades of continuous operation.

## Common Causes

- **Open circuit NTC thermistor** — The thermistor's internal resistance element has broken. This is the most common cause. The thermistor measures ambient temperature via a resistance curve; an open circuit reads as infinite resistance, which the controller interprets as a sensor completely out of range and displays 88.
- **Connector corrosion or disconnection** — The 2-pin push-on connector at the sensor or at the controller board has corroded, pulled loose, or been damaged during a defrost or service procedure. The sensor itself may be fine.
- **Chafed or broken sensor lead wire** — The small-diameter wire that runs from the sensor to the controller can be pinched by shelves, cut by wire clips, or broken by vibration at a sharp edge.
- **Controller input failure** — If the sensor and its wiring test good but 88 persists, the controller's sensor input circuit has failed. Less common, but happens on older controllers or after a power surge.
- **Wrong sensor installed during previous service** — A sensor with a different resistance curve (e.g., a 5 kΩ sensor installed where a 10 kΩ is required) will read out of range and may generate 88.

## Step-by-Step Fix {#step-by-step-fix}

1. **Identify which sensor is faulted.** On Hussmann controllers with a display menu, navigate to the sensor status screen (usually Sensor → Readings or Input Status). The display will show which sensor input is reading "open" or "88." Common sensor labels: DA (discharge air), RA (return air), DT (defrost termination), SA (saturation). Note the specific sensor before doing anything else.

2. **Locate the sensor physically.** Discharge air sensors are typically clipped to the evaporator coil outlet or near the case air curtain. Return air sensors mount near the return air grille at case bottom. Defrost termination sensors clip directly to the evaporator coil fins. Each sensor has a small probe (stainless or plastic body, ~3/4" long) with a 2–3 foot lead wire.

3. **Inspect the connector and wiring first.** Pull the sensor connector apart and inspect both sides for green corrosion, bent pins, or broken wire insulation at the crimp. Moisture intrusion during defrost is extremely common in these connectors. If corroded, clean with electrical contact cleaner and reconnect firmly. Pull the wire along its full route looking for any pinch points.

4. **Measure sensor resistance with a multimeter.** Disconnect the sensor from the controller wiring. Set your multimeter to resistance (Ω). Measure across the two sensor leads. The standard Hussmann NTC sensor (part 0528900) measures approximately 10 kΩ at 77°F (25°C). At typical case temperatures (35–38°F), expect approximately 15–20 kΩ. An open circuit reading (OL) confirms the sensor has failed.

5. **Compare against the resistance-temperature curve.** If your reading is in the hundreds of kΩ or millions, the sensor is out of range but not quite open — this can happen with a sensor that was submerged in water and then dried. Still replace it; the drift will worsen.

6. **Replace the sensor.** The Hussmann OEM NTC temperature sensor is part number **0528900** (~$30). It's a universal 10 kΩ NTC probe with a push-on 2-pin connector. Clip the new sensor to the same location as the old one, route the lead wire away from sharp edges and pinch points, and reconnect at the controller.

7. **Navigate to the controller's sensor menu and confirm a valid reading.** After replacement, the controller should immediately read a plausible temperature for the sensor location (e.g., 35–40°F for a discharge air sensor in a running case). If it still reads 88, check the new sensor's connector polarity and re-measure resistance — the connector is non-keyed and can be installed backwards on some controller models, though polarity typically doesn't matter for passive NTC sensors.

8. **Clear the alarm and monitor.** Most Hussmann controllers will clear the 88 fault automatically when a valid sensor reading is restored. If the alarm persists, navigate to the alarm clear menu and acknowledge it manually. Run the case through one full defrost cycle and confirm the defrost termination sensor reads correctly.

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Part Number | Typical Cost | Where to Buy |
|------|------------|-------------|-------------|
| Hussmann NTC Temperature Sensor | 0528900 | $25–$38 | [Search on Amazon](https://www.amazon.com/s?ascsubtag=ecf-hussmann-display-case-error-code-88-sensor-fault&k=Hussmann+NTC+Temperature+Sensor&tag=errorcodefixes-20) \| Parts Town / Amazon |
| Sensor Connector Kit (2-pin) | Generic 2-pin Molex | $5–$10 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-hussmann-display-case-error-code-88-sensor-fault&k=Generic+2-pin+Molex+Sensor+Connector+Kit+%282-pin%29&tag=errorcodefixes-20) \| Amazon / electrical supply |
| Hussmann Case Controller (if board failed) | Model-specific | $250–$450 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-hussmann-display-case-error-code-88-sensor-fault&k=Model-specific+Hussmann+Case+Controller+%28if+board+failed%29&tag=errorcodefixes-20) \| Hussmann dealer / Parts Town |
## When to Call a Professional

If replacing the sensor and verifying wiring doesn't clear the 88 code, and the controller's sensor input circuit has failed, controller replacement is required. On older Hussmann cases, the controller may be discontinued — a refrigeration controls specialist can often cross-reference a compatible aftermarket controller or reprogram a new controller to match the original setpoints. Don't attempt controller replacement without the original setpoint documentation (defrost times, fan delay, alarm thresholds) — incorrect setpoints can cause chronic defrost failures or product loss.

> **Pro tip:** Hussmann 88 faults that reappear within a week of sensor replacement almost always have a wiring issue — not a second bad sensor. Check the wire route carefully for a pinch point at the case shelf rail, which is the most common location for wire damage on Hussmann P series cases. Running new wire through the existing conduit is a 10-minute fix that permanently solves the recurring 88.
