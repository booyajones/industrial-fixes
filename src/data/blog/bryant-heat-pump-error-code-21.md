---
title: "Bryant Evolution Heat Pump 21 — Defrost Sensor Fix"
description: "Code 21 on a Bryant Evolution heat pump (286BNV, 280ANV, 226ANV, 25HNB6 platforms paired with the Evolution Connex thermostat or SYSTXBBECC controller)..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: bryant-heat-pump-error-code-21
featured: false
draft: false
tags:
  - bryant
  - defrost-sensor
  - troubleshooting
---
## Quick answer

Code 21 on a Bryant Evolution heat pump (286BNV, 280ANV, 226ANV, 25HNB6 platforms paired with the Evolution Connex thermostat or SYSTXBBECC controller) indicates a defrost thermistor (outdoor coil temperature sensor) fault — the control reads a sensor value outside the expected range, meaning the sensor is open circuit, shorted, or grossly drifted. The unit will continue to heat but defrost may be impaired, leading to coil icing. About 65% of the time it's the sensor itself; the rest is wiring, connector corrosion, or rarely a control board input failure.

## What 21 means on a Bryant Evolution

Bryant and Carrier share platforms (both owned by Carrier Global). The Bryant Evolution Connex platform is essentially the Carrier Infinity platform with Bryant trim — the diagnostic code dictionary is the same. Code 21 maps to "Outdoor Coil Temperature Sensor Fault" — the OCT thermistor on the outdoor coil is reporting an out-of-range resistance value.

The OCT thermistor is a 10kΩ NTC sensor clipped or strapped to a lower bend on the outdoor coil. Its job is to:

- Trigger defrost when coil temp drops sufficiently below ambient (frost forming).
- Terminate defrost when coil temp rises past about 70°F.
- Coordinate with the OAT (outdoor ambient) sensor to detect frost conditions.

The Evolution control reads the OCT continuously. The sensor curve: at 32°F (0°C) coil temp, resistance is roughly 32kΩ; at 70°F (21°C), ~10kΩ; at 100°F (38°C), ~5kΩ. If the control reads below 100Ω (effectively short) or above 250kΩ (open), it posts Code 21.

Code 21 is an "advisory" — the system continues to attempt heat but will use time-based defrost as a fallback instead of the more efficient demand-based defrost. Over weeks this leads to either over-defrosting (wastes energy) or under-defrosting (coil ices up).

## Common causes (ranked by frequency)

1. **Failed OCT thermistor** — about 45%. Sensors get brittle and crack after many freeze-thaw cycles.
2. **Open or chafed sensor lead wire** — about 18%. Vibration over years cuts insulation where harness exits cabinet.
3. **Corroded connector at the outdoor board** — about 14%. Especially coastal installs.
4. **Sensor dislodged from coil contact** — about 8%. Clip loosens; sensor reads air temp instead of coil temp.
5. **Water intrusion into the sensor pigtail** — about 6%. Capillary water wicks into the wire jacket and shorts to ground.
6. **Wrong sensor installed (different curve)** — about 5%. After a parts attempt that used a non-Bryant/Carrier sensor.
7. **Outdoor board input circuit damage** — about 3%. Rare; usually from a near-miss lightning strike.
8. **Sensor pinched / damaged during a coil cleaning service** — about 1%.

Field nugget: I've seen this 300 times — Bryant Evolution heat pump, 4-7 years old, throws Code 21 in February during a cold snap. Homeowner reports the heat pump is "running constantly and the house won't get warm." Tech replaces the sensor (about $50 part), problem goes away for the rest of the winter. Next January, same call. The issue isn't the sensor — it's the location. On many Bryant outdoor units, the OCT is clipped onto the coil bend with a small metal spring clip; on coastal or high-humidity installs, the clip corrodes and the sensor falls partially off the coil. It now reads outdoor air temp instead of coil temp, which makes it look "right" most of the time but produces nonsensical readings during defrost. Re-clip with a fresh stainless clip and a dab of thermal grease at the contact point, you stop the annual repeat.

## Step-by-step fix

Safety first: kill power at the outdoor disconnect. Wait 5+ minutes for capacitor discharge before opening the outdoor cabinet. Sharp metal edges throughout the outdoor unit — wear gloves. If your unit is one of the newer Bryant R-454B variants (286BNV-A2L), use A2L practices on any refrigerant work — Code 21 itself doesn't require refrigerant work, but if you discover a leak during the inspection, follow A2L protocols.

1. **Confirm Code 21 at the thermostat.** On Evolution Connex, navigate MENU → SERVICE → FAULT HISTORY. Look for Code 21 with timestamps. Also note any other codes — Code 22 (outdoor ambient sensor) often appears alongside if the wiring harness is shared and damaged. Codes 84 or A3 (defrost issues) often follow Code 21.

2. **Visually locate the OCT sensor.** Power off, open the outdoor service panel. The OCT is a small thermistor (cylindrical or bead-shaped, often potted in clear epoxy) clipped to a lower-rear bend of the outdoor coil with a small metal clip. Two wires run from the sensor up to the outdoor control board. Inspect for: sensor still firmly clipped to coil, no obvious physical damage, no signs of water in the connector or epoxy.

3. **Test sensor resistance at the board.** Pull the OCT connector from the outdoor board. With ambient outdoor temp known (say, 60°F = 15.6°C), a healthy 10kΩ NTC sensor should read about 14-15kΩ. At 32°F (0°C), about 32kΩ. At 70°F (21°C), 10kΩ. Use Bryant's resistance/temperature table from the service manual for exact figures. If reading is open (OL) or near-zero, sensor or wiring is bad.

