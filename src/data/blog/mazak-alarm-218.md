---
title: "Mazak Alarm 218 — Spindle Motor Overheat Fix"
description: "Mazak Alarm 218 (Spindle Motor Overheat) fires when the thermistor embedded in the spindle motor stator windings exceeds the trip threshold — typically..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "James Rutherford"
slug: mazak-alarm-218
featured: false
draft: false
tags:
  - mazak
  - cnc
  - industrial-maintenance
  - spindle-motor-overheat
---
## Quick answer

Mazak Alarm 218 (Spindle Motor Overheat) fires when the thermistor embedded in the spindle motor stator windings exceeds the trip threshold — typically about 302°F (150°C) on Mazatrol Matrix and M-Plus controls, slightly lower on older M32/M-Plus Junior. Nine times out of ten it isn't the motor — it's a fouled spindle cooler heat exchanger, low coolant level in the chiller, or a clogged motor fan filter dragging stator temperature up over a long roughing cycle.

## What Mazak Alarm 218 means

The spindle motor has a klixon or PTC thermistor (depending on motor vintage) wired through pins on the encoder feedback cable back to the spindle drive. On a Matrix or Matrix Nexus control, the spindle drive (Mazak-badged Mitsubishi MDS-D or MDS-DH series) reads the thermistor resistance continuously and posts Alarm 218 to the NC when temperature crosses threshold. The 218 latches — you cannot run the spindle until the motor cools and the alarm is acknowledged through Reset.

The control's internal logic adds a 5–10 second debounce before declaring 218, so a brief transient spike from a slug of hot air through the motor fan won't trip it. That same debounce is why operators sometimes see the temperature warning (a separate "spindle motor hot" message, no number) for 30 seconds before 218 lands. If you catch that pre-warning, you have time to pull the spindle out of cut and let it idle — a 1500 RPM no-load idle drops stator temperature about 20°F (11°C) per minute on a typical Integrex i-200.

The same alarm number on the older M32 and M-Plus controls means the same thing but reads from a different drive (Mazak MDS-A or MDS-B series on M32, MDS-C1 on M-Plus). The thermistor circuit and trip threshold are essentially the same, but the alarm history depth is shallower on those older controls — three events vs. ten on Matrix.

## Read the alarm history first

Do not clear 218 before you read the log. Clearing on a Matrix control does not wipe the alarm history, but it does drop the diagnostic snapshot that some Mazak service techs use to correlate spindle load against the trip.

On a Matrix or Matrix Nexus control:

1. Press the **Alarm** key on the operator panel (red triangle icon, upper right on Matrix; under the Maintenance menu on Smooth)
2. Tab to **Alarm History** (alarms shown with date/time and a sequential index)
3. The 218 entry includes spindle motor temperature at trip and the spindle load percentage at trip — write both down
4. Page back through history to look for prior warnings (the "spindle motor hot" pre-warning is logged as a separate entry, usually within the 10 minutes preceding the 218)
5. On Smooth (Smooth X, Smooth Ai, Smooth G), the path is **Maintenance → History → Alarm**, and the temperature-at-trip is shown in the detail pane on the right

On an older M32/M-Plus control:

1. Press **OPER ALM** to bring up the alarm screen
2. Use the page-down soft key to scroll through history (depth is 3–5 events depending on PLC version)
3. The detail will show alarm number, date, time, but not the temperature reading — for that you have to pull the spindle drive's own log via the maintenance port on the drive face

**Field insight — the one nugget that traps everyone on Alarm 218:** Mazak's spindle motor thermistor is a *negative-temperature-coefficient* type on Matrix-vintage motors (post-2008), but a *klixon snap-disc* on older M32-era motors. The Matrix control reads the NTC as a continuous resistance value, so a partial cable break inside the encoder cable jacket will be read as "infinite resistance = motor at 999°F = trip 218 immediately on power-up." If your 218 fires the instant you power on the machine, before the spindle has even turned, the motor is not overheating — you have a broken thermistor wire in the feedback cable, usually at the spindle headstock cable carrier where it flexes. Check resistance pin-to-pin at the drive end with the cable disconnected from the motor: should read 50–200 kΩ at room temperature on Matrix NTC, or a hard short on a cool klixon-type. Open circuit means broken wire.

## Common causes (ranked by frequency)

