---
title: "Yaskawa GA800 E19 Fault - Causes & Fix"
description: "E19 is a soft-charge answerback fault: the precharge relay didn't confirm closure. Most often a failed bypass relay or control board."
pubDatetime: 2026-06-05T09:54:32Z
modDatetime: 2026-06-05T09:54:32Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Soft-charge bypass relay/contactor for GA800"
most_likely_cause: "Failed or worn soft-charge bypass relay/contactor"
---

## Yaskawa GA800 E19 Fault — What It Means

The E19 fault on a Yaskawa GA800 VFD means the drive did not receive the expected confirmation signal that the soft-charge bypass relay or contactor closed properly during the precharge and startup sequence. The soft-charge circuit protects the drive by gradually charging the DC bus capacitors before applying full voltage. When the relay is supposed to close and bypass the precharge resistors, the drive monitors for an "answerback" signal to confirm the action happened. If that signal is missing or incorrect, the drive halts and displays E19.

This fault typically points to a problem with the soft-charge bypass relay itself (worn contacts, coil failure, or reaching its maintenance life limit), a control board issue that prevents proper sensing or output, or internal drive damage. The GA800 tracks relay cycles in parameter U4-06 [PreChargeRelayMainte], which can help identify if the relay has reached the end of its service life. The fault may appear intermittently at first and become persistent as the component degrades.

[Jump to Fix](#fix)

## Common Causes

- **Failed or worn soft-charge bypass relay/contactor** The relay contacts may be burned, stuck, or the coil may have failed, preventing proper closure and answerback signal.
- **Control board failure or sensing issue** The board may not be reading the relay state correctly or may have a faulty output circuit that prevents the answerback from registering.
- **Relay at or past maintenance life limit** The soft-charge relay has a finite number of cycles, and drives near this limit may begin to fail intermittently before stopping altogether.
- **Loose or corroded wiring to the relay** Poor connections at the relay terminals can interrupt the answerback signal path or prevent the relay from energizing fully.
- **Internal drive component damage** If the precharge circuit itself is damaged, the drive may not complete the soft-charge sequence even with a good relay and control board.

## Step-by-Step Fix {#fix}

1. {'lead': 'Record the fault and current operating conditions', 'text': 'Note the exact fault code, when it appeared, and any load or environmental changes before the fault.'}
2. {'lead': 'Power down and lock out the drive', 'text': 'Turn off incoming power, apply lockout/tagout, and wait for the DC bus to discharge completely (at least five minutes or until verified at zero volts).'}
3. {'lead': 'Re-energize the drive and attempt a restart', 'text': 'Restore power and run the drive to see if the fault was a one-time event or if it repeats immediately or intermittently.'}
4. {'lead': 'Check parameter U4-06 [PreChargeRelayMainte]', 'text': 'Review the relay cycle count to determine if the soft-charge relay is near or past its rated maintenance life, which may indicate replacement is needed.'}
5. {'lead': 'Inspect the soft-charge bypass relay/contactor for physical damage or wear', 'text': 'Look for burned contacts, loose mounting, corroded terminals, or any signs of overheating or mechanical failure on the relay itself.'}
6. {'lead': 'Test or replace the soft-charge bypass relay', 'text': 'If the relay shows wear or if parameter U4-06 indicates high cycle count, replace the relay and clear the fault to see if it resolves.'}
7. {'lead': 'Replace the control board or the complete drive if the fault persists', 'text': 'If a new relay does not clear the fault and wiring is verified intact, replace the control board or consult factory support for drive replacement, as the GA800 maintenance documentation does not cover deeper internal repairs.'}

## Parts Often Needed

| Part | Notes |
|------|-------|
| Soft-charge bypass relay/contactor for GA800 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e19-fault-code&k=Soft-charge+bypass+relay%2Fcontactor+for+GA800&tag=errorcodefixes-20) \| Confirm part number and voltage rating match your specific GA800 model and frame size. |
| GA800 control board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e19-fault-code&k=GA800+control+board+%28PCB%29&tag=errorcodefixes-20) \| Order the correct board revision for your drive firmware and frame size from Yaskawa or an authorized distributor. |

## When to Call a Pro

Call a qualified technician or Yaskawa-authorized service provider if the fault repeats after re-energizing, if you are not trained in VFD diagnostics and high-voltage work, or if replacing the soft-charge relay and control board does not clear the code. The GA800 maintenance documentation explicitly limits user-serviceable repairs to fan and control board replacement, so deeper internal faults require factory support or a complete drive replacement. Any work on VFDs involves lethal DC bus voltages that can persist long after input power is removed, so lockout/tagout and proper discharge verification are mandatory before opening the enclosure.

## See Also

- [Yaskawa GA800 E86 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-e86-fault-code/)
- [Yaskawa GA800 E46 Fault Code - Causes & Fix](/posts/yaskawa-ga800-vfd-e46-fault-code/)
- [Yaskawa GA800 E25 Fault - Causes & Fix](/posts/yaskawa-ga800-e25-fault-code/)
- [Yaskawa U1000 Fault Codes: Complete Guide](/posts/yaskawa-u1000-fault-codes/)
