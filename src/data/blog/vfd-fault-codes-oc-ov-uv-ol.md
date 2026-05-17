---
title: "VFD Fault Codes OC, OV, UV, OL — Complete Fix Guide"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-03-16T08:00:00Z
modDatetime: 2024-03-16T08:00:00Z
slug: vfd-fault-codes-oc-ov-uv-ol
featured: false
draft: false
tags:
  - vfd
  - industrial
  - motor-control
  - electrical
  - manufacturing
description: "VFD fault codes OC (overcurrent), OV (overvoltage), UV (undervoltage), and OL (overload) are the most common drive faults. This guide covers causes and fixes for all four across ABB, Yaskawa, Danfoss, and Siemens drives."
---

## VFD Fault Codes: OC, OV, UV, and OL

**What they mean:** Variable Frequency Drives (VFDs) are the motor controllers on virtually every industrial machine — conveyors, press brakes, compressors, fans, pumps, CNC axes, injection molders. When a VFD faults, it shuts down motor output and displays a fault code. The four most common fault codes across all major VFD brands — ABB, Yaskawa, Danfoss, Siemens, and others — are:

- **OC (Overcurrent):** The drive detected output current exceeding its rated limit. The IGBT transistors in the drive are at risk. Immediate shutdown.
- **OV (Overvoltage):** The DC bus voltage inside the drive exceeded its safe operating limit (typically 800–1000V DC on a 480V drive). Usually caused by regenerative energy from decelerating loads.
- **UV (Undervoltage):** The DC bus voltage dropped below the minimum threshold (typically 400–450V DC). Usually caused by input power problems.
- **OL (Overload):** The drive's internal thermal model calculated that the motor or drive has been running at excessive current for too long. A time-current protection, not an instantaneous fault.

Note: exact fault code naming varies by brand. ABB uses "OC1," "OC2," "OC3" for different phases; Yaskawa uses "oC," "oV," "UV," "oL1"; Danfoss uses "OC," "OV," "UV," "OL." The root cause and fix are identical regardless of the specific display string.

## Common Causes by Fault Type

### OC — Overcurrent
- **Load jam or mechanical binding** — The driven load seized or jammed, pulling the motor into stall current
- **Acceleration ramp too short** — The drive is commanding too fast a ramp-up, exceeding motor current limits during start
- **Ground fault on the motor or cable** — A single-phase to ground fault presents as an overcurrent condition
- **Failed IGBT in the drive output stage** — A shorted output transistor produces massive overcurrent immediately on start

### OV — Overvoltage
- **Deceleration ramp too short** — The motor decelerates faster than the load's rotational energy can be dissipated, regenerating energy back into the DC bus
- **Load inertia too high** — High-inertia loads (large fans, flywheels) pump energy back into the bus during deceleration
- **Input overvoltage from utility** — A utility voltage spike or tap misconfiguration drives the DC bus above its limit

### UV — Undervoltage
- **Input power interruption** — Brief utility outage, blown input fuse, or tripped input breaker
- **Input voltage too low** — Running a 480V drive on 440V supply, or voltage sagging under heavy building load
- **Loose or corroded input terminals** — A high-resistance connection on the L1, L2, or L3 input terminals causes voltage drop under load

### OL — Overload
- **Motor running near full load for extended periods** — The motor is undersized for the application, or the process load has increased
- **Motor cooling insufficient** — Self-cooled motors lose cooling effectiveness at low VFD output frequencies; the motor overheats without the drive's knowledge
- **Incorrect motor nameplate parameters entered** — If rated current is set too low in the drive parameters, the overload protection trips prematurely

## Step-by-Step Fix {#step-by-step-fix}

1. **Record the full fault log before resetting.** Most modern VFDs store fault history with timestamps and the operating conditions (output frequency, current, voltage) at the time of fault. Access this via the drive's keypad menu (typically under Fault History, Diagnostics, or Event Log). This data is invaluable — a fault that occurred at startup looks different from one that occurred after 20 minutes of running.

2. **For OC faults: check the mechanical load first.** Try to rotate the driven load by hand (with the drive locked out and power isolated). The load should turn freely. Any resistance — a jammed conveyor, a seized pump, a binding brake — will cause OC on every start attempt until the mechanical issue is resolved.

