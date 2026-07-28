---
title: "Danfoss FC302 ALARM 25 - Causes & Fix"
description: "ALARM 25 on a Danfoss FC302 VFD means brake resistor short circuit. The drive disables braking. Replace the brake resistor first."
pubDatetime: 2026-06-03T10:37:43Z
modDatetime: 2026-06-03T10:37:43Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss brake resistor"
most_likely_cause: "Failed brake resistor with internal short"
---

## What this code means
ALARM 25 (also called WARNING 25) on the Danfoss FC302 variable frequency drive indicates a brake resistor short-circuit fault. The drive continuously monitors the brake resistor and brake IGBT chopper circuit for short-circuit conditions during operation. When this fault occurs, the drive disables the dynamic braking function but may continue to run the motor. The warning protects the drive and signals that the brake resistor circuit has failed.

The drive also performs a brake resistor disconnection test at power-up, so related brake circuit faults can appear at startup or during heavy deceleration when the brake would normally engage. Loss of the brake function means the drive cannot safely dissipate regenerative energy during rapid stops, which can lead to overvoltage trips or longer deceleration times.

## Common Causes

- **Failed brake resistor with internal short** The brake resistor itself has burned out or developed an internal short circuit, the most common cause of ALARM 25.
- **Shorted brake IGBT or chopper section** The brake chopper power component inside the drive has failed short, triggering the fault even with a good external resistor.
- **Damaged brake resistor wiring or connections** Insulation failure, loose terminals, or conductor-to-ground contact in the brake resistor wiring creates a short-circuit path.
- **Heat damage from sustained overload** Repeated high-energy braking cycles without adequate cooling can char insulation and short the resistor windings or terminals.
- **Incorrect brake resistor installation** Wrong resistor value, reversed polarity, or missing insulation during installation can produce a short-circuit condition on power-up.

## Step-by-Step Fix {#fix}

1. **Disconnect all power** to the VFD and verify with a meter that DC bus capacitors have discharged before opening any enclosure or touching the brake circuit.
2. **Inspect the brake resistor and wiring** for visible heat damage, melted insulation, charred terminals, loose connections, or any conductor touching the enclosure or another conductor.
3. **Measure the brake resistor resistance** with a multimeter after disconnecting it from the drive. Compare the reading to the resistor nameplate value. A near-zero reading confirms an internal short.
4. **Disconnect the brake resistor leads** from the drive terminals and clear the fault. Power up the drive (without load if possible) to see if ALARM 25 returns. If the alarm clears, the external resistor or wiring is faulty.
5. **Replace the brake resistor** if your ohm test or visual inspection shows damage. Match the resistance and wattage rating to the original specification or consult the FC302 sizing guide for your frame size.
6. **Test the drive brake chopper** by reconnecting a known-good brake resistor. If ALARM 25 persists with good wiring and resistor, the internal brake IGBT or chopper circuit has failed and requires drive power-section repair or replacement.
7. **Verify brake option settings** in the drive parameters after repair. Confirm the brake function is enabled, the resistor value is entered correctly if required, and run a controlled deceleration test to prove braking works without faults.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss brake resistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-25-fault-code&k=Danfoss+brake+resistor&tag=errorcodefixes-20) \| Match ohm and watt rating to your FC302 frame size and braking duty. First component to replace when ALARM 25 is confirmed. |
| Brake resistor wiring kit or terminal lugs | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-25-fault-code&k=Brake+resistor+wiring+kit+or+terminal+lugs&tag=errorcodefixes-20) \| High-temperature wire and crimp terminals rated for the brake circuit current. Use when existing wiring shows heat damage or poor connections. |
| FC302 power section or brake chopper module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-25-fault-code&k=FC302+power+section+or+brake+chopper+module&tag=errorcodefixes-20) \| Required if the brake IGBT inside the drive has failed short. Availability varies by frame. Contact Danfoss or an authorized service center for serviceability. |

## When to Call a Pro

Call a qualified VFD technician or industrial electrician if you are not trained to work on live DC bus circuits or high-power brake resistors. If the alarm persists after you have replaced the brake resistor and verified all wiring, the internal brake chopper has likely failed and requires component-level drive repair or a new power section. A technician can perform safe DC bus discharge, measure brake IGBT gate signals, and access manufacturer service parts. Also call a pro if your application involves regenerative loads like cranes or centrifuges where loss of braking creates a safety hazard or if your facility requires arc-flash PPE and lockout procedures beyond your training.
