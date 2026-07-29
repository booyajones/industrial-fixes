---
title: "SEW-Eurodrive Fault F14 (Encoder Error): Sub-Codes 25-34, Hiperface, Resolver, and X14/X15 Wiring Checks"
description: "Decode MOVIDRIVE B fault F14 by sub-code: 25 = X15 encoder past 6542 rpm, 28/29 = RS485 errors on X15/X14, 31-33 = Hiperface, 34 = resolver. Plus the cable, shield, and encoder-type checks that actually clear it."
pubDatetime: 2026-07-28T08:00:00Z
modDatetime: 2026-07-28T08:00:00Z
author: "Error Code Fixes Editorial Team"
slug: sew-eurodrive-fault-f14-encoder
featured: false
draft: true
tags:
  - vfd
  - sew-eurodrive
most_likely_cause: "Encoder cable or shield fault - broken wire, short circuit, or a connector not seated correctly"
money_part: "Replacement encoder (Hiperface, resolver, or incremental - matched to the motor)"
free_checks:
  - "Read the fault memory for the F14 sub-code before touching anything; it tells you which connector (X14 or X15) and which encoder interface faulted."
  - "With the drive locked out and the DC bus discharged, unplug and reseat the encoder connector at the drive and at the motor end, and inspect the pins for bent contacts or corrosion."
  - "Check the encoder cable shield termination at both ends, and walk the cable route looking for crush points, chafing in the cable track, or a splice someone added."
---

## What this code means

Fault F14 on a SEW-Eurodrive MOVIDRIVE MDX60B/61B is an **encoder fault**. The drive lost valid feedback from the motor encoder, and the response is **immediate disconnection**: the axis drops out on the spot rather than ramping down, because a closed-loop drive that can no longer trust its speed and position feedback has no safe way to keep controlling the motor.

SEW's error list gives three documented causes for F14:

- The encoder cable or its shield is not connected correctly
- A short circuit or a broken wire in the encoder cable
- The encoder itself is defective

That list looks short, but F14 carries an extensive **sub-error code** that identifies exactly which encoder interface failed and how. On the MDX61B, the encoder connections live on the **X14 and X15 connectors**, and the sub-code tells you which of the two the drive was talking to when the fault hit, and whether the problem is communication, plausibility, overspeed, the option card, or the encoder itself. Reading the sub-code first is the difference between a ten-minute diagnosis and an afternoon of swapping parts.

You will find the sub-code stored with the fault in the drive's fault memory, readable from the keypad or through MOVITOOLS MotionStudio. Get it before you power anything down.

## F14 sub-codes 25-34: the full table

| Sub-code | Connector | What SEW says it means |
| --- | --- | --- |
| 25 | X15 | Speed range exceeded - the encoder is turning faster than 6542 rpm |
| 26 | X15 | Card defective (quadrant evaluation) |
| 27 | X14/X15 | Encoder connection faulty or encoder defective |
| 28 | X15 | RS485 communication error |
| 29 | X14 | RS485 communication error |
| 30 | X14/X15 | Unknown encoder type |
| 31 | X14/X15 | Hiperface plausibility error (lost increments) |
| 32 | X15 | Hiperface encoder error |
| 33 | X14 | Hiperface encoder error |
| 34 | X15 | Resolver error |

Read the table in three groups:

- **Wiring and communication faults (27, 28, 29, 31):** the drive and encoder are losing data between them. Sub-codes 28 and 29 are RS485 communication errors, and the only thing that changes between them is the connector: 28 points at X15, 29 points at X14. Sub-code 31 is a Hiperface plausibility error, meaning the drive detected lost increments - the feedback stream is arriving, but it does not add up. All of these point first at the cable, the shield, and the connectors, not at the encoder.
- **Encoder hardware faults (32, 33, 34):** the encoder itself is reporting or exhibiting an internal error. 32 is a Hiperface encoder error on X15, 33 is the same on X14, and 34 is a resolver error on X15. Check the wiring anyway - it is free - but these sub-codes are where a replacement encoder becomes the likely outcome.
- **Configuration and application faults (25, 26, 30):** sub-code 30 means the drive sees an encoder type it does not recognize on X14/X15, which is a setup problem, not a broken part. Sub-code 25 means the encoder on X15 exceeded its speed range of 6542 rpm, which is an application problem: something drove that shaft faster than the feedback system allows. Sub-code 26 flags the X15 card itself as defective in quadrant evaluation, which is an option-card replacement, not an encoder replacement.

## Common causes

