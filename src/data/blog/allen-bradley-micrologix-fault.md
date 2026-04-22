---
title: "Allen-Bradley MicroLogix 1400 Common Fault Codes"
description: "Allen-Bradley MicroLogix 1400 fault codes explained. Learn how to diagnose and clear major/minor faults using RSLogix 500, LED indicators, and the LCD display."
pubDatetime: 2026-04-22T18:00:00Z
modDatetime: 2026-04-22T18:00:00Z
author: "ErrorCodeFixes"
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

| [LED](https://www.amazon.com/s?k=LED&tag=errorcodefixe-20) | Color/State | Meaning | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | --- |---|---|
| RUN | [Green solid](https://www.amazon.com/s?k=Green%20solid&tag=errorcodefixe-20) | Application executing |
| [RUN](https://www.amazon.com/s?k=RUN&tag=errorcodefixe-20) | Off | Processor stopped / faulted | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | FLT | Red solid | [Major fault — CPU halted](https://www.amazon.com/s?k=Major%20fault%20%E2%80%94%20CPU%20halted&tag=errorcodefixe-20) |  | FLT | [Red blink](https://www.amazon.com/s?k=Red%20blink&tag=errorcodefixe-20) | Minor fault — CPU running |
| [BATT](https://www.amazon.com/s?k=BATT&tag=errorcodefixe-20) | Red | Replace battery immediately | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | COMM1/COMM2 | Yellow blink | [Serial/EtherNet activity](https://www.amazon.com/s?k=Serial%2FEtherNet%20activity&tag=errorcodefixe-20) |  | FORCE | [Yellow](https://www.amazon.com/s?k=Yellow&tag=errorcodefixe-20) | I/O forces active |

## Major Fault Codes (0000–0FFF)

Major faults halt the CPU. The FLT LED goes solid red.

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Type | Description | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | --- |---|---|
| 0004 | [Configuration](https://www.amazon.com/s?k=Configuration&tag=errorcodefixe-20) | I/O configuration file error |
| [0006](https://www.amazon.com/s?k=0006&tag=errorcodefixe-20) | Configuration | EE read error during power cycle | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 0007 | Configuration | [Watchdog timeout](https://www.amazon.com/s?k=Watchdog%20timeout&tag=errorcodefixe-20) |  | 0008 | [Configuration](https://www.amazon.com/s?k=Configuration&tag=errorcodefixe-20) | Internal processor fault |
| [0020](https://www.amazon.com/s?k=0020&tag=errorcodefixe-20) | Instruction | Illegal instruction execution | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 0021 | Instruction | [Division by zero](https://www.amazon.com/s?k=Division%20by%20zero&tag=errorcodefixe-20) |  | 0022 | [Instruction](https://www.amazon.com/s?k=Instruction&tag=errorcodefixe-20) | Illegal slot or address |
| [0030](https://www.amazon.com/s?k=0030&tag=errorcodefixe-20) | I/O | Local I/O communication fault | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 0031 | I/O | [I/O module failure](https://www.amazon.com/s?k=I%2FO%20module%20failure&tag=errorcodefixe-20) |  | 0042 | [Program](https://www.amazon.com/s?k=Program&tag=errorcodefixe-20) | Control stack overflow (too many nested subroutines) |
| [0043](https://www.amazon.com/s?k=0043&tag=errorcodefixe-20) | Program | Subroutine nesting fault | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 0060 | Memory | [RAM fault](https://www.amazon.com/s?k=RAM%20fault&tag=errorcodefixe-20) |  | 0080 | [CPU](https://www.amazon.com/s?k=CPU&tag=errorcodefixe-20) | Math coprocessor fault |

## Minor Fault Codes

Minor faults are logged but the CPU keeps running (FLT LED blinks).

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Description |
|---|---|
| [0081](https://www.amazon.com/s?k=0081&tag=errorcodefixe-20) | Battery low |
| [0082](https://www.amazon.com/s?k=0082&tag=errorcodefixe-20) | RTC (real time clock) error |
| [0085](https://www.amazon.com/s?k=0085&tag=errorcodefixe-20) | I/O module not responding (still scanned) |
| [0090](https://www.amazon.com/s?k=0090&tag=errorcodefixe-20) | User-defined fault (triggered by fault instruction in ladder) |
| [00A0](https://www.amazon.com/s?k=00A0&tag=errorcodefixe-20) | Communication timeout on serial port |

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

| Part | Rockwell P/N | Standard | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | --- |---|---|
| Lithium battery | [1769-BA](https://www.amazon.com/s?k=1769-BA&tag=errorcodefixe-20) | 3V CR-2032 equivalent |

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
