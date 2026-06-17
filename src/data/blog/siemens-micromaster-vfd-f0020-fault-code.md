---
title: "Siemens Micromaster F0020 - Causes & Fix"
description: "F0020 on a Siemens Micromaster means mains phase missing. Check for a blown fuse, tripped breaker, or loose input wiring at L1/L2/L3."
pubDatetime: 2026-06-02T10:31:53Z
modDatetime: 2026-06-02T10:31:53Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Input line fuses"
most_likely_cause: "Blown input fuse or tripped breaker"
---

## Siemens Micromaster F0020 — What It Means

F0020 on a Siemens Micromaster 440 VFD indicates a mains phase missing fault. The drive does not detect all three incoming supply phases while pulses are enabled and the drive is loaded. In plain terms, one of the three input power phases is absent or the supply is severely imbalanced, so the inverter shuts down to protect itself. The fault occurs only when the drive is running under load, not during idle or standby.

This is a supply-side issue in the vast majority of cases. The drive expects a three-phase supply at L1, L2, and L3. If one phase is open, the internal monitoring trips F0020 and the inverter switches off. Once you correct the upstream supply problem and restore all three phases, you can reset the fault through the drive's normal reset procedure.

[Jump to Fix](#fix)

## Common Causes

- **Blown input fuse or tripped breaker** One of the three incoming line fuses has blown or the breaker feeding the drive has tripped on a single pole, opening one phase.
- **Loose or burned input wiring** A terminal at L1, L2, or L3 is loose, corroded, or heat-damaged, creating an intermittent or permanent open connection on one phase.
- **Upstream disconnect or contactor failure** A failed disconnect switch, line contactor, or isolation device has lost continuity on one pole, cutting off one phase before it reaches the drive.
- **Utility phase loss** The utility supply itself has dropped one phase due to a transformer fault, downed line, or grid event upstream of your service entrance.
- **Severe voltage imbalance** Extreme imbalance or supply quality problems make one phase voltage sag so low that the drive no longer recognizes it as present.
- **Internal rectifier or input-stage hardware fault** If the supply is confirmed good at the drive terminals but F0020 persists, the drive's internal input power section has failed and cannot detect all three phases.

## Step-by-Step Fix {#fix}

1. **Lock out and tag out** the upstream disconnect or breaker, then verify zero voltage at the drive's input terminals before opening covers or touching wiring.
2. **Measure incoming voltage** at L1, L2, and L3 on the drive terminals using a multimeter. Check all three phase-to-phase pairs (L1-L2, L2-L3, L3-L1) and confirm balanced three-phase voltage within the limits on the drive's rating plate.
3. **Inspect upstream protection devices** including fuses, circuit breakers, disconnect switches, and any line contactors. Look for a blown fuse, tripped pole, or burned contact on one phase and replace or reset the failed component.
4. **Check and torque all power terminations** at L1, L2, L3 and at every upstream junction, looking for loose lugs, discoloration, heat marks, or corrosion that indicate a poor connection.
5. **Trace the open phase upstream** if one voltage pair is missing or severely low. Work back through your distribution panel, transformer secondary, and utility service entrance to locate the break.
6. **Restore power and reset the fault** once all three phases are present and balanced at the drive. Use the drive's standard reset button or control-panel reset function to clear F0020.
7. **Replace or service the drive** if the supply is confirmed correct at the input terminals but the fault immediately returns. The internal rectifier or input monitoring circuit has likely failed and requires manufacturer service or drive replacement.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Input line fuses | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-vfd-f0020-fault-code&k=Input+line+fuses&tag=errorcodefixes-20) \| Match the amperage and interrupt rating specified for your drive frame size and supply voltage. Replace all three fuses if one has blown to maintain balanced aging. |
| Input power terminals and lugs | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-vfd-f0020-fault-code&k=Input+power+terminals+and+lugs&tag=errorcodefixes-20) \| Replace any burned, cracked, or corroded terminals at L1, L2, or L3. Use copper lugs rated for the drive's input current and torque to the value in the installation manual. |
| Upstream circuit breaker or disconnect | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-vfd-f0020-fault-code&k=Upstream+circuit+breaker+or+disconnect&tag=errorcodefixes-20) \| If a pole has failed internally, replace the entire breaker or switch assembly. Confirm the replacement is rated for three-phase service and the full load current. |

## When to Call a Pro

Call a licensed electrician or drive specialist if you are not trained in three-phase power troubleshooting or if your facility safety rules require qualified personnel for energized diagnostics. Also call a professional if you have confirmed balanced three-phase voltage at the drive terminals but F0020 will not clear after reset. That points to an internal drive fault requiring manufacturer service or replacement. Finally, if the fault traces back to the utility supply or service entrance, contact your utility company and an electrical contractor to coordinate the repair safely.

## See Also

- [Siemens Micromaster F0035 - Causes & Fix](/posts/siemens-micromaster-vfd-f0035-fault-code/)
- [Siemens Micromaster F0011 - Causes & Fix](/posts/siemens-micromaster-f0011-fault-code/)
- [Siemens G120 F01625 - Causes & Fix](/posts/siemens-g120-f01625-fault-code/)
- [Siemens Micromaster F0015 - Causes & Fix](/posts/siemens-micromaster-vfd-f0015-fault-code/)
