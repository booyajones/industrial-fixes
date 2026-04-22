---
title: "APC Smart-UPS Error Codes: Complete Guide"
description: "APC Smart-UPS error codes and alarm diagnostics. LED codes, fault descriptions, and technician-level troubleshooting for APC UPS systems."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-04-22T23:45:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - electrical
  - apc
  - ups
  - power-quality
---

# APC Smart-UPS Error Codes

APC Smart-UPS (SUA, SMT, SMX, and SRT series) communicate faults via front panel LEDs and audible alarms. Advanced models with LCD displays show text fault messages. The PowerChute software provides detailed fault codes over USB or network.

## Smart-UPS LED/Alarm Code Table

| Alarm Pattern | Fault Description | Common Cause | Action |
|--------------|------------------|--------------|--------|
| Rapid beep | On battery | AC input failed | Check utility power |
| 4 beeps/30 sec | Battery low | Battery nearing depletion | Check battery capacity |
| Continuous beep | Critical fault | Overload or internal fault | Reduce load, check battery |
| Replace Battery LED | Battery replace needed | Battery past service life | Replace battery cartridge |
| Overload LED | Load too high | Connected load exceeds rating | Reduce load |
| Site Wiring Fault LED | Wiring fault | Grounding or wiring issue | Check building wiring |
| Fault LED (F01) | Internal fault — hardware | Internal UPS fault | Contact APC |
| Fault LED (F02) | Output overload | Load exceeds UPS rating | Reduce load |
| Fault LED (F03) | Battery overvoltage | Battery fault | Replace battery |
| Fault LED (F06) | Fan failure | Cooling fan fault | Contact APC |
| Fault LED (F11) | Calibration fault | Internal measurement error | Run calibration |

## Most Common Smart-UPS Faults

### Replace Battery
APC Smart-UPS batteries have a typical service life of 3–5 years. Elevated temperatures (above 25°C ambient) accelerate battery aging. When the Replace Battery LED illuminates, the battery internal resistance has increased to the point where runtime is below spec. Replace with APC-approved battery cartridges — third-party batteries may not communicate correctly with the UPS.

### Overload
The UPS cannot supply more power than its rated VA/watt output. If the connected load exceeds the UPS rating, the overload LED illuminates. The UPS will bypass to utility power if overload persists. Check connected equipment wattage — power strips can make this difficult to track. Disconnect non-critical loads.

### Site Wiring Fault
The Smart-UPS checks for proper AC site wiring. This fault triggers when: the outlet is ungrounded, hot and neutral are reversed, or there is a high-impedance neutral. Check the outlet with a receptacle tester. This fault does not prevent the UPS from operating but indicates a wiring safety issue.

### F06 — Fan Failure
Larger Smart-UPS models (1500 VA+) have internal cooling fans. Fan failure causes the UPS to overheat and derate. On SMX and SRT units, fans are field-replaceable. Check if the fan spins freely — dust accumulation can cause fan failure.

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| Battery cartridge | Match UPS model (APCRBC) — use OEM |
| Replacement fan | SRT and SMX series — model-specific |
| PowerChute software | Free download from APC website |
| Network management card | AP9630 or AP9640 for SNMP monitoring |

> **Pro tip:** APC Smart-UPS with network management cards send SNMP traps or email alerts on fault conditions. Connect the UPS to building network with an NMC card for remote monitoring and proactive battery replacement alerts before battery failure causes an outage.
