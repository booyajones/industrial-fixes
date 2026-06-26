---
title: "Danfoss FC302 VFD AL-127 - Causes & Fix"
description: "AL-127 is likely Alarm 38 with sub-code 127 (internal fault) or misread Alarm 13 (overcurrent). Check motor wiring and gate drivers."
pubDatetime: 2026-06-24T10:22:58Z
modDatetime: 2026-06-24T10:22:58Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - danfoss
money_part: "FC302 gate driver board"
most_likely_cause: "Failed gate driver circuit or motor winding short"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power cycle the drive (disconnect AC mains and DC-link, wait for capacitors to discharge) and verify the exact alarm number and sub-code on the display"
  - "Check for loose motor wiring or corroded terminals at the drive output and motor junction box"
---

## Danfoss FC302 VFD AL-127 — What It Means

The Danfoss FC302 does not have a documented AL-127 fault code in standard technical manuals. The most likely scenario is that you are seeing Alarm 38 (Internal Fault) with a sub-code number that includes 127, or the display is being misread as AL-127 when the actual fault is Alarm 13 (Overcurrent). Alarm 38 indicates a generic internal failure within the drive's power electronics, logic board, or sensor circuitry, and the sub-code defines the specific component failure such as a gate driver fault, memory error, or IGBT failure. Alarm 13 means the drive output current exceeded the peak current limit, typically 200% of rated current for 1.5 seconds, which points to a motor short, mechanical overload, or IGBT failure.

Because this code designation is ambiguous, you should first verify the exact alarm number and any sub-code displayed on the drive panel. If the display clearly shows a two-digit alarm number followed by a sub-code, consult Table 6.1 or Table 28 in your FC302 manual to decode the specific internal fault. If you see Alarm 13, focus on motor side diagnostics. If you see Alarm 38, the drive itself has an internal component failure that will require board-level repair or replacement.

## Before You Replace Anything

Technicians often replace the entire VFD power board without isolating the motor side first. Disconnect the motor and run the drive unloaded to determine whether the fault is in the drive or in the motor circuit.

[Jump to Fix](#fix)

## Common Causes

- **Failed gate driver circuits (~30%)** The circuitry controlling the IGBTs has failed, triggering Alarm 38 with a sub-code pointing to gate driver failure.
- **Motor winding short (~25%)** Partial or total short in motor windings causes Alarm 13 (Overcurrent) by exceeding the drive's peak current limit.
- **Failed IGBT modules (~20%)** Physical shorts in the power module or aging IGBT output regulators trigger internal fault codes.
- **Mechanical overload or jammed motor shaft (~15%)** Motor shaft is jammed or overloaded, drawing excessive current and tripping Alarm 13.
- **Control board or memory error (~10%)** Firmware corruption or memory failure on the control PCB triggers Alarm 38 with a sub-code indicating logic failure.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the drive display show a clear two-digit alarm number (like 13 or 38) and a separate sub-code number?</summary>
<div class="dtree-body"><strong>Yes:</strong> Write down both numbers and consult Table 6.1 or Table 28 in your FC302 manual to decode the specific fault, then follow the steps below for that alarm type.<br><strong>No:</strong> The display may be malfunctioning or the code is from a different drive series. Contact Danfoss technical support to verify the fault code before proceeding.</div>
</details>

<details class="dtree"><summary>With the motor disconnected from the drive output terminals, does the fault clear when you power up the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor or motor wiring is at fault. Inspect motor windings for shorts and check cable integrity.<br><strong>No:</strong> The drive has an internal component failure in the power board or control circuitry. Proceed to gate driver and IGBT testing.</div>
</details>

<details class="dtree"><summary>Do you measure continuity (near zero ohms) between any two motor output phases (U, V, W) with the motor disconnected?</summary>
<div class="dtree-body"><strong>Yes:</strong> The drive output section has a shorted IGBT or gate driver. Replace the power board or gate driver module.<br><strong>No:</strong> The fault is likely in the control board, memory, or sensor circuitry. Replace the control PCB or contact a drive repair specialist.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power cycle the drive.** Disconnect AC mains and DC-link power, wait at least 5 minutes for capacitors to discharge, then restore power and observe the exact alarm number and sub-code on the display.
2. **Record the alarm and sub-code.** Write down the full fault message (e.g., AL 38 followed by a number). Consult your FC302 manual Table 6.1 or Table 28 to decode the sub-code if Alarm 38 is shown.
3. **Disconnect the motor from the drive output terminals.** Remove wiring from U, V, and W terminals on the drive. Power up the drive and attempt to run it unloaded (no motor connected).
4. **Check motor wiring and windings.** If the fault cleared with the motor disconnected, use a megohmmeter to test motor winding insulation to ground (should be >10 megohms) and measure winding resistance between phases (should be balanced within 5%). Inspect motor cables for damage, moisture, or loose connections.
5. **Test drive output section.** With the motor still disconnected and drive powered down, use a multimeter to measure resistance between each pair of output terminals (U-V, V-W, W-U). You should see infinite resistance (open circuit). If you measure continuity, the IGBT module or gate driver is shorted and must be replaced.
6. **Inspect control board and gate driver cards.** Open the drive enclosure (observe all electrical safety lockout procedures). Look for burn marks, swollen capacitors, or corrosion on the control PCB and gate driver boards. Reseat all ribbon cables and connectors, then power up and retest.
7. **Replace the faulty component.** If testing confirms a failed gate driver, control board, or IGBT module, source the correct replacement part from Danfoss or an authorized repair center and install it following the manufacturer's service manual procedures.

## Parts Often Needed

| Part | Notes |
|------|-------|
| FC302 gate driver board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-127-fault-code&k=FC302+gate+driver+board&tag=errorcodefixes-20) \| Specific part number varies by drive frame size and voltage rating. Consult your drive nameplate and contact Danfoss for the correct replacement. |
| FC302 control PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-127-fault-code&k=FC302+control+PCB&tag=errorcodefixes-20) \| Main logic board. Verify firmware version compatibility and perform parameter backup before replacement. |

## When to Call a Pro

Call a qualified VFD technician or electrical contractor if you are not trained in high-voltage DC and AC power systems. The FC302 contains lethal DC-link voltages (up to 800 VDC) that persist after AC power is removed. Component-level diagnosis requires knowledge of IGBT gate drive circuits, current sensor verification, and firmware diagnostics. If the fault persists after motor-side checks or you lack the tools to safely discharge capacitors and measure high-voltage circuits, professional service is required. Drive repair specialists can also perform board-level component replacement and parameter recovery from backup, which is beyond typical in-house capabilities.

**Rough cost:** A pro service call runs about $300-800 for gate driver board replacement or motor repair.