1. **Spindle cooler (chiller) low on refrigerant, low on coolant water, or with a fouled heat exchanger** — by far the most common; the chiller can't pull heat out of the motor jacket fast enough during sustained heavy roughing
2. **Motor fan filter clogged with chips and coolant mist** — on machines with a fan-cooled spindle motor (older Integrex, Quick Turn Nexus), the foam filter on the back of the motor housing chokes airflow and stator temperature climbs
3. **Broken thermistor wire in the spindle encoder cable** — usually at the cable carrier flex point at the headstock; reads as infinite resistance = trip on power-up
4. **Aggressive roughing program with insufficient dwell time between heavy cuts** — toolpath problem masquerading as a machine fault; common after a CAM post update or a new operator
5. **Spindle bearing dragging from preload loss or contamination** — adds parasitic load, motor draws more current to maintain RPM, stator heats faster
6. **Failed thermistor inside the motor stator** — rare but does happen; usually after a motor rewind or a coolant ingress event

## Step-by-step diagnosis

Before you open anything: lock and tag the main disconnect at the cabinet, wait at least 5 minutes for the spindle drive bus capacitors to bleed down, and verify zero energy on the DC bus terminals of the spindle drive with a CAT-III meter. If the spindle is vertical or has any stored mechanical energy (live tooling, milling spindle in a turn-mill), release the spindle brake by hand per Mazak's procedure in the maintenance manual before reaching anywhere near the drawbar or spindle nose.

1. **Read alarm history before clearing.** Note the spindle motor temperature at trip, the spindle load percentage at trip, and any prior warnings within the last hour of run time. A trip at 150°C with 95% load tells a different story than a trip at 152°C with 30% load (the second is almost always a cooling problem, not a load problem).

2. **Check the spindle cooler.** Most Integrex, Quick Turn, and Variaxis machines use a Habor, Daikin, or Kuken oil chiller. Verify: (a) coolant level in the chiller reservoir (top of sight glass, not bottom), (b) heat exchanger fins clean and not packed with mist residue — pop the side cover and look, (c) chiller fan running when the spindle is hot, (d) outlet temperature within 5°F of setpoint when running. A chiller setpoint is typically 68–77°F (20–25°C); if outlet temp is at setpoint but motor still trips, the chiller is fine and the problem is downstream.

3. **Check coolant flow through the spindle motor jacket.** On a Mazatrol control: **Maintenance → Spindle → Cooler** shows flow rate and return temperature in real time on Matrix and Smooth controls. If flow is below the spec value on the chiller nameplate (typically 8–12 L/min on Integrex-class machines), suspect a clogged inlet strainer or a kinked hose at the headstock.

4. **Verify thermistor circuit integrity.** Power off, lock out, pull the encoder/feedback connector at the spindle drive end. Use a multimeter on the thermistor pair (pin assignment is in the spindle drive manual, section "Feedback Connector CN2" — usually pins 9 and 10 on MDS-D, pins 11 and 12 on MDS-DH). At room temperature you should read 50–200 kΩ on a Matrix-era NTC, or near-short (under 10Ω) on a klixon-type. Open circuit = broken wire in cable, usually at the headstock cable carrier.

5. **Check the motor fan.** On fan-cooled motors, the foam filter on the back housing should be cleanable in soapy water — replace if it's torn or permanently coolant-stained. The fan itself should spin freely by hand with no bearing rumble. If the fan stops running while motor temperature climbs, the fan is failed.

6. **Pull the alarm history correlated against the program.** If 218 always fires on the same line of the same NC program, the operator or programmer needs to reduce feed/speed at that cut or add a dwell. This is a process problem, not a machine problem — but it shows up at maintenance because the operator hits Reset and keeps running until something melts.

7. **Measure spindle drag.** With the machine at operating temperature but spindle off, rotate the spindle by hand (release the brake first if needed). It should turn smoothly with consistent torque. A binding spot, a rumble, or noticeably higher torque than a sister machine indicates bearing trouble. A spindle that has lost preload draws more current at every RPM, which over a long roughing cycle is enough to trip 218 even though the cooler and thermistor are fine.

8. **Bypass-test the thermistor with a known resistor.** Last-resort diagnostic. Disconnect the thermistor at the drive end and substitute a 100kΩ resistor across the same pins. Power up. If the alarm clears and stays cleared at idle, the thermistor or its cabling is the problem. **Do not run production with the resistor in place** — you have just disabled the motor's only thermal protection.

9. **Pull the motor and inspect the windings** if everything above checks out. Look for discoloration on the end-turns (varnish darkened past tan into brown = motor has been over-temp; past brown into black = winding insulation is compromised, motor needs rewind or replacement).

## Parts that may need replacement

Mazak sells spindle motors as complete assemblies under maker part numbers in the format MZ-####-####. They do not ship stator-only or rotor-only replacements outside of factory rewind service. For chillers, Habor and Daikin sell direct, and Mazak resells the same units with their own part number on the tag.

