---
title: "Schneider Altivar Fault OBF — Causes & Fix"
description: "What Schneider Altivar OBF fault means, why motor overload trips the drive, and how to fix it."
pubDatetime: 2026-04-22T10:00:00Z
modDatetime: 2026-04-22T10:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - schneider
money_part: "Replacement motor"
most_likely_cause: "Mechanical overload on the driven equipment"
---

## Schneider Altivar Fault OBF — What It Means

OBF (Motor Overload Fault) on a Schneider Altivar drive (ATV12, ATV320, ATV630) is a thermal protection fault. The drive's electronic motor thermal model calculated that the motor has been running above its rated current long enough to accumulate dangerous heat in the windings. OBF is a time-integrated calculation — a small overload over a long period trips OBF just as surely as a larger overload over a shorter time. The drive shuts down to prevent motor winding insulation failure.

[Jump to Fix](#fix)

## Common Causes

- **Mechanical overload on the driven equipment** — A fan or pump running against excess system resistance, a conveyor with a heavy load, or a compressor with high discharge pressure causes the motor to draw more current than its rating.
- **Motor parameters not set correctly in the drive** — If the motor rated current (parameter ItH on ATV) is set higher than the motor's nameplate current, the thermal model will not protect the motor and OBF trips are delayed until the model finally catches up.
- **High ambient temperature** — At elevated ambient temperatures, the motor's thermal capacity is reduced. The thermal model in many Altivar drives does not account for ambient temperature — derate the motor accordingly.
- **Motor single-phasing** — If one phase of the motor is drawing much more current than the others (due to a winding fault or loose connection), the thermal model accumulates heat faster than the nameplate suggests.

## Step-by-Step Fix {#fix}

1. **Check motor current vs. rated** — Monitor the Altivar output current (parameter LCR or via display) under full load conditions. Compare to the motor nameplate full-load amps (FLA). If current is above nameplate FLA, there is a mechanical overload or motor issue.
2. **Verify motor rated current setting** — Access parameter ItH (motor thermal current) or the motor nameplate current parameter in the Altivar. This must match the motor nameplate exactly — not the drive's rated output current.
3. **Reduce mechanical load** — Check the driven equipment. Pumps: verify discharge pressure is within design range. Fans: check for blocked filters or dampers in the closed position. Conveyors: reduce belt tension or payload if excessive.
4. **Check for single-phasing** — Use a clamp meter to measure current on all three output phases simultaneously. Imbalance greater than 10% indicates a motor winding problem or output connection issue.
5. **Allow motor to cool before restart** — OBF requires the thermal model to cool down before the drive will restart. Wait 10–30 minutes. On some ATV drives, the display shows the motor thermal state (0–100%) — wait until it drops below 80% before restarting.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Replacement motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-schneider-altivar-fault-obf&k=Replacement+motor&tag=errorcodefixes-20) \| If windings are confirmed overheated (insulation resistance test) |
| System components (impeller, filter) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-schneider-altivar-fault-obf&k=System+components+%28impeller%2C+filter%29&tag=errorcodefixes-20) \| If overload is caused by blocked system elements |
## When to Call a Pro

If OBF trips persist with the motor drawing current at or below nameplate FLA, the Altivar thermal model parameters need to be reviewed and configured by a Schneider-authorized technician to match the motor's thermal class and duty cycle.

## Related Articles

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS310 Fault 3130 — Causes & Fix](/posts/abb-acs310-fault-3130/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)
