---
title: "Carrier AquaSnap Chiller Fault Codes — 30RB/30RQ Guide"
description: "Carrier AquaSnap 30RB and 30RQ chiller fault codes for i-Vue and Pro-Dialog controllers: alarms, safety shutdowns, and troubleshooting steps."
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
