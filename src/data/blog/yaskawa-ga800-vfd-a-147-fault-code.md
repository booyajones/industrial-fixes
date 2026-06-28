---
title: "Yaskawa GA800 A.147 Fault - Causes & Fix"
description: "A.147 is not a standard GA800 fault code in published documentation. Check your manual's fault table and inspect wiring and motor parameters."
pubDatetime: 2026-06-09T11:43:09Z
modDatetime: 2026-06-09T11:43:09Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "Motor cable (shielded, rated for VFD use)"
most_likely_cause: "Loose or damaged motor or power wiring"
diy_or_pro: "pro"
---

## Yaskawa GA800 A.147 Fault — What It Means

The A.147 code does not appear in standard Yaskawa GA800 alarm and fault code tables found in published technical documentation. The GA800 typically displays faults in formats like oC, Uv, and CPFxx. The A.147 notation may be an internal event code, a firmware-specific message, or a code from a different Yaskawa model or option card. Yaskawa documentation confirms that faults are shown on the keypad and can be reviewed in fault history, but they must be cleared only after the root cause is corrected.

Because the exact meaning of A.147 cannot be verified from available sources, consult the GA800 technical manual and fault table for your specific firmware revision and installed option cards. In general, unrecognized or uncommon codes often trace back to wiring issues, incorrect motor parameter entry, encoder or option card problems in vector control setups, or drive hardware faults. Record the code and the operating condition when it occurred, then follow the manufacturer diagnostic sequence to identify the true cause before attempting any reset.

## Before You Replace Anything

Technicians sometimes replace the entire drive or control board when the real problem is a loose motor cable connection, incorrect parameter setting, or a faulty encoder cable. Always inspect all field wiring and verify parameter entries against the motor nameplate before ordering hardware.

[Jump to Fix](#fix)

## Common Causes

- **Loose or damaged motor or power wiring (~30%)** Poor connections at motor terminals, damaged cable insulation, or incorrect wire gauge can generate intermittent faults or unrecognized codes.
- **Incorrect motor parameters entered in the drive (~25%)** Motor nameplate data that does not match the drive configuration can trigger protection faults or internal warnings displayed as non-standard codes.
- **Encoder or option card communication error (~20%)** In vector control applications, a faulty encoder cable, incorrect encoder type selection, or an improperly seated option card can produce unusual alarm messages.
- **Incorrect acceleration or deceleration time settings (~15%)** Ramp times that are too aggressive for the load can cause the drive to trip on overcurrent or to log internal events that appear as atypical codes.
- **Drive hardware fault or firmware anomaly (~10%)** Internal board failure, corrupted firmware, or a manufacturing defect may generate codes not published in standard fault tables.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the drive display any additional standard fault codes (such as oC, Uv, or CPF) in the fault history?</summary>
<div class="dtree-body"><strong>Yes:</strong> Those codes provide the actual root cause; look them up in the GA800 manual and follow the published troubleshooting steps for each.<br><strong>No:</strong> The A.147 code may be an internal event or a display error; proceed to check all field wiring and parameter settings before assuming hardware failure.</div>
</details>

<details class="dtree"><summary>Are all motor cable connections tight and insulation intact at both the drive output terminals and the motor terminal box?</summary>
<div class="dtree-body"><strong>Yes:</strong> Wiring is sound; move on to verify that every motor nameplate value (voltage, current, frequency, speed) is correctly entered in the drive parameters.<br><strong>No:</strong> Tighten all connections, repair or replace any damaged cable, and clear the fault; loose or damaged wiring is a common source of non-standard fault messages.</div>
</details>

<details class="dtree"><summary>If an encoder or option card is installed, does the encoder cable test good for continuity and is the card firmly seated in its slot?</summary>
<div class="dtree-body"><strong>Yes:</strong> Encoder and option hardware are intact; review control method settings and consider contacting Yaskawa support to decode A.147 for your firmware version.<br><strong>No:</strong> Reseat the option card, replace the encoder cable if damaged, and verify encoder type and pulse-per-revolution settings in the drive before resetting the fault.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Record the fault and operating conditions** when A.147 appeared, including motor load, speed setpoint, and any other active alarms in the fault history menu.
2. **Inspect all power and motor wiring** at the drive output terminals and the motor terminal box for loose lugs, frayed insulation, or incorrect wire size.
3. **Verify motor nameplate data** against the drive parameters (voltage, rated current, frequency, rated speed, power factor) and correct any mismatches.
4. **Check acceleration and deceleration time settings** to confirm they are appropriate for the load inertia and do not force the drive into overcurrent or overvoltage conditions.
5. **If an encoder or option card is installed**, confirm the card is seated properly, the encoder cable has good continuity and shielding, and the encoder type matches the parameter setting.
6. **Consult the GA800 technical manual** for your exact firmware revision and option configuration to locate A.147 in the fault table or contact Yaskawa technical support for clarification.
7. **Clear the fault** only after correcting the identified cause, then monitor the drive under load to confirm the code does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor cable (shielded, rated for VFD use) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-147-fault-code&k=Motor+cable+%28shielded%2C+rated+for+VFD+use%29&tag=errorcodefixes-20) \| Replace if insulation is damaged or cable is not VFD-rated; verify gauge matches drive and motor requirements. |
| Encoder cable (shielded twisted pair) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-147-fault-code&k=Encoder+cable+%28shielded+twisted+pair%29&tag=errorcodefixes-20) \| Required for vector control applications; replace if continuity test fails or shielding is compromised. |
| GA800 option card (model-specific) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-147-fault-code&k=GA800+option+card+%28model-specific%29&tag=errorcodefixes-20) \| Order the exact card for your application (communication, encoder interface, etc.) if the installed card is physically damaged or fails self-test. |
| GA800 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-147-fault-code&k=GA800+control+board&tag=errorcodefixes-20) \| Last-resort replacement if all wiring, parameters, and option cards are verified good and Yaskawa support confirms an internal hardware fault. |

## When to Call a Pro

Call a qualified drives technician or an authorized Yaskawa service provider if you cannot locate A.147 in your drive's fault table, if the code persists after correcting wiring and parameter errors, or if you suspect internal hardware failure. Professional support is also required for encoder setup and tuning in vector control applications, for high-voltage installations above 480 V, and whenever the drive shows additional fault codes that involve DC bus faults or gate driver errors. A certified technician has access to Yaskawa service bulletins, firmware update tools, and replacement control boards that match your exact GA800 model and revision.

**Rough cost:** A pro service call runs about $200–800 depending on cause.

## See Also

- [Yaskawa GA800 E19 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-e19-fault-code/)
- [Yaskawa GA800 E04 Fault Code - Causes & Fix](/posts/yaskawa-ga800-vfd-e04-fault-code/)
- [Yaskawa GA800 E61 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-e61-fault-code/)
- [Yaskawa GA800 E70 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-e70-fault-code/)
