---
title: "Schweitzer SEL Relay Fault Codes — SEL-700 / SEL-351 Guide"
description: "Schweitzer Engineering Laboratories (SEL) protective relay fault codes and event records for SEL-700, SEL-351, SEL-387, and SEL-411 series relays."
pubDatetime: 2026-04-22T21:00:00Z
modDatetime: 2026-04-22T21:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - protective-relay
  - schweitzer
  - sel
  - power-distribution
---

## Schweitzer SEL Relay Fault Codes — Quick Reference

SEL relays record trip events using IEEE standard protection element numbers and SELOGIC-based event reports accessible via the front panel, ACSELERATOR QuickSet software, or EtherNet/IP/Modbus.

| [Element](https://www.amazon.com/s?i=industrial&k=Element&tag=errorcodefixes-20) | Function | Common Cause |
|---------|---------|-------------|
| [50 — Instantaneous OC](https://www.amazon.com/s?i=industrial&k=50+%E2%80%94+Instantaneous+OC&tag=errorcodefixes-20) | Fault current above pickup | Short circuit near relay |
| [51 — Time Overcurrent](https://www.amazon.com/s?i=industrial&k=51+%E2%80%94+Time+Overcurrent&tag=errorcodefixes-20) | Sustained overcurrent | Overload or slow-clearing fault |
| [67 — Directional OC](https://www.amazon.com/s?i=industrial&k=67+%E2%80%94+Directional+OC&tag=errorcodefixes-20) | Fault current direction | Reverse fault or backfeed |
| [27 — Undervoltage](https://www.amazon.com/s?i=industrial&k=27+%E2%80%94+Undervoltage&tag=errorcodefixes-20) | Voltage below setpoint | Supply sag or fault |
| [59 — Overvoltage](https://www.amazon.com/s?i=industrial&k=59+%E2%80%94+Overvoltage&tag=errorcodefixes-20) | Voltage above setpoint | Switching transient |
| [87 — Differential](https://www.amazon.com/s?i=industrial&k=87+%E2%80%94+Differential&tag=errorcodefixes-20) | Current imbalance across zone | Internal fault (transformer, motor) |
| [79 — Reclosing](https://www.amazon.com/s?i=industrial&k=79+%E2%80%94+Reclosing&tag=errorcodefixes-20) | Auto-reclose sequence | Temporary fault on line |
| [46 — Neg Sequence OC](https://www.amazon.com/s?i=industrial&k=46+%E2%80%94+Neg+Sequence+OC&tag=errorcodefixes-20) | Phase unbalance | Open phase, blown fuse |

## Reading SEL Event Reports

SEL relays store detailed event reports with oscillography. Access via:
1. **Front panel:** TAR EVENT or TARGET button to view trip cause
2. **Serial/Telnet:** `EVE` or `SUM` command for event summary
3. **ACSELERATOR QuickSet:** Download full event with waveform data

The event report shows: trip element, trip time, pre-fault and fault currents/voltages on all phases, and the SELOGIC equation that caused the trip.

## Most Common Trips

### 50 Instantaneous Overcurrent
A high-magnitude fault — check the fault current level in the event report. Magnitude and direction tell you whether the fault is in the protected zone. If the 50 element operated above the CT saturation level, verify oscillography shows clean current waveform.

### 51 Time Overcurrent
A slower overcurrent event. Look at the time-overcurrent curve in the settings to confirm the relay operated correctly. If the trip time seems inconsistent with your coordination study, verify the TCC setting (TD, TD87).

### 87 Differential Trip
A differential trip always requires investigation — it means current entering and leaving the protected zone do not balance. Before resetting, test the protected equipment (transformer or motor) to confirm the fault has cleared.

## Self-Diagnostic Alarms

SEL relays also generate self-diagnostic alarms:
- **ALARM — RAM Error** — memory fault, replace relay
- **ALARM — Clock Battery** — replace battery, event timestamps unreliable
- **ALARM — Analog Input** — CT or VT input out of expected range

## Jump to Fix

- **50/51 trip** → Download event report → Confirm fault location → Clear fault → Reset
- **87 differential trip** → Megohm test protected equipment → Confirm fault cleared
- **Self-diagnostic alarm** → Read alarm detail → Replace component or battery as indicated

## When to Call a Pro
SEL provides free technical support (24/7 by phone). For settings changes, coordination studies, or firmware updates, involve a qualified protection engineer.
