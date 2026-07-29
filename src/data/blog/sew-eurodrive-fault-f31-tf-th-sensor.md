---
title: "SEW-Eurodrive Fault F31 (TF/TH Sensor Tripped): Motor Thermistor Troubleshooting on MOVITRAC B and MOVIDRIVE B"
description: "SEW fault F31 means the motor's TF thermistor or TH thermostat tripped — or the sensor loop is open. How to ohm out the loop, when to jumper X10:1-X10:2 on MOVIDRIVE B, and what P835 controls."
pubDatetime: 2026-07-28T08:00:00Z
modDatetime: 2026-07-28T08:00:00Z
author: "Error Code Fixes Editorial Team"
slug: sew-eurodrive-fault-f31-tf-th-sensor
featured: false
draft: false
tags:
  - vfd
  - sew-eurodrive
most_likely_cause: "Open TF/TH sensor loop — sensor not connected, miswired, or the wiring between motor and drive is interrupted"
free_checks:
  - "Let the motor cool and reset"
  - "ohm out the TF/TH loop with the drive locked out"
  - "inspect the motor terminal box and drive-side sensor terminals"
---

## What this code means

SEW-Eurodrive fault F31 is **TF/TH sensor tripped** — the drive's thermal motor protection input has fired. In SEW's own words, motor winding temperature "is monitored using TF thermistors or TH bimetallic switches": TF is a thermistor, TH is a bimetallic switch (thermostat). Wired to the drive's sensor input, that loop is monitored by the inverter itself, and no additional monitoring unit is required. F31 means the drive no longer sees a healthy loop.

The catch, and the reason F31 wastes so much troubleshooting time, is that **two completely different problems produce the identical fault**. SEW's own error list gives three causes for F31:

1. The motor is too hot — the TF thermistor or TH thermostat has legitimately triggered.
2. The TF/TH is not connected, or is connected incorrectly.
3. The connection between the drive and the TF/TH on the motor is interrupted.

Cause 1 is the sensor doing its job. Causes 2 and 3 are wiring problems that *look* like an overheated motor to the drive, because an open loop and a hot thermistor are electrically the same thing. Your first task with any F31 is deciding which side of that line you are on.

The fault response also differs by drive family, and it matters:

- **MOVITRAC B:** F31 causes a stop with inhibit.
- **MOVIDRIVE B (MDX60B/61B):** the factory default response is **"No response"** — the reaction is programmable via parameter **P835**.

That MOVIDRIVE B default has a practical consequence: an MDX drive fresh out of the box ignores the TF input. If your MOVIDRIVE B is actively tripping on F31, someone set P835 to a tripping response — almost always deliberately, to protect the motor. Do not "fix" the fault by quietly setting P835 back to "No response" unless you have confirmed the motor genuinely has no TF/TH fitted and is protected some other way.

## TF thermistor vs. TH bimetallic switch

SEW fits one of two winding-temperature sensors, and knowing which one you have tells you what a healthy loop should look like at the meter:

- **TF (thermistor):** a temperature-dependent resistor sitting in the motor windings. Its resistance climbs sharply once the winding reaches its trip temperature. Cool motor = low resistance across the loop. Hot motor (or broken wire) = high resistance or open.
- **TH (bimetallic switch):** a bimetallic contact in the windings, closed when the motor is cool and opening at its trip temperature. Cool motor = continuity. Hot motor (or broken wire) = open circuit.

Either way, "open" is what the drive interprets as tripped — which is exactly why a wire that fell off a terminal produces the same F31 as a cooked motor.

Where the loop lands differs by drive family, and this is worth checking before you go hunting for terminals that do not exist on your unit:

- **MOVIDRIVE B (MDX60B/61B):** the sensor connects at **X10:1 (TF1, the KTY+/TF-/TH connection)**, returning to **X10:2 (DGND)**. X10:1 is factory set to "No response" via P835.
- **MOVITRAC B:** SEW's documented wiring is the **TF output VOTF and the TF input DI05TF**, with binary input DI05TF set to the TF signal. There is no documented X10:1-X10:2 jumper on MOVITRAC B — that provision is specific to MOVIDRIVE B. SEW also notes that TH bimetallic switches can alternatively be wired to 24VIO and a binary input set to "/External fault," in which case an open sensor shows up as an external-fault trip rather than F31.

One measurement rule: **check the sensor loop with a standard multimeter on a resistance range, never with an insulation tester (megger).** Insulation-test voltage belongs on the motor power windings, not on the thermistor circuit — it can damage the sensor. If you megger the motor, disconnect the sensor leads first.

## Common causes

