---
title: "Rheem Furnace 5 Flashes Error Code — Flame Sensor Fault Fix"
author: "Marcus Webb"
pubDatetime: 2024-03-15T08:00:00Z
modDatetime: 2024-03-15T08:00:00Z
slug: rheem-furnace-5-flashes-flame-sensor
featured: false
draft: false
tags:
  - hvac
  - rheem
  - furnace
  - flame-sensor
description: "Rheem furnace 5 flashes error code means a flame sensor fault — here's how to diagnose and fix it on Rheem, Ruud, and WeatherKing furnaces."
---

## Error Code: Rheem Furnace 5 Flashes

**What it means:** Five LED flashes on a Rheem, Ruud, or WeatherKing furnace indicate a flame sense fault. The control board attempted ignition, the burner lit, but the flame sensor failed to send a valid signal back to the board confirming stable flame. After two or three ignition attempts with no confirmed flame signal, the board locks out and blinks 5 times in a repeating sequence.

This is one of the most common furnace faults in the field. The flame sensor itself is usually the culprit — it's a $15–$25 part that corrodes over time — but don't replace it blindly. A cracked heat exchanger, gas pressure issue, or failed control board can produce the same lockout.

## Common Causes

- **Dirty or oxidized flame sensor rod** — The most common cause by far. A thin layer of oxidation on the sensor's stainless rod insulates it enough to drop the microamp signal below the board's 1–2 µA detection threshold.
- **Cracked or broken flame sensor** — Physical cracks in the ceramic insulator cause shorts to ground, killing the signal.
- **Weak gas pressure** — Low inlet or manifold gas pressure produces a small, unstable flame that doesn't fully engulf the sensor rod, causing intermittent detection.
- **Incorrect flame sensor position** — If the sensor rod is not sitting in the burner flame (bent, misaligned, or wrong replacement part), it will never read correctly.
- **Failed control board** — If a new sensor doesn't resolve the fault, the sensing circuit on the board itself may be defective.

## Step-by-Step Fix {#step-by-step-fix}

1. **Cut power to the furnace.** Turn the thermostat to OFF, then flip the furnace power switch or circuit breaker. Wait 60 seconds for capacitors to discharge before opening the access panel.

2. **Locate the flame sensor.** On most Rheem 80% and 90%+ units (Classic, Classic Plus, Prestige series), the flame sensor is a single rod mounted in a ceramic insulator at the left side of the burner assembly, directly in the path of the flame. It connects to the control board via a single orange or white wire with a push-on terminal.

3. **Disconnect the sensor wire and remove the sensor.** Use a 1/4" hex driver to remove the single mounting screw. Pull the sensor out carefully — the ceramic insulator is brittle.

4. **Inspect the sensor rod.** Look for a dull white, gray, or greenish coating on the stainless steel rod. That's oxidation. Also check the ceramic for cracks.

5. **Clean the rod with fine steel wool or emery cloth (#400 or finer).** Polish the rod until it's bright and shiny. Do NOT use sandpaper with a grit coarser than 400 — you'll scratch the rod and accelerate re-oxidation. Do NOT use spray cleaners or lubricants on the rod.

6. **Reinstall the sensor and restore power.** Reconnect the wire, reinstall the screw snugly (do not overtighten — you can crack the ceramic), and close the access panel. Restore power and cycle the thermostat through a heat call. Watch for normal ignition: inducer on → hot surface igniter glows → gas valve opens → burner lights → flame sensor confirms → blower starts.

7. **If the fault returns within one heating season:** Replace the sensor outright. The Rheem OEM replacement is part number **42-24195-01** (~$20). Verify the part number against your model's wiring diagram — some units use a different sensor geometry.

8. **Check gas pressure if a new sensor doesn't resolve the fault.** Connect a manometer to the manifold port. Rheem furnaces typically require 3.5" W.C. manifold pressure for natural gas. Low pressure = call the gas company or a licensed tech.

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Part Number | Typical Cost | Where to Buy |
|------|------------|-------------|---------------|
| Rheem OEM Flame Sensor | 42-24195-01 | $18–$25 | [Amazon](https://www.amazon.com/s?k=Rheem+OEM+Flame+Sensor&tag=errorcodefixes-20) \| [RepairClinic](https://www.repairclinic.com/Search/SearchResult?searchterm=42-24195-01&utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=rheem-furnace-5-flashes-flame-sensor) |
| Hot Surface Igniter (HSI) | SP10266 | $35–$45 | [Amazon](https://www.amazon.com/dp/B00BTLLJ40?ascsubtag=ecf-rheem-furnace-5-flashes-flame-sensor&tag=errorcodefixes-20) \| [RepairClinic](https://www.repairclinic.com/Search/SearchResult?searchterm=SP10266&utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=rheem-furnace-5-flashes-flame-sensor) |
| Rheem Control Board (if board is bad) | 62-24268-82 | $150–$220 | [Amazon](https://www.amazon.com/s?k=Rheem+Control+Board+%28if+board+is+bad%29&tag=errorcodefixes-20) \| [RepairClinic](https://www.repairclinic.com/Search/SearchResult?searchterm=62-24268-82&utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=rheem-furnace-5-flashes-flame-sensor) |

## When to Call a Professional

If you've cleaned or replaced the flame sensor and the 5-flash lockout persists, you're dealing with either a gas pressure problem, a cracked heat exchanger, or a failed control board — none of which are safe or simple DIY repairs. A cracked heat exchanger is a carbon monoxide hazard and requires immediate shutdown of the unit. A licensed HVAC technician can measure microamp output at the sensor terminal (should read 2–6 µA on a healthy Rheem system), verify gas pressure at manifold, and perform a combustion analysis. Don't run the furnace in lockout-reset cycles while troubleshooting — repeated ignition attempts without resolution can damage the igniter.

> **Pro tip:** Before ordering a replacement flame sensor, measure the microamp signal with a multimeter set to DC microamps in series with the sensor wire. A reading below 1.5 µA confirms a bad sensor. A reading of 0 µA often means a broken wire or cracked ceramic. A reading above 1.5 µA but still faulting usually points to the control board's sense circuit — save yourself a wasted parts order.
