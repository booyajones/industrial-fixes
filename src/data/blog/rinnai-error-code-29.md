---
title: "Rinnai Error Code 29 — System Communication Fault Fix"
author: "James Rutherford"
pubDatetime: 2026-04-26T18:15:00Z
modDatetime: 2026-04-26T18:15:00Z
slug: rinnai-error-code-29
featured: false
draft: false
tags:
  - rinnai
  - tankless
  - water-heater
  - error-codes
description: "Rinnai error code 29 indicates a system or communication fault on Rinnai tankless water heaters. Learn how to diagnose PCB failure, sensor faults, and wiring issues."
---

## Rinnai Error Code 29 — System / Communication Fault

**Rinnai Error Code 29** appears on Rinnai V-Series, RU-Series, and RUR-Series tankless water heaters and indicates a **system or communication fault** — specifically, the main PCB (printed circuit board) has detected an internal fault, a communication failure between the main board and a secondary board or remote controller, or a sensor reading that is outside plausible operating range.

Error Code 29 is a catch-all fault code that can point to several different root causes, which makes it one of the more challenging Rinnai error codes to diagnose.

---

## What Error Code 29 Means

On Rinnai tankless water heaters, the main PCB continuously monitors all sensors, internal communication buses, and sub-board signals. When it detects that something is communicating incorrectly — or not at all — it logs Error Code 29 and shuts down to prevent unsafe operation.

Unlike Error Code 11 (ignition failure) or Error Code 12 (flame loss), which point to a specific mechanical or combustion failure, Code 29 is electronic in nature. It typically means:

1. The main PCB itself has failed
2. A sensor has failed and is reporting impossible values
3. The wiring between the PCB and a sensor, sub-board, or remote controller has a fault
4. A Rinnai Remote Controller (MC-91-2 or similar) has lost communication with the unit

---

## Common Causes

- **Main PCB (control board) failure** — most common cause; the board's internal processor, memory, or communication IC has failed
- **Temperature sensor fault** — an NTC thermistor is reading an impossible value (far above or below its range), which the PCB interprets as a system-level fault
- **Communication failure with a remote controller** — the Rinnai wired remote (MC-91, MC-195U, or similar) has lost its communication link with the main unit
- **Wiring harness fault** — a connector has pulled out, a wire has broken internally (open circuit), or two wires have shorted together inside the unit due to heat or vibration
- **Power supply issue** — the unit's internal 12 VDC or 5 VDC power supply has failed, causing multiple subsystems to report communication faults simultaneously
- **Software/firmware corruption** — rare, but power surges or brownouts can corrupt the PCB firmware, causing spurious faults

---

## Step-by-Step Diagnosis {#step-by-step-fix}

### Step 1: Power cycle the unit

Turn the unit off at the power switch (or at the circuit breaker if no switch is accessible). Wait 60 seconds. Restore power. Attempt to run the unit. Some Code 29 faults are transient — caused by a momentary power glitch or communication timeout — and clear with a simple restart.

If Code 29 returns within seconds or within the first heating cycle, it is a persistent fault requiring further diagnosis.

### Step 2: Check the remote controller connection

If a Rinnai wired remote controller is installed:
1. Disconnect the two-wire remote controller cable from the main unit's remote terminals (marked "MC").
2. Power cycle the unit again without the remote connected.
3. If Code 29 clears without the remote connected, the fault is in the remote controller, its wiring, or its connection. Test the wiring continuity and, if OK, replace the remote controller.

If no remote controller is installed but Code 29 persists, proceed to Step 3.

### Step 3: Inspect all sensor wiring harnesses

With the unit powered off, open the front cover. Locate all sensor connectors on the main PCB and verify each one is firmly seated. Common sensors on Rinnai tankless units include:
- Inlet and outlet water temperature sensors
- Heat exchanger overheat sensor
- Combustion chamber sensor

Check each sensor connector for:
- Loose seating (push firmly until you feel it click)
- Corroded or green-tinted pins
- Damaged wiring (look for melting or cracking near heat sources)

### Step 4: Test the temperature sensors

Disconnect each NTC thermistor sensor connector from the PCB one at a time and measure resistance across the sensor terminals with a multimeter. At room temperature (70°F/21°C), healthy sensors typically read 10–12 kΩ. An open circuit (OL) or near-zero reading indicates a failed sensor.

Replace any failed sensor and test whether Code 29 clears.

### Step 5: Check supply voltage

Measure the AC supply voltage at the unit's power connection. It should be 120 VAC ±10% (108–132 VAC). A chronically low supply voltage can cause the PCB's internal power supplies to operate marginally, leading to communication errors.

If supply voltage is within spec, use a multimeter to check the PCB's internal DC supplies if accessible (consult the service manual for test points). A failed 12 VDC or 5 VDC rail explains widespread communication faults.

### Step 6: Replace the main PCB

If Steps 1–5 do not identify a fixable cause, the main PCB has failed. PCB replacement is the definitive fix for persistent Code 29 faults. Rinnai's service literature typically points to the PCB as the primary suspect when Code 29 is not cleared by sensor or remote controller replacement.

Order the correct PCB by model number — Rinnai's product line uses different board revisions across model years, and installing an incorrect board version can cause additional issues.

---

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Typical Cost | Where to Buy |
|------|-------------|-------------|
| Rinnai Main PCB / Control Board | $180–$400 | [Amazon](https://www.amazon.com/s?k=Rinnai+Main+PCB+%2F+Control+Board&tag=errorcodefixes-20) |
| NTC Temperature Sensor | $15–$35 | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-rinnai-error-code-29&tag=errorcodefixes-20) |
| Rinnai Remote Controller MC-91 | $80–$140 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-rinnai-error-code-29&k=Rinnai+remote+controller+MC-91+tankless&tag=errorcodefixes-20) |
| Remote Controller Wiring | $10–$25 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-rinnai-error-code-29&k=Rinnai+remote+controller+wiring+2+wire+cable&tag=errorcodefixes-20) |

---

## When to Call a Technician

Main PCB diagnosis and replacement involves working with the unit's internal wiring and live 120 VAC components. If you are not comfortable working with residential electrical systems, have a licensed plumber or HVAC technician perform the diagnosis. In many jurisdictions, service work on tankless gas appliances must be performed by a licensed technician.

Additionally, if Code 29 appeared after a lightning strike or power surge, have the unit fully evaluated — surges can damage multiple components simultaneously, and replacing only the PCB may leave hidden damage in place.

> **Pro tip:** Rinnai Code 29 faults that appear only when hot water demand is continuous for more than 10–15 minutes (but clear if you let the unit rest) often indicate an overheat sensor that is triggering from a marginal heat exchanger. Scale buildup inside the heat exchanger causes localized hot spots that trigger the overheat sensor, which the PCB interprets as a Code 29. Annual descaling with a tankless water heater flush kit can resolve or prevent this pattern.
