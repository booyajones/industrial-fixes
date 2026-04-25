---
title: "Schneider Modicon M340 PLC Common Error Codes"
description: "Schneider Modicon M340 PLC error codes and diagnostic LEDs explained. Learn how to identify I/O faults, communication errors, CPU faults, and power supply problems."
pubDatetime: 2026-04-22T18:00:00Z
modDatetime: 2026-04-22T18:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - schneider
  - modicon
  - plc
  - m340
  - error-code
  - industrial
---

## Schneider Modicon M340 PLC Error Codes

The Schneider Electric Modicon M340 is a mid-range PLC platform using the Unity Pro (now EcoStruxure Control Expert) programming environment. Faults are indicated through **front-panel LEDs**, **Unity Pro diagnostic screen**, and **system words** accessible in the ladder/FB program.

## M340 CPU LED Indicators

| LED | State | Meaning |
|---|---|---|
| RUN | Green solid | Application running normally |
| RUN | Green blinking | Standby or stopped |
| ERR | Red solid | Fatal error — CPU stopped |
| ERR | Red blinking | Non-fatal error (application continues) |
| I/O | Yellow solid | I/O module fault |
| I/O | Yellow blinking | I/O communication intermittent |
| ETH | Green solid | Ethernet link active |
| ETH | Green blinking | Ethernet activity |
| BAT | Red | Battery low (backup battery) |
| MEM | Yellow | Memory card issue |

## Common M340 Error Codes (via Unity Pro / Control Expert)

### CPU Faults

| [Fault Code](https://www.amazon.com/s?k=Fault+Code&tag=errorcodefixes-20) | Description | Action |
|---|---|---|
| 1 | Internal CPU fault | Power cycle, check firmware version |
| 2 | Memory fault | Check application download, replace SDRAM |
| 3 | Configuration error | Re-download application from Control Expert |
| 4 | I/O configuration mismatch | Verify rack hardware matches project config |
| 5 | Communication module fault | Check module seating, replace if needed |
| 10 | Watchdog timeout | Program scan time exceeded — optimize code |
| 11 | Task overflow | Mast/fast task overrun — reduce scan load |
| 20 | Power supply fault | Check 24VDC supply to CPU bus |

### I/O Module Faults

| [Fault](https://www.amazon.com/s?k=Fault&tag=errorcodefixes-20) | Cause | Fix |
|---|---|---|
| [Module not present](https://www.amazon.com/s?k=Module+not+present&tag=errorcodefixes-20) | Module removed or loose | Reseat module, check card guides |
| [Module configuration error](https://www.amazon.com/s?k=Module+configuration+error&tag=errorcodefixes-20) | Wrong module type in slot | Update hardware configuration in project |
| [Channel fault](https://www.amazon.com/s?k=Channel+fault&tag=errorcodefixes-20) | Individual I/O channel failure | Test wiring on channel; replace module if channel is burned |
| [Bus communication lost](https://www.amazon.com/s?k=Bus+communication+lost&tag=errorcodefixes-20) | Backplane fault or module hardware failure | Replace module; check backplane ribbon |

### Ethernet/Communication Faults

| [Fault](https://www.amazon.com/s?k=Fault&tag=errorcodefixes-20) | Meaning |
|---|---|
| [IP conflict](https://www.amazon.com/s?k=IP+conflict&tag=errorcodefixes-20) | Two devices with same IP on network |
| [No heartbeat from master](https://www.amazon.com/s?k=No+heartbeat+from+master&tag=errorcodefixes-20) | EtherNet/IP or Modbus TCP scanner not polling |
| [Time-out on remote I/O](https://www.amazon.com/s?k=Time-out+on+remote+I%2FO&tag=errorcodefixes-20) | Distributed Quantum or X80 remote I/O not responding |

## Accessing Faults in Control Expert (Unity Pro)

**Online fault display:**
1. Connect to the PLC with Control Expert (online mode)
2. Open **Diagnostic Viewer** (View → Diagnostic Viewer)
3. Review the fault table — faults listed by type, module, and timestamp

**System words:**
- `%SW125` — Mast task watchdog status
- `%SW116` — Last application error code
- `%SW117` — Last I/O error code
- `%SW124` — Configuration error code

## Watchdog / Task Overflow (Code 10/11)

Task overflow is common after large program changes. The M340 Mast task has a watchdog timeout (default 250 ms). If the scan takes longer, the CPU stops and ERR LED flashes.

Fix options:
1. Increase watchdog timeout in project settings (CPU properties → Tasks → Mast → Watchdog)
2. Move non-critical logic to Event or Fast tasks
3. Optimize loops — avoid large FOR loops inside Mast task
4. Check for runaway indirect addressing

## Battery Replacement (BAT LED)

The M340 CPU uses a CR2032 or similar lithium cell to retain program data during power loss. When BAT LED illuminates:
1. Download the application from Control Expert as backup
2. Power the PLC on
3. Replace battery while powered (hot-swap within 1 minute on most models)
4. M340 battery: Schneider P/N TSX MBP 100 or equivalent CR2032 3V lithium

## Firmware Updates

M340 CPUs run embedded firmware. Firmware mismatch between CPU and I/O modules can cause intermittent faults. Use Control Expert → Tools → Firmware Update to check and update.

## Emergency Recovery

If the CPU won't start (ERR solid, no RUN):
1. Clear memory: hold CLEAR button (if present) during power cycle
2. Transfer application from Control Expert in PROGRAM mode first, then switch to RUN
3. If SDRAM failure is suspected, contact Schneider Electric technical support — memory cannot be field-replaced on most M340 CPUs
