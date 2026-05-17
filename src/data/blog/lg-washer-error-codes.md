---
title: "LG Washer Error Codes — Complete Fix Guide"
description: "LG washer error codes for top-load and front-load models including Signature, WT, WM, WashTower, and TurboWash series. Covers LE, OE, UE, IE, dE, PE, FE, tE, and door/drain/balance codes."
pubDatetime: 2026-05-17T19:40:00Z
modDatetime: 2026-05-17T19:40:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - lg
  - washer
  - laundry
  - appliances
---
<!-- VOICE-GUARD-OFF -->

## LG Washer Error Code Reference

LG washers across the WT (top-load), WM (front-load), WashTower, and Signature lines share the same fault-code dictionary at the controller level. The codes below cover ~95% of what shows up on the panel display in residential service.

| Code | Fault | Most Likely Cause | First Action |
|------|-------|-------------------|--------------|
| LE | Motor lock / drive motor fault | Stator wiring loose, foreign object jamming drum | Pull power 5 min, check for items in tub |
| OE | Drain error | Drain pump clogged or restricted hose | Clean drain pump filter |
| UE / uE | Unbalanced load | Wet items bunched on one side | Redistribute load |
| IE | Inlet / fill error | Water supply off, inlet hose kinked, fill valve stuck | Verify both supply valves open |
| dE | Door not locked | Door not fully closed, lock assembly failed | Re-seat door, test lock |
| dE1 | Door switch fault | Switch or wiring open | Test door lock continuity |
| PE | Pressure sensor fault | Sensor hose disconnected or clogged | Inspect pressure tube to tub |
| FE | Overflow / overfill | Inlet valve stuck open, pressure sensor wrong | Shut supply, test inlet valve |
| tE | Heater / temperature sensor fault | Thermistor open or shorted, heater failed | Test thermistor and heater leads |
| CE | Current overload | Motor pulling excessive current | Check motor windings and bearings |
| SE | Hall sensor fault (front-load) | Motor rotor position sensor failed | Replace rotor position sensor |
| AE | Leak detected at base pan | Tub seal or pump hose leak | Pull cabinet, locate leak |
| 31 | High-level water sensor / suspension fault (Signature/WashTower) | Failed suspension rod or pressure sensor calibration | Inspect suspension rods, recalibrate |
| 1E | Inlet water-level sensor (some 2020+ models) | Pressure sensor or hose | Same as PE |

## The 4 Most Common LG Washer Faults

### UE / uE — Unbalanced Load (50% of all LG washer calls)

LG's UE algorithm is aggressive. The washer measures the drum-balance signature during spin and aborts if it detects too much imbalance. The fix is usually procedural, not a parts swap:

1. Stop the cycle and open the door (front-load) or lid (top-load).
2. Untangle wet items. Bath mats, comforters, and rugs are repeat offenders.
3. Restart on a different cycle (Bulky or Bedding cycles are tolerant of imbalance).

If UE fires on every load regardless of contents, the **suspension rods** (front-load) or **shock absorbers** (top-load) have failed. A washer that bounces noisily during the wash cycle is the telltale.

### OE — Drain Error

The pump can't move water out of the tub within the expected window. Workflow:

1. **Clean the drain pump filter.** Front-load LG washers have an access panel on the lower front kickplate — open it, find the round filter, place a shallow pan, unscrew. Lint, coins, and small items collect here. Clean it monthly.
2. **Check the drain hose for kinks.** The hose should rise to ~32-39 in then drop to the standpipe. A flat or kinked hose causes OE intermittently.
3. **Test the drain pump.** With the cabinet open, jumper the pump leads to test for direct operation. A failed pump is the most common parts replacement for chronic OE.

### IE — Inlet / Fill Error

The washer didn't reach the target water level in the fill window. Three checks:

1. Both supply valves open and supply pressure 20+ PSI.
2. Inlet hoses not kinked; inlet screens at the valve not clogged with sediment.
3. **Inlet solenoid valve** working — test by jumpering the leads with the supply on; valve should click and water flow.

### LE — Motor Lock

The drive motor is drawing current but the rotor isn't moving. Causes:

1. **Foreign object jamming the drum** — coins, hairpins, underwire bras in the gap between the inner and outer tub. Pull the rear access panel to look behind the drum.
2. **Bearings seized** — drum bearings have failed and the motor can't break the static friction. A rumbling spin cycle in the months prior is the warning.
3. **Stator wiring loose** — direct-drive LG motors have a stator behind the rotor; the 3-phase leads occasionally chafe or come loose at the connector.

## Parts That May Need Replacement {#parts}

| Part | Where to Buy | Typical Cost |
|------|--------------|--------------|
| Drain pump (LG AHA72914203 / WPW10581874-style) | [Check price on Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-washer-error-codes&k="AHA72914203"+LG+drain+pump&tag=errorcodefixes-20) \| RepairClinic | $40-$95 |
| Inlet solenoid valve (cold or hot) | [Check price on Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-washer-error-codes&k="LG+washer+inlet+valve"&tag=errorcodefixes-20) | $45-$80 |
| Door lock / interlock switch | [Check price on Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-washer-error-codes&k="LG+washer+door+lock"&tag=errorcodefixes-20) | $35-$75 |
| Suspension rod set (front-load, 4-pack) | [Check price on Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-washer-error-codes&k="LG+washer+suspension+rod"&tag=errorcodefixes-20) | $50-$120 |
| Drum bearings + seal kit | [Check price on Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-washer-error-codes&k="LG+washer+bearing+kit"&tag=errorcodefixes-20) | $30-$80 |
| Pressure sensor (water level) | [Check price on Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-washer-error-codes&k="LG+washer+pressure+sensor"&tag=errorcodefixes-20) | $25-$55 |
| Main control board (LG EBR-series, model-specific) | RepairClinic, LG parts | $180-$400 |
| Heater + thermistor assembly | [Check price on Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-washer-error-codes&k="LG+washer+heater"&tag=errorcodefixes-20) | $60-$140 |

## Technician Tips

- LG washers manufactured after 2018 store the **last 5 fault codes** with timestamps. Enter diagnostic mode: hold the Spin Speed and Soil Level buttons together for 3 seconds, then press Start. The display will scroll through stored codes.
- **Don't replace the control board first.** It's the most expensive part and the rarest failure. Verify the cheap stuff (filter, pump, valve, lock) eliminated before the board is suspect.
- LG's 10-year direct-drive motor warranty covers the motor *and* stator. If the customer is within 10 years of installation and the LE fault traces to the motor, the part is free — they just pay labor.
- For chronic UE on a relatively new front-load, level the unit. LG washers are sensitive to a level base — even a 1/4-inch tilt across the front feet causes nuisance UE.

## Common Code Combinations

- **OE → IE** in same load: the washer can't drain, then tries to refill and fails because the pressure sensor still reads water in the tub. Always clear OE first.
- **PE → IE → FE**: pressure sensor hose disconnected. The washer reads zero water, opens the inlet, then the sensor jumps to overflow when the tube reconnects under pressure. Replace the pressure tube clip.

If you've worked through the diagnostic above and the fault returns within 24 hours, the issue is upstream — usually a failed pressure sensor or a wiring harness break — and the next step is a real service call rather than another swap.
