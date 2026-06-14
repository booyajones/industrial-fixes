---
title: "ABB ACS550 AI2 LOSS Fault - Causes & Fix"
description: "AI2 LOSS on the ABB ACS550 means analog input 2 signal is lost or below the minimum threshold. Fix wiring, check field device, and verify parameters."
pubDatetime: 2026-05-27T10:38:45Z
modDatetime: 2026-05-27T10:38:45Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - abb
money_part: "Analog signal transmitter or sensor"
most_likely_cause: "Lost or disconnected AI2 wiring"
---

## ABB ACS550 AI2 LOSS Fault — What It Means

AI2 LOSS on an ABB ACS550 drive means the unit has detected that analog input 2 is lost or that the AI2 signal has fallen below the configured minimum or fault threshold. ABB's fault listing defines this as 'Analog input 2 is lost, or value is less than the minimum setting.' The fault is tied to parameter 3022 (AI2 FAULT LIMIT) and parameter 3001 (AI<MIN FUNCTION), which together control the threshold and the drive's response when the input drops.

This fault does not necessarily indicate a failed drive component. In most cases, the analog source feeding AI2 is disconnected, powered down, or misconfigured, so the drive sees a valid input loss rather than internal electronics failure. The drive is reacting to a real missing signal condition. Diagnosis focuses on the field wiring, the transmitter or controller sending the analog signal, and the drive's parameter setup.

[Jump to Fix](#fix)

## Common Causes

- **Lost or disconnected AI2 wiring** The most common cause is broken, loose, or disconnected wiring between the analog signal source and the drive's AI2 terminals, or corroded terminals that interrupt the signal path.
- **Field device powered down or failed** The transmitter, sensor, or controller feeding AI2 is turned off, has lost its power supply, or has failed internally and no longer outputs an analog signal.
- **Incorrect AI2 FAULT LIMIT setting (3022)** Parameter 3022 is set too high for the actual signal range, so normal operating signals are interpreted as a fault condition by the drive.
- **Signal type mismatch or configuration error** The drive is configured to expect a different analog input type (voltage vs. current) than what the field device is actually providing, or the input scaling is wrong.
- **Faulty analog input circuitry on the drive** Less common, but the drive's AI2 input circuit on the control board may be damaged, causing it to read the signal incorrectly even when field wiring and the source are good.

## Step-by-Step Fix {#fix}

1. **Verify the fault on the keypad.** Confirm the display shows AI2 LOSS and not a different alarm or warning. Record the fault code and any fault history from the drive's event log.
2. **Check the external analog source.** Confirm the transmitter, sensor, or controller feeding AI2 is powered on, functioning, and set to output the correct signal type (0-10V, 4-20mA, etc.). Measure its output with a multimeter at the device terminals.
3. **Inspect all AI2 wiring and connections.** Trace the cable from the field device to the drive's AI2 terminals. Look for loose screws, broken wires, corrosion, damaged cable jackets, or a broken shield or return conductor. Tighten all terminations.
4. **Measure the signal at the drive's AI2 terminals.** Use a multimeter to check the actual voltage or current arriving at the drive and compare it to the expected range and signal type configured in the drive parameters.
5. **Review and correct parameters 3022 and 3001.** Check that parameter 3022 (AI2 FAULT LIMIT) is set appropriately for your application and signal range, and that parameter 3001 (AI<MIN FUNCTION) matches the intended behavior when AI2 falls below minimum. Consult the ACS550 parameter manual for your installation's design values.
6. **Reset the drive and test.** After correcting wiring or parameters, clear the fault and run the drive. Observe whether AI2 LOSS reappears during normal operation.
7. **Isolate the input circuit if the fault persists.** Disconnect the field wiring and inject a known-good test signal (calibrated voltage or current source) directly into the drive's AI2 terminals. If the drive still faults with a good test signal, suspect the drive's analog input board and plan for control board repair or replacement.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Analog signal transmitter or sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs550-ai2-loss-fault-code&k=Analog+signal+transmitter+or+sensor&tag=errorcodefixes-20) \| Replace if the field device is confirmed failed and no longer outputs the correct analog signal to AI2. |
| Shielded analog input cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs550-ai2-loss-fault-code&k=Shielded+analog+input+cable&tag=errorcodefixes-20) \| Use if existing AI2 wiring is damaged, corroded, or does not match the required signal type and shielding for your installation. |
| ACS550 control board (I/O card) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs550-ai2-loss-fault-code&k=ACS550+control+board+%28I%2FO+card%29&tag=errorcodefixes-20) \| Required only if the drive's AI2 input circuit is proven faulty by substitution testing with a known-good signal source. Consult ABB for the exact board part number for your drive model. |

## When to Call a Pro

Call a qualified industrial electrician or drive technician if you are not trained to work safely around live AC drive terminals and control wiring. Also contact a professional if you have verified all field wiring and the analog source are correct but the fault persists, if you need to replace the drive's control board, or if you are unfamiliar with ABB drive parameter programming and cannot confidently adjust 3022 and 3001 without risking a process shutdown. ABB-certified service partners have the test equipment and parameter files to diagnose analog input circuit faults and perform board-level repairs or replacements under warranty or service contract.

## See Also

- [ABB ACS580 A3D0 Fault Code - Causes & Fix](/posts/abb-acs580-a3d0-fault-code/)
- [ABB ACS580 A0 Fault Code - Causes & Fix](/posts/abb-acs580-a0-fault-code/)
- [ABB ACS580 Fault Codes — Complete Diagnosis & Fix Guide](/posts/abb-acs580-fault-codes/)
- [ABB ACS880 Fault 2310 - Overcurrent Diagnosis and Fix](/posts/abb-acs880-fault-2310/)
