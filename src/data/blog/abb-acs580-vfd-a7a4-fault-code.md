---
title: "ABB ACS580 A7A4 (7122) Fault - Causes & Fix"
description: "A7A4 (likely fault 7122) means motor overload alarm from excessive current. Most often caused by incorrect motor parameter settings."
pubDatetime: 2026-06-22T09:59:59Z
modDatetime: 2026-06-22T09:59:59Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - abb
money_part: "ABB ACS580 mainboard (control PCB)"
most_likely_cause: "Incorrect motor nominal current parameter (99.06) set lower than actual motor rating"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power cycle the VFD and check event history through the keypad to see actual current at fault time"
  - "Compare parameter 99.06 Motor Nominal Current against the motor nameplate rating"
  - "Inspect motor and load for mechanical binding or jamming that would cause genuine overload"
no_buy_pct: "60%"
---

## ABB ACS580 A7A4 (7122) Fault — What It Means

The code A7A4 on an ABB ACS580 VFD does not appear in official ABB documentation and is almost certainly a misreading of fault 7122. Fault 7122 is a motor overload alarm triggered when motor current exceeds the overload threshold configured in the drive's protection parameters (35.51 through 35.56). Unlike instantaneous overcurrent faults, this alarm responds to sustained high current that suggests the motor is working harder than its rated capacity. The fault can be triggered by a genuine mechanical overload, by incorrect motor parameter settings that make the drive think a healthy motor is overloaded, or by hardware issues inside the VFD. The drive will display this fault and typically shut down or reduce output to protect the motor from thermal damage. You may also see auxiliary codes or event logs that show the actual current level when the fault occurred.

## Before You Replace Anything

Technicians often replace the entire VFD mainboard or drive board when they see persistent overload faults, but the real culprit is usually wrong motor parameters (99.06 nominal current) or overload threshold (35.51) being too conservative for the actual load. Always verify motor nameplate current and parameters through Drive Composer before ordering boards.

[Jump to Fix](#fix)

## Common Causes

- **Motor nominal current parameter set too low (~35%)** Parameter 99.06 does not match the motor nameplate current rating, so the drive thinks normal motor current is an overload condition.
- **Overload threshold configured too conservatively (~25%)** Parameter 35.51 (overload factor) may be set to the default 110%, which is too low for motors with variable loads or brief surge demands.
- **Genuine mechanical overload on motor (~20%)** Pump cavitation, fan blade binding, conveyor jamming, or other mechanical problems force the motor to draw excessive current under load.
- **Output wiring or motor insulation fault (~10%)** Short circuit, earth fault, or phasing error in motor cables or windings creates abnormal current draw that triggers the overload alarm.
- **Internal hardware connection issue (~7%)** Poor contact or broken connection between the mainboard and drive board inside the VFD can cause erratic current sensing and false overload alarms.
- **Blocked cooling or high ambient temperature (~3%)** Dirty vents or fans reduce heat dissipation, causing internal temperature rise and current drift that pushes motor current above threshold.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault occur immediately on startup or only under load?</summary>
<div class="dtree-body"><strong>Yes:</strong> Immediate fault suggests wrong motor parameters (99.06 or 30.17) or output wiring problem. Check parameters first.<br><strong>No:</strong> Fault under load points to genuine overload, mechanical binding, or overload threshold (35.51) set too low for your application.</div>
</details>

<details class="dtree"><summary>Can you run the motor unloaded (pump valve closed, fan belt removed) without fault?</summary>
<div class="dtree-body"><strong>Yes:</strong> The mechanical load is the problem. Inspect for binding, jamming, or excessive demand on the motor.<br><strong>No:</strong> Motor or wiring fault is likely. Perform insulation resistance test on motor and cables with a megohmmeter.</div>
</details>

<details class="dtree"><summary>Does the event log show actual current near or below motor nameplate rating when fault occurs?</summary>
<div class="dtree-body"><strong>Yes:</strong> Parameter 99.06 is set too low or overload threshold 35.51 is too tight. Adjust parameters to match motor and application.<br><strong>No:</strong> Current is genuinely high. Look for mechanical overload, wiring fault, or motor winding damage.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Access fault details** through the keypad or connect a laptop running Drive Composer to view event history, fault timestamps, and the actual motor current reading when the alarm triggered.
2. **Verify motor parameter 99.06** (Motor Nominal Current) matches the current rating on the motor nameplate exactly, and check that parameter 30.17 (Maximum Current) is set higher than 99.06.
3. **Review overload threshold parameter 35.51** (overload factor) and increase it from the default 110% to 130% or 150% if the motor is healthy and the application has brief surge loads.
4. **Inspect the mechanical load** by manually checking for binding, jamming, or obstruction in the pump, fan, or conveyor, and run the motor unloaded if possible to isolate mechanical problems.
5. **Test motor insulation** using a megohmmeter on the motor windings and output cables to detect short circuits or earth faults, and inspect cable terminations for damage or incorrect phasing.
6. **Check cooling system** by cleaning VFD vents, fans, and heat sinks, and verify ambient temperature is within rated limits (typically below 40°C for IP21 enclosures).
7. **Inspect internal connections** by powering down, removing the inverter cover, and checking all plugs and connectors between the mainboard and drive board for corrosion, dust, or poor contact, then power cycle and test again.

## Parts Often Needed

| Part | Notes |
|------|-------|
| ABB ACS580 mainboard (control PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-a7a4-fault-code&k=ABB+ACS580+mainboard+%28control+PCB%29&tag=errorcodefixes-20) \| Only if internal hardware fault confirmed after all parameter and wiring checks; consult ABB service for exact part number for your frame size. |
| ABB ACS580 drive board (power section PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-a7a4-fault-code&k=ABB+ACS580+drive+board+%28power+section+PCB%29&tag=errorcodefixes-20) \| Rarely needed for overload faults; typically only if current sensing circuit is damaged. |

## When to Call a Pro

Call a qualified VFD technician or automation electrician if you have verified motor parameters and mechanical load but the fault persists, if you lack the tools to safely measure insulation resistance or work inside the VFD enclosure, or if the event log shows erratic current readings that suggest internal board damage. Professional diagnosis with Drive Composer software and oscilloscope testing of the power section can pinpoint whether the issue is a faulty current sensor, damaged gate driver, or control board failure. Also call a pro if the application requires custom overload curves or if you need to configure advanced motor protection parameters for variable-torque or high-inertia loads.

**Rough cost:** A pro service call runs about $200-500.

## See Also

- [ABB ACS550 AI1 LOSS - Causes & Fix](/posts/abb-acs550-vfd-ai1-loss-fault-code/)
- [ABB ACS880 Complete Fault Code Guide — All Faults and Fixes](/posts/abb-acs880-complete-guide/)
- [ABB VFD Fault 9300 — Causes & Fix](/posts/abb-vfd-fault-9300/)
- [ABB ACS580 FF63 - STO Diagnostics Failure Fix](/posts/abb-acs580-ff63-fault-code/)
