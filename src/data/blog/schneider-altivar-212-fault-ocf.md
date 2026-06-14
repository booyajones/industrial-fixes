---
title: "Schneider Altivar 212 Fault OCF — Overcurrent Causes & Fix"
description: "What Schneider Altivar 212 fault OCF means, why overcurrent trips the drive, and how to fix it step by step."
pubDatetime: 2026-04-22T15:00:00Z
modDatetime: 2026-04-22T15:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - schneider
money_part: "Motor output cable"
most_likely_cause: "Too-fast acceleration ramp"
---

## Schneider Altivar 212 Fault OCF — What It Means

OCF (Overcurrent) on a Schneider Altivar 212 drive means the output current has exceeded the drive's instantaneous overcurrent trip threshold — typically 200–225% of the drive's rated current. The Altivar 212 is Schneider's HVAC-specific variable frequency drive, designed for fans, pumps, and air-handling units. OCF is a hard fault; the drive trips the output immediately to prevent damage to the IGBT power modules. Unlike a motor overload fault which integrates over time, OCF fires the instant current peaks above the limit.

[Jump to Fix](#fix)

## Common Causes

- **Too-fast acceleration ramp** — If the acceleration time (parameter ACC) is set too short, the motor draws very high inrush current at startup, exceeding the peak current limit and tripping OCF before the motor reaches speed.
- **Mechanical jam or seizure** — A seized pump, fan, or damper that locks the shaft during startup forces the motor to draw locked-rotor current (typically 6–8× FLA), easily exceeding the 200% OCF threshold.
- **Output short circuit** — A phase-to-phase or phase-to-ground short in the motor cable or at the motor terminals will cause an immediate OCF trip. This is a safety-critical fault.
- **Motor winding fault** — An inter-turn short in the motor creates a low-impedance path that draws excessive current from specific IGBTs in the drive.
- **Drive output IGBT fault** — A failed IGBT in the output stage can latch in a low-resistance state, appearing to the drive as an output short circuit and tripping OCF at every start attempt.

## Step-by-Step Fix {#fix}

1. **Do not immediately reset** — A quick reset of OCF followed by another immediate trip suggests a wiring or equipment fault. Investigate before cycling power.
2. **Check for a mechanical jam** — Manually rotate the fan or pump impeller (with power off) to confirm it spins freely. A seized impeller is immediately obvious.
3. **Increase the acceleration time (ACC parameter)** — If the motor accelerates freely but trips OCF at startup, increase the ACC ramp time from the default (typically 3 seconds on ATV212) to 10–30 seconds and test again.
4. **Inspect motor output cables** — Check the U, V, W cables for any physical damage. Measure L-L resistance between cable pairs with the motor disconnected — all three should read equal and non-zero (not near zero).
5. **Megohm test the motor** — With the cable disconnected at the drive, megohm-test each phase to ground. Values below 1 MΩ indicate insulation failure.
6. **Check for drive IGBT fault** — If OCF trips with no motor connected (output wires disconnected), the drive itself has a failed IGBT and requires repair or replacement.
7. **Reset and test** — After addressing the root cause, reset OCF from the keypad and test with a no-load startup.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor output cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-schneider-altivar-212-fault-ocf&k=Motor+output+cable&tag=errorcodefixes-20) \| Replace if damaged or megohm test reveals insulation failure |
| Drive (ATV212) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-schneider-altivar-212-fault-ocf&k=Drive+%28ATV212%29&tag=errorcodefixes-20) \| Required if IGBT failure is confirmed |
## When to Call a Pro

If the Altivar 212 trips OCF with no motor connected, the drive's power electronics have failed. Drive-level repair requires component-level electronics expertise or a factory exchange unit. Call a Schneider Electric-authorized service center.

## Related Articles

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS310 Fault 3130 — Causes & Fix](/posts/abb-acs310-fault-3130/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)
