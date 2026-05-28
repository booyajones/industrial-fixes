---
title: "Daikin RXYQ VRV System Error Codes — Complete Fault Code Guide"
description: "Complete guide to Daikin RXYQ VRV commercial system error codes, what each fault means, and step-by-step troubleshooting for the most common failures."
pubDatetime: 2026-04-22T22:00:00Z
modDatetime: 2026-04-22T22:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - hvac
  - daikin
  - vrv
  - commercial
---

## Daikin RXYQ VRV System Error Codes — What They Mean

The Daikin RXYQ is a commercial VRV (Variable Refrigerant Volume) outdoor unit used in multi-zone commercial HVAC applications. It communicates fault codes through the centralized control panel, BACnet/Modbus integration, or the remote controller display attached to each indoor unit. Error codes appear as alphanumeric codes (e.g., E1, E3, U0, L9) on the display.

[Jump to Fix](#fix)

## Daikin RXYQ Common Error Codes

| Code | Meaning |
|------|---------|
| E1 | Indoor PCB fault |
| E3 | High-pressure protection |
| E4 | Low-pressure protection |
| E5 | Outdoor fan motor fault |
| E7 | Electronic expansion valve (EEV) fault |
| E9 | Drain pump fault (indoor unit) |
| F3 | Discharge pipe temperature protection |
| F6 | Refrigerant overcharge / high-pressure protection |
| H6 | Outdoor fan motor position error |
| J3 | Discharge temperature sensor (Td) fault |
| J6 | Outdoor heat exchanger sensor fault |
| L4 | Radiation fin temperature rise |
| L5 | Inverter overcurrent protection |
| L9 | Compressor startup failure |
| U0 | Refrigerant shortage |
| U4 | Transmission error (outdoor to indoor) |
| U5 | Transmission error (remote to indoor) |
| UA | Refrigerant address setting error |

## Common Causes by Code

- **E3 — High pressure** — Dirty outdoor heat exchanger, failed outdoor fan motor, or refrigerant overcharge. On RXYQ systems with multiple outdoor units in parallel (heat recovery systems), check that all outdoor fan motors are running.
- **E4 — Low pressure** — Refrigerant leak, failed EEV, or operation in extreme cold ambient conditions. The RXYQ has broad operating range, but significant refrigerant loss (detectable by oil staining or electronic sniffer) is the primary cause.
- **E7 — EEV fault** — The electronic expansion valve controls refrigerant flow to each indoor unit. A sticking or failed EEV causes both E7 and downstream pressure/temperature faults. EEV coils can be tested for resistance (typically 33–56 ohms per winding pair).
- **L9 — Compressor startup failure** — The RXYQ uses inverter-driven compressors. L9 indicates the compressor failed to reach operating speed within the startup time limit. Causes: low discharge pressure (refrigerant leak), compressor mechanical failure, or inverter drive fault.
- **U0 — Refrigerant shortage** — The RXYQ calculates refrigerant balance using pressure and temperature sensors. U0 is a calculated alarm; confirm with actual gauge measurements. Leak search required.
- **U4 — Transmission error** — The outdoor and indoor units communicate via a two-wire F1/F2 bus. U4 indicates a communication break — check the F1/F2 wiring at all connection points, especially where cables pass through conduit (insulation damage is common).

## Step-by-Step Fix {#fix}

1. **Read the active fault code** — Access the remote controller on any affected indoor unit. Press the INSPECT button (some controllers) or check the unit display. On Daikin centralized controllers, the fault log shows all active and recent codes with timestamps.
2. **For E3 (high pressure)** — Confirm all outdoor fans are running. Inspect the outdoor heat exchanger for blockage — cottonwood seeds and leaves are common. Measure discharge pressure with refrigerant gauges (R-410A or R-32 depending on unit vintage).
3. **For E4 / U0 (low pressure / refrigerant shortage)** — Perform electronic leak detection across all refrigerant joints in the system. VRV systems have long refrigerant runs with many brazed joints — leaks at the indoor unit connections or header manifolds are common.
4. **For E7 (EEV fault)** — Confirm the EEV coil is seated on the valve body. Measure winding resistance between adjacent pins (compare to service data, typically 33–56 ohms). Listen for an audible click from the EEV during startup.
5. **For U4 (transmission error)** — Measure voltage on the F1/F2 bus at the outdoor unit header — should be approximately 10–30V DC pulsing. Check all wiring terminal tightness. Use Daikin's wiring check mode if available.
6. **For L9** — Check refrigerant charge first. If charge is correct, check the inverter module power supply and output. L9 with correct charge on a newer unit suggests inverter or compressor mechanical failure.

## Parts Often Needed

| Part | Notes |
|------|-------|
| EEV coil | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-rxyq-error-codes&k=EEV+coil&tag=errorcodefixes-20) \| Removable without opening refrigerant circuit |
| F1/F2 communication wire | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-rxyq-error-codes&k=F1%2FF2+communication+wire&tag=errorcodefixes-20) \| Twisted-pair shielded; replace if damaged |
| Outdoor fan motor | [Amazon](https://www.amazon.com/dp/B0D2L5NSMM?ascsubtag=ecf-daikin-rxyq-error-codes&tag=errorcodefixes-20) \| Confirm EC or AC type for RXYQ vintage |
| Outdoor PCB (control board) | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?ascsubtag=ecf-daikin-rxyq-error-codes&tag=errorcodefixes-20) \| For L9 or L5 after other causes ruled out |
| Refrigerant (R-410A or R-32) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-rxyq-error-codes&k=Refrigerant+%28R-410A+or+R-32%29&tag=errorcodefixes-20) \| Confirm refrigerant type from unit nameplate |
| Pressure sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-rxyq-error-codes&k=Pressure+sensor&tag=errorcodefixes-20) \| High and low side; check resistance before replacing |
## When to Call a Pro

Daikin VRV systems require Daikin-certified technicians for refrigerant work, inverter diagnosis, and address configuration. The RXYQ refrigerant addressing system (using rotary switches on each indoor unit PCB) is proprietary and misconfiguration causes system-wide faults. Contact a Daikin authorized service provider for L9, L5, or multi-unit U4 faults.

## Related Articles

- [Daikin A3 Error Code — Causes & Fix](/posts/daikin-a3-error-code/)
- [Daikin Applied Chiller Fault Codes Guide — WMC / AGZ / ALZ Series](/posts/daikin-applied-fault-codes/)
- [Daikin C4 Error Code — Heat Exchanger Coil Sensor: Causes & Fix](/posts/daikin-c4-error-code/)
- [Daikin C9 Error Code — Compressor Discharge Temperature Sensor Fault](/posts/daikin-c9-error-code/)
- [Daikin E1 Error Code Fix — Indoor Sensor Fault](/posts/daikin-e1-error-code/)

## See Also

- [Daikin C4 Error Code — Indoor Heat Exchanger Thermistor Fix](/posts/daikin-error-code-c4/)
- [Daikin U3 Error Code - Causes & Fix](/posts/daikin-u3-error-code/)
- [Daikin VRV / VRF U4 Error Code — Communication Fault Fix](/posts/daikin-vrv-vrf-u4-error-code/)
- [Daikin VRV IV Fault Codes - Commercial System Diagnostic Guide](/posts/daikin-vrv-iv-fault-codes/)
