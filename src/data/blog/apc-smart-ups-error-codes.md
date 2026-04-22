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

| [Alarm Pattern](https://www.amazon.com/s?k=Alarm%20Pattern&tag=errorcodefixe-20) | Fault Description | Common Cause | [Action](https://www.amazon.com/s?k=Action&tag=errorcodefixe-20) |  |--------------|------------------|--------------|--------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Rapid beep | On battery | [AC input failed](https://www.amazon.com/s?k=AC%20input%20failed&tag=errorcodefixe-20) | Check utility power |
| [4 beeps/30 sec](https://www.amazon.com/s?k=4%20beeps%2F30%20sec&tag=errorcodefixe-20) | Battery low | Battery nearing depletion | [Check battery capacity](https://www.amazon.com/s?k=Check%20battery%20capacity&tag=errorcodefixe-20) |  | Continuous beep | [Critical fault](https://www.amazon.com/s?k=Critical%20fault&tag=errorcodefixe-20) | Overload or internal fault | Reduce load, check battery | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Replace Battery LED | Battery replace needed | [Battery past service life](https://www.amazon.com/s?k=Battery%20past%20service%20life&tag=errorcodefixe-20) | Replace battery cartridge |
| [Overload LED](https://www.amazon.com/s?k=Overload%20LED&tag=errorcodefixe-20) | Load too high | Connected load exceeds rating | [Reduce load](https://www.amazon.com/s?k=Reduce%20load&tag=errorcodefixe-20) |  | Site Wiring Fault LED | [Wiring fault](https://www.amazon.com/s?k=Wiring%20fault&tag=errorcodefixe-20) | Grounding or wiring issue | Check building wiring | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Fault LED (F01) | Internal fault — hardware | [Internal UPS fault](https://www.amazon.com/s?k=Internal%20UPS%20fault&tag=errorcodefixe-20) | Contact APC |
| [Fault LED (F02)](https://www.amazon.com/s?k=Fault%20LED%20(F02)&tag=errorcodefixe-20) | Output overload | Load exceeds UPS rating | [Reduce load](https://www.amazon.com/s?k=Reduce%20load&tag=errorcodefixe-20) |  | Fault LED (F03) | [Battery overvoltage](https://www.amazon.com/s?k=Battery%20overvoltage&tag=errorcodefixe-20) | Battery fault | Replace battery | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Fault LED (F06) | Fan failure | [Cooling fan fault](https://www.amazon.com/s?k=Cooling%20fan%20fault&tag=errorcodefixe-20) | Contact APC |
| [Fault LED (F11)](https://www.amazon.com/s?k=Fault%20LED%20(F11)&tag=errorcodefixe-20) | Calibration fault | Internal measurement error | [Run calibration](https://www.amazon.com/s?k=Run%20calibration&tag=errorcodefixe-20) | ## Most Common Smart-UPS Faults

### Replace Battery
APC Smart-UPS batteries have a typical service life of 3–5 years. Elevated temperatures (above 25°C ambient) accelerate battery aging. When the Replace Battery LED illuminates, the battery internal resistance has increased to the point where runtime is below spec. Replace with APC-approved battery cartridges — third-party batteries may not communicate correctly with the UPS.

### Overload
The UPS cannot supply more power than its rated VA/watt output. If the connected load exceeds the UPS rating, the overload LED illuminates. The UPS will bypass to utility power if overload persists. Check connected equipment wattage — power strips can make this difficult to track. Disconnect non-critical loads.

### Site Wiring Fault
The Smart-UPS checks for proper AC site wiring. This fault triggers when: the outlet is ungrounded, hot and neutral are reversed, or there is a high-impedance neutral. Check the outlet with a receptacle tester. This fault does not prevent the UPS from operating but indicates a wiring safety issue.

### F06 — Fan Failure
Larger Smart-UPS models (1500 VA+) have internal cooling fans. Fan failure causes the UPS to overheat and derate. On SMX and SRT units, fans are field-replaceable. Check if the fan spins freely — dust accumulation can cause fan failure.

## Parts Commonly Needed | Part | [Notes](https://www.amazon.com/s?k=Notes&tag=errorcodefixe-20) |  |------|-------|
| Battery cartridge | [Match UPS model (APCRBC) — use OEM](https://www.amazon.com/s?k=Match%20UPS%20model%20(APCRBC)%20%E2%80%94%20use%20OEM&tag=errorcodefixe-20) |  | Replacement fan | [SRT and SMX series — model-specific](https://www.amazon.com/s?k=SRT%20and%20SMX%20series%20%E2%80%94%20model-specific&tag=errorcodefixe-20) |  | PowerChute software | [Free download from APC website](https://www.amazon.com/s?k=Free%20download%20from%20APC%20website&tag=errorcodefixe-20) |  | Network management card | AP9630 or AP9640 for SNMP monitoring |

> **Pro tip:** APC Smart-UPS with network management cards send SNMP traps or email alerts on fault conditions. Connect the UPS to building network with an NMC card for remote monitoring and proactive battery replacement alerts before battery failure causes an outage.
