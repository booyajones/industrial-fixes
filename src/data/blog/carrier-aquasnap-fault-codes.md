---
title: "Carrier AquaSnap Fault Codes: 30RB/30RQ Alarm List & Fixes"
description: "Real Carrier AquaSnap 30RB/30RQ chiller alarm codes from the Pro-Dialog manual: TH, Pr, P and compressor faults, likely causes, and how to fix each."
pubDatetime: 2026-04-22T21:00:00Z
modDatetime: 2026-04-22T21:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - chiller
  - carrier
  - aquasnap
  - hvac
money_part: "Condenser fan motor"
---

## Carrier AquaSnap Chiller Fault Codes — Quick Reference

Carrier AquaSnap 30RB (air-cooled liquid chiller) and 30RQ (heat pump) use the Pro-Dialog+ or i-Vue controller. Alarms appear as codes with descriptions on the controller display.

| Alarm Code | Meaning | Quick Fix |
|-----------|---------|-----------|
| A1 — Low Pressure | Suction pressure safety | Check refrigerant charge and evap flow |
| A2 — High Pressure | Discharge pressure safety | Check fans and condenser coil |
| A3 — Low LWT | Leaving water temp below limit | Check flow and freeze protection |
| A4 — Compressor Overload | Compressor motor tripped | Check current, voltage, and contacts |
| A5 — High Discharge Temp | Compressor discharge too hot | Check charge and condenser |
| A6 — Loss of Flow | Chilled water flow lost | Check pump, filter, and flow switch |
| A7 — Loss of Phase | Phase loss detected | Check electrical supply |
| A8 — High Motor Temp | Compressor thermal protection | Check voltage and cooling |

## Most Common Faults

### A1 — Low Pressure Alarm
Low refrigerant suction pressure is the top alarm on AquaSnap chillers. Check chilled water flow rate first — a closed pump valve, blocked strainer, or pump failure causes the evaporator to starve. If flow is confirmed, check the refrigerant charge.

### A2 — High Pressure Alarm
High discharge pressure trips are common in summer. Check: all condenser fans are running (visually verify), condenser coil is clean, and ambient temperature is within the unit's rating. 30RB units use multiple fans — if one fan fails, high pressure can follow on hot days.

### A6 — Loss of Flow
The flow switch in the evaporator has opened. Check: pump breaker, pump rotation (check at VFD if applicable), strainer, and flow switch condition. A dirty flow switch can give false trips.

## Pro-Dialog+ Controller Navigation

- **ALARM** button → shows active alarms and history
- **STATUS** button → live operating data (pressures, temperatures, current)
- **SETPOINTS** → operating limits configuration

## i-Vue Controller

