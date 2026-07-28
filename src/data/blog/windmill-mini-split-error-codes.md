---
title: "Windmill AC Mini Split Error Codes — Complete Fault Code Guide"
description: "Complete guide to Windmill AC mini split error codes, fault causes, and step-by-step troubleshooting for the most common communication, sensor, and protection faults."
pubDatetime: 2026-04-22T22:00:00Z
modDatetime: 2026-04-22T22:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - windmill
  - mini-split
money_part: "Indoor filter"
---

## Windmill AC Mini Split Error Codes — What They Mean

The Windmill AC is a direct-to-consumer mini split sold online and through select retailers. It is designed for straightforward installation and pairs with the Windmill app for Wi-Fi control and diagnostics. Error codes appear on the indoor unit display or through the Windmill mobile app when a fault occurs.

## Windmill AC Error Code Reference

| Code | Meaning |
|------|---------|
| E1 | Indoor/outdoor communication fault |
| E2 | Indoor fan motor fault |
| E3 | Outdoor fan motor fault |
| E4 | Indoor coil freeze protection |
| E5 | Compressor overload protection |
| E6 | High-pressure protection |
| E7 | Low-pressure protection |
| F1 | Room temperature sensor fault |
| F2 | Indoor coil temperature sensor fault |
| F3 | Outdoor ambient temperature sensor fault |
| F4 | Outdoor coil temperature sensor fault |
| F5 | Discharge temperature sensor fault |
| P0 | IPM/inverter protection |
| P6 | Compressor preheat protection |

## Common Causes by Code

- **E1 — Communication fault** — The communication cable between indoor and outdoor units is the usual suspect. Windmill AC uses a standard three-wire signal cable; confirm each wire is connected to the correct terminal on both units. A firmware communication error can also cause E1 — a full power cycle often clears it.
- **E2 — Indoor fan motor** — DC fan motor fault. Check for debris or ice on the indoor fan. After clearing any obstruction, if the fault persists, the motor or indoor PCB may need replacement.
- **E4 — Freeze protection** — Indoor coil is too cold. Usually caused by low airflow (dirty filter, blocked return), extremely cold return air temperature, or low refrigerant charge. Do not run the unit in cooling below 62°F indoor temperature — the Windmill AC has a low-ambient cooling lockout.
- **E6 — High pressure** — Dirty outdoor coil or failed outdoor fan. Also occurs in very hot weather (above 115°F outdoor ambient) — the unit has a high-ambient lockout at 115°F outdoor.
- **E7 — Low pressure** — Low refrigerant charge is the primary cause. Less common: a failed suction pressure sensor. Connect gauges to confirm before making refrigerant decisions.
- **P0 — IPM protection** — Inverter module overprotection. Low refrigerant charge, extremely high ambient temperature, or a failing compressor can trigger P0. Allow 30 minutes before restarting.
- **P6 — Compressor preheat** — At very cold outdoor temperatures (below 32°F), the Windmill AC compressor preheat cycle activates before startup. P6 is normal in cold weather — it clears automatically when the crankcase is warm enough.

## Step-by-Step Fix {#fix}

1. **Check the Windmill app** — The mobile app shows error descriptions and history. This is easier than reading LED flash codes on the indoor unit.
2. **For E1** — Power cycle both units (indoor via remote, outdoor via circuit breaker, wait 60 seconds). If E1 persists, check the three-wire signal cable at both units.
3. **For E2 / E3** — With power off, attempt to spin the fan blade by hand. Confirm free rotation. If free, power on and listen — silence indicates power delivery issue; hum without rotation indicates motor failure.
4. **For E4** — Turn off cooling mode. Run fan-only for 45 minutes. Check and replace the filter. After melting any ice, restart cooling and monitor — if E4 recurs within 30 minutes, suspect low refrigerant.
5. **For E6** — Clean the outdoor coil with a garden hose. Confirm outdoor fan runs. If clean coil and running fan still produce E6, check refrigerant charge (overcharge is a possible cause after service).
6. **For E7 / P0** — Connect manifold gauges (certified technician required). Check suction and discharge pressures. Low suction with high superheat = low charge. Low suction with low superheat = restriction.
7. **For P6** — Wait. P6 is a normal protective preheat cycle in cold weather. If P6 persists for more than 60 minutes, the crankcase heater may have failed.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Indoor filter | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-windmill-mini-split-error-codes&k=Indoor+filter&tag=errorcodefixes-20) \| Clean/replace; most common cause of E4 |
| Temperature sensors | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-windmill-mini-split-error-codes&tag=errorcodefixes-20) \| F1/F2/F3/F4/F5 types; NTC thermistors |
| Indoor PCB | [Amazon](https://www.amazon.com/s?k=Indoor+PCB&tag=errorcodefixes-20) \| For E2 with confirmed free-spinning motor |
| Communication cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-windmill-mini-split-error-codes&k=Communication+cable&tag=errorcodefixes-20) \| 3-conductor; replace if damaged |
| Outdoor PCB | [Amazon](https://www.amazon.com/s?k=Outdoor+PCB&tag=errorcodefixes-20) \| For E3 or P0 after other causes ruled out |
## When to Call a Pro

Refrigerant work on the Windmill AC requires EPA 608 certification. Contact Windmill customer support for warranty service — the Windmill AC comes with a 5-year parts warranty on the compressor and 1 year on parts.
