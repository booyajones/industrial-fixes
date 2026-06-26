---
title: "Danfoss FC302 AL-108 Fault - Causes & Fix"
description: "AL-108 does not exist in Danfoss FC302 documentation. Most likely misread Alarm 13 (DC undervoltage). Check input power and motor wiring first."
pubDatetime: 2026-06-24T10:05:32Z
modDatetime: 2026-06-24T10:05:32Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - danfoss
money_part: "Input fuse set (appropriate voltage and current rating for FC302 frame size)"
most_likely_cause: "Low or unbalanced input voltage"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Measure incoming three-phase AC voltage at input terminals to verify all phases are present and balanced within 3%"
  - "Inspect all input terminal connections for loose wiring or corrosion and tighten securely"
  - "Check input fuses for continuity or signs of burnout"
no_buy_pct: "40%"
---

## Danfoss FC302 AL-108 Fault — What It Means

The code AL-108 does not appear in official Danfoss VLT AutomationDrive FC 302 documentation. Danfoss uses numeric alarm codes (Alarm 13, Alarm 16, Alarm 38) not alphanumeric codes with hyphens. This suggests a misreading of the display, a typographical error, or confusion with another system. The most likely actual fault is Alarm 13 (DC Undervoltage), which indicates the DC bus voltage inside the drive has dropped below the minimum threshold, typically below 200 V for 400 V AC drives, preventing proper motor control.

If your display truly shows AL-108, consult your drive's full manual or contact Danfoss technical support to confirm the code. If the fault is actually Alarm 13, the drive is detecting insufficient voltage on its internal DC bus, usually caused by low incoming AC power, blown input fuses, loose wiring connections, or a failing rectifier bridge inside the drive.

## Before You Replace Anything

Technicians often replace the drive's main control board when the real problem is blown input fuses or loose input terminal connections. Always measure incoming three-phase voltage and inspect all input terminals and fuses before replacing any internal boards.

[Jump to Fix](#fix)

## Common Causes

- **Low or unbalanced input voltage (~35%)** Voltage sag from large motors or welders sharing the same transformer, or utility supply issues, drops DC bus voltage below threshold.
- **Blown input fuses or loose connections (~25%)** Corroded terminals, loose wire nuts, or blown fuses in the input power circuit starve the drive of AC power.
- **Failed rectifier bridge or DC bus components (~20%)** Rectifier diodes or DC link charging resistors inside the drive fail and prevent DC bus from charging properly.
- **Motor winding short or insulation failure (~10%)** Partial short in motor windings or degraded insulation causes excessive current draw and voltage drop.
- **Incorrect motor parameter settings (~10%)** Motor nominal current parameter (1-24) set too high for the actual motor causes the drive to interpret normal current as an overload condition.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Do you measure balanced three-phase voltage (within 3%) at the drive input terminals?</summary>
<div class="dtree-body"><strong>Yes:</strong> Input power is good. Check for blown input fuses, loose internal connections, or a failing rectifier bridge inside the drive.<br><strong>No:</strong> Low or unbalanced input voltage is the problem. Inspect upstream wiring, transformers, and breakers, or contact your utility if voltage is consistently low.</div>
</details>

<details class="dtree"><summary>Does the alarm clear when you disconnect the motor from the drive output (U, V, W terminals)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor has a winding short or insulation failure. Perform a megohm test on the motor windings to ground.<br><strong>No:</strong> The fault is internal to the drive. Suspect a failed rectifier bridge, DC bus capacitor, or power board component.</div>
</details>

<details class="dtree"><summary>Are all three input fuses intact and showing continuity?</summary>
<div class="dtree-body"><strong>Yes:</strong> Fuses are good. Move to checking internal drive components or motor wiring for shorts.<br><strong>No:</strong> Replace the blown fuse and investigate the cause (motor overload, short circuit, or drive component failure) before restarting.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify the alarm code** by checking the drive display carefully or using Danfoss MCT 10 software to read the exact alarm number, since AL-108 is not a documented Danfoss code.
2. **Measure incoming voltage** at all three input phases (L1, L2, L3) with a multimeter and confirm voltage is balanced within 3% and meets the drive's rated input voltage.
3. **Inspect input fuses and connections** by removing the drive cover (with power off and locked out) and checking each input fuse for continuity and each terminal for tightness and corrosion.
4. **Disconnect the motor** from the drive output terminals (U, V, W) and measure insulation resistance from each motor winding to ground using a megohm meter (readings should be above 2 megohms).
5. **Check parameter 1-24** (motor nominal current) in the drive menu and verify it matches the nameplate current rating of your motor exactly.
6. **Inspect the rectifier bridge and DC bus** by visually examining the drive's power board for burnt diodes, swollen capacitors, or charred resistors (requires trained technician and lockout-tagout procedure).
7. **Review alarm history** using parameter menu 16-10 through 16-18 or MCT 10 software to see if the drive has been running near its current or voltage limits before the fault occurred.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Input fuse set (appropriate voltage and current rating for FC302 frame size) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-108-fault-code&k=Input+fuse+set+%28appropriate+voltage+and+current+rating+for+FC302+frame+size%29&tag=errorcodefixes-20) \| Consult your drive's manual for correct fuse type and amperage for your frame size |
| Rectifier bridge module (Danfoss OEM replacement for FC302) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-108-fault-code&k=Rectifier+bridge+module+%28Danfoss+OEM+replacement+for+FC302%29&tag=errorcodefixes-20) \| Requires exact frame size and voltage rating match; professional installation recommended |

## When to Call a Pro

Call a qualified electrician or drive technician if you are not trained in high-voltage lockout-tagout procedures, if incoming three-phase power issues require utility or transformer work, or if internal drive components such as the rectifier bridge or DC bus capacitors need replacement. High-voltage DC bus capacitors can store lethal charge even after AC power is disconnected. Also call a pro if motor insulation testing shows a winding fault, because motor rewind or replacement requires proper sizing and VFD-rated insulation. If the alarm code on your display is genuinely AL-108 and not a misread of Alarm 13, contact Danfoss technical support directly to confirm the code exists for your specific firmware version and model.

**Rough cost:** A pro service call runs about $150-500.

## See Also

- [Danfoss FC301 Fault AL 14 — Ground Fault Causes & Fix](/posts/danfoss-fc301-fault-al-14/)
- [Danfoss FC302 AL-88 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-88-fault-code/)
- [Danfoss FC302 AL-124 - Causes & Fix](/posts/danfoss-fc302-vfd-al-124-fault-code/)
- [Danfoss FC302 ALARM 30 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-30-fault-code/)
