---
title: "Danfoss FC302 AL-134 - Causes & Fix"
description: "AL-134 is not a valid Danfoss FC302 alarm code. Check your display again; you likely have AL-13 (output current exceeded) or AL-14."
pubDatetime: 2026-06-25T09:22:30Z
modDatetime: 2026-06-25T09:22:30Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss LCP (Local Control Panel) for FC302"
diy_or_pro: "pro"
free_checks:
  - "Verify the exact alarm number on the drive display and check the alarm history log (consult your FC302 manual for how to access it)"
  - "Inspect all motor cable connections at both the drive output terminals and the motor junction box for loose or corroded lugs"
  - "Check for visible mechanical overload on the driven equipment (jammed pump impeller, seized conveyor, stuck damper)"
---

## What this code means
No fault code AL-134 exists in Danfoss FC 302 VFD documentation. Danfoss alarm codes range from 1 to 99, with the most common internal faults numbered AL-38 and below. The number 134 is outside the valid range and likely represents a misread display or a confusion with parameter numbers (such as 1-34) rather than an actual alarm. Double-check your control panel display and your drive's alarm history log. If you see AL-13, that indicates output current exceeded the safe threshold during operation. If you see AL-14, that points to a ground fault or earth leakage in the motor or cable. If you see a three-digit number displayed alongside an alarm, it may be a parameter reference or a subcode, not the alarm itself.

## Before You Replace Anything

Technicians sometimes replace IGBT modules or the entire inverter board when the real problem is a shorted motor winding or a corroded cable termination. Always disconnect the motor and run the drive unloaded to isolate whether the fault is internal to the drive or downstream in the motor circuit.

## Common Causes

- **Misread alarm code (~60%)** The display shows AL-13 or AL-14 but was read as 134, or a parameter number was confused for an alarm.
- **Display or keypad fault (~20%)** A failing control panel or LCP (local control panel) displays garbled characters or incorrect alarm numbers.
- **Custom alarm mapping (~10%)** A previous technician programmed a custom warning or external relay code that displays non-standard numbers.
- **Communication error (~10%)** A fieldbus or remote HMI is sending an invalid alarm code to the display due to wiring noise or protocol mismatch.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the drive display show exactly three digits (e.g. 134) with no hyphen or AL prefix?</summary>
<div class="dtree-body"><strong>Yes:</strong> You are likely viewing a parameter number or a data value, not an alarm code. Press the alarm history or status button to see actual fault codes.<br><strong>No:</strong> Write down the exact alarm code with its prefix (AL-xx or Wxx) and consult the Danfoss FC302 operating manual alarm table for that specific number.</div>
</details>

<details class="dtree"><summary>Does the alarm history log (accessed through the keypad menu) show AL-13 or AL-14 as the most recent fault?</summary>
<div class="dtree-body"><strong>Yes:</strong> You have a real overcurrent (AL-13) or ground fault (AL-14) condition. Disconnect the motor and run the drive unloaded to isolate the fault location.<br><strong>No:</strong> The display may be faulty or the drive may have a communication board issue. Power cycle the drive and check again.</div>
</details>

<details class="dtree"><summary>Can you access the drive's parameter list and verify parameter 1-24 (motor nominal current) matches your motor nameplate rating?</summary>
<div class="dtree-body"><strong>Yes:</strong> Motor parameters are set correctly. The fault is likely mechanical overload, motor winding failure, or drive internal damage.<br><strong>No:</strong> Incorrect motor parameters can cause false alarms or real overcurrent trips. Reprogram parameters 1-20 through 1-25 to match your motor exactly.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Write down the exact alarm code** displayed on the VFD keypad, including any prefix (AL, W, or none) and any accompanying text or subcodes.
2. **Access the alarm history log** by navigating the drive's keypad menu (consult your FC302 manual for the exact button sequence, typically Status > Alarm Log) and note the most recent faults.
3. **Cross-reference the alarm number** in the Danfoss FC302 operating manual alarm table to confirm the code exists and read its official definition.
4. **If the code is AL-13 or AL-14**, disconnect the motor cables from the drive output terminals (U, V, W) and attempt to run the drive unloaded at low speed to determine if the fault is internal or external.
5. **Inspect all motor cable terminations** at the drive and motor for loose lugs, corrosion, or damaged insulation, and tighten or clean connections as needed.
6. **Perform a motor megohm test** (insulation resistance to ground) using a 500V or 1000V megger; readings below 2 megohms indicate motor winding failure.
7. **Check for mechanical overload** on the driven equipment by rotating the motor shaft by hand (power off and locked out) to confirm it spins freely without binding or excessive drag.
8. **If the alarm code does not exist in the manual**, replace the LCP (local control panel) or keypad module, as it may be displaying corrupt data due to internal failure or communication noise.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss LCP (Local Control Panel) for FC302 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-134-fault-code&k=Danfoss+LCP+%28Local+Control+Panel%29+for+FC302&tag=errorcodefixes-20) \| Replacement keypad and display module if the original shows garbled or invalid alarm codes |
| Motor cable lugs and heat-shrink tube | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-134-fault-code&k=Motor+cable+lugs+and+heat-shrink+tube&tag=errorcodefixes-20) \| For repairing corroded or loose terminations that cause false current faults |

## When to Call a Pro

Call a qualified VFD technician or industrial electrician if you cannot locate the alarm code in your manual, if the drive continues to show non-standard codes after a power cycle and keypad replacement, or if you need to measure IGBT modules, DC bus voltage, or gate driver signals inside the drive. Any work inside the VFD enclosure requires high-voltage lockout and specialized test equipment. Also call a pro if the motor fails the megohm test, as rewinding or replacing a three-phase motor is not a DIY task.

**Rough cost:** A pro service call runs about $200-600 depending on whether the fault is in the motor, cable, or drive internals.
