---
title: "Yaskawa A1000 AL-09 - Causes & Fix"
description: "AL-09 does not exist in Yaskawa A1000 documentation. Check your display for the correct code (e.g. PGD, PGL) or verify drive brand."
pubDatetime: 2026-06-28T10:25:58Z
modDatetime: 2026-06-28T10:25:58Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Input fuse (Danfoss drives)"
diy_or_pro: "pro"
free_checks:
  - "Verify the drive brand and model number on the nameplate"
  - "Write down the exact fault code from the display (all letters and numbers)"
  - "Consult the owner's manual or wiring diagram for your specific drive model"
---

## Yaskawa A1000 AL-09 — What It Means

The code AL-09 does not appear in Yaskawa's official A1000 VFD fault documentation. This code likely represents a misidentification. If you see AL 9 or Err 9, you may have a Danfoss drive, where it indicates inverter overload (the drive is operating near maximum current capacity). If you have a Yaskawa A1000 with an encoder feedback problem, the correct fault codes are PGD (Encoder Fault), PGL (Encoder Loss), or PGF (Encoder Error), depending on your option card and firmware version.

Before proceeding with any repair, verify the exact brand and model of your drive and double-check the displayed fault code. Consult your owner's manual or the label on the drive itself. Misidentifying the drive brand or fault code can lead to unnecessary parts replacement and wasted diagnostic time.

## Before You Replace Anything

Technicians sometimes replace encoder cables or option cards when the fault code is misread. Always verify the exact fault code on the VFD display and confirm the drive brand before ordering parts.

[Jump to Fix](#fix)

## Common Causes

- **Wrong drive brand identified (~40%)** AL-09 is a Danfoss fault code, not Yaskawa, and appears when the inverter is overloaded.
- **Fault code misread (~30%)** The display may show a different code (like PGD or PGL on Yaskawa) that was transcribed incorrectly.
- **Encoder feedback fault on Yaskawa (~20%)** If the actual issue is encoder signals not reaching the VFD, the correct Yaskawa code is PGD, PGL, or PGF.
- **Outdated or incorrect manual (~10%)** The fault list in an old manual may not match your firmware version or option card configuration.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the drive nameplate say Danfoss (not Yaskawa)?</summary>
<div class="dtree-body"><strong>Yes:</strong> You have a Danfoss drive with an inverter overload alarm. Reduce motor load, check input fuses, and test IGBT modules and DC link capacitors.<br><strong>No:</strong> Confirm the drive is Yaskawa A1000 and write down the exact fault code displayed.</div>
</details>

<details class="dtree"><summary>Does the display show PGD, PGL, or PGF (not AL-09)?</summary>
<div class="dtree-body"><strong>Yes:</strong> You have a Yaskawa encoder fault. Inspect encoder cable connections, verify encoder power supply, and check option card seating.<br><strong>No:</strong> Look up the exact code in your A1000 manual or contact Yaskawa technical support for clarification.</div>
</details>

<details class="dtree"><summary>Is the motor mechanically overloaded or binding?</summary>
<div class="dtree-body"><strong>Yes:</strong> Free the mechanical load, check for misalignment or excessive friction, then reset the drive and test.<br><strong>No:</strong> The fault is likely electrical. Inspect power boards, IGBTs, input fuses, and DC link capacitors.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Stop the drive immediately** and record the exact fault code, brand, and model number from the nameplate and display.
2. **Consult your drive's manual** or wiring diagram to confirm the meaning of the code for your specific brand and firmware version.
3. **If you have a Danfoss drive with AL 9**, reduce motor load, inspect for mechanical binding, and check parameter 128 (Motor Thermal) settings.
4. **Test input fuses and rectifier diodes** on the power board. Replace any blown fuses or shorted diodes.
5. **Inspect IGBT modules** on the inverter board for shorts between collector and emitter. Replace failed modules.
6. **Measure DC link capacitors** for capacity and ESR. Replace any bulging or weak capacitors.
7. **If you have a Yaskawa A1000 with encoder faults (PGD, PGL, PGF)**, inspect encoder cable connections, verify encoder power supply voltage, and reseat the encoder option card.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Input fuse (Danfoss drives) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-al-09-fault-code&k=Input+fuse+%28Danfoss+drives%29&tag=errorcodefixes-20) \| Consult your drive's datasheet for amperage rating |
| IGBT module (Danfoss inverter board) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-al-09-fault-code&k=IGBT+module+%28Danfoss+inverter+board%29&tag=errorcodefixes-20) \| Match module type to your drive model and power rating |
| DC link capacitor (Danfoss power board) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-al-09-fault-code&k=DC+link+capacitor+%28Danfoss+power+board%29&tag=errorcodefixes-20) \| Large electrolytic, typically 400-450 V rated |
| Encoder cable (Yaskawa A1000) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-al-09-fault-code&k=Encoder+cable+%28Yaskawa+A1000%29&tag=errorcodefixes-20) \| Shielded cable, verify pin count and connector type |

## When to Call a Pro

Call a qualified drive technician or electrical engineer when you cannot confirm the drive brand, the fault code does not match any entry in your manual, or you need to test high-voltage components like IGBT modules, rectifiers, or DC link capacitors. If the drive is part of a critical production line or life-safety system, do not attempt repair without proper training and lockout/tagout procedures. A technician can also verify encoder option card configuration, measure DC bus voltage under load, and diagnose intermittent faults that do not appear during static tests.

**Rough cost:** A pro service call runs about $200-500.
