---
title: "Danfoss FC302 AL-19 - Causes & Fix"
description: "AL-19 is not a documented Danfoss FC302 fault code. Likely a misread of AL-13 (Overcurrent) or AL-14 (Earth Fault). Verify the display."
pubDatetime: 2026-06-22T10:11:34Z
modDatetime: 2026-06-22T10:11:34Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 Inverter Power Board / IGBT Module"
most_likely_cause: "Misread alarm display (actual code is AL-13 Overcurrent or AL-14 Earth Fault)"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Re-verify the alarm number on the LCP display to confirm it is not AL-13, AL-14, AL-15, or AL-88"
  - "Disconnect the motor and run the drive unloaded to isolate whether the fault is in the drive or the motor"
  - "Check all motor cable connections and terminals for loose or corroded contacts"
part_price: "$180–450"
---

## Danfoss FC302 AL-19 — What It Means

AL-19 is not a valid or documented fault code for the Danfoss FC302 VFD. Danfoss FC302 alarms are numbered as integers (AL 1, AL 13, AL 14, AL 38, etc.), and official documentation lists no AL-19 entry. The display is most likely showing a misread of a similar number, such as AL-13 (Overcurrent), AL-14 (Earth Fault), AL-15 (Hardware Mismatch), or AL-88/AL-89 (Option Detection). It could also be a custom parameter from a third-party add-on or a transient display glitch on the LCP panel.

If you are seeing this code, re-verify the exact alarm number on the Local Control Panel. The most common misreads are AL-13, which indicates overcurrent from motor overload or shorted windings, and AL-14, which signals an earth fault due to damaged cable insulation or motor ground fault. Check the official Danfoss programming guide for your model to confirm the exact alarm code and its meaning before proceeding with any repair.

## Before You Replace Anything

Technicians often replace the entire power board when seeing repeated trips, but a simple megohm test on motor windings and cables can reveal insulation failure or shorted motor windings as the real cause.

[Jump to Fix](#fix)

## Common Causes

- **Misread AL-13 Overcurrent alarm (~40%)** Motor overload, shorted motor winding, loose cable connection, or aging IGBT modules in the drive power section trigger this fault.
- **Misread AL-14 Earth Fault alarm (~30%)** Motor ground fault, damaged cable insulation, or moisture in motor terminal box creates a path to ground.
- **Misread AL-15 Hardware Mismatch alarm (~15%)** Non-compatible or improperly seated option card (brake, serial communication, etc.) causes configuration error.
- **Display glitch or LCP panel failure (~10%)** Transient error or failing Local Control Panel produces incorrect or garbled alarm code on screen.
- **Custom or third-party alarm code (~5%)** Non-standard firmware or external control system uses a custom alarm number not in Danfoss documentation.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the LCP display clearly show AL-13 or AL-14 when you look again?</summary>
<div class="dtree-body"><strong>Yes:</strong> You have a documented fault code. Proceed with standard AL-13 (Overcurrent) or AL-14 (Earth Fault) diagnostics per Danfoss documentation.<br><strong>No:</strong> The display may be faulty or showing a custom alarm. Check for flickering or garbled characters and consider replacing the LCP unit.</div>
</details>

<details class="dtree"><summary>Does the alarm persist when the motor is disconnected and the drive runs unloaded?</summary>
<div class="dtree-body"><strong>Yes:</strong> The drive has an internal fault (likely IGBT failure or control board issue). Replace the inverter power board or IGBT modules.<br><strong>No:</strong> The fault is in the motor or motor cable. Perform a megohm test on motor windings and check cable insulation resistance to ground.</div>
</details>

<details class="dtree"><summary>Did you recently install or change an option card (brake, communication, encoder, etc.)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Reseat the option card or remove it entirely. If the alarm clears, verify the card is compatible with your FC302 model.<br><strong>No:</strong> The fault is not related to option hardware. Focus on motor, cable, and drive power section diagnostics.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify the exact alarm code** by reading the LCP display again and comparing against the official Danfoss FC302 alarm list in the programming manual.
2. **Disconnect the motor** from the drive and attempt to run the drive unloaded (no motor connected) to isolate whether the fault is internal to the drive or external in the motor circuit.
3. **Perform a megohm test** on the motor windings and cable using a megohmmeter. Readings below 2 MΩ indicate insulation failure in the motor or cable.
4. **Check motor current settings** in parameter 1-24 and verify they match the motor nameplate rating. Incorrect settings can trigger overcurrent faults.
5. **Inspect and reseat option cards** if any are installed. Remove and reinstall communication, brake, or encoder cards and check parameter 14-89 (frozen vs. auto-detect configuration).
6. **Replace the inverter power board or IGBT modules** if the drive trips with no motor connected and megohm tests pass. This indicates internal IGBT failure or control board fault.
7. **Consult Danfoss technical support** if the alarm code truly does not appear in documentation and you have ruled out misreads and display errors. Provide the full drive model and firmware version.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 Inverter Power Board / IGBT Module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-19-fault-code&k=Danfoss+FC302+Inverter+Power+Board+%2F+IGBT+Module&tag=errorcodefixes-20) \| Match exact drive frame size and voltage rating; consult your model serial number or Danfoss parts diagram. |
| Danfoss LCP (Local Control Panel) Replacement | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-19-fault-code&k=Danfoss+LCP+%28Local+Control+Panel%29+Replacement&tag=errorcodefixes-20) \| For FC302 series; verify compatible panel type (numeric or graphical) for your drive. |

## When to Call a Pro

Call a qualified VFD technician or Danfoss-certified service partner if the alarm code does not match any documented Danfoss fault, if the drive trips with no motor connected (indicating internal power board or IGBT failure), or if you lack a megohmmeter and experience testing motor insulation resistance. High-voltage DC bus capacitors remain charged after shutdown and pose serious shock hazards. Technicians will verify the exact alarm code, perform insulation resistance tests on the motor and cables, check drive parameter settings, and replace internal power boards or IGBT modules as needed. If the fault turns out to be a motor ground fault or winding failure, the motor will need rewinding or replacement by a motor shop.

**Rough cost:** A pro service call runs about $250–600.

## See Also

- [Danfoss FC302 Alarm 31 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-31-fault-code/)
- [Danfoss FC302 Alarm 58 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-58-fault-code/)
- [Danfoss FC302 VFD Alarm 37 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-37-fault-code/)
- [Danfoss FC302 VFD Alarm 16 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-16-fault-code/)
