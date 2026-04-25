---
title: "Fujitsu Mini Split Error Codes — E and P Code Guide"
description: "Fujitsu mini split error codes: all E and P fault codes for Fujitsu Halcyon and Airstage systems with causes and fixes."
pubDatetime: 2026-04-22T16:00:00Z
modDatetime: 2026-04-22T16:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - mini-split
  - fujitsu
---

## Fujitsu Mini Split Error Codes — Quick Reference

Fujitsu mini-splits (Halcyon and Airstage series) display error codes via a blinking LED on the indoor unit or on the wired remote controller. **E-codes** are general faults; **P-codes** are protection/safety faults. To retrieve a fault code on units without a display: count the blinks on the operation LED. On units with a wired controller, codes appear directly on the screen.

| Code | Meaning | Quick Fix |
|------|---------|-----------|
| E1 | Indoor/outdoor communication fault | Check signal wiring |
| E3 | Indoor fan motor fault | Check fan motor and capacitor |
| E7 | Outdoor fan motor fault | Check outdoor fan motor |
| E8 | Indoor PCB fault | Replace indoor PCB |
| E9 | Communication fault between units | Check 3-wire signal cable |
| E0 | Startup/communication error | Check power and wiring |
| P1 | Freeze protection — cooling | Low refrigerant or blocked filter |
| P2 | High discharge temperature | Low refrigerant or EEV fault |
| P4 | Low pressure protection | Check refrigerant charge |
| P5 | High pressure protection | Clean outdoor coil |
| P6 | Overcurrent protection | Check compressor and refrigerant |
| P7 | IPM module fault | Outdoor inverter board failure |
| P8 | Indoor PCB fault | Replace indoor PCB |
| P9 | Outdoor PCB fault | Replace outdoor PCB |

## Most Common Codes

### E1: Indoor-Outdoor Communication
The most common fault on Fujitsu installations. Check the 3-wire communication cable between indoor and outdoor units at both terminal blocks. The cable must be shielded or at least separated from power wiring — routing the signal cable in the same conduit as line voltage causes induced interference that shows up as intermittent E1 faults.

Fujitsu terminal block wiring: Terminal 1 = Line 1 (L), Terminal 2 = Neutral (N), Terminal 3 = Signal (S). Verify all screws are tight and no bare wire strands are contacting adjacent terminals.

### E3: Indoor Fan Motor Fault
The indoor fan motor is not running or not reaching commanded speed. Check: (1) the fan wheel is not obstructed by debris, (2) the run capacitor is within spec (most Fujitsu indoor fan motors use a 1–3 µF capacitor), (3) the motor windings measure correct resistance. If the motor hums but doesn't spin, replace the capacitor first — it's much cheaper than the motor.

### E7: Outdoor Fan Motor Fault
The outdoor fan motor has failed or its position sensor isn't reporting correctly. On Fujitsu inverter outdoor units, the fan motor uses DC inverter control — a failed Hall effect sensor causes E7 codes even when the motor physically spins. Replace the outdoor fan motor assembly as a unit.

### P1: Freeze Protection (Cooling Mode)
The indoor coil temperature sensor detected abnormally low coil temperature — the coil is freezing. Causes: dirty air filter (most common), closed return air register, or low refrigerant charge. Replace the filter and allow ice to melt before restarting.

### P5: High Pressure Protection
High refrigerant pressure tripped the safety cutout. Clean the outdoor coil thoroughly. On Fujitsu RLS3H heat pump models, also check that the outdoor defrost cycle is functioning properly in winter — ice buildup on the outdoor coil can cause high pressure in heating mode.

### P7: IPM Module Fault
The Intelligent Power Module (inverter circuit) on the outdoor board has failed. This is typically an outdoor PCB replacement. However, before replacing, verify the power supply voltage is within spec (rated ±10%) — low or unbalanced voltage accelerates IPM failure.

## Retrieving Codes Without Display

On Fujitsu wall-mount models without wired controller, read the LED blink pattern on the indoor unit:
- **Error LED blinking:** Count blinks in groups. The pattern "blink-blink-blink...pause...blink-blink" = E3 code (3 blinks pause 2 blinks).
- **OPERATION LED:** Used for some protection codes. Refer to the service manual for your specific model.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Indoor fan motor | [Amazon](https://www.amazon.com/s?k=Indoor+fan+motor&tag=errorcodefixes-20) \| Model-specific; note motor winding resistance |
| Outdoor fan motor | [Amazon](https://www.amazon.com/s?k=Outdoor+fan+motor&tag=errorcodefixes-20) \| DC inverter motor with Hall sensor |
| Indoor PCB | [Amazon](https://www.amazon.com/s?k=Indoor+PCB&tag=errorcodefixes-20) \| Fujitsu 9709481xxx — match model |
| Indoor air thermistor | [Amazon](https://www.amazon.com/s?k=Indoor+air+thermistor&tag=errorcodefixes-20) \| Small NTC thermistor, 10 kΩ at 25°C |
## When to Call a Pro
P2 (high discharge temp), P4 (low pressure), P6 (overcurrent), and P7 (IPM fault) indicate refrigerant system or inverter drive problems that require professional tools and refrigerant certification to diagnose properly.

## Related Articles

- [Bosch Heat Pump E1 Error Code — Causes & Fix](/posts/bosch-heat-pump-e1-error-code/)
- [Carrier 24ANA Heat Pump Error Codes — Performance Series Diagnostic Guide](/posts/carrier-24ana-heat-pump-error-codes/)
- [Carrier Heat Pump E1 Error Code — Causes & Fix](/posts/carrier-heat-pump-e1-error-code/)
- [Carrier Heat Pump E4 Error Code — Causes & Fix](/posts/carrier-heat-pump-e4-error-code/)
- [Carrier Heat Pump E5 Error Code — Defrost Fault: Causes & Fix](/posts/carrier-heat-pump-e5-error-code/)
