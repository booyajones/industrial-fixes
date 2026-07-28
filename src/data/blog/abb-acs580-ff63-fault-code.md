---
title: "ABB ACS580 FF63 - STO Diagnostics Failure Fix"
description: "ABB ACS580 FF63 means STO diagnostics failure (SW internal malfunction). Reboot the control unit or cycle power. If it returns, contact ABB."
pubDatetime: 2026-05-27T10:37:21Z
modDatetime: 2026-05-27T10:37:21Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - abb
money_part: "ACS580 control board assembly"
most_likely_cause: "Internal software fault in STO diagnostics"
---

## What this code means
FF63 on an ABB ACS580 is logged as STO diagnostics failure with the additional description SW internal malfunction. STO stands for Safe Torque Off, which is the drive's built-in safety function that disables motor torque when commanded. This fault indicates that the drive's internal software has detected a problem in the diagnostics logic for that safety circuit, rather than a normal motor overload or wiring issue.

Because ABB labels this as an internal software malfunction, the fault originates inside the drive's control board or firmware, not from field wiring or external devices in most cases. The drive has flagged an inconsistency in how it is monitoring its own STO function, so the control unit needs to be reset or examined by a technician.

## Common Causes

- **Internal software fault in STO diagnostics** ABB documentation identifies FF63 explicitly as a software internal malfunction in the drive's Safe Torque Off monitoring logic.
- **Control board transient or memory error** A temporary glitch in the control unit's processor or memory can cause the STO diagnostics to report failure even when hardware is intact.
- **Firmware corruption or incomplete boot** If the drive's firmware did not load correctly during power-up, the STO diagnostic routine may fail its self-check and trigger FF63.
- **Control board hardware degradation** A failing component on the control board itself can cause repeated STO diagnostic faults that reappear after every reset or power cycle.

## Step-by-Step Fix {#fix}

1. **Record all fault details** from the drive keypad or Drive Composer software before clearing the fault, including the timestamp and any preceding events, so you have a complete history if escalation is needed.
2. **Reboot the control unit** by navigating to parameter 96.08 Control board boot and executing the reboot command, or by turning off all power to the drive and waiting at least 30 seconds before restoring it.
3. **Clear the fault** using the reset button on the keypad or the reset command in your software interface, then observe whether the drive returns to ready status without immediately re-faulting.
4. **Test the drive under no-load conditions** by enabling it without a motor connected or with the motor uncoupled, to see if FF63 reappears during the STO self-check sequence at startup.
5. **Check for repeated fault appearance** by running the drive through several enable and disable cycles, and by toggling any external STO input signals if your installation uses them, to confirm whether the fault is transient or persistent.
6. **Inspect the control board visually** for any signs of physical damage, burnt traces, or loose connectors, since internal board faults can sometimes show external clues even when the fault code is software-related.
7. **Contact ABB service or your local representative** if the fault returns after reboot and power cycle, because ABB's published troubleshooting explicitly directs persistent FF63 cases to professional service rather than further field resets.

## Parts Often Needed

| Part | Notes |
|------|-------|
| ACS580 control board assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-ff63-fault-code&k=ACS580+control+board+assembly&tag=errorcodefixes-20) \| Primary component for persistent FF63 faults; consult your drive's frame size and variant to confirm the exact service module or control unit part number. |
| ACS580 complete drive service module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-ff63-fault-code&k=ACS580+complete+drive+service+module&tag=errorcodefixes-20) \| May be required if the control board and power section share a single replaceable assembly in your frame size. |

## When to Call a Pro

Call a qualified drive technician or ABB service if FF63 returns immediately after a control-unit reboot and power cycle, because ABB's own troubleshooting text escalates persistent cases to professional support rather than further field troubleshooting. The fault is an internal software malfunction in the drive's safety diagnostics, so repair typically requires control-board replacement, firmware reload, or factory-level diagnostic tools that are not accessible through the standard keypad. Do not continue resetting the drive repeatedly if the fault keeps coming back, since a failing control board can cause unsafe or unpredictable behavior in the STO safety circuit.
