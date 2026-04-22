---
title: "Watlow PM6 Temperature Controller Error Codes: Complete Guide"
description: "Watlow PM6 temperature controller error codes and fault messages. Error causes and technician-level troubleshooting for industrial thermal systems."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-04-22T23:45:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - instruments
  - watlow
  - process-control
  - temperature-control
---

# Watlow PM6 Temperature Controller Error Codes

The Watlow PM6 is a 1/16 DIN PID temperature controller with dual display (process value and set point). It supports thermocouple, RTD, and process voltage/current inputs. Error messages appear on the upper (process) display.

## PM6 Error Code Table

| [Display](https://www.amazon.com/s?k=Display&tag=errorcodefixe-20) | Meaning | Cause | [Action](https://www.amazon.com/s?k=Action&tag=errorcodefixe-20) |  |---------|---------|-------|--------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | OPEN | Open sensor | [Open thermocouple or RTD](https://www.amazon.com/s?k=Open%20thermocouple%20or%20RTD&tag=errorcodefixe-20) | Check sensor continuity |
| [SHRT](https://www.amazon.com/s?k=SHRT&tag=errorcodefixe-20) | Shorted sensor | Shorted thermocouple or RTD | [Check sensor insulation](https://www.amazon.com/s?k=Check%20sensor%20insulation&tag=errorcodefixe-20) |  | OvEr | [Over-range input](https://www.amazon.com/s?k=Over-range%20input&tag=errorcodefixe-20) | Temperature above sensor max | Check sensor type and range | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Undr | Under-range input | [Temperature below sensor min](https://www.amazon.com/s?k=Temperature%20below%20sensor%20min&tag=errorcodefixe-20) | Check input type and polarity |
| [Err](https://www.amazon.com/s?k=Err&tag=errorcodefixe-20) | General error | Hardware or input fault | [Check input signal](https://www.amazon.com/s?k=Check%20input%20signal&tag=errorcodefixe-20) |  | InEr | [Input error](https://www.amazon.com/s?k=Input%20error&tag=errorcodefixe-20) | Signal out of specification | Verify input type matches sensor | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | tUnE | Auto-tune in progress | [PID auto-tune active](https://www.amazon.com/s?k=PID%20auto-tune%20active&tag=errorcodefixe-20) | Wait for completion |
| [ALo](https://www.amazon.com/s?k=ALo&tag=errorcodefixe-20) | Low alarm | Process below low alarm setpoint | [Check process condition](https://www.amazon.com/s?k=Check%20process%20condition&tag=errorcodefixe-20) |  | AHi | [High alarm](https://www.amazon.com/s?k=High%20alarm&tag=errorcodefixe-20) | Process above high alarm setpoint | Check process condition | [## Most Common PM6 Faults

### OPEN — Open Sensor
Check the thermocouple or RTD connection at both the PM6 terminals and the sensor head. On thermocouple circuits, open connections may be at extension wire joints. Measure sensor resistance: TC should be < 100 Ω, Pt100 RTD should be 100 Ω at 0°C, 138.5 Ω at 100°C.

### SHRT — Shorted Sensor
A short circuit in the thermocouple or RTD wiring. Common causes: pinched extension wire in machinery, damaged insulation from heat, or a shorted sensor element. Disconnect sensor at PM6 terminals and check resistance from each lead to ground.

### OvEr/Undr — Range Errors
If the process temperature is within expected range but the display shows OvEr or Undr, the input type is misconfigured. Verify input type (Inp parameter in menu) matches the connected sensor. A Type K sensor configured as Type J will read incorrectly.

### Auto-Tune (tUnE)
PM6 auto-tune uses relay output switching to identify process dynamics. During auto-tune, the output cycles on/off — this is normal. Auto-tune requires the process to be near operating temperature. If auto-tune fails, the PM6 reverts to previous PID values.

## Parts Commonly Needed](https://www.amazon.com/s?k=%23%23%20Most%20Common%20PM6%20Faults%0A%0A%23%23%23%20OPEN%20%E2%80%94%20Open%20Sensor%0ACheck%20the%20thermocouple%20or%20RTD%20connection%20at%20both%20the%20PM6%20terminals%20and%20the%20sensor%20head.%20On%20thermocouple%20circuits%2C%20open%20connections%20may%20be%20at%20extension%20wire%20joints.%20Measure%20sensor%20resistance%3A%20TC%20should%20be%20%3C%20100%20%CE%A9%2C%20Pt100%20RTD%20should%20be%20100%20%CE%A9%20at%200%C2%B0C%2C%20138.5%20%CE%A9%20at%20100%C2%B0C.%0A%0A%23%23%23%20SHRT%20%E2%80%94%20Shorted%20Sensor%0AA%20short%20circuit%20in%20the%20thermocouple%20or%20RTD%20wiring.%20Common%20causes%3A%20pinched%20extension%20wire%20in%20machinery%2C%20damaged%20insulation%20from%20heat%2C%20or%20a%20shorted%20sensor%20element.%20Disconnect%20sensor%20at%20PM6%20terminals%20and%20check%20resistance%20from%20each%20lead%20to%20ground.%0A%0A%23%23%23%20OvEr%2FUndr%20%E2%80%94%20Range%20Errors%0AIf%20the%20process%20temperature%20is%20within%20expected%20range%20but%20the%20display%20shows%20OvEr%20or%20Undr%2C%20the%20input%20type%20is%20misconfigured.%20Verify%20input%20type%20(Inp%20parameter%20in%20menu)%20matches%20the%20connected%20sensor.%20A%20Type%20K%20sensor%20configured%20as%20Type%20J%20will%20read%20incorrectly.%0A%0A%23%23%23%20Auto-Tune%20(tUnE)%0APM6%20auto-tune%20uses%20relay%20output%20switching%20to%20identify%20process%20dynamics.%20During%20auto-tune%2C%20the%20output%20cycles%20on%2Foff%20%E2%80%94%20this%20is%20normal.%20Auto-tune%20requires%20the%20process%20to%20be%20near%20operating%20temperature.%20If%20auto-tune%20fails%2C%20the%20PM6%20reverts%20to%20previous%20PID%20values.%0A%0A%23%23%20Parts%20Commonly%20Needed&tag=errorcodefixe-20) | Part | Notes | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------ |-------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Thermocouple (Type K/J/T) | Match existing sensor type | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | RTD sensor (Pt100) | For RTD input PM6 versions | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Solid-state relay | Match output type (SSR for current output) | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Mechanical relay | For relay output versions | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Replacement PM6 | Document all parameter values before replacing |

> **Pro tip:** Watlow PM6 parameters can be locked with a password to prevent unauthorized changes. If locked, consult the PM6 installation manual for the default unlock code (1234). Document all parameter values before any PM6 replacement — there is no backup-and-restore function.
