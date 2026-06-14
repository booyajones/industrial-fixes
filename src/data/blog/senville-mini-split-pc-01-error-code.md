---
title: "Senville Mini Split PC 01 Error Code - Causes & Fix"
description: "PC 01 means abnormal voltage at the outdoor unit (over or under). Most common fix: power-cycle, check supply voltage & wiring."
pubDatetime: 2026-05-31T08:37:04Z
modDatetime: 2026-05-31T08:37:04Z
author: "James Rutherford"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - senville
money_part: "Reactor (PFC coil)"
most_likely_cause: "Incoming power outside rated range"
---

## Senville Mini Split PC 01 Error Code — What It Means

The PC 01 (also displayed as P1) error on Senville LETO and AURA series mini splits means the outdoor unit has detected abnormal supply voltage, either too high or too low, and has shut itself down to protect the electronics. Senville calls this "Outdoor Voltage Protection." The fault can be triggered by incoming power outside the unit's rated range, loose or damaged wiring, or a failed component in the outdoor unit's power electronics path (typically the reactor or outdoor control board).

[Jump to Fix](#fix)

## Common Causes

- **Incoming power outside rated range** Supply voltage does not match the nameplate specification (110V or 220V depending on your model), or the feed voltage is unstable due to utility fluctuations or undersized wiring.
- **Loose, damaged, or miswired conductors** Power feed or interconnect wiring between the disconnect, outdoor unit, and indoor unit has loose terminals, corroded connections, or incorrect installation.
- **Faulty reactor** The reactor (PFC coil) in the outdoor unit has failed or shows resistance far from the normal close-to-zero-ohms reading, causing the board to sense abnormal voltage.
- **Failed outdoor control board or IPM module** The outdoor PCB or IPM board itself has developed a fault that causes it to misread or fail to regulate supply voltage correctly.

## Step-by-Step Fix {#fix}

1. **Power-cycle the system:** turn off the unit at the disconnect or breaker, wait two full minutes, then restore power and restart to see if the fault clears.
2. **Verify supply voltage at the outdoor unit:** use a multimeter to measure incoming line voltage at the outdoor disconnect and compare it to the nameplate rating (110V or 220V). Voltage must be stable and within the manufacturer's acceptable range.
3. **Inspect all power and interconnect wiring:** with power off, check every terminal in the outdoor unit, indoor unit, and disconnect for tight connections, corrosion, or signs of arcing or damage.
4. **Test the reactor resistance:** disconnect power, locate the reactor (PFC coil) in the outdoor unit, and measure its resistance with a multimeter. Senville states it should read close to zero ohms. If the reading is significantly higher or open, replace the reactor.
5. **Check DC bus voltage at P and N terminals:** with the unit powered but in standby, measure DC voltage between the P and N terminals on the outdoor board. Depending on your model, a normal reading may be approximately 310V, 340V, or 380V DC. Unstable or absent voltage points to the IPM board or power-supply circuit.
6. **Replace the outdoor control board if the reactor is good:** if the reactor tests normal and wiring is secure but the error persists, Senville's troubleshooting flow directs you to replace the outdoor PCB.
7. **Consult the IPM module if voltage remains unstable:** if DC bus voltage at P and N fluctuates or is missing even after reactor and wiring checks, consider replacing the IPM board before the main outdoor PCB.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Reactor (PFC coil) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-senville-mini-split-pc-01-error-code&k=Reactor+%28PFC+coil%29&tag=errorcodefixes-20) \| Order by your outdoor unit model number. Normal resistance is close to 0 ohms. |
| Outdoor control board (outdoor PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-senville-mini-split-pc-01-error-code&k=Outdoor+control+board+%28outdoor+PCB%29&tag=errorcodefixes-20) \| Match the board part number printed on your existing PCB or use your unit's model and serial number. |
| IPM module board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-senville-mini-split-pc-01-error-code&k=IPM+module+board&tag=errorcodefixes-20) \| Required if DC bus voltage is unstable. Confirm compatibility with your outdoor unit model. |

## When to Call a Pro

PC 01 involves live high-voltage AC and DC circuits and requires multimeter work inside the outdoor unit. Senville recommends that all PC 01 diagnostics and repairs be performed by a certified HVAC contractor. If you are not comfortable working with line voltage, measuring DC bus rails, or replacing control boards and reactors, call a licensed technician. Misdiagnosis or incorrect wiring can damage expensive electronics or create a safety hazard.
