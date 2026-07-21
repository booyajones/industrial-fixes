---
title: "ABB ACS550 VFD EXT FAULT 1 - Causes & Fix"
description: "External fault input 1 is active. Check that an external device wired to digital input 1 is signaling a problem or wiring is shorted."
pubDatetime: 2026-07-19T07:29:57Z
modDatetime: 2026-07-19T07:29:57Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - abb
money_part: "Replacement pressure switch or temperature sensor"
most_likely_cause: "External device legitimately signaling a fault condition"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Check the owner's manual or parameter list to identify which digital input is programmed as external fault 1"
  - "Inspect the external device wired to that input for visible damage or tripped condition"
  - "Measure continuity across the external device terminals to confirm it is open or closed as expected"
no_buy_pct: "65%"
---

## ABB ACS550 VFD EXT FAULT 1 — What It Means

The EXT FAULT 1 code on an ABB ACS550 variable frequency drive indicates that an external device connected to a programmable digital input has sent a fault signal to the drive. The ACS550 allows users to wire external sensors, pressure switches, emergency stops, or other control devices to digital inputs and configure those inputs to trigger a fault when activated. When the external device closes its contact or sends a signal, the drive trips to protect the motor or process.

This fault is almost always caused by either a legitimate alarm from the connected device (such as a low-pressure switch or high-temperature sensor) or by incorrect wiring and parameter settings. The drive itself is rarely defective. You need to identify which external device is wired to the digital input assigned as external fault 1, verify that device is functioning correctly, and confirm the drive parameters match the intended wiring.

## Before You Replace Anything

Technicians sometimes replace the drive control board when the real issue is a failed pressure switch, temperature sensor, or emergency stop button in the field wiring. Always measure continuity at the external device and verify its set point before ordering drive components.

[Jump to Fix](#fix)

## Common Causes

- **External device legitimately faulted (~45%)** A pressure switch, temperature sensor, flow switch, or emergency stop wired to the fault input has detected an out-of-range condition in the process.
- **Wiring short or ground fault (~25%)** The cable between the external device and the digital input terminal has a short to ground or another conductor, causing a false fault signal.
- **Incorrect parameter configuration (~15%)** The drive parameter assigning the digital input function or its active logic (normally open versus normally closed) does not match the field wiring.
- **Failed external sensor or switch (~10%)** The field device itself has failed in a closed or open state even though the process condition is normal.
- **Loose or corroded terminal connection (~5%)** The screw terminal at the drive or at the external device has loosened or corroded, creating intermittent contact that the drive reads as a fault.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is an external device (pressure switch, E-stop, sensor) physically wired to a digital input terminal on the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> Trace that wire to the field device and test the device for correct operation and set point.<br><strong>No:</strong> Check drive parameters to see if a digital input is mistakenly enabled as external fault 1 with no device connected, then disable or reconfigure the input.</div>
</details>

<details class="dtree"><summary>Does the fault clear immediately when you disconnect the external device wire from the digital input terminal?</summary>
<div class="dtree-body"><strong>Yes:</strong> The external device or its wiring is sending a fault signal; test the device and cable for shorts or legitimate alarm conditions.<br><strong>No:</strong> The drive parameter may be set to the wrong logic polarity or the input circuit inside the drive may be damaged; consult the parameter manual and verify logic settings.</div>
</details>

<details class="dtree"><summary>Does the external device show a tripped or alarm state (LED lit, mechanical flag, or open contact)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Resolve the process condition causing the device to trip (low pressure, high temperature, etc.) then reset the device and the drive.<br><strong>No:</strong> Check for a wiring fault, incorrect parameter logic, or a failed device that is sending a false signal.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive** and lock out the incoming supply to work safely on control wiring.
2. **Locate the digital input terminal** assigned as external fault 1 by consulting the drive parameter list (often parameter group 12 or 30 depending on firmware) and the wiring diagram on the inside of the drive door.
3. **Identify the external device** wired to that terminal, such as a pressure switch, temperature sensor, flow switch, or emergency stop button in the field.
4. **Inspect the external device** for visible damage, correct mounting, and proper set point adjustment; verify the process condition (pressure, temperature, flow) is within normal operating range.
5. **Measure continuity** across the device terminals with a multimeter to confirm the contacts are in the expected state (open or closed) for normal operation.
6. **Check the drive parameters** to verify the digital input function and active logic (normally open or normally closed) match the wiring and device type; reconfigure if necessary.
7. **Inspect the cable** between the drive and the external device for pinched insulation, loose terminals, or signs of water ingress that could cause a short or ground fault; tighten or replace as needed and re-land wires securely at both ends.
8. **Reset the drive** by cycling power or using the front keypad reset function, then monitor for recurrence; if the fault returns immediately, disconnect the external device wire at the drive terminal to isolate whether the fault is in the field wiring or the drive input circuit.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Replacement pressure switch or temperature sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs550-vfd-ext-fault-1-fault-code&k=Replacement+pressure+switch+or+temperature+sensor&tag=errorcodefixes-20) \| Match the voltage rating, set point range, and contact type to the original device specification. |
| Shielded control cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs550-vfd-ext-fault-1-fault-code&k=Shielded+control+cable&tag=errorcodefixes-20) \| Use the same wire gauge and shielding as the original run; consult the drive manual for recommended cable types for digital input wiring. |

## When to Call a Pro

Call a qualified electrician or controls technician if you are not familiar with reading VFD parameter menus, tracing control wiring, or working safely around industrial electrical panels. High-voltage AC input and output terminals are present inside the drive enclosure. A technician can quickly identify which external device is causing the fault, verify wiring polarity and shielding, reprogram parameters to match field conditions, and test the system under load to confirm the fault is resolved.

**Rough cost:** A pro service call runs about $150-400.

## See Also

- [ABB ACS580 A7A4 (7122) Fault - Causes & Fix](/posts/abb-acs580-vfd-a7a4-fault-code/)
- [ABB ACS550 AI2 LOSS Fault - Causes & Fix](/posts/abb-acs550-ai2-loss-fault-code/)
- [ABB ACS580 VFD E0004 Fault Code - Causes & Fix](/posts/abb-acs580-vfd-e0004-fault-code/)
- [ABB ACS580 VFD E0022 Fault - Causes & Fix](/posts/abb-acs580-vfd-e0022-fault-code/)
