---
title: "Yaskawa GA800 E29 Fault - Causes & Fix"
description: "E29 is a soft-charge answerback fault on the Yaskawa GA800 VFD. The most likely fix is replacing the precharge bypass relay or control board."
pubDatetime: 2026-06-05T10:00:23Z
modDatetime: 2026-06-05T10:00:23Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Soft-charge bypass relay"
most_likely_cause: "Failed soft-charge bypass relay"
---

## Yaskawa GA800 E29 Fault — What It Means

The E29 fault on a Yaskawa GA800 variable frequency drive is a soft-charge answerback fault. The drive does not receive the expected confirmation that the soft-charge bypass relay closed correctly during the capacitor charging phase at startup. This indicates a problem in the precharge circuit or its feedback signal.

The fault points to failure of the soft-charge bypass relay or contactor, or a control board issue preventing correct answerback detection. Yaskawa identifies the root cause as damage or failure in the relay or contactor on the soft-charge bypass relay circuit. If the fault persists after a power cycle, the relay path or control board will need replacement.

[Jump to Fix](#fix)

## Common Causes

- **Failed soft-charge bypass relay** The precharge bypass relay or contactor has failed or its contacts are not closing properly.
- **End-of-life relay wear** Monitor U4-06 (PreChargeRelayMainte) shows relay maintenance life over 90%, indicating the relay has reached end of service life.
- **Control board fault** The control board is not detecting the answerback signal correctly even when the relay operates.
- **Damaged relay circuit wiring** Wiring or connections in the soft-charge bypass relay circuit are open or damaged, preventing proper signal feedback.
- **Drive assembly failure** Internal drive-level failure prevents the precharge circuit from operating correctly after re-energize attempts.

## Step-by-Step Fix {#fix}

1. **Record the fault code** and confirm the drive model, serial number, and specifications before beginning any troubleshooting work.
2. **Re-energize the drive** by cycling power off and back on to see if the fault clears on its own after a reset.
3. **Check monitor U4-06** (PreChargeRelayMainte) to evaluate the maintenance life percentage of the precharge relay.
4. **Inspect the soft-charge bypass relay** and contactor path for visible damage, burnt contacts, or failed operation if the fault returns after reset.
5. **Replace the soft-charge bypass relay** or contactor if U4-06 exceeds 90% or if the relay shows signs of failure.
6. **Replace the control board** if the fault persists after relay replacement and all wiring checks pass.
7. **Replace the entire drive** if the fault remains after control board replacement and diagnostics confirm drive-level failure.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Soft-charge bypass relay | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e29-fault-code&k=Soft-charge+bypass+relay&tag=errorcodefixes-20) \| Replace if U4-06 exceeds 90% or relay contacts fail to close properly. |
| GA800 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e29-fault-code&k=GA800+control+board&tag=errorcodefixes-20) \| Required if answerback fault continues after relay replacement. |
| Yaskawa GA800 drive assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e29-fault-code&k=Yaskawa+GA800+drive+assembly&tag=errorcodefixes-20) \| Full drive replacement needed if board-level repairs do not resolve the fault. |

## When to Call a Pro

Call a qualified VFD technician or Yaskawa-authorized service provider if the fault persists after a simple power cycle, if you are not trained to work safely with high-voltage DC bus capacitors, or if you do not have the tools to measure relay operation and control board signals. E29 faults involve internal drive components and precharge circuits that require specific diagnostics and replacement procedures. If U4-06 shows relay maintenance life over 90%, replacement of the board or drive is recommended by the manufacturer and should be performed by trained personnel.

## See Also

- [Yaskawa GA800 F040 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-f040-fault-code/)
- [Yaskawa GA800 E98 Fault Code - Causes & Fix](/posts/yaskawa-ga800-vfd-e98-fault-code/)
- [Yaskawa A1000 OV Fault - Causes & Fix](/posts/yaskawa-a1000-vfd-ov-fault-code/)
- [Yaskawa GA800 E02 Fault Code - Causes & Fix](/posts/yaskawa-ga800-vfd-e02-fault-code/)
