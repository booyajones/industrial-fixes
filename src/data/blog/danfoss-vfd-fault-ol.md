---
title: "Danfoss VFD Fault OL — Causes & Fix"
description: "What Danfoss VFD fault OL means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T09:00:00Z
modDatetime: 2026-04-22T09:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Larger frame motor"
---

## Danfoss VFD Fault OL — What It Means

Danfoss VFD fault OL (Motor Overload) indicates that the drive's electronic thermal overload protection tripped. The drive monitors the product of output current and time using an inverse-time thermal model (the motor's I²t curve), and when the calculated motor temperature exceeds 100% of the motor thermal rating, it trips OL. This protection is programmed to match the motor's thermal class (parameter 1-90 on VLT FC series drives) and protects the motor from overheating when the motor doesn't have internal thermistors connected. OL is distinct from drive overcurrent faults — it's a sustained moderate overload, not an instantaneous spike.

[Jump to Fix](#fix)

## Common Causes

- **Mechanical overload on the driven equipment** — The pump, fan, or conveyor is drawing more torque than expected due to increased process resistance, material buildup, bearing wear, or a blocked inlet.
- **Motor parameters not matched to motor nameplate** — If the motor current rating (parameter 1-24) is set higher than the actual motor nameplate FLA, the thermal model allows more current than the motor can safely handle before tripping OL.
- **Undersized motor for the application** — The motor is genuinely running at or above its rated current for the given load. The application requires a larger motor frame.
- **High ambient temperature at motor** — The motor's rated current assumes a standard ambient (typically 40°C). In a high-temperature location, the motor's thermal capacity is reduced and the drive's overload model may underestimate actual motor temperature.

## Step-by-Step Fix {#fix}

1. **Check drive output current during normal operation** — Navigate to the monitoring display (Live List or Quick Menu on VLT drives). Check the actual motor current (parameter 16-12) during normal operation. Compare to the motor nameplate FLA. Running above 100% FLA continuously will trip OL.
2. **Verify motor nameplate parameters in the drive** — Check parameters 1-20 (Motor Power), 1-22 (Motor Voltage), 1-23 (Motor Frequency), 1-24 (Motor Current), and 1-25 (Motor Speed). All must match the motor nameplate exactly for the thermal model to work correctly.
3. **Inspect the driven load** — Check for mechanical binding, material buildup on impellers or conveyor, or increased process resistance. Disconnect the load and test motor no-load current if needed.
4. **Increase the OL warning threshold if application requires** — On Danfoss VLT drives, parameter 1-90 (Motor Thermal Protection) allows adjusting how aggressively thermal protection is applied. Only increase this value if the motor is genuinely rated for continuous operation at the running current.
5. **Let the drive and motor cool, then reset** — After the thermal fault, the drive won't allow restart until the motor thermal model cools below the reset threshold. This is automatic and proportional to the overload magnitude.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Larger frame motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-vfd-fault-ol&k=Larger+frame+motor&tag=errorcodefixes-20) \| Required if load genuinely exceeds motor rating |
| Load-side bearings or impeller | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-vfd-fault-ol&k=Load-side+bearings+or+impeller&tag=errorcodefixes-20) \| Clean or replace if mechanical drag is the root cause |
| Motor PTC thermistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-vfd-fault-ol&k=Motor+PTC+thermistor&tag=errorcodefixes-20) \| Wire into the drive's thermistor input for actual motor temperature feedback |
## When to Call a Pro

If the motor current is within nameplate rating, parameters are correct, and OL trips anyway, the motor may have developing insulation problems that reduce effective winding cross-section and increase running temperature. A motor insulation test and current analysis by an electrical contractor will confirm this.

## Related Articles

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS310 Fault 3130 — Causes & Fix](/posts/abb-acs310-fault-3130/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)

## See Also

- [Danfoss VLT Alarm 14 - Earth Fault: What It Means and How to Fix It](/posts/danfoss-vlt-alarm-14/)
- [Danfoss VFD Fault OCL — Causes & Fix](/posts/danfoss-vfd-fault-ocl/)
- [Danfoss VFD Fault Codes — FC301, FC302, FC102 Reference](/posts/danfoss-vfd-fault-codes/)
- [Danfoss VFD Fault E-Trip — Causes & Fix](/posts/danfoss-vfd-fault-e-trip/)
