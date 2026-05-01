---
title: "Carrier Infinity Error Code 179 — What It Means and How to Fix It"
description: "Carrier Infinity error 179 means the system lost communication with a component. Learn what causes it, how to trace the fault, and which parts fix it."
pubDatetime: 2026-04-25T12:00:00Z
modDatetime: 2026-04-25T12:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - carrier
  - error-codes
---

Carrier Infinity error code 179 is a communication fault. It means the Infinity thermostat has lost contact with one or more system components — most often the furnace control board, air handler, or outdoor unit. The Infinity system uses a two-wire communication bus called the **Infinity System Bus**, and error 179 fires when that bus goes silent.

[Jump to Fix](#how-to-fix-carrier-infinity-error-179)

## What Does Carrier Infinity Error 179 Mean?

The Carrier Infinity touch thermostat displays error 179 when it cannot establish or maintain communication with a connected system component. You may also see related messages like:

- **"Error 179 — Equipment Communication Fault"**
- **"Check System"** with a 179 code in the diagnostics menu
- Component-specific variants: **"Error 179-00"** (furnace), **"Error 179-01"** (outdoor unit), **"Error 179-02"** (accessory)

The Infinity system communicates over a **24V, 2-wire data bus** using terminals labeled **ABCD** or **+/−** depending on the generation of equipment. All components on the system share this bus — if one component has a wiring fault or hardware failure, it can corrupt communication for all other components.

### Common Causes of Error 179

1. **Loose or corroded wire at any terminal** — the most common cause
2. **Damaged thermostat wire** — pinched by sheet metal, nicked during installation, or weathered
3. **Failed furnace or air handler control board** — the board's communication chip has failed
4. **Failed outdoor unit control board** — common on variable-speed and Greenspeed units
5. **Thermostat hardware failure** — the Infinity touch thermostat itself can fail
6. **Multiple components on the bus conflicting** — addressing issues on multi-zone systems

---

## How to Fix Carrier Infinity Error 179

### Step 1: Power Cycle the System

1. Set the Infinity thermostat to **OFF**.
2. Turn off the furnace/air handler breaker at the electrical panel.
3. Turn off the outdoor unit breaker.
4. Wait **3 full minutes**.
5. Restore indoor unit power, wait 60 seconds, then restore outdoor unit power.
6. Resume normal thermostat operation.

A controlled restart resolves temporary communication lockups. If error 179 clears and doesn't return, monitor for recurrence.

### Step 2: Access the Thermostat Diagnostics

The Infinity thermostat has a built-in diagnostics screen that tells you exactly which component is failing:

1. From the home screen, go to **Menu > Diagnostics**.
2. Look for **"Equipment Status"** or **"Communication Status"**.
3. The display will show each connected component (furnace, outdoor, humidifier, ventilator, etc.) and whether it's communicating.
4. Note which components show as offline — that's where you focus.

### Step 3: Inspect Wiring at the Thermostat

1. Remove the Infinity thermostat from the wall plate.
2. Inspect the wiring terminals. The communication wires typically use the **A** and **B** terminals (or **+** and **−**).
3. Each wire should be fully seated with clean copper making contact. No corrosion, no bare wire touching adjacent terminals.
4. Disconnect and firmly reseat every wire.
5. Check the wire color consistency — if the system was ever serviced, wires may have been connected to wrong terminals.

**Standard Infinity wiring at the thermostat:**
- R — 24V power
- C — Common
- A — Communication A (positive)
- B — Communication B (negative)

### Step 4: Check Control Board Terminals at the Indoor Unit

1. Turn off the furnace/air handler at the breaker.
2. Open the blower compartment or control box.
3. Locate the control board and find the communication bus terminals.
4. Inspect for loose wires, terminals with corrosion, or discolored wires indicating heat damage.
5. Look for a blown fuse on the control board — a 3A or 5A automotive-style fuse on the board. Replace with the same rating if blown.
6. Restore power and check whether error 179 clears.

### Step 5: Inspect Wiring at the Outdoor Unit

1. Turn off the outdoor unit breaker.
2. Open the electrical access panel on the outdoor unit.
3. Locate where the control wire (typically 18-gauge, 4 or 5 wire) connects.
4. Inspect the terminals — outdoor units are exposed to weather and terminal corrosion is common.
5. Check for wire damage where the conduit enters the unit (conduit ends can cut through wire insulation over time).
6. Restore power and test.

### Step 6: Test the Communication Bus

With the system powered and error 179 active:

1. Set a multimeter to **DC millivolts**.
2. At the furnace control board, measure voltage between the **A** and **B** communication terminals.
3. You should see a pulsing voltage — typically **0–30V DC** pulsing at the bus communication frequency. Steady 0V = no signal. Steady high voltage = no devices responding.
4. If the bus is dead, identify which component powers the bus (typically the furnace control board) and test that board's output.

### Step 7: Replace the Failing Control Board

If wiring is intact and the diagnostic screen identifies one specific component as offline:

1. Order the replacement board for that component.
2. For the furnace: the CEPL130432-01 or model-specific board
3. For the outdoor unit: the variable-speed inverter board (model-specific — typically $300–$600)
4. Photograph all wiring before disconnecting.
5. Carrier Infinity boards sometimes require configuration after replacement — some technicians use the Bryant/Carrier service tool (SYSTXBBECC01-B) to reconfigure.

---

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|--------------|
| [Carrier Infinity Thermostat (SYSTXBBUID01-B or SYSTXBBECC01-B)](https://www.amazon.com/s?k=Carrier+Infinity+Thermostat+%28SYSTXBBUID01-B+or+SYSTXBBECC01-B%29&tag=errorcodefixes-20) | Thermostat communication hardware failed | $150–$350 |
| [Furnace Control Board (CEPL130432-01 or model-specific)](https://www.amazon.com/dp/B0CNZGZ1HS?tag=errorcodefixes-20) | Indoor board communication chip failure | $200–$450 |
| [Outdoor Unit Control Board (model-specific)](https://www.amazon.com/dp/B0CNZGZ1HS?tag=errorcodefixes-20) | Variable-speed or inverter board failure | $300–$700 |
| [Control Board Fuse (3A or 5A, ATC-type)](https://www.amazon.com/dp/B0CNZGZ1HS?tag=errorcodefixes-20) | Blown board fuse cutting communication power | $2–$5 |
| [18/5 or 18/8 Thermostat Wire](https://www.amazon.com/s?k=18%2F5+or+18%2F8+Thermostat+Wire&tag=errorcodefixes-20) | Damaged low-voltage wiring | $25–$60 per 50ft |

---

## When to Call a Pro

- Error 179 affects multiple components simultaneously — suggests a bus power or wiring short requiring systematic diagnosis
- Your system is a variable-speed Greenspeed or Infinity 21 unit — these have complex inverter boards that require careful installation and sometimes factory configuration
- Error 179 accompanies refrigerant fault codes — combined faults suggest a more serious system issue
- You can't identify which component is offline via diagnostics and wiring all checks out — Carrier dealers have service tools that can query each component directly
- The system is under warranty — board replacements are covered; DIY work may void it

---

## Frequently Asked Questions

**Is Carrier Infinity error 179 the same as Bryant Evolution communication fault?**
Essentially yes. Carrier and Bryant use the same system architecture. A Carrier Infinity error 179 is functionally identical to a Bryant Evolution communication fault. The diagnostic and repair process is the same, and parts frequently cross-reference.

**Can a bad C-wire cause Carrier Infinity error 179?**
Indirectly. The C wire provides the 24V common reference for the communication bus. If the C wire has high resistance or is disconnected, the bus voltage can become unstable and cause communication errors. Always verify the C wire is solid if you're chasing intermittent 179 errors.

**My Carrier Infinity error 179 only appears in cooling mode — why?**
Mode-specific communication faults usually point to the outdoor unit. When heating-only, the furnace may operate independently without full bus communication. In cooling mode, the outdoor unit must be on the bus. Check the outdoor unit wiring and control board.

**How do I clear error 179 on a Carrier Infinity thermostat?**
The error clears automatically when communication is restored — there's no manual reset for 179. Power cycling the system (breakers off, wait 3 min, restore) is the quickest way to attempt a reset. If the underlying fault is still present, the code will reappear.

**Does error 179 mean my Carrier Infinity system is broken?**
Not necessarily. The most common cause is a loose wire that reseating fixes in 10 minutes. Start with the simplest check (power cycle, inspect terminal connections) before assuming you need a $400 board.

## Related Articles

- [Carrier 11 Error Code — Causes & Fix](/posts/carrier-11-error-code/)
- [Carrier 12 Error Code — Causes & Fix](/posts/carrier-12-error-code/)
- [Carrier 13 Error Code — Limit Switch Lockout Fix](/posts/carrier-13-error-code/)
- [Carrier 13 Soft Lockout — What's Different from Hard Lockout](/posts/carrier-13-soft-lockout/)
- [Carrier 14 Error Code — Causes & Fix](/posts/carrier-14-error-code/)
