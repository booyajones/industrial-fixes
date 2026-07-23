---
title: "Yaskawa GA800 VFD AL-14 Fault - Causes & Fix"
description: "AL-14 on a Yaskawa GA800 indicates an external fault signal. Check your control wiring and reset any connected safety devices."
pubDatetime: 2026-07-21T07:36:02Z
modDatetime: 2026-07-21T07:36:02Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "Emergency stop button or contact block"
most_likely_cause: "External safety relay or E-stop circuit has opened"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Check if any emergency stop buttons are pressed or latched and reset them"
  - "Inspect control cabinet for tripped external relays or blown control fuses"
  - "Verify all safety interlocks (door switches, guards, light curtains) are closed and functioning"
no_buy_pct: "65%"
---

## Yaskawa GA800 VFD AL-14 Fault — What It Means

The AL-14 fault code on a Yaskawa GA800 variable frequency drive signals that an external fault input has been triggered. This means a device or system wired to the drive's external fault terminals has sent a stop or alarm signal. The drive halts operation to protect the motor and connected equipment.

The fault does not indicate a problem inside the drive itself. Instead, it reflects conditions in your process or safety chain: an external relay, emergency stop circuit, thermal overload, pressure switch, or PLC output has opened or changed state. To clear the fault, you must identify which external device tripped and correct the underlying condition before resetting the drive.

## Before You Replace Anything

Technicians sometimes replace the VFD control board when AL-14 appears, but this fault is always caused by an external signal. Trace the wiring to the fault input terminals and measure continuity through the connected safety devices before ordering any VFD parts.

[Jump to Fix](#fix)

## Common Causes

- **Emergency stop or safety relay opened (~40%)** An E-stop button, safety interlock, or external relay in the fault circuit has tripped and needs to be reset or repaired.
- **Thermal overload or motor protection relay tripped (~25%)** An external motor overload relay wired to the fault input has detected excessive current or temperature and opened the circuit.
- **PLC or process controller output changed state (~15%)** A programmable logic controller or process control system sent a fault signal due to an upstream alarm condition or out-of-range sensor reading.
- **Broken or loose wire to fault input terminal (~10%)** A damaged conductor, loose terminal screw, or corroded connection has interrupted the external fault circuit continuity.
- **Incorrect fault input parameter setting (~7%)** The drive's fault input is configured for normally-open when the external device is normally-closed, or vice versa, causing false trips.
- **Pressure or flow switch out of range (~3%)** A process pressure switch, flow switch, or level switch wired to the fault input has detected an abnormal condition and sent a stop signal.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Are any emergency stop buttons pressed or safety guards open?</summary>
<div class="dtree-body"><strong>Yes:</strong> Reset the E-stop or close the guard, then reset the VFD fault and attempt to restart.<br><strong>No:</strong> Proceed to check external relays and control wiring in the cabinet.</div>
</details>

<details class="dtree"><summary>Do you see any tripped relays or blown fuses in the control panel?</summary>
<div class="dtree-body"><strong>Yes:</strong> Determine why the relay or fuse tripped (overload, short, process alarm), correct the underlying problem, replace the fuse if needed, and reset.<br><strong>No:</strong> Use a multimeter to measure continuity across the fault input terminals with power off.</div>
</details>

<details class="dtree"><summary>Does the fault input circuit show continuity when all safety devices are closed?</summary>
<div class="dtree-body"><strong>Yes:</strong> The wiring is intact; check the VFD parameter for fault input polarity (normally-open vs. normally-closed) and adjust if needed.<br><strong>No:</strong> Trace the circuit to find the open device or broken wire, repair or replace it, then reset the drive.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the VFD** and lock out the main disconnect following your facility's lockout-tagout procedure.
2. **Locate the external fault input terminals** on the GA800 control terminal block (consult your model's wiring diagram for the exact terminal numbers).
3. **Trace the wiring** from those terminals back through the control circuit to identify all connected devices: E-stops, relays, overloads, switches, and PLC outputs.
4. **Inspect each device** in the fault chain for tripped state, physical damage, or out-of-spec process conditions (pressure, temperature, flow).
5. **Measure continuity** across the fault input circuit with a multimeter to confirm the path is complete when all safety devices are in the normal running position.
6. **Correct the root cause**: reset tripped devices, repair broken wires, replace failed switches, or adjust process parameters to bring conditions back into range.
7. **Restore power and reset the fault** using the VFD keypad or external reset input, then test the system under normal operating conditions to confirm the fault does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Emergency stop button or contact block | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-al-14-fault-code&k=Emergency+stop+button+or+contact+block&tag=errorcodefixes-20) \| Replacement if the E-stop mechanism is mechanically damaged or contacts are burned. |
| Control relay or safety relay | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-al-14-fault-code&k=Control+relay+or+safety+relay&tag=errorcodefixes-20) \| Use a relay with the same coil voltage and contact rating as the original device in your fault circuit. |

## When to Call a Pro

Call a qualified electrician or automation technician if you are unfamiliar with industrial control wiring, lockout-tagout procedures, or the specific safety devices in your system. AL-14 requires tracing multi-wire circuits that may involve PLC programming, safety-rated relays, and process instrumentation. A technician with access to your machine's electrical schematics and parameter list can quickly identify which external input is active and why. Professional help is necessary if the fault involves high-voltage contactors, motor protection relays that require calibration, or integration with a larger control system that you do not have documentation for.

**Rough cost:** A pro service call runs about $150-400.
