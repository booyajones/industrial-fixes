---
title: "Siemens G120 F03505 - Causes & Fix"
description: "Siemens G120 fault F03505 means analog input wire breakage. Learn the real causes and step-by-step fix for this wire-break fault."
pubDatetime: 2026-05-28T09:02:27Z
modDatetime: 2026-05-28T09:02:27Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Analog input field cable"
---

## Siemens G120 F03505 — What It Means

F03505 on a Siemens SINAMICS G120 indicates that the drive's wire-break monitoring has detected a loss of signal on an analog input. The drive continuously monitors the current at analog inputs referenced in p0756 and p0756[1], and when the measured current falls below the threshold set in parameter p0761[0…3], the fault triggers. This typically happens when the drive expects a 4–20 mA loop current but sees too little or no current at all.

The fault does not mean the drive itself is broken. It means the drive cannot see a valid signal from the upstream transmitter or sensor. The wire-break detection is a safety and diagnostic feature to alert you that the analog input circuit is open, disconnected, or delivering insufficient current to the control unit.

[Jump to Fix](#fix)

## Common Causes

- **Open circuit or loose terminal** A loose screw terminal, broken wire, or bad crimp in the analog input wiring interrupts the current loop and triggers the fault.
- **Transmitter or signal source not outputting enough current** The upstream device may be powered off, failed, or configured for the wrong output range, so the drive sees less than the expected loop current.
- **Incorrect wiring of the analog signal** The signal may be connected to the wrong terminals or wired in a way that prevents the drive from seeing the full loop current.
- **Damaged field cable or shielding** Physical damage to the analog input cable, poor shielding termination, or a broken conductor can cause intermittent or complete loss of signal.
- **Wire-break threshold set too high** If parameter p0761 is configured higher than the actual minimum signal level in your application, the drive will trip even when the loop is functioning normally.

## Step-by-Step Fix {#fix}

1. {'lead': 'Identify the faulted analog input channel', 'text': 'Check the drive display or parameter p0756 and p0756[1] to confirm which analog input is assigned and which channel triggered F03505.'}
2. {'lead': 'Read the actual input current in parameter r0752[x]', 'text': 'Use the keypad or commissioning software to read the measured current at the analog input and compare it to what you expect from the transmitter.'}
3. {'lead': 'Inspect the wiring from the transmitter to the drive', 'text': 'Look for loose terminals at both ends, damaged conductors, bad crimps, or breaks in the field cable that would open the current loop.'}
4. {'lead': 'Measure the loop current at the drive input terminals', 'text': 'Use a multimeter in series with the input to verify the actual current and confirm whether the transmitter is outputting a valid 4–20 mA signal.'}
5. {'lead': 'Check the upstream transmitter or sensor', 'text': "Confirm the field device is powered, operating correctly, and configured for the correct output type and range that matches the drive's input."}
6. {'lead': 'Review the wire-break threshold in parameter p0761', 'text': 'If the loop current is legitimate but below the threshold, adjust p0761 only if your application allows a lower minimum current, or consult your process documentation.'}
7. {'lead': 'Restore the circuit and reset the fault', 'text': 'After repairing the wiring or replacing the faulty transmitter, acknowledge or reset F03505 using the keypad, digital input, or control word, then verify normal operation.'}

## Parts Often Needed

| Part | Notes |
|------|-------|
| Analog input field cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-f03505-fault-code&k=Analog+input+field+cable&tag=errorcodefixes-20) \| Shielded twisted-pair cable rated for the signal type and environment, if the existing cable is damaged or broken. |
| 4–20 mA transmitter or sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-f03505-fault-code&k=4%E2%80%9320+mA+transmitter+or+sensor&tag=errorcodefixes-20) \| Replacement for the upstream signal source if it is not supplying the correct loop current or has failed. |
| Wire ferrules and terminal hardware | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-f03505-fault-code&k=Wire+ferrules+and+terminal+hardware&tag=errorcodefixes-20) \| For securing conductors at the control unit terminals if connections are loose or corroded. |

## When to Call a Pro

Call a qualified drive technician or instrumentation specialist if you have verified the wiring and transmitter are intact but the fault persists, or if you are not familiar with analog loop troubleshooting and safe work on live industrial control circuits. Also call for help if the analog input stage on the control unit is suspected to be defective after all external checks, or if you need assistance configuring parameters p0756, p0761, and the analog scaling for your specific process application.

## See Also

- [Siemens Micromaster F0023 - Causes & Fix](/posts/siemens-micromaster-f0023-fault-code/)
- [Siemens Micromaster F0001 - Causes & Fix](/posts/siemens-micromaster-f0001-fault-code/)
- [Siemens G120 A05000 - Causes & Fix](/posts/siemens-g120-a05000-fault-code/)
- [Siemens SINAMICS G120 F30011 Fault — Phase Loss Fix](/posts/siemens-sinamics-f30011-fault/)
