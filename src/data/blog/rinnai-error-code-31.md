---
title: "Rinnai Error Code 31 — Causes & Fix"
description: "What Rinnai error code 31 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T09:00:00Z
modDatetime: 2026-04-22T09:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - boiler
  - rinnai
money_part: "Combustion chamber / burner temperature sensor"
---

## Rinnai Error Code 31 — What It Means

Rinnai error code 31 indicates a burner sensor (combustion chamber sensor or heat exchanger outlet temperature sensor) fault. The sensor is reading a temperature outside the valid operating range — either excessively high, below the ambient-realistic minimum, or a full open/short circuit. Rinnai uses this sensor to modulate the gas valve and protect the heat exchanger from overheat. When the sensor reading is implausible, the unit shuts down to prevent uncontrolled operation. Error 31 is common on older units where sensor leads become brittle and cracked.

[Jump to Fix](#fix)

## Common Causes

- **Failed temperature sensor (open circuit)** — The NTC thermistor element inside the sensor degrades and the resistance drifts far outside the normal temperature-resistance curve. Open circuit is the most common failure mode.
- **Damaged sensor lead wire** — The sensor wires run through the hot combustion area and become brittle over years of thermal cycling. Hairline cracks in the insulation or conductor create intermittent or permanent open circuits.
- **Loose connector at PCB** — The sensor connector can work loose over time, creating a high-resistance connection the board reads as an extreme temperature value.
- **Scale buildup causing actual overheat** — In hard water installations, calcium scale on the heat exchanger prevents heat transfer to water, causing the actual heat exchanger wall temperature to spike and the sensor to read a genuine over-temperature condition.

## Step-by-Step Fix {#fix}

1. **Identify the burner sensor location** — Open the Rinnai service panel. The combustion chamber sensor is typically a small probe mounted on a bracket inside or near the combustion chamber. Trace the wire to identify it against the schematic.
2. **Test sensor resistance at room temperature** — Unplug the sensor connector and measure resistance across the two sensor leads. At 77°F (25°C), a typical Rinnai NTC sensor reads approximately 10 kΩ. Cross-reference with the temperature-resistance table in the service manual.
3. **Inspect wire and connector** — Trace the sensor wire from the probe to the PCB connector. Look for cracked insulation, burn marks, or abraded areas. Check the connector for corrosion or pushed-back pins.
4. **Check for scale on heat exchanger** — If resistance is within spec, the unit may be logging 31 due to genuine overheat from scale. Perform a descaling procedure with citric acid solution per Rinnai's service procedure.
5. **Replace sensor and test** — Install the OEM replacement sensor, route the wire away from hot surfaces, and plug in the connector. Run several heat cycles and confirm code 31 does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Combustion chamber / burner temperature sensor | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-rinnai-error-code-31&tag=errorcodefixes-20) \| Must match Rinnai model number — resistance curves vary |
| Descaling solution (citric acid) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-rinnai-error-code-31&k=Descaling+solution+%28citric+acid%29&tag=errorcodefixes-20) \| Use if scale is contributing to genuine overheat events |
| PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-rinnai-error-code-31&k=PCB&tag=errorcodefixes-20) \| Replace only if sensor input channel is confirmed defective |
## When to Call a Pro

If the sensor replacement clears the error but it returns after a few cycles, the heat exchanger may have significant scale buildup causing repeated overheat trips. A licensed technician can perform a full flush and combustion analysis to confirm the heat exchanger is functioning correctly.

## Related Articles

- [Rinnai CBU Combi Boiler Error Codes — Complete Fault Guide](/posts/rinnai-cbu-error-codes/)
- [Rinnai Error Code 11 No Ignition — Causes & Fix](/posts/rinnai-error-code-11-ignition/)
- [Rinnai Error Code 11 — No Ignition Fix](/posts/rinnai-error-code-11/)
- [Rinnai Error Code 12 — Causes & Fix](/posts/rinnai-error-code-12/)
- [Rinnai Error Code 14 — Causes & Fix](/posts/rinnai-error-code-14/)

## See Also

- [Rinnai Error Code 61 — Causes & Fix](/posts/rinnai-error-code-61/)
- [Rinnai Error Code 33 — Causes & Fix](/posts/rinnai-error-code-33/)
- [Rinnai Error Code 25 — Causes & Fix](/posts/rinnai-error-code-25/)
- [Rinnai Error Code 11 — No Ignition Fix](/posts/rinnai-error-code-11/)
