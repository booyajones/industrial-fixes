---
title: "Yaskawa GA800 E26 Fault - Causes & Fix"
description: "E26 is a soft-charge answerback fault: the bypass relay confirmation is missing. Most common fix is replacing the control board."
pubDatetime: 2026-06-05T09:58:47Z
modDatetime: 2026-06-05T09:58:47Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Yaskawa GA800 control board"
most_likely_cause: "Worn or damaged soft-charge bypass relay or contactor"
---

## Yaskawa GA800 E26 Fault — What It Means

The E26 fault on a Yaskawa GA800 VFD is a soft-charge answerback fault. During startup, the drive charges its DC bus through a soft-charge circuit and expects confirmation that the bypass relay or contactor has closed correctly. When that answerback signal is missing, the drive reports E26 and shuts down. This is a hardware-level fault in the precharge and bypass path, not a programming or configuration issue.

The fault typically points to a worn or damaged soft-charge bypass relay, a failed control board, or a combination of both. Yaskawa field service documentation for the GA800 platform treats this as a board-level or drive-level replacement issue rather than a component-level repair.

[Jump to Fix](#fix)

## Common Causes

- **Worn or damaged soft-charge bypass relay or contactor** The relay responsible for transferring the soft-charge circuit has failed or degraded and cannot provide the expected answerback confirmation.
- **Control board failure affecting relay drive or sensing** The board that drives the relay or reads the answerback signal has developed a fault, preventing proper soft-charge operation.
- **Precharge relay maintenance life exceeded** The relay has reached the end of its operational life, indicated by parameter U4-06 exceeding 90 percent, requiring board or drive replacement.
- **Intermittent contact or wiring issue in the bypass path** Loose connections, corrosion, or damaged wiring in the soft-charge bypass circuit prevent the answerback signal from reaching the control board.
- **Complete drive failure requiring replacement** Internal damage to the drive's soft-charge circuit or control electronics cannot be field-repaired and requires a full drive swap.

## Step-by-Step Fix {#fix}

1. **Power down the drive completely**, wait 30 seconds, then re-energize to confirm whether the E26 fault is momentary or persistent.
2. **Check parameter U4-06** [PreChargeRelayMainte] on the drive to view the performance life percentage of the soft-charge bypass relay.
3. **Replace the control board or drive** if U4-06 shows more than 90 percent, as the relay has exceeded its service life and replacement is required per Yaskawa guidance.
4. **Inspect all wiring and connections** in the soft-charge bypass relay path for loose terminals, corrosion, or physical damage if the relay life is acceptable.
5. **Test the soft-charge bypass relay or contactor** for proper operation, looking for wear, pitting, or failure to close when commanded by the control board.
6. **Replace the control board** if the relay tests good but the fault persists, as the board may have a failed relay driver or answerback sensing circuit.
7. **Replace the entire drive** if the fault returns after board replacement or if the drive exhibits other signs of complete failure, consistent with Yaskawa field repair scope for the GA800 platform.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e26-fault-code&k=Yaskawa+GA800+control+board&tag=errorcodefixes-20) \| Match the board to your drive's frame size and voltage rating. |
| Soft-charge bypass relay or contactor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e26-fault-code&k=Soft-charge+bypass+relay+or+contactor&tag=errorcodefixes-20) \| Replacement relay assembly for the precharge circuit, if separately serviceable on your drive model. |
| Yaskawa GA800 VFD (complete drive replacement) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e26-fault-code&k=Yaskawa+GA800+VFD+%28complete+drive+replacement%29&tag=errorcodefixes-20) \| Required when soft-charge circuitry or control board cannot be field-repaired. |

## When to Call a Pro

Call a qualified industrial electrician or drive technician if you are not trained in high-voltage DC bus work or VFD diagnostics. The GA800's internal DC bus holds lethal voltage even after power is removed, and improper handling can cause electric shock or equipment damage. If parameter U4-06 exceeds 90 percent or the fault returns after a power cycle, professional diagnosis and board or drive replacement is the documented repair path. A technician can safely discharge the bus, verify the soft-charge circuit, and perform board-level replacement or drive swap according to Yaskawa service procedures.

## See Also

- [Yaskawa A1000 GF Fault - Causes & Fix](/posts/yaskawa-a1000-vfd-gf-fault-code/)
- [Yaskawa A1000 AL-14 Fault - Causes & Fix](/posts/yaskawa-a1000-vfd-al-14-fault-code/)
- [Yaskawa A1000 LF2 Fault - Causes & Fix](/posts/yaskawa-a1000-vfd-lf2-fault-code/)
- [Yaskawa GA800 E28 Fault - Serial Watchdog Timeout Fix](/posts/yaskawa-ga800-e28-fault-code/)
