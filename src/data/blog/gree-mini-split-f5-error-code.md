---
title: "Gree Mini Split F5 Error Code - Causes & Fix"
description: "F5 means discharge temperature sensor fault. Most common fix: check connector, test sensor resistance, replace sensor if open or shorted."
pubDatetime: 2026-05-31T08:02:04Z
modDatetime: 2026-05-31T08:02:04Z
author: "Marcus Webb"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - gree
money_part: "Gree discharge temperature sensor"
---

## Gree Mini Split F5 Error Code — What It Means

The F5 error code on a Gree mini split indicates a discharge temperature sensor malfunction in the outdoor unit. This sensor monitors the temperature of the refrigerant leaving the compressor. Gree's official service documentation identifies F5 specifically as a compressor discharge sensor fault, meaning the control board has detected that the sensor is open, shorted, disconnected, or reading outside the expected range.

The discharge sensor is a thermistor mounted on the compressor discharge pipe. When it fails or loses connection, the system cannot safely monitor compressor operation and will shut down to prevent damage. The fault is electrical in nature rather than a refrigerant or mechanical problem.

[Jump to Fix](#fix)

## Common Causes

- **Sensor open or shorted** The thermistor itself has failed and no longer changes resistance with temperature, which is the most common electrical cause according to Gree service guidance.
- **Loose or disconnected connector** The plug at the sensor or control board has worked loose, corroded, or lost contact due to vibration or weather exposure.
- **Wiring damage between sensor and PCB** The harness has been pinched, chafed, or broken somewhere along its run, causing an open or intermittent short circuit.
- **Sensor resistance drift outside range** The thermistor still functions but reads implausibly high or low resistance for the actual temperature, triggering the fault logic.
- **Failed PCB sensor input circuit** If a known-good sensor still throws F5, the control board's sensor input circuitry has failed and the board requires repair or replacement.

## Step-by-Step Fix {#fix}

1. **Kill power at the breaker** and lockout, then remove the outdoor unit cover to access the compressor and control board.
2. **Locate the discharge temperature sensor** on the compressor discharge pipe (the hot gas line leaving the compressor) and inspect its connector for looseness, corrosion, or damaged pins.
3. **Disconnect the sensor plug** at the outdoor board and use a multimeter to measure resistance across the sensor terminals, checking for an open circuit (infinite resistance) or a dead short (zero resistance).
4. **Warm or cool the sensor body** gently with your hand or a heat gun while watching the meter, confirming that resistance changes smoothly with temperature rather than staying fixed or jumping erratically.
5. **Replace the discharge sensor** if it reads open, shorted, or does not track temperature, reconnecting the harness securely and checking that the new sensor is firmly seated against the pipe.
6. **Restore power and test** the system through a full cooling cycle, monitoring for the F5 code to clear and verifying stable operation.
7. **Inspect the outdoor PCB** if F5 persists after installing a known-good sensor and confirming all wiring is intact, as the board's sensor input circuit may need repair or replacement.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Gree discharge temperature sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-gree-mini-split-f5-error-code&k=Gree+discharge+temperature+sensor&tag=errorcodefixes-20) \| Match your outdoor model number, the thermistor that mounts on the compressor discharge pipe. |
| Sensor connector pigtail | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-gree-mini-split-f5-error-code&k=Sensor+connector+pigtail&tag=errorcodefixes-20) \| If the plug or wiring near the sensor is damaged and cannot be reliably repaired. |
| Outdoor unit control board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-gree-mini-split-f5-error-code&k=Outdoor+unit+control+board+%28PCB%29&tag=errorcodefixes-20) \| Required only if a verified good sensor still triggers F5, indicating a failed board input circuit. |

## When to Call a Pro

If you are not comfortable working with live electrical components or do not own a multimeter, call a licensed HVAC technician. Also call a pro if you replace the sensor and wiring but F5 returns, since board-level diagnosis and refrigerant-side inspection require gauges, recovery equipment, and EPA certification. Any work involving the refrigerant circuit or compressor replacement must be performed by a certified technician.