3. **For OC faults: extend the acceleration ramp.** Find the acceleration time parameter in the drive (labeled Accel Time, Ramp-Up Time, or similar — parameter P1-01 in ABB, C1-01 in Yaskawa). Increase it by 50% and retry. If the OC fault moves later in the start-up sequence (or disappears), the ramp was too aggressive.

4. **For OV faults: extend the deceleration ramp.** Find the deceleration time parameter (Decel Time, Ramp-Down Time). Increase it significantly — try doubling the value first. If OV still occurs on decel, the load inertia requires either a braking resistor (to dissipate regenerative energy as heat) or a drive with built-in regenerative capability. A braking resistor is the standard solution and adds $50–$300 depending on size.

5. **For UV faults: check input power quality.** Measure AC voltage at the drive's L1, L2, L3 input terminals with a multimeter or power quality meter while the load is running. Voltage should be within ±10% of drive rated voltage. Check input fuses, circuit breakers, and terminal torque. A loose input terminal creates high resistance that drops voltage under load — a common cause of intermittent UV faults.

6. **For OL faults: verify motor parameters in the drive.** Navigate to the motor nameplate parameter group in the drive (ABB: Group 99 Motor Data; Yaskawa: E2 parameters; Danfoss: Group 1-2x Motor Data). Confirm that the rated current matches the motor nameplate exactly. An entry 10% lower than nameplate will cause premature OL trips on a correctly sized motor.

7. **Check motor temperature and cooling.** At VFD speeds below 30 Hz, self-cooled (TEFC) motors lose cooling effectiveness because the shaft-mounted cooling fan slows proportionally. If the application requires sustained low-speed operation, the motor needs an external constant-speed cooling fan or must be derated. Measure motor frame temperature with an IR gun — above 90°C surface temperature indicates a thermal problem.

8. **For persistent or recurring faults: check output wiring and motor insulation.** With the drive locked out and isolated, use a megohmmeter (megger) to test motor winding insulation from each phase to ground. Results below 1 megohm indicate degraded motor insulation — a failing motor will cause OC and OL faults intermittently before eventually failing completely.

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Description | Typical Cost | Where to Buy |
|------|------------|-------------|-------------|
| Braking resistor | OV protection for high-inertia loads | $50–$300 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-vfd-fault-codes-oc-ov-uv-ol&k=OV+protection+for+high-inertia+loads&tag=errorcodefixes-20) \| Automation Direct / Grainger |
| Input line fuses | UV/OC protection on input | $5–$25 each | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-vfd-fault-codes-oc-ov-uv-ol&k=UV%2FOC+protection+on+input&tag=errorcodefixes-20) \| Grainger / McMaster-Carr |
| Drive replacement (≤5HP) | If IGBT shorted (OC on every start) | $200–$800 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-vfd-fault-codes-oc-ov-uv-ol&k=If+IGBT+shorted+%28OC+on+every+start%29&tag=errorcodefixes-20) \| AutomationDirect / Drives Warehouse |
| External motor cooling fan | OL fix for low-speed applications | $50–$200 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-vfd-fault-codes-oc-ov-uv-ol&k=OL+fix+for+low-speed+applications&tag=errorcodefixes-20) \| Grainger / Amazon |
## When to Call a Professional

If you've extended ramps, verified motor parameters, confirmed the mechanical load is free, and the fault code still persists — the fault is likely inside the drive (failed IGBT output transistor, blown gate driver, failed DC bus capacitor) or inside the motor (shorted winding, failed bearing causing high current draw). IGBT testing requires live measurements inside the drive's power section with potentially lethal DC bus voltages present (up to 1,000V DC). This work requires a qualified industrial electrician or drive service technician. Most drive manufacturers have authorized service centers that can bench-test drives and perform IGBT module replacement at substantially less cost than a new drive.

> **Pro tip:** After any VFD fault and reset, don't immediately return to normal operation — watch the first 5 minutes of running carefully. A fault that recurrs within the first 5 minutes at the same operating point means the root cause was not addressed. A fault that appears only after 30+ minutes of running usually points to a thermal issue (OL or OC from motor heating), not a parameter or mechanical problem. The timing of fault recurrence is one of the most useful diagnostic data points a technician has.

## Related Articles

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS310 Fault 3130 — Causes & Fix](/posts/abb-acs310-fault-3130/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)
