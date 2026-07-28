---
title: "Yaskawa GA800 A.120 Fault - Causes & Fix"
description: "A.120 means serial communication transmission error. Usually caused by wrong cable wiring, a short, or a loose connection. Fix by checking and repairing the communications cable."
pubDatetime: 2026-06-08T11:15:59Z
modDatetime: 2026-06-08T11:15:59Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
most_likely_cause: "incorrect communications cable wiring or a disconnected cable"
likelihood: "the most common cause"
diy_or_pro: "pro"
money_part: "Shielded twisted-pair communications cable"
---

## What this code means
The A.120 fault on a Yaskawa GA800 variable frequency drive indicates a serial communication transmission error in the drive's communication link. This alarm tells you that the drive cannot maintain a reliable data connection with an external controller, network, or operator interface because of a problem in the physical cabling or wiring between the drive and the other device.

The fault does not point to internal drive electronics failing. Instead it flags an issue in the pathway that carries serial commands and feedback data to and from the drive. Common fieldbus protocols (Modbus RTU, DeviceNet, or others depending on your option card) all rely on correctly wired twisted-pair or shielded cable. Any break, short, or mis-termination in that cable will trigger A.120 and halt communication-dependent operations.

## Before You Replace Anything

Technicians sometimes replace the communication option card or even the entire control board when the real problem is a damaged or incorrectly wired field cable. Always inspect and verify the cable wiring and continuity with a multimeter before swapping boards.

## Common Causes

- **Wrong wiring of the communications cable (~40%)** Terminal assignments (TX, RX, shield, ground) do not match the protocol standard or the receiving device, preventing handshake and data exchange.
- **Shorted or damaged cable conductors (~30%)** Pinched insulation, rodent damage, or environmental wear creates a short circuit between signal pairs or between signal and ground.
- **Disconnected or loose cable connection (~20%)** A terminal screw backed out, a connector not fully seated, or a broken crimp causes intermittent or total loss of the communication path.
- **Incorrect cable type or missing termination resistors (~10%)** Using unshielded or non-twisted-pair cable, or failing to install termination resistors at each end of a long bus, distorts the signal and triggers transmission errors.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is the communications cable securely connected at both the drive terminals and the remote device?</summary>
<div class="dtree-body"><strong>Yes:</strong> The physical connection is good. Move on to checking for shorts or incorrect wiring inside the cable.<br><strong>No:</strong> Reseat or reconnect the cable at both ends, tighten terminal screws to the torque specified in the GA800 manual, then reset the drive and test.</div>
</details>

<details class="dtree"><summary>Does the cable show visible damage (cuts, abrasion, pinch marks, or rodent chewing)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Replace the damaged section or the entire cable run. Use shielded twisted-pair cable rated for your protocol.<br><strong>No:</strong> Damage is not obvious. Use a multimeter to check conductor continuity and measure resistance between signal wires and between each wire and shield or ground to find hidden shorts.</div>
</details>

<details class="dtree"><summary>Does the alarm clear after you disconnect the communications cable from the drive and reset the fault?</summary>
<div class="dtree-body"><strong>Yes:</strong> The drive hardware is fine. The problem is in the cable, the remote device, or the network configuration. Inspect wiring pin-out and verify protocol settings.<br><strong>No:</strong> The alarm persists even with the cable disconnected. The communication interface hardware inside the drive may be damaged. Contact Yaskawa technical support with your model number, serial number, and fault details.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify the fault code** on the drive keypad and note which communication path is affected (for example, the RJ45 Ethernet port, RS-485 terminals, or an option-card connector).
2. **Power down** the machine and the GA800 drive, then lock out and tag out all upstream circuit breakers to work safely on wiring.
3. **Inspect the communications cable** at both ends for loose terminal screws, broken or frayed conductors, and correct pin or terminal assignments against the wiring diagram in your GA800 manual or the protocol specification sheet.
4. **Check for shorts and opens** with a multimeter: measure continuity through each conductor from end to end, and measure resistance between signal pairs and between each signal wire and shield or ground to detect shorts.
5. **Repair or replace** any damaged, shorted, or incorrectly wired section of cable, and confirm that the cable type (shielded twisted-pair, correct impedance) and any required termination resistors match the protocol requirements.
6. **Restore power**, clear the A.120 fault by pressing the RESET key on the keypad while the alarm code is displayed, and confirm that serial communication resumes without errors.
7. **If the alarm persists** after correcting the cable, escalate to Yaskawa technical support with the drive model and specification number, serial number, the A.120 code, and a description of the steps you have already taken.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Shielded twisted-pair communications cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-120-fault-code&k=Shielded+twisted-pair+communications+cable&tag=errorcodefixes-20) \| Match the cable type (for example, 18 AWG two-conductor shielded for RS-485 Modbus) to your protocol and run length. Consult the GA800 manual appendix for cable specifications. |
| Termination resistor (if required by protocol) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-120-fault-code&k=Termination+resistor+%28if+required+by+protocol%29&tag=errorcodefixes-20) \| Typically 120 Ω for RS-485 networks. Install one at each physical end of the bus. |

## When to Call a Pro

Call a qualified automation or electrical technician if you are not trained to work safely around industrial line voltage and control wiring, if you cannot access the wiring diagram or protocol specification for your system, or if the alarm returns after you have verified and repaired the cable. Also call a professional if the A.120 fault persists even with the communications cable disconnected, because that pattern suggests hardware damage inside the drive or the remote controller that requires factory-trained diagnosis and possible board replacement. Yaskawa technical support can walk a qualified technician through advanced diagnostics and provide replacement part numbers for communication option cards or control boards when field wiring is confirmed correct.

**Rough cost:** A pro service call runs about $150–400 depending on cable length and routing labor.
