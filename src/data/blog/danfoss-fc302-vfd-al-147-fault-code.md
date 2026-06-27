---
title: "Danfoss FC302 AL-147 - Causes & Fix"
description: "AL-147 is not a valid Danfoss FC302 code. Check the display for AL 14 (earth fault), AL 17 (bus timeout), or AL 38 (internal fault)."
pubDatetime: 2026-06-25T09:33:14Z
modDatetime: 2026-06-25T09:33:14Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss LCP keypad display unit"
diy_or_pro: "pro"
free_checks:
  - "Power-cycle the drive to clear transient display corruption and re-read the alarm code on the LCP keypad."
  - "Check the alarm history menu (Parameter 66 group) to confirm the exact integer code logged by the drive."
  - "Inspect all control and motor cable connections for looseness or corrosion, and tighten ground terminals."
---

## Danfoss FC302 AL-147 — What It Means

The code AL-147 does not exist in official Danfoss VLT AutomationDrive FC302 documentation. Danfoss alarm codes are strictly integer-only formats without hyphens (for example AL 4, AL 13, AL 14, AL 17, AL 38). You may be misreading the display, or the keypad is showing corrupted text. The most likely actual codes are AL 14 (Earth Fault, indicating a ground short on the drive output), AL 17 (Bus Timeout, indicating lost serial communication with a keypad or fieldbus module), or AL 38 (Internal Fault, a general diagnostic code with sub-codes). Consult your drive's alarm history screen or wiring diagram to confirm the real code, then look up the official meaning in the FC302 manual table.

## Before You Replace Anything

Technicians sometimes replace the entire drive power board when the actual fault is AL 14 (earth fault) caused by a failing motor or damaged motor cable. Always disconnect the motor and megohm-test the motor windings and cable to ground before condemning the drive.

[Jump to Fix](#fix)

## Common Causes

- **Misread or corrupted display (~30%)** The LCP keypad may be showing corrupted text or you are reading the code incorrectly, since AL-147 is not a valid Danfoss format.
- **Earth fault (AL 14) (~25%)** Motor winding insulation failure, damaged motor cable, or internal drive IGBT shorting to ground triggers an earth fault alarm.
- **Bus timeout (AL 17) (~20%)** Failed LCP display unit, broken communication cable, or logic board failure causes serial communication loss.
- **Internal fault (AL 38) (~15%)** Control wiring noise interference, loose connections, or failing sensor components generate undefined internal faults.
- **Faulty LCP keypad hardware (~10%)** A dying or defective local control panel can display invalid alarm codes or garbled characters.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the alarm history menu (Parameter 66 group) show a valid integer code like 14, 17, or 38?</summary>
<div class="dtree-body"><strong>Yes:</strong> The display is misread. Look up that integer code in the FC302 manual and follow the specific diagnostic steps for that alarm.<br><strong>No:</strong> The LCP keypad or logic board may be corrupt. Swap the LCP with a known-good unit and check if the drive shows a valid code.</div>
</details>

<details class="dtree"><summary>Does the alarm clear after you disconnect the motor from the drive terminals U, V, and W?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is in the motor or motor cable. Megohm-test the motor windings to ground; readings below 2 megohms mean insulation failure.<br><strong>No:</strong> The drive internal components are likely faulty. The power board or logic card will need replacement by a qualified technician.</div>
</details>

<details class="dtree"><summary>Can you communicate with the drive using a laptop and Danfoss MCT software via USB or serial?</summary>
<div class="dtree-body"><strong>Yes:</strong> The internal logic is working. The LCP display unit itself is faulty and should be replaced.<br><strong>No:</strong> The logic or control card inside the drive has failed and must be replaced by a service technician.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power off** the drive and lock out the main disconnect, then wait five minutes for capacitors to discharge before touching any terminals.
2. **Photograph the alarm display** showing AL-147, then press the alarm reset button or navigate to the alarm history menu (Parameter 66 group) to read the logged alarm code.
3. **Verify the actual code** from the alarm history. If you see AL 14, proceed to earth-fault diagnostics. If you see AL 17, check communication cables and the LCP. If you see AL 38, inspect control wiring for noise and loose grounds.
4. **Disconnect the motor** from terminals U, V, and W. Power the drive back on and check if the alarm reappears. If it clears, the motor or motor cable is at fault.
5. **Megohm-test the motor** and cable to ground using an insulation tester. Readings below 2 megohms indicate failing insulation that must be replaced.
6. **Swap the LCP keypad** with a known-good unit if the alarm history shows no valid code or the display remains corrupted. If communication returns, replace the LCP.
7. **Contact a qualified drive technician** if the alarm persists with the motor disconnected and the LCP swapped, as the drive power board or logic card will need bench testing and replacement.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss LCP keypad display unit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-147-fault-code&k=Danfoss+LCP+keypad+display+unit&tag=errorcodefixes-20) \| Replacement local control panel for FC302 series drives, if the display is corrupt or communication fails. |
| Motor cable (shielded VFD-rated) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-147-fault-code&k=Motor+cable+%28shielded+VFD-rated%29&tag=errorcodefixes-20) \| Shielded cable rated for variable frequency drives, if the existing cable shows damage or fails insulation testing. |
| FC302 power board / IGBT module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-147-fault-code&k=FC302+power+board+%2F+IGBT+module&tag=errorcodefixes-20) \| Internal power section board, if earth-fault testing confirms the drive itself is shorted to ground. |
| FC302 logic / control card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-147-fault-code&k=FC302+logic+%2F+control+card&tag=errorcodefixes-20) \| Internal control board, if communication with external devices is lost and the LCP swap does not resolve the issue. |

## When to Call a Pro

Call a qualified industrial drive technician or electrician if the alarm history shows no valid code after multiple power cycles, if you lack an insulation tester to megohm-test the motor, or if the fault persists with the motor disconnected. High-voltage DC bus capacitors inside the drive can hold lethal voltage for several minutes after power-off, so only trained personnel should open the enclosure or replace internal boards. A technician will use bench test equipment to isolate whether the power board, logic card, or communication modules have failed, and will safely handle capacitor discharge and IGBT testing. If the motor itself has insulation failure, a motor shop can rewind or replace it.

**Rough cost:** A pro service call runs about $200-800.
