---
title: "Yaskawa GA800 E23 Fault - Causes & Fix"
description: "Yaskawa GA800 E23 fault means the external regenerative braking resistor is disconnected or incorrectly wired. Fix by inspecting and repairing the resistor circuit."
pubDatetime: 2026-05-30T12:33:24Z
modDatetime: 2026-05-30T12:33:24Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
---

## Yaskawa GA800 E23 Fault — What It Means

The E23 fault on a Yaskawa GA800 drive indicates a problem with the external regenerative braking resistor circuit. Yaskawa specifically defines this condition as the external regenerative resistor being incorrectly wired, removed, or disconnected. The fault does not point to motor windings, encoder issues, or main input power problems. It is strictly a dynamic braking circuit alarm that prevents the drive from operating until the resistor connection is restored and verified.

This fault appears when the drive cannot detect continuity or proper connection through the external regen resistor terminals. The drive uses this resistor to dissipate energy during deceleration or regenerative braking. If the circuit is open or the resistor is missing, the drive has no safe path to shed that energy and will stop with E23 to protect itself and the application.

[Jump to Fix](#fix)

## Common Causes

- **Open or loose resistor leads** The wiring between the drive terminals and the external regenerative resistor has come loose, broken, or was never properly landed.
- **Resistor removed during service** The external braking resistor was disconnected for maintenance or troubleshooting and not reinstalled before the drive was powered back up.
- **Loose terminal screws or connectors** Terminal hardware at the drive or resistor mounting point has vibrated loose or corroded, opening the circuit.
- **Heat or vibration damage** The resistor leads or terminal block have been damaged by excessive heat cycles or mechanical vibration, causing an intermittent or permanent open.
- **Incorrect resistor installed** A non-approved or wrong-value resistor was installed that the drive cannot recognize or does not meet the circuit requirements for that model.
- **Drive-side circuit failure** If the external resistor and wiring are confirmed intact, the drive's internal braking circuit hardware may have failed and cannot detect the resistor.

## Step-by-Step Fix {#fix}

1. **Remove all power** to the drive and wait for the discharge indicator to go out or follow the manufacturer's safe discharge procedure before opening the enclosure or touching terminals.
2. **Locate the external regenerative resistor** and trace its leads back to the drive terminals, checking every connection point for tightness, corrosion, or physical damage.
3. **Inspect the resistor body and terminals** for signs of overheating, burned leads, cracks, or missing hardware that would open the circuit.
4. **Verify the resistor is the correct Yaskawa-approved part** for your GA800 model by consulting the drive nameplate and accessory documentation, and replace if the installed unit does not match.
5. **Repair or replace any damaged wiring, terminals, or connectors** in the regenerative resistor circuit, and confirm continuity from drive terminal to resistor and back.
6. **Restore power and reset the fault** from the drive keypad once the resistor circuit has been corrected and all connections are secure.
7. **If the E23 fault returns immediately** with a known-good resistor and verified wiring, suspect a drive internal circuit fault and contact Yaskawa support or an authorized service center for drive-level diagnostics.

## Parts Often Needed

| Part | Notes |
|------|-------|
| External regenerative braking resistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-e23-fault-code&k=External+regenerative+braking+resistor&tag=errorcodefixes-20) \| Must match the Yaskawa-approved rating and model for your GA800 frame size. Consult drive documentation for the correct part number. |
| Resistor wiring harness or lead set | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-e23-fault-code&k=Resistor+wiring+harness+or+lead+set&tag=errorcodefixes-20) \| Replace if conductors are broken, insulation is damaged, or terminals are burned. Use wire gauge and insulation rating per Yaskawa specifications. |
| Terminal block hardware and connectors | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-e23-fault-code&k=Terminal+block+hardware+and+connectors&tag=errorcodefixes-20) \| Replace any corroded, cracked, or loose terminal screws, lugs, or connector bodies in the regenerative resistor circuit. |

## When to Call a Pro

Call a qualified technician or contact Yaskawa support if you have confirmed the external regenerative resistor is correctly installed and wired but the E23 fault continues to appear. This indicates a possible drive-side hardware failure in the braking circuit that requires advanced diagnostics and access to service-level documentation. Also call a professional if you are not trained in high-voltage drive systems or do not have the tools to safely verify circuit continuity and proper grounding. Drive circuits store dangerous voltage even after power removal, and incorrect work on the braking resistor circuit can damage the drive or create a safety hazard.
