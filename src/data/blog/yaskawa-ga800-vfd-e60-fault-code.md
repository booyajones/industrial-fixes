---
title: "Yaskawa GA800 VFD E60 Fault - Causes & Fix"
description: "E60 is not a standard GA800 code. Verify the display shows UV3 (soft-charge relay fault). Most likely cause: failed bypass relay."
pubDatetime: 2026-06-06T11:45:43Z
modDatetime: 2026-06-06T11:45:43Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
most_likely_cause: "Failed soft-charge bypass relay or contactor"
likelihood: "the most common cause"
diy_or_pro: "pro"
money_part: "GA800 control board (PCB)"
---

## Yaskawa GA800 VFD E60 Fault — What It Means

E60 is not a documented fault code for the Yaskawa GA800 VFD in manufacturer literature. The GA800 uses UV3 to indicate a Soft Charge Answerback Fault, which means the soft-charge bypass relay or contactor has failed to respond correctly during power-up. This relay pre-charges the DC bus capacitors before the main contactor closes. If you see E60 on your display, first confirm the exact code shown on the keypad and verify whether it is actually UV3 or another fault code.

The soft-charge circuit protects the drive from inrush current during startup. When the relay fails, welds closed, or the control board cannot detect its status, the drive will not complete the power-up sequence and will halt with a fault. The GA800 tracks relay lifecycle in parameter U4-06 (PreChargeRelayMainte). When this value exceeds 90 percent, the relay is near end-of-life and board or drive replacement is recommended.

## Before You Replace Anything

Technicians sometimes replace the entire drive when only the control board is faulty. Check parameter U4-06 first to see if the relay maintenance counter is above 90 percent, which confirms relay wear and points to board replacement rather than a full drive swap.

[Jump to Fix](#fix)

## Common Causes

- **Failed soft-charge bypass relay** The relay that pre-charges the DC bus capacitors has worn out, welded closed, or will not energize.
- **Control board relay driver fault** The transistor or circuit on the control board that commands the relay has failed and cannot drive the coil.
- **Relay contact welding or sticking** High inrush current or repeated cycling has caused the relay contacts to weld together or stick, preventing normal operation.
- **End-of-life relay wear** The soft-charge relay has reached its rated number of operations, shown by U4-06 exceeding 90 percent.
- **Wiring or connector fault in relay circuit** A loose connection, broken wire, or corroded terminal prevents the control board from sensing relay status.
- **Incorrect fault code display** The displayed code may be misread or the drive may be reporting a different fault family, so always verify the exact alphanumeric code on the keypad.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the keypad display show UV3 instead of E60?</summary>
<div class="dtree-body"><strong>Yes:</strong> UV3 is the verified soft-charge answerback fault. Proceed to check parameter U4-06 and cycle power.<br><strong>No:</strong> Confirm the exact code by navigating to the fault history screen on the keypad. E60 may be a non-standard code or a misread display.</div>
</details>

<details class="dtree"><summary>Is parameter U4-06 (PreChargeRelayMainte) above 90 percent?</summary>
<div class="dtree-body"><strong>Yes:</strong> The relay is near end-of-life. Plan to replace the control board or the entire drive.<br><strong>No:</strong> The relay may have failed prematurely. Cycle power and inspect the control board for visible damage or burnt components.</div>
</details>

<details class="dtree"><summary>Does the fault clear after cycling power (turn off AC input, wait 60 seconds, re-energize)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Monitor the drive. If the fault returns, replace the control board or drive.<br><strong>No:</strong> The relay or control board has a permanent fault. Replace the control board or drive as the next step.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify the exact fault code** displayed on the GA800 keypad. Confirm whether it reads E60, UV3, or another code by checking the main display and navigating to the fault-history menu.
2. **Record parameter U4-06** (PreChargeRelayMainte) from the monitor menu. If the value is above 90 percent, the relay is at end-of-life and board or drive replacement is required.
3. **Turn off AC input power** to the drive and wait at least 60 seconds for the DC bus to discharge fully before re-energizing.
4. **Re-energize the drive** and observe whether the fault clears. If the drive powers up normally, monitor it during operation and check for intermittent faults.
5. **Inspect the control board** for visible signs of damage, burnt relay components, or loose connectors if the fault persists after re-energizing.
6. **Replace the control board** if U4-06 is high or if visual inspection shows relay or driver failure. Follow proper ESD precautions and make sure all connectors are seated firmly.
7. **Replace the entire drive** if the fault remains after control board replacement, or if the drive manufacturer recommends drive replacement for this fault condition based on the service bulletin for your serial number.

## Parts Often Needed

| Part | Notes |
|------|-------|
| GA800 control board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e60-fault-code&k=GA800+control+board+%28PCB%29&tag=errorcodefixes-20) \| Match the exact GA800 model and power rating. Verify part number from the existing board label. |
| Yaskawa GA800 VFD (replacement drive) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e60-fault-code&k=Yaskawa+GA800+VFD+%28replacement+drive%29&tag=errorcodefixes-20) \| Specify horsepower, voltage, and enclosure type. Use when board replacement is not sufficient or cost-effective. |

## When to Call a Pro

Call a qualified electrician or VFD technician if you see E60 or UV3 on a GA800 and are not trained in high-voltage industrial equipment. The drive contains lethal DC bus voltages that persist after AC power is removed. Technicians must use proper lockout/tagout, wait for full discharge, and verify zero voltage with a meter before touching internal components. Control board replacement requires ESD handling, correct seating of multi-pin connectors, and parameter backup and restoration. If the drive is part of a critical process or if you lack the tools to check U4-06 and perform power cycling safely, professional service will prevent extended downtime and secondary damage to motors or connected machinery.

**Rough cost:** A pro service call runs about $400-$1,200 for control board or drive replacement, 1-3 hours labor.

## See Also

- [Yaskawa GA800 E24 Fault Code - Causes & Fix](/posts/yaskawa-ga800-vfd-e24-fault-code/)
- [Yaskawa GA800 F023 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-f023-fault-code/)
- [Yaskawa GA800 E61 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-e61-fault-code/)
- [Yaskawa GA800 E39 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-e39-fault-code/)
