---
title: "ABB ACS355 Fault 2330 — Ground Fault"
description: "ABB ACS355 drive Fault 2330 means a ground fault has been detected on the output. Learn causes, diagnostic steps, and how to clear this VFD fault."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "Dana Kowalski"
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

| Cause | Likelihood |
|---|---|
| Failed motor winding insulation (aged motor) | High |
| Damaged output cable (chafed or pinched) | High |
| Moisture in motor terminal box | High |
| Long motor cable with high capacitive ground current | Medium |
| Drive output IGBT failure (internal fault) | Medium |
| Incorrect fault 2330 trip (ground fault threshold too sensitive) | Low |

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
| Motor (rewound or replacement) | [Amazon](https://www.amazon.com/s?k=Motor+%28rewound+or+replacement%29&tag=errorcodefixes-20) \| Match HP, voltage, frame, and poles |
| Motor cable (shielded) | [Amazon](https://www.amazon.com/s?k=Motor+cable+%28shielded%29&tag=errorcodefixes-20) \| Use shielded 4-conductor cable for VFD applications |
| ACS355 drive | [Amazon](https://www.amazon.com/s?k=ACS355+drive&tag=errorcodefixes-20) \| If output IGBT confirmed failed |
> **Pro tip:** The ABB ACS355 supports a ground fault trip sensitivity parameter. For long cable runs, check parameter 1601 and consult ABB application note AN-14-0046 for capacitive ground current calculations.

## Related Articles

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS310 Fault 3130 — Causes & Fix](/posts/abb-acs310-fault-3130/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)
- [ABB ACS550 AF10 Fault — Causes & Fix](/posts/abb-acs550-af10-heatsink/)
