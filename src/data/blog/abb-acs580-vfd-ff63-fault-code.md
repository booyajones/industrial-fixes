---
title: "ABB ACS580 FF63 Fault - STO Diagnostics Failure Fix"
description: "FF63 means STO diagnostics failure on your ABB ACS580 VFD. Reboot the control unit via parameter 96.08 or power cycle the drive."
pubDatetime: 2026-05-31T11:10:42Z
modDatetime: 2026-05-31T11:10:42Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - abb
---

## ABB ACS580 FF63 Fault — What It Means

FF63 on an ABB ACS580 drive indicates an STO diagnostics failure. STO stands for Safe Torque Off, a safety function that monitors the drive's ability to remove torque from the motor. This fault means the drive has detected a problem in the STO safety-monitoring path, not a problem with your motor or load. ABB categorizes this as a software internal malfunction in the STO diagnostic logic. The drive will not run until the fault is cleared and the underlying cause is resolved.

[Jump to Fix](#fix)

## Common Causes

- **Internal control-unit software fault** The drive's STO diagnostic logic has experienced an internal malfunction or communication error within the control board.
- **Loose or missing STO jumper or wiring** If STO inputs are not used, a missing or improperly installed jumper bridge on the STO terminals can trigger the fault.
- **External STO safety circuit interruption** An open contact, faulty relay, or wiring issue in the external safety chain feeding the STO inputs causes the drive to see an invalid STO condition.
- **Disturbed or corroded STO terminal connections** Vibration, heat cycling, or corrosion can create intermittent contact or open circuits at the STO terminal block.
- **Control-unit hardware degradation** If the fault persists after reboot and wiring checks, the control board itself may have failed and requires replacement.

## Step-by-Step Fix {#fix}

1. {'text': "**Record the fault history** by reviewing the drive's event log to confirm FF63 is isolated and not preceded by power loss, control-voltage drop, or other safety-chain events."}
2. {'text': '**Verify STO configuration** by checking your installation documentation to determine if the STO safety function is actually used in this application.'}
3. {'text': '**Inspect STO terminals and wiring** for loose connections, broken conductors, missing jumpers, or incorrect landing, especially if STO is not used and should be jumpered per ABB wiring diagrams.'}
4. {'text': '**Reboot the control unit** by setting parameter 96.08 Control board boot or by cycling power to the drive completely off and back on after 30 seconds.'}
5. {'text': '**Test run the drive** under observation after the fault clears to confirm normal operation and watch for any intermittent return of FF63.'}
6. {'text': '**Check for vibration or environmental factors** that may cause intermittent contact in the STO circuit, and secure all wiring and connections.'}
7. {'text': '**Contact ABB service or your local representative** if FF63 returns immediately or repeatedly after reboot and wiring corrections, as this indicates an internal control-unit fault requiring replacement.'}

## Parts Often Needed

| Part | Notes |
|------|-------|
| ABB ACS580 Control Unit / Control Board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-ff63-fault-code&k=ABB+ACS580+Control+Unit+%2F+Control+Board&tag=errorcodefixes-20) \| Required if FF63 persists after reboot and wiring checks. Contact ABB for frame-specific part number. |
| STO Terminal Jumper or Bridge Kit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-ff63-fault-code&k=STO+Terminal+Jumper+or+Bridge+Kit&tag=errorcodefixes-20) \| For installations not using external STO. Consult ABB wiring diagram for your drive frame. |
| External Safety Relay or Contactor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-ff63-fault-code&k=External+Safety+Relay+or+Contactor&tag=errorcodefixes-20) \| Replace if the external STO safety chain is used and shows signs of failure or intermittent operation. |

## When to Call a Pro

Call a qualified electrician or ABB-certified technician if the fault returns after you have verified and corrected STO wiring and rebooted the drive, or if you are unfamiliar with safe work on industrial VFDs. Because FF63 points to an internal control-unit fault when wiring is correct, persistent cases require factory support or control-board replacement that should be done by trained personnel. Always follow lockout-tagout procedures and consult ABB directly if the drive is under warranty or part of a safety-critical system.
