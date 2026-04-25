---
title: "Trane CenTraVac/RTHD Chiller Fault Codes — Complete Guide"
description: "Trane CenTraVac and RTHD chiller fault codes for Tracer AdaptiView: safety shutdowns, cycling shutdowns, diagnostic messages, and troubleshooting steps."
pubDatetime: 2026-04-22T21:00:00Z
modDatetime: 2026-04-22T21:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - chiller
  - trane
  - centravac
  - rthd
  - hvac
---

## Trane Chiller Fault Codes — Quick Reference

Trane CenTraVac (centrifugal) and RTHD (helical rotary) chillers use the Tracer AdaptiView TD7 touchscreen controller. Diagnostic messages appear as safety shutdowns (require manual reset) or cycling shutdowns (auto-reset).

| Fault | Type | Meaning | Quick Fix |
|-------|------|---------|-----------|
| Low Evaporator Refrigerant Pressure | Safety | Suction pressure below limit | Check flow and refrigerant charge |
| High Condenser Refrigerant Pressure | Safety | Discharge pressure above limit | Check condenser water or fans |
| Low LWT | Safety | Leaving chilled water temp too low | Check flow, setpoints |
| High Compressor Discharge Temp | Safety | Compressor discharge too hot | Check charge and condenser |
| Oil Pressure Low | Safety | Lube oil pressure below minimum | Check oil pump and oil level |
| Motor Winding Temp High | Safety | Motor thermal protection | Check current, voltage, cooling |
| Loss of Flow — Evap | Safety | Chilled water flow lost | Check pump and flow switch |
| Loss of Flow — Cond | Safety | Condenser water flow lost | Check tower pump and flow switch |

## Most Common Faults

### Low Evaporator Refrigerant Pressure (Safety)
On the CenTraVac, this is the most common safety shutdown. Check chilled water flow first using pump differential pressure or a flow meter. If flow is confirmed adequate, check refrigerant charge. A low charge on a centrifugal chiller causes the cooler to starve and the suction pressure drops.

### High Condenser Refrigerant Pressure (Safety)
Condenser pressure too high means the condenser is not rejecting heat properly. On water-cooled units (RTHD, CenTraVac), check condenser water temperature and flow rate. Tower fan operation, tower scaling, and fouled tube sheets all contribute.

### Oil Pressure Low (Safety — CenTraVac)
The CenTraVac centrifugal uses oil for bearing lubrication and gear lubrication. Check oil level in the sump. Check the oil pump operation. A clogged oil filter causes the pressure to drop below setpoint.

## Tracer AdaptiView Navigation

1. HOME SCREEN → tap the red alarm indicator to view active alarms
2. DIAGNOSTICS → HISTORY for past events with timestamp and conditions
3. REPORTS → EQUIPMENT for live readings

## RTHD vs CenTraVac Differences

| Feature | RTHD | CenTraVac |
|---------|------|-----------|
| Compressor type | Helical rotary screw | Centrifugal |
| Refrigerant | R-134a, R-513A | R-11, R-123, R-134a |
| Oil system | Shell/tube oil separator | Dedicated oil pump system |
| Surge protection | N/A | Yes — surge prevention control |

## Parts Often Needed

| Part | Notes |
|------|-------|
| Flow switch (evap or cond) | [Amazon](https://www.amazon.com/s?k=Flow+switch+%28evap+or+cond%29&tag=errorcodefixes-20) \| Check on flow-loss faults |
| Oil filter — CenTraVac | [Amazon](https://www.amazon.com/s?k=Oil+filter+%E2%80%94+CenTraVac&tag=errorcodefixes-20) \| Replace on oil pressure faults |
| Condenser tube cleaning | [Amazon](https://www.amazon.com/s?k=Condenser+tube+cleaning&tag=errorcodefixes-20) \| Required on high condenser pressure |
| Refrigerant charge | [Amazon](https://www.amazon.com/s?k=Refrigerant+charge&tag=errorcodefixes-20) \| After leak repair |
## Jump to Fix

- **Low evaporator pressure** → Confirm chilled water flow → Check charge
- **High condenser pressure** → Check condenser water temp and flow → Clean tubes
- **Low oil pressure (CenTraVac)** → Check oil level → Replace filter → Check pump

## When to Call a Pro
Trane has a nationwide service organization. CenTraVac centrifugal work and refrigerant handling require certified technicians. Contact Trane at 1-855-205-5611.

## Related Articles

- [Trane 1 Flash Error Code — Causes & Fix](/posts/trane-1-flash-error-code/)
- [Trane Error Code 126 — Ignition Lockout Fix](/posts/trane-126-error-code/)
- [Trane 2 Flashes Error Code — Causes & Fix](/posts/trane-2-flashes-error-code/)
- [Trane 3 Flashes Error Code — Pressure Switch Fault Fix](/posts/trane-3-flashes-error-code/)
- [Trane 3 Flash Pressure Switch Fault — Detailed Diagnosis Guide](/posts/trane-3-flashes-pressure-switch/)
