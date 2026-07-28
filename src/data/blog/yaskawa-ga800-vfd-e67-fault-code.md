---
title: "Yaskawa GA800 E67 Fault - Causes & Fix"
description: "E67 on a Yaskawa GA800 means serial communication transmission error. The most common fix is inspecting and correcting comm wiring."
pubDatetime: 2026-06-06T11:51:06Z
modDatetime: 2026-06-06T11:51:06Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
most_likely_cause: "Incorrect wiring, loose connection, or damaged serial communication cable"
likelihood: "the most common cause"
diy_or_pro: "pro"
money_part: "Serial communication cable"
---

## What this code means
E67 on a Yaskawa GA800 VFD is a serial communication transmission error. The drive has lost or cannot establish proper communication over its serial link. This fault typically points to a problem in the physical wiring, termination, or connection of the communication cable, or in the option card if a network module is installed.

The GA800 will trigger E67 when it detects incorrect comms wiring, an open or disconnected comms cable, or a short circuit in the comms conductors. It can also appear if a communication option board is not fully seated or has damaged pins. The drive cannot continue normal operation until the communication path is restored and the fault is cleared.

## Before You Replace Anything

Technicians sometimes replace the communication option card or even the main control board before checking the field wiring. Always inspect the comm cable end to end for loose terminals, reversed conductors, and shorts before ordering any parts.

## Common Causes

- **Incorrect wiring or pinout** The serial communication cable is wired with reversed conductors, wrong terminal assignments, or incorrect shielding connections.
- **Loose or unplugged communications wiring** A terminal screw is loose, a connector is not fully seated, or the cable has pulled out of the drive or network device.
- **Shorted or damaged comms cable** Conductors are shorted together or broken inside the cable, often at flex points, conduit entries, or field terminations.
- **Badly seated or damaged option card** The communication option module is not fully inserted into its slot, has bent connector pins, or poor contact at the backplane.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is the communication cable plugged in at both the drive and the network device or controller?</summary>
<div class="dtree-body"><strong>Yes:</strong> The cable is connected. Move to inspecting wiring pinout and checking for shorts or damage in the cable run.<br><strong>No:</strong> Reconnect the cable firmly at both ends, check that terminals are tight, and clear the fault to test.</div>
</details>

<details class="dtree"><summary>Does the drive have a communication option card or network module installed?</summary>
<div class="dtree-body"><strong>Yes:</strong> Remove and reseat the option card, inspect for bent pins or corrosion, and verify the card is the correct model for your network.<br><strong>No:</strong> The fault is in the field wiring. Focus on verifying cable pinout, shield grounding, and conductor continuity.</div>
</details>

<details class="dtree"><summary>Does the fault clear immediately after power cycling the drive with comms disconnected?</summary>
<div class="dtree-body"><strong>Yes:</strong> The drive itself is likely fine. The problem is in the cable, termination, or upstream network device. Verify wiring and test with a known-good cable.<br><strong>No:</strong> The fault may be latched or there is a persistent short. Clear the alarm from the keypad after fixing the wiring, or contact Yaskawa support with the model, serial, and fault details if wiring checks pass.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Note the fault code and communication path** from the GA800 keypad and consult the drive's elementary diagram to identify which serial port or option is in use.
2. **Inspect the serial communication cable** end to end for loose terminals, reversed or incorrectly landed conductors, missing shield connections, and physical damage at flex points and conduit entries.
3. **Test the cable for shorts and continuity** using a multimeter, checking each conductor pair and verifying that shield is not shorted to any signal wire.
4. **If a communication option card is installed**, power down the drive, remove the card, inspect the connector and backplane pins for damage or corrosion, then reseat the card firmly and verify all mounting screws or clips are secure.
5. **Correct any wiring faults** by re-terminating conductors to match the wiring diagram, replacing damaged sections of cable, and tightening all terminal screws.
6. **Clear the E67 fault** from the keypad and restore power to the drive and network, then monitor for fault recurrence during normal operation.
7. **If the fault persists after field wiring and option card checks**, gather the drive model and spec number, serial number, fault code, and application details and contact Yaskawa technical support for advanced diagnostics.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Serial communication cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e67-fault-code&k=Serial+communication+cable&tag=errorcodefixes-20) \| Replace if conductors are broken, shorted, or damaged beyond repair. Verify cable type and pinout match the GA800 port and network standard in use. |
| Communication option card or network module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e67-fault-code&k=Communication+option+card+or+network+module&tag=errorcodefixes-20) \| Order the correct Yaskawa option part number for your network (DeviceNet, Profibus, EtherNet/IP, etc.) if the existing card has bent pins or fails after reseating. |

## When to Call a Pro

Call a qualified VFD technician or system integrator if you are not familiar with industrial serial communication standards, do not have wiring diagrams for the drive and network, or if the fault persists after verifying cable continuity and option card seating. Communication troubleshooting often requires specialized test equipment, knowledge of network topology, and access to Yaskawa's support resources. If the drive is part of a larger automation system, involve the controls engineer or original installer to avoid disrupting other devices on the network.

**Rough cost:** A pro service call runs about $150-400 depending on cable run and option card.
