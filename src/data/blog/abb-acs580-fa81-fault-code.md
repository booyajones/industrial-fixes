---
title: "ABB ACS580 FA81 Fault - Safe Torque Off 1 Active"
description: "FA81 on ABB ACS580 means STO circuit 1 is open. Learn what breaks the safety loop, how to diagnose wiring and contacts, and restore drive operation."
pubDatetime: 2026-05-27T10:36:45Z
modDatetime: 2026-05-27T10:36:45Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - abb
money_part: "STO jumper wire or terminal bridge"
most_likely_cause: "Open or disconnected STO wiring"
---

## ABB ACS580 FA81 Fault — What It Means

FA81 on the ABB ACS580 indicates that Safe Torque Off circuit 1 is active or broken. The drive sees the STO1 safety channel as open, so it stops producing torque and refuses to run. This is a protective function, not a motor or power-stage failure. The drive is waiting for the safety circuit to close and signal that it is safe to operate.

The STO (Safe Torque Off) function is an external safety interlock. When the circuit is healthy and closed, the drive can run. When the circuit opens (by design or fault), the drive immediately inhibits torque. FA81 tells you the drive has lost continuity or supply in STO circuit 1, and you need to find where that loop is broken.

[Jump to Fix](#fix)

## Common Causes

- **Open or disconnected STO wiring** Loose terminal screws, broken wires, or unplugged connectors in the STO1 safety loop prevent the drive from seeing a closed circuit.
- **Failed or opened safety contact or relay** An external emergency-stop button, safety relay, or interlock switch in the STO chain has opened or failed, breaking circuit 1.
- **Missing or incorrect STO jumper** If no external safety device is used, a factory jumper or bridge must close the STO terminals, and a missing or loose jumper will trigger FA81.
- **Control board supply issue** Insufficient or unstable voltage on the control board (parameter 95.04) can prevent the STO input from being recognized as healthy.
- **Defective STO input circuit on the control board** Internal hardware fault on the drive's STO input can falsely report an open circuit even when external wiring is intact.

## Step-by-Step Fix {#fix}

1. {'lead': 'Power down and lock out', 'text': 'the drive at the main disconnect, wait for DC bus capacitors to discharge, and verify zero voltage before working on terminals.'}
2. {'lead': 'Inspect STO terminal wiring and jumpers', 'text': "at the drive's STO1 screw terminals (consult your ACS580 hardware manual for exact terminal labels), check for loose screws, broken wires, or missing factory jumpers if no external safety device is installed."}
3. {'lead': 'Trace the external safety circuit', 'text': 'from the drive STO terminals through all emergency-stop buttons, safety relays, interlocks, and contactors, and verify continuity across the entire chain when the circuit is meant to be closed.'}
4. {'lead': 'Check parameter 95.04 Control board supply', 'text': 'on the drive keypad or via the control panel to confirm supply voltage is within specification, and review parameter 31.22 STO indication run/stop to see the current state of the safety input.'}
5. {'lead': 'Restore continuity to STO circuit 1', 'text': 'by repairing wiring, replacing failed safety contacts or relays, or reinstalling the jumper, then measure continuity with a multimeter to confirm a closed loop.'}
6. {'lead': 'Restore power and reset the fault', 'text': 'at the drive keypad (consult your manual for the reset procedure), then monitor parameter 31.22 to verify STO1 is now seen as inactive or closed.'}
7. {'lead': 'Run a no-load test', 'text': 'with all safety devices in their normal operating state to confirm the drive accepts run commands and does not re-trigger FA81.'}

## Parts Often Needed

| Part | Notes |
|------|-------|
| STO jumper wire or terminal bridge | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-fa81-fault-code&k=STO+jumper+wire+or+terminal+bridge&tag=errorcodefixes-20) \| Factory-supplied part if no external safety device is used, verify part number in your ACS580 hardware manual. |
| Safety relay or emergency-stop contact | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-fa81-fault-code&k=Safety+relay+or+emergency-stop+contact&tag=errorcodefixes-20) \| External interlock device in the STO loop, replace if contacts are welded, burned, or mechanically failed. |
| ABB ACS580 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-fa81-fault-code&k=ABB+ACS580+control+board&tag=errorcodefixes-20) \| Required only if the STO input circuit is confirmed defective and external wiring and devices test good, consult ABB for the exact board assembly for your drive frame size. |

## When to Call a Pro

Call a qualified electrician or drive technician if you cannot locate the break in the STO safety circuit, if parameter 95.04 shows an out-of-spec control board supply that you cannot correct, or if the fault persists after you have verified and closed all external wiring and devices. STO circuits are safety-critical, and improper jumpers or bypasses can create serious hazards. A professional can perform isolation testing, interpret ABB diagnostic parameters, and replace the control board if the STO input hardware has failed internally.

## See Also

- [ABB ACS580 A0 Fault Code - Causes & Fix](/posts/abb-acs580-a0-fault-code/)
- [ABB ACS580 A2B1 Fault Code - Causes & Fix](/posts/abb-acs580-a2b1-fault-code/)
- [ABB VFD Fault 2310 — Causes & Fix](/posts/abb-vfd-fault-2310/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
