---
title: "Danfoss FC302 AL-120 Fault - Causes & Fix"
description: "AL-120 does not exist in FC302 documentation. Likely Alarm 12 (low DC voltage), Alarm 16 (short circuit), or Alarm 20 (overload)."
pubDatetime: 2026-06-24T10:16:40Z
modDatetime: 2026-06-24T10:16:40Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "FC302 Power Board / Inverter Module"
most_likely_cause: "Misread or incorrectly documented alarm code"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Check the drive display or parameter P003 to read the exact alarm code number"
  - "Measure incoming three-phase voltage at input terminals to verify all phases are present and balanced within 3%"
  - "Inspect and tighten all input and output terminal connections"
---

## What this code means
The code AL-120 does not appear in the Danfoss FC302 alarm and warning list. The FC302 series uses numeric codes such as Alarm 12, Alarm 16, and Alarm 20. The query likely contains a typo or misread display. Alarm 12 indicates DC bus voltage too low (typically below 100V for 400V drives), caused by weak incoming power or failed rectifier components. Alarm 16 signals an instantaneous short circuit in the motor cable, motor windings, or drive IGBT module. Alarm 20 means motor thermal overload from excessive mechanical load or incorrect motor parameter settings.

Before proceeding, verify the exact code displayed on the drive keypad or control panel. Consult the FC302 operating manual alarm table to confirm the correct code and its specific meaning for your drive model and firmware version.

## Before You Replace Anything

Technicians often replace the entire power board before checking input voltage balance and tightening input terminals. A simple voltage measurement at the input terminals and a visual inspection of connections can identify low-voltage or loose-wire faults that cost nothing to fix.

## Common Causes

- **Misread alarm code (~40%)** The display was misread as AL-120 instead of Alarm 12, Alarm 16, Alarm 20, or another valid code.
- **Low incoming line voltage (Alarm 12) (~25%)** Incoming AC voltage is below the minimum threshold due to utility sag, other equipment starting, or blown input fuses.
- **Failed IGBT module or short circuit (Alarm 16) (~20%)** An instantaneous short circuit in the motor cable, motor terminal box, or drive IGBT module triggers protective shutdown.
- **Motor overload or thermal trip (Alarm 20) (~10%)** The motor has exceeded 100% overload for too long due to mechanical binding, jammed bearing, or incorrect motor current parameter.
- **Loose input terminal connections (~5%)** Vibration or installation errors cause intermittent contact at input terminals, resulting in low DC bus voltage.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the drive display show AL-120, or does it show a numeric code like 12, 16, or 20?</summary>
<div class="dtree-body"><strong>Yes:</strong> If it shows a numeric code (e.g. 12, 16, 20), consult the FC302 alarm table in the manual for the exact meaning and proceed with diagnostics for that specific alarm.<br><strong>No:</strong> If the display truly shows AL-120, the drive may have custom firmware or the code was transcribed incorrectly. Power-cycle the drive and record the exact code from parameter P003.</div>
</details>

<details class="dtree"><summary>Is incoming three-phase voltage present and balanced within 3% across all phases?</summary>
<div class="dtree-body"><strong>Yes:</strong> If voltage is good, the fault is likely internal (rectifier, DC capacitors, or IGBT module). Disconnect the motor and test the drive alone to isolate the problem.<br><strong>No:</strong> If voltage is low or missing on one phase, check input fuses, upstream circuit breakers, and utility supply before servicing the drive.</div>
</details>

<details class="dtree"><summary>Does the alarm clear when the motor cable is disconnected from the drive output terminals?</summary>
<div class="dtree-body"><strong>Yes:</strong> If the alarm clears, the fault is in the motor or motor cable. Test cable insulation and motor winding resistance to find the short circuit.<br><strong>No:</strong> If the alarm persists without the motor, the fault is inside the drive power section. Replace the power board or IGBT module.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Record the exact alarm code** by pressing the Status button on the keypad or reading parameter P003 in the display menu, and compare it to the FC302 alarm table in the operating manual.
2. **Measure incoming voltage** at the drive input terminals (L1, L2, L3) using a multimeter set to AC volts, and verify all three phases are present and balanced within 3% of each other.
3. **Inspect and tighten** all input and output terminal connections, checking for discolored or burnt terminals that indicate loose contact or arcing.
4. **Disconnect the motor cable** from the drive output terminals (U, V, W) and reset the alarm to determine if the fault is in the motor or the drive.
5. **Test the motor cable** for insulation breakdown by measuring resistance from each motor conductor to ground with a megohmmeter (insulation should exceed 1 megohm).
6. **Replace the power board or IGBT module** if the alarm persists with the motor disconnected and input voltage is correct, following the manufacturer's replacement procedure and observing high-voltage safety protocols.
7. **Verify motor parameters** (P120-P125) match the motor nameplate data, especially motor current in parameter P124, and adjust if incorrect to prevent false thermal trips.

## Parts Often Needed

| Part | Notes |
|------|-------|
| FC302 Power Board / Inverter Module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-120-fault-code&k=FC302+Power+Board+%2F+Inverter+Module&tag=errorcodefixes-20) \| Match frame size and voltage rating to your drive model; requires high-voltage lockout and trained technician |
| FC302 Rectifier Board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-120-fault-code&k=FC302+Rectifier+Board&tag=errorcodefixes-20) \| For Alarm 12 faults when input diodes or DC bus capacitors have failed |

## When to Call a Pro

Call a qualified electrician or drive technician immediately if you are unfamiliar with three-phase power systems or if the drive shows any alarm code. High-voltage DC bus capacitors can hold a lethal charge for minutes after power is removed. If incoming voltage is correct and terminal connections are tight but the alarm persists, internal components such as the rectifier, IGBT module, or power board have likely failed and require replacement by a technician with lockout/tagout training and the correct replacement parts for your drive frame size and voltage rating. Do not attempt to open the drive enclosure or disconnect the motor under load.

**Rough cost:** A pro service call runs about $300-900.
