---
title: "Lennox Error Code 412 — Inducer Motor Fault (Detailed Guide)"
description: "Lennox error code 412 inducer motor fault: detailed diagnosis, step-by-step testing, replacement tips, and fixes for Lennox SLP98, EL296, and compatible furnaces."
pubDatetime: 2026-04-22T19:00:00Z
modDatetime: 2026-04-22T19:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - lennox
  - furnace
---

## Lennox Error Code 412 — What It Means

Lennox error code **412** specifically identifies an **inducer motor fault** — meaning the furnace control board detected that the inducer motor (draft inducer / combustion air blower) failed to start, stalled during operation, or the RPM feedback signal was lost. Code 412 appears on Lennox iComfort-equipped and SureLight control board furnaces including the SLP98V, EL296V, ML296V, and XC21 platform furnaces.

On Lennox furnaces, error codes are read from the iComfort thermostat diagnostic screen or from the control board's LED blink sequence: code 412 = 4 blinks, pause, 1 blink, pause, 2 blinks.

## Why Code 412 Is Different from Code 411

Lennox uses separate codes to distinguish between:
- **Code 411** — Pressure switch fault (inducer running but pressure switch didn't close)
- **Code 412** — Inducer motor fault (motor itself isn't operating correctly)

Always confirm which code is active before starting diagnosis.

## Causes of Code 412

| Cause | Likelihood | Test Method |
|-------|-----------|------------|
| [Failed inducer motor](https://www.amazon.com/dp/B00FDZ90B2?tag=errorcodefixes-20) | High | Verify 115VAC at motor; check for spin |
| [Failed inducer motor capacitor](https://www.amazon.com/dp/B01M05L7B3?tag=errorcodefixes-20) | High | Capacitor meter — compare to rated value |
| [Seized inducer wheel bearing](https://www.amazon.com/s?k=Seized+inducer+wheel+bearing&tag=errorcodefixes-20) | Medium | Hand-spin test with power off |
| [Control board not sending 115VAC to motor](https://www.amazon.com/dp/B0CNZGZ1HS?tag=errorcodefixes-20) | Medium | Measure voltage at motor terminals |
| [Failed RPM feedback circuit](https://www.amazon.com/s?k=Failed+RPM+feedback+circuit&tag=errorcodefixes-20) | Medium | Inspect tachometer wire; measure signal |
| [Inducer wheel clogged with debris](https://www.amazon.com/s?k=Inducer+wheel+clogged+with+debris&tag=errorcodefixes-20) | Lower | Visual inspection; clean wheel |

## Step-by-Step Diagnosis

**Step 1: Verify the motor is the fault source**
Turn power off. Try to spin the inducer wheel by hand through the inducer inlet. It should rotate freely with slight magnetic resistance. If the shaft is seized or extremely difficult to turn, the motor bearings have failed. Replace the inducer motor assembly.

**Step 2: Check capacitor**
Most Lennox inducer motors use a run capacitor (typically 4–8 µF). Test with a capacitor meter. Replace if the reading is more than 10% below the stamped rating. A failed capacitor is the most common cause of code 412 on motors under 10 years old.

**Step 3: Measure voltage at motor terminals**
With the furnace calling for heat, measure 115VAC at the inducer motor's power terminals after the startup sequence initiates (you typically have about 30 seconds before the board locks out). If no voltage is present with the board powered and past the initial startup delay, the control board output for the inducer may have failed.

**Step 4: Check RPM feedback**
Lennox SLP98 and variable-speed furnaces use a tachometer signal from the inducer motor to confirm it reached operating speed. Inspect the small multi-pin connector between the inducer motor and the control board. A single damaged wire in this connector can cause code 412 even when the motor is physically running.

**Step 5: Inspect the inducer wheel**
With power off, remove the inducer inlet screen or housing cover and visually inspect the wheel blades. Heavy lint and debris accumulation on the blades reduces motor speed and can cause overheating. Clean the wheel with a brush or compressed air.

## Inducer Motor Replacement Notes

- Lennox inducer motors are model-specific — record the furnace model number and the motor's existing part number before ordering
- Common Lennox inducer parts: 60M49 (LB-60049M), 26B23 series for SLP98 models
- After installation, verify the inducer wheel is centered on the motor shaft and the housing seal is intact
- Clear the fault code from the iComfort thermostat after repair: Settings → Advanced → Diagnostics → Clear Faults

## When to Call a Pro
RPM feedback circuit issues and control board diagnosis require an HVAC technician with Lennox service training. If the motor tests good but the board continues to report 412, a Lennox-certified tech can use iComfort diagnostic tools to read raw motor RPM data.

## Related Articles

- [Lennox Error Code 292 — Ignition Failure Fix](/posts/lennox-292-error-code/)
- [Lennox EL296V Error Codes — Variable-Speed Furnace Diagnostic Guide](/posts/lennox-el296v-error-codes/)
- [Lennox Elite Series Furnace Error Codes — Fault Code Diagnostic Guide](/posts/lennox-elite-series-furnace-codes/)
- [Lennox 103 Error Code — Causes & Fix](/posts/lennox-error-code-103/)
- [Lennox Error Code 111 — Causes & Fix](/posts/lennox-error-code-111/)
