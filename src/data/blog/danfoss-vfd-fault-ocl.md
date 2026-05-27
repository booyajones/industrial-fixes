---
title: "Danfoss VFD Fault OCL — Causes & Fix"
description: "What Danfoss OCL means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T08:00:00Z
modDatetime: 2026-04-22T08:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - danfoss
---

## Danfoss VFD Fault OCL — What It Means

Danfoss fault OCL (Overcurrent Limit) means the drive's output current reached the current limit threshold and the drive reduced output frequency to limit current. Unlike a hard OC trip that shuts the drive down immediately, OCL is a current-limiting intervention where the drive actively throttles output to stay within the current limit. On Danfoss FC301, FC302, and VLT series drives, OCL appears as a warning (not always a full trip) indicating the motor is consistently running at or near its current limit. If the condition is sustained, the drive may eventually trip on TRIP (motor thermal) or OC depending on configuration.

[Jump to Fix](#fix)

## Common Causes

- **Mechanical overload** — A pump fighting against high head pressure, a conveyor with excess load, or a fan with a dirty filter all force the motor to draw more current than normal and push the drive into OCL.
- **Acceleration ramp too fast** — If acceleration time is too short for the connected load inertia, the drive hits current limit during every startup sequence.
- **Motor current limit parameter set too low** — Parameter 4-16 (Motor Speed High Limit) or 4-18 (Current Limit) in the FC300 series may be set below the motor's rated current, causing frequent OCL.
- **Incorrect motor data** — If motor nameplate data (rated current, voltage, frequency) isn't entered correctly, the drive's internal model miscalculates limits and OCL appears at loads that shouldn't trigger it.

## Step-by-Step Fix {#fix}

1. **Check the mechanical load** — Inspect the driven equipment for signs of increased resistance: pump impeller clogging, belt tension, conveyor jam, fan blade buildup. Reduce the load and test.
2. **Verify motor data parameters** — Navigate to parameter group 1-2x (Motor Data). Confirm rated voltage, frequency, current, and power match the motor nameplate exactly. Run an AMA (Automatic Motor Adaptation) to calibrate.
3. **Increase acceleration time** — In parameter 3-41 (Ramp 1 Ramp-up Time), increase the value until the drive accelerates without hitting OCL. For high-inertia loads, acceleration times of 10–30 seconds are normal.
4. **Check current limit setting** — Verify parameter 4-18 (Current Limit) is set appropriately — typically 110–150% of motor rated current for most applications.
5. **Reset the system** — After parameter corrections, reset any active alarms and restart. Monitor output current during acceleration and at steady state.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor (oversized replacement) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-vfd-fault-ocl&k=Motor+%28oversized+replacement%29&tag=errorcodefixes-20) \| If the application genuinely needs more torque than the current motor can provide |
| VFD (larger frame) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-vfd-fault-ocl&k=VFD+%28larger+frame%29&tag=errorcodefixes-20) \| If the existing drive is undersized for the actual load current |
| Line filter/reactor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-vfd-fault-ocl&k=Line+filter%2Freactor&tag=errorcodefixes-20) \| Won't fix OCL but reduces electrical stress if OCL is marginal |
## When to Call a Pro

If OCL persists after correct motor data entry and appropriate ramp times, the application may require a detailed load analysis and a properly matched motor/drive combination — a job for a drives application engineer.

## Related Articles

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS310 Fault 3130 — Causes & Fix](/posts/abb-acs310-fault-3130/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)

## See Also

- [Danfoss FC-302 Alarm 13 — DC Link Overvoltage Fix](/posts/danfoss-fc302-alarm-13/)
- [Danfoss VLT Alarm 14 - Earth Fault: What It Means and How to Fix It](/posts/danfoss-vlt-alarm-14/)
- [Danfoss RX Controller Fault Codes — Troubleshooting Guide](/posts/danfoss-rx-controller-fault/)
- [Danfoss FC-302 Alarm 12 — Overcurrent Fix](/posts/danfoss-fc302-alarm-12/)
