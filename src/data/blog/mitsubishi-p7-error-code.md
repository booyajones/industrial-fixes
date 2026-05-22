---
title: "Mitsubishi P7 Error Code — System Mode Mismatch Fix"
description: "A Mitsubishi P7 means one or more indoor units in a multi-zone or VRF (variable refrigerant flow) system has requested a mode (heating or cooling) that..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: mitsubishi-p7-error-code
featured: false
draft: false
tags:
  - mitsubishi
  - hvac
  - error-codes
  - system-mode-mismatch
---
## Quick answer

A Mitsubishi P7 means one or more indoor units in a multi-zone or VRF (variable refrigerant flow) system has requested a mode (heating or cooling) that conflicts with what the outdoor or other indoor units are currently operating in. This is a heat pump / multi-zone problem unique to systems that can only run all indoors in the same mode (heat OR cool, not simultaneous) at the outdoor — which is the case for MXZ multi-zone heat pumps, but not for the more advanced City Multi R2 / WR2 heat recovery systems. The fix is usually rezoning the operating modes, not replacing hardware.

## What P7 means on a Mitsubishi

Mitsubishi's standard multi-zone MXZ heat pumps (MXZ-2C20NA, MXZ-3C24NA, MXZ-4C36NA, MXZ-5C42NA, MXZ-8C48NA series) use a single refrigerant circuit that can deliver heating OR cooling to multiple indoor heads simultaneously — but all indoors must be in the same mode (all heating or all cooling) at any given time.

If one indoor head is set to Cool mode and another indoor head on the same outdoor is set to Heat mode, the system can't physically deliver both. The microcontroller logic detects this mode conflict, declares P7 on the conflicting unit(s), and prevents operation of the unit whose mode "lost the priority battle." Typically the unit that was running first (or the master unit if configured) wins; the conflicting unit displays P7.

P7 is NOT a fault in the equipment sense — nothing is broken. It's the system telling you the operating modes you've requested aren't physically possible on this outdoor unit class.

The error appears on the wired remote (PAR-31MAA, PAR-32MAA, MA Smart) or wireless handheld with "P7" displayed alongside the address. If you have Kumo Cloud or AE-200 central control, P7 displays with the conflicting unit identified.

City Multi R2 (PURY-EP) and WR2 systems with heat recovery branch controllers (BC controllers, CMB-P series) CAN deliver heating and cooling simultaneously to different indoors. P7 should not occur on properly configured heat recovery systems unless something is wrong with the BC controller's mode logic.

## Common causes (ranked by frequency)

1. **Operator setting a conflicting mode on one head** — about 60%. Most common — someone in the household set one head to heat and another to cool. P7 fires on whichever lost the priority.
2. **Auto mode on multiple heads with different setpoints** — about 15%. Auto mode means the head decides heat vs cool based on room vs setpoint. Two heads in Auto in adjacent rooms with different setpoints can request opposite modes, triggering P7.
3. **Stuck or sticky mode setting in non-volatile memory** — about 8%. The remote thinks one mode is set, the indoor PCB thinks another. Power cycle of just the indoor often clears it.
4. **Misconfigured master/slave priority** — about 5%. Multi-zone systems can be configured for one indoor as master; if the priority settings are wrong, mode conflicts persist.
5. **Defective wired remote sending wrong mode commands** — about 4%. The PAR-31 or similar has a stuck button or failed PCB.
6. **Wireless interference between handheld remote and indoor receiver** — about 4%. Sometimes a partial command gets through, indoor goes to a mode the user didn't intend.
7. **Different platforms mixed (M-Series indoor on P-Series outdoor)** — about 2%. Compatibility issue from a recent install or swap.
8. **City Multi BC controller fault** — about 2%. Only applies to heat recovery systems; a real hardware issue with mode routing.

**Field-knowledge nugget:** Mitsubishi MXZ-5C42NA and MXZ-8C48NA multi-zone systems with five or more indoor heads installed in two-story homes have a particular P7 pattern that homeowners cause without realizing it. Upstairs gets warm in the afternoon, the homeowner sets the upstairs bedroom head to Cool, but downstairs is still in Heat mode from morning. P7 fires on the upstairs head. The homeowner sees "error" and calls service. The fix is education, not hardware — explain that the MXZ is a single-mode outdoor, and that switching seasons requires switching ALL heads to the same mode (or upgrading to a heat-recovery City Multi R2). On a Connecticut install where this happened three times in one summer, I added a laminated card next to the master remote explaining the limitation. No more nuisance calls. Sometimes the fix is documentation.

## Step-by-step fix

This is one of the easier codes to resolve — most P7 calls are operator-set, not equipment failures.

1. **Confirm P7 on the affected unit's controller.** Note the address number.

2. **Identify what mode every indoor unit is set to.** Walk through the house. For each Mitsubishi indoor head, check the wired remote or handheld remote display. Note: mode (Cool, Heat, Auto, Dry, Fan), setpoint temperature, fan speed.

