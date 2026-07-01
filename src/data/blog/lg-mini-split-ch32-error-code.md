---
title: "LG Mini Split CH32 Error Code - Causes & Fix"
description: "CH32 means compressor 1 discharge temperature is too high. Most often caused by low refrigerant or a leak. Check charge and sensor first."
pubDatetime: 2026-05-31T00:53:56Z
modDatetime: 2026-05-31T00:53:56Z
author: "Dana Kowalski"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - lg
money_part: "Discharge temperature sensor for LG outdoor unit"
most_likely_cause: "Insufficient refrigerant charge or active leak"
---

## LG Mini Split CH32 Error Code — What It Means

The CH32 code on an LG mini split or Multi V inverter outdoor unit means the discharge temperature of compressor 1 has exceeded safe operating limits. This is a protection event triggered when the outdoor compressor discharge line gets too hot. According to LG's own troubleshooting guidance, the primary cause is insufficient refrigerant or refrigerant leakage in the system. The code can also appear if the discharge temperature sensor has failed, is out of position, or is giving incorrect readings to the outdoor control board.

[Jump to Fix](#fix)

## Common Causes

- **Insufficient refrigerant charge or active leak** Low refrigerant from undercharge or leakage at brazed joints, flare connections, or damaged piping is the most common cause identified by LG.
- **Discharge temperature sensor failure or misposition** The sensor may be physically out of place, internally failed, or delivering incorrect resistance readings to the outdoor PCB.
- **Leaking or deformed refrigerant piping** Cracks, deformation, or loose connections in the outdoor discharge line or other piping can allow refrigerant loss and trigger overheat.
- **Faulty outdoor PCB sensor circuit** The outdoor control board may not be supplying the correct 5 V DC to the discharge sensor or may have a damaged sensor input.
- **Restricted outdoor heat rejection** Blocked coils, fan failure, or other outdoor-unit airflow problems can indirectly contribute to elevated discharge temperatures.

## Step-by-Step Fix {#fix}

1. {'lead': 'Access diagnostic data using LGMV or other LG monitoring tools', 'text': 'to view live refrigerant data, operating temperatures, and compressor status before opening the system.'}
2. {'lead': 'Inspect all refrigerant piping and connections for leaks', 'text': 'using leak detector or soap solution, focusing on brazed joints, flare fittings, bends, and any visible deformation or damage on the outdoor discharge line.'}
3. {'lead': 'Verify discharge temperature sensor position and mounting', 'text': 'on the outdoor unit to confirm the sensor is properly installed in the correct location on the compressor discharge line.'}
4. {'lead': 'Measure discharge sensor resistance at the outdoor PCB harness connection', 'text': 'and compare to specification; LG flags the fault if resistance is greater than 5 MΩ or less than 2 kΩ.'}
5. {'lead': 'Check sensor supply voltage at the outdoor PCB', 'text': 'which should read 5 V DC on the discharge temperature sensor circuit.'}
6. {'lead': 'Replace the discharge temperature sensor if resistance, voltage, or physical checks fail', 'text': 'and verify the new sensor reads correctly under operating conditions.'}
7. {'lead': 'Repair any refrigerant leak found, evacuate the system, and recharge to specification', 'text': 'then monitor discharge temperature and confirm the CH32 code clears and does not return.'}

## Parts Often Needed

| Part | Notes |
|------|-------|
| Discharge temperature sensor for LG outdoor unit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-mini-split-ch32-error-code&k=Discharge+temperature+sensor+for+LG+outdoor+unit&tag=errorcodefixes-20) \| Required if sensor resistance is out of range or sensor is physically damaged or mispositioned. |
| LG outdoor unit PCB (external control board) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-mini-split-ch32-error-code&k=LG+outdoor+unit+PCB+%28external+control+board%29&tag=errorcodefixes-20) \| Replace if 5 V sensor supply is missing or board sensor input circuit is faulty. |
| Refrigerant piping, flare nuts, or brazed joints | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-mini-split-ch32-error-code&k=Refrigerant+piping%2C+flare+nuts%2C+or+brazed+joints&tag=errorcodefixes-20) \| Order or fabricate replacement sections only if a leak is confirmed and cannot be re-brazed or re-sealed. |

## When to Call a Pro

CH32 faults require refrigerant system diagnostics, electronic sensor testing, and potentially brazing or vacuum work that are beyond typical homeowner tools and EPA certification. If you do not have LG diagnostic software, a manifold gauge set, a leak detector, and recovery equipment, call a licensed HVAC technician. Any repair involving refrigerant recovery, evacuation, or recharge must be performed by an EPA 608-certified technician. If the code persists after sensor and refrigerant checks, the outdoor PCB or compressor assembly may need replacement, which also requires professional evaluation and part sourcing from LG.

## See Also

- [LG Dishwasher HE Error Code - Causes & Fix](/posts/lg-dishwasher-he-error-code/)
- [LG Dryer E13 Error Code - Causes & Fix](/posts/lg-dryer-e13-error-code/)
- [LG Refrigerator Water Dispenser Not Working - Causes & Fix](/posts/lg-refrigerator-water-dispenser-not-working/)
- [LG Range F8 Error Code - Causes & Fix](/posts/lg-range-f8-error-code/)
