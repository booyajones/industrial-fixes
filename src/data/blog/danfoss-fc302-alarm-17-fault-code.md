---
title: "Danfoss FC302 Alarm 17 - Causes & Fix"
description: "Alarm 17 on Danfoss FC302 means standard bus timeout or control word timeout. Learn the 6 causes and 7 repair steps to restore communication."
pubDatetime: 2026-05-29T09:41:49Z
modDatetime: 2026-05-29T09:41:49Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Fieldbus communication cable"
most_likely_cause: "Loss of communication from the master controller"
---

## Danfoss FC302 Alarm 17 — What It Means

Alarm 17 on the Danfoss VLT AutomationDrive FC302 indicates a standard bus timeout or control word timeout. This means the drive has stopped receiving the expected control word or communication signal from the master controller over the serial fieldbus or control interface within the configured timeout period. The alarm triggers when communication is lost, and depending on how parameter 8-04 is set, the drive may ramp down and trip or just display a warning. This fault only appears when the drive is configured to monitor the communication link and the timeout function is active.

[Jump to Fix](#fix)

## Common Causes

- **Loss of communication from the master controller** The PLC, gateway, or supervisory device has stopped sending the control word to the drive over the serial bus.
- **Loose, broken, or miswired communication cable** Physical damage, poor connections, incorrect polarity, or improper termination on the fieldbus cable can interrupt the signal.
- **Communication equipment failure on the master side** A problem with the PLC output, gateway, or fieldbus interface can prevent the control word from reaching the drive.
- **Incorrect timeout configuration** Parameter 8-03 Control Word Timeout Time may be set too short for the application, or parameter 8-04 may not match the intended control strategy.
- **EMC or installation issues affecting the fieldbus** Electrical noise, poor shielding, or grounding problems can corrupt or block communication between the master and the drive.
- **Faulty communication interface or control card in the drive** If all external wiring and the master are confirmed good, the drive's internal communication board or control card may have failed.

## Step-by-Step Fix {#fix}

1. **Verify the active communication path** by confirming whether the drive is set for fieldbus or serial control rather than local keypad control, since Alarm 17 only applies to remote communication faults.
2. **Inspect the communication cable and terminations** at both the drive and master ends for looseness, damage, corrosion, reversed polarity, and proper shielding and grounding per EMC installation requirements.
3. **Confirm the master is sending the control word** by checking the PLC program output, network diagnostics, and the status of any gateways or fieldbus interfaces in the communication chain.
4. **Review parameter 8-03 Control Word Timeout Time** and increase it if your process requires a longer watchdog period, then check parameter 8-04 Control Word Timeout Function to confirm it matches your intended fault response (warning only or stop and trip).
5. **Test with known-good communication hardware** by swapping in a spare cable or verifying that any LCP keypad or communication accessory is operating normally and not generating false timeout signals.
6. **Reset the alarm and retest** after restoring communication and correcting any parameter settings, then monitor the drive under normal operation to confirm the fault does not return.
7. **Inspect the drive's communication interface or control card** if the fault persists after confirming all external wiring and master-side operation are correct, and replace the faulty board as required.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Fieldbus communication cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-17-fault-code&k=Fieldbus+communication+cable&tag=errorcodefixes-20) \| Replace if damaged, cut, or failing continuity and shield tests. |
| VLT control card or communication board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-17-fault-code&k=VLT+control+card+or+communication+board&tag=errorcodefixes-20) \| Required only if internal interface has failed after external checks are confirmed good. |
| Fieldbus gateway or interface module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-17-fault-code&k=Fieldbus+gateway+or+interface+module&tag=errorcodefixes-20) \| Needed if the master-side communication hardware is found defective. |

## When to Call a Pro

Call a qualified technician or automation integrator if you are not familiar with fieldbus wiring, PLC programming, or drive parameter configuration. If you have verified all cable connections and master controller outputs are correct but the alarm persists, the drive may require internal board replacement or advanced diagnostics that need manufacturer support. Also consult a professional if you work in a facility where communication network changes must be coordinated with other equipment or safety interlocks, or if the drive is part of a larger SCADA or DCS system.

## See Also

- [Danfoss FC302 Complete Fault Code Guide — All Faults and Fixes](/posts/danfoss-fc302-complete-guide/)
- [Danfoss FC102 VLT HVAC Drive Fault Codes — Complete Diagnostic Reference](/posts/danfoss-fc102-fault-codes/)
- [Danfoss VFD Fault UL — Causes & Fix](/posts/danfoss-vfd-fault-ul/)
- [Danfoss VFD Fault Codes — FC301, FC302, FC102 Reference](/posts/danfoss-vfd-fault-codes/)
