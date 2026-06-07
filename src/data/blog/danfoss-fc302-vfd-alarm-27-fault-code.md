---
title: "Danfoss FC302 Alarm 27 - Causes & Fix"
description: "Alarm 27 on Danfoss FC302 VFD signals a brake chopper or brake IGBT fault. Check brake resistor wiring and replace if shorted."
pubDatetime: 2026-06-04T09:09:33Z
modDatetime: 2026-06-04T09:09:33Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - danfoss
---

## Danfoss FC302 Alarm 27 — What It Means

Alarm 27 on the Danfoss VLT AutomationDrive FC 302 indicates a brake chopper or brake IGBT fault. The drive continuously monitors the brake IGBT circuit during operation and raises this alarm when that circuit fails or when the brake resistor circuit is shorted or overloaded. The brake chopper is the transistorized circuit that dumps DC-bus energy into the brake resistor during deceleration, so damage to either component will trigger this fault.

This is not a terminal 27 wiring issue. Warning 40 covers overload of digital output terminal 27, which is a separate code. Alarm 27 is specifically tied to the internal braking hardware and the external brake resistor circuit.

[Jump to Fix](#fix)

## Common Causes

- **Shorted or damaged brake resistor** The external brake resistor can fail short-circuit or open-circuit, or its wiring can be damaged or incorrectly connected, causing the drive to detect a fault in the brake chopper circuit.
- **Failed brake IGBT or chopper circuit** The internal brake IGBT transistor inside the drive can fail open or shorted, preventing proper dissipation of regenerative energy during deceleration.
- **Excessive regenerative energy** Fast deceleration, high load inertia, or an undersized brake resistor can overwork the brake chopper and cause thermal or electrical failure of the braking circuit.
- **Thermal stress or overheating** High ambient temperature, blocked airflow, failed cooling fans, or a defective IGBT thermal sensor can lead to overheating in the drive power section and brake chopper.
- **Soft-charge fuse failure** Blown soft-charge fuses in the drive's internal power section can be part of the fault path and prevent proper operation of the brake circuit.
- **Incorrect brake resistor specification** Installing a brake resistor with the wrong resistance value or power rating for the application can cause the chopper circuit to fail under load.

## Step-by-Step Fix {#fix}

1. **Lock out and tag out all power** to the drive and wait for DC-bus capacitors to discharge completely before opening the enclosure or touching any brake circuit wiring.
2. **Inspect the brake resistor wiring and connections** at the drive terminals for signs of damage, loose connections, arcing, or discoloration that would indicate overheating or a short.
3. **Disconnect the brake resistor** from the drive and test its resistance with a multimeter to confirm it is not shorted or open, and verify the value matches the specification for your drive model.
4. **Check the drive cooling system** by inspecting fans, heatsink airflow paths, and ambient temperature to confirm the unit is not overheating, and verify the IGBT thermal sensor is functioning if accessible.
5. **Test the soft-charge fuses** inside the drive power section according to the manufacturer's service manual to rule out an internal power fault.
6. **Replace the brake resistor** if it failed testing, ensuring the new resistor matches the resistance and power rating specified for the FC 302 application.
7. **Restore power and clear the alarm** through the drive's control panel, then run the drive under normal braking load and monitor for recurrence of the fault code.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Brake resistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-27-fault-code&k=Brake+resistor&tag=errorcodefixes-20) \| Must match the resistance and power rating specified for your FC 302 model and application. Consult the drive's documentation for the correct value. |
| Soft-charge fuses | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-27-fault-code&k=Soft-charge+fuses&tag=errorcodefixes-20) \| Internal fuses in the drive power section. Check the FC 302 service manual for correct type and rating before replacement. |
| IGBT thermal sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-27-fault-code&k=IGBT+thermal+sensor&tag=errorcodefixes-20) \| Only if diagnostics confirm sensor failure. This is an internal component requiring advanced repair skills. |
| Brake chopper power assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-27-fault-code&k=Brake+chopper+power+assembly&tag=errorcodefixes-20) \| Internal drive component. If the brake IGBT itself has failed, replacement typically requires factory service or a qualified drive repair center. |

## When to Call a Pro

Call a qualified industrial electrician or VFD technician if the brake resistor tests good and the fault persists, since internal brake IGBT or chopper circuit failure requires specialized tools and training to diagnose and repair. Also call a professional if you are not familiar with high-voltage DC-bus capacitor discharge procedures or if the drive requires replacement of internal power components like the brake chopper assembly or soft-charge fuses. Any work inside the drive enclosure involves lethal voltages and should only be performed by personnel trained in VFD service.

## See Also

- [Danfoss FC302 Alarm 23 - Causes & Fix](/posts/danfoss-fc302-alarm-23-fault-code/)
- [Danfoss FC302 Alarm 43 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-43-fault-code/)
- [Danfoss FC302 Alarm 22 - Hoist Brake Fault Fix](/posts/danfoss-fc302-vfd-alarm-22-fault-code/)
- [Danfoss FC302 Alarm 25 - Causes & Fix](/posts/danfoss-fc302-alarm-25-fault-code/)
