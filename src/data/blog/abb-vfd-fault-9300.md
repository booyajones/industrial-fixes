---
title: "ABB VFD Fault 9300 — Causes & Fix"
description: "What ABB VFD fault 9300 means, why the fan faults, and how to fix it step by step."
pubDatetime: 2026-04-22T12:00:00Z
modDatetime: 2026-04-22T12:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - abb
---

## ABB VFD Fault 9300 — What It Means

ABB fault 9300 is a **cooling fan fault** — the drive's internal cooling fan (which prevents the power electronics from overheating) has failed, is running too slowly, or its feedback signal is absent. ABB ACS drives in the ACS580, ACS880, and ACS850 series monitor the internal fan with a tachometer or current feedback; when the fan doesn't reach operating speed or the current signature is abnormal, fault 9300 is triggered. The drive may continue running briefly but will eventually thermal-trip if the cooling fan is not restored.

[Jump to Fix](#fix)

## Common Causes

- **Failed cooling fan** — Bearing wear or blade fouling causes the fan to stop or run slowly; this is the most common cause.
- **Fan power supply fault** — The 24VDC or 48VDC supply to the cooling fan fails; the fan has no power.
- **Fan feedback circuit failure** — The tach wire from the fan to the control board breaks or the feedback circuit on the board fails.
- **Dirty or blocked fan airflow path** — Accumulated dust on the fan blades or in the fan housing reduces RPM and airflow even if the motor is functional.

## Step-by-Step Fix {#fix}

1. **Lock out and inspect** — Apply LOTO. Open the drive enclosure and visually inspect the cooling fan. Look for accumulation of dust, debris, or damage to the fan blades.
2. **Clean the fan and heat sink** — Use compressed air to blow out the fan blades and the heat sink fins. Clogged heat sinks are a common cause of fan overload and subsequent fault 9300.
3. **Test fan power supply** — With the drive energized and the fault acknowledged, measure voltage at the fan connector. Expected voltage is typically labeled on the fan nameplate (commonly 24VDC or 48VDC). No voltage = power supply fault; trace to the internal PSU.
4. **Check fan feedback wire** — Locate the tach/feedback wire from the fan to the control board connector. Confirm it's firmly seated and the wire is unbroken.
5. **Replace the cooling fan** — ABB cooling fans are model- and frame-size-specific. Match the voltage, airflow (CFM), and connector type. Fan replacement is a standard maintenance item on ACS drives.
6. **Reset and confirm** — Acknowledge the fault (by default: toggle power or use the keypad), run the drive, and monitor thermal data in the parameter set to confirm temperatures are within range.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Internal cooling fan | [Amazon](https://www.amazon.com/s?k=Internal+cooling+fan&tag=errorcodefixes-20) \| ABB frame-size-specific; order by drive model number and frame size |
| Fan power supply (internal PSU) | [Amazon](https://www.amazon.com/s?k=Fan+power+supply+%28internal+PSU%29&tag=errorcodefixes-20) \| If fan supply voltage is absent |
## When to Call a Pro

If the fan is clean, supply voltage is present, and the fault persists, the control board's fan feedback input may be damaged. ABB drives can often be diagnosed remotely via the ABB DriveWindow or DDCS communication; contact ABB service or a certified integrator for advanced diagnostics.

## Related Articles

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS310 Fault 3130 — Causes & Fix](/posts/abb-acs310-fault-3130/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)
