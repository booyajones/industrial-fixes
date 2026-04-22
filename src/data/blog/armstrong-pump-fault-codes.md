---
title: "Armstrong Pump Fault Codes: Complete Guide"
description: "Armstrong pump fault codes and error diagnostics. Design Envelope pump fault codes, causes, and technician-level troubleshooting."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-04-22T23:45:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - pumps
  - armstrong
  - hvac
  - industrial
---

# Armstrong Pump Fault Codes

Armstrong Design Envelope pumps with integrated VFD and Pump Manager controls display fault codes on the integrated display. Armstrong's IPS (Intelligent Pump System) adds cloud diagnostics. For pumps with external drives, refer to the VFD fault codes (typically ABB or Danfoss).

## Armstrong Design Envelope Fault Code Table

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Fault Description | Common Cause | [Action](https://www.amazon.com/s?k=Action&tag=errorcodefixe-20) |  |------|------------------|--------------|--------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | F01 | Motor overcurrent | [Motor overload or winding fault](https://www.amazon.com/s?k=Motor%20overload%20or%20winding%20fault&tag=errorcodefixe-20) | Check motor amps and winding |
| [F02](https://www.amazon.com/s?k=F02&tag=errorcodefixe-20) | Drive overtemperature | High ambient or blocked cooling | [Clean fins, check fan](https://www.amazon.com/s?k=Clean%20fins%2C%20check%20fan&tag=errorcodefixe-20) |  | F03 | [Motor overtemperature](https://www.amazon.com/s?k=Motor%20overtemperature&tag=errorcodefixe-20) | Motor thermal limit | Check motor cooling and load | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | F04 | Undervoltage | [Low supply voltage](https://www.amazon.com/s?k=Low%20supply%20voltage&tag=errorcodefixe-20) | Check supply voltage |
| [F05](https://www.amazon.com/s?k=F05&tag=errorcodefixe-20) | Overvoltage | Supply voltage high | [Check voltage supply](https://www.amazon.com/s?k=Check%20voltage%20supply&tag=errorcodefixe-20) |  | F06 | [Input phase loss](https://www.amazon.com/s?k=Input%20phase%20loss&tag=errorcodefixe-20) | Missing supply phase | Check input fuses and supply | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | F07 | Ground fault | [Winding or cable insulation fault](https://www.amazon.com/s?k=Winding%20or%20cable%20insulation%20fault&tag=errorcodefixe-20) | Megger test motor |
| [F08](https://www.amazon.com/s?k=F08&tag=errorcodefixe-20) | Communication fault | BAS or Bluetooth loss | [Check BAS wiring](https://www.amazon.com/s?k=Check%20BAS%20wiring&tag=errorcodefixe-20) |  | F09 | [Sensor fault](https://www.amazon.com/s?k=Sensor%20fault&tag=errorcodefixe-20) | Pressure sensor failure | Check sensor wiring and calibration | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | F10 | Low flow warning | [Flow below minimum](https://www.amazon.com/s?k=Flow%20below%20minimum&tag=errorcodefixe-20) | Check system valves and demand |
| [F11](https://www.amazon.com/s?k=F11&tag=errorcodefixe-20) | Pump blocked | Impeller jam | [Check for debris in casing](https://www.amazon.com/s?k=Check%20for%20debris%20in%20casing&tag=errorcodefixe-20) |  | F12 | [Dry run](https://www.amazon.com/s?k=Dry%20run&tag=errorcodefixe-20) | No water detected | Check system pressure and fill | [## Most Common Armstrong Faults

### F01 — Motor Overcurrent
Armstrong Design Envelope pumps are sized for specific system curves. If system resistance increases (closed balancing valve, clogged strainer), current increases. Check system strainer (typically Y-strainer on pump inlet) — clean if dirty. Verify pump impeller diameter matches design conditions.

### F02 — Drive Overtemperature
The integrated VFD must have adequate airflow. Armstrong Design Envelope pumps should be installed with a minimum 6-inch clearance above and below the drive section. In hot mechanical rooms, add auxiliary cooling if ambient exceeds 40°C.

### F09 — Sensor Fault
Armstrong Design Envelope uses differential pressure sensors for automatic control. Check sensor tubing for blockage or air locks. Verify 4–20 mA signal at controller. Clean sensor pressure ports if system has debris.

### F12 — Dry Run
System water pressure below minimum triggers dry run protection. Check fill pressure (minimum 12 PSI for closed hydronic systems). Check for open drain valves or system leaks.

## Parts Commonly Needed](https://www.amazon.com/s?k=%23%23%20Most%20Common%20Armstrong%20Faults%0A%0A%23%23%23%20F01%20%E2%80%94%20Motor%20Overcurrent%0AArmstrong%20Design%20Envelope%20pumps%20are%20sized%20for%20specific%20system%20curves.%20If%20system%20resistance%20increases%20(closed%20balancing%20valve%2C%20clogged%20strainer)%2C%20current%20increases.%20Check%20system%20strainer%20(typically%20Y-strainer%20on%20pump%20inlet)%20%E2%80%94%20clean%20if%20dirty.%20Verify%20pump%20impeller%20diameter%20matches%20design%20conditions.%0A%0A%23%23%23%20F02%20%E2%80%94%20Drive%20Overtemperature%0AThe%20integrated%20VFD%20must%20have%20adequate%20airflow.%20Armstrong%20Design%20Envelope%20pumps%20should%20be%20installed%20with%20a%20minimum%206-inch%20clearance%20above%20and%20below%20the%20drive%20section.%20In%20hot%20mechanical%20rooms%2C%20add%20auxiliary%20cooling%20if%20ambient%20exceeds%2040%C2%B0C.%0A%0A%23%23%23%20F09%20%E2%80%94%20Sensor%20Fault%0AArmstrong%20Design%20Envelope%20uses%20differential%20pressure%20sensors%20for%20automatic%20control.%20Check%20sensor%20tubing%20for%20blockage%20or%20air%20locks.%20Verify%204%E2%80%9320%20mA%20signal%20at%20controller.%20Clean%20sensor%20pressure%20ports%20if%20system%20has%20debris.%0A%0A%23%23%23%20F12%20%E2%80%94%20Dry%20Run%0ASystem%20water%20pressure%20below%20minimum%20triggers%20dry%20run%20protection.%20Check%20fill%20pressure%20(minimum%2012%20PSI%20for%20closed%20hydronic%20systems).%20Check%20for%20open%20drain%20valves%20or%20system%20leaks.%0A%0A%23%23%20Parts%20Commonly%20Needed&tag=errorcodefixe-20) | Part | Notes | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------ |-------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Drive assembly | Armstrong-specific VFD — contact Armstrong | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Pressure sensor | Differential pressure transducer | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Motor seal kit | Annual replacement on higher-flow models | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Impeller | Match pump model and size | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Y-strainer basket | Clean or replace — prevents F11 and F12 |

> **Pro tip:** Armstrong Design Envelope pumps with Pump Manager technology log operational data. Register the pump with Armstrong Fluid Technology's cloud portal for remote monitoring, fault alerts, and efficiency trending accessible from any browser.
