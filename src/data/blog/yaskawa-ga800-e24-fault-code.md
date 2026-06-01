---
title: "Yaskawa GA800 E24 Fault - Causes & Fix"
description: "E24 on a Yaskawa GA800 indicates external 24 V control power is present while main circuit power has dropped out or is absent."
pubDatetime: 2026-05-30T12:34:00Z
modDatetime: 2026-05-30T12:34:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
---

## Yaskawa GA800 E24 Fault — What It Means

The E24 fault on a Yaskawa GA800 drive means the control circuitry is seeing external 24 V power still connected while the main circuit power supply has decreased or disappeared. The drive's logic remains partially powered by the 24 V control supply, but the main power required to operate the drive is not at the expected state. This is an undervoltage or control-power status condition, not a motor overload or output-stage fault. The drive is reporting that the external 24 V supply is energized at a time when the main circuit voltage has dropped below normal operating levels.

[Jump to Fix](#fix)

## Common Causes

- **Main circuit power loss** An upstream disconnect, blown fuse, breaker trip, or open contactor has interrupted the main power supply to the drive while the external 24 V control power remains on.
- **Voltage sag or brownout** The main circuit supply voltage has dropped below the drive's minimum threshold due to utility sag or high load on the feeder circuit.
- **Loose or burned power connections** Poor contact at line-side terminals, lugs, or busbars creates intermittent voltage drop or total loss of one or more phases to the drive's main input.
- **External 24 V supply still energized** The control power circuit is fed from a separate source that remains live when the main power is lost, triggering the fault condition by design.
- **Faulty upstream contactor or disconnect** The device controlling main power to the drive is stuck open, cycling, or has burned contacts that prevent stable power delivery.

## Step-by-Step Fix {#fix}

1. Verify main circuit power at the drive input terminals using a multimeter to confirm three-phase voltage is present and balanced according to the nameplate rating.
2. Check the external 24 V control supply to confirm it is still energized and measure actual voltage at the drive's 24 V terminals to verify it is within specification.
3. Inspect all upstream components including fuses, circuit breaker, disconnect switch, and contactor for signs of tripping, open contacts, or thermal damage.
4. Examine line-side wiring and terminal connections for loose lugs, corrosion, discoloration, or heat damage that could cause intermittent voltage drop.
5. Restore stable main circuit power by correcting any upstream issue, then remove the cause of the fault completely before attempting a reset.
6. Clear the E24 fault using the RESET function on the drive keypad only after confirming main power is stable and normal.
7. Monitor the drive through several start cycles to confirm the fault does not return, and escalate to Yaskawa technical support with model and serial number if the code persists after input power is verified normal.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Main circuit fuses for Yaskawa GA800 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-e24-fault-code&k=Main+circuit+fuses+for+Yaskawa+GA800&tag=errorcodefixes-20) \| Replace if blown or showing signs of thermal stress on upstream power supply. |
| Replacement contactor for GA800 input | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-e24-fault-code&k=Replacement+contactor+for+GA800+input&tag=errorcodefixes-20) \| Required if upstream contactor has burned or pitted contacts preventing stable main power delivery. |
| GA800 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-e24-fault-code&k=GA800+control+board&tag=errorcodefixes-20) \| Only if fault persists after all input power and 24 V supply issues are proven normal and Yaskawa support confirms internal failure. |

## When to Call a Pro

Call a qualified industrial electrician or drive technician if you are not trained to work safely on three-phase power systems, if the fault returns after you have verified and restored main circuit power, or if upstream supply components such as contactors or breakers require replacement. Because GA800 field repair documentation is limited and internal troubleshooting beyond power verification typically requires factory support, contact Yaskawa technical support directly if the E24 code persists after all external power supply conditions are confirmed normal. Do not attempt control board replacement without confirming the root cause with the manufacturer.
