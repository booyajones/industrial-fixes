---
title: "Rheem RA13 Air Conditioner Error Codes — Fault Code Diagnostic Guide"
description: "Complete guide to Rheem RA13 central air conditioner error codes, LED flash sequences, fault causes, and step-by-step repair procedures for technicians."
pubDatetime: 2026-04-22T23:00:00Z
modDatetime: 2026-04-22T23:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - rheem
  - air-conditioner
---

## Rheem RA13 Air Conditioner Error Codes — What They Mean

The Rheem RA13 (and its Ruud counterpart, the RA13) is a 13–14 SEER single-stage central air conditioner using R-410A refrigerant. It is designed for replacement and new construction applications where budget is the primary constraint. The RA13 uses a conventional control board with a status LED to communicate faults via flash codes. These units do not have a communicating bus — they operate in a standard thermostat-controlled on/off mode.

[Jump to Fix](#fix)

## Rheem RA13 LED Flash Code Reference

| [Flash Sequence](https://www.amazon.com/s?k=Flash%20Sequence&tag=errorcodefixe-20) | Fault |
|---|---|
| [1 flash](https://www.amazon.com/s?k=1%20flash&tag=errorcodefixe-20) | Normal — standby |
| [2 flashes](https://www.amazon.com/s?k=2%20flashes&tag=errorcodefixe-20) | High-pressure switch open |
| [3 flashes](https://www.amazon.com/s?k=3%20flashes&tag=errorcodefixe-20) | Low-pressure switch open |
| [4 flashes](https://www.amazon.com/s?k=4%20flashes&tag=errorcodefixe-20) | Compressor protection device open |
| [5 flashes](https://www.amazon.com/s?k=5%20flashes&tag=errorcodefixe-20) | Control board fault |
| [6 flashes](https://www.amazon.com/s?k=6%20flashes&tag=errorcodefixe-20) | Thermistor fault — outdoor sensor |
| [7 flashes](https://www.amazon.com/s?k=7%20flashes&tag=errorcodefixe-20) | Anti-short cycle lockout (5-minute delay) |
| [Rapid continuous](https://www.amazon.com/s?k=Rapid%20continuous&tag=errorcodefixe-20) | Low voltage — below 18VAC |

## Common Causes by Code

- **2 flashes — High pressure** — Dirty condenser coil, failed condenser fan capacitor, or refrigerant overcharge. The RA13 condenser coil is a spine-fin design that is more prone to debris accumulation on the bottom edges than a flat-fin coil.
- **3 flashes — Low pressure** — Refrigerant undercharge (leak), extremely cold ambient temperatures, or a failed low-pressure switch. The RA13's low-pressure cutout is set at 50 PSIG on R-410A systems.
- **4 flashes — Compressor protection** — The RA13 scroll compressor has an internal thermal overload. Also check the external crankcase heater (if installed) — a failed crankcase heater can cause liquid-slugging on startup in cold climates.
- **5 flashes — Board fault** — Typically caused by power surges or lightning. Check all board fuses, the 24V transformer, and inspect the board for burnt or corroded areas.
- **7 flashes — Anti-short cycle** — Normal protection function. The board prevents compressor restart for 5 minutes after shutdown. This is not a fault — it clears automatically.

## Step-by-Step Fix {#fix}

1. **Locate the status LED** — Remove the electrical access panel on the RA13 outdoor unit. The control board is mounted on the inside of the panel or on a bracket near the compressor compartment. The LED will be flashing the fault code.
2. **For 2 flashes (high pressure)** — Turn off the unit at the thermostat. Inspect the condenser coil from the outside — look for dirt buildup at the base (ground level) where debris collects. Also check the fan motor: grab the blade (with power off) and check for rough bearing feel. Test the run capacitor with a capacitor meter.
3. **For 3 flashes (low pressure)** — Connect R-410A manifold gauges to the service ports. Record static pressure (unit off) and operating pressures (unit running). If suction is below 70 PSIG with the unit running at 70°F ambient, charge is significantly low — find the leak.
4. **For 4 flashes (compressor protection)** — Power cycle after a 30-minute wait. Measure supply voltage at the disconnect — both legs at the same time to confirm voltage is balanced. Unbalanced voltage (more than 2% difference between legs) causes compressor overheating.
5. **Rapid flash (low voltage)** — Measure R-to-C voltage at the control board terminals. If below 18VAC, check the 40VA or 75VA transformer. Also verify no shorted control devices are dragging down the 24V circuit (disconnect the G, Y, W terminals one at a time to isolate).

## Parts Often Needed

| Part | Notes |
|---|---|
| [Dual run capacitor](https://www.amazon.com/s?k=Dual%20run%20capacitor&tag=errorcodefixe-20) | Most common RA13 failure; affects both fan and compressor |
| [Contactor](https://www.amazon.com/s?k=Contactor&tag=errorcodefixe-20) | 2-pole; inspect for pitting and carbon buildup |
| [High-pressure switch](https://www.amazon.com/s?k=High-pressure%20switch&tag=errorcodefixe-20) | Spade terminals; replaces easily |
| [Low-pressure switch](https://www.amazon.com/s?k=Low-pressure%20switch&tag=errorcodefixe-20) | 50 PSIG cutout for R-410A |
| [Control board](https://www.amazon.com/s?k=Control%20board&tag=errorcodefixe-20) | Check fuse first before ordering board |
| [Condenser fan motor](https://www.amazon.com/s?k=Condenser%20fan%20motor&tag=errorcodefixe-20) | Match RPM, HP, and shaft size |

## When to Call a Pro

Refrigerant handling on the RA13 requires EPA 608 certification. If the compressor draws high amperage (above nameplate FLA) but produces no cooling, the compressor may be mechanically failed — a technician with a clamp-on ammeter and manifold gauges can confirm this before an expensive replacement decision is made.
