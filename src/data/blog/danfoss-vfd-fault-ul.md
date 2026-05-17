---
title: "Danfoss VFD Fault UL — Causes & Fix"
description: "What Danfoss VFD fault UL means, why underload trips the drive, and how to fix it."
pubDatetime: 2026-04-22T10:00:00Z
modDatetime: 2026-04-22T10:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - danfoss
---

## Danfoss VFD Fault UL — What It Means

Fault UL (Underload) on a Danfoss FC series drive (FC102, FC202, FC302) indicates that the motor is drawing significantly less current than expected for the commanded speed and load. This is a process protection fault — the drive's underload curve detected that the mechanical load has dropped below the configured threshold, which typically signals a process problem: a broken belt on a fan or pump, pump cavitation, a conveyor chain that has snapped, or an empty hopper on a mixer.

[Jump to Fix](#fix)

## Common Causes

- **Broken or slipped drive belt** — A fan or pump driven by a V-belt loses its mechanical connection; the motor spins freely at low torque while the driven equipment does not move.
- **Pump cavitation** — A pump that has lost prime or is running against a closed valve cavitates — the impeller spins in vapor rather than liquid, dramatically reducing torque requirement.
- **Broken coupling or shaft** — A failed flexible coupling or sheared shaft key on the motor decouples it from the driven load.
- **Underload parameters set too aggressively** — Parameters 37-01 (Underload function) and 37-04 (Minimum motor current) configured with thresholds too close to the actual loaded operating point cause nuisance UL faults.

## Step-by-Step Fix {#fix}

1. **Inspect the driven equipment** — Before touching the drive, physically inspect the driven load. Check the drive belt for breakage or slippage. Check the coupling. Confirm the pump/fan is mechanically connected to the motor.
2. **Check pump prime** — For centrifugal pump applications, confirm the pump has prime and that all isolation valves are open. Reprime the pump if cavitation is suspected.
3. **Review the underload parameters** — Access the Danfoss parameter set (par 37-01 through 37-06). If the underload function is enabled, verify the trip delay (37-02) and the warning/trip threshold (37-04) are appropriate for the application. Increase the warning delay to filter transient low-load events.
4. **Compare actual vs. expected current** — Monitor the drive's output current display (par 16-14) during normal operation. Compare to the motor's rated current at the operating speed. Underload is indicated by current more than 20–30% below the expected loaded value.
5. **Clear the fault and restart** — Once the mechanical cause is corrected (belt replaced, pump primed), reset the UL fault via the LCP display (Reset key) or digital input and restart.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Drive belt (V-belt or synchronous) | [Amazon](https://www.amazon.com/s?i=industrial&k=Drive+belt+%28V-belt+or+synchronous%29&tag=errorcodefixes-20) \| Match pitch and length to OEM specification |
| Flexible coupling insert | [Amazon](https://www.amazon.com/s?i=industrial&k=Flexible+coupling+insert&tag=errorcodefixes-20) \| Replace spider/element if coupling is used |
| Pump foot valve or check valve | [Amazon](https://www.amazon.com/s?i=industrial&k=Pump+foot+valve+or+check+valve&tag=errorcodefixes-20) \| If pump repeatedly loses prime |
## When to Call a Pro

If UL trips after belt replacement or pump priming and no mechanical fault is visible, have a process engineer review the system design. Recurring cavitation indicates undersized pump, incorrect speed setting, or system curve mismatch.

## Related Articles

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS310 Fault 3130 — Causes & Fix](/posts/abb-acs310-fault-3130/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)
