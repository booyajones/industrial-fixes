---
title: "Danfoss FC302 Alarm 14 - Causes & Fix"
description: "Alarm 14 on a Danfoss FC302 VFD means earth fault: current is leaking to ground. Usually a bad motor cable or motor winding insulation."
pubDatetime: 2026-06-03T10:35:42Z
modDatetime: 2026-06-03T10:35:42Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Motor cable (shielded VFD-rated)"
most_likely_cause: "Motor winding insulation breakdown"
---

## What this code means
Alarm 14 on the Danfoss FC302 is an earth fault (ground fault). The drive has detected current leaking from the motor output circuit to ground instead of flowing through the U, V, and W motor windings. This leakage can occur in the motor itself, the motor cable, or inside the drive's inverter section. The fault protects the drive and motor from unsafe ground currents that can damage equipment or create safety hazards.

In practical terms, the drive is measuring output current that is not returning through the motor circuit as expected. The protection circuit trips to prevent further damage. The fault can be external (motor or cable insulation breakdown) or internal to the drive (faulty current sensor or power section component).

## Common Causes

- **Motor winding insulation breakdown** Moisture, contamination, or aging can degrade the motor winding insulation and allow current to leak to the motor frame and ground.
- **Damaged motor cable insulation** Cuts, abrasion, or deterioration of the motor cable insulation at conduit entries, junction boxes, or along the cable run allows current to reach ground.
- **Loose or incorrect wiring** Poor connections at the drive output terminals, motor junction box, or intermediate terminations can create intermittent ground paths or arcing.
- **Faulty current sensor inside the drive** A defective current sensor in the VFD can falsely report ground current even when none exists, and Danfoss identifies this as the most likely internal cause if the fault persists with the motor disconnected.
- **Internal drive power section failure** Failed IGBTs or power board components inside the inverter can create real ground leakage paths within the drive itself.

## Step-by-Step Fix {#fix}

1. **De-energize and lock out** the FC302 VFD and wait for internal capacitors to discharge before opening any covers or touching wiring.
2. **Inspect and tighten all output connections** at the drive U, V, W terminals, the motor junction box, and any intermediate junction boxes or conduit entries.
3. **Disconnect the motor leads from the drive** output terminals (note their positions first) and attempt to reset the drive and run it without the motor connected.
4. **If the drive still trips Alarm 14 with the motor disconnected**, the fault is inside the drive. Danfoss guidance points to a faulty current sensor as the most likely cause, especially if the displayed current reads greater than 0.3 A with no motor connected.
5. **If the drive runs normally with the motor disconnected**, the problem is in the motor or motor cable. Use a 1000 volt megohmmeter to test insulation resistance from each motor lead to ground and between phases.
6. **Repair or replace the motor cable** if insulation testing shows breakdown or if you find visible damage to the cable jacket, conduit fittings, or terminal blocks.
7. **If the motor insulation tests low**, the motor windings have failed and the motor requires rewind or replacement. If insulation tests pass but the fault remains, recheck all terminations and cable routing for intermittent contact with grounded metal.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor cable (shielded VFD-rated) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-14-fault-code&k=Motor+cable+%28shielded+VFD-rated%29&tag=errorcodefixes-20) \| Match the wire gauge and length to your original installation and use cable rated for variable frequency drive duty. |
| Danfoss FC302 current sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-14-fault-code&k=Danfoss+FC302+current+sensor&tag=errorcodefixes-20) \| Required if internal diagnostics confirm the sensor is faulty. Contact Danfoss service or an authorized repair center for the correct sensor for your drive frame size. |
| Replacement motor (same frame and HP) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-14-fault-code&k=Replacement+motor+%28same+frame+and+HP%29&tag=errorcodefixes-20) \| Needed if megohm testing confirms the motor winding insulation has failed and cannot be economically repaired. |

## When to Call a Pro

Call a qualified electrician or VFD technician if you are not trained in high-voltage electrical work or if the fault persists with the motor disconnected (indicating an internal drive problem). Internal drive repairs require specialized knowledge, proper test equipment, and access to Danfoss service parts. If you have confirmed the motor or cable is at fault through insulation testing, a motor shop or electrical contractor can replace the cable or motor. Any work inside the drive cabinet should be performed only by personnel familiar with inverter power sections and current-sensor diagnostics.
