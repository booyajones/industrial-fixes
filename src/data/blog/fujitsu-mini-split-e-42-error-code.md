---
title: "Fujitsu E:42 Error Code - Causes & Fix"
description: "E:42 means communication failure between indoor and outdoor units. Most often fixed by reseating wiring connectors or replacing a control board."
pubDatetime: 2026-05-31T01:08:46Z
modDatetime: 2026-05-31T01:08:46Z
author: "Dana Kowalski"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - fujitsu
---

## Fujitsu E:42 Error Code — What It Means

The E:42 code on a Fujitsu mini split signals a communication or control-board fault. The indoor and outdoor units have lost their ability to talk to each other over the low-voltage communication wiring. This is not a sensor or refrigerant issue. Instead, the system cannot exchange the DC voltage signals that carry operating commands and status updates between the evaporator and condenser sections. The fault can stem from loose or miswired connectors, damaged field wiring, or a failed PCB inside either unit.

Depending on your exact model family, the precise definition may vary slightly, but Fujitsu troubleshooting material consistently ties this class of code to indoor-outdoor communication loss. The system will not run until the communication path is restored.

[Jump to Fix](#fix)

## Common Causes

- **Loose or disconnected communication wiring** The low-voltage cable between indoor and outdoor units has worked free at a terminal block or was never fully seated during installation.
- **Loose connector on a control board** Molex-style plugs on the main PCB, controller PCB, external I/O PCB, or inverter PCB have vibrated loose or corroded over time.
- **Failed main PCB or controller PCB** The circuit board that manages communication has suffered component failure, lightning damage, or power-supply dropout and no longer sends or receives DC signals.
- **Miswired or reversed polarity field wiring** Communication conductors were swapped or landed on the wrong terminals during installation or a service call, preventing proper signaling.
- **Voltage drop or grounding issue** Poor line-voltage supply, undersized branch circuit, or missing equipment ground disrupts the DC communication power rail and causes intermittent faults.
- **Mismatched or unsupported indoor unit** An incompatible indoor head or air-handler model was paired with the outdoor condenser, and the protocol versions cannot communicate.

## Step-by-Step Fix {#fix}

1. **Power-cycle the system.** Turn off the disconnect or breaker, wait two minutes for capacitors to discharge, then restore power and check whether the E:42 returns.
2. **Verify model compatibility.** Cross-reference the indoor and outdoor model numbers in the installation manual to confirm they are designed to work together and that no pairing lockout is present.
3. **Inspect all communication wiring.** Trace the low-voltage cable from the indoor terminal strip to the outdoor board, looking for loose screws, broken strands, pinched insulation, or swapped polarity.
4. **Reseat every connector on both control boards.** Remove and firmly push back each molex plug on the indoor controller PCB, outdoor main PCB, external I/O board, and inverter PCB to eliminate intermittent contact.
5. **Measure DC communication behavior.** Use a multimeter across the communication terminals and watch for a fluctuating DC voltage rather than a flat or zero reading, which Fujitsu training describes as the hallmark of live signaling.
6. **Isolate the faulty board.** If wiring and connectors are secure and voltage is absent or flat, swap or replace the main PCB on the outdoor unit first, then the indoor controller PCB if the fault persists.
7. **Restore power and monitor.** Run the system through a full cooling and heating cycle, watching the display for code recurrence and listening for normal compressor staging and fan response.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Outdoor unit main PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-42-error-code&k=Outdoor+unit+main+PCB&tag=errorcodefixes-20) \| Match your exact condenser model number and serial prefix, as Fujitsu revises boards frequently. |
| Indoor unit controller PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-42-error-code&k=Indoor+unit+controller+PCB&tag=errorcodefixes-20) \| Verify compatibility with your air-handler or wall-mount head model and any wired remote controllers. |
| Communication wiring harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-42-error-code&k=Communication+wiring+harness&tag=errorcodefixes-20) \| Use only shielded, twisted-pair cable if you are replacing damaged field wiring between indoor and outdoor units. |

## When to Call a Pro

Call a licensed HVAC technician if the error returns after reseating connectors and verifying wiring polarity, if you do not own a multimeter or are uncomfortable working inside energized equipment, or if you suspect a board replacement is needed. Communication faults require methodical isolation of wiring versus board failure, and misdiagnosis can lead to unnecessary parts purchases. A qualified tech will also confirm refrigerant charge and system pairing during the same visit, protecting your warranty and catching secondary issues before they escalate.
