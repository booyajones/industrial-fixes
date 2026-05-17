---
title: "Allen-Bradley MicroLogix 1400 Common Fault Codes"
description: "Allen-Bradley MicroLogix 1400 fault codes explained. Learn how to diagnose and clear major/minor faults using RSLogix 500, LED indicators, and the LCD display."
pubDatetime: 2026-04-22T18:00:00Z
modDatetime: 2026-04-22T18:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - allen-bradley
  - micrologix
  - plc
  - rockwell
  - fault-code
  - industrial
---

## Allen-Bradley MicroLogix 1400 Fault Codes

The Allen-Bradley MicroLogix 1400 (1766-L32AWA, 1766-L32BXB, etc.) is a compact PLC from Rockwell Automation. It uses RSLogix 500 / Studio 5000 Logix Designer for programming and fault diagnosis. Faults appear on the **built-in LCD display**, **front-panel LEDs**, and in the **fault routine** accessible via software.

## Front Panel LED Status

| LED | Color/State | Meaning |
|---|---|---|
| RUN | Green solid | Application executing |
| RUN | Off | Processor stopped / faulted |
| FLT | Red solid | Major fault — CPU halted |
| FLT | Red blink | Minor fault — CPU running |
| [BATT](https://www.amazon.com/s?i=industrial&k=BATT&tag=errorcodefixes-20) | Red | Replace battery immediately |
| [COMM1/COMM2](https://www.amazon.com/s?i=industrial&k=COMM1%2FCOMM2&tag=errorcodefixes-20) | Yellow blink | Serial/EtherNet activity |
| [FORCE](https://www.amazon.com/s?i=industrial&k=FORCE&tag=errorcodefixes-20) | Yellow | I/O forces active |

## Major Fault Codes (0000–0FFF)

Major faults halt the CPU. The FLT LED goes solid red.

| [Code](https://www.amazon.com/s?i=industrial&k=Code&tag=errorcodefixes-20) | Type | Description |
|---|---|---|
| [0004](https://www.amazon.com/s?i=industrial&k="0004"&tag=errorcodefixes-20) | Configuration | I/O configuration file error |
| [0006](https://www.amazon.com/s?i=industrial&k="0006"&tag=errorcodefixes-20) | Configuration | EE read error during power cycle |
| [0007](https://www.amazon.com/s?i=industrial&k="0007"&tag=errorcodefixes-20) | Configuration | Watchdog timeout |
| [0008](https://www.amazon.com/s?i=industrial&k="0008"&tag=errorcodefixes-20) | Configuration | Internal processor fault |
| [0020](https://www.amazon.com/s?i=industrial&k="0020"&tag=errorcodefixes-20) | Instruction | Illegal instruction execution |
| [0021](https://www.amazon.com/s?i=industrial&k="0021"&tag=errorcodefixes-20) | Instruction | Division by zero |
| [0022](https://www.amazon.com/s?i=industrial&k="0022"&tag=errorcodefixes-20) | Instruction | Illegal slot or address |
| [0030](https://www.amazon.com/s?i=industrial&k="0030"&tag=errorcodefixes-20) | I/O | Local I/O communication fault |
| [0031](https://www.amazon.com/s?i=industrial&k="0031"&tag=errorcodefixes-20) | I/O | I/O module failure |
| [0042](https://www.amazon.com/s?i=industrial&k="0042"&tag=errorcodefixes-20) | Program | Control stack overflow (too many nested subroutines) |
| [0043](https://www.amazon.com/s?i=industrial&k="0043"&tag=errorcodefixes-20) | Program | Subroutine nesting fault |
| [0060](https://www.amazon.com/s?i=industrial&k="0060"&tag=errorcodefixes-20) | Memory | RAM fault |
| [0080](https://www.amazon.com/s?i=industrial&k="0080"&tag=errorcodefixes-20) | CPU | Math coprocessor fault |

## Minor Fault Codes

Minor faults are logged but the CPU keeps running (FLT LED blinks).

| [Code](https://www.amazon.com/s?i=industrial&k=Code&tag=errorcodefixes-20) | Description |
|---|---|
| [0081](https://www.amazon.com/s?i=industrial&k="0081"&tag=errorcodefixes-20) | Battery low |
| [0082](https://www.amazon.com/s?i=industrial&k="0082"&tag=errorcodefixes-20) | RTC (real time clock) error |
| [0085](https://www.amazon.com/s?i=industrial&k="0085"&tag=errorcodefixes-20) | I/O module not responding (still scanned) |
| [0090](https://www.amazon.com/s?i=industrial&k="0090"&tag=errorcodefixes-20) | User-defined fault (triggered by fault instruction in ladder) |
| [00A0](https://www.amazon.com/s?i=industrial&k="00A0"&tag=errorcodefixes-20) | Communication timeout on serial port |

## Reading Faults via LCD Display

The MicroLogix 1400 has a built-in 4-line LCD display on the front panel. When a fault occurs:
1. The display shows **FAULT** and a fault code
2. Press the **ESC** key to navigate to the fault info screen
3. The display shows the fault code (hex) and description

## Clearing Faults in RSLogix 500

1. Go online with RSLogix 500 (Communications → Go Online)
2. Navigate to **Controller Properties → General**
3. Under Status, look for Major Fault / Minor Fault
4. Click **Clear Faults** button
5. Switch controller to RUN mode

Or clear via ladder: use the **CLR** instruction with `S:12` (major fault word) or use the dedicated clear fault instruction in your fault routine (LAD 3).

## Fault Routine — LAD 3

The MicroLogix 1400 has a dedicated **fault subroutine** (LAD 3 by default). You can program automatic fault handling here:
- Log fault code to data file
- Energize a fault output (alarm light, beacon)
- Conditionally clear minor faults with `CLR S:5` (status word)
- For catastrophic faults, halt safely rather than fault-clearing

Leave LAD 3 empty if you want all faults to halt the CPU immediately (safest for machines).

## Battery Replacement

| Part | Rockwell P/N | Standard |
|---|---|---|
| [Lithium battery](https://www.amazon.com/s?i=industrial&k=Lithium+battery&tag=errorcodefixes-20) | 1769-BA | 3V CR-2032 equivalent |

Replace with power ON to retain RAM. The capacitor backup holds RAM for about 1 minute. Replace battery every 3–5 years or when BATT LED illuminates.

## Watchdog Timeout (Code 0007)

The MicroLogix 1400 watchdog default is **100 ms**. If the scan time exceeds this, fault 0007 triggers.

Fix options:
1. Open RSLogix 500 → Controller Properties → Advanced → Watchdog timer — increase to 500 ms or 1000 ms
2. Optimize ladder logic — reduce scan time
3. Check for infinite loops in SBR/JSR instructions
4. Move slow I/O reads to an event or interrupt routine

## Communication Faults (00A0)

If you're losing communication with the MicroLogix 1400 over RS-232/RS-485:
1. Verify baud rate matches on both ends (9600 default)
2. Check cable pinout (DF1 null modem or straight through depending on device)
3. Verify driver configuration in RSLinx Classic
4. Check for ground loops on long RS-485 runs

For EtherNet/IP: verify IP address isn't conflicting and the routing table in RSLinx is correct.

## Related Articles

- [Allen-Bradley PowerFlex 40 Complete Fault Code Guide](/posts/allen-bradley-powerflex-40-complete-guide/)
- [Allen Bradley PowerFlex 40 F2 Fault — Causes & Fix](/posts/allen-bradley-powerflex-40-f2-fault/)
- [Allen-Bradley PowerFlex 40 F3 Fault — Power Loss](/posts/allen-bradley-powerflex-40-f3/)
- [Allen Bradley PowerFlex 40 F7 Fault — Causes & Fix](/posts/allen-bradley-powerflex-40-f7-fault/)
- [Allen-Bradley PowerFlex 4M Fault Codes — F2, F4, F5, F7, F12 Fix Guide](/posts/allen-bradley-powerflex-4m-fault-codes/)
