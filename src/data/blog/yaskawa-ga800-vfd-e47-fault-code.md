---
title: "Yaskawa GA800 E47 Fault - Causes & Fix"
description: "E47 is not a standard GA800 code. Verify the exact display, clear external interlocks, check control wiring, then reset via keypad."
pubDatetime: 2026-06-06T11:35:17Z
modDatetime: 2026-06-06T11:35:17Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
most_likely_cause: "External interlock or control signal not cleared before reset attempt"
likelihood: "the most common cause when non-standard codes appear"
diy_or_pro: "pro"
money_part: "GA800 Control Board"
---

## Yaskawa GA800 E47 Fault — What It Means

E47 does not appear in Yaskawa's published GA800 fault code documentation. It may be a display error, an option card or communication alarm, or a non-standard message tied to external control or safety circuits. Yaskawa's troubleshooting process for any unconfirmed code is to record the exact display on the operator keypad, identify whether it is a fault or alarm, then follow the elementary diagram to check control terminals, wiring, and option hardware. Without a verified manufacturer definition for E47, technicians should treat it as an uncleared external condition or option-related issue rather than a core drive failure.

Yaskawa's reset procedure requires removing the cause of the fault or alarm first, then pressing RESET on the keypad while the code is displayed. If the code persists after all external causes are cleared and option hardware is disconnected, contact Yaskawa Technical Support with the model number, spec code, serial number, and failure details.

## Before You Replace Anything

Technicians sometimes replace the control board when the fault is actually caused by wiring in the external control circuit or an active safety input. Check the elementary diagram and verify all terminal connections before ordering boards.

[Jump to Fix](#fix)

## Common Causes

- **External interlock or safety input still active** A stop signal, emergency stop, or external relay contact may be open or energized, preventing normal operation and triggering a non-standard display.
- **Control terminal wiring fault** Loose, reversed, or shorted wiring at the drive's control terminals can generate unexpected fault codes or prevent proper reset.
- **Option card or communication problem** If the drive uses Ethernet, fieldbus, or another option card, a communication error or improperly seated card can produce non-documented alarm codes.
- **Drive or control board internal fault** A failing control board or internal hardware issue may display a code that does not match the published fault list.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the keypad show a different code when you cycle power to the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> The display may be corrupted or the fault is intermittent. Record both codes and check for loose control wiring or option card connections.<br><strong>No:</strong> The code is stable. Proceed to verify and clear all external control signals and interlocks before attempting reset.</div>
</details>

<details class="dtree"><summary>Are external control terminals (start/stop, safety inputs) wired to this drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> Use the elementary diagram to check every control terminal for proper voltage, continuity, and signal state. Disconnect external control wiring temporarily to isolate the drive.<br><strong>No:</strong> The fault is likely internal or related to an option card. Remove any communication or option hardware and attempt reset.</div>
</details>

<details class="dtree"><summary>Does the fault clear after you press RESET on the keypad with all external signals removed?</summary>
<div class="dtree-body"><strong>Yes:</strong> The cause was external. Reconnect control wiring one circuit at a time to identify the source, then repair wiring or replace the faulty input device.<br><strong>No:</strong> The drive has an internal fault. Contact Yaskawa Technical Support with the model number, spec code, and serial number for repair guidance.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Record the exact code** displayed on the operator keypad, including any prefix or suffix characters, and note whether the drive shows it as a fault or an alarm.
2. **Consult the elementary diagram** in the drive documentation or on the inside cover to identify all control terminals, safety inputs, and option connections used in your installation.
3. **Check control terminal wiring** for proper voltage, continuity, and signal state at each terminal block. Look for loose screws, reversed polarity, or shorted wires.
4. **Disconnect option hardware** such as Ethernet cards, fieldbus modules, or encoder feedback cables to isolate the drive from external communication faults.
5. **Remove all external control signals** by disconnecting start/stop wiring, safety interlocks, and any relay contacts, then verify the drive is in a clean idle state.
6. **Press RESET on the keypad** while the fault code is displayed. If the code clears, reconnect external circuits one at a time to identify the cause.
7. **Contact Yaskawa Technical Support** if the fault persists after all external causes are cleared. Provide the model number, spec code, serial number, and a description of the fault behavior for repair authorization and parts guidance.

## Parts Often Needed

| Part | Notes |
|------|-------|
| GA800 Control Board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e47-fault-code&k=GA800+Control+Board&tag=errorcodefixes-20) \| Field-replaceable if Yaskawa directs board-level repair after external causes are ruled out. |
| GA800 Cooling Fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e47-fault-code&k=GA800+Cooling+Fan&tag=errorcodefixes-20) \| Another field-serviceable component, though unlikely to cause E47. |

## When to Call a Pro

Call a qualified drive technician or contact Yaskawa Technical Support whenever a non-standard or undocumented fault code appears and you cannot identify the cause using the elementary diagram and control terminal checks. Professional diagnosis is required if the fault persists after all external control signals, option hardware, and wiring have been verified and disconnected. Do not attempt to replace the control board without authorization from Yaskawa, as the fault may be covered under warranty or require factory-level diagnostics. Yaskawa service material states that repair support is generally limited to fan and control board replacement, so field personnel should gather the model number, spec code, serial number, and failure details before calling for support.

**Rough cost:** A pro service call runs about $200–500 for wiring diagnosis and control board replacement if needed.
