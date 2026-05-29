---
title: "ABB ACS580 A5A0 Fault - Causes & Fix"
description: "ABB ACS580 A5A0 means Safe Torque Off is active. Learn the common wiring and safety-relay causes and how to restore STO signals."
pubDatetime: 2026-05-27T10:34:32Z
modDatetime: 2026-05-27T10:34:32Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - abb
---

## ABB ACS580 A5A0 Fault — What It Means

A5A0 on an ABB ACS580 drive means the Safe Torque Off (STO) function is active. The drive has lost the safety-circuit signal(s) on the STO connector, so it has disabled the motor and will not allow a start command until the STO inputs are restored and the fault is reset. STO is a hardware safety feature that de-energizes motor torque when external safety devices (like an E-stop, door switch, or safety relay) open the STO circuit.

The fault appears on the drive display when one or both STO channels are not energized. ABB's fault-tracing table identifies the cause as lost safety-circuit signals and directs you to check the safety circuit connections. The drive will remain in this faulted state until you restore the STO input wiring or external safety device and clear the fault.

[Jump to Fix](#fix)

## Common Causes

- **Open or disconnected STO wiring** Loose terminals, broken wires, or missing jumpers at the STO connector prevent the safety-circuit signal from reaching the drive.
- **External safety relay contact open** An E-stop, door interlock, light curtain, or safety relay has opened the STO circuit, either intentionally or because of a relay fault.
- **STO channel mismatch or timing issue** Both STO channels must switch together, and a delay or fault in one channel can trigger the fault even if the other is energized.
- **Incorrect STO jumper installation** If the drive is not using external safety hardware, missing or wrongly landed jumpers will leave the STO inputs open.
- **Diagnostic parameter set to fault on STO** The drive may be configured to trip on STO indication rather than just display a warning, so parameter settings can change fault behavior.

## Step-by-Step Fix {#fix}

1. **Verify the STO circuit status** by checking whether an external E-stop, door switch, safety relay, or light curtain is holding the STO inputs open, and confirm whether the safety device is intentionally activated or faulted.
2. **Inspect the STO connector wiring** on the drive for loose terminals, broken conductors, incorrect landing, or missing jumpers if the installation does not use external STO hardware.
3. **Test the external safety relay or safety device** to confirm both STO channels are switching correctly and that the relay contacts operate as intended, with no stuck or delayed contacts.
4. **Check the STO diagnostic parameter** in the drive settings to determine if the drive is configured to fault on STO indication or only warn, and adjust if the behavior does not match the application requirements.
5. **Restore the STO inputs** by closing the safety circuit (reset the E-stop, close the door, or repair the relay), then reset the fault on the drive and verify the drive accepts a start command.
6. **Measure continuity across the STO input terminals** with the safety circuit closed to confirm both channels are energized and there are no open connections in the wiring path.
7. **Contact ABB support or an authorized service center** if the fault persists after verifying all external wiring and safety devices, as internal STO hardware failure is an escalation beyond field repair.

## Parts Often Needed

| Part | Notes |
|------|-------|
| ABB safety relay (compatible model for STO) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-a5a0-fault-code&k=ABB+safety+relay+%28compatible+model+for+STO%29&tag=errorcodefixes-20) \| Replace if the existing safety relay has failed contacts or does not switch both STO channels simultaneously. |
| STO connector jumper or terminal block | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-a5a0-fault-code&k=STO+connector+jumper+or+terminal+block&tag=errorcodefixes-20) \| Use when the drive is installed without external safety devices and requires factory or field-supplied jumpers to close the STO loop. |

## When to Call a Pro

Call a qualified technician or ABB service if you have verified all external wiring, jumpers, and safety devices and the A5A0 fault still appears. Internal STO circuit board failure or complex safety-system integration issues require factory-trained diagnostics and replacement parts that are not field-serviceable. Also call a pro if your facility uses a certified safety system (Category 3 or 4) and you are not trained to work on machine-safety circuits, since improper changes can create hazards or violate safety standards.
