---
title: "Danfoss FC302 ALARM 24 - Causes & Fix"
description: "ALARM 24 on a Danfoss FC302 VFD means external fan fault. The drive detected the cooling fan stopped, is wired wrong, or airflow is blocked."
pubDatetime: 2026-06-04T09:08:55Z
modDatetime: 2026-06-04T09:08:55Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC 302 external cooling fan"
---

## Danfoss FC302 ALARM 24 — What It Means

ALARM 24 (or WARNING 24) on a Danfoss VLT AutomationDrive FC 302 indicates an external fan fault. The drive's fan-monitoring function has detected that the cooling fan is not running, not mounted correctly, or the fan-sense circuit is not reading properly. This is a protective alarm that prevents overheating damage to the drive's power components.

When fan monitoring is enabled, the drive expects feedback from the external fan circuit. If that feedback is missing or incorrect, ALARM 24 trips. In some installations the fan monitoring can be disabled via parameter 14-53, but disabling it does not fix a broken fan and leaves the drive without proper cooling protection.

[Jump to Fix](#fix)

## Common Causes

- **Blocked airflow around the drive** Dust, debris, or obstruction around the frequency converter or heat sink restricts cooling airflow and can cause the fan alarm to trip.
- **Failed or damaged heat sink fan** The external fan motor itself has seized, failed, or stopped spinning due to worn bearings or electrical failure.
- **Dirty heat sink** A clogged heat sink with accumulated dust or dirt restricts cooling and can overheat the drive, triggering the fan fault.
- **Fan not mounted or detected correctly** The fan is physically present but not mounted in the correct orientation, or the fan-sense circuit cannot detect it.
- **Loose or damaged fan wiring or connectors** The wiring or connectors for the external fan or fan-feedback circuit are loose, corroded, or broken, preventing the drive from sensing the fan.
- **Failed soft charge fuses or thermal sensor** Danfoss troubleshooting includes checking the soft charge fuses and IGBT thermal sensor when diagnosing fan-related alarms on the FC 302.

## Step-by-Step Fix {#fix}

1. **Verify the alarm code** on the drive display or event log to confirm it is ALARM 24 / external fan fault.
2. **Inspect airflow** around the drive and heat sink for obstructions, dust buildup, blocked vents, or any restriction to cooling airflow.
3. **Check the fan physically** by looking for rotation when the drive is powered, listening for unusual noise, and confirming the fan is mounted correctly and spins freely.
4. **Inspect fan wiring and connectors** for looseness, corrosion, or damage, especially if the fan is externally powered or uses a feedback signal to the drive.
5. **Check fan resistance** using a multimeter to test continuity and confirm the fan motor windings are intact, as recommended in Danfoss FC 302 troubleshooting instructions.
6. **Check the soft charge fuses** and IGBT thermal sensor if the fan checks out but the alarm persists, since Danfoss includes these components in the troubleshooting list for this alarm.
7. **Clear the alarm and test** after cleaning the heat sink, repairing wiring, or replacing the failed fan, and verify proper airflow and fan operation before returning the drive to full load.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC 302 external cooling fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-24-fault-code&k=Danfoss+FC+302+external+cooling+fan&tag=errorcodefixes-20) \| Replacement fan assembly for the heat sink, confirm your drive frame size and voltage. |
| Soft charge fuses for Danfoss FC 302 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-24-fault-code&k=Soft+charge+fuses+for+Danfoss+FC+302&tag=errorcodefixes-20) \| Check and replace if fuses test open during troubleshooting. |
| IGBT thermal sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-24-fault-code&k=IGBT+thermal+sensor&tag=errorcodefixes-20) \| Replace if the sensor circuit is implicated in continued fan or thermal faults. |

## When to Call a Pro

Call a qualified VFD technician or industrial electrician if you are not comfortable working with line-voltage drive electronics, if the fan and wiring check out but the alarm persists, or if you need to replace internal fuses or thermal sensors. A technician with Danfoss drive experience can safely diagnose fan-monitoring circuit issues, test the IGBT sensor, and make internal repairs. Also call a pro if the drive is part of a critical process system where downtime or incorrect repair could cause production loss or safety hazards.

## See Also

- [Danfoss FC302 Alarm 50 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-50-fault-code/)
- [Danfoss FC302 Alarm 22 - Hoist Brake Fault Fix](/posts/danfoss-fc302-vfd-alarm-22-fault-code/)
- [Danfoss FC302 VFD Alarm 28 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-28-fault-code/)
- [Danfoss FC302 Alarm 32 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-32-fault-code/)
