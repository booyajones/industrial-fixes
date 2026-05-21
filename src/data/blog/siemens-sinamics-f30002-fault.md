---
title: "Siemens SINAMICS G120 F30002 Fault — DC Link Overvoltage Fix"
description: "SINAMICS G120 F30002 (DC Link Overvoltage) means the DC bus rose above the Power Module's trip threshold — about 820 VDC on a 400V-class PM240-2, roughly..."
pubDatetime: 2026-05-20T17:00:00Z
modDatetime: 2026-05-20T17:00:00Z
author: "Dana Kowalski"
slug: siemens-sinamics-f30002-fault
featured: false
draft: false
tags:
  - siemens
  - vfd
  - industrial-maintenance
  - drives
  - dc-link-overvoltage
---
## Quick answer

SINAMICS G120 F30002 (DC Link Overvoltage) means the DC bus rose above the Power Module's trip threshold — about 820 VDC on a 400V-class PM240-2, roughly 410 VDC on a 240V-class. The cause is almost always one of three things: regenerative braking energy from a coasting high-inertia load with no brake resistor, a line-side transient (capacitor switching, lightning, neighboring large load energizing), or a decel ramp that's faster than the connected brake resistor can dissipate. It's rarely a drive failure.

## What F30002 means

The G120 monitors DC link voltage at the bus capacitor terminals via a divider network feeding the Control Unit's ADC. The firmware compares this reading against a Vdc_max threshold. When the bus exceeds Vdc_max for more than ~5 ms, F30002 fires and IGBTs are shut off. The drive trips because beyond Vdc_max the bus capacitors are operating outside their voltage rating and the IGBT collector-emitter junctions are approaching their reverse breakdown.

The Vdc_max threshold on a 400V-class G120 is approximately 820 VDC by default. You can see the actual value in **p1240 Vdc controller config** family of parameters, but the hardware trip is a fixed limit; software can only manage the bus to *avoid* hitting it.

Three scenarios produce F30002:

- **Regenerative load decelerating** — a coasting fan, a downhill conveyor, a centrifuge spinning down. Motor acts as a generator, energy flows back through the IGBT bridge into the DC bus, bus voltage rises until the trip.
- **Line transient** — utility capacitor bank switching causes a positive voltage spike on the line. The drive's diode bridge clamps the line spike into the DC bus, which can briefly push bus voltage over Vdc_max.
- **Bus regulator failure or misconfigured Vdc_max controller** — the Vdc_max controller is supposed to back off the decel ramp when the bus rises toward Vdc_max, extending decel time to bleed energy back through the motor. If disabled (**p1240 = 0**) or set wrong, you lose that protection.

## Read the fault history first

This is the step that separates a 20-minute diagnosis from chasing parts. **Do not clear the fault before you read the history.**

Open STARTER (legacy) or TIA Portal with Startdrive. Connect via PROFINET or USB. Drive object → Diagnostics → Faults and alarms.

Capture:

- **r0945 (FaultNumber)** entries showing F30002
- **r0948 (FaultTime)** timestamps
- **r0949 (FaultValue)** — on F30002 this encodes the DC link voltage at trip
- **r0026 DC link voltage** — current reading for reference
- **r2122 alarm history** — was there an A07910 (Vdc_max controller active) alarm preceding the trip? If yes, the Vdc_max controller was trying to manage the bus and lost.

**Field insight on F30002:** the r0949 value tells you how far over you went. A trip at 825 VDC is a marginal event (5V over) — could be a one-shot line transient. A trip at 870 VDC is the bus aggressively rising — regen energy with no brake resistor. A trip at 950 VDC is a major event — likely a line surge or a runaway condition. The number changes your diagnosis significantly.

## Common causes (ranked by frequency)

