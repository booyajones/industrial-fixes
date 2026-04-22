---
title: "Allen-Bradley PowerFlex Fault F002 — Causes & Fix"
description: "What Allen-Bradley PowerFlex F002 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T08:00:00Z
modDatetime: 2026-04-22T08:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - allen-bradley
---

## Allen-Bradley PowerFlex Fault F002 — What It Means

Allen-Bradley PowerFlex fault F002 means Auxiliary Input — a digital input configured as an external fault or auxiliary interlock has been activated (opened or closed, depending on configuration). The PowerFlex 4, 40, 70, and 700 series all use F002 for this purpose. The drive is not detecting a fault in its own electronics; it's responding to an external signal on a digital input terminal. Until the signal condition clears and the fault is reset, the drive won't run. This is a wiring and integration problem, not a drive component failure.

[Jump to Fix](#fix)

## Common Causes

- **External safety device open** — An E-stop circuit, safety relay, thermal overload, or interlock device wired to the auxiliary input terminal has opened, intentionally or due to a fault condition.
- **Wiring disconnection** — The wire from the auxiliary input terminal to the external device has come loose, been disconnected, or broken. The drive sees an open input and trips F002.
- **Incorrect input configuration** — If the digital input parameter is configured as "Aux Fault" but no external device is wired to that terminal, the floating input may read as faulted. The input needs to be either wired to a normally-closed contact or the parameter changed to "Not Used."
- **External device fault** — A motor overload relay that has tripped, a safety PLC output that has de-energized, or a pressure switch that opened under process conditions all trigger F002.

## Step-by-Step Fix {#fix}

1. **Identify which input is configured for Aux Fault** — Navigate to the digital input parameters (P036–P038 on PowerFlex 40, or equivalent on your model). Find which terminal is configured as "Aux Fault."
2. **Check the wiring at that terminal** — At the drive's I/O terminal block, verify the auxiliary input wire is present and firmly seated. A missing wire means the input is floating (open), which typically triggers the fault.
3. **Trace the external circuit** — Follow the wire from the drive terminal back to whatever device it connects to (safety relay, overload, interlock). Is the contact closed? Use a multimeter to measure continuity across the contact.
4. **Check the external device** — If it's a motor overload relay, has it tripped? Reset it. If it's a safety relay, check whether the safety system has detected an actual safety condition.
5. **Reset the system** — After the auxiliary circuit is restored (contact closed, wiring intact), press the drive's Stop/Reset button or cycle the enable input. F002 should clear.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [Terminal block wire (18–22 AWG)](https://www.amazon.com/s?k=Terminal%20block%20wire%20(18%E2%80%9322%20AWG)&tag=errorcodefixe-20) | Replace if the auxiliary input wire is damaged |
| [Motor overload relay](https://www.amazon.com/s?k=Motor%20overload%20relay&tag=errorcodefixe-20) | If the external device that tripped is the overload; reset or replace |
| [Safety relay (Pilz, Allen-Bradley GuardMaster)](https://www.amazon.com/s?k=Safety%20relay%20(Pilz%2C%20Allen-Bradley%20GuardMaster)&tag=errorcodefixe-20) | If the safety circuit is the interlock source and it has failed |

## When to Call a Pro

If F002 appears and no external device is wired to the auxiliary input terminal, a controls technician should review the drive parameters and program the unused input as "Not Used" to prevent false trips.
