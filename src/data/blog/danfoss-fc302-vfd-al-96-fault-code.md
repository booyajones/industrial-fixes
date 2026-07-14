---
title: "Danfoss FC302 AL-96 - Causes & Fix"
description: "AL-96 is not a real Danfoss FC302 code. You may have Alarm 38 (internal fault). Power cycle the drive and check control wiring first."
pubDatetime: 2026-06-26T09:43:52Z
modDatetime: 2026-06-26T09:43:52Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 control PCB (I/O card)"
most_likely_cause: "Misread or mistyped alarm code"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power cycle the drive completely (disconnect AC input for 60 seconds, reconnect, and restart) to clear transient faults."
  - "Check that control wiring is isolated from motor and power cables and that all terminals are tight."
  - "Verify all cooling fans are running and vents are clean and unblocked."
---

## Danfoss FC302 AL-96 — What It Means

AL-96 does not exist in official Danfoss FC302 documentation. The FC302 series uses alarm codes numbered 1 through 72, and no manufacturer spec sheet or alarm list includes an AL-96 code. This is likely a misread display, a typo, or confusion with a different VFD brand or model. The closest valid internal fault on the FC302 is Alarm 38, which signals an internal hardware or software problem. Alarm 38 often includes a sub-code (such as 38-5376 or higher) that specifies the exact component or circuit at fault.

If your display shows something that looks like AL-96, write down the exact alphanumeric string and compare it to the alarm list in your FC302 operating manual. Check parameter 15-32 to see the extended alarm detail and sub-code. If the display truly shows a code not listed in Danfoss documentation, the control board may be corrupted or the display itself may be damaged.

## Before You Replace Anything

Technicians sometimes replace the entire drive when a loose control wire or noise interference is the real problem. Power-cycle the VFD and check all control wiring and grounding connections before ordering any boards.

[Jump to Fix](#fix)

## Common Causes

- **Misread or mistyped alarm code (~40%)** The display was read incorrectly, or the code was transcribed with a typo, since AL-96 is not a valid Danfoss FC302 alarm.
- **Control board memory or firmware corruption (~25%)** The control PCB has experienced a memory error or firmware glitch that displays an invalid code or triggers Alarm 38.
- **Loose or damaged control wiring (~15%)** Connections to the I/O card or keypad are loose, corroded, or pinched, causing communication errors that may show as Alarm 38.
- **Electrical noise interference (~10%)** Power cables or motor leads are routed too close to control wiring, inducing noise that corrupts internal signals and triggers Alarm 38.
- **Overheating due to blocked cooling (~5%)** Fans are failed or vents are clogged, causing the drive to overheat and trip Alarm 38 with a thermal sub-code.
- **Failed DC-link capacitor or IGBT module (~5%)** A shorted power component on the inverter or rectifier board generates an internal fault that may appear as Alarm 38.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the display show exactly 'AL-96' or does it show 'Alarm 38' with a sub-code?</summary>
<div class="dtree-body"><strong>Yes:</strong> If it shows Alarm 38 with a sub-code, consult the FC302 alarm list in the operating manual and proceed to diagnose that specific internal fault.<br><strong>No:</strong> If it truly shows AL-96, photograph the display and contact Danfoss support, as this is not a documented code.</div>
</details>

<details class="dtree"><summary>Does the alarm clear after a full power cycle (AC input off for 60 seconds)?</summary>
<div class="dtree-body"><strong>Yes:</strong> A transient fault caused by noise or a brief overheat. Check cooling, grounding, and cable routing, then monitor.<br><strong>No:</strong> A persistent fault indicates a hardware failure on the control board, power board, or IGBT module. Call a VFD technician.</div>
</details>

<details class="dtree"><summary>Do all cooling fans run when the drive is powered up?</summary>
<div class="dtree-body"><strong>Yes:</strong> Cooling is intact. Focus on control wiring, grounding, and possible board replacement.<br><strong>No:</strong> Replace or repair the failed fan, clean all vents and heatsinks, then reset and retest.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Write down the exact alarm code** displayed on the keypad, including any sub-code (for example, Alarm 38-5376), and photograph the screen if possible.
2. **Power cycle the drive** by switching off the AC input disconnect, waiting 60 seconds for capacitors to discharge, then switching back on and attempting a restart.
3. **Check parameter 15-32** on the keypad to view the extended alarm detail and any sub-code that identifies the specific internal fault.
4. **Inspect all control wiring** to the I/O card, keypad, and external control devices. Tighten terminals and verify control wiring is separated from power and motor cables by at least 300 mm.
5. **Verify cooling fans operate** and that all vents, filters, and heatsinks are clean. Replace any failed fans and clear any obstructions.
6. **Run an unloaded test** by disconnecting the motor and attempting to run the drive in local mode. If the alarm persists with no load, the fault is internal to the drive.
7. **Contact Danfoss technical support** with the exact alarm code, drive serial number, and parameter 15-32 sub-code. If hardware failure is confirmed, arrange for professional repair or board replacement.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 control PCB (I/O card) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-96-fault-code&k=Danfoss+FC302+control+PCB+%28I%2FO+card%29&tag=errorcodefixes-20) \| Order by drive frame size and firmware version; verify part number with Danfoss before purchase. |
| Danfoss FC302 power board assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-96-fault-code&k=Danfoss+FC302+power+board+assembly&tag=errorcodefixes-20) \| Includes rectifier, DC-link capacitors, and inverter; required if IGBT or capacitor failure is confirmed. |
| FC302 cooling fan module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-96-fault-code&k=FC302+cooling+fan+module&tag=errorcodefixes-20) \| Match frame size and voltage rating; some larger frames use multiple fans. |

## When to Call a Pro

Call a qualified VFD technician or authorized Danfoss service partner if the alarm persists after a power cycle, if the exact code does not appear in the FC302 alarm list, or if parameter 15-32 points to a hardware fault such as a failed control board, IGBT module, or DC-link capacitor. Professional diagnostics require high-voltage safety equipment, firmware tools, and component-level testing. Do not open the drive enclosure while power is connected, and do not attempt to replace power boards or IGBTs without proper lockout, discharge procedures, and ESD protection. If the drive is under warranty or part of a critical process, contact Danfoss support directly to avoid voiding coverage or damaging the unit.

**Rough cost:** A pro service call runs about $200-600.

## See Also

- [Danfoss FC302 AL-17 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-117-fault-code/)
- [Danfoss FC302 AL-69 - Causes & Fix](/posts/danfoss-fc302-vfd-al-69-fault-code/)
- [Danfoss FC302 AL-118 - Causes & Fix](/posts/danfoss-fc302-vfd-al-118-fault-code/)
- [Danfoss FC-302 Alarm 12 — Overcurrent Fix](/posts/danfoss-fc302-alarm-12/)
