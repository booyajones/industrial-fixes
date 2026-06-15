---
title: "Yaskawa A1000 Hbb Fault - Causes & Fix"
description: "Hbb means the Safe Disable input is open, blocking drive output. Most often missing or loose jumpers at H1-HC and H2-HC are the cause."
pubDatetime: 2026-06-11T10:03:37Z
modDatetime: 2026-06-11T10:03:37Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Wire jumpers for H1-HC and H2-HC terminals"
most_likely_cause: "Missing or loose factory jumpers between H1-HC and H2-HC"
likelihood: "the most common cause"
diy_or_pro: "pro"
---

## Yaskawa A1000 Hbb Fault — What It Means

The Hbb fault on the Yaskawa A1000 VFD stands for Safe Disable Signal Input. The drive has detected that the Safe Disable circuit is open, so it has disabled the output to the motor. The A1000 uses two channels, H1 and H2, that must both be closed to HC for normal operation. When one or both channels are open, the drive protects itself by blocking all output and displaying Hbb.

This is a hardware interlock designed for safety applications. If you are not using an external safety relay or E-stop chain, the drive expects factory jumpers between H1-HC and H2-HC to keep the circuit closed. If those jumpers are missing, loose, or removed, the drive sees an open circuit and triggers Hbb. If you are using external safety contacts, any break in that wiring or an open relay contact will also cause the fault.

## Before You Replace Anything

Technicians sometimes replace the control board when the real problem is simply missing jumpers at the Safe Disable terminals. Always inspect H1, H2, and HC visually and test continuity across the jumpers before ordering any circuit board.

[Jump to Fix](#fix)

## Common Causes

- **Missing or loose H1-HC and H2-HC jumpers (~50%)** When Safe Disable is not being used, the factory jumpers between H1-HC and H2-HC must be in place and tight or the drive sees an open circuit and triggers Hbb.
- **Open or broken external safety wiring (~25%)** If you are using an external E-stop, safety relay, or interlock, any loose connection, broken wire, or open contact in that circuit will open the Safe Disable loop.
- **Incorrect digital input sink or source selection (~15%)** The drive's digital input circuit can be configured as sinking or sourcing, and if the selection does not match your wiring the input may read as open even when physically closed.
- **Intentional safety circuit activation (~5%)** An external safety device such as an E-stop button, light curtain, or safety relay may be intentionally opening the Safe Disable channels because of a real safety condition.
- **Damaged control board or terminal block (~5%)** If the H1, H2, or HC terminals or the internal input circuit are physically damaged, the drive may not see a closed Safe Disable loop even with correct wiring.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Are there wire jumpers installed between H1 and HC, and between H2 and HC, on the drive terminal strip?</summary>
<div class="dtree-body"><strong>Yes:</strong> The jumpers are present. Check that they are tight and making good contact, then move on to test for external wiring issues or incorrect sink/source configuration.<br><strong>No:</strong> The jumpers are missing. If you are not using an external Safe Disable circuit, install jumpers between H1-HC and H2-HC, then power-cycle the drive.</div>
</details>

<details class="dtree"><summary>Are you using an external safety relay, E-stop, or interlock wired to H1, H2, and HC?</summary>
<div class="dtree-body"><strong>Yes:</strong> Verify that both safety channels close at the same time and that all wiring connections are tight. Use a multimeter to confirm continuity from H1 to HC and H2 to HC when the safety circuit is closed.<br><strong>No:</strong> You should be using the factory jumpers instead. Install jumpers between H1-HC and H2-HC, then power-cycle the drive to clear the fault.</div>
</details>

<details class="dtree"><summary>Does the fault clear after you restore correct jumpers or wiring and power-cycle the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> The problem was in the wiring or jumpers. The drive should now run normally. Document what was missing or loose for future reference.<br><strong>No:</strong> The wiring is correct but the fault persists. Suspect a damaged terminal, broken trace on the control board, or an internal input circuit fault. Call a qualified VFD technician or contact Yaskawa support.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive** and follow lockout-tagout procedures before touching any terminals.
2. **Locate terminals H1, H2, and HC** on the A1000 control terminal strip and inspect them closely for jumpers or external wiring.
3. **If Safe Disable is not being used**, verify that a wire jumper is installed between H1 and HC, and another jumper between H2 and HC. If either jumper is missing or loose, install or tighten it.
4. **If you are using external safety contacts**, trace the wiring from your E-stop, safety relay, or interlock to H1, H2, and HC. Use a multimeter to confirm continuity across both channels when the safety circuit is closed.
5. **Check the digital input sink/source configuration** in the drive parameters or DIP switches to match your wiring type. Consult the A1000 manual for the correct setting for your installation.
6. **Restore power to the drive** after confirming correct jumpers or wiring, and monitor the display. Yaskawa recommends power-cycling after correcting the Safe Disable circuit.
7. **If the Hbb fault remains** with verified correct wiring and jumpers, inspect the H1, H2, and HC terminals for physical damage, corrosion, or loose terminal blocks, and consider calling Yaskawa or a VFD service technician for board-level diagnostics.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Wire jumpers for H1-HC and H2-HC terminals | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-hbb-fault-code&k=Wire+jumpers+for+H1-HC+and+H2-HC+terminals&tag=errorcodefixes-20) \| Typically 18–22 AWG short wire links. Use the gauge and type specified in the A1000 installation manual for your frame size. |
| Safety relay or external E-stop contacts | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-hbb-fault-code&k=Safety+relay+or+external+E-stop+contacts&tag=errorcodefixes-20) \| If you are adding or replacing an external Safe Disable circuit, choose dual-channel safety-rated relays or contacts that close both H1 and H2 simultaneously. |

## When to Call a Pro

Call a qualified VFD technician or industrial electrician if you are not familiar with variable frequency drive wiring, if the drive is part of a safety-rated machine installation, or if the Hbb fault persists after you have verified correct jumpers and wiring. High-voltage work on VFD power terminals and internal board-level diagnostics require specialized training and test equipment. Also call a pro if you need to integrate the Safe Disable circuit into a larger safety system with light curtains, E-stops, or safety PLCs, because improper wiring can create serious safety hazards.

**Rough cost:** A pro service call runs about $150-400 depending on service call and whether jumpers or wiring repair is needed.

## See Also

- [Yaskawa A1000 CPF14 Fault - Causes & Fix](/posts/yaskawa-a1000-vfd-cpf14-fault-code/)
- [Yaskawa GA800 E21 Fault Code - Causes & Fix](/posts/yaskawa-ga800-vfd-e21-fault-code/)
- [Yaskawa VFD Fault LF — Causes & Fix](/posts/yaskawa-vfd-fault-lf/)
- [Yaskawa GA800 E47 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-e47-fault-code/)
