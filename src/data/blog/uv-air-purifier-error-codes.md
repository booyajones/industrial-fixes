---
title: "UV Air Purifier Error Codes Guide — HVAC UV Systems"
description: "UV air purifier error codes for common HVAC UV systems including Honeywell UV, Fresh-Aire UV, Sanuvox, and Ultravation: fault codes, lamp failure indicators, and fixes."
pubDatetime: 2026-04-22T19:00:00Z
modDatetime: 2026-04-22T19:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - air-quality
  - uv
---

## UV Air Purifier Error Codes — Quick Reference

In-duct UV air purifiers use ultraviolet light to reduce microbial contaminants in HVAC airstreams. Major HVAC UV brands include Fresh-Aire UV, Sanuvox, Ultravation, Honeywell UV, and RGF. Most UV systems communicate status through LED indicators rather than numeric codes. The following covers the common fault patterns across brands.

| LED / Indicator State | Meaning | Action |
|----------------------|---------|--------|
| Green solid | Normal operation, lamp active | None |
| Green flashing | Lamp life warning (brand-specific) | Plan lamp replacement |
| Red / amber solid | Lamp end of life or lamp failure | Replace UV lamp |
| Red flashing | Power fault or ballast fault | Check 24VAC supply; inspect wiring |
| Off (no LED) | No power | Check power source; check fuse |
| Yellow flashing | Annual reminder (Honeywell UV) | Inspect lamp; reset timer |
| Alarm output active | Lamp failure relay triggered | Replace lamp; reset alarm |

## Brand-Specific Fault Indicators

### Fresh-Aire UV (APCO, TUV, BIO)
Fresh-Aire UV systems include a lamp life indicator. When the lamp ages past its rated life (typically 9,000 hours for standard lamps, 17,000 hours for extended-life lamps), the indicator turns from green to red. The lamp may still emit visible violet light but UV-C output decreases significantly with age — replace the lamp when indicated even if it still appears to glow.

**Reset procedure after lamp replacement:** Hold the reset button on the control module for 5 seconds until the LED returns to green.

### Sanuvox UV (Sanuvox R+, P+, Bio Wall)
Sanuvox systems use a photodiode sensor to actually measure UV output rather than just tracking runtime hours. When UV output drops below a threshold, the system activates its fault indicator. This is a more reliable method than timer-based systems. A red fault on a Sanuvox system means the lamp has truly degraded — not just that a timer has run out.

**Common Sanuvox fault cause:** Coil fouling. The Sanuvox coil irradiator is positioned to shine UV directly on the indoor coil. If the coil is heavily fouled with biofilm, the UV reflection off the coil changes and can affect the photodiode reading. Clean the coil first, then retest.

### Honeywell UV (UV-100, UV2400, UVBL)
Honeywell UV systems include a 12-month reminder light that flashes yellow at the one-year mark, regardless of lamp condition. This is a maintenance reminder — the lamp may still be functional. Test by checking that the lamp emits visible violet glow. Replace the lamp and reset the reminder timer.

### Ultravation UV (UVPhotoMax, Whisper Kleen)
Ultravation systems have an audible alarm (chirping) in addition to LED indicators when the lamp reaches end of life. The alarm is triggered by a runtime counter. Silence the alarm by replacing the lamp and pressing the reset button.

## UV Lamp Replacement — General Procedure

1. **Turn off the HVAC system** — do not touch UV lamps while the system is running
2. **UV lamps emit UV-C radiation** — do not look directly at the lamp and avoid skin exposure; use gloves
3. Remove the lamp by twisting counterclockwise (most single-pin lamps) or disconnecting the end caps (two-pin lamps)
4. Insert the new lamp — handle with a clean cloth or gloves; skin oils degrade quartz lamp envelopes
5. Reset the timer or lamp life counter per the brand's procedure
6. Verify the lamp illuminates (visible violet glow) within 60 seconds of system restart

## Lamp Life by Technology

| Lamp Type | Rated Life | Typical Brands |
|-----------|-----------|----------------|
| Standard UV-C (low pressure) | 9,000 hours (~1 year at 24/7) | Honeywell, Fresh-Aire standard |
| Extended-life UV-C | 17,000 hours (~2 years) | Fresh-Aire APCO, Sanuvox |
| Amalgam UV-C | 17,000+ hours | Sanuvox high-output systems |
| UV-C LED array | 25,000+ hours | REME Halo LED, newer systems |

## When to Call a Pro
If a UV system's fault indicator activates immediately after installing a new lamp, the ballast (electronic power supply) may have failed. Ballast replacement requires an HVAC technician familiar with the specific brand.