- **Broken encoder wire.** The classic F14. Encoder cables on servo axes routinely live in cable tracks and flex thousands of cycles a day. A single cracked conductor produces intermittent F14 trips that get more frequent over weeks. Intermittent faults that correlate with a particular machine position or motion are a flexing-cable signature.
- **Shield not connected correctly.** SEW lists the shield connection explicitly as an F14 cause. A floating or poorly terminated shield lets electrical noise from the motor cable and surrounding equipment corrupt the feedback signals, which typically shows up as the communication and plausibility sub-codes (28, 29, 31) rather than a hard, permanent fault.
- **Short circuit in the cable.** Crushed cable, pinched at a gland, or moisture in a connector shorting adjacent pins.
- **Connector problems.** A connector that was never fully latched after motor service, bent pins, or corrosion at either the drive end (X14/X15) or the motor end.
- **Defective encoder.** Real, but statistically the last thing on the list. Sub-codes 32, 33, and 34 are the ones that legitimately point here.
- **Wrong encoder type configured.** Sub-code 30 (unknown encoder type at X14/X15) is a commissioning or replacement-motor problem: the encoder type set in the drive does not match what is physically connected.

## Step-by-Step Fix {#fix}

1. **Read the fault memory first.** Get the F14 sub-code from the keypad or MOVITOOLS MotionStudio before cycling power. Note whether the fault is on X14 or X15 and whether it recurs at specific machine motions.
2. **De-energize and lock out.** These drives hold a lethal charge on the DC bus after power is removed. Lock out, wait the full discharge time stated in the manual, and verify zero volts before handling drive connectors or opening anything. If you are not qualified to work on drive power circuits, stop here and get someone who is - the feedback checks below only start after the drive is verified dead.
3. **Reseat both ends of the encoder cable.** Unplug the connector at X14 or X15 (whichever the sub-code named) and at the encoder end on the motor. Inspect pins for bending, corrosion, and moisture. Re-latch fully.
4. **Check the shield.** Verify the cable shield is actually terminated the way the SEW wiring diagram for your encoder type shows, at both ends. A shield that was cut back and never landed during installation can work for years and then start throwing F14 as the electrical environment changes.
5. **Test the cable.** With both ends unplugged, check conductor-to-conductor and conductor-to-shield for shorts, and check each conductor end-to-end for continuity while flexing the cable at the points where it moves. An intermittent open that only appears under flex is the most commonly missed find in this whole procedure.
6. **Verify the encoder type configuration.** For sub-code 30, and any time the motor or encoder was recently replaced, confirm the encoder type set in the drive matches the hardware on the shaft. A mismatch can also surface as fault F36 (see below) when the wrong type is set for the DIP11B absolute encoder card.
7. **Chase sub-code 25 as an application problem.** If the drive says the X15 encoder exceeded 6542 rpm, the encoder and cable may be fine. Ask why that shaft overspeeds: an overhauling load, wrong gearing after a mechanical change, or a setpoint and control configuration that lets the motor run away.
8. **Replace hardware last, and by sub-code.** Sub-code 26 condemns the X15 option card. Sub-codes 32, 33, and 34, with the cable and shield proven good, condemn the encoder or resolver. Swap the component the sub-code names, not the first thing that is easy to reach.

## The encoder-fault family: F08, F42, and F36

Encoder problems on MOVIDRIVE B do not always announce themselves as F14. Three other faults commonly trace back to the feedback system, and knowing which one you have narrows the search.

| Code | What it means | Encoder connection |
| --- | --- | --- |
| F08 | Speed monitoring (immediate disconnection, response programmable) | Encoder not connected correctly, or wrong direction of rotation - the A/A-bar and B/B-bar channel pairs swapped |
| F42 | Lag error - positioning following error (immediate disconnection, programmable) | Encoder connected incorrectly is the first documented cause; also short ramps, small P-component, small lag tolerance, blocked mechanics |
| F36 | Option missing / hardware not permitted (immediate disconnection) | Incorrect encoder type set for the DIP11B absolute encoder card; sub-code 2 = encoder slot error |

**F08 (speed monitoring)** trips when the speed or current controller sits at its set limit. Mechanical overload and a missing supply or motor phase are the headline causes, but a wrong-direction encoder is the sneaky one: if the A/A-bar and B/B-bar pairs are swapped, the drive sees rotation opposite to what it commands, drives harder, and F08 follows almost immediately at enable. SEW's remedy list includes checking the encoder connection, the wiring pairs, and the encoder supply voltage. Speed monitoring is configured in P500/P502 with delay times in P501/P503, and SEW's own footnote is blunt about the safety boundary: deactivating the monitoring or setting the delay too long cannot safely prevent a hoist from sagging. On a hoist axis, fix the fault - never widen the monitoring to make it go away. Sub-code 3 flags the actual-speed system limit exceeded, and sub-code 4 flags the maximum rotating field frequency exceeded (150 Hz in VFC mode, 600 Hz in V/f). We cover the full fault in the [SEW-Eurodrive F08 guide](/posts/sew-eurodrive-fault-f08/).