- **Sensor loop never wired in (new installs)** — F31 on first power-up of a fresh commissioning is almost always this. The TF/TH leads in the motor terminal box were never landed, or the sensor conductors in the motor cable were never terminated at the drive.
- **Interrupted loop on a machine that used to run** — a broken conductor in the motor cable, a corroded or vibrated-loose terminal in the motor terminal box, a chafed junction in a drag chain or conduit. The motor is cool, but the drive sees an open loop.
- **Motor genuinely overheating under load** — mechanical overload, a jammed or binding driven machine, too many starts per hour, or a duty cycle the motor was not sized for.
- **Cooling failure** — clogged fan cover, dirt-packed cooling fins, a broken shaft fan, or high ambient temperature around the motor.
- **Long running at low speed on a self-ventilated motor** — a standard motor's shaft-mounted fan moves far less air at low speed. A drive-fed motor loitering at low frequency under load can cook itself even though the current never looks alarming. Forced-ventilation fan kits exist for exactly this duty.

## Step-by-Step Fix {#fix}

Safety first: the sensor terminals live in the same enclosures as lethal voltages. The drive's DC bus holds a dangerous charge for minutes after power-off, and the motor terminal box carries the full output voltage. Lock out and tag out, wait the discharge time stated in the manual, and verify zero volts before opening either enclosure.

1. **Decide: hot motor or broken loop?** Was the motor working hard when it tripped, and is the frame hot to a careful touch? If yes, treat it as real overheating (steps 2 and 7). If the motor is cool — or F31 appeared the moment a new installation was powered up — treat it as a wiring/sensor problem (steps 3-6).
2. **Let the motor cool off and reset.** This is SEW's documented first action. If the fault clears after cooling and only returns after a stretch of hard running, the sensor is telling the truth; go to step 7.
3. **Ohm out the TF/TH loop.** Lock out, disconnect the sensor leads at the drive's sensor terminals, and measure resistance across the loop with the motor cool. A cool, healthy loop reads low resistance (TF) or dead continuity (TH). An open reading (OL) with a cool motor means the fault is in the wiring or the sensor, not the temperature.
4. **Split the loop to localize the break.** Open the motor terminal box and measure across the sensor terminals there. Open at the motor terminals with a cool motor points at the sensor itself or its internal leads; good at the motor but open at the drive end points at the interconnecting cable or a loose drive-side terminal. Re-land, repair, or replace as found.
5. **Check for miswiring.** On a new install, confirm the sensor conductors actually go to the drive's TF/TH input and not to a shield bar or a spare terminal, and confirm nobody ran the sensor pair inside the motor power cores where induced voltage and miswiring cause grief.
6. **No sensor fitted? Jumper it — on MOVIDRIVE B, X10:1 to X10:2.** SEW's documented provision when no TF/TH is connected on a MOVIDRIVE B is a jumper from terminal X10:1 to X10:2. Alternatively P835 can be set to "No response" where that is appropriate. Only do either when the motor truly has no TF/TH and is protected another way — see the next section before you reach for a wire link.
7. **If the motor is genuinely hot, fix the heat.** Clear the fan cover and fins, verify the shaft fan is intact, reduce the load or the starts-per-hour, lengthen accel ramps, and check for a binding driven machine. For sustained low-speed duty, fit forced ventilation or size up the motor. A repeatedly overheated motor also deserves an insulation test (sensor leads disconnected first) before you trust it again.

## When NOT to jumper out the sensor

The X10:1-X10:2 jumper and the P835 "No response" setting exist for motors that legitimately have no TF/TH fitted. They are not a workaround for a nuisance trip. Do not defeat the thermal sensor when:

- **The drive moves a hoist or any lifting application.** A motor that fails hot on a suspended load is a dropped-load scenario, not an inconvenience.
- **The motor is in an explosion-rated (Ex/ATEX) zone.** This is not a judgement call. SEW's startup section for explosion-proof AC asynchronous motors states that a certified safety function is used *in conjunction with temperature sensors in the motor* to provide safe operation in potentially explosive areas, and that the motor must be approved for such operation per its nameplate and EC type examination certificate. The thermistor is part of the certified protection scheme. Bridging it makes the installation non-compliant and genuinely dangerous. Stop and involve whoever owns the site's Ex documentation.
- **The machine runs unattended** — nights, weekends, remote pump houses. The thermistor is the only thing standing between a cooling failure and a burned-out motor (or worse).
- **You have not actually confirmed the loop is broken.** If you have not put a meter on the loop, you do not know the motor is not hot.

A jumper installed "temporarily" during commissioning has a way of becoming permanent. If you must bridge the input to keep production moving after confirming a cable fault, tag the drive, log it, and schedule the cable repair.

## F11 vs. F31 vs. F84: three thermal faults, three different things overheating

SEW drives report three distinct thermal problems with three different codes. Mixing them up sends you to the wrong end of the machine.

