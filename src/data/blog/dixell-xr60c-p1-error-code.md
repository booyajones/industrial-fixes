---
title: "Dixell XR60C P1 Error Code Fix — Sensor Fault"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-03-13T08:00:00Z
modDatetime: 2024-03-13T08:00:00Z
slug: dixell-xr60c-p1-error-code
featured: false
draft: false
tags:
  - refrigeration
  - dixell
  - controller
  - sensor
  - commercial
description: "Dixell XR60C P1 error code means probe 1 (the main temperature sensor) has failed or is disconnected. This guide covers sensor testing, replacement, and controller setup."
---

## Error Code: Dixell XR60C P1

**What it means:** P1 on the Dixell XR60C electronic controller indicates a fault with Probe 1 — the main temperature control sensor. The XR60C is a widely used commercial refrigeration controller found in walk-in coolers, reach-in cases, and refrigerated display cases from brands including True, Beverage-Air, Hussmann, and others. When it displays P1, the controller has detected that the probe is open-circuit, short-circuit, or reading a temperature outside the sensor's rated range.

When P1 is active, the controller typically switches the compressor and fans to a default safety state (either continuously on or off, depending on configuration) — it cannot regulate temperature without a valid sensor reading.

## Common Causes

- **Failed NTC probe** — The NTC (negative temperature coefficient) thermistor element inside the probe has failed. Probes in cold, wet environments fail from moisture intrusion, corrosion, or physical damage.
- **Disconnected probe wiring** — The probe lead pulled out of the controller terminal, or the connector at the probe end came loose. Common in cases with heavy door traffic that stresses the wire.
- **Probe wire damaged** — Rodents chewing on probe wire, wire caught in a door gasket, or a wire nicked against a sharp metal edge can break the conductor without obvious external damage.
- **Probe frozen in ice** — If the probe is located in a reach-in freezer and defrost hasn't been running, the probe can become encased in ice that stresses or breaks the wire or probe body.
- **Wrong probe type installed as replacement** — The XR60C uses an NTC 10kΩ at 25°C probe. Installing an NTC 5kΩ or PTC probe as a replacement will produce an out-of-range reading and trigger P1.
- **Controller input failure** — Rarely, the analog input circuit on the controller itself fails. If a confirmed working probe plugged in still shows P1, the controller is suspect.

## Step-by-Step Fix {#step-by-step-fix}

1. **Locate Probe 1.** On the XR60C, Probe 1 is connected to terminals 10 and 11 (probe input, marked P1 on the controller). Trace the wire from those terminals to the probe tip, which is typically clipped to the evaporator coil or mounted in the return air stream.

2. **Inspect the probe and wiring visually.** Check the full length of the probe wire for cuts, kinks, or pinch points. Check the probe tip for ice buildup, physical damage, or corrosion. Check that the wire ends are firmly seated in terminals 10 and 11.

3. **Disconnect the probe from the controller and measure resistance.** With a multimeter set to Ohms, measure resistance across the two probe leads. An NTC 10kΩ probe in a 35°F (2°C) refrigerator should read approximately 20,000–25,000 Ω. In a 0°F (-18°C) freezer, expect approximately 80,000–100,000 Ω. A reading of OL (open circuit) means the probe wire or element is broken. A reading of 0 Ω means a short. Either confirms a failed probe.

4. **Test with a known-good substitute.** If you have a spare NTC 10kΩ probe or a resistor of known value (e.g., 10kΩ = approximately 77°F / 25°C), connect it to terminals 10 and 11 in place of the probe. If P1 clears and the controller shows a temperature reading, the original probe is confirmed bad and the controller input is confirmed good.

5. **Replace the probe.** Order the correct NTC 10kΩ probe for the XR60C (Dixell part or compatible aftermarket). Route and secure the new probe to the same location as the original. Ensure the probe tip is making good thermal contact with the air stream or coil surface.

6. **After replacement, verify setpoints.** The XR60C can lose parameter settings if the controller has been power-cycled repeatedly during the fault. Navigate to the SET menu and confirm: St (set point) = your target temp, LS (minimum set) and US (maximum set) = appropriate limits for your application, and P2 function if you have a second probe installed (defrost termination, condenser monitoring, etc.).

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Where to Buy | Typical Cost | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------ |-------------|-------------|
| NTC 10kΩ replacement probe (universal, 6 ft lead) | [Grainger, Amazon, Parts Town](https://www.amazon.com/s?k=Grainger%2C%20Amazon%2C%20Parts%20Town&tag=errorcodefixe-20) | $12–$30 |
| [Dixell XR60C replacement controller](https://www.amazon.com/s?k=Dixell%20XR60C%20replacement%20controller&tag=errorcodefixe-20) | Parts Town, Restaurant Equipment World | $60–$120 | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Probe mounting clip | Parts Town, HVAC distributor | $2–$8 |

## When to Call a Professional

If a confirmed good probe still produces P1 on the controller, the XR60C input circuit has failed and the controller needs replacement. The XR60C is not field-repairable at the board level — replace the unit. When replacing the controller, photograph all existing parameters before removing the old unit, then re-enter them exactly on the new one. Incorrect parameters on a replacement controller can cause the case to freeze product (if defrost timing is wrong) or fail to cool (if the set point migrated). Tell your refrigeration tech: "XR60C showing P1, I tested with a known good probe and P1 persists. I need a controller swap and parameter verification."

> **Pro tip:** The Dixell XR60C has a built-in alarm relay output. If your refrigeration case has a remote alarm panel or BMS connection, that relay will trip on P1. Before calling a tech, confirm the P1 alarm is actually on the XR60C display — not just an alarm panel showing "case alarm." The alarm panel doesn't tell you which controller or which probe failed on multi-case installations.
