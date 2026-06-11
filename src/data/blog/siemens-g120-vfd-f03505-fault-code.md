---
title: "Siemens G120 F03505 - Causes & Fix"
description: "F03505 means analog input wire break on Siemens G120 VFD. Most often a broken wire or loose connection. Check wiring and threshold settings."
pubDatetime: 2026-06-01T11:29:14Z
modDatetime: 2026-06-01T11:29:14Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Shielded analog signal cable"
---

## Siemens G120 F03505 — What It Means

F03505 on a Siemens SINAMICS G120 is a fault that means 'Analog input, wire break.' The drive's wire-break monitoring has detected that the analog input current has dropped below the configured threshold set in parameter p0761. This is not a warning but a fault that stops operation. The drive expects a continuous current loop signal from an external device (like a pressure or flow transmitter) and triggers F03505 when the current falls too low or disappears entirely. You can read the actual measured analog input current in parameter r0752[x] to compare it against your threshold.

[Jump to Fix](#fix)

## Common Causes

- **Open or broken wire in the analog input loop** The signal cable from your transmitter or controller to the G120 analog input terminal has been cut, damaged, or has an internal break.
- **Loose or corroded terminal connections** The wire connections at the drive input terminals or at the field transmitter have backed out, corroded, or oxidized, interrupting the current path.
- **Signal source outputting current below threshold** The upstream analog transmitter or signal conditioner is malfunctioning or misconfigured and is not providing enough loop current to satisfy the wire-break monitoring threshold in p0761.
- **Incorrect wire-break threshold setting** Parameter p0761 is set too high for your application, so a valid low-current signal is incorrectly interpreted as a wire break.
- **Damaged analog input circuitry on the control unit** If all external wiring and sources are confirmed good, the analog input circuit on the G120 control unit itself may have failed.
- **Incorrect analog input parameter assignment** The drive's analog input configuration (such as p0756 or p0756[1] on CU240D-2 units) is set incorrectly, causing the monitoring function to behave unexpectedly.

## Step-by-Step Fix {#fix}

1. {'lead': 'Read the current fault data', 'text': 'On the drive keypad or via your HMI, check parameter r0752[x] to read the actual measured analog input current right now and compare it to the threshold set in p0761.'}
2. {'lead': 'Inspect all analog input wiring for breaks or damage', 'text': 'Trace the signal cable from the field transmitter or signal source all the way to the G120 analog input terminals and look for cuts, pinch points, or visible damage to the conductors.'}
3. {'lead': 'Check and tighten all terminal connections', 'text': "Remove and reseat each wire at the drive input terminals and at the transmitter, cleaning any corrosion or oxidation you find, then torque to the manufacturer's specification."}
4. {'lead': 'Verify the signal source is outputting correct loop current', 'text': 'Use a multimeter in series with the loop to measure the actual current being sent by your transmitter or controller and confirm it is above the threshold in p0761 under normal operating conditions.'}
5. {'lead': 'Review and adjust parameter p0761 if needed', 'text': 'If your application uses a legitimately low analog signal, consult your G120 manual and lower the wire-break monitoring threshold in p0761 to a value that suits your loop current range.'}
6. {'lead': 'Check analog input assignment parameters', 'text': 'Verify that parameters like p0756 (or p0756[1] on CU240D-2 variants) are correctly configured for your control unit and that wire-break monitoring is enabled and set appropriately for your application.'}
7. {'lead': 'Clear the fault and test', 'text': "Once the wiring, source, or parameterization issue is corrected, use the drive's fault reset button or command to clear F03505 and run a test cycle to confirm the analog input current stays above threshold."}

## Parts Often Needed

| Part | Notes |
|------|-------|
| Shielded analog signal cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f03505-fault-code&k=Shielded+analog+signal+cable&tag=errorcodefixes-20) \| Replace if the existing wire is cut, damaged, or has intermittent continuity in the loop. |
| Analog input terminal block or connector | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f03505-fault-code&k=Analog+input+terminal+block+or+connector&tag=errorcodefixes-20) \| Use if the existing terminals are corroded, cracked, or no longer hold the wire securely. |
| Analog transmitter or signal source | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f03505-fault-code&k=Analog+transmitter+or+signal+source&tag=errorcodefixes-20) \| Replace the upstream current-loop transmitter if it cannot output adequate loop current even after recalibration. |
| G120 control unit (CU240 or equivalent) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f03505-fault-code&k=G120+control+unit+%28CU240+or+equivalent%29&tag=errorcodefixes-20) \| Required only if all external wiring and sources test good but the analog input circuitry on the drive is confirmed failed. |

## When to Call a Pro

Call a qualified drive technician or controls integrator if you have verified continuity and correct current in the external loop but the fault persists, if you are unsure how to safely measure live current loops or modify drive parameters, or if you suspect the control unit's analog input hardware is damaged. Also get professional help if your system uses complex multi-channel analog configurations or safety-rated signals where incorrect parameterization could create a hazard. Working inside an energized VFD cabinet requires electrical training and appropriate PPE.

## See Also

- [Siemens G120 F01611 - Causes & Fix](/posts/siemens-g120-f01611-fault-code/)
- [Siemens G120 F01015 Fault - Causes & Fix](/posts/siemens-g120-vfd-f01015-fault-code/)
- [Siemens G120 F01662 - Causes & Fix](/posts/siemens-g120-f01662-fault-code/)
- [Siemens Micromaster F0060 - Causes & Fix](/posts/siemens-micromaster-f0060-fault-code/)
