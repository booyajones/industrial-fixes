---
title: "Rheem RPH Series Packaged Unit Error Codes: Complete Guide"
description: "Rheem RPH packaged heat pump error codes and fault diagnostics. Flash codes, fault descriptions, and step-by-step technician fixes."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-05-01T08:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - rheem
  - packaged-unit
  - heat-pump
---

# Rheem RPH Series Packaged Unit Error Codes

Rheem RPH packaged heat pump units use an LED diagnostic indicator on the control board. Flash sequences indicate specific faults — count flashes between 3-second pauses. Units with the EcoNet communicating system display alphanumeric codes on the thermostat.

## RPH Flash Code Table

| Flashes | Fault Description | Common Cause | Action |
|---------|------------------|--------------|--------|
| 2 | Low-pressure lockout | Low charge or frozen coil | Check refrigerant charge |
| 3 | High-pressure lockout | Dirty coil or failed fan | Wash condenser coil |
| 4 | Open high-pressure switch | Overcharge or condenser blockage | Check subcooling |
| 5 | Open low-pressure switch | Low refrigerant, TXV issue | Inspect TXV and charge level |
| 6 | Outdoor fan motor fault | Failed motor or run capacitor | Check capacitor and motor amps |
| 7 | Defrost fault | Defrost sensor or board failure | Check sensor clip and board |
| 8 | Reversing valve stuck | Mechanical or solenoid failure | Check 24 VAC to solenoid |
| 9 | Control board failure | Internal failure | Replace control board |
| Steady ON | Normal operation or continuity | No active fault | N/A |

## Most Common RPH Faults

### 3 Flashes — High-Pressure Lockout
Most common summer service call on packaged units. Verify condenser fan rotation (should pull air up through the coil). Wash coil with commercial coil cleaner. Check for restricted condenser fan discharge.

### 2 Flashes — Low Pressure
In cooling mode: check refrigerant charge using subcooling method. In heating mode: ice on outdoor coil triggers LP trip — verify defrost system operation.

### 7 Flashes — Defrost Fault
Confirm defrost thermostat is clipped firmly to the liquid line near the outdoor coil. Check defrost board timing pins — jumper JP1 sets cycle time. Verify defrost terminates within 14 minutes.

### 8 Flashes — Reversing Valve
Rheem RPH reversing valves are energized in cooling. If stuck in one position, you'll have cooling-only or heating-only operation. Measure solenoid coil resistance (typically 18–30 ╬⌐).

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| Defrost board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-rheem-rph-error-codes&k=Defrost+board&tag=errorcodefixes-20) \| Critical — match to exact model |
| Defrost thermostat | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-rheem-rph-error-codes&k=Defrost+thermostat&tag=errorcodefixes-20) \| Available in multiple trip temperatures |
| Run capacitor | [Amazon](https://www.amazon.com/dp/B01M05L7B3?ascsubtag=ecf-rheem-rph-error-codes&tag=errorcodefixes-20) \| Dual-run — test both sections |
| Reversing valve | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-rheem-rph-error-codes&k=Reversing+valve&tag=errorcodefixes-20) \| Match tonnage and refrigerant type |
| Contactor | [Amazon](https://www.amazon.com/dp/B0CJFZQVPT?ascsubtag=ecf-rheem-rph-error-codes&tag=errorcodefixes-20) \| Check for pitting and coil voltage |
| Control board | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?ascsubtag=ecf-rheem-rph-error-codes&tag=errorcodefixes-20) \| Match unit serial and model number |
> **Pro tip:** Rheem RPH units with EcoNet log fault history with timestamps. Connect EcoNet app to retrieve detailed fault history before servicing — saves significant diagnostic time.

## Related Articles

- [Rheem Classic Series Furnace Error Codes — Complete Guide](/posts/rheem-classic-furnace-error-codes/)
- [Rheem Air Handler E1 Error Code — Causes & Fix](/posts/rheem-error-code-e1/)
- [Rheem Furnace 2 Flashes — Pressure Switch Fault](/posts/rheem-furnace-2-flashes/)
- [Rheem Furnace 3 Flashes Error Code — Causes & Fix](/posts/rheem-furnace-3-flashes/)
- [Rheem Furnace 4 Flashes — Open High Temperature Limit Fix](/posts/rheem-furnace-4-flashes/)

<!-- INTERNAL-LINK-AUTO -->
**Related:** [Rheem Performance Platinum PDN tankless error codes](/posts/rheem-performance-platinum-pdn-error-codes/)

## See Also

- [Rheem EcoNet A101 Error Code — Causes & Fix](/posts/rheem-econet-a101-error-code/)
- [Rheem Furnace 7 Flashes Error Code — Causes & Fix](/posts/rheem-furnace-7-flashes/)
- [Rheem Prestige RP20 Heat Pump Error Codes - Full Fault Code Reference](/posts/rheem-rp20-heat-pump-error-codes/)
- [Rheem Furnace 2 Flashes — Pressure Switch Fault](/posts/rheem-furnace-2-flashes/)
