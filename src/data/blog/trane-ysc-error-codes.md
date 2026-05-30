---
title: "Trane YSC Packaged Rooftop Error Codes — Fault Code Diagnostic Guide"
description: "Complete guide to Trane YSC packaged rooftop unit error codes, LED flash sequences, common fault causes, and step-by-step repair procedures for commercial technicians."
pubDatetime: 2026-04-22T23:00:00Z
modDatetime: 2026-04-22T23:00:00Z
author: "Marcus Webb"
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

| Display Code | Fault |
|---|---|
| HP | High-pressure switch trip |
| LP | Low-pressure switch trip |
| FP | Freeze protection — supply air low temperature |
| OFC | Outdoor fan circuit fault |
| IFC | Indoor fan circuit fault |
| HPS | High-pressure switch lockout (manual reset required) |
| LPS | Low-pressure switch lockout (manual reset required) |
| LLT | Liquid line temperature sensor fault |
| RAT | Return air temperature sensor fault |
| SAT | Supply air temperature sensor fault |
| OAT | Outdoor air temperature sensor fault |
| COM | Communication fault |
| 88 | Self-test mode |

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
| Condenser fan motor | [Amazon](https://www.amazon.com/dp/B0D2L5NSMM?ascsubtag=ecf-trane-ysc-error-codes&tag=errorcodefixes-20) \| Multiple motors on larger tonnage; match HP and RPM |
| Run capacitor | [Amazon](https://www.amazon.com/dp/B01M05L7B3?ascsubtag=ecf-trane-ysc-error-codes&tag=errorcodefixes-20) \| Check µF against nameplate before replacing motor |
| ReliaTel controller | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-trane-ysc-error-codes&k=ReliaTel+controller&tag=errorcodefixes-20) \| For persistent COM or sensor faults |
| Supply/return air sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-trane-ysc-error-codes&k=Supply%2Freturn+air+sensor&tag=errorcodefixes-20) \| NTC thermistor; causes FP, SAT, or RAT codes |
| High-pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-trane-ysc-error-codes&tag=errorcodefixes-20) \| 610 PSIG for R-410A |
| Liquid line filter-drier | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-trane-ysc-error-codes&k=Liquid+line+filter-drier&tag=errorcodefixes-20) \| Replace after any refrigerant-side repair |
## When to Call a Pro

Trane YSC units require HVAC-R licensed technicians for refrigerant service. The ReliaTel controller has advanced diagnostic capability through the Rover service tool — a dealer-level device that provides sensor readings, fault history, and configuration. BACnet integration troubleshooting should involve the building automation contractor as well as the HVAC technician.

## Related Articles

- [Trane 1 Flash Error Code — Causes & Fix](/posts/trane-1-flash-error-code/)
- [Trane Error Code 126 — Ignition Lockout Fix](/posts/trane-126-error-code/)
- [Trane 2 Flashes Error Code — Causes & Fix](/posts/trane-2-flashes-error-code/)
- [Trane 3 Flashes Error Code — Pressure Switch Fault Fix](/posts/trane-3-flashes-error-code/)
- [Trane 3 Flash Pressure Switch Fault — Detailed Diagnosis Guide](/posts/trane-3-flashes-pressure-switch/)

## See Also

- [Trane XV20i Heat Pump Error Codes — Common Faults & Fixes](/posts/trane-xv20i-heat-pump-error-codes/)
- [Trane VRF System Error Codes Guide](/posts/trane-vrf-error-codes/)
- [Trane Heat Pump 1 Flash Error Code — Causes & Fix](/posts/trane-heat-pump-1-flash/)
- [Trane XV20i/XV18 Fault 126 — Low Pressure Cutout Fix](/posts/trane-heat-pump-error-code-126/)
