---
title: "Schneider Altivar 630 Fault Codes: Complete Guide"
description: "Schneider Altivar 630 VFD fault codes and diagnostics. ATV630 fault codes, causes, and technician-level troubleshooting for industrial drives."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-05-01T08:00:00Z
author: "Dana Kowalski"
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

| Code | Fault Description | Common Cause | Action |
|------|------------------|--------------|--------|
| OCF | Overcurrent fault | Motor overload, short circuit | Check motor winding, reduce accel time |
| OBF | Brake resistor overload | Brake resistor undersized | Increase resistor size or duty cycle |
| SCF | Short circuit fault | Output short or ground fault | Megger test motor and cables |
| OHF | Drive overheating | Ambient temp, blocked airflow | Check cooling fans, clean heatsink |
| OLF | Motor overload | Motor thermal protection | Check motor amps vs. nameplate |
| ULF | Motor underload | Load loss or broken belt | Check mechanical load |
| PHF | Input phase loss | Missing supply phase | Check input fuses and supply |
| CRF | Pre-charge circuit fault | Precharge relay or resistor | Check DC bus and precharge |
| USF | Undervoltage fault | Low supply voltage | Check supply voltage |
| COF | Communication fault | Fieldbus communication loss | Check network wiring and master |
| EEF | EEPROM fault | Parameter memory error | Restore factory defaults |
| INF | Internal fault | Drive internal failure | Contact Schneider support |
| LFF | Load feedback fault | Encoder or speed feedback error | Check encoder wiring |
| TJF | IGBT junction overtemp | Drive overloading or cooling fault | Check load and cooling |

## Most Common ATV630 Faults

### OCF — Overcurrent Fault
Check motor insulation with a megohmmeter (1000 VDC, reading should be > 1 M╬⌐). Verify motor wiring is correct (star vs. delta connection). Increase acceleration ramp time (ACT parameter). Check for mechanical binding in the driven load.

### OHF — Overheating
The ATV630 has a built-in thermal sensor. Measure ambient temperature — the drive is rated to 50°C (122°F) with derating above 40°C. Clean cooling fins with compressed air. Verify cooling fan rotates on command.

### SCF — Short Circuit
Disconnect motor cables and perform insulation test. Also check for ground faults at motor terminals. If motor tests good, the fault may originate in the output IGBT module.

### PHF — Phase Loss
Check all three input phases with a multimeter. Measure voltage balance — more than 2% phase imbalance can cause PHF. Check input fuses individually.

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| Cooling fans | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-schneider-atv630-fault-codes&k=Cooling+fans&tag=errorcodefixes-20) \| Internal drive fans — match voltage and size |
| Input fuses | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-schneider-atv630-fault-codes&k=Input+fuses&tag=errorcodefixes-20) \| Match voltage and ampere rating |
| Brake resistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-schneider-atv630-fault-codes&k=Brake+resistor&tag=errorcodefixes-20) \| Match ohm rating and wattage |
| HMI panel | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-schneider-atv630-fault-codes&k=HMI+panel&tag=errorcodefixes-20) \| Match drive series |
| I/O extension cards | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-schneider-atv630-fault-codes&k=I%2FO+extension+cards&tag=errorcodefixes-20) \| Match catalog number |
> **Pro tip:** ATV630 fault history is stored in the drive memory. Navigate to [1.10 DIAGNOSTICS] ΓåÆ [FAULT HISTORY] on the HMI to view last 10 faults with timestamps and drive conditions at time of fault.
