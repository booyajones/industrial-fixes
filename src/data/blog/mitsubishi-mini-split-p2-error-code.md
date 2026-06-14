---
title: "Mitsubishi Mini Split P2 Error - Causes & Fix"
description: "P2 means a faulty indoor pipe thermistor (TH2). Most often fixed by reseating the sensor in its holder or replacing the thermistor."
pubDatetime: 2026-05-31T00:49:31Z
modDatetime: 2026-05-31T00:49:31Z
author: "James Rutherford"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - mitsubishi-electric
money_part: "Mitsubishi indoor pipe thermistor (TH2)"
most_likely_cause: "Thermistor disconnected from holder"
---

## Mitsubishi Mini Split P2 Error — What It Means

The P2 error on Mitsubishi Electric mini-split systems indicates a pipe sensor fault on the indoor unit, specifically the TH2 thermistor that monitors temperature on the indoor coil piping circuit. Mitsubishi's fault table labels this as a pipe (liquid or two-phase pipe) sensor error, not a compressor overheat or refrigerant issue. The indoor control board has detected that the thermistor signal is out of range, open, shorted, or missing entirely.

This code will prevent normal operation until the sensor circuit is restored. The fault is electrical in nature and points to the sensor itself, its wiring harness, or the indoor control board input circuit.

[Jump to Fix](#fix)

## Common Causes

- **Thermistor disconnected from holder** The TH2 or TH5 pipe sensor has slipped out of its mounting clip on the indoor coil piping, breaking thermal contact and causing an out-of-range reading.
- **Open or shorted thermistor** The sensor element itself has failed internally, reading infinite resistance (open) or near-zero resistance (shorted), both of which the board interprets as a fault.
- **Loose or disconnected wiring** The sensor harness connector at the indoor board or at the sensor lead is loose, corroded, or fully unplugged.
- **Reversed or incorrect connection** The sensor wiring has been connected backward or to the wrong terminal during prior service, sending an invalid signal to the control board.
- **Indoor control board fault** The input circuit on the indoor PCB has failed, misreading a good sensor as faulty or failing to power the thermistor circuit correctly.

## Step-by-Step Fix {#fix}

1. {'lead': 'Turn off power to both indoor and outdoor units', 'text': 'Switch off the breaker or disconnect to safely inspect sensor and wiring components without risk of shock or short-circuit damage.'}
2. {'lead': 'Locate and inspect the indoor pipe thermistor', 'text': 'Find the TH2 sensor on the indoor evaporator coil piping (usually clipped to the liquid or suction line) and check that it is fully seated in its holder and not damaged or corroded.'}
3. {'lead': 'Check the sensor harness and connectors', 'text': 'Trace the thermistor wires from the sensor to the indoor control board, inspecting for loose pins, broken conductors, corrosion, or reversed polarity at every connection point.'}
4. {'lead': 'Measure thermistor resistance', 'text': "Disconnect the sensor leads and use a multimeter to measure resistance across the thermistor terminals, then compare the reading to the manufacturer's thermistor table for your model (consult your service literature for the correct curve)."}
5. {'lead': 'Reseat or replace the sensor if faulty', 'text': 'If the sensor is loose, clip it firmly back into the holder with good thermal contact; if resistance is out of spec or the sensor is damaged, replace the TH2 thermistor with a genuine Mitsubishi part.'}
6. {'lead': 'Replace the indoor control board if the fault persists', 'text': "If the sensor and wiring both test good and the P2 code returns after power reset, replace the indoor PCB per Mitsubishi's troubleshooting directive."}
7. {'lead': 'Restore power and verify operation', 'text': 'Turn the system back on, run a cooling or heating cycle, and confirm that the P2 code clears and the unit operates normally without re-flagging the fault.'}

## Parts Often Needed

| Part | Notes |
|------|-------|
| Mitsubishi indoor pipe thermistor (TH2) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-mini-split-p2-error-code&k=Mitsubishi+indoor+pipe+thermistor+%28TH2%29&tag=errorcodefixes-20) \| Verify part number against your indoor model tag; TH2 and TH5 sensors may differ by series. |
| Mitsubishi indoor control PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-mini-split-p2-error-code&k=Mitsubishi+indoor+control+PCB&tag=errorcodefixes-20) \| Required if sensor and wiring test good but fault persists; match board part number to your exact indoor unit model. |

## When to Call a Pro

Call a licensed HVAC technician if you are uncomfortable working with live electrical components, cannot safely access the indoor coil, or lack a multimeter and thermistor resistance chart for your model. Also call a pro if the P2 code returns after you have verified and replaced the sensor, since board-level diagnosis and refrigerant-side checks require gauges, recovery equipment, and EPA certification. If your system is under warranty, contact an authorized Mitsubishi Electric dealer to avoid voiding coverage with DIY repairs.

## See Also

- [Mitsubishi E4 Error Code — Causes & Fix](/posts/mitsubishi-e4-error-code/)
- [Mitsubishi Mini Split P6 Error Code Fix](/posts/mitsubishi-p6-error-code/)
- [Mitsubishi Mr. Slim Error Code P6 - What It Means and How to Fix It](/posts/mitsubishi-mr-slim-error-code-p6/)
- [Mitsubishi Mini Split Won't Turn On - Causes & Fix](/posts/mitsubishi-mini-split-wont-turn-on/)
