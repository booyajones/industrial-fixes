---
title: "Mitsubishi Mini Split E1 Error Code — Indoor Thermistor Fault Fix"
author: "Marcus Webb"
pubDatetime: 2026-04-26T17:00:00Z
modDatetime: 2026-04-26T17:00:00Z
slug: mitsubishi-mini-split-e1-error
featured: false
draft: false
tags:
  - mini-split
  - mitsubishi
  - hvac
  - thermistor
description: "Mitsubishi mini split E1 error code indicates an indoor thermistor fault. Learn how to diagnose a failed room temperature sensor and fix E1 on MSZ and MXZ series units."
---

## Error Code: Mitsubishi Mini Split E1

**What it means:** The E1 error code on Mitsubishi mini split systems points to a fault in the indoor unit's room temperature thermistor (also called the ambient air sensor or return air sensor). This thermistor monitors the room air temperature and feeds that data to the control board, which uses it to regulate system operation and determine when target temperature setpoint has been reached. When the board detects that the thermistor is reading an implausible value — or no value at all (open circuit) — it locks out the system and displays E1.

E1 is a common fault identified by HVAC professionals as one of the top Mitsubishi mini split sensor errors. The good news: the indoor thermistor is an inexpensive, accessible part. Many homeowners and facilities managers can replace it without calling a technician.

## Common Causes

- **Failed indoor room temperature thermistor** — The NTC (negative temperature coefficient) thermistor has drifted out of spec, developed an open circuit, or shorted internally. This is the primary cause of E1.
- **Loose or disconnected thermistor connector** — The small plastic connector between the thermistor and the control board has come loose, creating an intermittent or open circuit.
- **Damaged thermistor wiring** — The thin wires running from the thermistor to the PCB have been pinched, frayed, or nicked during filter cleaning or maintenance.
- **Contaminated or wet thermistor** — In high-humidity environments or after a refrigerant leak causes frost buildup in the indoor unit, condensation or water can flood the thermistor, degrading its resistance characteristics.
- **Failed indoor control board** — If the thermistor reads correctly with a multimeter but E1 persists, the board's thermistor input circuit may have failed.

## Step-by-Step Diagnosis {#step-by-step-fix}

1. **Power down the indoor unit.** Turn off the mini split and switch off the breaker. Remove the front cover and filter panel. Take a photo of the interior before touching anything — this is your reference.

2. **Locate the indoor thermistor.** The room temperature thermistor on most Mitsubishi indoor units (MSZ-GL, MSZ-GE, MSZ-FH, and related series) is a small bead or pin-type sensor, typically clipped to the air intake area or the front of the evaporator coil. It connects to the control board via a small 2-pin or 3-pin connector. A separate thermistor monitors the evaporator coil (pipe thermistor, which causes E9 errors, not E1).

3. **Inspect the connector and wiring.** Gently unplug and re-plug the thermistor connector. Look for bent pins, green corrosion, or broken wire insulation. If the connector shows corrosion, clean the pins with electrical contact cleaner and reconnect.

4. **Test thermistor resistance.** Disconnect the thermistor from the board. Set a multimeter to resistance (Ω) mode. Measure across the two thermistor leads. At room temperature (approximately 77°F / 25°C), most Mitsubishi indoor thermistors read approximately 10–15 kΩ. An open circuit (OL) confirms a failed thermistor. A short circuit (near 0 Ω) also confirms failure. Check your service manual for the exact resistance-temperature chart for your model.

5. **Compare to spec.** If the measured resistance is wildly off from the expected value at the current room temperature, the thermistor is out of spec and should be replaced even if it doesn't show a full open circuit.

6. **Restore power and monitor.** After reconnecting or replacing the thermistor, restore power and observe whether E1 clears. If the code persists after a confirmed good thermistor is installed, the indoor control board may need to be replaced.

## How to Fix It

- **Failed or out-of-spec thermistor:** Order the correct replacement thermistor for your specific Mitsubishi model (see label on indoor unit for model number). The thermistor clips into place and the connector snaps onto the board — no soldering required. This repair takes about 15 minutes.
- **Loose connector:** Re-seat the connector firmly. Apply a small amount of dielectric grease to prevent future corrosion.
- **Damaged wire:** Splice and heat-shrink any damaged section, or replace the entire thermistor assembly.
- **Failed control board:** If all thermistor checks pass but E1 persists, replace the indoor PCB. Document all wiring before removal.

## Parts You May Need

- [Mitsubishi Indoor Room Temperature Thermistor Sensor](https://www.amazon.com/s?k=Mitsubishi+mini+split+indoor+room+thermistor+sensor&tag=errorcodefixes-20)
- [Mitsubishi Indoor Unit Control Board PCB](https://www.amazon.com/dp/B0CNZGZ1HS?tag=errorcodefixes-20)
- [Electrical Contact Cleaner Spray](https://www.amazon.com/s?k=electrical+contact+cleaner+spray&tag=errorcodefixes-20)
- [Dielectric Grease for Electrical Connectors](https://www.amazon.com/s?k=dielectric+grease+electrical+connectors&tag=errorcodefixes-20)
- [Digital Multimeter for HVAC Diagnostics](https://www.amazon.com/dp/B08ZJSN5X3?tag=errorcodefixes-20)

## When to Call a Technician

If the thermistor tests open or out-of-spec and replacement does not clear E1, the issue has moved to the control board — or there is a wiring harness problem that is not obvious on visual inspection. A Mitsubishi-certified technician can use the SG-K900AT service tool to read the raw thermistor input value on the board and confirm whether the fault is in the sensor circuit or the board itself. Control board replacement is feasible as a DIY task if you are methodical about documenting wiring before removal.

## Related Error Codes

- [Mitsubishi Mini Split E9 Error Code — Pipe Thermistor Fault](/posts/mitsubishi-mini-split-e9-error-code/)
- [Mitsubishi Mini Split E6 Error Code — Communication Error Fix](/posts/mitsubishi-mini-split-e6-error/)
- [Mitsubishi Mini Split P8 Error Code — Outdoor Heat Exchanger Overtemp](/posts/mitsubishi-mini-split-p8-error/)
- [Mitsubishi Mini Split U4 Error Code — Outdoor Thermistor Fault](/posts/mitsubishi-mini-split-u4-error-code/)
