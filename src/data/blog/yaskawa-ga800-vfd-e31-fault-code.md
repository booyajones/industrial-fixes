---
title: "Yaskawa GA800 E31 Fault - Causes & Fix"
description: "E31 on a Yaskawa GA800 VFD means the Safe Torque Off (STO) safety circuit is open. Check the STO jumper or external safety relay."
pubDatetime: 2026-06-05T10:01:44Z
modDatetime: 2026-06-05T10:01:44Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "STO terminal jumper wire"
---

## Yaskawa GA800 E31 Fault — What It Means

The E31 fault on a Yaskawa GA800 variable frequency drive indicates a Safe Torque Off (STO) or safety circuit-related fault. The drive is not seeing a valid STO enable signal on its safety input terminals. This is not a motor overload or inverter problem. The STO function is a built-in safety feature that prevents the drive from producing torque unless the safety circuit is complete and valid.

In practical terms, the drive will not run until the STO input condition is satisfied. If your installation does not use an external safety relay or E-stop chain, the STO terminals must have the factory jumper installed. If you are using external safety devices (such as E-stops, gate switches, or light curtains), those devices must all be closed and feeding a continuous signal to the STO input terminals. The drive will hold the E31 fault and inhibit operation until the safety loop is restored.

[Jump to Fix](#fix)

## Common Causes

- **Missing or removed STO jumper** If the installation runs without external safety devices, the STO terminals require a jumper that may have been removed during installation or service work.
- **Open safety relay or E-stop in the STO chain** Any tripped E-stop, open gate switch, light curtain, or safety relay contact in the STO loop will interrupt the safety signal and trigger the fault.
- **Miswired STO input terminals** Incorrect wiring or loose connections at the STO input terminals after installation or control cabinet changes will prevent the drive from seeing a valid safety condition.
- **Failed safety relay output** A safety relay with a failed or intermittent output contact will cause the STO signal to drop out and the drive to fault.
- **Incorrect terminal assignment or parameterization** If the STO-related terminals were reassigned or control parameters changed, the drive may not recognize the safety input configuration.

## Step-by-Step Fix {#fix}

1. **Verify the fault code** on the drive keypad or operator display and note the exact fault number to confirm it is E31 before proceeding.
2. **Inspect the STO terminal jumper** if your installation does not use external safety devices, and install or reseat the jumper between the STO input terminals as shown in the GA800 wiring diagram.
3. **Check all external safety devices** in the STO chain, including E-stop buttons, gate switches, light curtains, and safety relay contacts, and verify each device is closed and passing continuity.
4. **Examine the STO input terminal wiring** for loose connections, damaged wire insulation, or incorrect terminal assignments, and repair or reconnect any faulty wiring.
5. **Test the safety relay output** if an external safety relay feeds the STO inputs, using a multimeter to confirm the relay is energized and its output contacts are closed when the safety chain is satisfied.
6. **Reset the fault** from the drive keypad or operator after the STO circuit is restored, and observe the drive for normal startup and operation.
7. **Replace the failed safety component** (relay, E-stop, or switch) if the fault returns immediately after reset, and verify the new device restores the STO signal before returning the drive to service.

## Parts Often Needed

| Part | Notes |
|------|-------|
| STO terminal jumper wire | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e31-fault-code&k=STO+terminal+jumper+wire&tag=errorcodefixes-20) \| Factory jumper for installations without external safety control, consult your GA800 wiring diagram for terminal location. |
| Safety relay or safety controller | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e31-fault-code&k=Safety+relay+or+safety+controller&tag=errorcodefixes-20) \| Replacement for failed external relay feeding the STO input chain, must match your existing safety system voltage and contact rating. |
| E-stop button or gate safety switch | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e31-fault-code&k=E-stop+button+or+gate+safety+switch&tag=errorcodefixes-20) \| Replacement for any failed safety interlock device in the STO loop, confirm contact type (normally closed) before ordering. |

## When to Call a Pro

Call a qualified electrician or controls technician if you are not familiar with safety circuit wiring or cannot locate the STO terminals on your drive. If the fault persists after you have confirmed all external safety devices are closed and wiring is correct, the drive's internal safety input circuitry may require factory service or replacement. Any work on industrial VFD safety circuits should be performed by trained personnel familiar with machine safety standards and lockout procedures.
