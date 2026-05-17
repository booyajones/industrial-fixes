---
title: "Kaeser SIGMA CONTROL 2 Fault Codes: Complete Guide"
description: "Kaeser SIGMA CONTROL 2 fault codes and diagnostics. Compressor warnings, shutdowns, causes, and technician-level troubleshooting."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-05-01T08:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - compressor
  - kaeser
  - industrial
---

# Kaeser SIGMA CONTROL 2 Fault Codes

Kaeser compressors with SIGMA CONTROL 2 (second generation) use text-based alarm messages displayed on the controller panel. The SIGMA CONTROL 2 provides more detail and connectivity than the original Sigma Control, including Ethernet integration and remote monitoring via SIGMA NETWORK.

## SIGMA CONTROL 2 Fault Reference

| Alarm Message | Category | Common Cause | Action |
|--------------|----------|--------------|--------|
| Final compression temp — Warning | Warning | Approaching high temp limit | Clean coolers, check oil |
| Final compression temp — Shutdown | Shutdown | Excessive temperature | Clean coolers, check oil, check ambient |
| Motor protection — Shutdown | Shutdown | Motor overload | Check motor amps and load |
| Emergency stop — Active | Shutdown | E-stop circuit open | Check all E-stop switches |
| Pressure sensor — Fault | Warning | Failed pressure transducer | Check sensor wiring and signal |
| Temperature sensor — Fault | Warning | Failed temperature sensor | Check sensor resistance |
| Dryer — Fault | Warning | Integrated dryer alarm | Check refrigerant dryer operation |
| Service — Required | Maintenance | Service interval reached | Perform scheduled service |
| Fan motor — Fault | Shutdown | Cooling fan motor fault | Check fan motor amps and contactor |
| Condensate drain — Fault | Warning | Drain solenoid not operating | Check drain solenoid and timer |
| Oil filter — Service | Maintenance | Oil filter replacement due | Replace oil filter element |
| Differential pressure — High | Warning | Separator element clogged | Replace separator element |
| Communication — Fault | Warning | Network communication loss | Check Ethernet and network config |
| Phase — Fault | Shutdown | Phase loss or reversal | Check input power quality |

## Most Common SIGMA CONTROL 2 Faults

### Final Compression Temp — Shutdown
Kaeser's shutdown threshold is typically 110°C (230°F). Warning precedes shutdown by approximately 5°C. Root cause is almost always a dirty cooler. Kaeser SIGMA CONTROL 2 logs the temperature trend — review to see if temp is climbing progressively or suddenly.

### Dryer Fault
On packages with integrated refrigerated dryer, the SIGMA CONTROL 2 monitors dryer operation. Dryer fault triggers if the dryer controller generates an alarm. Check the dryer controller (separate display inside the package) for a specific fault. Common: dryer refrigerant pressure alarm, condenser fan fault, or high pressure dewpoint.

### Service Required
SIGMA CONTROL 2 tracks service intervals by operating hours. Service due alerts appear in advance of the actual service interval (configurable, typically 100 hours before). Perform Kaeser-specified maintenance and reset the service counter in the SIGMA CONTROL 2 menu (requires service password).

### Communication Fault
SIGMA CONTROL 2 supports Modbus, PROFIBUS, PROFINET, and Ethernet. A communication fault means the controller cannot communicate with the BMS, master controller, or SIGMA NETWORK. Check network cable connections and verify IP address configuration.

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| Oil separator element | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-kaeser-sigma-control-faults&k=Oil+separator+element&tag=errorcodefixes-20) \| Kaeser-specific — match model |
| Oil filter element | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-kaeser-sigma-control-faults&k=Oil+filter+element&tag=errorcodefixes-20) \| Match package model |
| Pressure transducer | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-kaeser-sigma-control-faults&k=Pressure+transducer&tag=errorcodefixes-20) \| Check signal output (typically 4–20 mA) |
| Temperature sensor | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-kaeser-sigma-control-faults&tag=errorcodefixes-20) \| NTC thermistor — check resistance |
| Condensate drain solenoid | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-kaeser-sigma-control-faults&k=Condensate+drain+solenoid&tag=errorcodefixes-20) \| Match voltage and orifice size |
| Fan motor contactor | [Amazon](https://www.amazon.com/dp/B0D2L5NSMM?ascsubtag=ecf-kaeser-sigma-control-faults&tag=errorcodefixes-20) \| Check contact condition |
> **Pro tip:** Kaeser SIGMA CONTROL 2 can be connected to SIGMA NETWORK for remote monitoring. Kaeser service centers can remotely access fault logs and performance data. Register the compressor on SIGMA NETWORK to enable predictive maintenance alerts.

## Related Articles

- [Air Compressor Fault Codes: Complete Guide](/posts/air-compressor-fault-codes/)
- [Atlas Copco Air Compressor Fault Codes — Complete Guide](/posts/atlas-copco-compressor-fault-codes/)
- [BOGE Air Compressor Error Codes - Complete Guide](/posts/boge-compressor-error-codes/)
- [Chicago Pneumatic Compressor Fault Codes — Complete Guide](/posts/chicago-pneumatic-compressor-faults/)
- [CompAir Air Compressor Fault Codes - Complete Guide](/posts/compair-compressor-fault-codes/)
