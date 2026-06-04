---
title: "Gree HC Error Code - Causes & Fix"
description: "HC means PFC protection fault in the outdoor unit inverter power circuit. Most often caused by low voltage or failed capacitors."
pubDatetime: 2026-05-31T08:04:58Z
modDatetime: 2026-05-31T08:04:58Z
author: "James Rutherford"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - gree
---

## Gree HC Error Code — What It Means

HC on Gree mini-split systems stands for PFC Protection, indicating a fault in the power factor correction circuit inside the outdoor unit. The inverter control board has detected that the DC bus or PFC stage is not building or regulating voltage correctly, so it trips protection to prevent damage. This is not a sensor issue but a real power-stage fault in the outdoor unit's electronic control board and associated circuitry.

[Jump to Fix](#fix)

## Common Causes

- **Low or unstable supply voltage** Mains power feeding the outdoor unit is below specification or fluctuating, preventing the PFC circuit from operating normally.
- **Failed diode bridge or rectifier** One or more diodes in the AC-to-DC rectifier stage on the outdoor PCB are open or shorted, blocking proper DC voltage generation.
- **Weak or bulged electrolytic capacitors** PFC or DC bus capacitors have lost capacitance or failed outright, causing unstable voltage or no output at all.
- **Damaged PFC reactor or inductor** The line filter or PFC reactor coil is open, shorted, or has high resistance due to heat or vibration damage.
- **Failed IPM or inverter module** The intelligent power module or related drive circuitry is shorted or degraded, pulling down the power stage and triggering protection.
- **Transient power disturbance** A momentary voltage spike or brownout caused a false trip, and the error may clear after a full power reset.

## Step-by-Step Fix {#fix}

1. **Turn off power at the breaker**, wait 60 seconds, restore power, and observe whether the HC code returns after a full power cycle to rule out a transient trip.
2. **Measure the supply voltage** at the outdoor unit terminals with a multimeter while the unit is powered to confirm it is stable and within the rated range for your model.
3. **Remove the outdoor unit cover** and inspect the main PCB for bulged or leaking capacitors, burned traces, cracked solder joints, or discolored components.
4. **Test the diode bridge** with your multimeter in diode mode by checking each diode for proper one-way conduction in the forward direction and high resistance in reverse.
5. **Check the DC bus capacitors** for visible swelling or, if you have an ESR meter, measure capacitance to confirm they have not degraded below rating.
6. **Check the PFC reactor or inductor** for continuity and normal low resistance using your ohmmeter, and inspect its connections and solder joints for damage or looseness.
7. **Measure the DC voltage** at the output of the rectifier stage with AC power applied (220 V AC input should yield approximately 300 V DC) only if upstream components test good and you are qualified to work on live high-voltage circuits.
8. **Replace the outdoor PCB, diode bridge, capacitors, or IPM** as indicated by your test results, or call a qualified technician if you are not comfortable diagnosing high-voltage inverter circuitry.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Outdoor unit main control board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-gree-mini-split-hc-error-code&k=Outdoor+unit+main+control+board+%28PCB%29&tag=errorcodefixes-20) \| Match the exact board part number printed on your existing PCB or consult Gree service documentation for your model. |
| Electrolytic capacitor set (PFC / DC bus) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-gree-mini-split-hc-error-code&k=Electrolytic+capacitor+set+%28PFC+%2F+DC+bus%29&tag=errorcodefixes-20) \| Verify voltage and capacitance ratings match the original parts before soldering replacements onto the board. |
| IPM (Intelligent Power Module) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-gree-mini-split-hc-error-code&k=IPM+%28Intelligent+Power+Module%29&tag=errorcodefixes-20) \| Only replace if upstream rectifier and capacitor tests are normal and the module tests shorted or abnormal. |

## When to Call a Pro

HC codes involve high-voltage DC bus circuitry, live inverter power stages, and surface-mount board-level diagnosis that require specialized tools and training. If you are not comfortable working with 300 V DC or interpreting diode-mode and capacitance readings on live inverter boards, call a qualified HVAC technician or authorized Gree service provider. If your visual inspection and simple voltage checks do not reveal an obvious fault, professional board-level diagnostics or board replacement is the safest and most reliable path forward.
