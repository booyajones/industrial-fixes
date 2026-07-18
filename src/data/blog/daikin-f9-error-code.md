---
title: "Daikin F9 Error Code: Causes, Diagnosis & How to Fix It"
description: "Seeing a Daikin F9 error? Learn how to pull the exact fault code from the remote, check the indoor coil thermistor, and know when C4 or a pro repair is the real fix."
pubDatetime: 2026-04-22T16:00:00Z
modDatetime: 2026-04-22T16:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - daikin
money_part: "Indoor coil thermistor"
most_likely_cause: "Failed thermistor"
---

## Daikin F9 Error Code — What It Means

Daikin error code **F9** indicates a fault with the **indoor heat exchanger temperature sensor (thermistor)**. The sensor that monitors the indoor coil temperature for freeze protection and capacity control is reading outside the expected range. F9 appears on Daikin wall-mount, ceiling cassette, and floor-console indoor units.

[Jump to Fix](#fix)

On Daikin systems, F9 specifically refers to the **indoor heat exchanger midpoint thermistor** (also called the "liquid pipe thermistor" or "coil outlet thermistor"). This is separate from the room air temperature thermistor (which causes different codes).

## Common Causes

- **Failed thermistor** — After years of exposure to condensation and refrigerant temperatures (−5°F to 130°F cycling), the NTC thermistor resistance drifts out of spec. Complete failure shows as OL (open circuit) or 0 Ω (short circuit).
- **Loose or corroded connector** — The thermistor connects to the indoor PCB via a 2-pin plug. On Daikin indoor units, this connector is typically on the right side of the PCB. Vibration from fan operation loosens the connection.
- **Thermistor physically dislodged** — The sensor is held in the indoor coil fins by a clip. If the indoor unit was serviced, cleaned, or if the filter was replaced roughly, the thermistor clip may have been pulled off the coil. A thermistor hanging in air reads incorrect temperature.
- **Moisture on PCB** — Condensation in the indoor unit can reach the PCB and corrode the thermistor input circuit.

## Step-by-Step Fix {#fix}

1. **Remove the indoor unit front panel and filter** — on Daikin FTXS and FTXB series, the front panel lifts off the bottom edge and swings up. Remove the filters.
2. **Open the indoor unit chassis** — remove the bottom and side screws (typically 3–5 Phillips screws) to access the inside of the indoor unit.
3. **Locate the heat exchanger thermistor** — it's a small cylindrical sensor (about the size of a pencil eraser) clipped into the indoor coil. It has a 2-wire lead going to the PCB.
4. **Check the clip position** — verify the thermistor is seated in the coil fins, not hanging loose. Reseat it in the clip if it's dislodged.
5. **Test resistance** — unplug the connector from the PCB and measure resistance across the two sensor wires. At room temperature (~70°F / 21°C), a Daikin indoor coil thermistor typically reads 5–7 kΩ. Reading OL or 0 Ω means replacement.
6. **Re-seat the PCB connector** — if resistance is good, clean the PCB connector with contact cleaner and re-seat firmly.
7. **Restore power and test** — if F9 clears, the repair is complete. If it persists with a good thermistor and secure connector, the PCB sensor input may be damaged.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Indoor coil thermistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-f9-error-code&k=Indoor+coil+thermistor&tag=errorcodefixes-20) \| Daikin 1845004 or model-specific; verify pin count |
| Indoor PCB | [Amazon](https://www.amazon.com/s?k=Indoor+PCB&tag=errorcodefixes-20) \| Match to full model code; F9 from bad PCB is rare |
| Contact cleaner | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-f9-error-code&k=Contact+cleaner&tag=errorcodefixes-20) \| For connector maintenance |
## When to Call a Pro
If the thermistor and connector check out but F9 persists, the indoor PCB is likely the issue. PCB replacement is feasible for those comfortable with electronics, but sourcing the correct part number from the unit's model code is essential — Daikin has many PCB variants.

## Related Articles

- [Daikin A3 Error Code — Causes & Fix](/posts/daikin-a3-error-code/)
- [Daikin Applied Chiller Fault Codes Guide — WMC / AGZ / ALZ Series](/posts/daikin-applied-fault-codes/)
- [Daikin C4 Error Code — Heat Exchanger Coil Sensor: Causes & Fix](/posts/daikin-c4-error-code/)
- [Daikin C9 Error Code — Compressor Discharge Temperature Sensor Fault](/posts/daikin-c9-error-code/)
- [Daikin E1 Error Code Fix — Indoor Sensor Fault](/posts/daikin-e1-error-code/)

<!-- INTERNAL-LINK-AUTO -->
**Related:** [Rheem EcoNet A101 error code fix](/posts/rheem-econet-a101-error-code/)

## See Also

- [Daikin Applied Chiller Fault Codes Guide — WMC / AGZ / ALZ Series](/posts/daikin-applied-fault-codes/)
- [Daikin A3 Error Code — Causes & Fix](/posts/daikin-a3-error-code/)
- [Daikin VRV E7 Error Code — Causes & Fix](/posts/daikin-vrv-e7-error-code/)
- [Daikin UA Error Code — Mismatched Indoor/Outdoor Unit Fix](/posts/daikin-error-code-uA/)

