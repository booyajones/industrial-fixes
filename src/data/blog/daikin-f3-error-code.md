---
title: "Daikin F3 Error Code — Causes & Fix"
description: "What Daikin F3 error code means, why the discharge temp sensor faults, and how to fix it step by step."
pubDatetime: 2026-04-22T12:00:00Z
modDatetime: 2026-04-22T12:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - mini-split
  - daikin
money_part: "Discharge temperature sensor (thermistor)"
---

## Daikin F3 Error Code — What It Means

The Daikin F3 error code indicates a **discharge temperature sensor (thermistor) fault** on the outdoor unit. The discharge sensor monitors compressor outlet temperature to protect the compressor from overheating. When the sensor reads out of its valid range — either an open circuit (disconnected/failed) or a short circuit (shorted thermistor) — the outdoor unit board logs F3 and stops compressor operation. The system will not resume heating or cooling until the sensor or its wiring is restored to normal range.

[Jump to Fix](#fix)

## Common Causes

- **Failed discharge thermistor** — Thermistors age and drift out of spec; an open or short reading means the sensor must be replaced.
- **Loose or corroded wiring connector** — The small JST or plug-in connector at the sensor or the outdoor board backs out over time, breaking the circuit.
- **Wiring harness damage** — Rodent chewing, UV degradation, or pinching by the sheet metal causes a break or short in the sensor wire.
- **Outdoor board thermistor input failure** — Rarely, the board's thermistor input circuit fails; the sensor tests fine but the board can't read it.

## Step-by-Step Fix {#fix}

1. **Locate the discharge sensor** — The discharge temperature sensor is clipped to the compressor discharge line (hot copper line exiting the compressor) inside the outdoor unit. It has a small probe and a 2-wire connector.
2. **Disconnect and measure resistance** — With power off and unit at ambient temperature, disconnect the sensor connector and measure resistance across the two sensor wires. Cross-reference the resistance value against the Daikin thermistor resistance/temperature table for your model (typically ~10–20 kΩ at 25°C).
3. **Inspect the connector and harness** — Check for corrosion, pushed-out pins, or damaged wire. Clean corroded contacts with electrical contact cleaner; reseat the connector firmly.
4. **Check for shorts** — Measure resistance between each sensor wire and ground. Should read open circuit (∞ Ω). Any reading indicates a shorted harness.
5. **Replace the sensor** — If resistance is out of spec, replace the discharge thermistor. Clip the new sensor to the same location on the discharge pipe and route the wire away from sharp edges.
6. **Power on and verify** — Restore power and confirm F3 is cleared. Run the system in cooling mode for 10 minutes and verify the outdoor unit operates normally.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Discharge temperature sensor (thermistor) | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-daikin-f3-error-code&tag=errorcodefixes-20) \| Must match Daikin model; resistance spec varies by series |
| Sensor harness wiring | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-f3-error-code&k=Sensor+harness+wiring&tag=errorcodefixes-20) \| If the harness is damaged; use equivalent gauge wire |
## When to Call a Pro

If the sensor and wiring test good but F3 persists, the outdoor unit PCB may have a failed thermistor input circuit. PCB replacement on Daikin outdoor units requires refrigerant system awareness and should be done by a certified HVAC technician.

## Related Articles

- [Daikin A3 Error Code — Causes & Fix](/posts/daikin-a3-error-code/)
- [Daikin Applied Chiller Fault Codes Guide — WMC / AGZ / ALZ Series](/posts/daikin-applied-fault-codes/)
- [Daikin C4 Error Code — Heat Exchanger Coil Sensor: Causes & Fix](/posts/daikin-c4-error-code/)
- [Daikin C9 Error Code — Compressor Discharge Temperature Sensor Fault](/posts/daikin-c9-error-code/)
- [Daikin E1 Error Code Fix — Indoor Sensor Fault](/posts/daikin-e1-error-code/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Mitsubishi mini split P5 drain fault](/posts/mitsubishi-p5-error-code/)

## See Also

- [Daikin Applied Chiller Fault Codes Guide — WMC / AGZ / ALZ Series](/posts/daikin-applied-fault-codes/)
- [Daikin RXYQ VRV System Error Codes — Complete Fault Code Guide](/posts/daikin-rxyq-error-codes/)
- [Daikin RXQ VRV System Error Codes (Outdoor Unit): Complete Guide](/posts/daikin-vrv-rxq-error-codes/)
- [Daikin L5 Error Code — Compressor Lock Fix](/posts/daikin-error-code-l5/)
