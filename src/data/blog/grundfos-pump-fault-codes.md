---
title: "Grundfos Circulator Pump Fault Codes — Complete Guide"
description: "Grundfos pump fault codes for MAGNA, UPS, Alpha, and CM series: all LED and display fault codes, causes, and step-by-step fixes for Grundfos circulators."
pubDatetime: 2026-04-22T19:00:00Z
modDatetime: 2026-04-22T19:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - plumbing
  - grundfos
  - pump
---

## Grundfos Pump Fault Codes — Quick Reference

Grundfos circulators and variable-speed pumps display fault codes through LED indicators or digital displays depending on the model. MAGNA, Alpha, and CM series pumps use LED color and flash patterns; MAGNA3 and larger pumps display numeric codes. The Grundfos GO app (Bluetooth) can also read faults on compatible models.

| Code / LED | Model | Meaning | Quick Fix |
|-----------|-------|---------|-----------|
| [Red LED solid](https://www.amazon.com/s?ascsubtag=ecf-grundfos-pump-fault-codes&k=Red+LED+solid&tag=errorcodefixes-20) | Alpha, UPS | Pump fault — overload or locked rotor | Check for air lock; verify voltage |
| [Red flashing](https://www.amazon.com/s?ascsubtag=ecf-grundfos-pump-fault-codes&k=Red+flashing&tag=errorcodefixes-20) | MAGNA | Protection mode active | Check system pressure; check liquid temp |
| F1 | MAGNA, CM | Dry running / no liquid detected | Prime pump; check suction valve |
| F2 | MAGNA3 | Overcurrent / overload | Check system resistance; verify impeller |
| F3 | MAGNA3 | Overvoltage | Check supply voltage |
| F4 | MAGNA3 | Undervoltage | Check supply voltage; check wiring |
| F5 | MAGNA3 | Overtemperature — motor | Check liquid temperature; reduce load |
| F6 | MAGNA3 | Locked rotor | Check for debris; manually free impeller |
| F7 | MAGNA3 | Internal fault | Replace pump head |
| ALT | MAGNA | Alternating mode active | Normal in dual-pump installations |
| [Constant red](https://www.amazon.com/s?ascsubtag=ecf-grundfos-pump-fault-codes&k=Constant+red&tag=errorcodefixes-20) | Alpha | Blocked impeller or air-locked | Bleed air; inspect impeller |

## Most Common Faults

### Red LED / F6 — Locked Rotor / Blocked Impeller
A locked rotor is the most common fault on Grundfos wet-rotor circulators, especially after a long shutdown period. Calcium deposits or debris can jam the impeller against the pump body. On most Grundfos pumps, there is a bleed screw on the pump head — remove it with a flathead screwdriver and insert a coin or screwdriver to manually rotate the pump shaft. If the shaft moves freely after manual rotation, re-close the bleed screw, power cycle the pump, and it should run.

**Caution:** Hot water systems can release steam from the bleed screw. Allow to cool first.

### F1 — Dry Running
The pump is operating without sufficient liquid in the system. Grundfos pumps with dry-run protection will fault and shut down to protect the ceramic shaft bushing from damage. Check that all isolation valves on the pump suction side are open. On new installations, the system may need to be bled of air — open all air vents at the high points of the system and refill.

### F5 — Motor Overtemperature
The pump motor temperature exceeded its limit. On hot water systems, verify the system water temperature is within the pump's rated range (MAGNA series is typically rated to 230°F / 110°C). If the system temperature is normal, check for restricted flow — a partially closed valve upstream or downstream of the pump can cause the motor to work harder and generate more heat.

### Red Flashing / F3/F4 — Voltage Issues
Check the supply voltage at the pump terminals. Grundfos MAGNA and Alpha pumps are typically rated 1-phase 115VAC or 230VAC (check pump label). Voltage outside ±10% of the rated value will cause voltage faults. On 230VAC systems, verify both legs are present and balanced.

### F2 — Overcurrent / Overload
The pump is drawing more current than rated. This can be caused by:
- Partially closed valve creating excessive back-pressure
- Impeller damage causing imbalance
- Incorrect pump selected for the system (too large)
- Liquid viscosity higher than expected (glycol concentration too high)

## Grundfos Alpha Series Fault LED Meanings

| [LED Pattern](https://www.amazon.com/s?ascsubtag=ecf-grundfos-pump-fault-codes&k=LED+Pattern&tag=errorcodefixes-20) | Meaning |
|------------|---------|
| [Solid green](https://www.amazon.com/s?ascsubtag=ecf-grundfos-pump-fault-codes&k=Solid+green&tag=errorcodefixes-20) | Normal operation |
| [Flashing green](https://www.amazon.com/s?ascsubtag=ecf-grundfos-pump-fault-codes&k=Flashing+green&tag=errorcodefixes-20) | Auto-adapt mode — learning curve |
| [Solid red](https://www.amazon.com/s?ascsubtag=ecf-grundfos-pump-fault-codes&k=Solid+red&tag=errorcodefixes-20) | Fault — check for blockage |
| [Alternating green/red](https://www.amazon.com/s?ascsubtag=ecf-grundfos-pump-fault-codes&k=Alternating+green%2Fred&tag=errorcodefixes-20) | Protection mode |

## Pump Venting Procedure (Air-Lock Removal)

1. Locate the bleed screw on the front of the pump motor head
2. Place a towel under the pump to catch water
3. Slowly open the bleed screw ¼–½ turn counterclockwise
4. Air will hiss out, followed by water — close when steady water appears
5. Power cycle the pump

## When to Call a Pro
Persistent F7 (internal fault) requires pump head replacement. Grundfos offers replacement pump heads (motor + electronics) that bolt onto the existing valve body — this is the recommended repair vs. replacing the entire pump assembly.
