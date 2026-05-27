---
title: "Mitsubishi Mini Split E9 Error Code — Outdoor Thermistor 2 Fault Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2026-04-26T17:45:00Z
featured: false
draft: false
tags:
  - mini-split
  - mitsubishi
  - hvac
description: "Mitsubishi mini split E9 error code means outdoor thermistor 2 (discharge pipe) fault. Learn the causes, how to test the thermistor, and fix it step by step."
---

## Mitsubishi Mini Split E9 Error Code — What It Means

The **E9 error code** on a Mitsubishi mini split indicates a fault with the **outdoor unit's second thermistor** — specifically the outdoor discharge pipe thermistor, designated TH3 in Mitsubishi's service manuals (some models call it the outdoor liquid pipe thermistor). This is the temperature sensor that monitors the refrigerant leaving the outdoor coil during cooling, or entering the outdoor coil during heating. When the control board reads an implausible resistance from this sensor — either open circuit (infinite resistance) or short circuit (near-zero resistance) — it locks out the system and displays E9 on the indoor unit.

E9 is the outdoor thermistor 2 fault. It is different from E1 (indoor room temperature thermistor) and functions as a companion fault in the outdoor sensor group. The system cannot safely manage refrigerant temperatures without accurate data from this sensor, so the lockout is designed to protect the compressor from operating under unknown conditions.

[Jump to Fix](#fix)

## Common Causes

- **Failed thermistor element** — The thermistor's resistance-temperature curve has drifted out of specification due to age, heat cycling fatigue, or physical damage. A failed thermistor will measure open or near-zero resistance at room temperature.
- **Corroded or damaged wiring harness** — The wire from the thermistor bead to the outdoor PCB connector runs through the outdoor unit chassis. It can be pinched by panels during service, nicked by rodents, or corroded from moisture intrusion over years of operation.
- **Moisture in the PCB connector** — Water finds its way into the outdoor unit's PCB connector block and corrodes the thermistor pin terminals. This creates a variable resistance that can spike E9 intermittently or permanently.
- **Outdoor PCB failure** — The thermistor input circuit on the outdoor control board has failed — a less common but definitive cause when the thermistor itself tests within spec.
- **Loose connector** — Vibration from the compressor can slowly work the thermistor connector loose from the PCB header, creating an intermittent open circuit.

## Step-by-Step Fix {#fix}

1. **Power off the outdoor unit** — Turn off the mini split from the remote, then shut off the breaker for the outdoor unit. Wait 5 minutes for capacitors to discharge before opening the service panel.

2. **Locate thermistor TH3 on the outdoor PCB** — Open the outdoor unit service panel (typically 4–6 screws on the front). The outdoor PCB is mounted inside. Identify the thermistor connectors — they are usually 2-pin white or grey plastic connectors labeled TH1, TH2, TH3 on the board or in the wiring diagram printed inside the panel cover.

3. **Test the thermistor resistance** — Disconnect the TH3 (Thermistor 2) connector and measure resistance across the two thermistor leads with a digital multimeter set to resistance (ohms). At 25°C (77°F) room temperature, Mitsubishi outdoor thermistors typically read **10 kΩ to 15 kΩ**. Check the service manual resistance table for your exact model. A reading of OL (open) or less than 1 kΩ at room temperature confirms thermistor failure.

4. **Inspect the thermistor wire** — Trace the wire from the connector to the thermistor bead, which is clipped or inserted into the discharge pipe or coil tube. Look for: pinched or kinked wire, chafed insulation from rubbing against metal edges, or rodent damage. A wire fault causes the same electrical symptom as a failed thermistor element.

5. **Clean the PCB connector** — If the thermistor tests good but E9 persists, focus on the connector. Spray electrical contact cleaner into both sides of the TH3 connector. Inspect the pins for green oxidation or pushed-back pins. Use a small pin to gently re-tension any pin that has lost its grip.

6. **Reconnect, power on, and reset** — After service, reconnect all connectors, close the service panel, restore breaker power, and let the outdoor unit initialize. Press the RESET button on the indoor unit (or toggle the breaker off/on) to clear the fault. Run the unit in cooling or heating mode and confirm E9 does not return after the first 5 minutes of operation.

## Parts You May Need

| Part | Notes |
|------|-------|
| Outdoor discharge pipe thermistor (TH3) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-mini-split-e9-error&k=mitsubishi+mini+split+outdoor+thermistor+TH3&tag=errorcodefixes-20) — Must match your model number; thermistors are not interchangeable across series |
| Electrical contact cleaner | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-mini-split-e9-error&k=electrical+contact+cleaner+spray&tag=errorcodefixes-20) — Use before replacing the thermistor if corrosion is present on pins |
| Outdoor PCB (control board) | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?ascsubtag=ecf-mitsubishi-mini-split-e9-error&tag=errorcodefixes-20) — Replace only after confirming thermistor and wiring are good |
| Wire repair kit / heat shrink | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-mini-split-e9-error&k=wire+repair+heat+shrink+connectors&tag=errorcodefixes-20) — Use for splicing a damaged thermistor wire |

## When to Call a Technician

If the thermistor and wiring both test good and E9 persists after connector cleaning, the outdoor PCB has failed. PCB replacement on Mitsubishi outdoor units involves disconnecting the refrigerant pressure switch and other safety interlocks, which should be performed by an HVAC technician familiar with Mitsubishi's system. Additionally, if you observe refrigerant oil staining near the discharge pipe where TH3 mounts, a refrigerant leak may have damaged the thermistor or wiring — refrigerant system work requires EPA 608 certification.

## Related Articles

- [Mitsubishi Mini Split E1 Error Code — Indoor Thermistor Fault Fix](/posts/mitsubishi-mini-split-e1-error/)
- [Mitsubishi Mini Split E6 Error Code — Communication Fault Fix](/posts/mitsubishi-mini-split-e6-error/)
- [Mitsubishi Mini Split P8 Error Code — Drain Pan / Float Switch Fix](/posts/mitsubishi-mini-split-p8-error/)
- [Mitsubishi Mini Split U4 Error Code — Outdoor Communication Fault Fix](/posts/mitsubishi-mini-split-u4-error-code/)
- [Mitsubishi Mini Split Error Codes — Complete Fault Code Guide](/posts/mitsubishi-mini-split-error-codes/)

## See Also

- [Mitsubishi vs Daikin Mini-Splits — A Service Tech's Honest Comparison (2026)](/posts/mitsubishi-vs-daikin-mini-splits/)
- [Mitsubishi FR-A800 Fault E.OC1, Overcurrent During Acceleration Fix](/posts/mitsubishi-fr-a800-fault-eoc1/)
- [Mitsubishi E3 Error Code — Indoor Fan Motor Fault Fix](/posts/mitsubishi-e3-error-code/)
- [Mitsubishi P-Series H6 — Outdoor Fan Motor Fix](/posts/mitsubishi-heat-pump-error-code-h6/)
