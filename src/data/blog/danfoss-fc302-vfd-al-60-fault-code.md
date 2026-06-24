---
title: "Danfoss FC302 AL-60 Fault - Causes & Fix"
description: "AL-60 (External Interlock) means the drive detected an open safety circuit and coasted the motor to a stop. Check the 24 VDC wiring."
pubDatetime: 2026-06-22T10:13:44Z
modDatetime: 2026-06-22T10:13:44Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 control card"
most_likely_cause: "Open safety circuit (blown fuse, tripped overload relay, or loose wire)"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify which digital input terminal is programmed as External Interlock in Parameter 5-XX"
  - "Measure voltage between the External Interlock terminal and the 0 VDC terminal (typically terminal 18 or 19) with a multimeter to confirm 24 VDC is present"
  - "Inspect all wiring, fuses, and overload relay contacts in the safety loop for opens or loose connections"
no_buy_pct: "60%"
---

## Danfoss FC302 AL-60 Fault — What It Means

Alarm 60 (External Interlock) means the Danfoss FC302 drive has detected that a digital input terminal programmed for the External Interlock safety function is not receiving 24 Volts DC. When this happens, the drive immediately zeros its output and coasts the motor to a stop. This is a programmable safety feature intended to stop the motor if a safety device like an emergency stop button, gate sensor, or overload relay is activated.

The alarm appears because the circuit connected to the configured External Interlock terminal is open or has lost voltage. The terminal must receive 24 VDC for the drive to run. If the terminal is programmed for this function but lacks the required voltage, the drive trips and displays Alarm 60.

## Before You Replace Anything

Technicians sometimes replace the control card when the alarm persists, but the actual fault is usually an open wire, blown fuse, or tripped overload relay in the 24 VDC safety loop. Always measure voltage at the terminal and trace the circuit before swapping the card.

[Jump to Fix](#fix)

## Common Causes

- **Open safety circuit (~50%)** A blown fuse, tripped overload relay, or loose wire between the 24 VDC supply and the External Interlock terminal breaks the safety loop.
- **Tripped motor overload relay (~25%)** If the External Interlock is wired to the auxiliary contacts (95 & 96) of a motor overload relay, the overload may have tripped and opened the circuit.
- **Incorrect terminal programming (~10%)** The terminal may be physically wired but not correctly programmed in Parameter 5-XX to recognize the External Interlock function.
- **Loose or corroded connections (~10%)** Corrosion or loose wire terminations at the input terminal or the 24 VDC source interrupt the voltage signal.
- **Failed control card (~5%)** In rare cases where 24 VDC is present at the terminal but the alarm persists, the internal control card circuitry detecting the voltage may be faulty.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does your multimeter show 24 VDC at the External Interlock terminal (referenced to 0 VDC)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The wiring is intact. The control card may be faulty. Call a qualified technician to diagnose the internal circuitry.<br><strong>No:</strong> The safety circuit is open. Trace the wiring from the 24 VDC supply to find the blown fuse, tripped relay, or loose connection.</div>
</details>

<details class="dtree"><summary>Is the motor overload relay tripped or showing an open auxiliary contact?</summary>
<div class="dtree-body"><strong>Yes:</strong> Reset the overload relay and investigate why the motor is overloading. Check for mechanical binding or incorrect overload settings.<br><strong>No:</strong> Check for blown fuses, open wires, or loose terminals in the 24 VDC safety loop.</div>
</details>

<details class="dtree"><summary>Does Parameter 5-XX show the correct digital input terminal assigned to External Interlock?</summary>
<div class="dtree-body"><strong>Yes:</strong> The programming is correct. Focus on the physical wiring and voltage measurements.<br><strong>No:</strong> Reprogram the parameter to match the terminal where the safety circuit is wired.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify the terminal assignment** by checking Parameter 5-XX (or the specific parameter group for digital inputs) to confirm which terminal is set to External Interlock.
2. **Measure voltage at the terminal** using a multimeter between the designated digital input terminal and the 0 VDC terminal (typically terminal 18 or 19). You should read 24 VDC.
3. **Trace the safety circuit if voltage is 0 VDC** by checking for continuity between terminals 5 & 6 on connector X55 of the bypass board (if applicable), and inspect the wiring from the 24 VDC supply (terminal 12) to the input terminal. Look for open wires, blown fuses, or tripped overload relays.
4. **Check the motor overload relay** by inspecting auxiliary contacts (95 & 96) for an open condition. Reset the relay if it has tripped.
5. **Perform a temporary jumper test (only if safe to do so)** by placing a jumper wire between control card terminal 12 (24 VDC) and the digital input terminal programmed as External Interlock. If the alarm clears, the fault is in the external wiring or safety devices.
6. **Repair or replace faulty wiring** by replacing blown fuses, repairing open wires, or tightening loose connections in the 24 VDC safety loop.
7. **Replace the control card if voltage is confirmed present** and the alarm persists after ruling out all wiring and programming issues. Contact Danfoss or a certified technician for control card replacement.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 control card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-60-fault-code&k=Danfoss+FC302+control+card&tag=errorcodefixes-20) \| Only needed if 24 VDC is confirmed at the terminal and all wiring is intact |
| 24 VDC power supply | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-60-fault-code&k=24+VDC+power+supply&tag=errorcodefixes-20) \| If the existing supply is faulty or undersized for the safety circuit |

## When to Call a Pro

Call a qualified VFD technician or industrial electrician if you are not comfortable working with 24 VDC control circuits, interpreting parameter programming, or diagnosing internal control card faults. The technician will have the tools to measure voltage at the terminals, trace wiring, and reprogram parameters safely. If the safety circuit involves motor overload relays, emergency stops, or other industrial safety devices, a professional should verify the system meets all safety standards before returning the drive to service. Control card replacement requires proper handling of static-sensitive components and familiarity with Danfoss parameter backup and restore procedures.

**Rough cost:** A pro service call runs about $150-400 depending on whether the fix is a fuse, wiring repair, or control card replacement.

## See Also

- [Danfoss FC302 Alarm AL 29 — Causes & Fix](/posts/danfoss-fc302-fault-al-29/)
- [Danfoss FC301 Fault AL 14 — Ground Fault Causes & Fix](/posts/danfoss-fc301-fault-al-14/)
- [Danfoss VFD Fault OCL — Causes & Fix](/posts/danfoss-vfd-fault-ocl/)
- [Danfoss FC302 Alarm 74 - Causes & Fix](/posts/danfoss-fc302-vfd-al-74-fault-code/)
