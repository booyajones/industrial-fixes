---
title: "Yaskawa A1000 AL16 - Causes & Fix"
description: "AL16 means encoder feedback fault-the drive lost the position signal from the motor. Most often a loose or broken encoder cable."
pubDatetime: 2026-06-28T10:33:41Z
modDatetime: 2026-06-28T10:33:41Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Yaskawa encoder option card (PGD2 or PGX2)"
most_likely_cause: "Broken or loose encoder cable or terminations"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power off the drive and wait for the CHARGE light to go out, then inspect the encoder cable for visible damage and verify all plug connections at the option card and motor encoder plug are fully seated and tight."
  - "Open the motor peckerhead (terminal box) and look for loose, folded, or melted wires where the encoder cable connects inside the motor."
  - "Use a multimeter to check continuity of each encoder signal wire from the option card to the motor plug, looking for open circuits or short circuits to ground."
no_buy_pct: "60%"
---

## Yaskawa A1000 AL16 — What It Means

The AL16 fault (displayed without a hyphen) indicates that the Yaskawa A1000 VFD has lost the encoder feedback signal from the motor or the signal is outside the acceptable range. The drive relies on this feedback for closed-loop vector control or servo applications to verify the motor's speed and position. Without a valid encoder signal, the drive cannot safely operate in closed-loop mode and trips to protect the system.

This fault is almost always a wiring or hardware issue rather than a motor problem. The encoder signal must travel from the motor through a cable to an option card (such as a PGD2 or PGX2) mounted in the drive. Any break, loose connection, or damage along that path will trigger AL16. In some cases incorrect parameter settings can also cause the fault if the drive is expecting a different encoder type or resolution than what is actually installed.

## Before You Replace Anything

Technicians often replace the encoder option card or the encoder itself before inspecting the wiring. Check continuity and resistance of the encoder cable and inspect connections inside the motor terminal box (peckerhead) first, as loose or folded wires there are a frequent hidden cause.

[Jump to Fix](#fix)

## Common Causes

- **Broken or disconnected encoder cable (~35%)** The cable between the encoder and the drive option card is cut, unplugged, or has broken conductors inside the jacket.
- **Loose or faulty terminations (~30%)** Screw terminals or plug connections at the option card or the motor encoder plug are loose, oxidized, or improperly seated.
- **Internal wiring damage in motor peckerhead (~20%)** Loose connections inside the motor's terminal box where the encoder wires connect, often folded behind other wires or damaged by heat.
- **Damaged encoder (~10%)** The motor encoder itself has failed internally due to contamination, bearing wear, or electronics failure.
- **Option card or control board failure (~5%)** The encoder input option card or the drive's main control board is defective and cannot read the signal.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>With power off, do all encoder cable connections at the drive option card and motor plug feel tight and fully seated?</summary>
<div class="dtree-body"><strong>Yes:</strong> Wiring connections are likely good. Proceed to continuity testing of the cable and internal motor wiring inspection.<br><strong>No:</strong> Reseat all connections firmly. Power up and test. If the fault clears, the loose connection was the cause. If not, continue diagnostics.</div>
</details>

<details class="dtree"><summary>Does a continuity test of each encoder signal wire show less than 1 ohm from the option card to the motor plug, with no shorts to ground?</summary>
<div class="dtree-body"><strong>Yes:</strong> The cable is intact. The fault is likely a bad encoder, option card, or incorrect parameters. Check parameter E5-02 matches encoder resolution.<br><strong>No:</strong> The cable has an open or short. Repair or replace the encoder cable and re-test.</div>
</details>

<details class="dtree"><summary>After inspecting the motor peckerhead, are all encoder wire terminations inside the motor tight and undamaged?</summary>
<div class="dtree-body"><strong>Yes:</strong> Internal motor wiring is good. Suspect the encoder itself or the option card. Swap the option card with a known-good unit to isolate.<br><strong>No:</strong> Re-terminate any loose or damaged wires inside the peckerhead, close the box, and re-test. This often resolves the fault.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power off the drive** and lock out the disconnect. Wait for the CHARGE indicator light to extinguish completely before touching any wiring.
2. **Inspect the encoder cable** for visible cuts, abrasion, or burn marks along its entire length from the drive to the motor.
3. **Check all external terminations** at the encoder option card inside the drive cabinet and at the encoder plug on the motor. Tighten any loose screws or reseat connectors.
4. **Open the motor peckerhead** (terminal box) and look for loose, folded, or heat-damaged encoder wires where they connect inside. Re-terminate any suspect connections.
5. **Perform continuity tests** on each encoder signal wire using a multimeter. Verify less than 1 ohm resistance end to end and no shorts between signal lines or to ground.
6. **Swap the encoder option card** with a known-good spare if available. If the fault clears, the original card was defective. If the fault persists, suspect the encoder or control board.
7. **Verify drive parameters** E5-01 (motor type) and E5-02 (encoder resolution) match the actual motor and encoder specifications. If closed-loop operation is not required, change parameter L6-01 to open-loop mode to bypass the encoder check.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa encoder option card (PGD2 or PGX2) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-al-16-fault-code&k=Yaskawa+encoder+option+card+%28PGD2+or+PGX2%29&tag=errorcodefixes-20) \| Match the card model to your drive series and encoder signal type (TTL or HTL). |
| Replacement encoder cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-al-16-fault-code&k=Replacement+encoder+cable&tag=errorcodefixes-20) \| Order the correct length and connector type for your motor model; consult the motor nameplate or manual. |
| Motor encoder (incremental or absolute) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-al-16-fault-code&k=Motor+encoder+%28incremental+or+absolute%29&tag=errorcodefixes-20) \| Must match the motor shaft size and encoder resolution (pulses per revolution) specified in parameter E5-02. |

## When to Call a Pro

Call a qualified technician or VFD specialist if you are not comfortable working around high-voltage industrial equipment or if you lack the tools to safely lock out power and perform continuity testing. If the fault persists after checking all wiring and connections, the encoder, option card, or main control board may need replacement, which requires knowledge of drive configuration and parameter setup. If the drive is part of a critical production process, a professional can minimize downtime and verify proper closed-loop tuning after repair.

**Rough cost:** A pro service call runs about $200-600.

## See Also

- [Yaskawa GA800 F023 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-f023-fault-code/)
- [Yaskawa A1000 AL-22 - Causes & Fix](/posts/yaskawa-a1000-vfd-al-22-fault-code/)
- [Yaskawa GA800 E42 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-e42-fault-code/)
- [Yaskawa GA800 E10 Fault Code - Causes & Fix](/posts/yaskawa-ga800-e10-fault-code/)
