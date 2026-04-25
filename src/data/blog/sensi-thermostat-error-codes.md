---
title: "Emerson Sensi Thermostat Error Codes — Complete Guide"
description: "Emerson Sensi thermostat error codes explained: E1 through E9, Wi-Fi connection issues, and offline alerts. Fix common Sensi errors fast."
pubDatetime: 2026-04-22T18:00:00Z
modDatetime: 2026-04-22T18:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - sensi
  - emerson
  - thermostat
  - hvac
  - error-code
---

## Emerson Sensi Thermostat Error Codes

Emerson Sensi thermostats (ST55U, ST75U, UP500W, and 1T) use a combination of display codes and app alerts. Unlike traditional thermostats, many Sensi faults appear in the **Sensi app** rather than on the thermostat display itself.

## Sensi Error Codes — Quick Reference

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixes-20) | Meaning | Fix |
|---|---|---|
| E1 | Indoor temperature sensor fault | Replace thermostat |
| E2 | Outdoor/remote sensor fault | Check/replace remote sensor probe |
| E3 | Communication timeout | Check Wi-Fi, restart thermostat |
| E4 | Internal memory error | Factory reset |
| E5 | Wiring configuration error | Check wiring, re-run setup |
| E6 | Equipment protection delay | Wait 5 min (compressor protection) |
| E7 | Low voltage on HVAC wiring | Check transformer output |
| E8 | Short cycle protection active | Wait, then investigate HVAC fault |
| E9 | Over-temperature protection | Check for extreme ambient conditions |

## Most Common Sensi Issues

### "Offline" in the Sensi App (No Display Code)

The Sensi app shows the thermostat as "offline" or "unavailable." This is a Wi-Fi connectivity issue, not an HVAC fault.

**Fixes:**
1. Check that your 2.4GHz Wi-Fi network is active (Sensi uses 2.4GHz only, not 5GHz)
2. Move your router/access point closer if signal is weak (Sensi needs -70 dBm or better)
3. Restart the Sensi thermostat: press the small reset button on the side or disconnect and reconnect the wiring
4. Delete and re-add the thermostat in the app
5. Check if your router is blocking MAC addresses or has device limits reached

### E6 — Equipment Protection Delay

E6 is not a fault — it's the compressor short-cycle protection timer. After a power outage or thermostat restart, the Sensi waits 5 minutes before allowing the compressor to start. This prevents compressor damage from rapid restart.

**What to do:** Wait 5 minutes. The thermostat will start the equipment automatically. If you see E6 repeatedly, the system is short-cycling — check for other HVAC issues.

### E5 — Wiring Configuration Error

E5 appears during initial setup if the Sensi detects an unexpected wiring configuration. Common causes:
- Wire in the wrong terminal
- O/B terminal not set correctly (heat pump direction)
- System type mismatch (conventional vs. heat pump setting)

**Fix:** In the Sensi app, go to Equipment Setup and re-run the configuration wizard. Verify that the system type (conventional, heat pump, boiler) matches your actual HVAC equipment.

### E7 — Low Voltage

E7 means the Sensi is measuring low 24VAC from your HVAC system. Normal is 24–28VAC. Under 22VAC, the thermostat can't operate reliably.

**Fix:**
1. Check furnace/air handler power
2. Measure voltage at the R and C terminals with a multimeter
3. If below 22V, the transformer may be failing or overloaded with too many accessories

## Sensi App Alerts (Not Display Codes)

| [App Alert](https://www.amazon.com/s?k=App+Alert&tag=errorcodefixes-20) | Meaning |
|---|---|
| ["Short cycling detected"](https://www.amazon.com/s?k=%22Short+cycling+detected%22&tag=errorcodefixes-20) | Equipment running briefly and stopping repeatedly |
| ["Hasn't reached setpoint"](https://www.amazon.com/s?k=%22Hasn%27t+reached+setpoint%22&tag=errorcodefixes-20) | System running too long, not hitting target temp |
| ["Low battery" (Sensi Lite)](https://www.amazon.com/s?k=%22Low+battery%22+%28Sensi+Lite%29&tag=errorcodefixes-20) | Replace AA batteries |
| ["Filter reminder"](https://www.amazon.com/s?k=%22Filter+reminder%22&tag=errorcodefixes-20) | Time-based alert, not a fault |

## Factory Reset — Sensi

If you need to fully reset and re-pair the Sensi thermostat:
1. In the Sensi app: Settings → (thermostat name) → Remove Device
2. On the thermostat: hold the Sensi logo or reset pinhole (varies by model) for 10 seconds until display clears
3. Re-add in the app: Add Device → Sensi → follow pairing instructions

## Sensi Wi-Fi Thermostat Model Numbers

| [Model](https://www.amazon.com/s?k=Model&tag=errorcodefixes-20) | Notes |
|---|---|
| [ST55U](https://www.amazon.com/s?k=ST55U&tag=errorcodefixes-20) | Basic Wi-Fi, 7-day |
| [ST75U](https://www.amazon.com/s?k=ST75U&tag=errorcodefixes-20) | Smart features, Alexa/Google |
| 1T | Touchscreen, humidity display |
| [UP500W](https://www.amazon.com/s?k=UP500W&tag=errorcodefixes-20) | Universal, works with all HVAC types |
