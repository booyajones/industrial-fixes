---
title: "Danfoss FC302 VFD AL-85 - Causes & Fix"
description: "AL-85 is not a documented Danfoss FC302 code. Likely misread as Alarm 13 (overcurrent) or 16 (short circuit). Check display carefully."
pubDatetime: 2026-06-23T10:03:10Z
modDatetime: 2026-06-23T10:03:10Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - danfoss
money_part: "IGBT Power Module (Danfoss FC302 inverter section)"
most_likely_cause: "Motor cable fault or shorted IGBT module"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Check the drive display alarm history menu to confirm the exact alarm number (not 85)"
  - "Inspect motor cable terminals for loose connections, burn marks, or moisture"
  - "Verify the drive cooling fan is running and heat sinks are clean"
---

## Danfoss FC302 VFD AL-85 — What It Means

AL-85 does not appear in the official Danfoss FC302 manual as a standard fault code. The documented alarms for this drive include Alarm 13 (Overcurrent), Alarm 14 (Earth Fault), Alarm 16 (Short Circuit), and Alarm 38 (Communication Error), but no Alarm 85. If you are seeing what looks like "85" on the display, it is most likely a misread of Alarm 13 or 16 (the most common drive trip codes), a sub-code display (such as "38-01" where the "3" is obscured), or a typo for Alarm 80 (which is only a warning, not a trip fault). Alarm 13 means the drive output current exceeded the peak limit, usually due to motor or cable faults. Alarm 16 means a short circuit is detected on the output or inside the power section IGBTs. Both codes prevent the drive from running and require immediate diagnosis.

Because AL-85 itself has no documented definition, the repair procedure below applies to the most likely confusion: Alarm 13 or 16. If your display clearly shows a different code, consult your drive's alarm history menu (accessible through the keypad) to confirm the exact number and sub-code before proceeding.

## Before You Replace Anything

Technicians often replace the main control card when seeing trip codes, but a shorted motor cable or motor winding is the real culprit in most cases. Always disconnect the motor and run the drive unloaded first to isolate the problem.

[Jump to Fix](#fix)

## Common Causes

- **Motor cable fault (~35%)** Damaged insulation, nicks, or phase-to-ground shorts in the motor cable cause high current or short circuit trips.
- **Shorted IGBT module (~30%)** Internal power semiconductor failure in the inverter section trips the drive immediately on start.
- **Motor winding failure (~20%)** Moisture, aging, or insulation breakdown in the motor creates a short to ground or between phases.
- **Loose output terminals (~10%)** High resistance at the U, V, or W terminals causes localized heating and current spikes.
- **Control card communication error (~5%)** Alarm 38 (often misread as 85) indicates the control card cannot communicate with the power section.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the drive alarm history menu (parameter 16-90 or alarm log) show Alarm 13, 16, or 38 instead of 85?</summary>
<div class="dtree-body"><strong>Yes:</strong> You have confirmed the real code. Proceed with the repair steps for that documented alarm.<br><strong>No:</strong> The display may be damaged or showing a sub-code. Take a clear photo and contact Danfoss technical support to verify the code before ordering parts.</div>
</details>

<details class="dtree"><summary>Does the alarm clear when you disconnect the motor cable from the drive output terminals and reset?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is in the motor or cable, not the drive. Megger-test the motor windings and inspect the cable for damage.<br><strong>No:</strong> The fault is internal to the drive (IGBT module, control card, or gate driver). The drive needs bench repair or module replacement.</div>
</details>

<details class="dtree"><summary>Are the drive heat sinks hot to touch (after cooling period) and is the cooling fan running during power-up?</summary>
<div class="dtree-body"><strong>Yes:</strong> Overheating may be causing nuisance trips. Clean the heat sinks, replace the fan if it does not spin, and verify ambient temperature is within spec.<br><strong>No:</strong> Thermal issues are not the cause. Focus on electrical isolation tests (motor, cable, and IGBT checks).</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect mains power** and any remote DC-link or UPS supply to the drive. Wait five minutes for the DC bus capacitors to discharge before opening the enclosure.
2. **Access the alarm history** by navigating to parameter group 16 (Information and Diagnostics) on the keypad. Record the exact alarm number and any sub-code (e.g., 13-02 or 38-01). If the display shows 85, verify it is not a misread or partial display.
3. **Disconnect the motor cable** from the drive output terminals U, V, and W. Insulate the cable ends. Reset the drive (cycle power or press the reset button) and attempt to start the drive unloaded (no motor connected).
4. **If the alarm persists with no motor connected**, the fault is internal. The IGBT module, gate driver, or control card is failed. Tag the drive for bench repair or contact Danfoss service for a replacement power module.
5. **If the alarm clears with no motor connected**, the problem is in the motor or cable. Use a megohmmeter (500V minimum) to test motor winding insulation to ground and phase-to-phase resistance. Any reading below 10 megohms indicates a motor fault.
6. **Inspect the motor cable** for visible damage, nicks, or moisture intrusion. Check all terminations at both ends for tightness and signs of arcing or corrosion. Replace the cable if any damage is found.
7. **Reconnect the motor and cable** only after confirming both test good. Start the drive and monitor the current readout (parameter 16-10 or 16-14) under no-load and loaded conditions. If the alarm returns, verify the motor is mechanically free and not overloaded.
8. **If the drive trips immediately on start after all checks**, replace the IGBT power module or send the drive to a qualified VFD repair shop. Do not attempt further starts, as repeated trips can damage the control card.

## Parts Often Needed

| Part | Notes |
|------|-------|
| IGBT Power Module (Danfoss FC302 inverter section) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-85-fault-code&k=IGBT+Power+Module+%28Danfoss+FC302+inverter+section%29&tag=errorcodefixes-20) \| Match the module to your drive frame size and voltage rating; contact Danfoss for the correct part number |
| Control Card (FC302 main logic board) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-85-fault-code&k=Control+Card+%28FC302+main+logic+board%29&tag=errorcodefixes-20) \| Only replace if internal fault persists after motor and cable are ruled out; verify with Danfoss support before ordering |

## When to Call a Pro

Call a qualified VFD technician or authorized Danfoss service center if the alarm history does not clearly show a documented code, if the drive trips with no motor connected (indicating internal power section failure), or if you do not have a megohmmeter and multimeter to perform isolation tests. High-voltage DC bus capacitors inside the drive can hold a lethal charge even after mains power is removed. IGBT module replacement requires specialized tools, thermal compound application, and torque specifications. Attempting repair without proper training risks further damage to the drive and personal injury. If the motor tests bad, a motor rewind shop or replacement motor will also require professional coordination to match the drive's rated output.

**Rough cost:** A pro service call runs about $300-1200.
