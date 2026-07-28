---
title: "Scotsman 5-Flash Code — Pressure Sensor Fault Fix"
description: "Five flashes on a Scotsman Prodigy (or \"PS Fault\" / \"Pressure Sensor\" on Prodigy Plus) means the high-side pressure transducer is reading out of range —..."
pubDatetime: 2026-05-20T17:00:00Z
modDatetime: 2026-05-20T17:00:00Z
author: "Marcus Webb"
slug: scotsman-5-flash-code
featured: false
draft: false
tags:
  - scotsman
  - commercial-refrigeration
  - ice-machine
  - pressure-sensor-fault
  - troubleshooting
---
## Quick answer

Five flashes on a Scotsman Prodigy (or "PS Fault" / "Pressure Sensor" on Prodigy Plus) means the high-side pressure transducer is reading out of range — either electrically impossible or physically impossible. The controller doesn't know what the system pressure actually is, so it shuts down rather than guess. In my experience this code is roughly 50% failed transducer, 25% wiring or connector issue, 15% clogged sensor port (oil migration or debris), and 10% genuine board-side fault.

## What the 5-flash code means on a Scotsman

The 5-flash code only exists on Scotsman heads equipped with an electronic pressure transducer — primarily Prodigy Plus (C0322/C0522/C0722/C0830 from approximately 2018 onward) and Brilliance series. Legacy Prodigy heads use mechanical pressure switches and won't throw this code in the same way (they'll just refuse to start or throw a different protection code).

The transducer is a 0-5 VDC ratiometric sensor — typically mounted on the discharge line or receiver — that translates pressure into a voltage signal the control board reads. Most Scotsman transducers map roughly 0.5 VDC = 0 psig and 4.5 VDC = 500 psig (a 100 psig / volt slope). If the controller sees voltage outside roughly 0.2 to 4.8 VDC, it knows the sensor is reporting nonsense — either open, shorted, disconnected, or physically blocked from sensing the actual pressure — and throws the 5-flash.

Diagnostic entry: hold OFF+ON for 5 seconds on Prodigy; menu navigation on Prodigy Plus. On Prodigy Plus you can usually read the live transducer voltage in service mode under Sensors > High Side Pressure. That's the single most useful diagnostic on this code — voltage at the board pin tells you immediately whether the problem is upstream of the board (sensor, wiring, port) or in the board itself.

This is one of the few Scotsman codes where the failure is almost always electrical, not refrigeration. Don't put gauges on it as your first move — pull the transducer voltage first.

## Common causes (ranked by frequency)

1. **Failed pressure transducer** — internal sensing element drift or complete failure. Outputs stuck at supply voltage, ground, or a fixed mid-range value. Most common failure mode past the 4-year mark.
2. **Connector or wiring issue** — three-pin connector (typically +5V, signal, ground) corroded, water-intruded, or pin pushed back in the housing. The connector lives in a humid environment.
3. **Clogged sensor port** — refrigerant oil migrated into the sensor port and gelled, or debris from a previous brazing/installation event blocks the port. Sensor reads a frozen value instead of actual pressure.
4. **Damaged sensor cable** — chafed harness, rodent damage, or a cable pinched during a previous panel reassembly.
5. **Loose Schrader fitting under the transducer** — slow refrigerant loss past the sensor's Schrader-style mount can cause an erratic reading and intermittent 5-flash.
6. **Control board input fault** — rare but real. Board ADC channel for the transducer drifts or fails.

## Step-by-step fix

1. **Read history and enter live sensor view.** Diagnostic mode. Note 5-flash count and any concurrent codes. On Prodigy Plus, navigate to Service > Sensors > High Side Pressure (or equivalent depending on firmware). Note the live voltage reading with the unit OFF and at rest. A healthy transducer on a system equalized at, say, 90 psig (R-404A at 70°F room) should read roughly 1.4 VDC at the board. A reading of 0.0 VDC, 5.0 VDC, or fixed at exactly 0.5 or 4.5 is the sensor saturated at a rail.

2. **Verify supply voltage at the transducer connector.** Power up the unit, pull the connector at the transducer (typically a Molex Mini-Fit or weatherproof Deutsch). With the connector disconnected, measure between the +5V pin and ground pin — should read 4.95-5.05 VDC. No voltage = wiring back to the board is open, or the board has lost its sensor supply. Voltage present = wiring is good, problem is downstream (sensor itself or sensor port).

