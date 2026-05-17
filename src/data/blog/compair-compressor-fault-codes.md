---
title: "CompAir Air Compressor Fault Codes - Complete Guide"
description: "CompAir rotary screw compressor fault codes and alarms: causes, diagnostic steps, and repair guidance for L, D, and B series."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - compressor
  - compair
  - industrial
---

## CompAir Compressor Fault Codes - Quick Reference

CompAir (Gardner Denver brand) rotary screw compressors use the Delcos XL and Delcos Pro controllers on L, D, and B series machines. Alarms fall into warnings (continue running) and shutdowns (compressor stops).

| Fault | Meaning | Quick Fix |
|-------|---------|-----------|
| High Discharge Temp | Air/oil temperature exceeded | Check cooler, oil level, fan |
| Low Oil Level | Oil level sensor triggered | Add oil, check for leaks |
| Motor Overload | Motor current too high | Check phases, load, voltage |
| High Pressure | System pressure exceeded set point | Check pressure relief, regulator |
| E-Stop | Emergency stop circuit open | Reset E-stop, inspect wiring |
| Service Due | Maintenance interval reached | Perform PM, reset counter |
| Oil Separator DP High | Separator restricted | Replace separator element |
| Sensor Fault | Sensor signal out of range | Check sensor and wiring |
| Phase Fault | Phase loss or imbalance | Check supply voltage |
| Blowdown Valve | Valve not operating correctly | Inspect valve actuator |

## Most Common Faults

### High Discharge Temperature
Clean the cooler bundle and verify fan operation first. CompAir oil coolers are often cooled by a fan driven by the main motor belt or a separate motor - check that the fan runs at full speed. Also check oil type and level; synthetic oil is strongly preferred.

### Oil Separator DP High
Separator element typically needs replacement every 2,000–6,000 hours depending on operating conditions. Running dusty environments accelerates clogging. A blocked separator increases energy consumption and causes oil carryover into the air system.

### Phase Fault
CompAir machines are sensitive to supply voltage quality. Missing phase, voltage imbalance above 3%, or frequent dips trigger this fault. Verify at the incoming terminal block under load, not just at the disconnect.

### Motor Overload
Check current draw on all three phases with a clamp meter. Unbalanced loading, incorrect motor rotation on initial setup, or a sticking inlet valve can all cause nuisance overloads.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Oil separator element | [Amazon](https://www.amazon.com/s?i=industrial&k=Oil+separator+element&tag=errorcodefixes-20) \| Main PM part |
| Air filter element | [Amazon](https://www.amazon.com/dp/B0CLBFXLYJ?tag=errorcodefixes-20) \| Replace per service schedule |
| Oil filter cartridge | [Amazon](https://www.amazon.com/s?i=industrial&k=Oil+filter+cartridge&tag=errorcodefixes-20) \| Replace with separator |
| Temperature sensors (NTC) | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?tag=errorcodefixes-20) \| Common fault after heat cycles |
| Inlet valve repair kit | [Amazon](https://www.amazon.com/s?i=industrial&k=Inlet+valve+repair+kit&tag=errorcodefixes-20) \| Sticking causes overloads |
## When to Call a Pro
If the compressor shuts down on high temperature after cooler cleaning and oil service, suspect airend discharge valve or screw wear. CompAir airend rebuilds require factory tooling and specifications.

## Related Articles

- [Air Compressor Fault Codes: Complete Guide](/posts/air-compressor-fault-codes/)
- [Atlas Copco Air Compressor Fault Codes — Complete Guide](/posts/atlas-copco-compressor-fault-codes/)
- [BOGE Air Compressor Error Codes - Complete Guide](/posts/boge-compressor-error-codes/)
- [Chicago Pneumatic Compressor Fault Codes — Complete Guide](/posts/chicago-pneumatic-compressor-faults/)
- [Copeland Compressor Error Code 1 — High Pressure Cutout Fix](/posts/copeland-compressor-error-code-1/)
