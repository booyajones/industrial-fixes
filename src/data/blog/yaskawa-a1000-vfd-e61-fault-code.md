---
title: "Yaskawa A1000 VFD E61 Fault - Causes & Fix"
description: "E61 indicates an external thermal relay or overload contact has opened. Check the motor overload relay and its wiring first."
pubDatetime: 2026-07-24T07:34:10Z
modDatetime: 2026-07-24T07:34:10Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "Motor overload relay"
most_likely_cause: "tripped motor overload relay"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Check if the motor overload relay has tripped and reset it manually"
  - "Inspect wiring between the overload relay and the VFD input terminal for loose or broken connections"
  - "Verify the motor is not mechanically jammed or overloaded by checking that the driven equipment turns freely"
part_price: "$30-120"
no_buy_pct: "60%"
---

## Yaskawa A1000 VFD E61 Fault — What It Means

The E61 fault on a Yaskawa A1000 variable frequency drive signals that an external thermal relay or overload protection device has tripped and opened its contact. The drive monitors a dedicated input terminal for external safety devices such as motor overload relays, thermal switches, or other normally-closed contact devices. When this input sees an open circuit, the drive shuts down and displays E61to protect the motor and driven equipment.

This fault does not mean the drive itself has failed. It means something downstream has detected a problem (usually motor overtemperature or overcurrent) and sent the signal back to the drive. The A1000 is simply reporting what the external protective device told it.

## Before You Replace Anything

Technicians sometimes replace the VFD when the external overload relay or its wiring is actually at fault. Always verify continuity on the external safety circuit and inspect the motor overload relay before swapping the drive.

[Jump to Fix](#fix)

## Common Causes

- **Tripped motor overload relay (~50%)** The thermal overload protecting the motor has detected sustained overcurrent and opened its contact.
- **Open wiring or loose terminal (~25%)** A broken wire or loose screw terminal in the external safety circuit between the overload relay and the drive input creates an open circuit.
- **Motor running too hot (~15%)** The motor is drawing excessive current due to a blocked fan, clogged vents, high ambient temperature, or sustained overload on the driven equipment.
- **Faulty overload relay (~7%)** The overload relay itself has failed and remains open even when the motor is not overheating.
- **Incorrect parameter setting (~3%)** The drive parameter for the external fault input is configured incorrectly or the input terminal assignment does not match the actual wiring.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the overload relay reset button pop out or show a trip flag?</summary>
<div class="dtree-body"><strong>Yes:</strong> The relay has tripped. Press the reset button and check for sustained overcurrent or motor overheating before restarting.<br><strong>No:</strong> The relay may not be the issue. Move on to check wiring and terminal continuity.</div>
</details>

<details class="dtree"><summary>Do you measure continuity across the normally-closed contacts of the overload relay when it is reset?</summary>
<div class="dtree-body"><strong>Yes:</strong> The relay contacts are good. Inspect the wiring from the relay to the drive input terminal for breaks or loose connections.<br><strong>No:</strong> The overload relay has failed internally or is still tripped. Replace the relay or verify proper reset procedure.</div>
</details>

<details class="dtree"><summary>Does the motor run without excessive noise, vibration, or mechanical resistance?</summary>
<div class="dtree-body"><strong>Yes:</strong> Mechanical load is normal. Check drive parameters and wiring.<br><strong>No:</strong> A jammed bearing, seized pump, or other mechanical fault is overloading the motor. Fix the mechanical issue before resetting the drive.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect power** to the VFD and motor circuit at the main disconnect and verify zero voltage with a meter.
2. **Locate the motor overload relay** in the circuit between the VFD output and the motor, or in the control panel where external safety devices are wired.
3. **Check the overload relay** for a trip indicator or reset button. If tripped, press the reset button and listen for a click indicating the contacts have closed.
4. **Measure continuity** across the normally-closed contacts of the overload relay using a multimeter. You should see near-zero ohms when the relay is reset.
5. **Trace the wiring** from the overload relay contacts to the VFD external fault input terminal (consult your model's wiring diagram for the correct terminal number). Inspect each connection for tightness and each wire for breaks or damage.
6. **Inspect the motor** for signs of overheating, blocked cooling vents, or mechanical binding. Rotate the motor shaft by hand to check for excessive resistance.
7. **Review drive parameters** for the external fault input. Verify the terminal is enabled and configured as a normally-closed safety contact. Consult your model's parameter table for the specific setting number and options.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor overload relay | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-e61-fault-code&k=Motor+overload+relay&tag=errorcodefixes-20) \| Choose a relay rated for your motor's full-load current; consult the motor nameplate and relay selection chart. |
| Control wiring and terminals | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-e61-fault-code&k=Control+wiring+and+terminals&tag=errorcodefixes-20) \| Use 18 AWG or heavier wire for the external safety circuit; crimp or ferrule all connections. |

## When to Call a Pro

Call a qualified industrial electrician or controls technician if you are not trained to work inside a VFD control panel. High voltage (often 480V or higher) is present even when the drive is in fault mode. The technician will use a multimeter and wiring diagram to trace the external fault circuit, verify continuity, check parameter settings, and diagnose motor or mechanical issues. If the fault persists after resetting the overload and verifying wiring, the problem may lie in drive parameter configuration or a failed input circuit on the drive itself, both of which require experience with VFD commissioning and programming.

**Rough cost:** A pro service call runs about $200-600.
