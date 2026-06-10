---
title: "Yaskawa GA800 A.114 Fault - Causes & Fix"
description: "A.114 on a Yaskawa GA800 indicates a serial communication transmission error. Most often caused by incorrect wiring or a damaged cable."
pubDatetime: 2026-06-08T11:07:53Z
modDatetime: 2026-06-08T11:07:53Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
most_likely_cause: "incorrect or damaged communications wiring"
likelihood: "the most common cause"
diy_or_pro: "pro"
---

## Yaskawa GA800 A.114 Fault — What It Means

The A.114 fault on a Yaskawa GA800 variable frequency drive is a serial communication transmission error. This means the drive has detected a problem in the communication path between the VFD and an external device or network. The fault typically appears when there is incorrect wiring on the communications circuit, a short circuit in the communication cable, or a disconnected or open cable in the communications path. If your drive uses an optional network or fieldbus card, the fault can also indicate poor seating of the option card or poor connector contact.

Unlike motor or power section faults, this code points specifically to the control and data wiring rather than the driven load or power components. The GA800 manual instructs you to remove the cause of the fault or alarm first, then press the RESET button on the keypad to clear the code. If the fault returns immediately after reset, the underlying wiring defect or card seating issue has not been corrected and further inspection or component substitution is required.

## Before You Replace Anything

Technicians sometimes replace the control board or option card before checking the cable and terminals. Always inspect and test the communication cable for shorts, opens, and correct terminal connections first, since wiring defects account for most A.114 faults.

[Jump to Fix](#fix)

## Common Causes

- **Incorrect wiring on the communications circuit (~40%)** Reversed terminals, wrong conductor assignments, or connections to the wrong terminal block cause the drive to lose valid data frames and trigger the transmission error.
- **Short circuit in the communication cable (~25%)** Pinched insulation, nicked conductors, or a crushed cable can short signal lines together or to shield or ground, corrupting the data stream.
- **Disconnected or open cable (~20%)** A loose terminal screw, broken conductor, or unplugged connector interrupts the communication path entirely and generates the fault immediately.
- **Poorly seated communication option card (~10%)** If the drive uses a network or fieldbus option card, inadequate engagement in the slot or contaminated connector pins can cause intermittent or persistent loss of communication.
- **Failed communication option card or control board (~5%)** After wiring and seating are verified correct, the option card or the drive's control board itself may have failed and require replacement per Yaskawa service parts guidance.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is a communication cable visibly damaged, pinched, or disconnected?</summary>
<div class="dtree-body"><strong>Yes:</strong> Repair or replace the cable section and verify correct terminal connections before attempting to clear the fault.<br><strong>No:</strong> Proceed to inspect the option card seating and control board connector integrity.</div>
</details>

<details class="dtree"><summary>Does the drive use an optional network or fieldbus card?</summary>
<div class="dtree-body"><strong>Yes:</strong> Power down safely, reseat the card firmly, inspect connector pins for damage or contamination, then power up and check if the fault clears.<br><strong>No:</strong> The fault is on the drive's built-in serial port. Verify wiring to the external device and check for configuration mismatches.</div>
</details>

<details class="dtree"><summary>Does the fault return immediately after pressing RESET?</summary>
<div class="dtree-body"><strong>Yes:</strong> The underlying cause has not been corrected. Isolate by substitution with a known-good cable, option card, or by testing the connected device on another drive.<br><strong>No:</strong> The wiring or seating correction was successful. Monitor the drive during normal operation to confirm the fault does not recur.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive safely** and wait for all indicators to extinguish before touching any wiring or internal components, following all Yaskawa safety precautions for high-voltage equipment.
2. **Inspect the communication wiring** at both the drive terminals and the remote device for reversed or incorrect terminal assignments, loose screws, nicked insulation, pinched cable sections, and any visible shorts between conductors or to shield or ground.
3. **If an option or network card is installed**, remove power, open the drive enclosure per the service manual, and carefully reseat the card by pressing it firmly into the slot, then inspect the connector and pins for mechanical damage, corrosion, or poor engagement.
4. **Correct any wiring defect** by repairing damaged cable sections, re-terminating conductors to the correct terminals per the wiring diagram, and ensuring all terminal screws are torqued to specification.
5. **Restore power and press the RESET button** on the keypad while the A.114 code is displayed to clear the fault, only after you have removed the cause.
6. **If the code returns immediately**, isolate the problem by substitution testing with a known-good communication cable, testing the option card in a different slot or drive, or swapping the connected remote device with a verified working unit.
7. **Replace the communication option card or control board** if troubleshooting points to drive electronics and reseating does not resolve the fault, using Yaskawa service parts appropriate for your GA800 model.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Communication cable (shielded twisted pair or fieldbus-rated) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-114-fault-code&k=Communication+cable+%28shielded+twisted+pair+or+fieldbus-rated%29&tag=errorcodefixes-20) \| Replace if damaged, shorted, or open. Match the cable type and gauge to your network specification. |
| Yaskawa GA800 communication option card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-114-fault-code&k=Yaskawa+GA800+communication+option+card&tag=errorcodefixes-20) \| Order the correct network interface card (DeviceNet, Profibus, EtherNet/IP, etc.) for your application if reseating does not resolve the fault. |
| Yaskawa GA800 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-114-fault-code&k=Yaskawa+GA800+control+board&tag=errorcodefixes-20) \| Field-replaceable per Yaskawa service documentation. Replace only if the fault follows the drive electronics after wiring and option card are verified good. |

## When to Call a Pro

Call a qualified VFD technician or industrial electrician if you are not trained to work safely around high-voltage motor drive equipment, if the fault persists after you have inspected and corrected visible wiring defects, or if you need to replace the control board or option card and are unfamiliar with drive enclosure procedures. Communication troubleshooting on industrial networks often requires protocol analyzers, network configuration tools, and familiarity with fieldbus standards that are beyond typical facility maintenance scope. A pro can also verify that device addresses, baud rates, and protocol parameters match across the entire communication link, which is essential when wiring inspection alone does not resolve the fault.

**Rough cost:** A pro service call runs about $150-400 for diagnosis and cable or option card replacement.
