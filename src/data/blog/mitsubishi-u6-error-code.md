---
title: "Mitsubishi U6 Error Code — Causes & Fix"
description: "What Mitsubishi mini-split U6 error code means, why the coil sensor faults, and how to fix it step by step."
pubDatetime: 2026-04-22T12:00:00Z
modDatetime: 2026-04-22T12:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - mini-split
  - mitsubishi
---

## Mitsubishi U6 Error Code — What It Means

The Mitsubishi U6 error code indicates a **coil temperature sensor (thermistor) fault** on the outdoor unit. Specifically, U6 points to the outdoor coil thermistor (also called the heat exchanger sensor), which monitors refrigerant temperature at the outdoor coil to regulate defrost cycles and protect system operation. When the sensor reads outside its valid resistance range — open or shorted — the outdoor unit board stores U6 and may shut down or limit operation. This is distinct from the discharge sensor (U1) or the ambient sensor.

[Jump to Fix](#fix)

## Common Causes

- **Failed outdoor coil thermistor** — Sensor resistance drifts out of spec due to age or heat cycling; open circuit is the most common failure.
- **Connector loosened by vibration** — The outdoor unit vibrates during compressor operation; thermistor connectors work loose over time.
- **Moisture intrusion into connector** — Water ingress in the connector causes corrosion, increasing resistance and causing the board to read the sensor as open.
- **PCB thermistor input circuit failure** — Rarely, the outdoor board's input for the coil sensor fails; sensor tests fine but the board still stores U6.

## Step-by-Step Fix {#fix}

1. **Locate the outdoor coil sensor** — Open the outdoor unit panel. The coil thermistor is a small probe clipped directly onto the outdoor heat exchanger fins or coil tubing, with a 2-wire lead running to the PCB.
2. **Inspect the connector** — Check the connector at both the sensor and the PCB for pushed-out pins, corrosion, or water. Clean with contact cleaner and reseat firmly.
3. **Measure sensor resistance** — With power off, disconnect the sensor and measure resistance. Compare against the Mitsubishi thermistor resistance chart (typically ~10–15 kΩ at 25°C). Out-of-range reading = replace sensor.
4. **Check for shorts to ground** — Measure from each sensor wire to the chassis ground. Any reading other than open circuit indicates a shorted harness.
5. **Replace the sensor if needed** — Clip the new sensor onto the same coil location. Secure the wire away from moving parts and sharp metal edges.
6. **Power on and verify** — Restore power, run in cooling mode for 10 minutes, and confirm U6 is cleared and the outdoor unit operates normally.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Outdoor coil thermistor | [Amazon](https://www.amazon.com/s?k=Outdoor+coil+thermistor&tag=errorcodefixes-20) \| Must match the Mitsubishi part number for your model; thermistor specs vary by series |
| Thermistor harness wire | [Amazon](https://www.amazon.com/s?k=Thermistor+harness+wire&tag=errorcodefixes-20) \| If the wire is damaged; use shielded wire of equivalent gauge |
## When to Call a Pro

If the sensor measures in-spec and connections are clean but U6 persists, the outdoor PCB has a failed input and requires replacement. Mitsubishi outdoor boards are model-specific; consult a Mitsubishi Diamond Contractor for PCB sourcing and programming verification.

## Related Articles

- [Mitsubishi City Multi P8 / E6 Error Codes — Causes & Fix](/posts/mitsubishi-city-multi-error-codes/)
- [Mitsubishi PEX City Multi Error Codes (Indoor Unit): Complete Guide](/posts/mitsubishi-city-multi-pex-error/)
- [Mitsubishi CNC Alarm 500 — Causes & Fix](/posts/mitsubishi-cnc-alarm-500/)
- [Mitsubishi CNC Alarm Y96 — Causes & Fix](/posts/mitsubishi-cnc-alarm-y96/)
- [Mitsubishi E1 Error Code — Indoor/Outdoor Communication Fault Fix](/posts/mitsubishi-e1-error-code/)
