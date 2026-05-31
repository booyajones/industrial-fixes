---
title: "Lennox ResolvePlus Rooftop Unit Error Codes: Complete Guide"
description: "Lennox ResolvePlus RTU error codes and fault diagnostics. Covers flash codes, communicating system faults, and technician-level troubleshooting."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-05-01T08:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - hvac
  - lennox
  - rooftop-unit
  - commercial-hvac
---

# Lennox ResolvePlus Rooftop Unit Error Codes

Lennox ResolvePlus packaged rooftop units use a flashing LED diagnostic system on the integrated control board. The control stores up to 5 fault codes in memory. For units with Lennox communicating thermostats (iComfort), fault codes display as numeric codes directly.

## ResolvePlus Fault Code Table

| Code | Fault Description | Common Cause | Action |
|------|------------------|--------------|--------|
| 111 | Pressure switch fault | Blocked inducer, failed switch | Measure flue pressure |
| 114 | Limit switch open | Dirty filter, blocked return | Replace filter, check airflow |
| 125 | Ignition failure | Low gas, weak igniter | Check gas pressure and igniter |
| 204 | High-pressure switch open | Dirty condenser coil | Wash coil, check fan operation |
| 223 | Low-pressure switch open | Low refrigerant charge | Check charge, inspect TXV |
| 225 | Freeze fault | Low airflow or refrigerant | Check filter and evaporator coil |
| 231 | Discharge temperature high | Refrigerant issue, condenser fan | Inspect condenser fan motors |
| 327 | Communication fault | Wiring issue to communicating thermostat | Check communication wiring |
| 332 | Blower motor fault | Failed ECM motor or VFD | Check motor for proper operation |
| 411 | Flame sensor fault | Dirty or failed flame sensor | Clean sensor, measure ┬╡A |
| 412 | Inducer motor fault | Failed inducer motor | Check inducer amp draw |
| 432 | Gas valve fault | Failed gas valve | Check 24 VAC at valve |
| 540 | Loss of communication | Communication board or wiring | Inspect communication connections |

## Most Common ResolvePlus Faults

### Code 114 — Limit Switch Open
Check the air filter first. ResolvePlus units are sensitive to static pressure — a dirty filter or blocked return can trip the limit at low ambient temperatures. Verify blower motor speed matches installed ESP.

### Code 125 — Ignition Failure
Check inducer operation before gas pressure. If the inducer doesn't prove, the gas valve won't open. Verify inducer pressure switch closes (typically -0.30 to -0.45 in. w.c.).

### Code 204 — High-Pressure Switch
On R-410A units, high-side pressure above 590 psi trips the HP switch. Wash the condenser coil, verify condenser fan rotation and amp draw.

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| Integrated control board | [Amazon](https://www.amazon.com/s?k=Integrated+control+board&tag=errorcodefixes-20) \| Must match unit model |
| Flame sensor | [Amazon](https://www.amazon.com/s?k=Flame+sensor&tag=errorcodefixes-20) \| Measure ┬╡A before replacing |
| Inducer motor | [Amazon](https://www.amazon.com/dp/B00FDZ90B2?ascsubtag=ecf-lennox-resolve-plus-error-codes&tag=errorcodefixes-20) \| Check capacitor first |
| Limit switch | [Amazon](https://www.amazon.com/dp/B0BN3TRG9R?ascsubtag=ecf-lennox-resolve-plus-error-codes&tag=errorcodefixes-20) \| Match temperature rating |
| ECM blower motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lennox-resolve-plus-error-codes&k=ECM+blower+motor&tag=errorcodefixes-20) \| Check motor module and control board |
> **Pro tip:** Lennox ResolvePlus fault history is accessible via the field diagnostic tool or iComfort interface. Always retrieve fault history before clearing codes to identify intermittent problems.

## Related Articles

- [Lennox Error Code 292 — Ignition Failure Fix](/posts/lennox-292-error-code/)
- [Lennox EL296V Error Codes — Variable-Speed Furnace Diagnostic Guide](/posts/lennox-el296v-error-codes/)
- [Lennox Elite Series Furnace Error Codes — Fault Code Diagnostic Guide](/posts/lennox-elite-series-furnace-codes/)
- [Lennox 103 Error Code — Causes & Fix](/posts/lennox-error-code-103/)
- [Lennox Error Code 111 — Causes & Fix](/posts/lennox-error-code-111/)

## See Also

- [Lennox SL280UHV Error Codes — Complete Fault Code Diagnostic Guide](/posts/lennox-sl280uhv-error-codes/)
- [Lennox Healthy Climate Error Codes — Complete Guide](/posts/lennox-healthy-climate-error-codes/)
- [Lennox Error Code 224 — HSI Relay Failure Fix](/posts/lennox-error-code-224/)
- [Lennox Error Code 332 — Causes & Fix](/posts/lennox-error-code-332/)
