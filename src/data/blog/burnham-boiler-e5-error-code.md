---
title: "Burnham Boiler E5 Error Code — Causes & Fix"
description: "What Burnham boiler error code E5 means, why a sensor fault occurs, and how to diagnose and fix the temperature sensor."
pubDatetime: 2026-04-22T11:00:00Z
modDatetime: 2026-04-22T11:00:00Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - boiler
  - burnham
---

## Burnham Boiler E5 Error Code — What It Means

E5 on a Burnham boiler indicates a sensor fault. Depending on the specific Burnham model and control type, E5 typically points to a problem with the water temperature sensor (supply, return, or outdoor reset sensor) or the flue temperature sensor. The boiler control cannot read a valid temperature and shuts down to prevent operating without accurate feedback — which could allow the boiler to overheat or fail to meet setpoints safely.

[Jump to Fix](#fix)

## Common Causes

- **Failed NTC thermistor** — The temperature sensor has drifted out of specification or failed open/short. This is the most common cause of E5.
- **Loose or corroded sensor connector** — The sensor plug at the control board or the immersion well has vibrated loose or developed oxidation that increases contact resistance.
- **Damaged sensor lead wire** — The wire from the immersion sensor to the control board has been chafed against a hot surface, pinched, or broken.
- **Faulty control board sensor input** — The analog input circuit on the boiler control board has failed, reading the sensor as out of range even when the sensor is good.

## Step-by-Step Fix {#fix}

1. **Identify which sensor the E5 fault references** — Consult your Burnham boiler's installation and operating manual. E5 may reference the supply sensor, return sensor, or outdoor sensor depending on the control model. The fault code detail is often in the manual's diagnostic table.
2. **Inspect the sensor and connector** — Locate the referenced sensor on the boiler. Check that the connector is fully seated and that there is no corrosion on the pins. Unplug and re-seat the connector firmly.
3. **Measure sensor resistance** — Disconnect the sensor from the board and measure resistance with a multimeter. Compare to the resistance-temperature table in the service manual. For most Burnham NTC sensors, resistance at 68°F (20°C) is approximately 10–12 kΩ. An open (OL) or very low reading confirms failure.
4. **Inspect the sensor wire** — Trace the wire from the sensor to the board. Look for insulation damage near heat sources or pipe clamps. Repair any damage with high-temperature rated wire.
5. **Replace the faulty sensor** — Order the replacement sensor for your Burnham model. Insert the immersion sensor into the sensor well with heat-transfer compound and reconnect the wiring.
6. **Check the outdoor sensor if equipped** — If your system has an outdoor reset sensor and the E5 is associated with it, check the outdoor sensor and its wiring for the same faults.
7. **Reset the system** — Restore power and verify E5 is cleared. Confirm the boiler fires and reaches setpoint temperature normally.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Supply water temperature sensor (NTC) | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-burnham-boiler-e5-error-code&tag=errorcodefixes-20) \| Match to Burnham control model; immersion type most common |
| Outdoor reset sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-burnham-boiler-e5-error-code&k=Outdoor+reset+sensor&tag=errorcodefixes-20) \| Only if fault references outdoor sensor input |
| Sensor wiring harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-burnham-boiler-e5-error-code&k=Sensor+wiring+harness&tag=errorcodefixes-20) \| Replace if insulation is damaged near heat source |
| Boiler control board | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?ascsubtag=ecf-burnham-boiler-e5-error-code&tag=errorcodefixes-20) \| Replace only if sensors test good and fault persists |
## When to Call a Pro

If the replacement sensor does not clear E5 and the wiring is confirmed intact, the control board likely has a failed input. A Burnham-authorized service technician can perform a full board-level diagnostic and confirm correct replacement parts.

## Related Articles

- [American Water Heater Error Codes — Complete Guide](/posts/american-water-heater-error-codes/)
- [AO Smith Water Heater 3 Flashes — What It Means and How to Fix It](/posts/ao-smith-water-heater-3-flashes/)
- [AO Smith Water Heater 4 Flashes — What It Means and How to Fix It](/posts/ao-smith-water-heater-4-flashes/)
- [A.O. Smith Water Heater Error Codes Guide](/posts/ao-smith-water-heater-error-codes/)
- [Bradford White Water Heater Error Code 1 — Pilot Outage Fix](/posts/bradford-white-error-code-1/)
