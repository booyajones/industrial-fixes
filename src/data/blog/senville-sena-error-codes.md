---
title: "Senville SENA Series Mini Split Error Codes — Complete Fault Guide"
description: "Complete guide to Senville SENA series mini split error codes, fault causes, and step-by-step troubleshooting for communication, sensor, and protection faults."
pubDatetime: 2026-04-22T22:00:00Z
modDatetime: 2026-04-22T22:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - senville
  - mini-split
---

## Senville SENA Series Mini Split Error Codes — What They Mean

The Senville SENA series covers a range of ductless mini split units from 9,000 to 36,000 BTU, including standard single-zone, multi-zone (MULTI series), and LETO/AURA model variants. All SENA units display error codes on the indoor unit LED display. The code flashes or appears as a static display when a fault is active.

[Jump to Fix](#fix)

## Senville SENA Error Code Reference

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Meaning |
|------|---------|
| [E1](https://www.amazon.com/s?k=E1&tag=errorcodefixe-20) | Indoor/outdoor communication error |
| [E2](https://www.amazon.com/s?k=E2&tag=errorcodefixe-20) | Indoor fan motor error |
| [E3](https://www.amazon.com/s?k=E3&tag=errorcodefixe-20) | Outdoor fan motor error |
| [E4](https://www.amazon.com/s?k=E4&tag=errorcodefixe-20) | High-pressure protection |
| [E5](https://www.amazon.com/s?k=E5&tag=errorcodefixe-20) | Low-pressure protection |
| [E6](https://www.amazon.com/s?k=E6&tag=errorcodefixe-20) | Compressor overcurrent or overload |
| [E7](https://www.amazon.com/s?k=E7&tag=errorcodefixe-20) | IPM (inverter power module) protection |
| [E8](https://www.amazon.com/s?k=E8&tag=errorcodefixe-20) | AC input current protection |
| [F0](https://www.amazon.com/s?k=F0&tag=errorcodefixe-20) | Outdoor ambient temperature sensor fault |
| [F1](https://www.amazon.com/s?k=F1&tag=errorcodefixe-20) | Indoor temperature sensor fault |
| [F2](https://www.amazon.com/s?k=F2&tag=errorcodefixe-20) | Indoor coil temperature sensor fault |
| [F3](https://www.amazon.com/s?k=F3&tag=errorcodefixe-20) | Outdoor coil temperature sensor fault |
| [F4](https://www.amazon.com/s?k=F4&tag=errorcodefixe-20) | Discharge temperature sensor fault |
| [F5](https://www.amazon.com/s?k=F5&tag=errorcodefixe-20) | Suction temperature sensor fault |
| [P1](https://www.amazon.com/s?k=P1&tag=errorcodefixe-20) | High-pressure switch protection |
| [P2](https://www.amazon.com/s?k=P2&tag=errorcodefixe-20) | Low-pressure switch protection |
| [P4](https://www.amazon.com/s?k=P4&tag=errorcodefixe-20) | Freeze protection (indoor coil too cold) |

## Common Causes by Code

- **E1 — Communication** — The three-wire communication cable between indoor and outdoor units. On SENA units, this is typically labeled as Terminal 1, 2, and 3. Loose terminals at either unit are the most common field cause. Also caused by a failed component on either unit's PCB.
- **E4 — High pressure** — Dirty outdoor coil, failed outdoor fan motor, or refrigerant overcharge. Also occurs in cooling mode if the indoor coil is completely iced over (from an earlier low-refrigerant run), blocking indoor airflow.
- **E5 — Low pressure** — Refrigerant leak, dirty indoor filter blocking evaporator airflow (can cause low suction pressure), or a failed low-pressure sensor.
- **E7 — IPM protection** — The inverter power module drives the variable-speed compressor. E7 indicates an overcurrent or overheat condition in the IPM. Often caused by low refrigerant charge putting excessive load on the compressor, or a failing compressor drawing too many amps.
- **F1 / F2 — Sensor faults** — NTC thermistors in the indoor unit. F1 is room temperature, F2 is coil temperature. A loose connector on the indoor PCB is the most common cause — reseat before replacing the sensor.
- **P4 — Freeze protection** — The indoor coil temperature has dropped below the freeze setpoint. This is a protective shutdown, not a primary fault. Look for the underlying cause: low refrigerant, dirty filter, or extremely low return air temperature.

## Step-by-Step Fix {#fix}

1. **Note the display code** — The Senville SENA indoor unit displays the error code on the temperature readout. The code appears when the fault is active and clears when the fault condition resolves.
2. **For E1** — Inspect all three communication wires at both the indoor and outdoor terminal blocks. Senville SENA units use push-in or screw terminals; confirm each wire is fully inserted and secure.
3. **For E4 / P1** — Turn off the unit. Clean the outdoor coil with a garden hose. Confirm the outdoor fan runs when the unit is powered on. If both are fine, check refrigerant charge — overcharge is a possible cause after DIY recharge attempts.
4. **For E5 / P2** — Check the indoor filter and clean or replace it. Connect refrigerant gauges and check suction pressure. If low, perform a leak check before adding refrigerant.
5. **For E7** — Do not repeatedly restart the unit with E7 active — IPM damage can result. Allow the outdoor unit to cool for 30 minutes. If E7 recurs immediately, check compressor amp draw with a clamp meter under load.
6. **For F1 / F2** — Open the indoor unit front cover. Locate the sensor wire connecting to the PCB. Unplug and measure resistance — compare to sensor chart in the Senville SENA service manual (available on Senville's website).
7. **For P4** — Check the indoor filter immediately. If clean, allow ice on the indoor coil to melt with the fan running (unit off for 30–60 minutes) before diagnosing further.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [Indoor room temp sensor](https://www.amazon.com/s?k=Indoor%20room%20temp%20sensor&tag=errorcodefixe-20) | F1; NTC 10kΩ at 25°C typical |
| [Indoor coil sensor](https://www.amazon.com/s?k=Indoor%20coil%20sensor&tag=errorcodefixe-20) | F2; clip-on type on evaporator |
| [Outdoor PCB](https://www.amazon.com/s?k=Outdoor%20PCB&tag=errorcodefixe-20) | For E7 after charge and compressor confirmed |
| [Communication cable](https://www.amazon.com/s?k=Communication%20cable&tag=errorcodefixe-20) | 3-conductor; replace full run |
| [Indoor PCB](https://www.amazon.com/s?k=Indoor%20PCB&tag=errorcodefixe-20) | For E2 or E1 with confirmed good wiring |
| [Outdoor fan motor](https://www.amazon.com/s?k=Outdoor%20fan%20motor&tag=errorcodefixe-20) | For E3; confirm DC or AC type |

## When to Call a Pro

Refrigerant diagnosis (E5, P2, E4) requires EPA 608 certification. If the SENA unit has E7 (IPM protection), a certified technician should measure compressor current draw and refrigerant pressures simultaneously — running an undercharged or overcharged system repeatedly destroys the IPM and compressor.
