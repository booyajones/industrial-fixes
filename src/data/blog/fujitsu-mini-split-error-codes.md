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

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Meaning | Quick Fix | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------ |---------|-----------|
| E1 | [Indoor/outdoor communication fault](https://www.amazon.com/s?k=Indoor%2Foutdoor%20communication%20fault&tag=errorcodefixe-20) | Check signal wiring |
| [E3](https://www.amazon.com/s?k=E3&tag=errorcodefixe-20) | Indoor fan motor fault | Check fan motor and capacitor | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | E7 | Outdoor fan motor fault | [Check outdoor fan motor](https://www.amazon.com/s?k=Check%20outdoor%20fan%20motor&tag=errorcodefixe-20) |  | E8 | [Indoor PCB fault](https://www.amazon.com/s?k=Indoor%20PCB%20fault&tag=errorcodefixe-20) | Replace indoor PCB |
| [E9](https://www.amazon.com/s?k=E9&tag=errorcodefixe-20) | Communication fault between units | Check 3-wire signal cable | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | E0 | Startup/communication error | [Check power and wiring](https://www.amazon.com/s?k=Check%20power%20and%20wiring&tag=errorcodefixe-20) |  | P1 | [Freeze protection — cooling](https://www.amazon.com/s?k=Freeze%20protection%20%E2%80%94%20cooling&tag=errorcodefixe-20) | Low refrigerant or blocked filter |
| [P2](https://www.amazon.com/s?k=P2&tag=errorcodefixe-20) | High discharge temperature | Low refrigerant or EEV fault | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | P4 | Low pressure protection | [Check refrigerant charge](https://www.amazon.com/s?k=Check%20refrigerant%20charge&tag=errorcodefixe-20) |  | P5 | [High pressure protection](https://www.amazon.com/s?k=High%20pressure%20protection&tag=errorcodefixe-20) | Clean outdoor coil |
| [P6](https://www.amazon.com/s?k=P6&tag=errorcodefixe-20) | Overcurrent protection | Check compressor and refrigerant | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | P7 | IPM module fault | [Outdoor inverter board failure](https://www.amazon.com/s?k=Outdoor%20inverter%20board%20failure&tag=errorcodefixe-20) |  | P8 | [Indoor PCB fault](https://www.amazon.com/s?k=Indoor%20PCB%20fault&tag=errorcodefixe-20) | Replace indoor PCB |
| [P9](https://www.amazon.com/s?k=P9&tag=errorcodefixe-20) | Outdoor PCB fault | Replace outdoor PCB | [## Most Common Codes

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

## Parts Often Needed](https://www.amazon.com/s?k=%23%23%20Most%20Common%20Codes%0A%0A%23%23%23%20E1%3A%20Indoor-Outdoor%20Communication%0AThe%20most%20common%20fault%20on%20Fujitsu%20installations.%20Check%20the%203-wire%20communication%20cable%20between%20indoor%20and%20outdoor%20units%20at%20both%20terminal%20blocks.%20The%20cable%20must%20be%20shielded%20or%20at%20least%20separated%20from%20power%20wiring%20%E2%80%94%20routing%20the%20signal%20cable%20in%20the%20same%20conduit%20as%20line%20voltage%20causes%20induced%20interference%20that%20shows%20up%20as%20intermittent%20E1%20faults.%0A%0AFujitsu%20terminal%20block%20wiring%3A%20Terminal%201%20%3D%20Line%201%20(L)%2C%20Terminal%202%20%3D%20Neutral%20(N)%2C%20Terminal%203%20%3D%20Signal%20(S).%20Verify%20all%20screws%20are%20tight%20and%20no%20bare%20wire%20strands%20are%20contacting%20adjacent%20terminals.%0A%0A%23%23%23%20E3%3A%20Indoor%20Fan%20Motor%20Fault%0AThe%20indoor%20fan%20motor%20is%20not%20running%20or%20not%20reaching%20commanded%20speed.%20Check%3A%20(1)%20the%20fan%20wheel%20is%20not%20obstructed%20by%20debris%2C%20(2)%20the%20run%20capacitor%20is%20within%20spec%20(most%20Fujitsu%20indoor%20fan%20motors%20use%20a%201%E2%80%933%20%C2%B5F%20capacitor)%2C%20(3)%20the%20motor%20windings%20measure%20correct%20resistance.%20If%20the%20motor%20hums%20but%20doesn't%20spin%2C%20replace%20the%20capacitor%20first%20%E2%80%94%20it's%20much%20cheaper%20than%20the%20motor.%0A%0A%23%23%23%20E7%3A%20Outdoor%20Fan%20Motor%20Fault%0AThe%20outdoor%20fan%20motor%20has%20failed%20or%20its%20position%20sensor%20isn't%20reporting%20correctly.%20On%20Fujitsu%20inverter%20outdoor%20units%2C%20the%20fan%20motor%20uses%20DC%20inverter%20control%20%E2%80%94%20a%20failed%20Hall%20effect%20sensor%20causes%20E7%20codes%20even%20when%20the%20motor%20physically%20spins.%20Replace%20the%20outdoor%20fan%20motor%20assembly%20as%20a%20unit.%0A%0A%23%23%23%20P1%3A%20Freeze%20Protection%20(Cooling%20Mode)%0AThe%20indoor%20coil%20temperature%20sensor%20detected%20abnormally%20low%20coil%20temperature%20%E2%80%94%20the%20coil%20is%20freezing.%20Causes%3A%20dirty%20air%20filter%20(most%20common)%2C%20closed%20return%20air%20register%2C%20or%20low%20refrigerant%20charge.%20Replace%20the%20filter%20and%20allow%20ice%20to%20melt%20before%20restarting.%0A%0A%23%23%23%20P5%3A%20High%20Pressure%20Protection%0AHigh%20refrigerant%20pressure%20tripped%20the%20safety%20cutout.%20Clean%20the%20outdoor%20coil%20thoroughly.%20On%20Fujitsu%20RLS3H%20heat%20pump%20models%2C%20also%20check%20that%20the%20outdoor%20defrost%20cycle%20is%20functioning%20properly%20in%20winter%20%E2%80%94%20ice%20buildup%20on%20the%20outdoor%20coil%20can%20cause%20high%20pressure%20in%20heating%20mode.%0A%0A%23%23%23%20P7%3A%20IPM%20Module%20Fault%0AThe%20Intelligent%20Power%20Module%20(inverter%20circuit)%20on%20the%20outdoor%20board%20has%20failed.%20This%20is%20typically%20an%20outdoor%20PCB%20replacement.%20However%2C%20before%20replacing%2C%20verify%20the%20power%20supply%20voltage%20is%20within%20spec%20(rated%20%C2%B110%25)%20%E2%80%94%20low%20or%20unbalanced%20voltage%20accelerates%20IPM%20failure.%0A%0A%23%23%20Retrieving%20Codes%20Without%20Display%0A%0AOn%20Fujitsu%20wall-mount%20models%20without%20wired%20controller%2C%20read%20the%20LED%20blink%20pattern%20on%20the%20indoor%20unit%3A%0A-%20**Error%20LED%20blinking%3A**%20Count%20blinks%20in%20groups.%20The%20pattern%20%22blink-blink-blink...pause...blink-blink%22%20%3D%20E3%20code%20(3%20blinks%20pause%202%20blinks).%0A-%20**OPERATION%20LED%3A**%20Used%20for%20some%20protection%20codes.%20Refer%20to%20the%20service%20manual%20for%20your%20specific%20model.%0A%0A%23%23%20Parts%20Often%20Needed&tag=errorcodefixe-20) | Part | Notes | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------ |-------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Indoor fan motor | Model-specific; note motor winding resistance | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Outdoor fan motor | DC inverter motor with Hall sensor | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Indoor PCB | Fujitsu 9709481xxx — match model | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Indoor air thermistor | Small NTC thermistor, 10 kΩ at 25°C |

## When to Call a Pro
P2 (high discharge temp), P4 (low pressure), P6 (overcurrent), and P7 (IPM fault) indicate refrigerant system or inverter drive problems that require professional tools and refrigerant certification to diagnose properly.
