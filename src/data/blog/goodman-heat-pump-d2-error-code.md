---
title: "Goodman D2 Error Code - Causes & Fix"
description: "D2 means required airflow exceeds indoor unit capacity during system test. Most often fixed by reducing airflow trim settings in commissioning."
pubDatetime: 2026-05-31T09:09:25Z
modDatetime: 2026-05-31T09:09:25Z
author: "Dana Kowalski"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - goodman
money_part: "Indoor blower motor assembly"
---

## Goodman D2 Error Code — What It Means

On Goodman side-discharge inverter heat pumps (and related Amana/Daikin family equipment), the D2 code appears during system test or commissioning when the required airflow is greater than the indoor unit's capability. The system is being asked to deliver more airflow than the indoor air handler configuration allows. This is not a standard universal code across all Goodman models, so check your exact model number and service literature. The fault is usually a configuration mismatch rather than a failed component.

The system test detects that the indoor side cannot move enough air for the selected outdoor unit or installed setup. This typically happens after equipment replacement, partial system changes, or when commissioning trim settings are too high for the indoor blower's capacity.

[Jump to Fix](#fix)

## Common Causes

- **Equipment mismatch between outdoor and indoor units** The outdoor heat pump capacity exceeds what the indoor air handler can support, especially after replacement or partial system upgrades.
- **Airflow trim settings too high in commissioning menu** Cool or heat airflow trim values push demand beyond the indoor unit's allowed range during system test.
- **Incorrect airflow settings for cool or heat operation** Commissioning parameters do not match the actual installed equipment combination or duct configuration.
- **Duct restrictions or undersized ductwork** High static pressure or restricted airflow paths reduce the available airflow margin and can contribute to failing the system test check.
- **Blower motor or control board limiting indoor airflow** Failing blower assembly or air handler control board cannot deliver the airflow demanded by the outdoor unit configuration.

## Step-by-Step Fix {#fix}

1. **Confirm the exact model numbers** of both the outdoor heat pump and indoor air handler and verify the combination is a manufacturer-approved match using the HRI or matched-system data tables.
2. **Enter the system test or commissioning menu** using the service access procedure for your model and inspect the current airflow trim settings for cool and heat modes.
3. **Reduce the airflow trim settings** by 10% increments for both cool and heat, then rerun the system test to see if the D2 code clears.
4. **Rerun the system test** after each trim adjustment and watch for the D2 fault to disappear, confirming the indoor unit can now meet the airflow requirement.
5. **Check for duct restrictions** by measuring static pressure at the air handler and inspecting supply and return ducts for blockages, undersized runs, or excessive length.
6. **Inspect the indoor blower assembly** for dust buildup, belt condition (if belt-drive), or motor bearing noise that could limit airflow capacity.
7. **Verify matched-system sizing** if D2 persists after trim corrections, as the outdoor unit may be oversized for the indoor air handler and require equipment replacement or reconfiguration.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Indoor blower motor assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-goodman-heat-pump-d2-error-code&k=Indoor+blower+motor+assembly&tag=errorcodefixes-20) \| Only if blower cannot deliver rated airflow after correct commissioning and duct checks. |
| Air handler control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-goodman-heat-pump-d2-error-code&k=Air+handler+control+board&tag=errorcodefixes-20) \| Replace if blower control outputs are faulty and airflow trim adjustments have no effect. |

## When to Call a Pro

Call a licensed HVAC technician immediately for D2 faults. This code requires access to the commissioning menu, manufacturer matched-system data, and static pressure measurement tools that homeowners do not typically have. Incorrect trim settings or mismatched equipment can damage the compressor or void warranties. A technician will verify the indoor and outdoor units are correctly paired, adjust airflow parameters to match the installed system, and measure static pressure to rule out duct problems. If the equipment is mismatched, the technician can recommend the correct indoor unit or outdoor unit replacement to achieve a stable, efficient system.

## See Also

- [Amana / Goodman Furnace 3 Flash Error Code — Causes & Fix](/posts/goodman-amana-furnace-3-flash/)
- [Goodman GMSS96 Furnace Error Codes — Flash Code Diagnostic Guide](/posts/goodman-gmss96-error-codes/)
- [Goodman E8 Error Code - Causes & Fix](/posts/goodman-heat-pump-e8-error-code/)
- [Goodman Heat Pump E2 Error Code - Causes & Fix](/posts/goodman-heat-pump-e2-error-code/)
