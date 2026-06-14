---
title: "ABB ACS580 A2A1 - Causes & Fix"
description: "A2A1 on the ABB ACS580 is an informative warning for current calibration, not a trip fault. Learn what it means and how to clear it."
pubDatetime: 2026-05-26T21:46:55Z
modDatetime: 2026-05-26T21:46:55Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - abb
money_part: "Motor cable (if damaged during separate troubleshooting)"
most_likely_cause: "Requested ID run or calibration"
---

## ABB ACS580 A2A1 — What It Means

A2A1 (auxiliary code 2281) on an ABB ACS580 is not a trip fault. It is an informative warning that tells you current offset and gain measurement calibration will occur at the next drive start. ABB classifies this as a normal calibration message, not evidence of a failed power stage, motor, or wiring problem.

The drive has been commanded or configured to perform a current measurement calibration, typically as part of commissioning, an ID run sequence, or after certain parameter changes. You will see this message appear before the drive completes its calibration at the next startup. It does not indicate overcurrent, earth fault, or motor damage on its own.

[Jump to Fix](#fix)

## Common Causes

- **Requested ID run or calibration** The drive was configured to perform an identification run or current calibration through the commissioning parameters (such as parameter 99.13 ID run requested).
- **Recent parameter changes** Motor or drive parameters were modified and the control unit flagged a need to recalibrate current measurements at the next start.
- **Commissioning sequence** The drive is in a startup or recommissioning workflow where ABB's current offset and gain calibration is part of the normal initialization.
- **Power cycle after configuration** The drive was powered down after a setup change and the warning persists until the calibration completes on the next run.

## Step-by-Step Fix {#fix}

1. Confirm the code is A2A1 and verify it is listed as an informative warning, not a trip fault, in the drive display or event log.
2. Check commissioning parameters to see if an ID run or current calibration was intentionally requested (review parameter 99.13 and related startup settings).
3. Cycle power or start the drive normally so it can perform the current offset and gain calibration at the next start as ABB specifies.
4. Monitor the display after startup to confirm the A2A1 warning clears once calibration completes.
5. Review recent parameter changes or startup sequences if the message returns unexpectedly after the first calibration cycle.
6. If you suspect a separate motor or wiring issue (unrelated to A2A1), disconnect the motor cable from the drive and measure insulation resistance of the motor and cable using 1000 V DC (ABB specifies motor insulation must be more than 100 MΩ at 25 °C for reference).
7. Consult the ACS580 fault code list to rule out nearby current or earth fault codes (A2B1, A2B3, A2B4) if other symptoms appear alongside the A2A1 warning.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor cable (if damaged during separate troubleshooting) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-a2a1-fault-code&k=Motor+cable+%28if+damaged+during+separate+troubleshooting%29&tag=errorcodefixes-20) \| Only replace if insulation testing reveals a fault unrelated to the A2A1 calibration warning. |
| ABB ACS580 control unit or electronics board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-a2a1-fault-code&k=ABB+ACS580+control+unit+or+electronics+board&tag=errorcodefixes-20) \| Only needed if calibration fails repeatedly and ABB service identifies a current measurement circuit defect (not typical for A2A1). |

## When to Call a Pro

Call a qualified technician or ABB service if the A2A1 warning does not clear after a normal startup cycle, if calibration fails repeatedly, or if new fault codes appear alongside A2A1. Also call if you are unfamiliar with drive commissioning parameters or if you need to perform an insulation resistance test on the motor and cable. A persistent A2A1 that returns after every power cycle may indicate a parameter configuration issue or a rare current measurement circuit problem that requires factory support or a control board replacement.

## See Also

- [ABB Inverter Fault Code F0001 - Causes & Fix](/posts/abb-inverter-fault-code-f0001/)
- [ABB ACS580 Fault 3210 — DC Overvoltage Fix](/posts/abb-acs580-fault-3210/)
- [ABB VFD Fault 5010 — Causes & Fix](/posts/abb-vfd-fault-5010/)
- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
