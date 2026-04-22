---
title: "Fluke Multimeter Error Codes — Guide"
description: "Fluke multimeter error codes and OL/display indicators: what each means and how to fix it."
pubDatetime: 2026-04-22T19:00:00Z
modDatetime: 2026-04-22T19:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - refrigeration
  - fluke
---

## Fluke Multimeter Error Codes — What They Mean

Fluke multimeters (87V, 117, 175, 179, 289 and other True-RMS models) display error indicators and codes when measurement conditions are outside normal parameters or when the meter detects a problem.

| Display | Meaning |
|---------|---------|
| OL | Overload — measured value exceeds range |
| FUSE | Input fuse blown |
| LO BATT | Battery low — replace before critical measurements |
| CAL | Calibration required |
| Err | Input error (wrong test lead position for selected function) |
| --- | Continuity mode with no connection detected |

[Jump to Fix](#fix)

## Most Common Fluke Display Issues and Fixes {#fix}

### OL — Overload
The measured value exceeds the currently selected range. On autoranging meters: the value genuinely exceeds the meter's maximum for that function. On manual range: switch to a higher range. OL on resistance = open circuit (no continuity).

### FUSE — Blown Input Fuse
The current measurement fuse has blown from excessive current through the mA or A input. Replace with the exact Fluke-specified fuse (check model manual — 11A 1000V or 440mA fuses are common). Never substitute with a higher-rated fuse.

### LO BATT
Replace the battery. Fluke meters use 9V alkaline or AA cells depending on model. Low battery causes measurement drift — don't trust readings until replaced.

### Err / Wrong Lead Position
The test leads are plugged into the wrong input jacks for the selected measurement function. Verify test lead positions match the measurement: V/Ω/Hz leads for voltage and resistance, A or mA leads for current only.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Fluke replacement fuse | Must match exact rating — see model manual |
| 9V or AA battery | Replace immediately when LO BATT appears |
| Test lead set | Replace if leads are damaged |

## When to Call a Pro

If OL appears on all functions with known-good connections and correct range, the input amplifier or ADC inside the meter may have failed. Fluke calibration services handle internal repair.
