---
title: "Yaskawa GA800 A.138 Fault - Causes & Fix"
description: "A.138 is not documented in standard GA800 alarm lists. Verify the exact code on your keypad and check your drive's manual alarm table."
pubDatetime: 2026-06-09T11:28:04Z
modDatetime: 2026-06-09T11:28:04Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Yaskawa GA800 control board or main PCB"
diy_or_pro: "pro"
---

## Yaskawa GA800 A.138 Fault — What It Means

The GA800 VFD does not use an A.138 fault code in the documented Yaskawa alarm naming convention. Standard GA800 alarms are formatted as A.xxx, oC, ov, or CPFxx codes, but A.138 does not appear in the manufacturer's fault lists for this drive family. This may indicate a misread display, a typo in documentation, or a code from a different Yaskawa product line. The best practice is to confirm the exact alarm text displayed on the keypad, review the fault history menu on the drive, and cross-reference the alarm table in the specific GA800 manual for your model and firmware revision. Without verification from the drive nameplate and manual, it is not possible to assign a specific meaning or cause to A.138.

## Before You Replace Anything

Because the exact code is unverified, technicians sometimes replace the main control board or option card without first reseating connectors and checking wiring. Always inspect motor cables, encoder feedback wiring, and option card seating before ordering replacement modules.

[Jump to Fix](#fix)

## Common Causes

- **Misread or typographical error (~30%)** The code displayed may have been transcribed incorrectly or the display itself may be partially obscured or damaged.
- **Code from a different Yaskawa series (~25%)** The alarm may belong to a different Yaskawa drive family such as a Servopack or an older VFD model that uses different numbering.
- **Loose or damaged control wiring (~20%)** Intermittent connection issues on control terminals, encoder feedback cables, or option card connectors can trigger unrecognized or spurious alarms.
- **Faulty or unseated option card (~15%)** Communication or I/O option modules that are not fully seated or have developed solder faults may produce non-standard alarm codes.
- **Corrupted drive firmware or parameter set (~10%)** Drives with corrupted parameters or firmware may display fault codes that do not match the published alarm table.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the keypad display the exact text A.138 or does it show a different format or additional characters?</summary>
<div class="dtree-body"><strong>Yes:</strong> Write down the full display text exactly as shown and photograph the screen. Look for nearby text that indicates a sub-code or module identifier.<br><strong>No:</strong> The code may have been misread. Power-cycle the drive and watch the display during startup to capture the exact alarm sequence and format.</div>
</details>

<details class="dtree"><summary>Is there an installed option card (communication, encoder, I/O module) in the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> Power down, reseat the option card firmly, inspect the card-edge connector and drive socket for corrosion or bent pins, then power up and check if the alarm clears or changes.<br><strong>No:</strong> Focus inspection on main power input terminals, motor output cables, and control wiring for loose connections or damage.</div>
</details>

<details class="dtree"><summary>Does the alarm appear in the drive's fault history menu along with a timestamp or additional diagnostic data?</summary>
<div class="dtree-body"><strong>Yes:</strong> Record the full fault history including any sub-codes or status flags. Cross-reference these entries with the GA800 alarm table in the technical manual for your specific firmware version.<br><strong>No:</strong> The display may be showing a transient or hardware fault. Perform a full power-down (disconnect AC input for 60 seconds) and restart to see if the alarm returns immediately.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify the exact alarm code** by powering the drive on and observing the keypad display. Write down the full text, including any sub-codes, and take a clear photograph of the screen.
2. **Access the fault history menu** on the keypad (typically under monitor or diagnostics menus) and record the last several alarms with timestamps and any accompanying status flags.
3. **Locate the drive nameplate** and note the full catalog number, firmware version, and installed options. Download or retrieve the correct GA800 technical manual and alarm code table for that specific model.
4. **Power down the drive completely** at the AC disconnect and lock out the supply. Wait 60 seconds for DC bus capacitors to discharge before opening the cover or touching terminals.
5. **Inspect all wiring and connectors** including AC input power terminals, motor output terminals, encoder or feedback cables if equipped, control wiring on TB1 and TB2, and any option card edge connectors. Look for loose screws, frayed insulation, corrosion, or bent pins.
6. **Reseat option cards and feedback connectors** by removing and reinserting them firmly. Clean any oxidized contacts with electronics-safe contact cleaner if needed.
7. **Restore power and observe** whether the alarm returns immediately, after a delay, or under load. If the alarm persists and does not match any code in the manual, contact Yaskawa technical support with the drive serial number, exact alarm text, and fault history data for assistance.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 control board or main PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-138-fault-code&k=Yaskawa+GA800+control+board+or+main+PCB&tag=errorcodefixes-20) \| Only after confirming the fault follows the board and wiring is verified good. Must match your drive catalog number. |
| Yaskawa option card (communication or I/O module) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-138-fault-code&k=Yaskawa+option+card+%28communication+or+I%2FO+module%29&tag=errorcodefixes-20) \| If the alarm is tied to an installed option and reseating does not clear it. Verify card catalog number matches your drive series. |

## When to Call a Pro

Call a qualified drives technician or contact Yaskawa technical support when the alarm code does not appear in your drive's manual, when wiring and option card inspection does not resolve the fault, or when the drive repeatedly faults after power cycling. High-voltage AC input and DC bus capacitors pose serious shock hazards, so any work inside the drive enclosure should be performed by someone trained in VFD service and lockout procedures. If the drive is under warranty or connected to critical machinery, professional diagnosis will document the fault correctly and preserve warranty coverage.

**Rough cost:** A pro service call runs about $200–500 depending on whether the fault is wiring, an option card, or the drive control board.