## More Daikin F9 Error Code fault codes

Compiled from manufacturer service manuals and authorized documentation.

| Code | What it means | Likely cause | How to fix |
| --- | --- | --- | --- |
| F3 | Malfunction of discharge pipe temperature (discharge pipe temperature abnormally high) | Defective discharge pipe thermistor, genuinely high discharge temperature (often from low refrigerant charge or clogged/restricted piping), poor connector contact, or defective outdoor unit control PCB | Check refrigerant charge and for restrictions, inspect the discharge pipe thermistor and its connection, and replace the thermistor or PCB if faulty. Refrigerant work requires a licensed technician; do not keep resetting on this code. |
| F6 | Abnormal high pressure or refrigerant overcharged | Refrigerant overcharge, disconnection of the heat-exchanger (deicer), outdoor-air, or liquid-pipe thermistor, or defective outdoor unit PCB; dirty/blocked outdoor coil and a failing outdoor fan can also drive high pressure | Clean the outdoor coil, confirm the outdoor fan runs, verify the charge is correct, and check the thermistor connections and EXV. High-pressure and charge work is a technician job. |


## How to troubleshoot Daikin F9 Error Code

## How to diagnose a Daikin fault code the right way

**Read the exact code first.** Daikin residential and ductless units report faults as a two-character alphanumeric code (for example C4, C9, F3, F6, U0). On wall-mount units you retrieve it with the remote: aim at the unit and press the diagnostic button (often labeled Cancel/Timer Cancel), then cycle until the unit beeps a continuous tone to confirm the displayed code. On wired controllers the code shows directly on the screen. Write down the full code before ordering parts, because a mis-read digit points at the wrong component.

**Know the fault families.** Daikin groups codes by area: A-codes are indoor unit faults, C-codes are indoor sensor (thermistor) faults, E and H/F codes cover outdoor unit, compressor, and refrigerant-circuit protection, and U-codes cover communication and installation problems. The indoor heat-exchanger (liquid-pipe) thermistor abnormality is documented as **C4** and the room/suction-air thermistor as **C9** in Daikin service manuals, so if your unit is flagging a coil-temperature sensor problem, confirm which of those it is actually showing.

**Sensor faults follow a predictable pattern.** Most thermistor codes are caused, in rough order, by: a connector that vibrated loose or corroded at the indoor PCB, a sensor clip that got knocked off the coil during cleaning or a filter change, water intrusion onto the sensor head, and only then an actually-failed thermistor. Always inspect and reseat the connector and confirm the sensor is seated in the coil before condemning the part. A thermistor is an NTC device: unplug it and measure resistance, then compare against the temperature/resistance table for that model. An open circuit (OL) or dead short (0 ohms) confirms replacement.

**Safety and when to call a pro.** Kill power at the disconnect before opening any panel, and never probe the PCB with the unit energized. Retrieving the code and inspecting a connector is reasonable for a confident DIYer, but Daikin dealers generally treat opening the indoor chassis, replacing coil thermistors, and anything touching the sealed refrigerant circuit (F3, F6, high/low-pressure and charge faults) as technician work. If the sensor and its wiring test good and the code returns, the fault is on the PCB or in the refrigerant system, and that is the point to bring in a licensed tech rather than swapping parts blindly.


## Frequently asked questions

### How do I read the exact error code on my Daikin unit?

On a wall-mount unit, point the remote at the indoor unit and press the diagnostic button (usually the Cancel or Timer Cancel key), then step through the codes until you hear a long continuous beep, which confirms the active code. Wired controllers display the code on-screen. Note the full two-character code before troubleshooting.

### My Daikin is flagging an indoor coil temperature sensor. Which code is that?

On most Daikin mini-splits the indoor heat-exchanger (liquid-pipe) thermistor abnormality is reported as C4, and the room/suction-air thermistor as C9, per Daikin service manuals. If you are unsure what your unit is actually showing, pull the exact code from the remote before ordering a sensor, since the fix differs by component.

### What usually causes a Daikin thermistor fault code?

In practice it is most often a loose or corroded connector at the indoor PCB, or a sensor that was knocked out of its clip on the coil during cleaning or a filter change, before the thermistor itself has actually failed. Reseat and inspect the connection first, then measure the sensor's resistance and replace it only if it reads open or shorted.

### Can I fix a Daikin sensor fault myself?

Reading the code and inspecting or reseating the sensor connector is reasonable for a confident DIYer with the power isolated. Replacing a coil thermistor inside the indoor chassis, and any code tied to the refrigerant circuit such as F3 or F6, is generally technician work. If the sensor tests good but the code returns, the PCB or refrigerant system is the likely cause and a licensed tech should take over.

### How do I reset a Daikin error code?

Turn the unit off at the remote, then cut power at the breaker or disconnect for a few minutes before restoring it. If the code was a one-time glitch it will clear; if the underlying fault is still present, the code will return and the component needs to be diagnosed rather than just reset.

