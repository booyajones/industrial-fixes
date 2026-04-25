---
title: "Carrier Infinity Series 24ACC6 Error Codes — Fault Code Diagnostic Guide"
description: "Complete guide to Carrier Infinity 24ACC6 air conditioner error codes, flash sequences, fault causes, and step-by-step fixes for the most common failures."
pubDatetime: 2026-04-22T23:00:00Z
modDatetime: 2026-04-22T23:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - carrier
  - air-conditioner
  - infinity
---

## Carrier Infinity 24ACC6 Error Codes — What They Mean

The Carrier Infinity 24ACC6 is a high-efficiency single-stage central air conditioner designed to operate within Carrier's Infinity communicating system. It uses a two-speed or variable-speed blower paired with an Infinity touch thermostat and communicates faults through both the thermostat display and a diagnostic LED on the outdoor control board. Flash codes appear when the unit is in standalone (non-communicating) mode; alphanumeric codes appear on the Infinity thermostat in full communicating mode.

[Jump to Fix](#fix)

## Carrier 24ACC6 Error Code Reference

| Code / Flash | Meaning |
|---|---|
| 2 flashes | High-pressure switch open |
| 3 flashes | Low-pressure switch open |
| 4 flashes | Compressor protection active |
| 5 flashes | Outdoor control board fault |
| 6 flashes | Outdoor ambient temperature sensor fault |
| 7 flashes | Discharge line temperature sensor fault |
| 8 flashes | Communication bus fault (Infinity link) |
| 11 flashes | Thermistor fault — outdoor coil sensor |
| Thermostat: 174 | High-pressure trip |
| Thermostat: 175 | Low-pressure trip |
| Thermostat: 178 | Compressor communication fault |
| Thermostat: 179 | Outdoor fan fault |

## Common Causes by Code

- **Code 2 / Error 174 — High pressure** — Dirty condenser coil, failed outdoor fan motor, or refrigerant overcharge. The 24ACC6 uses R-410A and is factory-charged; overcharge usually follows an improper service event.
- **Code 3 / Error 175 — Low pressure** — Refrigerant leak, failed low-pressure switch, or ambient temperature below 40°F without the low-ambient kit installed. Inspect Schrader valves and service port caps — they are common leak points on older units.
- **Code 4 — Compressor protection** — Compressor internal overload or low line voltage. The 24ACC6 compressor overload resets automatically after 20–30 minutes. Check capacitor before suspecting a failed compressor.
- **Code 8 / Error 178 — Communication fault** — Broken Infinity control wire between thermostat, air handler, and outdoor unit. Also triggered by a failed Infinity board or thermostat.
- **Code 11 — Coil thermistor** — The outdoor coil temperature sensor is mounted on the liquid line. Corrosion or a loose connector is the typical cause. Resistance should follow the NTC thermistor curve in the service manual.

## Step-by-Step Fix {#fix}

1. **Check the thermostat display first** — In communicating mode, the Infinity touch thermostat shows alphanumeric fault codes directly. Navigate to System > Diagnostics to view all active and historical alerts.
2. **For Code 2 / high pressure** — Turn the unit off at the thermostat. Inspect the condenser coil for fouling — cottonwood, grass clippings, and pet hair accumulate along the coil base. Flush from inside-out with a garden hose. Confirm the condenser fan is drawing air upward.
3. **For Code 3 / low pressure** — Connect manifold gauges (R-410A). Suction pressure should be 100–115 PSI at 70°F ambient. Low charge requires finding the leak before adding refrigerant. Use an electronic leak detector at service ports, coil connections, and line set fittings.
4. **For Code 8 / communication** — Check the control wire for damage (staples through the wire are a common installation defect). Verify the wire is connected to the correct terminals on all three components. Test voltage at the board.
5. **Clear faults** — Power cycle the outdoor disconnect, wait 30 seconds, and restore power. Monitor for fault recurrence within the first cooling cycle.

## Parts Often Needed

| Part | Notes |
|---|---|
| Run capacitor | [Amazon](https://www.amazon.com/s?k=Run+capacitor&tag=errorcodefixes-20) \| Dual run capacitor for compressor and fan motor |
| Contactor | [Amazon](https://www.amazon.com/s?k=Contactor&tag=errorcodefixes-20) \| Check for pitted or welded contacts |
| Low-pressure switch | [Amazon](https://www.amazon.com/s?k=Low-pressure+switch&tag=errorcodefixes-20) \| Replace if Code 3 persists with correct charge |
| Outdoor coil thermistor | [Amazon](https://www.amazon.com/s?k=Outdoor+coil+thermistor&tag=errorcodefixes-20) \| For Code 11; inexpensive OEM part |
| Infinity control board | [Amazon](https://www.amazon.com/s?k=Infinity+control+board&tag=errorcodefixes-20) \| For persistent Code 5 or communication faults |
| Condenser fan motor | [Amazon](https://www.amazon.com/s?k=Condenser+fan+motor&tag=errorcodefixes-20) \| Confirm correct rotation before condemning |
## When to Call a Pro

Refrigerant work requires EPA 608 certification. Infinity system communication faults can require Carrier Service Advisor software (ICP/SA) to perform advanced diagnostics — this is a dealer-level tool not available to the general public. If the Infinity thermostat is showing fault codes not covered in the standard code list, contact a Carrier factory-authorized dealer.

## Related Articles

- [Carrier 11 Error Code — Causes & Fix](/posts/carrier-11-error-code/)
- [Carrier 12 Error Code — Causes & Fix](/posts/carrier-12-error-code/)
- [Carrier 13 Error Code — Limit Switch Lockout Fix](/posts/carrier-13-error-code/)
- [Carrier 13 Soft Lockout — What's Different from Hard Lockout](/posts/carrier-13-soft-lockout/)
- [Carrier 14 Error Code — Causes & Fix](/posts/carrier-14-error-code/)
