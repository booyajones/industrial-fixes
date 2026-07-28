---
title: "Navien E037 Error Code - Causes & Fix"
description: "E037 is not a documented Navien error code. Likely misread as E035 (gas pressure), E036 (communication), or E039 (flow sensor)."
pubDatetime: 2026-06-30T10:05:40Z
modDatetime: 2026-06-30T10:05:40Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - water-heater
  - navien
money_part: "Gas Pressure Sensor (GPS)"
diy_or_pro: "pro"
free_checks:
  - "Verify the exact error code displayed; check if it is E035, E036, E039, or E030 instead of E037"
  - "Open and close the pressure relief valve to clear debris from the flow sensor (if code turns out to be E039)"
  - "Inspect all wiring harness connections between the PCB and sensors for looseness or corrosion"
---

## What this code means
E037 does not appear in Navien's official error code database for residential tankless water heaters. The manufacturer does not list E037 in any service manual, FAQ, or diagnostic guide. This strongly suggests the display was misread or the unit is a non-North American model with different firmware. The closest valid codes are E035 (abnormal gas pressure sensor), E036 (communication failure between PCB and dual venturi), and E039 (abnormal water flow sensor). Technicians should verify the exact code displayed and cross-reference the model's official documentation.

If the code is confirmed as E037, contact Navien technical support directly at 1-800-519-8794 for model-specific guidance. In most cases, re-reading the display or consulting the unit's wiring diagram will reveal one of the adjacent documented codes.

## Before You Replace Anything

Technicians sometimes replace the main PCB when E036 communication errors appear, but loose Ready-link cables or incorrect DIP switch settings are the actual cause. Check all cable seating and switch positions before ordering a board.

## Common Causes

- **Misread display (~50%)** The code is actually E035, E036, E039, or E030, and the technician or homeowner recorded it incorrectly.
- **Gas pressure sensor fault (if E035) (~20%)** The gas pressure sensor has failed, its wiring is loose, or gas supply pressure is outside the 4.5 to 10.5 inches of water column range for natural gas.
- **Communication failure (if E036) (~15%)** The PCB-to-dual venturi cable is loose, the DIP switch settings are incorrect, or one of the boards has failed.
- **Flow sensor obstruction (if E039) (~10%)** Debris prevents the water flow sensor impeller from spinning, or the inlet strainer is clogged.
- **Non-North American firmware (~5%)** The unit was imported or installed with firmware that uses a different error code set than Navien's U.S. or Canadian models.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the display clearly show E037, or could it be E035, E036, or E039?</summary>
<div class="dtree-body"><strong>Yes:</strong> Take a photo of the display and compare it to the error code list in your model's manual. If it matches E035, E036, or E039, follow the repair steps for that code.<br><strong>No:</strong> The code is confirmed as E037. Contact Navien technical support with your model and serial number to verify firmware version and code meaning.</div>
</details>

<details class="dtree"><summary>Does the unit produce hot water intermittently, or does it fail to ignite at all?</summary>
<div class="dtree-body"><strong>Yes:</strong> Intermittent operation suggests a flow sensor issue (E039) or gas pressure fluctuation (E035). Check the inlet filter and pressure relief valve first.<br><strong>No:</strong> Complete failure to ignite points to a communication or sensor fault (E036 or E035). Inspect all wiring harnesses and measure gas pressure.</div>
</details>

<details class="dtree"><summary>Has the unit been serviced recently or relocated?</summary>
<div class="dtree-body"><strong>Yes:</strong> Loose connections or incorrect DIP switch settings after service are common. Re-seat all cables and verify gas pressure meets the 4.5 to 10.5 inch specification.<br><strong>No:</strong> Component wear or debris accumulation is more likely. Flush the heat exchanger and check sensor continuity.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Photograph the display** and verify the exact error code shown. Compare it to your model's official error code list in the installation and operation manual.
2. **Power down the unit** at the circuit breaker and wait 60 seconds. Restore power and observe if the code reappears or changes to a documented code.
3. **Open the front cover** and inspect all wiring harnesses for loose connections, corrosion, or pinched wires. Re-seat every connector between the PCB and sensors.
4. **Measure incoming gas pressure** with a manometer if you have E035 symptoms. Natural gas should read 4.5 to 10.5 inches of water column under flow.
5. **Open and close the pressure relief valve** slowly to flush debris from the flow sensor and heat exchanger inlet if symptoms match E039.
6. **Check DIP switch settings** on the main PCB and dual venturi if communication failure (E036) is suspected. Consult the wiring diagram for your model's correct configuration.
7. **Contact Navien technical support** at 1-800-519-8794 with your model number, serial number, and photo of the display to confirm the code and obtain model-specific guidance.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Gas Pressure Sensor (GPS) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-navien-tankless-e037-error-code&k=Gas+Pressure+Sensor+%28GPS%29&tag=errorcodefixes-20) \| Required if E035 is confirmed and the sensor tests faulty or shows no continuity. |
| Water Flow Sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-navien-tankless-e037-error-code&k=Water+Flow+Sensor&tag=errorcodefixes-20) \| Needed if E039 is confirmed and the impeller does not spin after cleaning. |
| Main PCB or Dual Venturi Board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-navien-tankless-e037-error-code&k=Main+PCB+or+Dual+Venturi+Board&tag=errorcodefixes-20) \| Only replace after verifying all cables and DIP switches if E036 persists; expensive and often wrongly blamed. |

## When to Call a Pro

Call a licensed plumber or Navien-certified technician immediately. Since E037 is not a documented code, professional diagnosis is required to identify the actual fault. If the code turns out to be E035 or E036, the repair involves gas system measurement, electrical diagnostics, and PCB replacement, all of which require specialized tools and training. Attempting gas pressure adjustments or board swaps without proper equipment can create safety hazards or void the warranty. A qualified technician can also contact Navien's technical support line directly to obtain firmware-specific guidance and make sure any non-standard codes are interpreted correctly.

**Rough cost:** A pro service call runs about $150-400 depending on which valid code is confirmed.
