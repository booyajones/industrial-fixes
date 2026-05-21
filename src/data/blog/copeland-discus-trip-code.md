---
title: "Copeland Discus Compressor Trip Codes — CoreSense Diagnostic Reference"
description: "Copeland Discus compressors equipped with CoreSense protection trip on internally-monitored faults — high discharge temperature, motor protection trip, low..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Marcus Webb"
slug: copeland-discus-trip-code
featured: false
draft: false
tags:
  - copeland
  - commercial-refrigeration
  - refrigeration
  - compressor-protection-trip-codes
  - troubleshooting
---
## Quick answer

Copeland Discus compressors equipped with CoreSense protection trip on internally-monitored faults — high discharge temperature, motor protection trip, low oil pressure, phase fault, or short cycle. The CoreSense module flashes an LED code pattern through its window: 1 flash = high discharge temp, 2 flashes = motor protection, 3 = phase fault, 4 = short cycle, 5 = low oil pressure, 6 = welded contactor, 7 = mis-wired. Don't replace the compressor until you've read the LED count and addressed the root cause.

## What Discus CoreSense codes mean

Copeland Discus compressors are semi-hermetic reciprocating compressors used heavily in commercial walk-in cooler/freezer racks, ice machines, and process refrigeration. Discus compressors built since approximately 2013 ship with CoreSense Diagnostics or CoreSense Protection modules — small electronic modules mounted in the compressor terminal box that monitor compressor operation through embedded thermistors (discharge line), motor protectors, current transformers, and oil pressure sensors.

When the CoreSense module detects a fault condition, it does three things: (1) opens the compressor contactor coil circuit through its internal relay, killing the compressor; (2) latches the fault until manually reset (or auto-reset, depending on configuration); and (3) flashes a coded LED pattern through the module's clear window indicating the specific fault that tripped.

The CoreSense LED code library:

