---
title: "Siemens G120 F01122 - Causes & Fix"
description: "F01122 (A01122) means frequency at the measuring probe input is too high. Check probe wiring, scaling, and parameters before replacing anything."
pubDatetime: 2026-05-31T11:19:23Z
modDatetime: 2026-05-31T11:19:23Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Measuring probe or encoder"
most_likely_cause: "Sensor generating excessive pulse frequency"
---

## What this code means
F01122 (officially listed as A01122 in Siemens documentation) is an alarm indicating that the frequency at the measuring probe input is too high. This is not a power stage or motor fault. The drive is receiving a pulse signal at its measuring probe input terminal that exceeds the configured or hardware limit. The alarm points to an issue on the sensor or input side, not the drive's output or internal power components. In most cases, the problem lies with the sensor device generating the signal, the wiring between the sensor and drive terminals, or incorrect parameter configuration for the probe input type and scaling.

## Common Causes

- **Sensor generating excessive pulse frequency** The encoder, tachometer, or other measuring probe connected to the input is outputting pulses at a rate higher than the drive can accept or is configured to handle.
- **Incorrect probe parameter settings** The drive parameters for the measuring probe input do not match the actual sensor type, pulse-per-revolution setting, or frequency range of the connected device.
- **Wiring or terminal faults** Loose connections, shorts, swapped signal wires, or poor shielding at the probe input terminals can cause the drive to interpret noise or corrupted signals as excessively high frequency.
- **Incorrect signal conditioning or scaling** An external signal conditioner, frequency multiplier, or pulse converter between the sensor and drive is misconfigured and passing an amplified or unscaled pulse train.
- **Control unit internal I/O issue** If the alarm persists after verifying external wiring and configuration, the control unit's measuring input circuitry may have failed and is misreading the input frequency.

## Step-by-Step Fix {#fix}

1. **Acknowledge and document the alarm** on the drive keypad or via the commissioning software, then note which terminal is assigned as the measuring probe input in your drive parameters.
2. **Identify the measuring probe device** (encoder, tachometer, pulse sensor) connected to that input and confirm its rated output frequency range and pulse-per-revolution or pulse-per-unit specification from its datasheet.
3. **Inspect the probe wiring and terminals** from the sensor to the G120 input, checking for loose terminal screws, damaged conductors, missing or broken shield connections, incorrect polarity, and any signs of moisture or contamination at the connector.
4. **Measure the actual signal frequency at the probe output** using an oscilloscope or frequency counter while the system is running at the condition that triggered the alarm, and compare the measured frequency to the drive's input specification and your parameter settings.
5. **Review and correct drive parameters** for the measuring probe input, including sensor type selection, pulses per revolution, frequency scaling factor, and maximum input frequency limit, ensuring they match your actual sensor and application requirements.
6. **Reduce the pulse frequency if needed** by slowing the mechanical process, changing encoder resolution, adjusting gear ratios, or reconfiguring an external pulse conditioner to output a lower frequency within the drive's acceptable range.
7. **Power cycle the drive and clear the alarm** after making corrections, then monitor for recurrence under normal operating conditions. If the alarm returns immediately with verified-good wiring and correct parameters, suspect a control unit fault and consult Siemens service or plan for control unit replacement.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Measuring probe or encoder | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f01122-fault-code&k=Measuring+probe+or+encoder&tag=errorcodefixes-20) \| Replacement sensor if the original is damaged or outputting incorrect frequency. Match type, pulse rate, and mounting to your application. |
| Shielded encoder cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f01122-fault-code&k=Shielded+encoder+cable&tag=errorcodefixes-20) \| Use proper shielded twisted-pair cable rated for encoder signals. Verify length and capacitance limits for your probe type. |
| G120 Control Unit (CU) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f01122-fault-code&k=G120+Control+Unit+%28CU%29&tag=errorcodefixes-20) \| Required only if alarm persists after confirming external wiring and configuration are correct. Order the correct CU model for your G120 frame size and firmware. |

## When to Call a Pro

Call a qualified drives technician or Siemens-certified service provider if you do not have the tools to measure pulse frequency at the sensor output, if you are unfamiliar with drive parameter configuration for encoder or probe inputs, or if the alarm continues after you have verified wiring integrity and corrected all parameter settings. Control unit replacement requires proper firmware transfer, parameter backup, and commissioning. If your process is safety-critical or the drive is part of a coordinated multi-axis system, have a professional perform all diagnostic and repair work.
