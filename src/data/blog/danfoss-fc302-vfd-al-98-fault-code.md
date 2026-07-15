---
title: "Danfoss FC302 AL-98 Fault - Causes & Fix"
description: "AL-98 means the internal Real-Time Clock has failed or lost its settings. Most common fix: reset the warning and manually set the clock parameters."
pubDatetime: 2026-06-23T10:15:57Z
modDatetime: 2026-06-23T10:15:57Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 Control PCB (Logic Card)"
most_likely_cause: "Power interruption with backup circuit failure"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Press the Reset key on the LCP to clear the warning and see if it returns immediately"
  - "Check the LCP display for any other active warnings or faults that might point to a broader control supply issue"
  - "Verify that the drive operates normally after clearing the warning, even if the clock is not set"
part_price: "$250-600"
---

## Danfoss FC302 AL-98 Fault — What It Means

The AL-98 fault (often displayed as Warning 98) on a Danfoss FC302 VFD indicates a Clock Fault. The internal Real-Time Clock (RTC) chip has not been set, has failed, or the stored time data has been lost. This is typically a warning rather than a trip, so the drive can usually continue operating, but time-based functions like scheduling, data logging with timestamps, or automatic start and stop routines will be unreliable or inactive.

The fault is usually triggered by a power interruption combined with a failing backup circuit that cannot sustain the RTC, or by a hardware failure of the RTC integrated circuit on the control board itself. It is distinct from internal hardware faults and specifically points to the clock subsystem.

## Before You Replace Anything

Technicians sometimes replace the entire power board when the fault is actually on the control PCB. Test by swapping the logic card first, which is a faster and cheaper diagnostic step.

[Jump to Fix](#fix)

## Common Causes

- **Power interruption with backup failure (~45%)** A loss of mains power combined with a failing DC-link backup capacitor or control supply circuit that cannot sustain the RTC microchip during shutdown.
- **Control board RTC IC failure (~30%)** The Real-Time Clock integrated circuit on the control PCB has physically failed or is damaged.
- **Firmware or software glitch (~15%)** Corrupted firmware or a reset in the logic card causing the clock to default to zero or an invalid state.
- **Environmental stress on control board (~10%)** Excessive heat or vibration has damaged components on the control board, including the RTC circuit.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the warning clear when you press the Reset key on the LCP?</summary>
<div class="dtree-body"><strong>Yes:</strong> The RTC may just need to be reset manually via parameters (Group 14 or RTC parameters). Set the clock and monitor for recurrence.<br><strong>No:</strong> The warning is latched and likely indicates a hardware failure on the control board. Proceed with power cycle and board inspection.</div>
</details>

<details class="dtree"><summary>Does the warning return immediately after a full power cycle (AC mains off for 10 minutes)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The control board RTC circuit has failed. A logic card swap is needed to confirm the diagnosis.<br><strong>No:</strong> The fault may have been a one-time event from a power glitch. Set the clock parameters and monitor the drive for several days.</div>
</details>

<details class="dtree"><summary>Is the internal 10 V control supply stable and within 9.5 V to 10.5 V?</summary>
<div class="dtree-body"><strong>Yes:</strong> The control supply is good. Focus on the RTC IC and logic card as the likely fault point.<br><strong>No:</strong> An unstable control supply can cause RTC and other logic faults. The control board or power board may need replacement.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Clear the warning** by pressing the Reset key on the Local Control Panel (LCP) and observe whether it returns immediately.
2. **Set the clock manually** using the drive parameters in Group 14 or the specific RTC parameter group to verify that the RTC can accept new data.
3. **Perform a full power cycle** by disconnecting AC mains and any remote DC-link power (including UPS or batteries), then wait 5 to 10 minutes for the DC link to discharge completely before reconnecting power.
4. **Inspect the control PCB** for visible damage such as burnt components, cracked integrated circuits, or signs of overheating on the logic card.
5. **Test the internal control supply** by measuring the 10 V rail with a multimeter. Voltage should be between 9.5 V and 10.5 V under normal operation.
6. **Swap the control PCB (logic card)** with a known-good unit to confirm whether the RTC fault is isolated to the control board.
7. **Monitor the drive** after repair for several operating cycles to make sure the clock retains settings and the warning does not recur.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 Control PCB (Logic Card) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-98-fault-code&k=Danfoss+FC302+Control+PCB+%28Logic+Card%29&tag=errorcodefixes-20) \| The standard replacement for RTC and clock faults. Confirm voltage rating and frame size match your drive model. |
| Danfoss FC302 Power Board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-98-fault-code&k=Danfoss+FC302+Power+Board&tag=errorcodefixes-20) \| Only needed if the 10 V control supply is unstable or damaged, which can affect the RTC circuit. |

## When to Call a Pro

Call a qualified technician or control systems integrator if you are not comfortable working inside the VFD enclosure or handling control board diagnostics. This fault involves electronic troubleshooting and board-level repair, which requires familiarity with VFD internals, safe lockout and tagout procedures, and access to replacement control boards. If the drive is still under warranty or part of a critical industrial process, professional service is recommended to avoid downtime and make sure proper documentation of the repair.

**Rough cost:** A pro service call runs about $300-800 depending on control board replacement and labor.

## See Also

- [Danfoss FC302 Alarm 34 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-34-fault-code/)
- [Danfoss FC302 VFD ALARM 39 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-39-fault-code/)
- [Danfoss FC302 VFD Alarm 33 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-33-fault-code/)
- [Danfoss FC302 VFD Alarm 16 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-16-fault-code/)
