---
title: "Siemens SIPROTEC Protective Relay Faults: Complete Guide"
description: "Siemens SIPROTEC relay faults and diagnostic messages. Hardware, communication, and protection faults with technician-level troubleshooting steps."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-04-22T23:45:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - electrical
  - siemens
  - protective-relay
  - power-quality
---

# Siemens SIPROTEC Protective Relay Faults

Siemens SIPROTEC relays protect feeders, transformers, generators, and transmission lines. Faults appear on the front display, in DIGSI, or through SCADA event logs. Most problems fall into three buckets: protection trips caused by real system events, hardware alarms inside the relay, and communication faults between the relay and the station network.

## Common SIPROTEC Fault Table

| [Fault](https://www.amazon.com/s?k=Fault&tag=errorcodefixe-20) | Meaning | Common Cause | [Action](https://www.amazon.com/s?k=Action&tag=errorcodefixe-20) |  |------|---------|--------------|--------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Hardware fault | Internal relay hardware problem | [Power supply, CPU, or I/O board issue](https://www.amazon.com/s?k=Power%20supply%2C%20CPU%2C%20or%20I%2FO%20board%20issue&tag=errorcodefixe-20) | Review self-test log in DIGSI |
| [Time sync fault](https://www.amazon.com/s?k=Time%20sync%20fault&tag=errorcodefixe-20) | Clock synchronization lost | IRIG-B, SNTP, or GPS source failure | [Check time source and wiring](https://www.amazon.com/s?k=Check%20time%20source%20and%20wiring&tag=errorcodefixe-20) |  | Battery fault | [Backup battery weak](https://www.amazon.com/s?k=Backup%20battery%20weak&tag=errorcodefixe-20) | Aging battery on older models | Replace battery if model uses one | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Comm fault | SCADA or IEC 61850 communication lost | [Ethernet issue, switch problem, bad settings](https://www.amazon.com/s?k=Ethernet%20issue%2C%20switch%20problem%2C%20bad%20settings&tag=errorcodefixe-20) | Check link lights and network config |
| [CT circuit fault](https://www.amazon.com/s?k=CT%20circuit%20fault&tag=errorcodefixe-20) | Current input abnormal | Open CT secondary or wiring error | [Check CT wiring immediately](https://www.amazon.com/s?k=Check%20CT%20wiring%20immediately&tag=errorcodefixe-20) |  | VT circuit fault | [Voltage input abnormal](https://www.amazon.com/s?k=Voltage%20input%20abnormal&tag=errorcodefixe-20) | Blown fuse, PT loss, wiring error | Check PT fuses and inputs | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Trip circuit supervision | Trip circuit open | [Open trip coil circuit or blown fuse](https://www.amazon.com/s?k=Open%20trip%20coil%20circuit%20or%20blown%20fuse&tag=errorcodefixe-20) | Check breaker trip circuit continuity |
| [Relay blocked](https://www.amazon.com/s?k=Relay%20blocked&tag=errorcodefixe-20) | Protection element blocked | Interlock active or setting group logic | [Review binary inputs and logic](https://www.amazon.com/s?k=Review%20binary%20inputs%20and%20logic&tag=errorcodefixe-20) |  | Self test failed | [Relay internal diagnostic failed](https://www.amazon.com/s?k=Relay%20internal%20diagnostic%20failed&tag=errorcodefixe-20) | Firmware, memory, or board issue | Reboot and inspect diagnostics | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Disturbance record full | Event memory full | [Oscillography not exported](https://www.amazon.com/s?k=Oscillography%20not%20exported&tag=errorcodefixe-20) | Download and clear records |
| [Setting group error](https://www.amazon.com/s?k=Setting%20group%20error&tag=errorcodefixe-20) | Invalid setting or mismatch | Bad parameter set or import | [Compare active setting group](https://www.amazon.com/s?k=Compare%20active%20setting%20group&tag=errorcodefixe-20) |  | Breaker failure start | [Breaker did not clear fault](https://www.amazon.com/s?k=Breaker%20did%20not%20clear%20fault&tag=errorcodefixe-20) | Breaker mechanism or trip circuit issue | Check breaker timing and trip coil | [## Most Common SIPROTEC Faults

### Trip Circuit Supervision Alarm
This is one of the most common relay alarms in the field. The relay monitors continuity through the breaker trip coil. If the trip path opens, the relay raises an alarm. Check trip coil resistance, breaker control fuses, and all terminal screws in the trip circuit.

### CT Circuit Fault
Treat CT circuit alarms seriously. An open CT secondary can create dangerous voltage. Inspect terminal blocks, shorting blocks, and test switches before touching wiring. Confirm the relay sees expected current on all phases after repairs.

### Communication Fault
For IEC 61850 stations, start with the physical layer. Check switch port status, relay link LEDs, fiber jumpers, and IP settings. In DIGSI, review the communication diagnostics to confirm whether the fault is MMS, GOOSE, or time sync related.

### Hardware Fault
SIPROTEC relays run internal self-tests. If a hardware fault appears, capture the exact message before power-cycling. Export the fault buffer and disturbance records. Repeated hardware faults usually point to a failing power supply or main processing board.

## Parts Commonly Needed](https://www.amazon.com/s?k=%23%23%20Most%20Common%20SIPROTEC%20Faults%0A%0A%23%23%23%20Trip%20Circuit%20Supervision%20Alarm%0AThis%20is%20one%20of%20the%20most%20common%20relay%20alarms%20in%20the%20field.%20The%20relay%20monitors%20continuity%20through%20the%20breaker%20trip%20coil.%20If%20the%20trip%20path%20opens%2C%20the%20relay%20raises%20an%20alarm.%20Check%20trip%20coil%20resistance%2C%20breaker%20control%20fuses%2C%20and%20all%20terminal%20screws%20in%20the%20trip%20circuit.%0A%0A%23%23%23%20CT%20Circuit%20Fault%0ATreat%20CT%20circuit%20alarms%20seriously.%20An%20open%20CT%20secondary%20can%20create%20dangerous%20voltage.%20Inspect%20terminal%20blocks%2C%20shorting%20blocks%2C%20and%20test%20switches%20before%20touching%20wiring.%20Confirm%20the%20relay%20sees%20expected%20current%20on%20all%20phases%20after%20repairs.%0A%0A%23%23%23%20Communication%20Fault%0AFor%20IEC%2061850%20stations%2C%20start%20with%20the%20physical%20layer.%20Check%20switch%20port%20status%2C%20relay%20link%20LEDs%2C%20fiber%20jumpers%2C%20and%20IP%20settings.%20In%20DIGSI%2C%20review%20the%20communication%20diagnostics%20to%20confirm%20whether%20the%20fault%20is%20MMS%2C%20GOOSE%2C%20or%20time%20sync%20related.%0A%0A%23%23%23%20Hardware%20Fault%0ASIPROTEC%20relays%20run%20internal%20self-tests.%20If%20a%20hardware%20fault%20appears%2C%20capture%20the%20exact%20message%20before%20power-cycling.%20Export%20the%20fault%20buffer%20and%20disturbance%20records.%20Repeated%20hardware%20faults%20usually%20point%20to%20a%20failing%20power%20supply%20or%20main%20processing%20board.%0A%0A%23%23%20Parts%20Commonly%20Needed&tag=errorcodefixe-20) | Part | Notes | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------ |-------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Relay power supply module | Match exact SIPROTEC model | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Front communication cable | Needed for local DIGSI connection | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Test switch block | Useful when CT/VT circuits require safe isolation | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Backup battery | Older models only | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Ethernet SFP or patch cord | Check station network media type |

> **Pro tip:** Pull the event log and disturbance record before you clear anything. SIPROTEC relays capture precise timing, target bits, and oscillography. That data tells you whether the relay saw a real power system event or an internal problem.