| Part | Part Number (form) | Typical Cost | Where to Buy |
|---|---|---|---|
| Spindle oil chiller, Habor 200V class | HBO-200-D-AS-FN (Habor cross) | $2,800–$3,800 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=mazak-alarm-218), [Wolf Automation](https://www.wolfautomation.com) |
| Spindle motor thermistor cable assy (Matrix) | MZ-cable PN from spindle parts list | $480–$720 | Mazak direct, eBay used |
| Motor fan kit (rear fan, Integrex i-200) | MZ-fan PN per maintenance manual | $310–$450 | Mazak direct, eBay |
| Motor fan filter foam (cut to fit) | generic foam, 1/4" thick | $18–$30 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| Replacement spindle motor (Quick Turn Nexus 250) | MZ-spindle assy PN | $9,500–$14,000 | Mazak direct, eBay (used, often pulled) |
| Thermistor harness pins/contacts | Tyco MR-#### crimp | $4–$12 each | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=mazak-alarm-218), [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| CAT-III multimeter for thermistor R-check | Fluke 87V | $480–$560 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=mazak-alarm-218) |
| Inspection scope for spindle bore | Vividia VA-980 | $390–$540 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |

## When to call a CNC service engineer

Call Mazak Technical Service (or your authorized dealer) when: the thermistor and cooler test good but 218 keeps firing under normal load (suggests internal motor problem requiring rewind or replacement); the spindle rotates by hand with detectable roughness (bearing replacement on most Integrex and Variaxis spindles is a factory operation, not a field job); the chiller has been replaced and outlet temperature still drifts; or any time you suspect the spindle drive itself (MDS-D, MDS-DH) is misreading the thermistor — drive diagnostics require a Mazak service laptop with the proprietary diagnostic software.

## FAQs

**Can I reset Alarm 218 and keep running if the motor feels only warm to the touch?** You can press Reset once the temperature drops back below threshold, and the alarm will clear. But the underlying cause (cooler, fan, thermistor, drag) is still there. Two or three repeated trips on the same shift will char the winding varnish even if no single trip is dramatic. Fix the root cause.

**My 218 fires only after lunch when the shop warms up. Real or coincidence?** Real. Ambient temperature stacks on top of motor temperature. If your shop swings from 68°F at 7 AM to 88°F by 1 PM, the chiller has 20°F less headroom in the afternoon. Either improve cooler airflow (clean the heat exchanger fins, ensure the chiller isn't blowing into a wall) or lower the chiller setpoint by 5°F.

**Reference Mazak Maintenance Manual section for the spindle cooler?** On Matrix machines: Maintenance Manual chapter "Spindle System / Spindle Cooler Unit." The chiller flow spec, setpoint range, and filter cleaning interval are in the same chapter. Mazak's recommended interval for heat exchanger fin cleaning is every 6 months in a typical shop, every 3 months in a heavy-mist environment.

**Does Alarm 218 mean the motor is destroyed?** Not by itself — the trip exists precisely to prevent destruction. A single 218 event from a transient is fine. Repeated 218 events without addressing the cause, especially while the operator hits Reset and runs through, will eventually destroy the winding insulation. Look at the alarm history depth: one or two events per month is acceptable while you diagnose; ten events per shift means you have already done damage.

**Difference between Alarm 218 and Alarm 230?** 218 is spindle motor stator overheat (thermistor in windings). 230 on most Mazak controls is spindle drive overtemperature (heat sink thermistor on the drive itself in the cabinet). 230 means the cabinet cooling is the problem — door seals, cabinet fan, panel A/C — not the motor.

## Related guides

- [Mazak Alarm 415 — Position Detector Error Fix](/posts/mazak-alarm-415/)
- [Mazak Matrix Alarm 1041 — Battery Voltage Drop Fix](/posts/mazak-alarm-1041/)
- [Mazak Servo Parameter Error Fix](/posts/mazak-servo-parameter-error/)
- [Fanuc Alarm 300 — APC Battery Voltage Low Fix](/posts/fanuc-alarm-300/)
- [Fanuc Alarm 430 — Servo Motor Overheat Fix](/posts/fanuc-alarm-430/)
- [Haas Alarm 128 — Spindle Drive Fault Fix](/posts/haas-alarm-128/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Best multimeter for HVAC techs (2026)](/posts/best-multimeter-for-hvac/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Best clamp meter (2026)](/posts/best-clamp-meter-for-electricians/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Best 4-20mA loop calibrator](/posts/best-loop-calibrator-for-vfd-techs/)

## See Also

- [Mazak Matrix Alarm 1041 — Battery Voltage Drop / Encoder Battery Fix](/posts/mazak-alarm-1041/)
- [Mazak Alarm 700 — MPC Alarm](/posts/mazak-alarm-700-mpc/)
- [Mazak CNC Alarm 30 — Servo Alarm Fix](/posts/mazak-cnc-alarm-30-servo-alarm/)
- [Mazak Alarm 900 Tool Magazine Index Fault - Causes & Fix](/posts/mazak-alarm-900-magazine/)
