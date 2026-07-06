---
title: "Yaskawa A1000 AL-33 - Causes & Fix"
description: "AL-33 means the drive sees a disconnected motor cable. Most common fix: check U, V, W terminals at drive and motor for loose or broken wires."
pubDatetime: 2026-06-29T10:50:43Z
modDatetime: 2026-06-29T10:50:43Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "Motor power cable (U, V, W)"
most_likely_cause: "Disconnected or loose motor cable at U, V, W terminals"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Visually inspect U, V, W terminals at both the drive and motor junction box for loose screws or burned contacts"
  - "Use a multimeter to test continuity between U, V, W at the drive and motor terminals (should read near 0 Ω)"
part_price: "$50-150 for a replacement motor power cable, depending on length and gauge"
no_buy_pct: "60%"
---

## Yaskawa A1000 AL-33 — What It Means

The AL-33 fault code (also displayed as A.b33) on a Yaskawa A1000 VFD indicates a Current Detection Error 3. The drive's internal current detection circuit has registered an open circuit or voltage drop on channel 3, meaning it cannot see the expected current flow from the motor. This protection logic is triggered when the drive believes the servomotor main circuit cable is disconnected or the current signal is not being received properly.

Unlike overcurrent or ground faults, this is a specific alarm for an open state in the current sensor path. The drive expects continuous current feedback during operation, and when that signal drops to zero or shows a pattern consistent with a broken wire, it throws AL-33 to prevent damage.

## Before You Replace Anything

Technicians sometimes replace the entire control board when the real problem is a broken wire inside the cable jacket or a loose screw terminal in the motor junction box. Always perform a continuity test on the U, V, W cable before ordering boards.

[Jump to Fix](#fix)

## Common Causes

- **Disconnected motor cable (~45%)** The U, V, W power cable between the drive and the motor is unplugged, loose at a terminal, or physically broken.
- **Broken wiring inside cable harness (~25%)** A wire inside the cable jacket is severed due to vibration, crushing, or flex fatigue, even if the outer insulation looks intact.
- **Loose termination in motor junction box (~15%)** Connections inside the motor peckerhead are loose, oxidized, or melted, breaking the circuit path.
- **Damaged control or option card (~10%)** A faulty encoder option card or the main control board fails to process current feedback, triggering a false disconnected alarm.
- **Incorrect closed-loop settings (~5%)** The drive is configured for sensorless closed-loop mode but feedback is missing or the cable is open, causing detection logic errors.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Do all three U, V, W terminals show continuity (near 0 Ω) between the drive and motor?</summary>
<div class="dtree-body"><strong>Yes:</strong> The cable is intact. Check for loose connections in the motor junction box or a faulty control board inside the drive.<br><strong>No:</strong> One phase is open. Replace the motor power cable or repair the broken wire.</div>
</details>

<details class="dtree"><summary>Is the motor junction box (peckerhead) free of melted, oxidized, or loose connections?</summary>
<div class="dtree-body"><strong>Yes:</strong> The issue is likely internal to the drive. Test by temporarily switching to open-loop (V/f) mode or replace the control board.<br><strong>No:</strong> Clean and re-terminate the connections in the motor junction box, ensuring all screws are tight.</div>
</details>

<details class="dtree"><summary>Does the fault clear when you temporarily change from closed-loop to open-loop control mode?</summary>
<div class="dtree-body"><strong>Yes:</strong> The problem is in the feedback path or encoder circuit, not the power cable. Check encoder wiring and option cards.<br><strong>No:</strong> The power cable or internal current sensor is faulty. Replace the cable or the drive's control board.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive** and wait for the CHARGE light to extinguish (approximately 5 minutes) so the DC bus capacitors are safe to work around.
2. **Inspect all U, V, W terminals** at the drive output and inside the motor junction box. Look for loose screws, burned contacts, or corrosion. Tighten any loose terminals to the manufacturer's specified torque (consult your model's manual).
3. **Test continuity** on each of the three motor power wires using a multimeter. Measure between the drive U terminal and motor U terminal, then repeat for V and W. Resistance should be less than 1 Ω (practically 0 Ω). If any phase reads open, the cable is broken.
4. **Open the motor junction box** (peckerhead) and inspect the internal connections. Look for melted wires, folded-back conductors, or loose lugs that may have been missed in the visual check. Re-seat and tighten all connections.
5. **Re-seat encoder and option card connectors** at the drive. A loose encoder feedback cable can trigger similar detection errors. Remove and firmly re-insert the connectors.
6. **Test in open-loop mode** (V/f control) if the motor is confirmed connected but the fault persists. Change the motor control method parameter temporarily to bypass closed-loop feedback logic. If the fault clears, the issue is in the feedback path, not the power cable.
7. **Replace the control board or power card** if the cable and all connections test perfect and the fault remains. A damaged current detection circuit on the gate drive board or main control board is the likely cause at this point.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor power cable (U, V, W) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-al-33-fault-code&k=Motor+power+cable+%28U%2C+V%2C+W%29&tag=errorcodefixes-20) \| Match the original gauge and length, rated for VFD service (shielded if possible). |
| Yaskawa A1000 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-al-33-fault-code&k=Yaskawa+A1000+control+board&tag=errorcodefixes-20) \| Order by exact drive model and revision number from the nameplate. |

## When to Call a Pro

Call a qualified electrician or VFD technician if you are not comfortable working around high-voltage industrial equipment. This fault requires safe lockout/tagout, testing with the DC bus charged down, and interpreting continuity measurements on motor power circuits. If the cable and terminations test good but the fault persists, the repair involves replacing internal drive boards or the entire VFD, which requires expertise in drive commissioning, parameter backup, and proper grounding practices. Incorrect wiring or board replacement can damage the drive or motor and create arc-flash hazards.

**Rough cost:** A pro service call runs about $150-400 for cable replacement or terminal repair, $600-1,200 if control board replacement is needed.

## See Also

- [Yaskawa GA800 VFD F038/oS Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-f038-fault-code/)
- [Yaskawa GA800 E08 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-e08-fault-code/)
- [Yaskawa GA800 E51 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-e51-fault-code/)
- [Yaskawa GA800 E02 Fault Code - Causes & Fix](/posts/yaskawa-ga800-vfd-e02-fault-code/)
