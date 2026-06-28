---
title: "Danfoss FC302 AL-112 - Causes & Fix"
description: "AL-112 is not a documented Danfoss FC302 code. Re-check the display for the exact alarm number (e.g. Alarm 11, 12, or 38) and consult the manual."
pubDatetime: 2026-06-26T09:44:43Z
modDatetime: 2026-06-26T09:44:43Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 control card (PCB)"
diy_or_pro: "pro"
free_checks:
  - "Power-cycle the drive (disconnect AC mains for 30 seconds, reconnect, and observe the display)"
  - "Record the exact alarm number and any sub-code shown on the LCP"
  - "Check all option card and control wiring connections for loose or corroded terminals"
---

## Danfoss FC302 AL-112 — What It Means

The FC302 variable frequency drive uses alarm codes numbered 1 through 99 and beyond, displayed in the format "Alarm X" on the LCP (local control panel). AL-112 does not appear in the official Danfoss documentation for this drive series. You may be misreading the display or encountering a custom firmware code. Danfoss alarm codes are listed in the operating instructions manual under section 6.1 (Table 6.1 for Alarm 38 sub-codes) and section 9.4. Common alarms include Alarm 11 (motor overload), Alarm 12 (overtemperature), and Alarm 38 (internal fault with a two-digit sub-code).

Before attempting any repair, power-cycle the drive and confirm the exact code shown on the display. Write down the full alarm number and any sub-code. If the code persists, cross-reference it against the official VLT AutomationDrive FC 302 Operating Instructions. If you have Alarm 38, note the sub-code (e.g. 38-01, 38-12) because it indicates the specific internal failure. Without the correct code, you cannot identify the fault or order the right part.

## Before You Replace Anything

Do not replace the control card or inverter board until you verify the exact alarm number. Many Danfoss codes clear after a parameter reset or power cycle, saving hundreds in unnecessary parts.

[Jump to Fix](#fix)

## Common Causes

- **Misread or non-standard code (~70%)** AL-112 does not match any published Danfoss FC302 alarm, so the display may show a different number (Alarm 11, 12, 38) or a custom firmware code.
- **Alarm 38 internal fault (~15%)** If the actual code is Alarm 38, a sub-code indicates a control board, gate driver, or DC-link fault requiring part replacement.
- **Alarm 11 motor overload (~10%)** If the code is Alarm 11, the motor current exceeds the set limit due to a mechanical jam, wrong parameter, or motor failure.
- **Alarm 12 overtemperature (~5%)** If the code is Alarm 12, the heatsink or inverter section is too hot because of blocked airflow, failed fan, or high ambient temperature.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the LCP display show a two-digit alarm number (e.g. 'Alarm 11' or 'Alarm 38') instead of 'AL-112'?</summary>
<div class="dtree-body"><strong>Yes:</strong> You have a standard Danfoss code. Look up that alarm number in the FC302 manual Table 6.1 or 9.4 and follow the troubleshooting steps for that specific fault.<br><strong>No:</strong> The code may be custom firmware or a misread. Contact Danfoss technical support with your drive serial number and firmware version to confirm the code meaning.</div>
</details>

<details class="dtree"><summary>Does the alarm clear after a full power cycle (AC mains off for 30 seconds)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault was transient or caused by a parameter conflict. Monitor the drive and check wiring and grounding if it returns.<br><strong>No:</strong> The fault is latched or hardware-based. Record the exact code and sub-code, then consult the manual or call a qualified technician for board-level diagnostics.</div>
</details>

<details class="dtree"><summary>Are any option cards or control terminals loose or corroded?</summary>
<div class="dtree-body"><strong>Yes:</strong> Reseat all option cards, tighten control terminal screws, and check for moisture or contamination. Power-cycle and test.<br><strong>No:</strong> The fault is internal to the drive. You will need the exact alarm number to proceed with board or power-section diagnostics.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect AC mains power** to the drive and wait 30 seconds for capacitors to discharge, following lockout-tagout procedures.
2. **Power the drive back on** and watch the LCP closely during startup to capture the exact alarm number and any sub-code (e.g. Alarm 38-12).
3. **Write down the code** exactly as it appears, including hyphens and digits, and take a photo of the display if possible.
4. **Open the FC302 operating instructions** (available from Danfoss support or on the CD shipped with the drive) and turn to the Alarms section (typically chapter 6 or 9).
5. **Cross-reference the alarm number** in Table 6.1 (for Alarm 38 sub-codes) or the main alarm list (section 9.4) to find the documented cause and corrective action.
6. **Inspect all control wiring and option cards** for loose terminals, damaged cables, or signs of moisture, and reseat or replace as needed.
7. **If the alarm is Alarm 38 with a sub-code**, contact Danfoss technical support or a qualified VFD technician for board-level diagnostics and part identification, as internal faults often require control card or inverter module replacement.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 control card (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-112-fault-code&k=Danfoss+FC302+control+card+%28PCB%29&tag=errorcodefixes-20) \| Order by drive model and firmware version if Alarm 38 sub-code points to control-board failure. |
| Danfoss FC302 power card / inverter module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-112-fault-code&k=Danfoss+FC302+power+card+%2F+inverter+module&tag=errorcodefixes-20) \| Required for Alarm 38 sub-codes indicating gate driver or IGBT faults. |

## When to Call a Pro

Call a qualified VFD technician or electrician if you cannot locate the exact alarm code in the manual, if the alarm is Alarm 38 (internal fault), or if you lack the tools and training to work safely inside the drive cabinet. High DC-link voltages (up to 800 VDC) remain present for minutes after AC power is removed, and incorrect diagnostics can destroy expensive power modules. A technician will use oscilloscope and multimeter tests to pinpoint the failed component, verify parameter settings, and flash firmware if needed. Professional diagnostics and repair typically cost between two hundred and six hundred dollars, depending on parts and labor.

**Rough cost:** A pro service call runs about $200-600.

## See Also

- [Danfoss FC302 AL-95 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-95-fault-code/)
- [Danfoss FC302 AL-165 - Causes & Fix](/posts/danfoss-fc302-vfd-al-165-fault-code/)
- [Danfoss VFD Fault OL — Causes & Fix](/posts/danfoss-vfd-fault-ol/)
- [Danfoss FC302 AL-82 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-82-fault-code/)
