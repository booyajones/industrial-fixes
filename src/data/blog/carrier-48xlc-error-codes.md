---
title: "Carrier 48XLC Packaged Unit Error Codes — Fault Code Diagnostic Guide"
description: "Complete guide to Carrier 48XLC packaged rooftop unit error codes, diagnostic LED flash codes, common fault causes, and step-by-step repair procedures."
pubDatetime: 2026-04-22T23:00:00Z
modDatetime: 2026-04-22T23:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - carrier
  - packaged-unit
  - commercial
---

## Carrier 48XLC Packaged Unit Error Codes — What They Mean

The Carrier 48XLC is a light commercial single-package gas/electric rooftop unit in the 3–12.5 ton range. It is designed for small commercial applications — retail, schools, light industrial — and is installed on rooftops or pads. The 48XLC features Carrier's WeatherMaker control board, which uses an LED status indicator for standalone diagnostics and supports connection to Carrier's i-Vu or 33ZC zone controllers for BACnet/IP integration.

[Jump to Fix](#fix)

## Carrier 48XLC LED Fault Code Reference

| LED Flash | Fault |
|---|---|
| 1 flash | Normal — no fault present |
| 2 flashes | High-pressure switch trip |
| 3 flashes | Low-pressure switch trip |
| 4 flashes | Compressor lockout — exceeded trip limit |
| 5 flashes | Freeze protection lockout — evaporator coil ice |
| 6 flashes | Outdoor fan motor fault |
| 7 flashes | Return air sensor fault |
| 8 flashes | Supply air sensor fault |
| 9 flashes | Outdoor coil temperature sensor fault |
| 10 flashes | Control board fault |
| 11 flashes | Communication fault |

## Common Causes by Code

- **2 flashes — High pressure** — Fouled condenser coil is the top cause on rooftop units. 48XLC coils collect debris from HVAC exhaust vents, rooftop gravel, and bird droppings. Also check refrigerant overcharge — a tech who topped off without recovering first is a common service history flag.
- **3 flashes — Low pressure** — Refrigerant undercharge, evaporator freeze (cascade with Code 5), or extremely low ambient temperatures. Check return air temperature and filter condition when investigating Code 3.
- **4 flashes — Compressor lockout** — Carrier's 48XLC locks out the compressor after three consecutive pressure switch trips and requires a manual reset. Do not reset without finding the root cause.
- **5 flashes — Freeze protection** — The supply air temperature sensor detects supply air at or below 35°F — typically caused by restricted airflow (dirty filters, closed dampers) or low refrigerant charge in part-load conditions.
- **11 flashes — Communication** — BACnet/IP or Linkage communication loss. Verify IP addressing, confirm the controller is powered, and check Cat5 cable for damage.

## Step-by-Step Fix {#fix}

1. **Check the status LED** — Open the controls access panel (front or end of the 48XLC unit). The WeatherMaker board's LED is usually labeled "Status." Count flashes in the repeated cycle.
2. **For Code 2 (high pressure)** — Shut down. Access the condenser section (usually the end opposite the controls). Inspect the coil for debris — use a coil cleaner approved for rooftop use. Rinse from inside-out. Check fan blades for damage and blade pitch uniformity.
3. **For Code 5 (freeze protection)** — Check return air filters first. Measure return air static pressure — high static indicates airflow restriction. If filters are clean, check for closed economizer dampers or closed supply grilles in the conditioned space.
4. **For Code 4 (compressor lockout)** — Cycle the 48XLC main disconnect to reset. If the unit trips again within one cooling cycle, the root cause (high or low pressure) has not been resolved. Address the underlying pressure issue before returning the unit to service.
5. **Communication fault (Code 11)** — Confirm the BACnet/IP controller has a valid IP address and can ping other devices on the network. Check the MS/TP shielding at the controller and at the unit — ground loops on improperly shielded RS-485 wiring cause intermittent communication faults.

## Parts Often Needed

| Part | Notes |
|---|---|
| Run capacitor | [Amazon](https://www.amazon.com/dp/B01M05L7B3?ascsubtag=ecf-carrier-48xlc-error-codes&tag=errorcodefixes-20) \| Fan motor capacitor; check before replacing motor |
| Condenser fan motor | [Amazon](https://www.amazon.com/dp/B0D2L5NSMM?ascsubtag=ecf-carrier-48xlc-error-codes&tag=errorcodefixes-20) \| Match existing HP, RPM, and shaft diameter |
| Supply air sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-carrier-48xlc-error-codes&k=Supply+air+sensor&tag=errorcodefixes-20) \| NTC thermistor; causes Code 8 or freeze lockout |
| High-pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-carrier-48xlc-error-codes&tag=errorcodefixes-20) \| Spade terminal; 610 PSIG for R-410A |
| WeatherMaker control board | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?ascsubtag=ecf-carrier-48xlc-error-codes&tag=errorcodefixes-20) \| For Code 10; verify fuses first |
| Compressor contactor | [Amazon](https://www.amazon.com/dp/B0CJFZQVPT?ascsubtag=ecf-carrier-48xlc-error-codes&tag=errorcodefixes-20) \| Check contact gap and coil resistance |
## When to Call a Pro

Commercial packaged units require licensed HVAC-R technicians for refrigerant work and, in many jurisdictions, a commercial HVAC contractor license for service. BACnet/IP integration troubleshooting requires network access and familiarity with the building automation system. Compressor replacement on a 48XLC is a 4–8 hour job requiring cranes or rigging for heavy-tonnage units.

## Related Articles

- [Carrier 11 Error Code — Causes & Fix](/posts/carrier-11-error-code/)
- [Carrier 12 Error Code — Causes & Fix](/posts/carrier-12-error-code/)
- [Carrier 13 Error Code — Limit Switch Lockout Fix](/posts/carrier-13-error-code/)
- [Carrier 13 Soft Lockout — What's Different from Hard Lockout](/posts/carrier-13-soft-lockout/)
- [Carrier 14 Error Code — Causes & Fix](/posts/carrier-14-error-code/)
