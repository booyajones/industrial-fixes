---
title: "Yaskawa GA800 E88 Fault - Causes & Fix"
description: "E88 on Yaskawa GA800 means Safe Torque Off (STO) circuit is open. Most common fix: check safety relay, E-stop, or STO jumper wiring."
pubDatetime: 2026-06-08T10:43:20Z
modDatetime: 2026-06-08T10:43:20Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
most_likely_cause: "Open STO circuit from safety relay, E-stop, or missing jumper"
likelihood: "the most common cause"
diy_or_pro: "pro"
money_part: "Safety relay (Pilz, Schmersal, or machine OEM)"
---

## Yaskawa GA800 E88 Fault — What It Means

The E88 fault on a Yaskawa GA800 VFD indicates that the Safe Torque Off (STO) safety circuit is not satisfied. The drive is designed to prevent torque output unless the STO input terminals see a valid permissive signal from the external safety chain. When this circuit is open or the safety relay is not energized, the drive refuses to run and displays E88.

This is not a motor overload or internal drive failure. The fault exists specifically to enforce the safety interlock. The drive will remain inhibited until the STO input path is correctly wired and closed, typically by energizing a safety relay or closing an E-stop loop that feeds the STO terminals.

## Before You Replace Anything

Technicians sometimes suspect the drive control board or internal STO circuit when the real cause is an unenergized or miswired external safety relay. Always verify the safety relay output state and field wiring at the STO terminals before ordering drive parts.

[Jump to Fix](#fix)

## Common Causes

- **Open safety relay or E-stop loop (~45%)** The external safety relay feeding the STO input is not energized, reset, or the E-stop chain is open.
- **Missing or removed STO jumper (~25%)** When the application does not use an external safety circuit, a jumper is required at the STO terminals and it may be missing or loose.
- **Miswired STO input terminals (~15%)** The STO field wiring was landed incorrectly or swapped during installation or service.
- **Broken or loose field wiring (~10%)** A conductor between the safety output device and the drive STO terminal is damaged, disconnected, or corroded.
- **Safety relay not reset after power loss (~5%)** Control power is present but the safety relay requires a manual reset or interlock acknowledgment that has not been performed.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is there an external safety relay or E-stop in your system?</summary>
<div class="dtree-body"><strong>Yes:</strong> Check that the safety relay is energized and its output contacts are closed. Reset any latched E-stop or interlock devices.<br><strong>No:</strong> The STO terminals likely require a factory jumper. Inspect the drive STO terminal block for a missing or loose jumper wire.</div>
</details>

<details class="dtree"><summary>Does the safety relay show power and an active output (LED on or relay energized)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Measure continuity from the safety relay output to the drive STO input terminals to find a broken or loose field wire.<br><strong>No:</strong> Troubleshoot the safety relay input circuit, E-stop devices, or interlock switches feeding the relay coil.</div>
</details>

<details class="dtree"><summary>After restoring the STO circuit, does the fault clear when you cycle power to the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> The external safety chain was the root cause. Test a normal start command to verify the drive runs.<br><strong>No:</strong> Escalate to Yaskawa technical support with the drive model, spec number, and serial number for internal STO circuit diagnosis.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify the fault code** on the drive keypad and confirm the display shows E88 and that the drive is in a faulted, inhibited state.
2. **Identify the safety chain** feeding the STO input by reviewing the machine wiring diagram or control panel layout to locate the safety relay, E-stop devices, and any interlocks.
3. **Inspect the safety relay** and verify it is receiving control power, energized, and showing an active output (check for indicator LED or measure coil voltage).
4. **Check the STO terminal wiring** at the drive for missing jumpers, loose conductors, or incorrect landing, comparing against the GA800 terminal diagram for your model.
5. **Measure continuity** from the safety relay output contacts through the field wiring to the drive STO input terminals to find any open or high-resistance path.
6. **Correct the wiring or relay state** by resetting the safety relay, replacing a missing jumper, or repairing broken field wire, then restore the STO circuit to the closed permissive condition.
7. **Cycle drive power** and re-test the start command only after the STO path is valid and the fault has cleared from the keypad display.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Safety relay (Pilz, Schmersal, or machine OEM) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e88-fault-code&k=Safety+relay+%28Pilz%2C+Schmersal%2C+or+machine+OEM%29&tag=errorcodefixes-20) \| Match voltage and contact rating to the original relay feeding the STO input. |
| STO jumper wire or terminal block jumper | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e88-fault-code&k=STO+jumper+wire+or+terminal+block+jumper&tag=errorcodefixes-20) \| Use factory-supplied jumper or appropriate gauge wire per GA800 manual for non-safety applications. |
| Field wiring (shielded multi-conductor) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e88-fault-code&k=Field+wiring+%28shielded+multi-conductor%29&tag=errorcodefixes-20) \| Replace damaged cable between safety relay output and drive STO terminals with appropriate gauge and rating. |

## When to Call a Pro

Call a qualified electrician or controls technician if you are not familiar with safety relay circuits, industrial control wiring, or the specific safety architecture of your machine. The STO function is a safety-critical circuit and incorrect wiring can create a hazard. If the external safety chain is verified and the fault persists, contact Yaskawa technical support with the drive model, spec number, and serial number for diagnosis of the internal STO circuit or possible control board issues. Do not attempt drive disassembly or internal repairs without factory training.

**Rough cost:** A pro service call runs about $150-400 depending on safety relay or field wiring repair.

## See Also

- [Yaskawa GA800 E97 Fault Code - Causes & Fix](/posts/yaskawa-ga800-vfd-e97-fault-code/)
- [Yaskawa A1000 AL-31 Fault - Causes & Fix](/posts/yaskawa-a1000-vfd-al-31-fault-code/)
- [Yaskawa GA800 F042 - Causes & Fix](/posts/yaskawa-ga800-vfd-f042-fault-code/)
- [Yaskawa GA800 A.148 - Causes & Fix](/posts/yaskawa-ga800-vfd-a-148-fault-code/)
