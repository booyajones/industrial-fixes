---
title: "Weil-McLain ECG Boiler Error Codes — Complete Fault Guide"
description: "Complete guide to Weil-McLain ECG series gas boiler error codes, fault causes, and step-by-step troubleshooting for the most common heating system failures."
pubDatetime: 2026-04-22T22:00:00Z
modDatetime: 2026-04-22T22:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - plumbing
  - weil-mclain
  - boiler
---

## Weil-McLain ECG Boiler Error Codes — What They Mean

The Weil-McLain ECG (ECG-Series) is a cast-iron gas boiler designed for hydronic heating systems. It uses a standing pilot or intermittent ignition system and a series of safety controls to protect the boiler and heating system. Faults on the ECG are indicated by lockout status on the Beckett or Honeywell ignition module, LED flash codes on the aquastat relay, or visible indicators depending on the model and accessories.

[Jump to Fix](#fix)

## Weil-McLain ECG Fault Indicators

| Indicator | Meaning |
|-----------|---------|
| Red LED flashing (fast) | Ignition lockout — failed to establish flame |
| Red LED flashing (slow) | Soft lockout — pressure or temperature limit tripped |
| Red LED steady | Control board fault |
| Pilot out (standing pilot) | Pilot light extinguished — thermocouple or draft |
| Limit switch open | High temperature or pressure limit tripped |
| Low water cutoff open | Low water in boiler — flow or makeup issue |

## Common ECG Fault Codes (Beckett AFG Ignition Module)

| Flash Code | Meaning |
|------------|---------|
| 1 flash | Pilot/ignition failed — lockout |
| 2 flashes | Pilot established but main burner failed |
| 3 flashes | Flame signal lost during run |
| 4 flashes | Limit string open (limit, pressure switch, LWCO) |
| 5 flashes | Control board fault |

## Common Causes

- **Ignition lockout (pilot out)** — On standing pilot models: thermocouple failure (weak millivolt signal), pilot orifice clogged with debris, draft problems extinguishing the pilot. The thermocouple should generate at least 18–20 mV DC when the pilot flame engulfs the tip.
- **Ignition lockout (intermittent ignition)** — On models with Beckett or Honeywell electronic ignition: failed igniter, low gas pressure, dirty flame sensor, or blocked flue.
- **Limit trip (Code 4 / slow LED)** — The ECG limit switch opens if the boiler water temperature exceeds the setpoint (typically 180–200°F). Common causes: failed circulator pump, zone valves all closed, air in the system, or a failed limit switch that trips early.
- **Low water cutoff (LWCO)** — The McDonnell & Miller or Hydrolevel LWCO on the ECG opens if the boiler water level drops below the probe. Causes: steam loss, system leak, or a failed LWCO probe with mineral scale coating.
- **Pressure relief valve weeping** — If the system pressure exceeds 30 PSI, the relief valve opens. Check the expansion tank pre-charge and confirm no fill valve is stuck open.

## Step-by-Step Fix {#fix}

1. **Identify the fault** — Check the ignition module LED, the aquastat LED if present, and visually inspect the pilot flame (for standing pilot models). On intermittent ignition, listen for igniter clicking during startup.
2. **For ignition lockout (standing pilot)** — Light the pilot manually per the instructions on the boiler jacket. Hold the pilot button for 30–60 seconds to heat the thermocouple. If the pilot won't stay lit when the button is released, the thermocouple needs replacement.
3. **For ignition lockout (electronic)** — Press the red RESET button on the ignition module. During the next startup attempt, confirm gas is flowing (you should hear/smell brief ignition). If no flame establishes, check gas pressure and flame sensor.
4. **For limit trip** — Check the aquastat setpoint (typically 180°F supply, 160°F differential). Confirm the circulation pump is running — listen for pump noise and feel for warm return pipes. Check all zone valves for proper operation.
5. **For LWCO lockout** — Inspect the boiler sight glass (if equipped) or probe port. If water level is normal, the LWCO probe may be coated with scale — clean the probe with fine steel wool or a light acid wash (diluted white vinegar).
6. **For pressure relief weeping** — Check system pressure gauge. Normal is 12–20 PSI for hot water boilers. If pressure is high, test the expansion tank — press the Schrader valve; water should not come out.
7. **Reset module** — Press the red RESET button on the ignition module. Do not press more than twice without diagnosing — repeated resets without investigation can flood the combustion chamber with gas.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Thermocouple | [Amazon](https://www.amazon.com/s?k=Thermocouple&tag=errorcodefixes-20) \| For standing pilot models; $10–20 |
| Ignition module (Beckett/Honeywell) | [Amazon](https://www.amazon.com/s?k=Ignition+module+%28Beckett%2FHoneywell%29&tag=errorcodefixes-20) \| For electronic ignition lockout |
| Circulator pump | [Amazon](https://www.amazon.com/s?k=Circulator+pump&tag=errorcodefixes-20) \| For limit trips with zone valve confirmed open |
| Low water cutoff (LWCO) | [Amazon](https://www.amazon.com/s?k=Low+water+cutoff+%28LWCO%29&tag=errorcodefixes-20) \| For LWCO lockout with normal water level |
| Expansion tank | [Amazon](https://www.amazon.com/s?k=Expansion+tank&tag=errorcodefixes-20) \| For pressure relief weeping; confirm pre-charge |
| Aquastat relay | [Amazon](https://www.amazon.com/s?k=Aquastat+relay&tag=errorcodefixes-20) \| For control failures on older ECG models |
## When to Call a Pro

Gas boiler work involves gas combustion, high-temperature/pressure systems, and often asbestos insulation on older installations. If you smell gas, see carbon deposits on the burner, or the LWCO has tripped on a steam boiler, stop operating the unit and call a licensed heating contractor immediately.

## Related Articles

- [American Water Heater Error Codes — Complete Guide](/posts/american-water-heater-error-codes/)
- [AO Smith Water Heater 3 Flashes — What It Means and How to Fix It](/posts/ao-smith-water-heater-3-flashes/)
- [AO Smith Water Heater 4 Flashes — What It Means and How to Fix It](/posts/ao-smith-water-heater-4-flashes/)
- [A.O. Smith Water Heater Error Codes Guide](/posts/ao-smith-water-heater-error-codes/)
- [Bradford White Water Heater Error Code 1 — Pilot Outage Fix](/posts/bradford-white-error-code-1/)