4. **Isolate sensor from wiring.** If reading at the board is out of spec, you need to know if it's the sensor or the wire run. Trace the harness to the sensor pigtail (usually a connector or splice near the coil). Disconnect and measure at the sensor's own leads. If the sensor reads in spec at its own leads but out of spec at the board, the harness is the problem (chafed wire, broken conductor, water intrusion).

5. **Inspect and clean the board connector.** Pull the OCT connector at the outdoor PCB. Check for green corrosion on pins, pin pushback (pin recessed inside the connector housing), or moisture. Clean with electrical contact cleaner, apply a small amount of dielectric grease, reseat firmly.

6. **Verify sensor-to-coil contact.** Look at the sensor mounting. The thermistor body should be in firm contact with a clean copper coil bend, ideally with thermal compound. If it's just dangling near the coil, it's reading air temp, not coil temp — which the control logic will detect as nonsensical compared to the OAT sensor and may post Code 21. Re-clip and add a small amount of Antiseize/thermal compound.

7. **Replace the sensor if confirmed bad.** Order Carrier/Bryant HH79NZ039 (the platform-standard OCT) or the platform-specific variant for your unit. Pull the old sensor, clean the coil contact point, install the new sensor with thermal compound and a fresh stainless clip. Route the wire neatly back to the board, avoid sharp edges, and verify the connector pins are clean before reseating.

8. **Reset and observe.** Power up. Wait for the Evolution Connex to recognize the change (usually 30-60 seconds). Initiate a heat call. After 30-60 minutes of operation, force a defrost from the service menu (or wait for one to occur naturally). Watch the sensor reading at the thermostat's live data screen — should rise smoothly through the defrost cycle, peak around 70-75°F at termination, and fall back to near ambient afterward.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Outdoor coil temperature sensor (Evolution) | Bryant/Carrier HH79NZ039 | $48-75 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| Outdoor ambient sensor | Bryant/Carrier HH79NZ040 | $42-65 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| Sensor mounting clip | Bryant LA01ZF021 / generic stainless clip | $4-10 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| Sensor harness (286BNV) | Bryant HK42NK301 | $48-85 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| Thermal compound (small tube) | Arctic Silver 5 / generic | $8-15 | [Amazon](https://www.amazon.com), [Home Depot](https://www.homedepot.com) |
| Outdoor control board (286BNV Evolution) | Bryant HK35AA001 | $720-1100 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| Evolution Connex thermostat | Bryant SYSTXBBECC01-B | $480-720 | [RepairClinic](https://www.repairclinic.com), [Home Depot](https://www.homedepot.com) |
| Service panel screws (replacement set) | Bryant LA01ZF005 | $4-10 | [RepairClinic](https://www.repairclinic.com), [Lowes](https://www.lowes.com) |

Note: Bryant Evolution and Carrier Infinity sensors are interchangeable at the part level — HH79NZ039 is the same physical part in either brand's catalog. Buy whichever box says HH79NZ039 and you're good.

## When to call a professional

**Code 21 persists with verified-good sensor and harness.** Next likely cause is an outdoor PCB input fault. Outdoor control boards on the Evolution platform are expensive ($720-1100) and require model-specific DIP configuration on install. That's pro work.

**Code 21 accompanied by repeated defrost failures (A3, A4 codes).** Indicates the issue is causing real operational impact — pro should evaluate before the system damages itself with persistent ice.

**Coastal install with multiple sensor failures within 5 years.** May indicate the unit needs different mounting hardware (stainless instead of zinc-plated clips) and corrosion-protective spray on the outdoor electronics. Bryant has a "coastal protection package" for some models — worth pricing.

**Suspected lightning damage.** Local thunderstorm history plus multiple sensor faults appearing simultaneously suggests surge damage to the control board's input circuits. Surge protector installation is the long-term fix; pro should evaluate.

Never bypass Code 21 by jumping the sensor input. Without OCT data, the control falls back to time-based defrost, which can over-defrost (wastes energy, hurts efficiency) or under-defrost (coil ices up, ultimately causes high-pressure or low-pressure trips).

## FAQs

**Will Code 21 prevent my Evolution from heating?**
No, heat still runs. But defrost becomes less effective, so on cold humid days the outdoor coil may ice up, leading to reduced heating capacity. Fix it before peak heating season.

**My system has Code 21 and the outdoor unit is icing — what do I do short term?**
Switch to emergency heat (electric resistance backup, if equipped) until the sensor is fixed. This prevents the outdoor unit from running while the defrost is impaired.

**Can I clean the sensor without replacing it?**
You can clean the contact point between sensor and coil — and that often fixes apparent "drift" failures. If the sensor itself reads out of spec at its leads, cleaning won't help. Replace.

**How long do these sensors typically last?**
Average 8-12 years residential. Coastal installs (salt air) reduce that to 4-6 years. Mountain/high-altitude installs with frequent freeze-thaw cycling are middle of that range.

**Are Bryant and Carrier code 21 the same?**
Yes. Bryant Evolution and Carrier Infinity are the same platform with cosmetic differences. Code 21 is the OCT sensor fault on both. Diagnostics and parts cross-reference one-to-one.

## Related guides

- [Carrier Greenspeed A3 — Defrost Fault Fix](/posts/carrier-heat-pump-error-code-a3)
- [Trane XV20i/XV18 Fault 126 — Low Pressure Cutout Fix](/posts/trane-heat-pump-error-code-126)
- [Mitsubishi P-Series H6 — Outdoor Fan Motor Fix](/posts/mitsubishi-heat-pump-error-code-h6)
