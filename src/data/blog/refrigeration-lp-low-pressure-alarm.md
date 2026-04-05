---
title: "LP Alarm – Commercial Refrigeration Low Pressure Fault"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-01-29T08:00:00Z
modDatetime: 2024-01-29T08:00:00Z
slug: refrigeration-lp-low-pressure-alarm
featured: false
draft: false
tags:
  - refrigeration
  - compressor
  - low-pressure
  - alarm-codes
description: "LP (Low Pressure) alarms on commercial refrigeration systems shut down the compressor to prevent damage. Here's a systematic approach to finding the root cause."
---

## What LP Alarm Means

An **LP (Low Pressure) alarm** on commercial refrigeration equipment — walk-in coolers, reach-in cases, condensing units — indicates the suction pressure dropped below the low pressure cutout (LPCO) setpoint. The compressor shuts off immediately to prevent running in a vacuum, which causes oil loss and bearing damage.

Typical LPCO setpoints:
- **R-404A / R-448A systems:** 10–15 PSIG
- **R-22 systems:** 40–50 PSIG  
- **R-134a systems:** 15–20 PSIG

## Common Causes

### Refrigerant-Side Issues
- **Low refrigerant charge** (leak) — most common cause
- Restricted or clogged filter-drier
- Restricted or failed TXV/EEV (expansion valve)
- Liquid line solenoid valve stuck closed

### Load-Side Issues
- Excessive frost buildup on evaporator coils (poor defrost)
- Evaporator fan motor failure (no airflow over coil)
- Blocked evaporator air intake or discharge

### Ambient / Mechanical Issues
- Very low ambient temperature causing compressor to pull down too fast
- Defrost cycle ending with suction pressure not recovering

## Diagnostic Steps

1. **Check the sight glass.** Bubbles in the sight glass on a properly charged system indicate low refrigerant. A solid liquid line with bubbles = low charge or restriction upstream.

2. **Measure suction pressure at the service port.** Compare to manufacturer saturation tables for the actual return air temperature. Suction pressure should correspond to a temperature 10–20°F below return air temp.

3. **Check superheat.** Attach a clamp thermometer to the suction line near the evaporator. Calculate superheat = suction line temp - saturation temp at suction pressure. Normal superheat: 8–12°F for TXV, 10–20°F for fixed orifice. High superheat = starved evaporator (low charge or restricted TXV).

4. **Inspect evaporator.** A heavily frosted coil restricts airflow and drops suction pressure. Initiate a manual defrost and let coil clear before re-evaluating.

5. **Check TXV operation.** Pinch the bulb with your hand to warm it — the valve should open and suction pressure should rise. If no change, TXV may be stuck or have a lost charge.

6. **Pull a refrigerant charge log.** If the system required charging within the last 12 months, you have a leak. Perform a leak search with electronic detector before recharging.

## Clearing the Alarm

Most controllers (Danfoss AK, Dixell, Emerson EC): the LP alarm auto-resets after a set number of minutes once pressure recovers. If the compressor tripped on the LPCO switch (manual reset type), locate the switch on the compressor suction service valve and press the reset button.

> **Do not simply reset and restart** without diagnosing root cause. Repeated low-pressure operation destroys compressor oil viscosity and leads to early compressor failure.
