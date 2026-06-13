---
title: "Fujitsu Mini Split Not Responding to Remote - Causes & Fix"
description: "Dead batteries or incorrect battery installation in the remote control is the most common cause. Replace batteries and verify polarity."
pubDatetime: 2026-06-11T11:46:26Z
modDatetime: 2026-06-11T11:46:26Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - hvac
  - mini-split
  - fujitsu
  - symptom
---

## Fujitsu Mini Split Not Responding to Remote — What's Happening

When a Fujitsu mini split does not respond to the remote, the unit is not receiving or processing commands from either the handheld infrared remote or the wired wall controller. Fujitsu separates troubleshooting by control type: infrared models rely on battery power and line-of-sight to the indoor unit receiver, while wired controller systems use low-voltage wiring and a remote supply voltage from the indoor controller PCB.

On wired-controller systems, Fujitsu service guidance identifies a 3A fault code as an indoor unit communication circuit error. This fault directs technicians to check terminal connections between the remote controller and indoor unit for open or shorted wiring, then verify remote supply voltage. If 12 VDC is present at the controller PCB connector CNC01, the remote controller is suspect. If 0 VDC is present, the indoor controller PCB is faulty.

[Jump to Fix](#fix)

## Most Likely Causes

- **Dead or incorrectly installed batteries** Weak, dead, or backwards batteries in the handheld remote prevent signal transmission and are the first check in Fujitsu consumer guidance.
- **Loose or open wiring on wired remote systems** Disconnected, shorted, or miswired low-voltage remote cables at the indoor unit terminal block interrupt communication and trigger a 3A fault.
- **Blocked or failed infrared receiver on IR models** Obstructions in front of the indoor unit receiver or a failed receiver prevent the unit from detecting remote signals even when batteries are good.
- **Remote lockout or bad reset state** The indoor unit or handheld remote may enter a locked or unresponsive state after a power interruption or microprocessor glitch.
- **Failed handheld remote** The remote control itself can fail internally, transmitting no infrared signal or no valid command to the unit.
- **Failed indoor controller PCB** When remote supply voltage is missing (0 VDC at CNC01) on wired systems, the indoor unit's controller PCB has lost the ability to power or communicate with the remote.

## How to Diagnose and Fix {#fix}

1. Confirm whether the system uses an infrared handheld remote or a wired wall controller, because Fujitsu diagnostic steps differ by control type.
2. Check that the indoor unit has power by verifying the breaker is on, the disconnect is closed, and any fuse in the branch box is intact.
3. For infrared remotes, replace the batteries with fresh ones and verify correct polarity, then test the remote by aiming it at the indoor unit receiver from close range.
4. For wired remotes, inspect the low-voltage cable and terminal connections at both the remote and indoor unit for loose, disconnected, or shorted wires.
5. On wired systems, measure DC voltage at connector CNC01 on the indoor controller PCB: if 12 VDC is present, replace the wired remote controller. If 0 VDC is present, replace the indoor controller PCB.
6. Power down the indoor unit at the disconnect or branch box for five minutes, then restore power to reset any lockout or fault state.
7. If the remote still does not work after battery and wiring checks, test the infrared output of a handheld remote with a smartphone camera (the IR LED will glow on the camera screen when a button is pressed). If no glow appears, the remote is faulty.
8. If the remote transmits infrared but the unit does not respond, inspect the indoor unit receiver window for obstructions and consider replacing the indoor controller PCB if the receiver has failed.

## Parts You Might Need

| Part | Notes |
|------|-------|
| Fujitsu wired remote controller | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-not-responding-to-remote&k=Fujitsu+wired+remote+controller&tag=errorcodefixes-20) \| Replacement wall controller for systems with low-voltage wired remotes when 12 VDC is present at CNC01. |
| Fujitsu indoor unit controller PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-not-responding-to-remote&k=Fujitsu+indoor+unit+controller+PCB&tag=errorcodefixes-20) \| Main control board in the indoor unit when remote supply voltage is 0 VDC or the receiver circuit has failed. |
| Fujitsu infrared handheld remote | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-not-responding-to-remote&k=Fujitsu+infrared+handheld+remote&tag=errorcodefixes-20) \| Battery-powered wireless remote when the original remote shows no infrared output or fails internally. |

## Related Error Codes

If your appliance also shows a code on the display, these match this problem:

- [Fujitsu Mini Split E 01 error code](/posts/fujitsu-mini-split-e-01-error-code/)
- [Fujitsu Mini Split E 02 error code](/posts/fujitsu-mini-split-e-02-error-code/)
- [Fujitsu Mini Split E 03 error code](/posts/fujitsu-mini-split-e-03-error-code/)
- [Fujitsu Mini Split E 04 error code](/posts/fujitsu-mini-split-e-04-error-code/)
- [Fujitsu Mini Split E 05 error code](/posts/fujitsu-mini-split-e-05-error-code/)
- [Fujitsu Mini Split E 06 error code](/posts/fujitsu-mini-split-e-06-error-code/)
- [Fujitsu Mini Split E 07 error code](/posts/fujitsu-mini-split-e-07-error-code/)
- [Fujitsu Mini Split E 08 error code](/posts/fujitsu-mini-split-e-08-error-code/)
- [Fujitsu Mini Split E 09 error code](/posts/fujitsu-mini-split-e-09-error-code/)
- [Fujitsu Mini Split E 10 error code](/posts/fujitsu-mini-split-e-10-error-code/)
- [Fujitsu Mini Split E 11 error code](/posts/fujitsu-mini-split-e-11-error-code/)
- [Fujitsu Mini Split E 12 error code](/posts/fujitsu-mini-split-e-12-error-code/)

## When to Call a Pro

Call a qualified HVAC technician if you have verified fresh batteries and good power to the unit but the remote still does not work, or if you are uncomfortable measuring low-voltage DC at the controller PCB. Wired remote systems require voltage checks at the indoor unit board and correct diagnosis of whether the fault lies in the remote controller or the indoor PCB. Technicians have the Fujitsu fault trees and meters to measure 12 VDC supply at connector CNC01, replace the indoor controller PCB when voltage is absent, and properly commission the new board or remote after replacement.
