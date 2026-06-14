---
title: "Lenze SMD Fault 0x0001 — Overcurrent"
description: "Lenze SMD fault 0x0001 means overcurrent on the drive output. Learn the common causes, parameter checks, and repair steps."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - lenze
  - smd
  - overcurrent
money_part: "VFD-rated motor cable"
most_likely_cause: "Acceleration time is too short"
---

## Lenze SMD Fault 0x0001 — What It Means

**Fault 0x0001** on a Lenze SMD drive means the inverter detected **overcurrent** on the output stage. This usually happens during startup, acceleration, or a sudden load change. The drive trips immediately to protect the IGBTs.

[Jump to Fix](#fix)

## Common Causes

- **Acceleration time is too short**. The motor demands more current than the drive can deliver during ramp-up.
- **Motor or load is mechanically jammed**. A stalled load produces very high current instantly.
- **Output short or motor winding fault**. Damaged motor leads or grounded windings look like overcurrent.
- **Motor data is programmed incorrectly**. Wrong voltage, frequency, or current values distort control.
- **Failed output transistor**. If the drive faults instantly with the motor disconnected, suspect internal IGBT damage.

## Step-by-Step Fix {#fix}

1. **Increase acceleration time** in the Lenze parameter menu. If the trip happens during ramp-up, double the accel time first.
2. **Check the mechanical load**. Rotate the shaft by hand with power off. Any binding or jam must be fixed before resetting.
3. **Disconnect the motor and megger it**. Measure each phase to ground. Below 1 MΩ means the motor or cable has an insulation failure.
4. **Verify motor nameplate parameters** in the drive. Voltage, full-load amps, and base frequency must match.
5. **Check the output stage**. If the drive trips with the motor disconnected, the output transistors are likely damaged.
6. **Test with no load** if the application allows. If the fault disappears unloaded, the driven machine is the problem.

## Parts Often Needed

| Part | Notes |
|------|-------|
| VFD-rated motor cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lenze-smd-fault-0x0001&k=VFD-rated+motor+cable&tag=errorcodefixes-20) \| Replace damaged output cable |
| Motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lenze-smd-fault-0x0001&k=Motor&tag=errorcodefixes-20) \| Replace if windings are shorted or grounded |
| Lenze SMD drive | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lenze-smd-fault-0x0001&k=Lenze+SMD+drive&tag=errorcodefixes-20) \| Replace if output stage is failed |
## When to Call a Pro

If you have correct parameters, a free-turning load, and a clean megger test but 0x0001 still occurs, the drive itself is probably damaged internally.

## Related Articles

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS310 Fault 3130 — Causes & Fix](/posts/abb-acs310-fault-3130/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)
