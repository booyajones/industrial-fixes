---
title: "Carrier 48XLC Packaged Unit Error Codes — Fault Code Diagnostic Guide"
description: "Complete guide to Carrier 48XLC packaged rooftop unit error codes, diagnostic LED flash codes, common fault causes, and step-by-step repair procedures."
pubDatetime: 2026-04-22T23:00:00Z
modDatetime: 2026-04-22T23:00:00Z
author: "ErrorCodeFixes"
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

| [LED Flash](https://www.amazon.com/s?k=LED%20Flash&tag=errorcodefixe-20) | Fault |
|---|---|
| [1 flash](https://www.amazon.com/s?k=1%20flash&tag=errorcodefixe-20) | Normal — no fault present |
| [2 flashes](https://www.amazon.com/s?k=2%20flashes&tag=errorcodefixe-20) | High-pressure switch trip |
| [3 flashes](https://www.amazon.com/s?k=3%20flashes&tag=errorcodefixe-20) | Low-pressure switch trip |
| [4 flashes](https://www.amazon.com/s?k=4%20flashes&tag=errorcodefixe-20) | Compressor lockout — exceeded trip limit |
| [5 flashes](https://www.amazon.com/s?k=5%20flashes&tag=errorcodefixe-20) | Freeze protection lockout — evaporator coil ice |
| [6 flashes](https://www.amazon.com/s?k=6%20flashes&tag=errorcodefixe-20) | Outdoor fan motor fault |
| [7 flashes](https://www.amazon.com/s?k=7%20flashes&tag=errorcodefixe-20) | Return air sensor fault |
| [8 flashes](https://www.amazon.com/s?k=8%20flashes&tag=errorcodefixe-20) | Supply air sensor fault |
| [9 flashes](https://www.amazon.com/s?k=9%20flashes&tag=errorcodefixe-20) | Outdoor coil temperature sensor fault |
| [10 flashes](https://www.amazon.com/s?k=10%20flashes&tag=errorcodefixe-20) | Control board fault |
| [11 flashes](https://www.amazon.com/s?k=11%20flashes&tag=errorcodefixe-20) | Communication fault |

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
| [Run capacitor](https://www.amazon.com/s?k=Run%20capacitor&tag=errorcodefixe-20) | Fan motor capacitor; check before replacing motor |
| [Condenser fan motor](https://www.amazon.com/s?k=Condenser%20fan%20motor&tag=errorcodefixe-20) | Match existing HP, RPM, and shaft diameter |
| [Supply air sensor](https://www.amazon.com/s?k=Supply%20air%20sensor&tag=errorcodefixe-20) | NTC thermistor; causes Code 8 or freeze lockout |
| [High-pressure switch](https://www.amazon.com/s?k=High-pressure%20switch&tag=errorcodefixe-20) | Spade terminal; 610 PSIG for R-410A |
| [WeatherMaker control board](https://www.amazon.com/s?k=WeatherMaker%20control%20board&tag=errorcodefixe-20) | For Code 10; verify fuses first |
| [Compressor contactor](https://www.amazon.com/s?k=Compressor%20contactor&tag=errorcodefixe-20) | Check contact gap and coil resistance |

## When to Call a Pro

Commercial packaged units require licensed HVAC-R technicians for refrigerant work and, in many jurisdictions, a commercial HVAC contractor license for service. BACnet/IP integration troubleshooting requires network access and familiarity with the building automation system. Compressor replacement on a 48XLC is a 4–8 hour job requiring cranes or rigging for heavy-tonnage units.
