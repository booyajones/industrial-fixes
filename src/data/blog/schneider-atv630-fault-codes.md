---
title: "Schneider Altivar 630 Fault Codes: Complete Guide"
description: "Schneider Altivar 630 VFD fault codes and diagnostics. ATV630 fault codes, causes, and technician-level troubleshooting for industrial drives."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-04-22T23:45:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - schneider
  - industrial
  - motor-control
---

# Schneider Altivar 630 Fault Codes

The Schneider Electric Altivar 630 (ATV630) is a mid-range variable frequency drive rated 0.75–800 kW. Fault codes display on the HMI panel as text messages. The ATV630 uses the same fault architecture as the ATV600 and ATV900 families but with drive-specific fault parameters.

## ATV630 Fault Code Table

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Fault Description | Common Cause | [Action](https://www.amazon.com/s?k=Action&tag=errorcodefixe-20) |  |------|------------------|--------------|--------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | OCF | Overcurrent fault | [Motor overload, short circuit](https://www.amazon.com/s?k=Motor%20overload%2C%20short%20circuit&tag=errorcodefixe-20) | Check motor winding, reduce accel time |
| [OBF](https://www.amazon.com/s?k=OBF&tag=errorcodefixe-20) | Brake resistor overload | Brake resistor undersized | [Increase resistor size or duty cycle](https://www.amazon.com/s?k=Increase%20resistor%20size%20or%20duty%20cycle&tag=errorcodefixe-20) |  | SCF | [Short circuit fault](https://www.amazon.com/s?k=Short%20circuit%20fault&tag=errorcodefixe-20) | Output short or ground fault | Megger test motor and cables | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | OHF | Drive overheating | [Ambient temp, blocked airflow](https://www.amazon.com/s?k=Ambient%20temp%2C%20blocked%20airflow&tag=errorcodefixe-20) | Check cooling fans, clean heatsink |
| [OLF](https://www.amazon.com/s?k=OLF&tag=errorcodefixe-20) | Motor overload | Motor thermal protection | [Check motor amps vs. nameplate](https://www.amazon.com/s?k=Check%20motor%20amps%20vs.%20nameplate&tag=errorcodefixe-20) |  | ULF | [Motor underload](https://www.amazon.com/s?k=Motor%20underload&tag=errorcodefixe-20) | Load loss or broken belt | Check mechanical load | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | PHF | Input phase loss | [Missing supply phase](https://www.amazon.com/s?k=Missing%20supply%20phase&tag=errorcodefixe-20) | Check input fuses and supply |
| [CRF](https://www.amazon.com/s?k=CRF&tag=errorcodefixe-20) | Pre-charge circuit fault | Precharge relay or resistor | [Check DC bus and precharge](https://www.amazon.com/s?k=Check%20DC%20bus%20and%20precharge&tag=errorcodefixe-20) |  | USF | [Undervoltage fault](https://www.amazon.com/s?k=Undervoltage%20fault&tag=errorcodefixe-20) | Low supply voltage | Check supply voltage | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | COF | Communication fault | [Fieldbus communication loss](https://www.amazon.com/s?k=Fieldbus%20communication%20loss&tag=errorcodefixe-20) | Check network wiring and master |
| [EEF](https://www.amazon.com/s?k=EEF&tag=errorcodefixe-20) | EEPROM fault | Parameter memory error | [Restore factory defaults](https://www.amazon.com/s?k=Restore%20factory%20defaults&tag=errorcodefixe-20) |  | INF | [Internal fault](https://www.amazon.com/s?k=Internal%20fault&tag=errorcodefixe-20) | Drive internal failure | Contact Schneider support | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | LFF | Load feedback fault | [Encoder or speed feedback error](https://www.amazon.com/s?k=Encoder%20or%20speed%20feedback%20error&tag=errorcodefixe-20) | Check encoder wiring |
| [TJF](https://www.amazon.com/s?k=TJF&tag=errorcodefixe-20) | IGBT junction overtemp | Drive overloading or cooling fault | [Check load and cooling](https://www.amazon.com/s?k=Check%20load%20and%20cooling&tag=errorcodefixe-20) | ## Most Common ATV630 Faults

### OCF — Overcurrent Fault
Check motor insulation with a megohmmeter (1000 VDC, reading should be > 1 MΩ). Verify motor wiring is correct (star vs. delta connection). Increase acceleration ramp time (ACT parameter). Check for mechanical binding in the driven load.

### OHF — Overheating
The ATV630 has a built-in thermal sensor. Measure ambient temperature — the drive is rated to 50°C (122°F) with derating above 40°C. Clean cooling fins with compressed air. Verify cooling fan rotates on command.

### SCF — Short Circuit
Disconnect motor cables and perform insulation test. Also check for ground faults at motor terminals. If motor tests good, the fault may originate in the output IGBT module.

### PHF — Phase Loss
Check all three input phases with a multimeter. Measure voltage balance — more than 2% phase imbalance can cause PHF. Check input fuses individually.

## Parts Commonly Needed | Part | [Notes](https://www.amazon.com/s?k=Notes&tag=errorcodefixe-20) |  |------|-------|
| Cooling fans | [Internal drive fans — match voltage and size](https://www.amazon.com/s?k=Internal%20drive%20fans%20%E2%80%94%20match%20voltage%20and%20size&tag=errorcodefixe-20) |  | Input fuses | [Match voltage and ampere rating](https://www.amazon.com/s?k=Match%20voltage%20and%20ampere%20rating&tag=errorcodefixe-20) |  | Brake resistor | [Match ohm rating and wattage](https://www.amazon.com/s?k=Match%20ohm%20rating%20and%20wattage&tag=errorcodefixe-20) |  | HMI panel | [Match drive series](https://www.amazon.com/s?k=Match%20drive%20series&tag=errorcodefixe-20) |  | I/O extension cards | Match catalog number |

> **Pro tip:** ATV630 fault history is stored in the drive memory. Navigate to [1.10 DIAGNOSTICS] → [FAULT HISTORY] on the HMI to view last 10 faults with timestamps and drive conditions at time of fault.
