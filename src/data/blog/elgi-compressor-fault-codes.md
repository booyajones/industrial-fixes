---
title: "ELGi Air Compressor Fault Codes Guide — Troubleshooting Alarms"
description: "ELGi air compressor fault codes for EG, EN, and AB series: alarms, shutdown causes, and troubleshooting steps for rotary screw and reciprocating compressors."
pubDatetime: 2026-04-22T21:00:00Z
modDatetime: 2026-04-22T21:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - compressor
  - elgi
  - industrial
---

## ELGi Compressor Fault Codes — Quick Reference

ELGi compressors (EG, EN, AB series) use an electronic controller that monitors temperature, pressure, motor current, and maintenance intervals. Alarm messages appear on the display with a fault description and recommended action.

| Fault | Meaning | Quick Fix |
|-------|---------|-----------|
| High Discharge Temperature | Air end outlet temp exceeded | Check oil, cooler, fan |
| High Oil Temperature | Oil circuit too hot | Clean oil cooler, check oil level |
| Low Oil Pressure | Oil pressure dropped below setpoint | Check oil level and filter |
| Motor Overload | Motor drew excess current | Check voltage and demand |
| High Pressure | System pressure above limit | Check pressure switch and unloader |
| Air/Oil Separator Choked | Separator element restricted | Replace separator element |
| Sensor Failure | Temp or pressure sensor fault | Inspect sensor and harness |
| Service Required | Scheduled PM due | Perform PM and reset counter |

## Most Common Faults

### High Discharge Temperature
ELGi compressors are known for robust cooling systems but they still trip on high discharge temp when oil is low, coolers are dirty, or ambient temperature is excessive. Begin with the oil sight glass — ensure oil is at the correct level when the machine is stopped. Clean the oil cooler core with compressed air.

### Air/Oil Separator Choked
The separator element removes oil droplets from compressed air. As it loads up with oil and debris, the differential pressure across it rises. When the DP exceeds the setpoint (usually around 10 psi), the controller alarms. Replace the element — do not simply reset and continue.

### Low Oil Pressure
Check oil level first. Then check the oil filter — a clogged filter on initial cold startup can drop pressure before oil flow is established. If oil level and filter are fine, inspect the oil pressure sensor and wiring.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Oil separator element | [Amazon](https://www.amazon.com/s?k=Oil+separator+element&tag=errorcodefixes-20) \| Main periodic wear item |
| Oil filter | [Amazon](https://www.amazon.com/s?k=Oil+filter&tag=errorcodefixes-20) \| Replace with separator service |
| Temperature sensor | [Amazon](https://www.amazon.com/s?k=Temperature+sensor&tag=errorcodefixes-20) \| Common after heat cycling |
| Cooling fan contactor | [Amazon](https://www.amazon.com/s?k=Cooling+fan+contactor&tag=errorcodefixes-20) \| Check on temp-related faults |
## Jump to Fix

- **High discharge temp** → Verify oil level → Clean cooler → Check fan
- **Separator choked** → Replace element → Reset alarm
- **Low oil pressure** → Check oil level → Replace filter → Inspect sensor

## When to Call a Pro
ELGi has a global dealer network. If faults persist after parts replacement, contact an ELGi authorized service center for airend diagnostics and controller configuration checks.

## Related Articles

- [Air Compressor Fault Codes: Complete Guide](/posts/air-compressor-fault-codes/)
- [Atlas Copco Air Compressor Fault Codes — Complete Guide](/posts/atlas-copco-compressor-fault-codes/)
- [BOGE Air Compressor Error Codes - Complete Guide](/posts/boge-compressor-error-codes/)
- [Chicago Pneumatic Compressor Fault Codes — Complete Guide](/posts/chicago-pneumatic-compressor-faults/)
- [CompAir Air Compressor Fault Codes - Complete Guide](/posts/compair-compressor-fault-codes/)
