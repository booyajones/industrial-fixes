---
title: "York YSC Rooftop Unit Error Codes Guide"
description: "Complete York YSC series rooftop unit error codes. Covers all E-codes, P-codes, and flash codes with technician-level diagnostic steps."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - york
  - rooftop-unit
  - commercial-hvac
---

# York YSC Rooftop Unit Error Codes: Complete Guide

The York YSC series is a light commercial packaged rooftop unit covering 2–12.5 tons. Fault codes are displayed via the LED on the IFC board (flash codes) and alphanumeric codes on the optional diagnostic panel or communicating thermostat.

## York YSC Flash Code Table

| Flash Count | Fault | Common Cause |
|---|---|---|
| 1 flash | System lockout | Manual reset required |
| 2 flashes | Low-pressure switch open | Low refrigerant, dirty filter |
| 3 flashes | High-pressure switch open | Dirty condenser, fan failure |
| 4 flashes | Limit switch open | Airflow restriction |
| 5 flashes | Rollout switch open | Heat exchanger issue |
| 6 flashes | Ignition lockout | Gas, igniter, or sensor fault |
| 7 flashes | Flame sense fault | Dirty or failed flame sensor |
| 8 flashes | Pressure switch stuck closed | Faulty pressure switch |
| 9 flashes | Reverse rotation — blower | Blower wired incorrectly or failed |

## York YSC Alphanumeric Fault Codes

| Code | Description | Likely Cause / Action |
|---|---|---|
| E1 | Control board communication fault | Check wiring harness, replace board |
| E2 | Supply air temperature sensor fault | Check sensor resistance, replace |
| E3 | Return air temperature sensor fault | Check or replace return sensor |
| E4 | Outdoor air temperature sensor fault | Check or replace outdoor sensor |
| E5 | Discharge temperature sensor fault | Check sensor at compressor discharge |
| E6 | High-pressure switch lockout — circuit 1 | Check condenser coil, fan, refrigerant |
| E7 | High-pressure switch lockout — circuit 2 | Check condenser coil, fan, refrigerant |
| E8 | Low-pressure switch lockout | Check refrigerant charge and airflow |
| E9 | Compressor time delay active | Wait — normal startup protection |
| P1 | Low-ambient compressor lockout | Ambient below minimum — check settings |
| P2 | Low-ambient heating lockout | Ambient too low for heating operation |
| P3 | Brownout / low voltage lockout | Check supply voltage |
| H1 | High humidity lockout | Dehumidification mode — check controls |

## Most Common YSC Faults and Fixes

### E6 / E7 — High-Pressure Lockout
The most frequent YSC summer fault:
1. Check condenser coil — clean if dirty
2. Verify all condenser fan motors are running (check run capacitors)
3. Check refrigerant charge — superheat and subcooling
4. Confirm the high-pressure switch trips correctly (replace if stuck open or failing intermittently)

### Flash 4 — Open Limit Switch
The most frequent YSC heating fault:
1. Replace dirty air filter
2. Confirm all supply grilles are open and unobstructed
3. Check blower motor and run capacitor
4. Test limit switch continuity at room temperature

### E2 / E3 / E4 — Sensor Faults
Temperature sensors on York YSC units have a nominal resistance of 10K ohms at 77°F (25°C). Check resistance with a multimeter and compare to the resistance chart in the service manual.

### Flash 6 — Ignition Lockout
1. Measure gas pressure at manifold: 3.5 in. w.c. natural gas
2. Inspect hot surface igniter for cracks
3. Clean or replace flame sensor
4. Check for combustion air obstructions

## YSC Parts Reference

| Part | Notes |
|---|---|
| [Temperature sensor](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-york-ysc-error-codes&tag=errorcodefixes-20) | 10K thermistor — York part S1-02525919700 |
| [Hot surface igniter](https://www.amazon.com/dp/B00BTLLJ40?ascsubtag=ecf-york-ysc-error-codes&tag=errorcodefixes-20) | Model-specific — check tonnage and model suffix |
| [Flame sensor rod](https://www.amazon.com/s?k=Flame+sensor+rod&tag=errorcodefixes-20) | Measure µA before replacing |
| [High-pressure switch](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-york-ysc-error-codes&tag=errorcodefixes-20) | Check trip pressure setting |
| [Run capacitor](https://www.amazon.com/dp/B01M05L7B3?ascsubtag=ecf-york-ysc-error-codes&tag=errorcodefixes-20) | Check µF on both compressor and fan caps |
| [IFC control board](https://www.amazon.com/s?k=IFC+control+board&tag=errorcodefixes-20) | York part number varies by tonnage |

> **Note:** The York YSC shares many components with the Coleman and Luxaire commercial RTU lines. Parts are interchangeable.

## Related Articles

- [York 2 Flashes Error Code — Causes & Fix](/posts/york-2-flashes-error-code/)
- [York 3 Flashes Error Code — Causes & Fix](/posts/york-3-flashes-error-code/)
- [York 4 Flashes Error Code — Open Limit Device Fix](/posts/york-4-flashes-error-code/)
- [York 5 Flashes Error Code — Causes & Fix](/posts/york-5-flashes-error-code/)
- [York Furnace 6 Flashes Error Code — Pressure Switch Fault Fix](/posts/york-6-flashes-pressure-switch-fault/)

## See Also

- [York YXV Heat Pump Error Codes - Fault Code Reference](/posts/york-yxv-heat-pump-error-codes/)
- [York Affinity Series Packaged Unit Error Codes: Complete Guide](/posts/york-affiniti-error-codes/)
- [York 2 Flashes Error Code — Causes & Fix](/posts/york-2-flashes-error-code/)
- [York 3 Flashes Error Code — Causes & Fix](/posts/york-3-flashes-error-code/)
