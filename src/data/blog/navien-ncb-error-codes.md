---
title: "Navien NCB Combi Boiler Error Codes — Complete Fault Guide"
description: "Complete guide to Navien NCB combi boiler error codes, what each fault means, and step-by-step troubleshooting for heating and hot water failures."
pubDatetime: 2026-04-22T22:00:00Z
modDatetime: 2026-04-22T22:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - plumbing
  - navien
  - boiler
---

## Navien NCB Combi Boiler Error Codes — What They Mean

The Navien NCB (NCB-180, NCB-210, NCB-240) is a condensing combination boiler that provides both space heating and domestic hot water from a single unit. It displays error codes on the front panel display. The NCB has two heat exchangers — primary for heating and secondary for DHW — making fault diagnosis more nuanced than a standard tankless water heater.

[Jump to Fix](#fix)

## Navien NCB Error Code Reference

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Meaning |
|------|---------|
| [E001](https://www.amazon.com/s?k=E001&tag=errorcodefixe-20) | Ignition failure |
| [E002](https://www.amazon.com/s?k=E002&tag=errorcodefixe-20) | Flame loss during operation |
| [E003](https://www.amazon.com/s?k=E003&tag=errorcodefixe-20) | Ignition lockout (repeated failure) |
| [E004](https://www.amazon.com/s?k=E004&tag=errorcodefixe-20) | False flame detected |
| [E006](https://www.amazon.com/s?k=E006&tag=errorcodefixe-20) | DHW outlet overtemperature |
| [E007](https://www.amazon.com/s?k=E007&tag=errorcodefixe-20) | DHW outlet temperature sensor fault |
| [E008](https://www.amazon.com/s?k=E008&tag=errorcodefixe-20) | Heating supply temperature sensor fault |
| [E009](https://www.amazon.com/s?k=E009&tag=errorcodefixe-20) | Heating return temperature sensor fault |
| [E010](https://www.amazon.com/s?k=E010&tag=errorcodefixe-20) | Condensate pressure switch fault |
| [E011](https://www.amazon.com/s?k=E011&tag=errorcodefixe-20) | Cascade / system communication fault |
| [E012](https://www.amazon.com/s?k=E012&tag=errorcodefixe-20) | DHW inlet temperature sensor fault |
| [E016](https://www.amazon.com/s?k=E016&tag=errorcodefixe-20) | Heating temperature exceeded maximum |
| [E021](https://www.amazon.com/s?k=E021&tag=errorcodefixe-20) | Low water pressure in heating system |
| [E022](https://www.amazon.com/s?k=E022&tag=errorcodefixe-20) | Heating system overpressure |
| [E024](https://www.amazon.com/s?k=E024&tag=errorcodefixe-20) | Fan motor fault |
| [E028](https://www.amazon.com/s?k=E028&tag=errorcodefixe-20) | DHW flow sensor fault |
| [E030](https://www.amazon.com/s?k=E030&tag=errorcodefixe-20) | Freeze protection active |
| [E034](https://www.amazon.com/s?k=E034&tag=errorcodefixe-20) | DHW temperature sensor (secondary) fault |
| [E040](https://www.amazon.com/s?k=E040&tag=errorcodefixe-20) | 3-way valve fault (heating vs. DHW switching) |

## Common Causes by Code

- **E001 / E003 — Ignition** — Low gas pressure, blocked combustion air, or a failed igniter. The NCB's condensate pressure switch (E010) often appears alongside E001 — check the condensate drain first.
- **E010 — Condensate pressure switch** — The NCB uses a pressure switch to confirm proper condensate drainage. A blocked condensate drain, frozen drain line (exterior drain in cold climates), or failed pressure switch causes E010. Confirm the condensate drain flows freely before any other diagnosis.
- **E021 — Low water pressure** — The NCB heating circuit requires minimum 12 PSI. If the system pressure drops below this, E021 appears. The pressure gauge is on the front of the NCB — normal operating range is 12–18 PSI. Add water through the fill valve if low.
- **E022 — Overpressure** — Heating system pressure has exceeded the maximum (usually 30 PSI). This indicates a failed expansion tank or a fill valve stuck open. Check the system expansion tank pre-charge pressure.
- **E024 — Fan** — The combustion fan motor has failed. Check fan rotation and confirm power supply to the motor.
- **E040 — 3-way valve** — The NCB uses a 3-way valve to direct hot water to either the heating circuit or the DHW heat exchanger. A stuck or failed 3-way valve causes either heating-only or DHW-only operation depending on which position it is stuck in.

## Step-by-Step Fix {#fix}

1. **Read the front panel display** — The NCB shows the active error code. Press and hold the INFO button to see system status including water pressure, temperatures, and flow rate.
2. **For E021 (low pressure)** — Locate the fill valve (manual fill or auto-fill depending on installation). Open slowly to raise system pressure to 15 PSI. If pressure does not hold (drops again within a day), there is a leak in the heating system.
3. **For E010 (condensate)** — Trace the condensate drain from the NCB to its drain point. Confirm the drain is not frozen (exterior drain lines in cold climates must be insulated). Clear any blockage with warm water.
4. **For E001 / E003** — Check gas supply at the meter and at other gas appliances. Inspect the exterior air intake and exhaust terminations. If venting is clear and gas is confirmed, test the igniter and gas valve.
5. **For E040 (3-way valve)** — Listen for the 3-way valve motor switching during a hot water demand vs. a heating demand. The valve motor should audibly click and turn. If stuck, confirm 24V power to the valve motor, then inspect the valve mechanism for scale or physical obstruction.
6. **For E024 (fan)** — Access the combustion fan inside the NCB cabinet. Spin by hand — should rotate freely. Confirm the fan receives power during startup; listen for spin-up before each ignition attempt.
7. **Reset** — Press RESET on the front panel. For E003 lockout, hold RESET for 5 seconds.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [3-way valve motor](https://www.amazon.com/s?k=3-way%20valve%20motor&tag=errorcodefixe-20) | E040; replace motor before full valve assembly |
| [Condensate pressure switch](https://www.amazon.com/s?k=Condensate%20pressure%20switch&tag=errorcodefixe-20) | E010 after drain confirmed clear |
| [Expansion tank](https://www.amazon.com/s?k=Expansion%20tank&tag=errorcodefixe-20) | For E022 (overpressure) — check pre-charge |
| [Fan motor assembly](https://www.amazon.com/s?k=Fan%20motor%20assembly&tag=errorcodefixe-20) | E024; includes wheel |
| [DHW flow sensor](https://www.amazon.com/s?k=DHW%20flow%20sensor&tag=errorcodefixe-20) | E028; descale before replacing |
| [3-way valve seal kit](https://www.amazon.com/s?k=3-way%20valve%20seal%20kit&tag=errorcodefixe-20) | If valve leaks internally |

## When to Call a Pro

The NCB's dual-function design (heating + DHW) requires diagnosis of both the heating circuit and the domestic water circuit. Low system pressure diagnosis (E021) should include a leak search throughout the heating piping. Gas valve replacement requires a licensed plumber or gas technician in most jurisdictions.
