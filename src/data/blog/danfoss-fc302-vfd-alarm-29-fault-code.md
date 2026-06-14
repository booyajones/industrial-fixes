---
title: "Danfoss FC302 VFD Alarm 29 - Causes & Fix"
description: "Alarm 29 means heatsink over-temperature. Most common fix: clean blocked air vents, replace failed cooling fans, or clear dust from fins."
pubDatetime: 2026-06-04T09:10:39Z
modDatetime: 2026-06-04T09:10:39Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss VLT FC 302 cooling fan assembly"
most_likely_cause: "Blocked or failed cooling fans"
---

## Danfoss FC302 VFD Alarm 29 — What It Means

Alarm 29 on a Danfoss VLT FC 302 means the drive has detected heatsink over-temperature. The heatsink temperature exceeded its safe operating limit, so the VFD trips to protect the power section, especially the IGBTs. Danfoss documents this as "Heat Sink temp" and describes the condition as "The maximum temperature of the heat sink is exceeded." The exact threshold temperature is model-dependent and not published for every frame size, but it is typically in the range of 90 to 95 degrees Celsius. The alarm will cause the drive to shut down and must be cleared after the root cause is corrected.

[Jump to Fix](#fix)

## Common Causes

- **Blocked or failed cooling fans** The most common cause is loss of cooling airflow due to failed fans, blocked intake or exhaust vents, or clogged heatsink fins.
- **Dust and debris buildup on heatsink** Accumulated dust on the heatsink fins reduces heat transfer and causes the drive to overheat even with fans running.
- **High ambient temperature or poor ventilation** Installation in a hot environment or enclosed cabinet without adequate ventilation can push the drive past its thermal limit.
- **Drive overloading or excessive duty cycle** Operating the drive at higher load or duty cycle than it was sized for generates excess heat and can trigger thermal shutdown.
- **Failed power card or fan control circuit** If fans receive no voltage or do not respond to commands, the power card or fan control circuit may be faulty.

## Step-by-Step Fix {#fix}

1. **Check the alarm history** in the drive's display or parameter menu to confirm Alarm 29 and review the heatsink temperature readout if available.
2. **Inspect all cooling fans** to verify they are spinning at startup and during operation, and listen for unusual noise indicating bearing failure.
3. **Clear all air vents and filters** on the drive enclosure and cabinet, removing any obstructions, dust, or debris blocking airflow.
4. **Clean the heatsink fins** with compressed air or a soft brush to remove dust buildup and restore heat dissipation.
5. **Measure the ambient temperature** around the drive and confirm it is within the FC 302's rated range for your frame size, and verify the drive has proper mounting clearance.
6. **Force fans to 100 percent** using the drive's parameter test function (if supported) to confirm fan operation, then measure voltage at the fan circuit if fans do not run.
7. **Replace the fan assembly** if voltage is present but the fan does not spin, or replace the power card if no voltage reaches the fan terminals.
8. **Reset the alarm** only after correcting the cause, then monitor heatsink temperature during a test run to confirm normal cooling.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss VLT FC 302 cooling fan assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-29-fault-code&k=Danfoss+VLT+FC+302+cooling+fan+assembly&tag=errorcodefixes-20) \| Match to your drive's frame size and voltage rating. |
| Danfoss VLT FC 302 power card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-29-fault-code&k=Danfoss+VLT+FC+302+power+card&tag=errorcodefixes-20) \| Required if fan voltage supply is absent and fan circuit is confirmed open. |

## When to Call a Pro

Call a qualified VFD technician or contact Danfoss technical support if the alarm persists after cleaning the heatsink, verifying fan operation, and confirming proper ventilation. Internal faults such as a failed power card, rectifier issues, or damage to the IGBT module require specialized diagnostics and replacement. If you are unable to measure fan voltage, interpret parameter settings, or safely work inside the drive enclosure while observing electrical safety lockout procedures, professional service is necessary. Do not attempt to bypass thermal protection or operate the drive with recurring over-temperature alarms, as this can cause permanent damage to the power section.

## See Also

- [Danfoss FC302 Alarm 55 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-55-fault-code/)
- [Danfoss FC302 Alarm AL 29 — Causes & Fix](/posts/danfoss-fc302-fault-al-29/)
- [Danfoss FC302 Alarm 25 - Causes & Fix](/posts/danfoss-fc302-alarm-25-fault-code/)
- [Danfoss FC302 Alarm 34 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-34-fault-code/)
