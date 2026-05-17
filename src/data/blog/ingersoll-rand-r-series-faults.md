---
title: "Ingersoll-Rand R-Series Compressor Fault Codes: Complete Guide"
description: "Ingersoll-Rand R-Series rotary screw compressor fault codes and diagnostics. Fault codes, causes, and technician-level troubleshooting."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-05-01T08:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - compressor
  - ingersoll-rand
  - industrial
---

# Ingersoll-Rand R-Series Compressor Fault Codes

Ingersoll-Rand R-Series rotary screw compressors (R7.5–R90) use the Intellisys® controller for monitoring and fault management. Faults display on the Intellisys panel as text messages. The controller logs fault history with timestamps and run hours.

## R-Series Fault Code Table

| Fault | Fault Description | Common Cause | Action |
|-------|------------------|--------------|--------|
| HIGH TEMP | High discharge temperature | Cooler dirty, low oil, high ambient | Clean cooler, check oil level |
| HIGH TEMP WARN | Temperature warning | Approaching shutdown threshold | Pre-clean cooler before shutdown |
| STAR DELTA FAULT | Starter transition fault | Contactor or timing issue | Check starter sequence |
| OVERLOAD | Motor overload trip | Motor overload or high current | Check motor amps and load |
| HIGH PRESSURE | Discharge pressure too high | Excessive demand or closed valve | Check discharge valve |
| LOW INLET PRESSURE | Inlet filter restricted | Dirty inlet filter | Replace inlet air filter |
| OIL FAULT | Low oil pressure | Low oil, failed oil pump | Check oil level and pump |
| PHASE FAULT | Phase loss or imbalance | Supply fault | Check input voltage |
| EMERGENCY STOP | E-stop activated | E-stop button pressed | Check E-stop circuit |
| SERVICE LEVEL 1 | Preventive maintenance due | Hours elapsed | Perform scheduled PM |
| SERVICE LEVEL 2 | Major PM due | Major service interval | Perform major PM |
| SENSOR FAULT | Temperature sensor failure | Failed thermistor | Replace temperature sensor |
| DRAIN FAULT | Auto-drain failure | Solenoid drain valve stuck | Check drain valve operation |

## Most Common R-Series Faults

### HIGH TEMP — High Discharge Temperature
Ingersoll-Rand R-Series maximum discharge temperature is typically 235°F (113°C) for standard models. High temp shutdowns are almost always caused by dirty oil coolers or dirty air coolers. Blow cooler fins with low-pressure air or wash with coil cleaner. Check oil level with the unit loaded and running.

### OVERLOAD — Motor Overload
Check three-phase supply voltage and balance. A 5% voltage imbalance can cause 25%+ current imbalance. Reset the overload relay after determining the cause. Check unloader operation — if the unit is starting under load, motor current is excessive on startup.

### LOW INLET PRESSURE — Inlet Filter
Ingersoll-Rand R-Series inlet filters have a differential pressure switch that triggers this alarm when restriction is excessive. Check filter element — replace at the service interval or when restriction is detected. Do not operate the compressor with a dirty filter; accelerated airend wear results.

### SERVICE LEVEL 1/2
The Intellisys controller tracks service intervals by run hours. Level 1 is typically the oil filter and separator element interval (every 2,000 hours). Level 2 is the major service interval (airend inspection, oil change, full filter replacement). Perform maintenance and reset the service timer in the Intellisys menu.

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| Inlet air filter | [Amazon](https://www.amazon.com/dp/B0CLBFXLYJ?ascsubtag=ecf-ingersoll-rand-r-series-faults&tag=errorcodefixes-20) \| Replace at scheduled interval |
| Oil filter element | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-ingersoll-rand-r-series-faults&k=Oil+filter+element&tag=errorcodefixes-20) \| IR-specific — match model |
| Oil separator element | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-ingersoll-rand-r-series-faults&k=Oil+separator+element&tag=errorcodefixes-20) \| Replace at Level 2 interval |
| Compressor oil | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-ingersoll-rand-r-series-faults&k=Compressor+oil&tag=errorcodefixes-20) \| IR synthetic — model-specific |
| Auto-drain solenoid valve | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-ingersoll-rand-r-series-faults&k=Auto-drain+solenoid+valve&tag=errorcodefixes-20) \| Check for stuck-open or stuck-closed |
| Temperature sensor | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-ingersoll-rand-r-series-faults&tag=errorcodefixes-20) \| Match Intellisys controller input type |
> **Pro tip:** Ingersoll-Rand Intellisys controllers on networked compressor rooms can be monitored remotely via the IR Connect app. Fault alerts can be sent to maintenance personnel by email or text, enabling faster response to high-temperature events before the compressor shuts down.

## Related Articles

- [Air Compressor Fault Codes: Complete Guide](/posts/air-compressor-fault-codes/)
- [Atlas Copco Air Compressor Fault Codes — Complete Guide](/posts/atlas-copco-compressor-fault-codes/)
- [BOGE Air Compressor Error Codes - Complete Guide](/posts/boge-compressor-error-codes/)
- [Chicago Pneumatic Compressor Fault Codes — Complete Guide](/posts/chicago-pneumatic-compressor-faults/)
- [CompAir Air Compressor Fault Codes - Complete Guide](/posts/compair-compressor-fault-codes/)
