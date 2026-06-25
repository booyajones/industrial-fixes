---
title: "Danfoss FC302 VFD ALARM 38 - Causes & Fix"
description: "ALARM 38 (Internal Fault) means the control card detected an undefined hardware or firmware error. Most often cleared by a power cycle."
pubDatetime: 2026-06-23T10:19:11Z
modDatetime: 2026-06-23T10:19:11Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 Control PCB (Logic Card)"
most_likely_cause: "Transient software error or firmware glitch"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power cycle the drive completely (disconnect mains, wait for DC link discharge, reconnect power) to clear transient errors"
  - "Check Parameter 15-32 to retrieve the specific sub-code and determine if the fault is transient or hardware-related"
  - "Inspect control wiring and option card seating for loose connections or incorrect signal type programming"
no_buy_pct: "40%"
---

## Danfoss FC302 VFD ALARM 38 — What It Means

ALARM 38 (Internal Fault) is a generic catch-all error code on the Danfoss FC302 (and FC-102 series) indicating that the drive's control card has detected a condition that does not match any other specific alarm criteria. It signals an undefined internal hardware failure, software corruption, memory error, or gate driver circuit fault. The specific underlying failure is logged in Parameter 15-32 (Alarm Log: Error Code) as a sub-code (e.g., 5376–65535), which provides the exact internal fault number required for advanced diagnosis.

Note: There is no specific "AL-102" fault code in Danfoss documentation. This may be a misinterpretation of the model series (FC-102) or a typo. The standard internal fault code for both FC-102 and FC-302 series is ALARM 38.

## Before You Replace Anything

Technicians sometimes replace the entire power stage board when the fault is actually a control PCB or firmware issue. Always retrieve the sub-code from Parameter 15-32 and power cycle the drive multiple times before ordering any boards.

[Jump to Fix](#fix)

## Common Causes

- **Transient software error or firmware glitch (~40%)** Temporary memory corruption or logic fault that clears after a full power cycle, often triggered by voltage spikes or electromagnetic interference.
- **Control board (logic PCB) failure (~30%)** Failed components on the control card such as gate driver circuits, memory chips, or processor subsystems.
- **Firmware or parameter memory corruption (~15%)** Corrupted parameter storage or firmware blocks caused by severe power surges, lightning strikes, or aging EEPROM cells.
- **Gate driver circuit fault (~10%)** Failure in the circuitry that drives the inverter IGBTs, preventing proper switching signal generation.
- **Transient power surge damage (~5%)** Lightning or severe voltage spikes damaging control electronics while leaving the power stage physically intact.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the alarm clear after a full power cycle (mains disconnected, DC link discharged, then reconnected)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault was likely a transient software error. Monitor the drive for recurring alarms and check for external electrical noise sources.<br><strong>No:</strong> The fault is a genuine hardware or firmware failure. Proceed to retrieve the sub-code from Parameter 15-32 and inspect control wiring.</div>
</details>

<details class="dtree"><summary>Does Parameter 15-32 show the same sub-code after multiple power cycles?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is repeatable hardware damage. Replace the control PCB or power stage board depending on the sub-code value (consult Danfoss support for sub-code interpretation).<br><strong>No:</strong> The fault is intermittent. Check for loose option cards, wiring faults, or environmental factors (heat, humidity, vibration).</div>
</details>

<details class="dtree"><summary>Are all option cards and control wiring connections properly seated and secured?</summary>
<div class="dtree-body"><strong>Yes:</strong> Wiring is not the issue. The fault is internal to the drive hardware. Contact a qualified VFD technician for board-level diagnosis.<br><strong>No:</strong> Reseat all option cards and tighten control terminal connections, then power cycle the drive again.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Retrieve the sub-code from Parameter 15-32** on the LCP display and write down the specific error number (this identifies whether the fault is memory, gate driver, or logic card related).
2. **Power cycle the drive completely** by turning it OFF, disconnecting mains power, waiting for all LEDs to go dark (DC link discharge), then reconnecting power.
3. **Check if the alarm clears** after the power cycle. If the drive runs normally and ALARM 38 does not return, the fault was a transient software error and no further action is needed.
4. **Inspect control wiring and option cards** if the alarm persists. Verify that all cards are fully seated, terminal connections are tight, and programming matches the analog signal type.
5. **Run input terminal and voltage tests** using the drive's diagnostic menu to confirm no external signal interference is confusing the control logic.
6. **Verify cooling system operation** by checking that heatsink fans are running and vents are not blocked (though ALARM 38 is not a temperature alarm, overheating can cause component failure).
7. **Replace the control PCB (logic card)** if the alarm persists after multiple power cycles and the sub-code indicates a control board fault (most common hardware repair).
8. **Replace the power stage board** if the sub-code indicates IGBT or gate driver circuit issues (consult Danfoss technical support for sub-code interpretation before ordering parts).

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 Control PCB (Logic Card) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-102-fault-code&k=Danfoss+FC302+Control+PCB+%28Logic+Card%29&tag=errorcodefixes-20) \| Match the exact part number printed on your current control card; varies by drive frame size and firmware version. |
| Danfoss FC302 Power Stage Board (Inverter Module) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-102-fault-code&k=Danfoss+FC302+Power+Stage+Board+%28Inverter+Module%29&tag=errorcodefixes-20) \| Required only if sub-code indicates gate driver or IGBT fault; consult Danfoss support for proper diagnosis. |

## When to Call a Pro

Call a qualified VFD technician or industrial electrician if the alarm persists after a power cycle, if you lack the tools or training to safely work inside the drive enclosure, or if the sub-code from Parameter 15-32 indicates a hardware fault requiring board replacement. VFD internals carry high voltage (DC link capacitors can remain charged even after mains power is disconnected) and require proper lockout/tagout procedures. Board-level diagnosis and firmware recovery also require factory diagnostic software and training. If the drive is under warranty or part of a critical process, contact Danfoss technical support or an authorized service center before attempting repairs.

**Rough cost:** A pro service call runs about $300-800 depending on whether control card or power stage replacement is needed.

## See Also

- [Danfoss FC302 ALARM 35 - Causes & Fix](/posts/danfoss-fc302-alarm-35-fault-code/)
- [Danfoss FC302 Alarm 27 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-27-fault-code/)
- [Danfoss FC302 AL-91 - Causes & Fix](/posts/danfoss-fc302-vfd-al-91-fault-code/)
- [Danfoss FC302 Alarm 74 - Causes & Fix](/posts/danfoss-fc302-vfd-al-74-fault-code/)
