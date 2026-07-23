---
title: "Yaskawa GA800 VFD AL-18 Fault - Causes & Fix"
description: "AL-18 signals an external alarm input triggered on the Yaskawa GA800 VFD. Most often caused by a wired safety interlock or sensor."
pubDatetime: 2026-07-21T07:41:44Z
modDatetime: 2026-07-21T07:41:44Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "Replacement thermal overload relay or sensor"
most_likely_cause: "Triggered external safety interlock or sensor"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Check all emergency stop buttons and safety interlocks to confirm they are reset and not mechanically stuck"
  - "Inspect the motor and driven equipment for overheating, jams, or physical obstructions that would trip a thermal or limit switch"
  - "Review the VFD parameter list to identify which digital input is configured for the alarm function and trace its wiring"
no_buy_pct: "60%"
---

## Yaskawa GA800 VFD AL-18 Fault — What It Means

The AL-18 fault on a Yaskawa GA800 variable frequency drive indicates that an external alarm contact has been triggered. The GA800 can be configured to monitor external devices such as safety interlocks, thermal switches, pressure sensors, or emergency stop circuits through its digital input terminals. When the drive detects a change of state on the configured alarm input, it logs AL-18 and typically stops operation to protect the motor or connected equipment.

This fault does not point to an internal drive failure. Instead, it means a field-wired device or circuit connected to the drive's control terminals has opened or closed in a way that signals a problem condition. The root cause lies in the external system, not the VFD itself. Diagnosing AL-18 requires checking the wiring, the status of field devices, and the parameter settings that assign alarm functions to specific input terminals.

## Before You Replace Anything

Technicians sometimes replace the VFD main control board when AL-18 appears, assuming an internal fault. Always verify the external alarm circuit and field devices first, which costs nothing and often reveals a tripped sensor or open interlock as the true cause.

[Jump to Fix](#fix)

## Common Causes

- **External safety interlock or emergency stop triggered (~40%)** A wired safety circuit, e-stop button, or door interlock has opened and signaled the drive to halt operation.
- **Thermal overload or sensor tripped (~25%)** A motor thermal switch, bearing temperature sensor, or process thermal relay has exceeded its set point and opened the alarm contact.
- **Loose or damaged wiring at alarm input terminals (~15%)** Corroded, broken, or improperly landed wires at the digital input terminals can create intermittent or false alarm signals.
- **Incorrect alarm input parameter configuration (~10%)** The drive parameter that assigns alarm function to a digital input may be set incorrectly, or the input polarity may be reversed.
- **Faulty field sensor or relay (~8%)** The external switch, relay, or sensor connected to the alarm input has failed and is sending a continuous alarm signal.
- **Ground fault or electrical noise on control wiring (~2%)** High electrical noise or a ground fault in the control circuit can falsely trigger the alarm input.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Are any emergency stop buttons, safety gates, or interlocks visibly open or not reset?</summary>
<div class="dtree-body"><strong>Yes:</strong> Reset the interlock or e-stop and clear the fault; if it does not recur, the external device was the cause.<br><strong>No:</strong> Proceed to check the motor and driven equipment for jams, overheating, or thermal trips.</div>
</details>

<details class="dtree"><summary>Does the VFD display or parameter readout show which digital input is active?</summary>
<div class="dtree-body"><strong>Yes:</strong> Trace the wiring from that terminal to the field device and inspect for loose connections, corrosion, or a tripped sensor.<br><strong>No:</strong> Consult the drive parameter list to identify which input is configured for external alarm and verify its wiring and polarity.</div>
</details>

<details class="dtree"><summary>Does the fault clear when you temporarily jumper or disconnect the alarm input at the VFD terminals?</summary>
<div class="dtree-body"><strong>Yes:</strong> The problem is in the external wiring or field device; inspect and test each component in the alarm circuit.<br><strong>No:</strong> Check for incorrect parameter settings, reversed input polarity, or electrical noise on the control circuit.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down and lock out** the drive following site safety procedures before inspecting any wiring.
2. **Review the drive parameter list** (consult your GA800 manual) to identify which digital input terminal is configured for external alarm and note its expected state (normally open or normally closed).
3. **Inspect all wired alarm devices** such as emergency stops, safety interlocks, thermal switches, and sensors; confirm they are reset and mechanically free.
4. **Check the wiring** at the drive's control terminals for loose screws, broken strands, corrosion, or incorrect polarity; tighten and repair as needed.
5. **Test the field device** by measuring continuity or resistance with a multimeter; replace any sensor or switch that is open when it should be closed, or vice versa.
6. **Clear the fault** from the drive keypad or parameter menu and attempt to restart; monitor whether the alarm recurs immediately or under specific conditions.
7. **If the fault persists** after verifying all external devices and wiring, consult a qualified electrician or drives technician to check for ground faults, noise issues, or internal drive faults.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Replacement thermal overload relay or sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-al-18-fault-code&k=Replacement+thermal+overload+relay+or+sensor&tag=errorcodefixes-20) \| Only if testing confirms the existing sensor has failed and cannot be reset. |
| Emergency stop button or safety interlock switch | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-al-18-fault-code&k=Emergency+stop+button+or+safety+interlock+switch&tag=errorcodefixes-20) \| Replace if the existing switch is mechanically damaged or electrically open when it should be closed. |

## When to Call a Pro

Call a qualified electrician or VFD technician if you are not trained to work on industrial control systems, if the fault recurs after you have verified and reset all external devices, or if you cannot identify which digital input is configured for the alarm. High-voltage wiring, parameter programming, and troubleshooting control circuits require specialized knowledge and test equipment. A professional can use the drive's diagnostic menu to pinpoint the active input, measure signal integrity, and reconfigure parameters safely. If the external alarm circuit includes safety-rated interlocks or machine guarding, only a certified technician should modify or bypass those devices to maintain compliance with workplace safety regulations.

**Rough cost:** A pro service call runs about $150-400.