- **1 flash, pause, repeat** — High discharge line temperature (>275 °F typically)
- **2 flashes** — Motor protection trip (overload sensed by internal thermistors)
- **3 flashes** — Phase fault (loss of phase or phase reversal on 3-phase compressors)
- **4 flashes** — Short cycle (compressor cycling faster than minimum off-time allows)
- **5 flashes** — Low oil pressure (semi-hermetic Discus only — scrolls don't have this)
- **6 flashes** — Welded contactor (current detected with no run signal)
- **7 flashes** — Miswired (incorrect terminal connections, rare after initial commissioning)

The module continues to flash the code until the fault is cleared via the reset button (Copeland CoreSense module is typically 998-0500-XX series, the reset is a recessed push button accessed through a port on the module face).

CoreSense codes point at *symptoms*, not root causes. A 1-flash high discharge fault on a walk-in freezer rack could trace to a dirty condenser, low refrigerant charge, restricted condenser airflow, or a stuck-shut metering device. Your job is to determine *why* the fault tripped.

## Common causes by trip code

**1 flash — High discharge temperature:**
- Dirty or restricted condenser (most common)
- Low refrigerant charge
- Failed condenser fan motor
- Stuck-closed liquid line solenoid or filter-drier
- High suction superheat from a starved evaporator
- Compressor internal mechanical wear (worn rings, leaking valves)

**2 flashes — Motor protection:**
- Motor overload from sustained high pressure
- Liquid floodback from a flooded evaporator
- Loose terminal stub connections
- Failed motor windings (open phase or shorted turns)
- Low voltage supply causing high current draw

**3 flashes — Phase fault:**
- Open phase on 3-phase supply (blown line fuse, broken conductor)
- Phase reversal at the building service (after recent electrical work)
- Failed contactor on one of three poles
- Loose terminal at the compressor stub

**4 flashes — Short cycle:**
- Low charge causing rapid LP-cutout cycles
- Failed pressure switches (LP cuts in too early)
- Improper controller setpoint (too narrow deadband)
- Refrigeration system undersized for load

**5 flashes — Low oil pressure (semi-hermetic only):**
- Failed oil pump
- Worn oil pump pickup
- Refrigerant flooding diluting oil
- Stuck-shut oil pressure differential switch
- Excessive blowby past worn piston rings

**6 flashes — Welded contactor:**
- Contactor pole(s) welded closed from prior overcurrent event
- Stuck mechanical linkage
- Failed contactor coil staying engaged

**7 flashes — Miswired:**
- Phase-to-phase connections crossed at the compressor terminal box
- Control wiring on wrong terminals
- After service work where terminal connections were rearranged

## Step-by-step diagnostic approach

1. **Read the LED flash count carefully.** Stand at the CoreSense module window and watch a complete code cycle. The LED will flash the count, pause about 2-3 seconds, repeat. Note exactly how many flashes per cycle. A single misread of the count sends you down the wrong diagnostic path.

2. **Identify the compressor model and CoreSense module part.** Copeland Discus model numbers are stamped on the compressor data plate (typical format: 4DR3F32KE-TFD-800 or similar). The CoreSense module is typically a 998-0500-XX or 998-0511-XX series part. Note both before ordering parts.

3. **For 1 flash (high discharge), check head pressure first.** Connect gauges to the rack's high-side and low-side service ports. On a typical R-404A medium-temp rack at 95 °F ambient, expect discharge pressure 270-320 PSI and suction 30-45 PSI. Discharge climbing toward 400+ PSI = condenser/airflow issue. Clean the condenser, verify fan operation, check head-pressure control on remote systems.

4. **For 2 flashes (motor protection), measure motor current.** Use a clamp meter on each compressor lead during a run cycle. On a typical 5 HP semi-hermetic R-404A medium-temp Discus, expect run current 12-18 A per phase, all phases within 10% of each other. Imbalanced current or sustained high current points to motor, supply voltage, or refrigerant-side issue. Megger windings to ground (after disconnecting from CoreSense and any electronics) to check insulation — should be >100 MΩ.

5. **For 3 flashes (phase fault), verify supply voltage and phase rotation.** Check L1-L2, L2-L3, and L1-L3 phase-to-phase voltages — all three should be within 2% on a healthy 3-phase service. Use a phase rotation meter to verify ABC sequence (Discus compressors require correct rotation; reverse rotation runs the compressor backwards and triggers protection). Check the contactor with a meter — all three poles should make/break together.

6. **For 4 flashes (short cycle), examine cycle history.** CoreSense logs run time and cycle counts. With a Copeland service interface tool (or by counting cycles manually over a 30-minute observation period), determine actual cycling rate. Walk-in coolers should cycle no more than 3-4 times per hour at steady-state. Cycling 8-12 times per hour points to controller setpoint, pressure switch failure, or load mismatch.

7. **For 5 flashes (low oil), check oil level and pressure differential.** Semi-hermetic Discus compressors have an oil sight glass — should be 1/4 to 1/2 full at steady-state run. Below 1/4 = low oil charge (add Mobil EAL Arctic 22CC or specified POE oil to bring up). Cloudy or foamy oil = refrigerant flooding, diagnose evaporator side. Measure oil pressure differential at the oil pressure switch — should be 9-15 PSI above suction pressure on a healthy compressor.

8. **For 6 flashes (welded contactor), replace the contactor.** Don't try to clean welded contact tips — they'll re-weld immediately. Replace the entire contactor with a like-rated part. Investigate why the contactor welded — usually a prior overcurrent event from a frozen or hot-locked-rotor condition that the original contactor wasn't sized to interrupt.

> **Field knowledge nugget:** On Copeland Discus compressors installed on parallel rack systems for medium-temp walk-in coolers (typical setup: three 4DR3 or 6DR3 series compressors on a common suction header), I see a consistent CoreSense 5-flash (low oil) pattern that traces to oil-distribution issues across the rack rather than oil-loss in any single compressor. The trap: parallel racks rely on oil equalization through a shared oil-line system, and over 4-6 years of operation, the oil filter and oil-line strainers gradually clog with carbon and wax. The result is one compressor "hoards" oil while another runs short. The 5-flash compressor isn't actually losing oil — it's the one not getting its share. The diagnostic tell: pull the oil level sight glasses on all rack compressors during run. If one is overfull and another is bone-dry while CoreSense throws 5-flash on the dry one, you've got an oil distribution problem, not a single-compressor failure. Fix is replacing the oil filter (typical Copeland 998-0500-XX format part number for the rack oil filter assembly), cleaning the oil-line strainers, and verifying the oil regulator floats are not stuck. Bring a 1-quart bottle of the correct POE oil (Mobil EAL Arctic 22CC for R-404A, R-407A; different oil for CO2 transcritical) on these calls; you'll need to top off the dry compressor after distribution is restored.

**Safety:** Walk-in coolers and freezers present door-entrapment risk — always wedge the door open during service. Compressor terminal-box work involves 3-phase line voltage (208/240/480 VAC depending on installation); lockout-tagout per OSHA 29 CFR 1910.147. CoreSense modules contain capacitors that can hold charge after power-off — wait at least 60 seconds after disconnect before terminal-box work. R-404A is the most common Discus refrigerant on legacy installations; newer installations use R-448A (Solstice N40), R-449A (Opteon XP40), or R-454A as A1-rated R-404A replacements. CO2 (R-744) Discus systems run at very high pressures (up to 1500 PSI on the high side, transcritical) and require specific high-pressure recovery equipment and training. EPA 608 Type II certification is required for sealed-system work.

## Parts that may need replacement

| Part | OEM Number (typical) | Typical Cost | Where to Buy |
|---|---|---|---|
| CoreSense Diagnostics module | 998-0500-XX | $245–$385 | [Parts Town](https://www.partstown.com?aff=PLACEHOLDER-PT) |
| CoreSense Protection module | 998-0511-XX | $185–$285 | [Parts Town](https://www.partstown.com?aff=PLACEHOLDER-PT) |
| Discharge line thermistor | 998-0500 family | $65–$115 | [Parts Town](https://www.partstown.com?aff=PLACEHOLDER-PT) |
| Oil pressure differential switch | 998-0500-XX | $145–$245 | [Parts Town](https://www.partstown.com?aff=PLACEHOLDER-PT) |
| 3-phase contactor (rack duty) | varies by amp rating | $145–$385 | [Parts Town](https://www.partstown.com?aff=PLACEHOLDER-PT) |
| POE refrigeration oil (1 qt) | Mobil EAL Arctic 22CC | $35–$65 | [Parts Town](https://www.partstown.com?aff=PLACEHOLDER-PT) / [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| Rack oil filter cartridge | 998-0500 family | $85–$165 | [Parts Town](https://www.partstown.com?aff=PLACEHOLDER-PT) |

For any compressor work, replace the suction filter-drier and the oil filter — both are normal service items at compressor change-out.

## When to call a professional

Call a CFESA-certified commercial refrigeration tech (preferably with parallel rack experience) if:

- The compressor is on a multi-compressor parallel rack — rack troubleshooting requires understanding of oil management, suction-pressure regulation, and head-pressure control across the rack.
- The system uses CO2 (R-744) refrigerant — transcritical CO2 systems require specialized training and equipment.
- The compressor itself shows mechanical failure indicators (excessive vibration, knocking, unusual noises). Compressor replacement on a rack is involved sealed-system work.
- The system is under Copeland warranty (typically 1 year on the module, 5 year on the compressor) — authorized servicer required.
- Phase rotation issues persist after verifying compressor terminal wiring — likely a building electrical issue requiring coordination with the electrician.

## FAQs

**How do I reset a Copeland CoreSense fault?**
Press and hold the recessed reset button on the CoreSense module face for 3 seconds with the fault indicated. If the underlying cause is fixed, the fault clears. If not, the fault re-trips within seconds to minutes.

**Will CoreSense let me run the compressor manually past a trip?**
No, and don't try to bypass it. CoreSense's protection circuit interrupts the contactor coil — bypassing it removes the compressor's protection layer entirely. A compressor running with welded valves at high discharge temperature will fail catastrophically and possibly cause a refrigerant fire on an A2L system.

**Can I replace a CoreSense module on a running compressor?**
No. Power off, lockout-tagout, and verify zero voltage in the terminal box before module replacement. The module's internal capacitors hold charge after power-off — wait 60 seconds before opening.

**Why does my CoreSense show 4 flashes (short cycle) but my pressure controller seems set correctly?**
Often the pressure controller cycle is correct but a leaking liquid line solenoid or a partially-stuck thermostatic expansion valve causes rapid pressure fluctuations that mimic short cycling. Check the liquid line solenoid for proper opening/closing and verify TXV bulb mounting and contact with the suction line.

**Does CoreSense work on older Copeland compressors without it?**
No. CoreSense is a specific module added to Copeland compressors since approximately 2013. Older Discus compressors used external Klixon-style overloads and didn't have the diagnostic LED. Adding CoreSense to an older compressor requires a retrofit kit and may not be supported for all older models.

## Related guides

- [Heatcraft Beacon II E1 Error Code — Sensor Fault Fix](/posts/heatcraft-beacon-ii-error-code)
- [Kelvinator Walk-In Controller Fault Codes](/posts/kelvinator-walkin-error-code)
- [Manitowoc HPCO Error Code — High Pressure Cut Out Fix](/posts/manitowoc-hpco-error-code)