| Code | What it watches | What SEW says causes it | First fix |
| --- | --- | --- | --- |
| F11 | **The drive itself** — heat sink temperature too high, or its temperature sensor defective. On size 7 units, sub-codes 6-8 indicate the phase-module sensor for phase U/V/W; sub-code 3 is overtemperature of the switched-mode power supply. | Thermal overload of the inverter; a defective phase-module temperature sensor; on MOVITRAC B, a braking resistor integrated in the heat sink adds heat. | Reduce load and improve cooling; check the fan. If F11 trips when the drive is clearly not hot, the sensor is faulty (phase-module replacement on size 7). On MOVITRAC B, mount the integrated braking resistor externally. |
| F31 | **The motor's physical sensor** — the TF thermistor / TH thermostat loop. | Motor too hot; TF/TH not connected or connected incorrectly; the drive-to-sensor connection interrupted. | Cool and reset; test and repair the sensor loop; jumper X10:1-X10:2 on MOVIDRIVE B only if no sensor is fitted. |
| F84 | **The drive's calculated thermal motor model / UL monitoring** — no physical sensor required. Sub-code 2: short or open circuit in the temperature sensor (KTY type, set via P530); sub-code 3: no thermal motor model available. | Motor utilization too high; IN-UL monitoring (P345/P346) triggered. | Reduce load, extend ramps, allow longer pauses between cycles; check P345/P346; select a larger motor if it is undersized. |

The practical read: **F11 = drive hot, F31 = motor's own sensor says hot (or its loop is open), F84 = the drive's math says the motor is being overworked.** A machine that throws F84 but never F31 is being thermally overworked in a way the model catches before the winding sensor does — that is a sizing or duty-cycle conversation, not a wiring one. A machine that throws F31 with a cool motor is a wiring problem, full stop.

## When to Call a Pro

- **The TF/TH itself is dead.** The sensor sits inside the motor windings, so it is not a field-replaceable part. A failed sensor on an otherwise good motor means a motor shop visit — and on a motor that has been repeatedly overheated, a rewind-versus-replace decision.
- **The motor has tripped hot more than once for no obvious reason.** Repeated legitimate trips mean an insulation test and a hard look at sizing and duty cycle before the winding fails outright.
- **Anything involving an Ex-rated motor.** Thermal protection on certified motors is a compliance matter. Get the qualified people in.
- **You suspect the drive's sensor input.** If the loop measures healthy at the drive terminals with the motor cool and F31 persists, the drive-side input may be at fault — that is a unit-level repair for an SEW-certified technician.
- **Any work inside the drive.** The DC bus stores a lethal charge after power-off. If diagnosis goes past the accessible terminals, stop and bring in a qualified tech.

## Frequently asked questions

### Why do I get F31 immediately on a brand-new installation?

Because the sensor loop was never completed. On first power-up the drive sees an open TF/TH circuit and reports it as a tripped sensor. Land the TF/TH leads from the motor terminal box on the drive's sensor input. If the motor genuinely has no TF/TH, SEW's documented provision on MOVIDRIVE B is a jumper from X10:1 to X10:2.

### The motor is stone cold but F31 won't clear. What's wrong?

The loop is open somewhere between the drive and the winding sensor. An open circuit is electrically identical to a hot thermistor, so the drive keeps reporting F31. Lock out, disconnect the sensor leads at the drive, and ohm the loop; then split it at the motor terminal box to find which segment is broken.

### Can I just set P835 to "No response" and move on?

P835 is the documented parameter for the TF sensor response on MOVIDRIVE B, and "No response" is actually the factory default — so if the drive is tripping, someone configured that protection on purpose. Only disable it when the motor has no TF/TH fitted and has other thermal protection, and never on hoists, Ex-zone motors, or unattended machinery.

### What's the difference between F31 and F84?

F31 comes from the physical sensor in the motor windings. F84 comes from the drive's calculated thermal motor model and IN-UL monitoring (parameters P345/P346) — it can fire with no motor sensor connected at all, and its sub-codes cover a short/open KTY sensor (sub-code 2, sensor type set in P530) and a missing thermal model (sub-code 3). F84's cure is load, ramps, pauses, and motor sizing; F31's cure is cooling, the sensor loop, or both.

### Can I test the thermistor with an insulation tester?

No. Megger the motor windings if you need to, but disconnect the TF/TH leads first and test the sensor loop only with a standard multimeter on a resistance range. Insulation-test voltage can destroy the thermistor.

## Sources

The F31 causes and responses, the X10:1-X10:2 provision, P835, and the F11/F84 comparisons were checked against these two SEW-Eurodrive PDFs.

- *Compact Operating Instructions — MOVIDRIVE MDX60B/61B* (SEW-Eurodrive document 16920813) — Section 3 wiring diagram for the basic unit (terminal X10:1 "KTY+/TF-/TH connection, connect to X10:2 via TF/TH, factory set to 'No response' (→ P835)") and Section 6.2.3 Error list (F31, F11, F84 entries and sub-codes): [archived official PDF](https://web.archive.org/web/20130124101658/http://download.sew-eurodrive.com/download/pdf/16920813.pdf)
- *Operating Instructions V3 — MOVITRAC B* (SEW-Eurodrive document 16810813) — Section 4.9 "TF thermistor and TH bimetallic switch," Section 5.10 startup of explosion-proof AC asynchronous motors, and Section 7.2 List of faults (F-00 – F-113) for the MOVITRAC B F31, F11, and F84 entries: [archived official PDF](https://web.archive.org/web/20210805131920/https://download.sew-eurodrive.com/download/pdf/16810813.pdf)
