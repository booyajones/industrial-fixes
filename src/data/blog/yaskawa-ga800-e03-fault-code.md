---
title: "Yaskawa GA800 E03 Fault Code - Causes & Fix"
description: "E03 on a Yaskawa GA800 drive typically indicates an external fault input problem on terminal S3. Learn how to diagnose and clear it."
pubDatetime: 2026-05-30T12:23:05Z
modDatetime: 2026-05-30T12:23:05Z
author: "James Rutherford"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
---

## Yaskawa GA800 E03 Fault Code — What It Means

The GA800 drive is reporting an external fault condition, most commonly displayed as EF3 (External Fault Terminal S3). The drive has detected that an external interlock or safety device wired to the S3 digital input terminal has opened or sent a fault signal, or that the input is incorrectly configured. This is not an internal drive failure. The drive is responding to a condition in your field wiring or connected equipment, such as a safety relay, limit switch, pressure switch, or other normally-closed contact that has tripped or lost continuity.

The exact designation 'E03' is not confirmed in manufacturer GA800 documentation, but technicians often see this displayed when an external fault input (EF3) is active. The drive will not run until the external fault circuit is restored and the fault is cleared from the keypad. This fault does not indicate a blown IGBT, DC bus problem, or internal component failure. It tells you to look outside the drive cabinet at the devices and wiring feeding the fault input.

[Jump to Fix](#fix)

## Common Causes

- **External interlock or safety device has tripped.** A relay contact, emergency stop, pressure switch, limit switch, or overload connected to terminal S3 has opened and is sending a fault signal to the drive.
- **Loose or broken wiring on terminal S3.** The conductor landed on S3 or its common has come loose, corroded, or broken, causing the input circuit to open and triggering the fault.
- **Parameter H1-01 assigns external fault function but terminal is not wired correctly.** The drive is configured to expect a normally-closed contact on S3, but the field device is wired backward, the wrong logic (source vs. sink) is applied, or the terminal is left floating.
- **Field device in the fault circuit has failed or changed state.** The external safety relay, flow switch, thermal overload, or other interlock wired to S3 has failed in the open position or legitimately detected a real process fault.
- **Control board input circuit for S3 is damaged.** After ruling out all wiring and external devices, the digital input path on the GA800 control board itself may be shorted or open, though this is uncommon compared to field wiring issues.

## Step-by-Step Fix {#fix}

1. **Confirm the exact fault code** displayed on the keypad. Note whether it reads 'EF3' or a similar external-fault designation, and record any additional trip information shown.
2. **Identify and inspect all external devices** wired to terminal S3. Check safety relays, limit switches, pressure switches, emergency stops, and any other interlock contacts in the fault circuit for open contacts, tripped state, or mechanical failure.
3. **Check terminal S3 wiring** at the drive. Verify that conductors are tight, landed on the correct terminals (S3 and its common), not damaged, and that polarity and source/sink logic match your drive's input configuration.
4. **Review parameter H1-01** and any other MFDI input assignments. Confirm that the function assigned to S3 matches your field wiring and that the terminal is not enabled for external fault unless your application actually uses that input.
5. **Restore the external fault circuit.** Reset or close the tripped device, repair any broken wiring, or remove the fault condition in the field equipment. Measure continuity across the S3 input and common to verify the circuit is closed before proceeding.
6. **Clear the fault** from the keypad using the RESET function. Do not re-energize the drive or attempt to run until the external fault circuit is confirmed closed and stable.
7. **Test drive operation.** Command a start and observe whether the fault returns. If it does, isolate the S3 input by temporarily jumpering the terminal (only for testing with appropriate safety lockout) to determine whether the fault is in the field circuit or the drive input itself.

## Parts Often Needed

| Part | Notes |
|------|-------|
| External fault relay or safety interlock | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-e03-fault-code&k=External+fault+relay+or+safety+interlock&tag=errorcodefixes-20) \| Replace the field device (relay, limit switch, pressure switch) if it has failed in the open state or is confirmed defective after testing. |
| Field wiring for terminal S3 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-e03-fault-code&k=Field+wiring+for+terminal+S3&tag=errorcodefixes-20) \| Use appropriately rated control wire (typically 18 to 22 AWG shielded) if existing conductors are damaged, corroded, or undersized. |
| GA800 control board (if input circuit is damaged) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-e03-fault-code&k=GA800+control+board+%28if+input+circuit+is+damaged%29&tag=errorcodefixes-20) \| Only required if the S3 input path is confirmed shorted or open after all field wiring and devices are ruled out. Consult Yaskawa or your distributor for the correct replacement board and firmware version for your drive model. |

## When to Call a Pro

Call a qualified drive technician or controls integrator if you cannot locate the external device or interlock causing the fault, if the wiring diagram for your machine is missing or unclear, or if the fault persists after you have verified and restored all external circuits. Also call for help if you are unfamiliar with digital input wiring, source/sink logic, or parameter configuration on the GA800. Do not attempt to bypass safety interlocks permanently or disable the external fault input without a full hazard review and machine risk assessment. If the control board input itself is suspected, replacement and parameter backup/restore should be performed by someone trained on Yaskawa drives to avoid loss of application settings or further damage.

## See Also

- [Yaskawa GA800 E17 Fault - Causes & Fix](/posts/yaskawa-ga800-e17-fault-code/)
- [Yaskawa GA800 oC Fault — Overcurrent Fix](/posts/yaskawa-ga800-error-oc/)
- [Yaskawa GA800 E21 Fault - Causes & Fix](/posts/yaskawa-ga800-e21-fault-code/)
- [Yaskawa VFD Fault UV1 — Causes & Fix](/posts/yaskawa-vfd-fault-uv1/)
