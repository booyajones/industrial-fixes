---
title: "MRCOOL EH 0A Error Code - Causes & Fix"
description: "EH 0A means indoor unit EEPROM parameter error on MRCOOL mini splits. Usually needs indoor control board replacement after reset."
pubDatetime: 2026-05-31T07:53:12Z
modDatetime: 2026-05-31T07:53:12Z
author: "James Rutherford"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - mrcool
money_part: "MRCOOL indoor control board / PCB"
---

## MRCOOL EH 0A Error Code — What It Means

EH 0A (also logged as EH 00) on your MRCOOL mini split signals an indoor unit EEPROM parameter error. The control board's stored configuration memory is faulty, unreadable, or corrupted. In practice MRCOOL treats this as an indoor PCB problem unless a simple reset or wiring fix clears it first. The indoor unit may stop responding to the remote or display garbled symbols when this fault is active.

[Jump to Fix](#fix)

## Common Causes

- **Corrupted EEPROM parameters** A power surge, brownout, or interrupted firmware event can scramble the stored configuration data on the indoor control board.
- **Failed indoor control board** The PCB itself has degraded or stopped responding correctly to commands from the remote or outdoor unit.
- **Loose or damaged wiring at the indoor PCB** Connections to the display panel or terminal block may have vibrated loose or corroded over time.
- **Abnormal incoming voltage** Unstable supply voltage can cause the EEPROM to write invalid data or fail to initialize properly on startup.
- **Garbled display misread as a fault code** If the screen shows an undefined or scrambled symbol, verify it is not simply a temperature reading before treating it as EH 0A.

## Step-by-Step Fix {#fix}

1. **Power-cycle the system** by turning off the breaker for 15 minutes, then restore power and check whether the code clears.
2. **Verify incoming voltage** with a multimeter at the indoor unit disconnect to rule out supply problems before opening the chassis.
3. **Turn off power at the breaker**, remove the indoor unit cover, and inspect the control board for loose connectors or visible burn marks.
4. **Reseat every wire harness** on the indoor PCB, push each connector firmly into place, and check terminal screws for tightness.
5. **Test the remote control response** by cycling modes and fan speeds. If the indoor unit does not respond at all, the indoor PCB requires replacement.
6. **Replace the indoor control board** if the fault persists after wiring is secure and voltage is normal. Use the correct board for your model.
7. **Restore power and run a test cycle** to confirm the new board initializes without error and responds to all remote commands.

## Parts Often Needed

| Part | Notes |
|------|-------|
| MRCOOL indoor control board / PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mrcool-mini-split-eh-0a-error-code&k=MRCOOL+indoor+control+board+%2F+PCB&tag=errorcodefixes-20) \| Primary replacement part. Match your model number and voltage rating exactly. |
| Indoor wiring harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mrcool-mini-split-eh-0a-error-code&k=Indoor+wiring+harness&tag=errorcodefixes-20) \| Replace only if connectors are melted or pins are corroded beyond cleaning. |

## When to Call a Pro

If you are not comfortable working inside live electrical equipment or cannot access the indoor unit safely, call a licensed HVAC technician. Board-level diagnosis and replacement require shutting off high-voltage power and handling static-sensitive components. A pro can also verify that the outdoor unit and refrigerant circuit are not contributing to the fault, and will have access to MRCOOL factory service documentation and genuine replacement boards.