The i-Vue touchscreen shows alarm icons in the top bar. Tap the icon to see fault description. The event history shows the last 200 events with timestamps.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Condenser fan motor | [Amazon](https://www.amazon.com/dp/B0D2L5NSMM?ascsubtag=ecf-carrier-aquasnap-fault-codes&tag=errorcodefixes-20) \| Replace on A2 high pressure faults |
| Flow switch | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-carrier-aquasnap-fault-codes&k=Flow+switch&tag=errorcodefixes-20) \| Replace on repeated A6 faults |
| Refrigerant charge | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-carrier-aquasnap-fault-codes&k=Refrigerant+charge&tag=errorcodefixes-20) \| After leak repair |
| High pressure switch | [Amazon](https://www.amazon.com/dp/B013IHQ8CU?ascsubtag=ecf-carrier-aquasnap-fault-codes&tag=errorcodefixes-20) \| Replace if repeatedly tripping |
## Jump to Fix

- **A1 low pressure** → Check chilled water flow → Check refrigerant charge → Inspect evap
- **A2 high pressure** → Verify all fans running → Clean condenser coil
- **A6 loss of flow** → Check pump → Inspect strainer → Test flow switch

## When to Call a Pro
Carrier (Carrier Commercial Service) handles refrigerant work and compressor replacement. Call 1-800-379-6484 for service support.

## Related Articles

- [Carrier 11 Error Code — Causes & Fix](/posts/carrier-11-error-code/)
- [Carrier 12 Error Code — Causes & Fix](/posts/carrier-12-error-code/)
- [Carrier 13 Error Code — Limit Switch Lockout Fix](/posts/carrier-13-error-code/)
- [Carrier 13 Soft Lockout — What's Different from Hard Lockout](/posts/carrier-13-soft-lockout/)
- [Carrier 14 Error Code — Causes & Fix](/posts/carrier-14-error-code/)

## See Also

- [Carrier 21 Error Code — Gas Heating Lockout Fix](/posts/carrier-21-error-code/)
- [Carrier Infinity Zoning System Error Codes — Complete Guide](/posts/carrier-infinity-zoning-error/)
- [Carrier Infinity Error Code 179 — What It Means and How to Fix It](/posts/carrier-infinity-error-179/)
- [Carrier 24 Error Code — Causes & Fix](/posts/carrier-24-error-code/)

## More Carrier Aquasnap fault codes

Compiled from manufacturer service manuals and authorized documentation.

| Code | What it means | Likely cause | How to fix |
| --- | --- | --- | --- |
| TH-01 | Sensor fault, fluid entering the water heat exchanger (entering-water thermistor) | Defective or disconnected entering-water thermistor, or a wiring/connector fault | Inspect the entering-water thermistor and its harness/connector, measure its resistance against the sensor temperature table, and replace the thermistor if it reads out of range. Resets automatically once a valid reading returns. |
| Pr-01 | Discharge pressure transducer fault, circuit A | Defective discharge pressure transducer or a wiring/supply-voltage signal out of range | Check the circuit-A discharge transducer wiring and connector and verify supply voltage; replace the transducer if the signal stays out of range. Auto-resets when voltage normalizes. |
| Pr-04 | Suction pressure transducer fault, circuit A | Defective suction pressure transducer or wiring signal out of range | Inspect the suction transducer and its harness; replace the transducer if the reading is invalid. Auto-resets when the signal returns to range. |
| P-01 | Water heat exchanger frost protection | Low or lost chilled-water flow, or a defective leaving-water thermistor | Restore full evaporator flow first: open isolation valves, clean the strainer, and confirm the pump is running and prime. Then verify the leaving-water thermistor before restarting. |
| P-14 | Water flow control and customer interlock fault | Evaporator pump defect or water flow switch fault (loss of flow or an open interlock contact) | Check the pump breaker and rotation, clean the strainer, and test the flow switch and any customer interlock contact for continuity. A dirty or sticking flow switch causes false trips. Manual reset. |
| P-16 | Compressor A1 not started or no pressure increase | Wiring/connection problem, failed contactor, or a compressor that will not build pressure | Verify compressor power, contactor pull-in, and wiring; confirm the compressor actually runs and builds discharge pressure. Manual reset. |
| P-28 | Control box thermostat or phase reversal detected | Control box poorly ventilated/overheated, phase reversal on the supply, or a poor electrical connection | Check phase sequence and the incoming supply, confirm control-box ventilation and the box thermostat, and tighten electrical connections. Auto-resets when the contact closes. |


## How to troubleshoot Carrier Aquasnap

## How to work an AquaSnap 30RB/30RQ alarm

Carrier AquaSnap chillers with Pro-Dialog+ or i-Vue controls report faults as alphanumeric codes grouped by system: **TH-** (thermistor/sensor), **Pr-** (pressure transducer), **Co-** (board communication), **P-** (process/operating faults), and **C1-C4** (per-compressor faults with a numeric subcode). Every code in the controller carries a reset type (automatic vs manual) and a probable cause in the manual, so read the full code text on the ALARM screen before acting rather than reacting to the category alone.

**Check flow before charge.** The most common shutdowns on these units — frost protection (P-01), flow/interlock (P-14), and low-pressure trips — are almost always a water-side problem, not a refrigerant problem. Confirm full chilled-water flow first: open isolation valves, clean the evaporator strainer, verify the pump runs and is primed, and test the flow switch (a sticking or fouled switch causes intermittent false trips). Only after flow is proven should you investigate refrigerant charge or the leaving-water thermistor.

**High-pressure and compressor faults skew seasonal.** High-pressure switch trips (compressor subcode 03) and high-discharge conditions cluster on hot days. Verify the condenser coil is clean and every condenser fan is spinning — on multi-fan 30RB units a single failed fan motor can drive a circuit into a high-pressure lockout when ambient is high. For compressor motor-temperature and motor faults, check voltage balance, current draw, and contactor operation before assuming the compressor itself is bad.

**Auto-reset vs manual reset.** Sensor and transducer faults (TH-, Pr-) generally self-clear when a valid signal returns, which points you at a wiring/connector or a failed sensor rather than a real process problem. Manual-reset faults (most P- and compressor codes) latch deliberately after a safety event — clear the underlying cause first, because repeated manual resets on an unresolved high-pressure or motor-temperature fault can damage the compressor.

**Safety and when to call a pro.** These are commercial R-410A packaged chillers with 3-phase power and high-current compressors. Refrigerant recovery/charging requires EPA certification, and compressor or transducer replacement is skilled work. Lock out and tag out before opening the control box. Owner-side tasks (strainer cleaning, checking pump breakers/rotation, clearing a dirty coil, tightening a flagged connection, reading and logging codes) are reasonable in-house; anything touching the refrigerant circuit, the compressor, or repeated safety lockouts should go to Carrier Commercial Service or a qualified commercial refrigeration contractor.


## Frequently asked questions

### My AquaSnap keeps tripping on a flow or frost alarm (P-01 / P-14). What causes it?

Almost always a loss of chilled-water flow, not a refrigerant fault. The usual culprits are a clogged evaporator strainer, a closed or throttled isolation valve, a pump that is off/failed or spinning the wrong way, or a dirty flow switch giving false trips. Restore and prove full flow first, then check the leaving-water thermistor. P-14 is a manual-reset fault, so clear the cause before resetting.

### The chiller trips high pressure on hot afternoons. What do I check first?

A compressor high-pressure switch fault (subcode 03) on a 30RB points at the condenser side: confirm the condenser coil is clean and unobstructed and that every condenser fan is actually running. One failed fan motor can push a circuit over the high-pressure limit when ambient is high. On a 30RQ water-cooled/heat-pump side, verify condenser water flow and that valves are open. Also confirm ambient is within the unit's rating.

### What's the difference between an automatic-reset and a manual-reset alarm?

Sensor and transducer faults (TH-, Pr-) are usually automatic-reset: they clear on their own once a valid signal returns, so they point to a wiring/connector issue or a failed sensor. Process and compressor faults (most P- and C1-C4 codes) are manual-reset: the control latches them after a safety event and you must clear the underlying cause and reset at the controller. Repeatedly resetting an unresolved high-pressure or motor-temperature fault risks compressor damage.

### How do I see and reset alarms on the Pro-Dialog+ or i-Vue controller?

On Pro-Dialog+, the ALARM button shows active alarms and history; STATUS shows live pressures, temperatures and current. On the i-Vue touchscreen, tap the alarm icon in the top bar to read the fault text, and the event history logs recent events with timestamps. Read the full code and its probable-cause text before resetting, and only reset after the cause is fixed.

### Can I recharge or repair the refrigerant circuit myself?

No. AquaSnap 30RB/30RQ units use R-410A and 3-phase compressors; refrigerant recovery and charging require EPA certification, and compressor or transducer replacement is skilled commercial work. Owner-side troubleshooting (cleaning the strainer and condenser coil, checking pump breakers and rotation, tightening a flagged connection, logging codes) is fine, but refrigerant and compressor work should go to Carrier Commercial Service or a qualified commercial refrigeration contractor.