3. **Measure transducer output at the connector.** Reconnect the transducer. Back-probe the signal pin to ground. With the unit at rest you should see a voltage corresponding to standing pressure (1.0-1.5 VDC typical for R-404A at room temp). Start a freeze cycle and watch the voltage climb as discharge pressure builds. If voltage is stuck (doesn't move with pressure), the sensor is dead. If voltage is wildly out of expected range, the sensor is also dead — or, less commonly, its port is blocked.

4. **Confirm against a real gauge.** Put a manifold gauge on a Schrader on the high side. Compare the actual pressure to what the transducer voltage maps to (using the 100 psig/volt slope, subtracting the 0.5 V offset: psig = (V - 0.5) × 100). If the transducer voltage maps to 90 psig but the gauge shows 240 psig, the sensor is reading wrong and either it or its port is the problem.

5. **Inspect the sensor port for blockage.** This step requires sealed-system access. Recover, valve out, or pump down enough to safely remove the transducer. Inspect the port with a light — look for oil residue, gelled lubricant, or solder debris. **Field insight: on Prodigy Plus C0522 and C0722 units that have had a previous compressor changeout, the transducer port is the #1 catch point for braze flux particles flushed downstream. If the unit has an exchange compressor sticker on the dome, suspect the port before the sensor — I've pulled clean transducers and found a 2mm flux ball blocking the port a dozen times.**

6. **Inspect wiring along the harness.** Eyeball the entire transducer harness from connector to the board J-plug. Look for chafe marks, rodent bites (more common than you'd think in older kitchens), pinch points at panel edges, and water intrusion at the connector. Continuity-test all three pins from the transducer connector to the board J-plug pins with the harness disconnected at both ends.

7. **Replace transducer if bench evidence points there.** OEM is 12-2920-31 on most Prodigy Plus heads (verify by serial-plate; Scotsman has run two suppliers across model years and the part number can vary). Schrader-style mount means you can usually swap without recovery — depress the Schrader core slightly to relieve trapped pressure, swap quickly, and the lost refrigerant is negligible. Confirm new sensor reads correctly in service mode before closing the panel.

8. **Clear codes, verify, and document.** Clear code history, watch a full freeze and harvest cycle while monitoring live transducer voltage and confirming the readings track actual pressures throughout the cycle. If voltage tracks correctly and the 5-flash doesn't return, you're done.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|------|------------|--------------|--------------|
| High-side pressure transducer (Prodigy Plus) | 12-2920-31 | $145-$215 | [Parts Town](https://partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=scotsman-5-flash-code) |
| Pressure transducer harness | 12-2935-01 | $58-$92 | [Parts Town](https://partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=scotsman-5-flash-code) |
| Transducer Schrader core kit | 02-3415-01 | $12-$22 | [Parts Town](https://partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=scotsman-5-flash-code) |
| Control board (Prodigy Plus) | 12-2838-21 | $295-$420 | [Parts Town](https://partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=scotsman-5-flash-code) |
| Schrader core depressor tool | — | $14-$24 | [Amazon](https://amazon.com) |
| Multimeter with min/max (Fluke 117) | — | $189-$220 | [Amazon](https://amazon.com) |
| Back-probe lead set | — | $32-$48 | [Amazon](https://amazon.com) |

Verify part numbers against the serial-plate model on your specific unit — the transducer P/N varied between 2018 and 2024 production.

## When to call a professional

If your diagnosis points to a clogged sensor port and the unit doesn't have a service Schrader at the transducer mount (some early Prodigy Plus builds don't), you'll need recovery and a brazing setup to safely remove the sensor — EPA 608 work. If you've cleared the sensor, the wiring, and the port and the 5-flash still comes back, the control board itself may have a faulty ADC channel for that input. Board replacement requires parameter and dip-switch configuration to match the head model; if you've never done a board swap on a Prodigy Plus, watch a Scotsman service video or call a contractor — running the wrong model parameters will give you a ghost-coded unit that won't ice properly.

Brilliance R-290 units: any work that opens the refrigerant circuit requires HC-certified handling and ventilation. Don't improvise.

## FAQs

**Q: The 5-flash comes and goes. Is the sensor failing or fine?**
A: Intermittent 5-flash codes are almost always a connector or wiring issue, not the sensor element itself. Pull the connector, inspect for green corrosion or pin push-back, reseat firmly, and watch. If reseating clears it for 3-5 days, the connector body is degraded and you should replace the harness as a unit, not just resocket the pins.

**Q: I replaced the transducer and the code came back in 10 minutes. What went wrong?**
A: Three possibilities. One: the new sensor is also dead (Schrader-style sensors sometimes get shelf-damaged). Two: the sensor port is partially blocked and the new sensor is reading the same blocked-port value. Three: the harness is the actual fault and the new sensor is being driven by the same bad signal path. Pull the new sensor, test on a known-good rig if you have one, then move to the harness.

**Q: Can I run the unit without the pressure transducer connected?**
A: No. Most Prodigy Plus firmware revisions will refuse to enter a freeze cycle with the pressure transducer reading out of range — the controller uses it for cutoff and harvest decisions. A disconnected sensor reads as a hard fault and the unit will sit locked out.

**Q: Does the transducer affect the freeze cycle directly, or just protection?**
A: Both. On Prodigy Plus, the firmware uses high-side pressure as one of the inputs for the adaptive harvest-trigger logic — too-low head pressure or too-high head pressure can extend the cycle. Replacing a drifting transducer often clears a 5-flash AND restores normal cycle times if the cycle was getting long.

**Q: Why does the transducer fail more often than the mechanical pressure switch on older models?**
A: Electronic transducers have a thin diaphragm and sensing element that's sensitive to pressure spikes, vibration, and moisture intrusion at the connector. Mechanical pressure switches are essentially indestructible but provide on/off info only, not a continuous reading. The trade-off is more capable control at the cost of more sensor failures over a 10-year unit life.

## Related guides

- [Scotsman 2-Flash Code — Long Freeze Cycle](/posts/scotsman-2-flash-code)
- [Scotsman 3-Flash Code — Long Harvest Cycle](/posts/scotsman-3-flash-code)
- [Scotsman 4-Flash Code — High Discharge Temperature](/posts/scotsman-4-flash-code)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Hoshizaki vs Manitowoc ice machines](/posts/hoshizaki-vs-manitowoc-ice-machines/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Manitowoc vs Scotsman ice machines](/posts/manitowoc-vs-scotsman-ice-machines/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Manitowoc E01 long freeze cycle fix](/posts/manitowoc-e01-error-code/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** Hoshizaki E2 long freeze cycle fix

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Scotsman 1-flash bin full fix](/posts/scotsman-1-flash-code/)
