---
title: "Yaskawa GA800 E02 Fault - Causes & Fix"
description: "Yaskawa GA800 E02 (Er-02) is a minor fault caused by incorrect motor data during Auto-Tuning. Fix by verifying nameplate data and rerunning tuning."
pubDatetime: 2026-05-30T12:22:18Z
modDatetime: 2026-05-30T12:22:18Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Motor power cable (3-phase shielded)"
most_likely_cause: "Incorrect motor nameplate data entered during Auto-Tuning"
---

## Yaskawa GA800 E02 Fault — What It Means

The E02 (also displayed as Er-02) fault on a Yaskawa GA800 drive is a minor fault triggered when incorrect motor data has been entered during the Auto-Tuning process. Auto-Tuning is the drive's procedure for learning the electrical characteristics of the connected motor, and if the nameplate parameters you input do not match the actual motor, the drive cannot complete tuning successfully and throws this code.

This fault is typically recoverable by correcting the motor parameter entries and rerunning the Auto-Tuning sequence. It does not usually indicate a hardware failure in the drive itself, though wiring problems or mechanical overload can also prevent successful tuning and produce the same code.

[Jump to Fix](#fix)

## Common Causes

- **Incorrect motor nameplate data entered during Auto-Tuning** Voltage, current, frequency, or horsepower values typed into the drive do not match the actual motor plate, preventing the drive from accurately learning motor characteristics.
- **Faulty wiring or loose connections** Open circuits, corroded terminals, or defective cable connections between the drive output and motor can interrupt Auto-Tuning and trigger the fault.
- **Mechanical load too heavy or binding** Excessive load, seized bearings, or mechanical obstruction prevents the motor from responding normally during the tuning cycle, causing the drive to fault out.
- **Incompatible motor type for the drive settings** The connected motor does not match the drive's configured control mode or motor type selection, leading to tuning failure.

## Step-by-Step Fix {#fix}

1. {'lead': 'Press RESET on the keypad', 'text': 'while the E02 fault code is displayed to clear the fault and prepare the drive for parameter correction.'}
2. {'lead': 'Verify motor nameplate data', 'text': "against the values entered in the drive's motor parameters (voltage, current, frequency, horsepower, and rated speed). Correct any discrepancies in the drive's parameter list."}
3. {'lead': 'Inspect all motor and drive wiring', 'text': 'for loose terminals, open circuits, damaged insulation, or corroded connections. Tighten all terminals and repair or replace any defective cables.'}
4. {'lead': 'Check the mechanical load', 'text': 'by rotating the motor shaft by hand (with power off and locked out) to confirm free movement and no binding, seized bearings, or obstruction.'}
5. {'lead': 'Rerun Auto-Tuning', 'text': 'using the corrected motor nameplate data and with the motor mechanically free. Follow the Auto-Tuning procedure in your GA800 manual to allow the drive to relearn motor parameters.'}
6. {'lead': 'Confirm drive and motor compatibility', 'text': "by reviewing the drive's motor type setting and control mode to match the actual motor (induction, permanent magnet, synchronous) and application requirements."}
7. {'lead': 'Contact Yaskawa technical support', 'text': 'if the fault persists after parameter correction, wiring repair, and successful Auto-Tuning. Provide the drive model, serial number, fault code, and application details for escalation.'}

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor power cable (3-phase shielded) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-e02-fault-code&k=Motor+power+cable+%283-phase+shielded%29&tag=errorcodefixes-20) \| Replace if insulation is damaged or conductors are corroded during wiring inspection. |
| Terminal block connectors | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-e02-fault-code&k=Terminal+block+connectors&tag=errorcodefixes-20) \| Replace any cracked, burned, or loose terminal blocks found at the drive output or motor junction box. |

## When to Call a Pro

Call a qualified drives technician or Yaskawa-certified service provider if the E02 fault returns after you have verified and corrected all motor nameplate data, repaired wiring, confirmed free mechanical movement, and successfully completed Auto-Tuning. Persistent faults may indicate internal drive circuit issues, advanced parameter conflicts, or application mismatches that require diagnostic software and factory-level support. Always involve a professional if you are unsure how to perform Auto-Tuning safely or if your application includes complex multi-motor configurations or specialized control modes.

## See Also

- [Yaskawa GA800 E08 Fault Code - Causes & Fix](/posts/yaskawa-ga800-e08-fault-code/)
- [Yaskawa GA800 E19 Fault - Causes & Fix](/posts/yaskawa-ga800-e19-fault-code/)
- [Yaskawa A1000 OC Fault — Overcurrent](/posts/yaskawa-a1000-fault-oc/)
- [Yaskawa A1000 Fault UV1, DC Bus Undervoltage Causes & Fix](/posts/yaskawa-a1000-fault-uv1/)
