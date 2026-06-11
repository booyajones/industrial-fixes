---
title: "Siemens Micromaster F0085 - Causes & Fix"
description: "F0085 means External Fault: an input terminal stopped the drive. Check which digital input is wired for fault and fix the tripped device."
pubDatetime: 2026-06-02T10:41:33Z
modDatetime: 2026-06-02T10:41:33Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Replacement external fault device (relay, switch, or interlock)"
---

## Siemens Micromaster F0085 — What It Means

F0085 on a Siemens Micromaster 420 or 440 VFD indicates an External Fault. The drive has been tripped by a signal on a control terminal that is configured to stop the inverter when activated. This is not an internal power-stage failure. Instead, an external device or input wired to the drive's digital terminals is holding the fault condition active, preventing the drive from running.

[Jump to Fix](#fix)

## Common Causes

- **Digital input configured for external fault is active** A terminal programmed as an external-fault input is seeing a closed contact or active signal from an upstream device.
- **E-stop, safety interlock, or permissive chain is open** A field device such as an emergency stop button, pressure switch, float switch, overload relay, or thermal contact is intentionally tripping the drive through the external-fault input.
- **Loose or damaged control wiring** Terminal screws, cable continuity, or connections in the external-fault circuit are faulty, causing the input to change state unexpectedly.
- **Failed external device or contact** A relay, switch, or auxiliary contact in the fault chain has failed and is holding the input active even though the process condition is normal.
- **Miswired terminal assignment** The external-fault input is connected to the wrong terminal or is picking up a signal that should not trigger a fault.

## Step-by-Step Fix {#fix}

1. **Verify the fault code** on the drive keypad or display and confirm the drive model is a Micromaster 420 or 440.
2. **Identify which digital input** is assigned to external fault by reviewing the drive parameters and control wiring diagram for your machine.
3. **Inspect the external-fault circuit** end-to-end, including all safety devices, auxiliary contacts, terminal screws, cable runs, and any interposing relays.
4. **Check whether the input is held active** by a legitimate device trip (process condition, E-stop, overload) or by a wiring or configuration problem.
5. **Test the external devices** one by one if possible, bypassing or temporarily disabling the fault input only if machine design and safety rules permit, to isolate the source of the signal.
6. **Correct the root cause**, whether that means resetting a tripped device, repairing wiring, or reconfiguring the terminal assignment, then restore the external permissive chain.
7. **Reset the drive** and verify that F0085 clears and the drive runs normally. If the fault persists after the circuit is proven good, consult Siemens service or run the drive's self-test procedures to check for an inverter hardware issue.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Replacement external fault device (relay, switch, or interlock) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-vfd-f0085-fault-code&k=Replacement+external+fault+device+%28relay%2C+switch%2C+or+interlock%29&tag=errorcodefixes-20) \| Use if a field device in the fault chain has failed and is holding the input active. |
| Control terminal wiring and connectors | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-vfd-f0085-fault-code&k=Control+terminal+wiring+and+connectors&tag=errorcodefixes-20) \| Replace damaged cables or terminal blocks in the external-fault input circuit. |
| Siemens Micromaster inverter/converter module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-vfd-f0085-fault-code&k=Siemens+Micromaster+inverter%2Fconverter+module&tag=errorcodefixes-20) \| Required only if self-test and circuit verification point to a fault in the drive itself, consult Siemens service for the correct replacement part number for your model. |

## When to Call a Pro

Call a qualified electrician, controls technician, or Siemens-authorized service provider if you cannot identify which terminal is assigned to external fault, if the wiring diagram is missing, if the fault persists after verifying and correcting the external circuit, or if you are unfamiliar with VFD parameter programming and safe lockout procedures. External-fault circuits often tie into machine safety systems, so any work must comply with electrical codes and occupational safety requirements for your facility.
