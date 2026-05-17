---
title: "True T-23 Refrigerator Error Codes — Fault Code Diagnostic Guide"
description: "Complete guide to True T-23 commercial refrigerator error codes, diagnostic LED codes, common fault causes, and step-by-step repair procedures."
pubDatetime: 2026-04-22T23:00:00Z
modDatetime: 2026-04-22T23:00:00Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - refrigeration
  - true-refrigeration
  - commercial-refrigeration
---

## True T-23 Refrigerator Error Codes — What They Mean

The True T-23 is a one-section reach-in commercial refrigerator widely used in bars, restaurants, and foodservice operations. It is part of True's T-series line — one of the most common commercial refrigerators in service in North America. Older T-23 models used analog temperature controls with no error codes. Newer T-23 units equipped with the True Digital Control (TDC) system display error codes on the temperature readout display when a fault is detected.

[Jump to Fix](#fix)

## True T-23 Digital Control Error Code Reference

| Code | Fault |
|---|---|
| E1 | Ambient temperature sensor fault |
| E2 | Cabinet temperature sensor fault — top |
| E3 | Cabinet temperature sensor fault — bottom (where equipped) |
| E4 | Evaporator coil temperature sensor fault |
| E5 | Defrost sensor fault |
| E6 | High temperature alarm — cabinet above setpoint |
| E7 | Door open alarm — door held open beyond time limit |
| E8 | Defrost cycle timeout — defrost took too long |
| EE | Control board fault |

## Common Causes by Code

- **E1 — Ambient sensor** — The ambient temperature sensor is mounted near the condenser. It is used by the controller to adjust defrost timing and fan operation. If it reads out of range, the controller uses default values and triggers E1 as a warning.
- **E2 / E3 — Cabinet sensor** — The cabinet temperature sensors are NTC thermistors mounted in the cabinet interior. A sensor that reads out of range may have a broken lead (from being caught in the door) or have a corroded connector due to moisture inside the cabinet.
- **E6 — High temperature alarm** — The cabinet temperature has risen above the high-temperature alarm threshold (typically 10°F above setpoint). Common causes: door left open, condenser coil fouling, failed evaporator fan motor, or refrigerant undercharge.
- **E8 — Defrost timeout** — The defrost heater is running but the defrost sensor hasn't reached the termination temperature within the maximum defrost time. Cause: failed defrost heater, failed defrost termination thermostat, or heavy ice buildup from a door gasket leak.
- **EE — Board fault** — Power surge damage or moisture intrusion. Check the board for corrosion or burn marks.

## Step-by-Step Fix {#fix}

1. **Check the display** — The True TDC controller displays error codes on the digital temperature readout. Codes that alternate with the temperature reading indicate an active fault. A code shown alone (without alternating) indicates a lockout requiring reset.
2. **For E6 (high temperature)** — Check the condenser coil and fan. The T-23 condenser is at the bottom of the unit — clean it by pulling the unit out and brushing the coil fins. The condenser fan should be blowing air across the coil and out the bottom front grille.
3. **For E8 (defrost timeout)** — Remove the interior back panel to access the evaporator. If the evaporator is encased in ice, the defrost heater has failed or the defrost termination thermostat is not cutting off the heater. Measure heater continuity (cold resistance typically 20–60 Ω).
4. **For E2/E3 (cabinet sensor)** — Disconnect the sensor and measure resistance at room temperature — compare to the NTC curve in the True service manual. If the resistance is open or shorted, replace the sensor. Also inspect the sensor lead for damage in the door hinge area.
5. **For EE (board fault)** — Power cycle the unit by unplugging for 60 seconds. If EE returns, inspect the board for physical damage. Contact True Refrigeration for replacement board part numbers.

## Parts Often Needed

| Part | Notes |
|---|---|
| Cabinet temperature sensor | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-true-t-23-error-codes&tag=errorcodefixes-20) \| True part; check connector type |
| Defrost heater | [Amazon](https://www.amazon.com/dp/B07FVP4CY6?ascsubtag=ecf-true-t-23-error-codes&tag=errorcodefixes-20) \| Matches voltage and wattage |
| Evaporator fan motor | [Amazon](https://www.amazon.com/dp/B01N0J3ZEH?ascsubtag=ecf-true-t-23-error-codes&tag=errorcodefixes-20) \| Shaded pole type; match CFM |
| Defrost termination thermostat | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-true-t-23-error-codes&tag=errorcodefixes-20) \| Check cutout temperature rating |
| Condenser fan motor | [Amazon](https://www.amazon.com/dp/B0D2L5NSMM?ascsubtag=ecf-true-t-23-error-codes&tag=errorcodefixes-20) \| Bottom-mounted; check rotation |
| True Digital Control board | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?ascsubtag=ecf-true-t-23-error-codes&tag=errorcodefixes-20) \| For EE fault; verify power supply first |
## When to Call a Pro

True T-23 refrigerators with refrigerant undercharge require EPA 608 certified technicians for refrigerant service. If the unit is repeatedly tripping high temperature (E6) with a clean condenser and working fans, the issue may be a low refrigerant charge — a technician with manifold gauges should verify system pressures before condemning the compressor.

## Related Articles

- [True Refrigeration E1 Error Code — Causes & Fix](/posts/true-refrigeration-e1-error-code/)
- [True Refrigeration E2 Error Code — Causes & Fix](/posts/true-refrigeration-e2-error-code/)
- [True Refrigeration E3 Error Code — Causes & Fix](/posts/true-refrigeration-e3-error-code/)
- [True Refrigeration E4 Error Code — Causes & Fix](/posts/true-refrigeration-e4-error-code/)
- [True Refrigeration E5 Error Code — Defrost Sensor Causes & Fix](/posts/true-refrigeration-e5-error-code/)
