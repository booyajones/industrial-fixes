---
title: "Danfoss VLT 2900 Fault Codes: Complete Guide"
description: "Danfoss VLT 2900 VFD fault codes and diagnostics. AL-series alarm codes, causes, and technician-level troubleshooting for VLT 2900 drives."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-04-22T23:45:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - danfoss
  - industrial
  - motor-control
---

# Danfoss VLT 2900 Fault Codes

The Danfoss VLT 2900 series is a general-purpose VFD rated 0.37–30 kW. Alarm codes display on the LCP (Local Control Panel) as "AL" followed by a number. Warning codes display as "W" codes. The VLT 2900 is an older series — replacement is the VLT FC301/302 family.

## VLT 2900 Fault Code Table

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Fault Description | Common Cause | [Action](https://www.amazon.com/s?k=Action&tag=errorcodefixe-20) |  |------|------------------|--------------|--------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | AL 1 | 10V supply low | [10V reference output shorted](https://www.amazon.com/s?k=10V%20reference%20output%20shorted&tag=errorcodefixe-20) | Check terminal 50 wiring |
| [AL 2](https://www.amazon.com/s?k=AL%202&tag=errorcodefixe-20) | Live zero fault | Reference input below minimum | [Check analog input signal](https://www.amazon.com/s?k=Check%20analog%20input%20signal&tag=errorcodefixe-20) |  | AL 4 | [Phase loss (motor)](https://www.amazon.com/s?k=Phase%20loss%20(motor)&tag=errorcodefixe-20) | Missing output phase | Check motor connections | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | AL 5 | DC link overvoltage | [Regeneration or voltage spike](https://www.amazon.com/s?k=Regeneration%20or%20voltage%20spike&tag=errorcodefixe-20) | Extend decel ramp, add brake |
| [AL 7](https://www.amazon.com/s?k=AL%207&tag=errorcodefixe-20) | DC link overvoltage (fault) | Persistent overvoltage | [Check input voltage](https://www.amazon.com/s?k=Check%20input%20voltage&tag=errorcodefixe-20) |  | AL 13 | [Overcurrent](https://www.amazon.com/s?k=Overcurrent&tag=errorcodefixe-20) | Motor short or overload | Megger test motor, reduce load | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | AL 14 | Ground fault | [Motor winding ground](https://www.amazon.com/s?k=Motor%20winding%20ground&tag=errorcodefixe-20) | Megger test motor |
| [AL 15](https://www.amazon.com/s?k=AL%2015&tag=errorcodefixe-20) | Drive incompatible | Wrong hardware | [Check drive model](https://www.amazon.com/s?k=Check%20drive%20model&tag=errorcodefixe-20) |  | AL 16 | [Short circuit](https://www.amazon.com/s?k=Short%20circuit&tag=errorcodefixe-20) | Output short circuit | Check motor and cables | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | AL 17 | Control word timeout | [Serial communication loss](https://www.amazon.com/s?k=Serial%20communication%20loss&tag=errorcodefixe-20) | Check network connection |
| [AL 25](https://www.amazon.com/s?k=AL%2025&tag=errorcodefixe-20) | Brake resistor short | Brake resistor failure | [Check brake resistor resistance](https://www.amazon.com/s?k=Check%20brake%20resistor%20resistance&tag=errorcodefixe-20) |  | AL 29 | [Heatsink overtemp](https://www.amazon.com/s?k=Heatsink%20overtemp&tag=errorcodefixe-20) | Cooling blocked or high ambient | Clean fins, check fan | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | AL 34 | Communication fault | [Fieldbus timeout](https://www.amazon.com/s?k=Fieldbus%20timeout&tag=errorcodefixe-20) | Check communication network |
| [AL 38](https://www.amazon.com/s?k=AL%2038&tag=errorcodefixe-20) | Motor thermal limit | Motor overtemperature | [Reduce load, check motor cooling](https://www.amazon.com/s?k=Reduce%20load%2C%20check%20motor%20cooling&tag=errorcodefixe-20) |  | AL 41 | [Analog input 53 low](https://www.amazon.com/s?k=Analog%20input%2053%20low&tag=errorcodefixe-20) | Signal below minimum | Check signal from sensor/controller | [## Most Common VLT 2900 Faults

### AL 13 — Overcurrent
The VLT 2900 is sensitive to output impedance. Verify motor data in parameters 102–106 (nameplate data). Increase parameter 207 (acceleration time). If the fault is immediate on start, check for a short circuit at output terminals.

### AL 29 — Heatsink Overtemperature
VLT 2900 units installed in enclosures must have adequate ventilation. Heatsink temperature limit is 90°C. Clean fins with compressed air. In enclosed panels, provide fan-forced cooling with adequate airflow through the panel.

### AL 5 — DC Link Overvoltage
Most common on applications with high inertia loads (fans, pumps, centrifuges). The VLT 2900 DC bus charges if motor decelerates faster than the drive absorbs energy. Extend decel time (parameter 208) or add brake chopper/resistor.

### AL 14 — Ground Fault
Use megohmmeter at 1000 VDC on all motor windings and cables. Also check PE (ground) connection integrity at both motor and drive. Long cables act as capacitors and can cause nuisance ground fault trips on older drives.

## Parts Commonly Needed](https://www.amazon.com/s?k=%23%23%20Most%20Common%20VLT%202900%20Faults%0A%0A%23%23%23%20AL%2013%20%E2%80%94%20Overcurrent%0AThe%20VLT%202900%20is%20sensitive%20to%20output%20impedance.%20Verify%20motor%20data%20in%20parameters%20102%E2%80%93106%20(nameplate%20data).%20Increase%20parameter%20207%20(acceleration%20time).%20If%20the%20fault%20is%20immediate%20on%20start%2C%20check%20for%20a%20short%20circuit%20at%20output%20terminals.%0A%0A%23%23%23%20AL%2029%20%E2%80%94%20Heatsink%20Overtemperature%0AVLT%202900%20units%20installed%20in%20enclosures%20must%20have%20adequate%20ventilation.%20Heatsink%20temperature%20limit%20is%2090%C2%B0C.%20Clean%20fins%20with%20compressed%20air.%20In%20enclosed%20panels%2C%20provide%20fan-forced%20cooling%20with%20adequate%20airflow%20through%20the%20panel.%0A%0A%23%23%23%20AL%205%20%E2%80%94%20DC%20Link%20Overvoltage%0AMost%20common%20on%20applications%20with%20high%20inertia%20loads%20(fans%2C%20pumps%2C%20centrifuges).%20The%20VLT%202900%20DC%20bus%20charges%20if%20motor%20decelerates%20faster%20than%20the%20drive%20absorbs%20energy.%20Extend%20decel%20time%20(parameter%20208)%20or%20add%20brake%20chopper%2Fresistor.%0A%0A%23%23%23%20AL%2014%20%E2%80%94%20Ground%20Fault%0AUse%20megohmmeter%20at%201000%20VDC%20on%20all%20motor%20windings%20and%20cables.%20Also%20check%20PE%20(ground)%20connection%20integrity%20at%20both%20motor%20and%20drive.%20Long%20cables%20act%20as%20capacitors%20and%20can%20cause%20nuisance%20ground%20fault%20trips%20on%20older%20drives.%0A%0A%23%23%20Parts%20Commonly%20Needed&tag=errorcodefixe-20) | Part | Notes | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------ |-------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | LCP control panel | Available as replacement accessory | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Brake resistor | Match resistance and power rating | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Cooling fan | Specific to VLT 2900 frame size | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Fuses | Note: VLT 2900 uses specific semiconductor fuse types |

> **Pro tip:** Danfoss VLT 2900 drives are discontinued. When parts are no longer available, the FC301/FC302 is the recommended migration path. Danfoss provides a parameter migration guide for converting VLT 2900 parameters to FC302 equivalents.
