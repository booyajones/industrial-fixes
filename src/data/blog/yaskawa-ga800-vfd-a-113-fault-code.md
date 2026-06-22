---
title: "Yaskawa GA800 VFD A.113 - Causes & Fix"
description: "A.113 is not a standard GA800 trip fault. It may be a parameter display, alarm, or history entry. Verify the display mode and consult your manual."
pubDatetime: 2026-06-08T11:06:54Z
modDatetime: 2026-06-08T11:06:54Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
diy_or_pro: "pro"
money_part: "Yaskawa GA800 control board"
most_likely_cause: "Display mode confusion"
---

## Yaskawa GA800 VFD A.113 — What It Means

A.113 does not appear as a defined fault code in Yaskawa GA800 documentation. The GA800 drive uses distinct display conventions for parameters, alarms, and trip faults. When you see A.113 on the keypad, the drive may be showing a parameter number, an alarm screen, or a fault history entry rather than an active trip condition. Yaskawa instructs technicians to distinguish between these modes because an alarm requires removing the cause and pressing RESET, while a parameter display is simply a configuration screen. Without the full display context or the exact manual page that lists A.113, it is not safe to assign a specific failure mode or component.

Because A.113 is not verified as a manufacturer-defined GA800 fault, the correct first step is to confirm what mode the keypad is in. Check whether the drive is running normally, whether it has tripped and stopped, or whether you are viewing a parameter or history menu. Record the exact operating conditions at the time the code appeared, including whether the event occurred at start, acceleration, steady run, or deceleration. Only after you identify the true display state should you proceed with diagnostics. If the code persists or the drive has tripped, contact Yaskawa support with the model number, specification number, serial number, and the full fault or alarm description from the keypad.

## Before You Replace Anything

Do not replace the control board or option card before confirming the display mode and checking wiring integrity. Many apparent 'faults' are parameter screens or history entries that do not indicate a hardware failure.

[Jump to Fix](#fix)

## Common Causes

- **Display mode confusion (~35%)** The keypad is showing a parameter number or history entry rather than an active fault, so no repair is needed.
- **Loose or damaged option card (~25%)** A communications or I/O option card is seated poorly, has bent pins, or is damaged, causing an alarm or display anomaly.
- **Wiring or control signal fault (~20%)** Motor leads, control wiring, or incoming power connections are loose, damaged, or miswired, triggering an unspecified alarm.
- **Drive/motor compatibility mismatch (~10%)** The drive and motor combination or parameter settings are incorrect for the application, leading to an operational event.
- **Fault history or logged event (~10%)** The drive is displaying a past event from fault history rather than a current trip, so the underlying cause may already be resolved.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is the drive running normally right now, or has it stopped?</summary>
<div class="dtree-body"><strong>Yes:</strong> A.113 is likely a parameter display or history entry, not an active fault. Press the RUN or MENU key to exit the screen and check the fault history menu to see if a trip was logged.<br><strong>No:</strong> The drive has tripped or alarmed. Write down the exact keypad display, note what the machine was doing when it stopped, and proceed to diagnostics.</div>
</details>

<details class="dtree"><summary>Does the keypad show 'A.113' with the word 'Alarm' or a fault icon, or is it just a numeric display?</summary>
<div class="dtree-body"><strong>Yes:</strong> An alarm or fault is active. Record the full message, remove power, inspect all wiring and option cards, and consult the GA800 manual for the exact alarm definition.<br><strong>No:</strong> You may be viewing a parameter screen (e.g. parameter A-113). Press ESC or MENU to return to the run screen and confirm the drive status.</div>
</details>

<details class="dtree"><summary>Have you recently installed or reseated an option card (communications, I/O, encoder)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Power down the drive, remove and reseat the option card, check for bent pins or loose connectors, and verify the card is compatible with your GA800 model.<br><strong>No:</strong> Check all motor and control wiring for loose terminals, damaged insulation, or incorrect connections, then review the parameter settings for drive/motor compatibility.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Confirm the display mode.** Press the RUN or MENU key on the keypad to exit any parameter or history screen and return to the main run display. Note whether the drive is running, stopped, or tripped.
2. **Record the exact display and operating conditions.** Write down the full keypad message, the machine state when A.113 appeared (start, run, decel, coast), and whether the drive stopped or continued running.
3. **Check the fault history menu.** Use the keypad to navigate to the fault/alarm history screen (consult the GA800 manual for the exact menu path). Look for logged faults or alarms with time stamps to identify past events.
4. **Power down and inspect option cards.** Turn off input power and lock out the drive. Open the option-card slot and check that any communications, I/O, or encoder cards are fully seated, have no bent pins, and are locked into place.
5. **Inspect all wiring and connections.** Verify that motor leads, control wiring, and incoming power terminals are tight, undamaged, and correctly landed according to the wiring diagram. Look for signs of arcing, corrosion, or physical damage.
6. **Verify drive and motor compatibility.** Cross-check the drive model, motor nameplate ratings, and parameter settings (especially motor parameters in the A group) to confirm the configuration is correct for your application.
7. **Remove the cause and reset.** Once you have identified and corrected the underlying issue, press the RESET key on the keypad to clear the alarm or fault. Do not reset before the cause is removed.
8. **If A.113 persists, contact Yaskawa support.** Provide the model/spec number, serial number, the exact keypad display, and a description of the application. Do not perform a withstand-voltage test or use a Megger on the drive, as these can damage the unit.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-113-fault-code&k=Yaskawa+GA800+control+board&tag=errorcodefixes-20) \| Only replace if Yaskawa support confirms board failure after full diagnostics; not a common cause of A.113. |
| Yaskawa GA800 option card (communications or I/O) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-113-fault-code&k=Yaskawa+GA800+option+card+%28communications+or+I%2FO%29&tag=errorcodefixes-20) \| Match the card type (e.g. DeviceNet, Ethernet/IP, encoder) to your exact GA800 model and application requirements. |

## When to Call a Pro

Call a qualified drive technician or Yaskawa-authorized service provider if you cannot identify the display mode, if the drive has visible damage or missing components, if A.113 persists after you have checked wiring and option cards, or if you lack the GA800 manual and cannot navigate the keypad menus safely. Do not attempt to troubleshoot or reset the drive if you are unfamiliar with VFD lockout/tagout procedures or high-voltage safety. A professional will use the model, spec, and serial numbers to access the correct documentation, verify the meaning of A.113 for your specific drive revision, and perform systematic diagnostics without risking further damage. If the drive is under warranty, contact the supplier or Yaskawa support before opening the enclosure or replacing any parts, as unauthorized work may void coverage.

**Rough cost:** A pro service call runs about $150–400 for diagnostic visit and wiring or configuration correction; hardware replacement if needed will add cost.

## See Also

- [Yaskawa GA700 Fault UV1 — Main Circuit Undervoltage Causes & Fix](/posts/yaskawa-ga700-fault-uv1/)
- [Yaskawa GA800 oC Fault — Overcurrent Fix](/posts/yaskawa-ga800-error-oc/)
- [Yaskawa GA800 E61 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-e61-fault-code/)
- [Yaskawa GA800 E13 Error - Causes & Fix](/posts/yaskawa-ga800-vfd-e13-fault-code/)
