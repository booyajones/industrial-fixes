---
title: "Trane YSC Packaged Rooftop Error Codes — Fault Code Diagnostic Guide"
description: "Complete guide to Trane YSC packaged rooftop unit error codes, LED flash sequences, common fault causes, and step-by-step repair procedures for commercial technicians."
pubDatetime: 2026-04-22T23:00:00Z
modDatetime: 2026-04-22T23:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - trane
  - packaged-unit
  - commercial
---

## Trane YSC Packaged Rooftop Error Codes — What They Mean

The Trane YSC is a light commercial gas/electric packaged rooftop unit available in 3–12.5 tons. It is the evolution of the popular Trane Precedent series and is designed for schools, retail, and light commercial applications. The YSC features Trane's ReliaTel controller, which communicates faults through a 7-segment LED display or multi-flash LED depending on the controller version. Newer YSC units with the Tracer UC400B controller support BACnet and LonWorks communication.

[Jump to Fix](#fix)

## Trane YSC ReliaTel Fault Code Reference

| [Display Code](https://www.amazon.com/s?k=Display%20Code&tag=errorcodefixe-20) | Fault |
|---|---|
| [HP](https://www.amazon.com/s?k=HP&tag=errorcodefixe-20) | High-pressure switch trip |
| [LP](https://www.amazon.com/s?k=LP&tag=errorcodefixe-20) | Low-pressure switch trip |
| [FP](https://www.amazon.com/s?k=FP&tag=errorcodefixe-20) | Freeze protection — supply air low temperature |
| [OFC](https://www.amazon.com/s?k=OFC&tag=errorcodefixe-20) | Outdoor fan circuit fault |
| [IFC](https://www.amazon.com/s?k=IFC&tag=errorcodefixe-20) | Indoor fan circuit fault |
| [HPS](https://www.amazon.com/s?k=HPS&tag=errorcodefixe-20) | High-pressure switch lockout (manual reset required) |
| [LPS](https://www.amazon.com/s?k=LPS&tag=errorcodefixe-20) | Low-pressure switch lockout (manual reset required) |
| [LLT](https://www.amazon.com/s?k=LLT&tag=errorcodefixe-20) | Liquid line temperature sensor fault |
| [RAT](https://www.amazon.com/s?k=RAT&tag=errorcodefixe-20) | Return air temperature sensor fault |
| [SAT](https://www.amazon.com/s?k=SAT&tag=errorcodefixe-20) | Supply air temperature sensor fault |
| [OAT](https://www.amazon.com/s?k=OAT&tag=errorcodefixe-20) | Outdoor air temperature sensor fault |
| [COM](https://www.amazon.com/s?k=COM&tag=errorcodefixe-20) | Communication fault |
| [88](https://www.amazon.com/s?k=88&tag=errorcodefixe-20) | Self-test mode |

## Common Causes by Code

- **HP — High pressure** — Blocked condenser coil or failed condenser fan motor. YSC rooftop units with downflow discharge can accumulate debris on the bottom edge of the condenser coil where gravity pulls dirt.
- **LP — Low pressure** — Refrigerant undercharge from a leak. Common leak points: liquid line filter-drier, service port Schrader valves, and brazed joints. Also verify the unit hasn't been put in low-ambient operation without a low-ambient kit.
- **FP — Freeze protection** — Check supply air filters and return air static. Also check for economizer damper stuck open in winter (causes cold outdoor air to mix with return air, artificially dropping coil temperature).
- **OFC — Outdoor fan circuit** — Confirm condenser fan motor power and capacitor. On multi-fan units, one failed motor will trigger OFC even if others run.
- **COM — Communication** — BACnet/LON communication loss. On older YSC with N2, check the N2 wiring polarity (N2+ and N2- must be correct) and address DIP switch settings.

## Step-by-Step Fix {#fix}

1. **Read the display** — Open the ReliaTel controller box on the YSC. The display shows the active fault code. Use a ReliaTel-compatible service tool (Rover or RTM) for detailed historical fault review and sensor readings.
2. **For HP fault** — Shut down the unit. Access the condenser section. Inspect the coil for blockage on all accessible sides. Measure condenser fan motor amps — compare to nameplate. A motor drawing below rated amps may have incorrect capacitor or voltage.
3. **For LP fault** — Connect manifold gauges. Check subcooling at the liquid service port — subcooling below 5°F indicates undercharge. Locate the leak with UV dye or an electronic leak detector before adding refrigerant.
4. **For FP fault** — Turn on the indoor fan only (set thermostat to Fan ON). Check static pressure drop across the filter bank. A pressure drop greater than 0.1" WC above the design specification indicates dirty or damaged filters.
5. **For lockout (HPS or LPS)** — The YSC ReliaTel requires a manual reset after three consecutive pressure switch trips. Reset by cycling power at the main disconnect or through the Rover service tool. Confirm root cause before reset.

## Parts Often Needed

| Part | Notes |
|---|---|
| [Condenser fan motor](https://www.amazon.com/s?k=Condenser%20fan%20motor&tag=errorcodefixe-20) | Multiple motors on larger tonnage; match HP and RPM |
| [Run capacitor](https://www.amazon.com/s?k=Run%20capacitor&tag=errorcodefixe-20) | Check µF against nameplate before replacing motor |
| [ReliaTel controller](https://www.amazon.com/s?k=ReliaTel%20controller&tag=errorcodefixe-20) | For persistent COM or sensor faults |
| [Supply/return air sensor](https://www.amazon.com/s?k=Supply%2Freturn%20air%20sensor&tag=errorcodefixe-20) | NTC thermistor; causes FP, SAT, or RAT codes |
| [High-pressure switch](https://www.amazon.com/s?k=High-pressure%20switch&tag=errorcodefixe-20) | 610 PSIG for R-410A |
| [Liquid line filter-drier](https://www.amazon.com/s?k=Liquid%20line%20filter-drier&tag=errorcodefixe-20) | Replace after any refrigerant-side repair |

## When to Call a Pro

Trane YSC units require HVAC-R licensed technicians for refrigerant service. The ReliaTel controller has advanced diagnostic capability through the Rover service tool — a dealer-level device that provides sensor readings, fault history, and configuration. BACnet integration troubleshooting should involve the building automation contractor as well as the HVAC technician.
