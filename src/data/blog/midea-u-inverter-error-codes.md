---
title: "Midea U-Inverter Mini Split Error Codes — Complete Fault Guide"
description: "Complete guide to Midea U-Inverter mini split error codes, what each fault means, and step-by-step troubleshooting for the most common failures."
pubDatetime: 2026-04-22T22:00:00Z
modDatetime: 2026-04-22T22:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - midea
  - mini-split
---

## Midea U-Inverter Mini Split Error Codes — What They Mean

The Midea U-Inverter is a window-mounted mini split with a unique U-shaped design that allows the window to remain partially open. It uses an inverter-driven compressor for variable-speed operation. The U-Inverter communicates fault codes through its LED display and through the Midea mobile app when connected via Wi-Fi.

[Jump to Fix](#fix)

## Midea U-Inverter Error Code Reference

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Meaning |
|------|---------|
| [E1](https://www.amazon.com/s?k=E1&tag=errorcodefixe-20) | Indoor room temperature sensor fault |
| [E2](https://www.amazon.com/s?k=E2&tag=errorcodefixe-20) | Indoor coil temperature sensor fault |
| [E3](https://www.amazon.com/s?k=E3&tag=errorcodefixe-20) | Outdoor coil temperature sensor fault |
| [E4](https://www.amazon.com/s?k=E4&tag=errorcodefixe-20) | High-temperature protection (compressor or discharge) |
| [E5](https://www.amazon.com/s?k=E5&tag=errorcodefixe-20) | Freeze protection (indoor coil too cold) |
| [E6](https://www.amazon.com/s?k=E6&tag=errorcodefixe-20) | Communication error (indoor PCB to outdoor module) |
| [E7](https://www.amazon.com/s?k=E7&tag=errorcodefixe-20) | Outdoor fan motor fault |
| [E8](https://www.amazon.com/s?k=E8&tag=errorcodefixe-20) | PFC module protection |
| [E9](https://www.amazon.com/s?k=E9&tag=errorcodefixe-20) | Compressor drive fault (IPM protection) |
| [F0](https://www.amazon.com/s?k=F0&tag=errorcodefixe-20) | Discharge temperature sensor fault |
| [P2](https://www.amazon.com/s?k=P2&tag=errorcodefixe-20) | Low-pressure protection |
| [P6](https://www.amazon.com/s?k=P6&tag=errorcodefixe-20) | Compressor preheat active |

## Common Causes by Code

- **E1 / E2 — Indoor sensors** — The U-Inverter indoor sensors are located on the main PCB (room sensor) and clipped to the indoor coil (coil sensor). Connector dislodgement from vibration is a common cause — reseat the connector before replacing the sensor.
- **E4 — High temperature protection** — The compressor discharge temperature or the compressor shell temperature has exceeded the protection limit. Low refrigerant charge is the primary cause — a U-Inverter window unit doesn't have field-serviceable refrigerant connections, so low charge indicates a factory leak or seal failure.
- **E5 — Freeze protection** — Indoor coil is icing up. Common in the U-Inverter if the unit is running at maximum cooling capacity in a room that is already very cold, or if the indoor side is blocked. The U-shaped design means airflow depends on the clearances around the unit in the window opening — confirm the installation allows adequate airflow.
- **E6 — Communication error** — The U-Inverter has a split architecture with electronics on both the indoor and outdoor sections. The E6 communication error between the two halves often occurs after the unit is removed and reinstalled in a window — check the internal communication cable connection between sections.
- **E9 — IPM protection** — Inverter power module protection. Usually a downstream effect of E4 or low refrigerant — do not restart repeatedly.
- **P6 — Preheat** — Normal in cold outdoor temperatures. The compressor crankcase is heating before startup. Clears automatically.

## Step-by-Step Fix {#fix}

1. **Check the Midea app** — The Midea Home app shows fault codes with descriptions and timestamps. Enable this feature in the app settings.
2. **For E1 / E2** — Open the indoor unit front panel. Locate the sensor connectors on the PCB. Unplug and measure resistance — a room-temperature reading of approximately 10 kΩ (NTC 10kΩ type) is normal.
3. **For E5 — Freeze protection** — Turn off cooling mode and run fan-only for 60 minutes. Check that the window opening has proper clearances as specified in the Midea U-Inverter installation guide — the unit needs at least 6 inches of clearance on the outdoor section for airflow.
4. **For E6** — Remove the unit from the window and inspect the internal cable connecting the indoor and outdoor sections. This is a flat ribbon cable or multi-pin connector depending on the U-Inverter generation. Ensure it is fully seated.
5. **For E4 / E9** — Turn the unit off for at least 30 minutes. Do not try to bypass these protections. If E4 or E9 recurs on the next startup cycle, the unit likely has low refrigerant and should be returned or serviced under warranty.
6. **For E7 / P2** — Check outdoor airflow by confirming nothing is blocking the outdoor section of the U-Inverter (the section that hangs outside the window). Debris, leaves, or bird nests can obstruct the outdoor coil and fan.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [Room temperature sensor (E1)](https://www.amazon.com/s?k=Room%20temperature%20sensor%20(E1)&tag=errorcodefixe-20) | NTC 10kΩ; confirm U-Inverter model number |
| [Coil temperature sensor (E2)](https://www.amazon.com/s?k=Coil%20temperature%20sensor%20(E2)&tag=errorcodefixe-20) | Clip-on type; confirm coil sensor vs. room sensor |
| [Indoor PCB](https://www.amazon.com/s?k=Indoor%20PCB&tag=errorcodefixe-20) | For E6 with confirmed cable connection |
| [Internal cable assembly](https://www.amazon.com/s?k=Internal%20cable%20assembly&tag=errorcodefixe-20) | Between indoor and outdoor sections |
| [Outdoor PCB](https://www.amazon.com/s?k=Outdoor%20PCB&tag=errorcodefixe-20) | For E9 after charge confirmed |

## When to Call a Pro

The Midea U-Inverter is a sealed refrigerant system — it is not designed for field recharging. If the unit has low refrigerant (indicated by E4, E9, or P2 that persists), contact Midea customer service (1-855-643-3248) for warranty replacement. DIY refrigerant access on a sealed window unit is not recommended.
