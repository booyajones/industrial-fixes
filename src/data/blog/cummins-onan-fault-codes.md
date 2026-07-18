---
title: "Cummins Onan Generator Fault Codes: List & Fixes"
description: "Every Cummins Onan generator fault code explained, from RV blink codes to commercial shutdowns, with the likely cause and a step-by-step fix for each."
pubDatetime: 2026-04-22T19:00:00Z
modDatetime: 2026-04-22T19:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - generator
  - cummins
  - onan
  - electrical
---

## Cummins Onan Generator Fault Codes — Quick Reference

Cummins Onan generators cover the range from compact RV gensets (QG 2500, QD 3200) to commercial diesel generators (MDKD, DSGAA series). Fault codes are displayed on the generator control panel or via the Onan app. RV-series generators use a simplified blink code system.

| Code | Series | Meaning | Quick Fix |
|------|--------|---------|-----------|
| 2 blinks | RV QG/QD | Low oil pressure | Add oil; check oil sender |
| 3 blinks | RV QG/QD | High coolant temperature | Check coolant; check fan |
| 4 blinks | RV QG/QD | Overcrank (fail to start) | Check fuel, spark, choke |
| 5 blinks | RV QG/QD | Field (voltage) fault | AVR or control board issue |
| 6 blinks | RV QG/QD | Governor fault | Governor calibration needed |
| 7 blinks | RV QG/QD | Controller fault | Replace control board |
| 8 blinks | RV QG/QD | Low voltage / high voltage | Load issue or AVR fault |
| Code 13 | Commercial | Low oil pressure warning | Check oil level |
| Code 14 | Commercial | Low oil pressure shutdown | Immediate shutdown — add oil |
| Code 22 | Commercial | High coolant temp warning | Check cooling system |
| Code 23 | Commercial | High coolant temp shutdown | Stop generator; check coolant |
| Code 35 | Commercial | Engine fail to start | Check fuel, battery, starter |
| Code 36 | Commercial | Engine overspeed | Governor problem |
| Code 45 | Commercial | Low fuel | Refuel |
| Code 54 | Commercial | Battery charger fault | Check charger AC supply |

## Most Common Faults

### 4 Blinks / Code 35 — Fail to Start (Overcrank)
**RV Generators (QG 2500, QD 3200):**
The most common failure on RV Onan generators. Root causes by frequency:
1. **Fuel delivery:** RV generators pull fuel from the main fuel tank via a small pickup tube. If the tank is below 1/4 full, the pickup may not reach fuel, especially on grades. Fill the tank and retry.
2. **Carburetor varnish:** RV generators often sit for months between uses. A varnished carburetor main jet is very common. Remove the bowl, clean the jet with a fine wire, and spray carburetor cleaner.
3. **Choke:** Onan RV generators have a vacuum-operated automatic choke. If the choke stays open on a cold start, the engine won't start. Check the choke vacuum hose and the choke butterfly plate.
4. **Spark plugs:** Replace spark plugs if the generator hasn't been serviced in 2+ years.

### 2 Blinks / Code 14 — Low Oil Pressure
For RV generators: use SAE 30 or 10W-30 per the Onan manual. Check the dipstick. If oil level is correct and the generator immediately shuts down on restart, the oil pressure sender may be failed. Bypass test: a technician can temporarily jumper the oil pressure switch to verify the engine actually has oil pressure.

### 5 Blinks — Field Fault (Voltage Fault)
The generator's field excitation circuit has a fault. This is usually the AVR (automatic voltage regulator) or the excitation winding in the alternator. The AVR on Onan QG/QD generators is a small board inside the control compartment. Inspect for burned components or loose connectors. If the AVR board shows burn damage, replace it.

### 3 Blinks / Code 22/23 — High Engine Temperature
On liquid-cooled commercial Onan generators, check the coolant level, radiator fins, thermostat, and water pump impeller. On the air-cooled RV QG series, check that the generator's cooling air inlet and exhaust openings are not blocked by debris or insulation material.

### Code 36 — Engine Overspeed
Onan commercial generators (MDKD, DSGAA) use a mechanical governor with electronic trim. Overspeed faults indicate the governor has lost control. Check the governor actuator wiring first — a failed or disconnected actuator is a common cause. On mechanical governors, check the flyweight assembly and governor spring.

## Onan RV Generator Maintenance

