---
title: "Wilo Circulator Pump Fault Codes: Complete Guide"
description: "Wilo circulator pump fault codes and error diagnostics. LED indicator codes, fault causes, and technician-level troubleshooting for Wilo pumps."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-04-22T23:45:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - pumps
  - wilo
  - hvac
  - industrial
---

# Wilo Circulator Pump Fault Codes

Wilo circulator pumps (Stratos, TOP-S, Yonos, and commercial series) communicate faults via LED indicators and, on advanced models, a display panel. Wilo pumps are widely used in HVAC hydronic systems, district heating, and industrial circulation.

## Wilo Stratos/TOP Series Fault Code Table

| [LED/Code](https://www.amazon.com/s?k=LED%2FCode&tag=errorcodefixe-20) | Fault Description | Common Cause | [Action](https://www.amazon.com/s?k=Action&tag=errorcodefixe-20) |  |----------|------------------|--------------|--------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Red LED steady | Fault/lockout | [Overtemperature, blocked impeller](https://www.amazon.com/s?k=Overtemperature%2C%20blocked%20impeller&tag=errorcodefixe-20) | Check fluid temp, clear blockage |
| [Red LED flashing](https://www.amazon.com/s?k=Red%20LED%20flashing&tag=errorcodefixe-20) | Warning | Fault present but pump running | [Read fault via Wilo-Net or display](https://www.amazon.com/s?k=Read%20fault%20via%20Wilo-Net%20or%20display&tag=errorcodefixe-20) |  | E01 | [Blocked pump](https://www.amazon.com/s?k=Blocked%20pump&tag=errorcodefixe-20) | Impeller locked or air-locked | Vent system, check for debris | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | E02 | Overtemperature | [Fluid temp too high](https://www.amazon.com/s?k=Fluid%20temp%20too%20high&tag=errorcodefixe-20) | Check system temp, verify bypass |
| [E03](https://www.amazon.com/s?k=E03&tag=errorcodefixe-20) | Dry run | No fluid detected | [Fill and vent system](https://www.amazon.com/s?k=Fill%20and%20vent%20system&tag=errorcodefixe-20) |  | E04 | [Undervoltage](https://www.amazon.com/s?k=Undervoltage&tag=errorcodefixe-20) | Supply below minimum | Check power supply | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | E05 | Overvoltage | [Supply above maximum](https://www.amazon.com/s?k=Supply%20above%20maximum&tag=errorcodefixe-20) | Check power supply |
| [E06](https://www.amazon.com/s?k=E06&tag=errorcodefixe-20) | Motor overload | Excessive load or stall | [Check mechanical load](https://www.amazon.com/s?k=Check%20mechanical%20load&tag=errorcodefixe-20) |  | E07 | [Electronic fault](https://www.amazon.com/s?k=Electronic%20fault&tag=errorcodefixe-20) | Internal board fault | Contact Wilo service | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | E10 | Communication fault | [Wilo-Net or BACnet/Modbus error](https://www.amazon.com/s?k=Wilo-Net%20or%20BACnet%2FModbus%20error&tag=errorcodefixe-20) | Check network wiring |
| [E11](https://www.amazon.com/s?k=E11&tag=errorcodefixe-20) | Sensor fault | Differential pressure sensor failure | [Check sensor connections](https://www.amazon.com/s?k=Check%20sensor%20connections&tag=errorcodefixe-20) |  | E12 | [Under-flow](https://www.amazon.com/s?k=Under-flow&tag=errorcodefixe-20) | Flow below minimum setpoint | Check system for closed valves | [## Most Common Wilo Pump Faults

### E01 — Blocked Pump
Wilo circulators are maintenance-free, but system contamination can jam the impeller. Shut off the pump, isolate with service valves, and remove the motor head from the pump body. Check for debris in the impeller chamber. Also check for air lock — purge the pump air vent screw (typically on top of pump body) while system is running.

### E02 — Overtemperature
Wilo Stratos pumps are rated to 95°C fluid temperature. If system temperature exceeds rating, the pump locks out. Check the system boiler or heat source temperature controller. Also verify the pump is not installed in an orientation where it traps heat.

### E03 — Dry Run
Dry run protection prevents pump damage when the system runs low on water. Check system fill pressure (minimum 12 PSI for most closed-loop hydronic systems). Check backflow preventer fill valve. If system recently drained, re-fill and bleed air from highest points.

### E10 — Communication Fault
Wilo pumps with Wilo-Net, BACnet, or Modbus connectivity will fault if the building automation system (BAS) loses communication. Check network wiring at the pump terminal block and verify BAS controller is online.

## Parts Commonly Needed](https://www.amazon.com/s?k=%23%23%20Most%20Common%20Wilo%20Pump%20Faults%0A%0A%23%23%23%20E01%20%E2%80%94%20Blocked%20Pump%0AWilo%20circulators%20are%20maintenance-free%2C%20but%20system%20contamination%20can%20jam%20the%20impeller.%20Shut%20off%20the%20pump%2C%20isolate%20with%20service%20valves%2C%20and%20remove%20the%20motor%20head%20from%20the%20pump%20body.%20Check%20for%20debris%20in%20the%20impeller%20chamber.%20Also%20check%20for%20air%20lock%20%E2%80%94%20purge%20the%20pump%20air%20vent%20screw%20(typically%20on%20top%20of%20pump%20body)%20while%20system%20is%20running.%0A%0A%23%23%23%20E02%20%E2%80%94%20Overtemperature%0AWilo%20Stratos%20pumps%20are%20rated%20to%2095%C2%B0C%20fluid%20temperature.%20If%20system%20temperature%20exceeds%20rating%2C%20the%20pump%20locks%20out.%20Check%20the%20system%20boiler%20or%20heat%20source%20temperature%20controller.%20Also%20verify%20the%20pump%20is%20not%20installed%20in%20an%20orientation%20where%20it%20traps%20heat.%0A%0A%23%23%23%20E03%20%E2%80%94%20Dry%20Run%0ADry%20run%20protection%20prevents%20pump%20damage%20when%20the%20system%20runs%20low%20on%20water.%20Check%20system%20fill%20pressure%20(minimum%2012%20PSI%20for%20most%20closed-loop%20hydronic%20systems).%20Check%20backflow%20preventer%20fill%20valve.%20If%20system%20recently%20drained%2C%20re-fill%20and%20bleed%20air%20from%20highest%20points.%0A%0A%23%23%23%20E10%20%E2%80%94%20Communication%20Fault%0AWilo%20pumps%20with%20Wilo-Net%2C%20BACnet%2C%20or%20Modbus%20connectivity%20will%20fault%20if%20the%20building%20automation%20system%20(BAS)%20loses%20communication.%20Check%20network%20wiring%20at%20the%20pump%20terminal%20block%20and%20verify%20BAS%20controller%20is%20online.%0A%0A%23%23%20Parts%20Commonly%20Needed&tag=errorcodefixe-20) | Part | Notes | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------ |-------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Impeller assembly | Match pump model and impeller diameter | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Electronic insert (motor head) | Full replacement motor assembly | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Wilo-Net gateway | For BAS integration | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Pressure sensor | Differential pressure transducer for variable speed control | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Service kit | Seal and O-ring set |

> **Pro tip:** Wilo Stratos and high-efficiency models have a built-in energy monitoring function. Track pump power consumption via the display or Wilo-Net — a sudden increase in power often indicates a developing fault (worn bearing, increased system resistance) before an alarm occurs.