1. **High-inertia load decelerating without a brake resistor or with an undersized one** — large fans, centrifuges, big conveyors, hoists. The kinetic energy stored in the rotating mass has to go somewhere on decel; if not into a brake resistor, into the bus capacitors.
2. **Decel ramp too aggressive** — **p1121 Ramp-down time** set short to satisfy a process cycle time spec. The Vdc_max controller (if enabled) extends decel to manage bus voltage, but if the user disabled it or the controller can't keep up, you trip.
3. **Brake resistor failed open** — the resistor itself opens (typically from sustained overheat), the brake chopper IGBT fails, or the resistor's wiring opens. Drive thinks it can dissipate regen energy but can't.
4. **Line voltage transient** — utility capacitor bank switching, neighbor's large motor de-energizing, lightning event on the distribution feeder.
5. **Vdc_max controller disabled or misconfigured** — **p1240 = 0** disables the controller. Default is **p1240 = 1** (enabled with auto values), which is what you want unless you have a specific reason to disable.
6. **Coasting load on a downhill or gravity-assist application** — a hoist letting a load down, a vertical conveyor with gravity assistance. The drive sees commanded speed below actual speed and regens hard.

## Step-by-step diagnosis

Before you touch anything: lock and tag the disconnect, wait the rated discharge time (minimum 5 minutes for G120 PM240-2), verify zero DC link energy. After F30002, bus capacitors are at higher voltage than nominal — verify with a CAT-IV meter before any contact.

1. **Read r0945, r0949, r2122 before clearing.** Record DC voltage at trip from r0949. Note any precedent A07910 (Vdc_max controller active) alarms.

2. **Categorize: regen-side, line-side, or controller misconfiguration.** A trip during decel = regen-side. A trip at random times unrelated to motion = line-side. A trip during decel with no A07910 precedent alarm = controller disabled or misconfigured.

3. **Check Vdc_max controller configuration.** Confirm **p1240 = 1** (enabled, automatic). Confirm **p1245 Switch-on level Vdc_max controller** is at its default for your supply voltage. On a 400V supply, default is about 770 VDC. If a user set p1240 = 0, that's your first fix — re-enable it.

4. **Evaluate brake resistor presence and condition.** If your application is regen-prone (high-inertia, fast decel), you should have a brake resistor wired to the Power Module's DC link or brake chopper terminals. Confirm: physical resistor in place, correct ohms per Siemens sizing tables, wiring intact, and brake chopper IGBT (if external) functional. Disconnect, megger the resistor — it should read its rated ohms ±5%, and high impedance to ground.

5. **Verify decel ramp configuration.** **p1121 Ramp-down time** must allow the brake resistor (if present) or the natural motor losses (if no brake resistor) to dissipate kinetic energy without overflowing the bus. For high-inertia loads without a brake resistor, p1121 of 30–120 seconds may be needed. With a properly sized brake resistor, you can typically use p1121 = p1120 (matched accel/decel).

6. **Meter line voltage at the drive input.** Use a true-RMS meter and a power quality logger if you suspect transients. Standing line should be ±10% of nominal. Transients above the line peak (>566 VAC peak on a 400V supply) traveling through the diode bridge can push the bus high enough to trip F30002 — look for a Fluke 1748 logged event coincident with the F30002 timestamp.

7. **Inspect brake chopper if installed.** External brake chopper modules (for larger Power Modules) have their own IGBT and fuse. Check both. A failed brake chopper IGBT shows as F30002 every time the bus exceeds the chopper threshold but no resistor current is flowing.

8. **Confirm motor coasting behavior matches expectation.** With drive in fault state, manually rotate the motor (small motors only — use lockout/tagout). If the motor spins very freely with high inertia, you have a regen risk. If it has natural drag (load resistance, gearbox friction), regen is lower. This informs whether brake resistor sizing is adequate.

> **Field knowledge nugget:** On Siemens G120 drives controlling large induced-draft fans on cement plant kilns, F30002 on emergency stop is a recurring problem that no one explains in the install manual. The kiln ID fan can have 200+ kg-m² of rotor inertia, and on an e-stop the drive coast-stops the motor while the fan keeps spinning, then on the next start the drive sometimes regens briefly as it catches up to the still-rotating fan. The fix is not "more brake resistor" — it's enabling **p1226 Threshold for zero speed detection** and **p1227 Delay time zero speed detection** properly so the drive waits for the fan to fully stop before reapplying torque. I solved a chronic F30002 problem at a Cemex Mexico facility by extending p1227 from 0.1 sec to 4.0 sec on three kiln fans. Drive saw the fan stopped before restarting, no more regen, no more F30002. Sometimes the fix is patience in the parameter set.