| [Service Item](https://www.amazon.com/s?ascsubtag=ecf-cummins-onan-fault-codes&k=Service+Item&tag=errorcodefixes-20) | Interval |
|-------------|----------|
| [Engine oil](https://www.amazon.com/s?ascsubtag=ecf-cummins-onan-fault-codes&k=Engine+oil&tag=errorcodefixes-20) | Every 150 hours or annually |
| [Air filter](https://www.amazon.com/dp/B0CLBFXLYJ?ascsubtag=ecf-cummins-onan-fault-codes&tag=errorcodefixes-20) | Every 150 hours |
| [Spark plugs](https://www.amazon.com/s?ascsubtag=ecf-cummins-onan-fault-codes&k=Spark+plugs&tag=errorcodefixes-20) | Every 150 hours |
| [Fuel filter](https://www.amazon.com/s?ascsubtag=ecf-cummins-onan-fault-codes&k=Fuel+filter&tag=errorcodefixes-20) | Every 150 hours |
| [Carburetor cleaning](https://www.amazon.com/s?ascsubtag=ecf-cummins-onan-fault-codes&k=Carburetor+cleaning&tag=errorcodefixes-20) | As needed (every 2–3 seasons if run infrequently) |

## When to Call a Pro
Onan commercial generator faults (Code 22+, voltage faults, governor faults) require a Cummins-authorized service center. Do not attempt to adjust AVR or governor settings without proper test equipment and Onan service training.

## How to troubleshoot Cummins Onan

## How to diagnose an Onan generator that faults out

Onan gensets store a fault code that is either shown on a digital display or flashed as a blink code on the Control Switch status light. After a fault shutdown the light repeatedly blinks 2, 3, or 4 times: two blinks is a low-oil-pressure fault, three blinks is a service fault, and four blinks means cranking exceeded 30 seconds without starting. For a three-blink service fault, press the Stop switch once to display the two-digit second-level code (tens-digit blinks, a pause, then units-digit blinks, so five flashes, pause, one flash = Code 51). Always read and write down the exact code before you start replacing parts, and note whether it keeps running (warning) or shuts the genset down.

**Check the cheap, common things first, in this order:**

1. **Fuel and battery.** The two most frequent real-world failures on Onan RV units are stale/insufficient fuel and a weak battery. RV gensets draw from the main tank through a pickup that sits above the tank bottom, so the generator can starve above roughly a quarter tank, especially on a grade. A slow crank (Code 32) is almost always a discharged battery or corroded cables, not the engine.
2. **Stale fuel and carburetor varnish.** Units that sit for months develop varnish in the carburetor jets. If the engine cranks but will not fire or dies under load, suspect the carburetor before the control board.
3. **Oil level and the oil-pressure switch.** A low-oil-pressure shutdown that appears with correct oil often points at a failed oil-pressure sender rather than an actual pressure loss; a technician can confirm.
4. **Airflow.** Air-cooled RV sets overheat when the intake or exhaust is blocked by debris or insulation; liquid-cooled commercial sets need coolant level, radiator fins, thermostat, and water-pump flow checked.

**Safety:** never run a generator in an enclosed space (carbon monoxide), and disconnect the battery negative and the shore/coach power before working on the AVR, wiring, or exhaust. Exhaust components stay hot long after shutdown.

**When to stop and call a pro:** overspeed (Code 31), voltage-sense (Code 27), field/rotor (Codes 38/41/48), configuration (Code 37), and any commercial voltage or governor fault require dealer test equipment and Onan training. Do not adjust AVR or governor settings by trial and error.


## Frequently asked questions

### What is the most common Onan RV generator problem?

Failure to start (overcrank / Code 4). On RV units that sit unused, the usual causes are stale fuel, a varnished carburetor jet, or fuel starvation when the main tank is below a quarter full. Fresh fuel, a carburetor cleaning, and a fresh set of spark plugs resolve most of these before any control-board work is needed.

### What does Onan fault code 32 mean and how do I fix it?

Code 32 is Low Cranking Speed: the engine turned slower than 180 rpm for more than 2 seconds while starting. It is almost always a weak or undercharged battery, corroded/loose battery cables, or oil that is too thick for the temperature. Clean and tighten both cable ends, recharge or replace the battery, and use oil of the correct viscosity, then clear the code.

### How do I read Onan blink codes without a display?

Watch the Control Switch status lamp after a shutdown. A three-blink service fault means you press Stop once to make it flash the two-digit code, with a pause between the tens and units digits, for example five flashes then one flash equals Code 51. Count carefully and write the number down before troubleshooting.

### My Onan starts then shuts down after a few seconds. Why?

A start-then-die is usually fuel starvation (varnished carburetor, clogged filter, low tank) or a low-oil-pressure shutdown. If oil is full and it still trips on oil pressure immediately, the oil-pressure sender is a common culprit. Read the stored code to confirm which system tripped.

### Which Onan faults are safe to fix myself and which need a dealer?

Fuel, battery, oil, spark plugs, filters, and clearing a blocked cooling inlet are DIY. Overspeed (31), voltage-sense (27), field/rotor faults (38, 41, 48), configuration (37), and any AVR or governor adjustment need an authorized Onan service center with proper test equipment.


## Related guides

- [Generac Generator Error Codes](/posts/generac-generator-error-codes/)

