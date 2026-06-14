---
title: "Schneider Altivar 61 OBF Fault — Causes & Fix"
description: "What Schneider Altivar 61 OBF fault means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T14:00:00Z
modDatetime: 2026-04-22T14:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - schneider
money_part: "Motor (if windings damaged)"
most_likely_cause: "Motor running at sustained overcurrent"
---

## Schneider Altivar 61 OBF Fault — What It Means

The OBF fault on the Schneider Electric Altivar 61 variable speed drive indicates motor overload — the drive's thermal protection model has detected that the motor current has exceeded the programmed overload threshold for long enough to risk motor damage. The Altivar 61 is widely used in pump and fan HVAC applications; OBF is the motor thermal trip, distinct from OCF (overcurrent trip).

[Jump to Fix](#fix)

## Common Causes

- **Motor running at sustained overcurrent** — A pump or fan with a heavy load running continuously near or above the motor FLA accumulates thermal count until OBF trips.
- **ItH (motor thermal current) parameter set too low** — If the motor thermal current parameter is set below the actual motor FLA, OBF trips prematurely under normal conditions.
- **High ambient temperature in motor environment** — Motors in hot spaces lose cooling effectiveness, drawing more current for the same torque output.
- **Cooling fan failure on the motor** — Forced-ventilated motors with a failed shaft fan overheat rapidly at full load, tripping OBF.

## Step-by-Step Fix {#fix}

1. **Check the motor thermal current parameter** — On the ATV61 keypad, navigate to [MOTOR CONTROL] → [ItH] and verify it matches the motor nameplate FLA. Adjust to correct value if wrong.
2. **Measure motor current** — Use the [MONITORING] menu to read output current during normal operation. Compare to motor nameplate FLA. Current at or above FLA during normal operation = mechanical overload or undersized motor.
3. **Inspect the load** — Check pump for cavitation, blockage, or worn impeller. Check fan for debris on blades or damaged housing causing resistance.
4. **Check motor cooling** — Confirm the motor ventilation path is clear and the cooling fan is running. Force-ventilated motors fail rapidly when cooling fails.
5. **Reset and monitor** — Navigate to [FAULT RESET] to reset OBF. Monitor ItH accumulation (available in monitoring menu) over the next run cycle.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor (if windings damaged) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-schneider-altivar-61-fault-obf&k=Motor+%28if+windings+damaged%29&tag=errorcodefixes-20) \| Test winding resistance and insulation before replacement |
| Motor cooling fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-schneider-altivar-61-fault-obf&k=Motor+cooling+fan&tag=errorcodefixes-20) \| Replace if not running on force-ventilated motor |
## When to Call a Pro

If OBF trips with correct parameters and no mechanical overload, the motor may be undersized for the application. Consult an Schneider application engineer for drive/motor sizing review.

## Related Articles

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS310 Fault 3130 — Causes & Fix](/posts/abb-acs310-fault-3130/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)