3. **Look for the mode conflict.** Common patterns:
   - One head in Cool, another in Heat — obvious conflict
   - Multiple heads in Auto with very different setpoints in different rooms — Auto-mode conflict
   - One head in Dry mode (which is technically cooling) while another is in Heat

4. **Set all indoor heads to the same mode.** Either all Cool or all Heat. Take any heads not currently needed and turn them Off (Off doesn't conflict with any active mode).

5. **If the conflict was caused by Auto mode on multiple heads,** change the heads to manual Cool or Heat instead of Auto. Auto mode is convenient but causes problems on multi-zone MXZ systems with diverse heating/cooling loads.

6. **Power-cycle the indoor unit displaying P7.** Drop power at the breaker for 60 seconds. Restore. The fault should clear on its own once mode conflicts are resolved.

7. **Verify normal operation across all heads.** Run all active heads for at least 10 minutes. P7 should not return as long as modes remain consistent.

8. **If P7 returns despite consistent modes,** check the wired remote. Try operating via the wireless handheld instead. If wired remote causes P7 but handheld doesn't, the wired remote is sending wrong commands — replace the remote.

9. **Educate the user.** Walk through the multi-zone limitation. Show them how to verify all heads are in the same mode. Print or laminate a quick-reference card if you're in a service-contract relationship.

## Parts that may need replacement

P7 rarely requires hardware replacement. When it does:

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| PAR-31MAA wired remote controller | Mitsubishi PAR-31MAA | $185-285 | [HVAC Parts Shop](https://www.hvacpartsshop.com) |
| PAR-32MAA wired remote (current model) | Mitsubishi PAR-32MAA | $245-345 | [HVAC Parts Shop](https://www.hvacpartsshop.com), [Grainger](https://www.grainger.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=mitsubishi-p7-error-code) |
| Wireless handheld remote (M-Series) | Mitsubishi E12758450 | $45-85 | [Amazon](https://www.amazon.com), [HVAC Parts Shop](https://www.hvacpartsshop.com) |
| Indoor PCB (replacement) | Model-specific (E22M-prefix family) | $385-585 | [HVAC Parts Shop](https://www.hvacpartsshop.com) |
| Indoor signal receiver (IR window assembly) | Model-specific | $85-145 | [HVAC Parts Shop](https://www.hvacpartsshop.com) |
| AE-200 central controller (commercial systems) | Mitsubishi AE-200A | $1,800-2,400 | [HVAC Parts Shop](https://www.hvacpartsshop.com) |

## When to call a professional

Call a licensed HVAC tech with Mitsubishi training for P7 if:

- The system is City Multi (PURY, PUMY, R2 heat recovery). VRF systems have additional mode-management logic involving BC controllers and address configurations that require the Mitsubishi service tool to diagnose properly.
- P7 persists after you've confirmed all heads are in the same mode. Either a configuration issue with master/priority assignments, or a real PCB issue.
- The system has more than 5 indoor heads. Mode coordination across many heads benefits from a centralized control like AE-200 — installation review may be appropriate.
- You're upgrading from a standard MXZ to a heat-recovery R2 system because of frequent P7s. The upgrade is significant and needs proper engineering.
- The unit is under Mitsubishi factory warranty.

## FAQs

**Why can't my multi-zone Mitsubishi do heating and cooling at the same time?**
Because the MXZ heat pump has a single refrigerant circuit. Refrigerant either flows in the heating direction (motor running clockwise, four-way valve in heat position) or the cooling direction. It can't be both at once. Heat-recovery systems (City Multi R2) use additional mode-changing branch controllers but cost significantly more.

**Is P7 a "fault" I need to fix, or just informational?**
It's informational in the sense that nothing is broken, but it's a fault in that the unit displaying P7 will not operate until you resolve the mode conflict. It's an operating-limit notification, not a hardware failure.

**My MXZ is set to Auto mode on all heads. Why am I getting P7?**
Auto mode lets each head independently decide heating or cooling based on room temp vs setpoint. If rooms have different temperatures or different setpoints, the heads may request opposite modes. Solution: switch to manual Cool or Heat seasonally rather than relying on Auto on a multi-zone MXZ system.

**Can I upgrade my MXZ outdoor to a heat-recovery system?**
Not as a parts swap — heat recovery requires a different outdoor, different indoors that support 3-pipe systems, and BC controllers. This is a system redesign, not a component upgrade. Talk to your installer about cost vs benefit.

**My PAR-31 wired remote shows P7 but the system seems to be running. Is it actually faulted?**
On some Mitsubishi platforms the P7 is logged but doesn't necessarily prevent operation if the conflict is intermittent. Check whether the affected indoor is actually delivering — if airflow and temperature change as commanded, the system has resolved internally. P7 should still be cleared by addressing the mode conflict.

## Related guides

- [Mitsubishi Mini Split P1 Error Code — Indoor Coil Thermistor Fix](/posts/mitsubishi-p1-error-code)
- [Mitsubishi P3 Error Code — Outdoor Coil Thermistor Fix](/posts/mitsubishi-p3-error-code)
- [Mitsubishi P4 Error Code — Drain Switch Fix](/posts/mitsubishi-p4-error-code)
