---
title: "Siemens S7-300/400 CPU Fault Code Guide"
description: "Siemens S7-300 and S7-400 PLC fault codes explained. Learn how to diagnose STOP mode, hardware errors, and diagnostic buffer entries using STEP 7 and TIA Portal."
pubDatetime: 2026-04-22T18:00:00Z
modDatetime: 2026-04-22T18:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - siemens
  - s7-300
  - s7-400
  - plc
  - fault-code
  - industrial
---

## Siemens S7-300 / S7-400 CPU Fault Codes

Siemens S7-300 and S7-400 PLCs indicate faults through **front-panel LEDs**, the **diagnostic buffer** (accessible via STEP 7 or TIA Portal), and **OB (Organization Block) calls** in the user program. Understanding these layers is key to fast diagnosis.

## Front Panel LED Status

| LED | State | Meaning |
|---|---|---|
| RUN | Green solid | CPU executing program |
| [STOP](https://www.amazon.com/s?i=industrial&k=STOP&tag=errorcodefixes-20) | Yellow solid | CPU stopped (no fault) |
| [STOP](https://www.amazon.com/s?i=industrial&k=STOP&tag=errorcodefixes-20) | Yellow blinking | CPU in STOP due to fault |
| SF | Red solid | System/group fault |
| BF | Red solid | Bus fault (PROFIBUS/DP) |
| [DC5V](https://www.amazon.com/s?i=industrial&k=DC5V&tag=errorcodefixes-20) | Green solid | 5V internal supply OK |
| [FRCE](https://www.amazon.com/s?i=industrial&k=FRCE&tag=errorcodefixes-20) | Yellow | Force mode active |
| [MAINT](https://www.amazon.com/s?i=industrial&k=MAINT&tag=errorcodefixes-20) | Yellow | Maintenance required |

**SF + STOP blinking together = hardware or software fault — read the diagnostic buffer immediately.**

## Reading the Diagnostic Buffer

The diagnostic buffer stores the last 100 events including all faults. Access via:

**STEP 7 (Classic):**
1. Open SIMATIC Manager
2. Right-click CPU → Module Information
3. Select Diagnostic Buffer tab
4. Read fault events in chronological order (most recent at top)

**TIA Portal:**
1. Open project, go online
2. CPU → Diagnostics → Diagnostic Buffer
3. Double-click any event for detailed description

## Common S7 CPU Fault Events

| [Event Code](https://www.amazon.com/s?i=industrial&k=Event+Code&tag=errorcodefixes-20) | Description | Cause |
|---|---|---|
| [16#A502](https://www.amazon.com/s?i=industrial&k=16%23A502&tag=errorcodefixes-20) | Startup complete | Normal — CPU went from STOP to RUN |
| [16#A503](https://www.amazon.com/s?i=industrial&k=16%23A503&tag=errorcodefixes-20) | STOP mode entered | Manual STOP or fault |
| [16#253A](https://www.amazon.com/s?i=industrial&k=16%23253A&tag=errorcodefixes-20) | OB not loaded — CPU stops | Missing OB (e.g., OB82 or OB86 not present) |
| [16#2521](https://www.amazon.com/s?i=industrial&k=16%232521&tag=errorcodefixes-20) | I/O access error | Module missing or failed at accessed address |
| [16#2522](https://www.amazon.com/s?i=industrial&k=16%232522&tag=errorcodefixes-20) | I/O write error | Output module fault |
| [16#2526](https://www.amazon.com/s?i=industrial&k=16%232526&tag=errorcodefixes-20) | Timeout on I/O access | Module not responding |
| [16#A29F](https://www.amazon.com/s?i=industrial&k=16%23A29F&tag=errorcodefixes-20) | Configuration error | Hardware config doesn't match physical racks |
| [16#4500](https://www.amazon.com/s?i=industrial&k=16%234500&tag=errorcodefixes-20) | Rack failure | Module in rack not communicating |
| [16#4B00](https://www.amazon.com/s?i=industrial&k=16%234B00&tag=errorcodefixes-20) | PROFIBUS DP station failure | Remote DP device went offline |
| [16#CAFE](https://www.amazon.com/s?i=industrial&k=16%23CAFE&tag=errorcodefixes-20) | CPU memory card error | Remove and reinstall memory card |

## OB (Organization Block) Error Handling

The S7 calls specific OBs when faults occur. If the OB is **not loaded in the CPU**, the CPU goes to STOP mode instead of handling the fault gracefully.

| OB | Trigger | Common Requirement |
|---|---|---|
| [OB80](https://www.amazon.com/s?i=industrial&k="OB80"&tag=errorcodefixes-20) | Cycle time fault (watchdog) | Needed if cycle time can be exceeded |
| [OB81](https://www.amazon.com/s?i=industrial&k="OB81"&tag=errorcodefixes-20) | Power supply fault | Needed for redundant power supply systems |
| [OB82](https://www.amazon.com/s?i=industrial&k="OB82"&tag=errorcodefixes-20) | Diagnostic interrupt | Needed for intelligent I/O modules with diagnostics |
| [OB83](https://www.amazon.com/s?i=industrial&k="OB83"&tag=errorcodefixes-20) | Insert/remove module | Needed for hot-plug capable systems |
| [OB84](https://www.amazon.com/s?i=industrial&k="OB84"&tag=errorcodefixes-20) | CPU hardware fault | Rare, needed for fault-tolerant systems |
| [OB85](https://www.amazon.com/s?i=industrial&k="OB85"&tag=errorcodefixes-20) | Program sequence fault | Load OB to prevent CPU stop on error |
| [OB86](https://www.amazon.com/s?i=industrial&k="OB86"&tag=errorcodefixes-20) | Loss of rack / DP station | **Most commonly missing** — add empty OB86 |
| [OB122](https://www.amazon.com/s?i=industrial&k="OB122"&tag=errorcodefixes-20) | I/O access error | Load to prevent stop on missing I/O |

**Fastest fix for "OB not loaded" stops:** Create an empty OB with the required number and download it to the CPU.

## PROFIBUS DP Fault (BF LED)

The BF LED indicates a PROFIBUS bus fault. Common causes:
- DP slave device powered off or disconnected
- Termination resistors missing at both ends of the DP bus
- Cable damaged or shielding broken
- Address conflict between DP slaves
- PROFIBUS speed mismatch (configured vs. actual)

Diagnostic: Read the diagnostic buffer for event 16#4B00 — it includes the DP address of the failed station.

## I/O Access Error (16#2521)

The CPU tried to read or write an I/O address that doesn't exist or belongs to a failed module.

Fix:
1. Check the physical hardware at the failing slot number (diagnostic buffer includes slot/address)
2. Remove and reseat the module
3. Verify the STEP 7 hardware configuration matches physical rack layout
4. If module is failed, replace it

## Watchdog / Cycle Time Fault (OB80)

Default cycle time on S7-300: **150 ms**. S7-400: **6000 ms**. If exceeded, OB80 is called. If OB80 is missing, CPU stops.

Fix:
1. Load an empty or logging OB80
2. Increase maximum cycle time in CPU properties (right-click CPU → Object Properties → Cycle/Clock Memory)
3. Optimize scan-heavy loops — avoid large FOR loops in OB1

## S7-400H (Redundant) Specific Faults

S7-400H fault events include redundancy state changes:
- `16#673E` — Master/standby switchover
- `16#6733` — H system partially degraded

These are not always errors — some are expected during updates or hardware changes. Check if the switchover was planned.

## Related Articles

- [Siemens Sinumerik 828D Alarm Codes Guide — Complete Diagnostic Reference](/posts/siemens-828d-alarm-codes/)
- [Siemens 840D Alarm 380000 — Causes & Fix](/posts/siemens-840d-alarm-380000/)
- [Siemens Circuit Breaker Fault Codes - Complete Guide](/posts/siemens-circuit-breaker-fault-codes/)
- [Siemens Desigo BMS Fault Codes - Complete Guide](/posts/siemens-desigo-fault-codes/)
- [Siemens Cerberus/MXL Fire Alarm Fault Codes — Troubleshooting Guide](/posts/siemens-fire-alarm-fault-codes/)
