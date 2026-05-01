---
title: "Mitsubishi FR-A800 Fault E.OC1, Overcurrent During Acceleration Fix"
description: "What Mitsubishi FR-A800 Fault E.OC1 means, why overcurrent happens during acceleration, and how to diagnose the motor, load, and parameter causes."
pubDatetime: 2026-04-24T23:50:00Z
modDatetime: 2026-04-24T23:50:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - mitsubishi
  - fr-a800
---

## Mitsubishi FR-A800 Fault E.OC1, What It Means

On a Mitsubishi FR-A800, **Fault E.OC1** means **overcurrent during acceleration**. The inverter output current rose above the drive's safe threshold while the motor was speeding up, so the FR-A800 shut down to protect the power section.

This is one of the most common high-pressure production faults because it happens right at machine start. If a conveyor, pump, spindle, or extruder will not get through the ramp, the whole line stays down.

[Jump to Fix](#fix)

## Common Causes

- **Acceleration time is too short** for the motor and load inertia.
- **Motor is starting into a jammed or heavy load**. Bearings, gearboxes, and driven equipment may be binding.
- **Output short or damaged motor cable**. Insulation failure can look like an overcurrent spike during ramp-up.
- **Motor data or control settings are wrong**. Incorrect base frequency, motor current, or vector settings can make the drive overreact.
- **Restart command given while the motor is still coasting**. The inverter tries to grab a moving motor and current spikes immediately.
- **Drive or motor is undersized for the application**. The line may have been changed without resizing the inverter.

## Step-by-Step Fix {#fix}

1. **Check whether the motor is free to turn**. Lock out, then verify the driven load is not seized. On production equipment, a mechanical jam is just as common as an electrical fault.
2. **Lengthen the acceleration ramp**. Increase acceleration time and test again. If E.OC1 clears, you likely had an aggressive start command for the real load inertia.
3. **Make sure the motor is not being restarted while still spinning**. If the application frequently reissues start commands before the motor stops, enable the proper flying-start or restart strategy for the machine.
4. **Inspect the output cable and motor insulation**. Disconnect the motor leads and test phase-to-phase and phase-to-ground. A damaged cable can trip E.OC1 before the motor even gets moving.
5. **Verify the FR-A800 motor parameters**. Confirm motor full-load current, base frequency, rated voltage, and control mode match the nameplate and the actual application.
6. **Run the motor uncoupled if possible**. If the inverter accelerates the motor cleanly with the load removed, your fault is mechanical or application-related, not a bad drive.
7. **Check for rapid direction changes or torque reversals**. Commands that swing from forward to reverse under load can create severe current spikes.
8. **Review drive sizing and recent process changes**. If a larger product, heavier roll, or different gearbox was added, the original drive may no longer have enough margin.

## Parts Often Needed

| Part | Notes |
|------|-------|
| VFD-rated motor cable | [Amazon](https://www.amazon.com/s?k=VFD+rated+motor+cable&tag=errorcodefixes-20) \| Replace cable with damaged insulation or repeated flex damage |
| Insulation tester | [Amazon](https://www.amazon.com/s?k=megohmmeter+insulation+tester&tag=errorcodefixes-20) \| Required to separate cable faults from motor faults |
| Output reactor | [Amazon](https://www.amazon.com/s?k=output+reactor+vfd&tag=errorcodefixes-20) \| Useful on long motor leads or harsh reflected-wave installations |
| Replacement 3-phase motor | [Amazon](https://www.amazon.com/s?k=3+phase+motor+inverter+duty&tag=errorcodefixes-20) \| Needed when winding damage or bearing drag is driving current up |
| Encoder cable / feedback cable hardware | [Amazon](https://www.amazon.com/s?k=industrial+encoder+cable&tag=errorcodefixes-20) \| Relevant on vector applications with feedback issues |

## When to Call a Professional

Call a Mitsubishi drive specialist if E.OC1 remains after a longer ramp, a verified free-turning load, and a clean motor insulation test. If the fault happens with the motor disconnected, or if current spikes instantly on enable, the inverter power section may be damaged.

## See Also

- [Mitsubishi FR-A800 Fault E7, Overload Causes and Fix](/posts/mitsubishi-fr-a800-fault-e7/)
- [Mitsubishi FR-D700 Fault Codes, Common Trips and Fixes](/posts/mitsubishi-fr-d700-fault-codes/)
- [Mitsubishi FR Series Fault E6, Ground Fault Guide](/posts/mitsubishi-fr-series-fault-e6/)
- [VFD Fault Codes OC, OV, UV, OL, What They Mean](/posts/vfd-fault-codes-oc-ov-uv-ol/)

## Related Articles

- [Mitsubishi City Multi P8 / E6 Error Codes — Causes & Fix](/posts/mitsubishi-city-multi-error-codes/)
- [Mitsubishi PEX City Multi Error Codes (Indoor Unit): Complete Guide](/posts/mitsubishi-city-multi-pex-error/)
- [Mitsubishi CNC Alarm 500 — Causes & Fix](/posts/mitsubishi-cnc-alarm-500/)
- [Mitsubishi CNC Alarm Y96 — Causes & Fix](/posts/mitsubishi-cnc-alarm-y96/)
- [Mitsubishi E1 Error Code — Indoor/Outdoor Communication Fault Fix](/posts/mitsubishi-e1-error-code/)
