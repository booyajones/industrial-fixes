---
title: "Bosch xF1 Error Code - Causes & Fix"
description: "xF1 on Bosch heat pumps means DC bus voltage error (industrial) or high-pressure fault (residential). Check airflow and pressure switch first."
pubDatetime: 2026-05-31T09:15:48Z
modDatetime: 2026-05-31T09:15:48Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - hvac
  - mini-split
  - bosch
---

## Bosch xF1 Error Code — What It Means

The xF1 error code on Bosch heat pump systems has different meanings depending on your model family. On Bosch industrial air-to-air heat pumps, xF1 indicates a DC bus voltage error at the outdoor inverter or compressor drive. On Bosch residential IDS/IDP heat pump models, the related P1/F1 fault points to high-pressure protection in heating mode or an open high-pressure switch.

Because Bosch uses the same fault label across different product lines with different definitions, you must identify your exact model platform before diagnosing. Industrial units require inverter power-section troubleshooting, while residential IDS/IDP units typically trip this code due to restricted refrigerant flow or airflow problems that cause system pressure to climb above safe limits.

[Jump to Fix](#fix)

## Common Causes

- **Restricted refrigerant flow or circuit blockage** A clog in the refrigerant piping, filter-drier, or expansion device forces pressure to spike and triggers the high-pressure fault on residential models.
- **Outdoor airflow restriction in cooling** A blocked condenser coil, failed condenser fan, or obstructed outdoor unit prevents heat rejection and raises discharge pressure.
- **Indoor airflow restriction in heating** A dirty indoor coil, clogged air filter, or reduced blower speed limits heat absorption and drives liquid-line pressure up in heating mode.
- **Failed high-pressure switch** The high-pressure safety switch may open prematurely or show high resistance even when system pressures are normal.
- **Unit left in force mode** Operating the system in forced-run or test mode bypasses normal control logic and can produce false high-pressure faults.
- **DC bus voltage fault on industrial models** On industrial air-to-air units the xF1 code signals a power-section or inverter problem rather than a refrigerant-pressure issue.

## Step-by-Step Fix {#fix}

1. **Verify your model platform** by checking the unit label and service manual, because Bosch uses xF1 for DC bus voltage errors on industrial systems and P1/F1 for high-pressure faults on residential IDS/IDP models.
2. **Exit force mode** if the unit is in a test or forced-run setting, since this can trigger false pressure faults during normal operation.
3. **Check refrigerant pressures** using manifold gauges, looking for approximately 130 psi on the suction line in cooling and approximately 357 psi on the liquid line in heating as general reference points for IDS/IDP systems.
4. **Test the high-pressure switch** by locating the yellow Molex connector labeled CN1 on the control board, unplugging it, and measuring resistance across the two yellow wires with a multimeter set to ohms; replace the switch if resistance is 1 ohm or greater.
5. **Inspect airflow paths** by verifying condenser fan operation and checking for debris on the outdoor coil in cooling mode, or confirming indoor blower speed and replacing the air filter in heating mode.
6. **Look for refrigerant restrictions** by examining the filter-drier, expansion valve, and service ports for ice formation or blockage if pressures remain abnormal after confirming airflow is adequate.
7. **Consult model-specific service documentation** for DC bus voltage troubleshooting on industrial units, since the manufacturer does not publish step-by-step inverter diagnostic flows in the general error-code table.

## Parts Often Needed

| Part | Notes |
|------|-------|
| High-Pressure Switch | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-bosch-heat-pump-xf1-error-code&k=High-Pressure+Switch&tag=errorcodefixes-20) \| Yellow-wire Molex connector; replace if resistance measures 1 ohm or higher during continuity test. |
| Condenser Fan Motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-bosch-heat-pump-xf1-error-code&k=Condenser+Fan+Motor&tag=errorcodefixes-20) \| Outdoor fan assembly; needed if fan fails to run or runs slowly during cooling operation. |
| Air Filter | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-bosch-heat-pump-xf1-error-code&k=Air+Filter&tag=errorcodefixes-20) \| Match your model's size; replace if clogged or dirty to restore indoor airflow in heating mode. |

## When to Call a Pro

Call a licensed HVAC technician if you have an industrial Bosch heat pump showing xF1, because inverter and DC bus diagnostics require specialized meters and model-specific voltage thresholds not published in general service materials. On residential IDS/IDP systems, call for help if refrigerant pressures are far outside the approximate reference ranges (130 psi suction in cooling, 357 psi liquid in heating), if you find ice on refrigerant lines suggesting a deeper restriction, or if the high-pressure switch tests good but the fault returns immediately after reset. Professional gauges, refrigerant handling certification, and access to Bosch's full wiring diagrams are necessary to trace intermittent pressure faults and inverter power issues safely.
