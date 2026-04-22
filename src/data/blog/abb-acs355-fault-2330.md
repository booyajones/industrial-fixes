---
title: "ABB ACS355 Fault 2330 — Ground Fault"
description: "ABB ACS355 drive Fault 2330 means a ground fault has been detected on the output. Learn causes, diagnostic steps, and how to clear this VFD fault."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - abb
  - acs355
  - ground-fault
---

# ABB ACS355 Fault 2330 — Ground Fault

**Fault 2330** on the ABB ACS355 variable frequency drive means the drive has detected a ground fault condition on the output — significant current is flowing from one or more output phases to earth ground. The drive shuts down immediately to prevent damage to the motor and drive output stage.

## Jump to Fix

- [Most Likely Cause](#most-likely-cause)
- [Diagnosis Steps](#diagnosis)
- [Parts](#parts)

## What Is a Ground Fault on a VFD?

In a properly wired motor and drive system, output current should flow only through the motor windings — not to ground. A ground fault means current is finding a path to earth through:
- Damaged motor winding insulation
- Damaged motor cable insulation
- Moisture or contamination in the motor or cable
- Faulty output wiring

## Common Causes {#most-likely-cause}

| [Cause](https://www.amazon.com/s?k=Cause&tag=errorcodefixe-20) | Likelihood |
|---|---|
| [Failed motor winding insulation (aged motor)](https://www.amazon.com/s?k=Failed%20motor%20winding%20insulation%20(aged%20motor)&tag=errorcodefixe-20) | High |
| [Damaged output cable (chafed or pinched)](https://www.amazon.com/s?k=Damaged%20output%20cable%20(chafed%20or%20pinched)&tag=errorcodefixe-20) | High |
| [Moisture in motor terminal box](https://www.amazon.com/s?k=Moisture%20in%20motor%20terminal%20box&tag=errorcodefixe-20) | High |
| [Long motor cable with high capacitive ground current](https://www.amazon.com/s?k=Long%20motor%20cable%20with%20high%20capacitive%20ground%20current&tag=errorcodefixe-20) | Medium |
| [Drive output IGBT failure (internal fault)](https://www.amazon.com/s?k=Drive%20output%20IGBT%20failure%20(internal%20fault)&tag=errorcodefixe-20) | Medium |
| [Incorrect fault 2330 trip (ground fault threshold too sensitive)](https://www.amazon.com/s?k=Incorrect%20fault%202330%20trip%20(ground%20fault%20threshold%20too%20sensitive)&tag=errorcodefixe-20) | Low |

## Step-by-Step Diagnosis {#diagnosis}

**Step 1 — Disconnect the motor cable from the drive**
- Power off the drive and wait for DC bus to discharge (minimum 5 minutes)
- Disconnect the motor cable at the U, V, W output terminals of the ACS355
- If Fault 2330 no longer appears on power-up: the fault is in the motor or cable

**Step 2 — Megger test the motor**
- Using a 500V or 1000V insulation resistance tester (megger):
- Measure insulation resistance from each motor phase terminal to the motor frame (ground)
- Acceptable minimum: 1 MΩ (IEC standard) — above 100 MΩ is ideal
- Below 1 MΩ: motor insulation is failed — motor requires rewinding or replacement
- Test with the motor cable disconnected from the motor to isolate the motor from the cable

**Step 3 — Megger test the motor cable**
- With both ends of the cable disconnected (from drive and motor):
- Measure insulation resistance conductor-to-ground on each conductor
- Below 1 MΩ: cable is damaged — replace

**Step 4 — Check for moisture**
- Inspect the motor terminal box for condensate, water infiltration, or corrosion
- Dry the terminal box with a heat gun
- Apply insulating spray if corrosion is present

**Step 5 — Check cable length and shielding**
- Long unshielded motor cables create capacitive ground currents that can falsely trip Fault 2330
- ACS355 applications: use shielded cable for runs over 30 meters
- Check ABB ACS355 parameter 1601 (Ground Fault) — if set to OFF, the fault indication may be from an internal fault

**Step 6 — Check drive output IGBTs**
- If Fault 2330 appears with the motor disconnected: the drive output stage may have failed
- Check for shorted IGBT by measuring resistance from each output terminal (U, V, W) to DC+ and DC-
- A failed IGBT shows very low resistance in both directions — requires drive repair or replacement

## Fault 2330 Reset

After identifying and fixing the fault:
1. Reconnect motor cable
2. Reset the ACS355 by pressing the STOP/RESET button or cycling power
3. Run a test at low speed first to confirm the fault has cleared

## Replacement Parts {#parts}

| Part | Notes |
|---|---|
| [Motor (rewound or replacement)](https://www.amazon.com/s?k=Motor%20(rewound%20or%20replacement)&tag=errorcodefixe-20) | Match HP, voltage, frame, and poles |
| [Motor cable (shielded)](https://www.amazon.com/s?k=Motor%20cable%20(shielded)&tag=errorcodefixe-20) | Use shielded 4-conductor cable for VFD applications |
| [ACS355 drive](https://www.amazon.com/s?k=ACS355%20drive&tag=errorcodefixe-20) | If output IGBT confirmed failed |

> **Pro tip:** The ABB ACS355 supports a ground fault trip sensitivity parameter. For long cable runs, check parameter 1601 and consult ABB application note AN-14-0046 for capacitive ground current calculations.
