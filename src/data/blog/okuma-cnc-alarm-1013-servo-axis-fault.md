---
title: "Okuma CNC Alarm 1013 — Servo Axis Fault Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-03-15T08:00:00Z
modDatetime: 2024-03-15T08:00:00Z
slug: okuma-cnc-alarm-1013-servo-axis-fault
featured: false
draft: false
tags:
  - cnc
  - okuma
  - servo
  - alarm
description: "Okuma CNC alarm 1013 means servo amplifier thermal overload on OSP-P300 and P200 series controllers — here's how to diagnose and fix it."
---

## Error Code: Okuma CNC Alarm 1013

**What it means:** Alarm 1013 on Okuma CNC machines equipped with OSP-P300 or OSP-P200 series controllers indicates a servo amplifier thermal overload fault. The servo drive amplifier for one of the machine's axes has exceeded its thermal protection threshold and shut down to prevent damage to the output power transistors (IPM — Intelligent Power Module) inside the amplifier unit.

Alarm 1013 always includes an axis identifier in the full alarm text displayed on the OSP controller — for example "ALARM 1013 X-AXIS SERVO AMPLIFIER OVERLOAD" or "1013 Z SERVO OH." The axis name tells you which specific amplifier to investigate.

## Common Causes

- **Servo amplifier cooling fan failure** — The most common cause. Okuma servo amplifiers (Okuma's IGBT Drive units, or third-party Fanuc/Mitsubishi amplifiers on older machines) have integral cooling fans. When the fan fails, the amplifier overheats within 30–60 minutes of operation and trips the thermal sensor.
- **Blocked or restricted airflow in the electrical cabinet** — Cabinet filter mats that are clogged with dust, chips, or coolant mist restrict airflow across the amplifier heatsinks. On machines in heavy chip-producing environments, this is an extremely common maintenance miss.
- **Machine axis running under excessive load** — If the axis is fighting a mechanical issue (worn linear guideway, inadequate lubrication, damaged ballscrew, or external mechanical interference), the servo amplifier works harder, generates more heat, and exceeds the thermal limit.
- **Ambient temperature exceeding design limits** — Servo amplifiers in Okuma machines are typically rated for 0–45°C (32–113°F) ambient. In summer, small electrical rooms without air conditioning can exceed this range.
- **Amplifier internal component degradation** — Older electrolytic capacitors in the amplifier's power supply section dry out over time, reducing the DC bus capacitance and causing the amplifier to run hotter than designed.
- **Excessive duty cycle** — Applications with very high acceleration/deceleration rates and short cycle times can thermally saturate an amplifier that is correctly sized for continuous duty but undersized for the actual duty cycle.

## Step-by-Step Fix {#step-by-step-fix}

1. **Allow the machine to cool before inspection.** Power the machine off, open the electrical cabinet, and wait 20–30 minutes before touching any amplifier components. The IPM modules inside the amplifier can remain hot enough to cause burns for several minutes after shutdown.

2. **Locate the affected axis amplifier.** Okuma servo amplifiers are typically mounted in a rack inside the main electrical cabinet. Each amplifier is labeled by axis (X, Z, C, Y, etc.) on its front face or on the mounting rail label below it. Confirm you're looking at the right unit.

3. **Check the amplifier cooling fan.** Every Okuma servo amplifier has one or more integral fans on the rear or side of the unit that blow air across the heatsink. Power the machine on briefly (without running any programs) and immediately check whether the fan(s) on the alarmed amplifier are spinning. A fan that's not spinning or spinning slowly is the culprit. Fan replacement is typically inexpensive ($20–$60 for a standard 40mm or 60mm DC fan) and is accessible without full amplifier removal on most Okuma units.

4. **Inspect and clean the cabinet air filters.** Okuma electrical cabinets have filter mats on intake louvers, typically at the bottom or front of the cabinet door. Remove and clean or replace these filters. A severely clogged filter mat reduces airflow enough to cause overtemperature conditions even with good fans.

5. **Check the axis for mechanical resistance.** After cooling, perform a manual jog of the alarmed axis at a slow feedrate (10–50 mm/min) and observe the servo load meter in the OSP diagnostic screen. A healthy, well-lubricated axis should run at less than 30% servo load during slow jog. Load values above 60–70% during slow jogging indicate mechanical friction — inspect the linear guides for adequate lubrication, check for debris between the way covers, and verify the ballscrew is not binding.

6. **Verify lubrication system operation.** Okuma machines use automatic one-shot lubrication systems that deliver oil to the linear guideways and ballscrew nuts on a timed cycle. If the lube pump is empty, has a blocked line, or the timer has been incorrectly set, the ways run dry and servo load increases substantially. Check the oil reservoir level and listen for the pump cycle (typically every 20–60 minutes of operation).

7. **Check electrical cabinet ambient temperature.** If the machine is in a hot environment, verify that the cabinet air conditioning unit (most Okuma machines have a cabinet-mounted A/C unit) is running and cooling effectively. A failed cabinet A/C unit in summer can raise internal temperatures to 55°C+, well above the amplifier's design limit.

8. **Clear the alarm after addressing the root cause.** On OSP-P300/P200, press the RESET button once after the amplifier has cooled and the root cause has been resolved. If the alarm returns within the first heat cycle, the root cause was not fully resolved.

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Part Number | Typical Cost | Where to Buy |
|------|------------|-------------|-------------|
| Amplifier Cooling Fan (40mm or 60mm DC) | Match by voltage/CFM/frame | $20–$60 | [Amazon](https://www.amazon.com/s?k=Match+by+voltage%2FCFM%2Fframe+Amplifier+Cooling+Fan+%2840mm+or+60mm+DC%29&tag=errorcodefixes-20) \| Grainger / Amazon |
| Cabinet Air Filter Mat | Okuma part or cut-to-size foam | $10–$30 | [Amazon](https://www.amazon.com/s?k=Okuma+part+or+cut-to-size+foam+Cabinet+Air+Filter+Mat&tag=errorcodefixes-20) \| Okuma dealer / filter supply |
| Okuma IGBT Servo Amplifier (if failed) | Axis-specific, contact Okuma | $2,000–$6,000 | [Amazon](https://www.amazon.com/s?k=Axis-specific%2C+contact+Okuma+Okuma+IGBT+Servo+Amplifier+%28if+failed%29&tag=errorcodefixes-20) \| Okuma America dealer |
| One-Shot Lube Oil (ISO 68 way oil) | Generic ISO 68 | $15–$30/gallon | [Amazon](https://www.amazon.com/s?k=Generic+ISO+68+One-Shot+Lube+Oil+%28ISO+68+way+oil%29&tag=errorcodefixes-20) \| Grainger / MSC Industrial |
## When to Call a Professional

If the cooling fan is operational, the cabinet is clean, the axis moves freely under manual jog, and Alarm 1013 still returns within the first hour of operation after a cool-down reset, the amplifier's IPM module or internal power supply components are degraded and the unit needs repair or replacement. Okuma servo amplifier repair requires oscilloscope verification of the gate drive signals, capacitor ESR testing, and IPM testing — this is not field-serviceable without specialized equipment. Okuma America's service division and their regional distributors can provide factory-authorized repair. Always obtain the machine's parameter backup before any amplifier replacement to avoid re-commissioning from scratch.

> **Pro tip:** On Okuma machines with multiple servo axes, Alarm 1013 that always affects the same axis and always appears after approximately the same run time (e.g., 45 minutes) is almost always a failing amplifier cooling fan — not a load or lubrication issue. The fan's reduced airflow allows the heatsink to heat up on a predictable thermal time constant. Replacing the fan usually costs under $40 and 20 minutes of labor and avoids a $3,000+ amplifier replacement.