**F42 (lag error)** is the positioning-mode cousin. The position controller compares commanded position against encoder-reported position, and when the difference exceeds the lag error tolerance, the axis trips. An incorrectly connected encoder is the first cause in SEW's list, ahead of acceleration ramps that are too short, a positioning-controller P-component that is too small, badly set speed controller parameters, a lag tolerance set too tight, and mechanics that are simply blocked. The documented remedies run in the same order: check the encoder connection and the wiring of motor and mains phases, extend the ramps, increase the P-component and the lag error tolerance, reset the speed controller parameters, and confirm the mechanism actually moves freely.

**F36 (option missing / hardware not permitted)** is the fault that appears when the drive's option-card and encoder configuration does not match reality: an option card type that is not allowed, a setpoint source, control signal source, or operating mode not permitted for the fitted card, or an incorrect encoder type set for the DIP11B absolute encoder card. Sub-codes 2, 3, and 4 map to the encoder slot, fieldbus slot, and expansion slot respectively. The fix is configuration: fit the correct card, set P100/P101 and P700/P701 correctly, and set the correct encoder type. On MOVITRAC B the equivalent checks are P121 for the FBG11B keypad and P120 plus P642 for the FIO12B option.

If you are seeing F14 and one of these together in the fault history, work the F14 sub-code first. A feedback path you cannot trust will keep generating downstream speed-monitoring and lag faults no matter how much you tune.

## When to call a pro

Anything inside the drive enclosure sits on or near the DC bus, which holds lethal voltage after power-off. If you are not trained and authorized for drive-level electrical work, limit yourself to reading the fault memory and inspecting the accessible encoder cable route, and bring in a qualified technician for the rest.

Call SEW service or a qualified drives technician when the cable and shield test good and the configuration is verified but F14 persists (that is option-card or encoder territory, and sub-codes 26, 32, 33, and 34 say which), when sub-code 25 overspeed keeps recurring and the mechanical cause is not obvious, or when the axis is a hoist. On hoists, remember SEW's warning on the related speed-monitoring parameters: monitoring exists to stop the load from sagging, and no one should ever widen or disable it to silence a fault.

## Frequently asked questions

### Where do I see the F14 sub-code?

It is stored with the fault in the drive's fault memory. Read it from the keypad or with MOVITOOLS MotionStudio before you cycle power, and note it down; the sub-code is the single most useful piece of information in the whole diagnosis because it names the connector (X14 or X15) and the failing element.

### What is F14 sub-code 25, exactly?

Sub-code 25 means the encoder on X15 exceeded its permissible speed range: it turned faster than 6542 rpm. Treat it as an application or mechanical problem, not a wiring problem. Something allowed the shaft to spin beyond what the feedback system supports.

### F14 sub-code 28 vs 29 - what is the difference?

Both are RS485 communication errors on the encoder interface. The only difference is location: 28 is the X15 connection, 29 is the X14 connection. In both cases check the cable, connectors, and shield on the named connector first.

### Can a swapped encoder channel pair cause F14?

A swapped A/A-bar, B/B-bar pair classically shows up as fault F08 speed monitoring rather than F14, because the drive sees rotation in the wrong direction and runs its controller into the limit. F14 is about the feedback link itself failing: bad cable, bad shield, communication errors, or a defective encoder.

### The motor was just replaced and now I get F14 sub-code 30 or F36. Why?

Sub-code 30 means the drive found an unknown encoder type at X14/X15, and F36 covers an incorrect encoder type set for the DIP11B absolute encoder card. Both say the configured encoder type no longer matches the hardware. Set the correct encoder type for the new motor's feedback device and confirm the option-card parameters (P100/P101, P700/P701) are valid for the fitted card.

## Sources

- Compact Operating Instructions - MOVIDRIVE MDX60B/61B, SEW-Eurodrive document 16920813, Section 6.2.3 Error list. Archived official PDF: https://web.archive.org/web/20130124101658/http://download.sew-eurodrive.com/download/pdf/16920813.pdf
- MOVITRAC B Operating Instructions, 2009-05, SEW-Eurodrive document 16810813, Section 7.2 List of faults (F-00 - F-113). Archived official PDF: https://web.archive.org/web/20210805131920/https://download.sew-eurodrive.com/download/pdf/16810813.pdf
- Operating Instructions - MOVIDRIVE MDX60B/61B Inverter, SEW-Eurodrive document 11696613 (manufacturer's canonical source; the SEW download portal was serving a maintenance page at the time of writing): https://download.sew-eurodrive.com/download/pdf/11696613.pdf