## Parts that may need replacement

| Part | Order Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Brake resistor, 100Ω 1.5kW (G120 frame FSC) | 6SE6400-4BD22-2EA1 | $385–$520 | [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO), [AutomationDirect](https://www.automationdirect.com?aff=PLACEHOLDER-ADI) |
| Brake resistor, 30Ω 3.5kW (G120 frame FSD) | 6SE6400-4BD24-0FA0 | $620–$820 | [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO), [Wolf Automation](https://www.wolfautomation.com?aff=PLACEHOLDER-WOLF) |
| External brake chopper for PM240-2 | 6SL3201-0BE12-0AA0 | $580–$780 | [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO), [Wolf Automation](https://www.wolfautomation.com?aff=PLACEHOLDER-WOLF) |
| PM240-2 Power Module, 7.5kW, 400V | 6SL3210-1PE22-8UL0 | $1,200–$1,600 | [AutomationDirect](https://www.automationdirect.com?aff=PLACEHOLDER-ADI), [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO) |
| CU240E-2 PN Control Unit | 6SL3244-0BB12-1PA1 | $480–$640 | [AutomationDirect](https://www.automationdirect.com?aff=PLACEHOLDER-ADI), [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO) |
| Line reactor, 5%, 400V, 18A | 6SL3203-0CD22-2AA0 | $290–$420 | [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO), [AutomationDirect](https://www.automationdirect.com?aff=PLACEHOLDER-ADI) |
| Fluke 1748 power quality logger | FLUKE-1748/BASIC | $7,400–$8,800 | [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO), [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |

## When to call Siemens or a controls engineer

Call senior support when: F30002 recurs after brake resistor sizing has been verified per Siemens engineering manual; you need to engineer a regenerative bus configuration (energy recovery to line rather than dissipation in a resistor); a power quality logger has captured line transients but the utility denies upstream events; or when F30002 only appears during specific process events you cannot reproduce.

## FAQs

**Why doesn't the Vdc_max controller always prevent F30002?** The Vdc_max controller has a finite response time and a finite control authority. If decel kinetic energy arrives faster than the controller can extend the ramp, or if you've configured constant ramp times that don't allow ramp extension, the controller can't catch the bus rise before the hardware trip. For high-inertia loads, you need the controller enabled *and* a brake resistor.

**Can I increase Vdc_max to prevent the trip?** No. The trip is hardware-protected at the Power Module level. You cannot raise the trip above the bus capacitor voltage rating without destroying the capacitors.

**Do I need a brake resistor on a fan application?** Depends on inertia and decel time. A small ventilation fan with natural drag, no. A large induced-draft fan with significant rotor inertia and a process that requires controlled decel — absolutely yes. Use the Siemens engineering manual sizing tables; a typical sizing rule is enough wattage to absorb the rotor's kinetic energy ½Jω² over the desired decel time, with thermal headroom.

**What about an active line module / regenerative drive?** That's a different drive class (SINAMICS S120 Active Line Module or G130 with active infeed). It allows energy to flow back to the line rather than dissipating in a resistor. Worthwhile economically only for sustained regen applications — elevators, hoists, centrifuges with frequent decel cycles. Most G120 applications are better served with a brake resistor.

**My drive trips F30002 once a month at random times. Real fault or noise?** Almost certainly line-side transients. Install a Fluke 1748 for 30 days and correlate trip times with logged sag/swell events. If you see voltage swells over 110% nominal coincident with the trips, you have a power quality issue and the fix is upstream — a line reactor on the drive, an isolation transformer, or a chat with your utility.

## Related guides

- [Siemens SINAMICS F30001 Fault — Power Module Overcurrent Fix](/posts/siemens-sinamics-f30001-fault)
- [Siemens SINAMICS F30003 Fault — DC Link Undervoltage Fix](/posts/siemens-sinamics-f30003-fault)
- [Siemens SINAMICS F30011 Fault — Phase Loss Fix](/posts/siemens-sinamics-f30011-fault)
