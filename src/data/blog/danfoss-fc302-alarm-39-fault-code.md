---
title: "Danfoss FC302 Alarm 39 - Causes & Fix"
description: "Danfoss FC302 Alarm 39 means heatsink sensor fault. Learn the common causes (power card, gate drive, ribbon cable) and repair steps."
pubDatetime: 2026-05-30T12:21:12Z
modDatetime: 2026-05-30T12:21:12Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - danfoss
---

## Danfoss FC302 Alarm 39 — What It Means

Alarm 39 on the Danfoss VLT AutomationDrive FC 302 indicates a heatsink sensor fault. The drive is not receiving feedback from the IGBT thermal sensor. Danfoss states that the thermal sensor signal is not available on the power card, which means the fault is in the temperature sensing circuit.

The fault path involves the power card, the gate drive card, or the ribbon cable connecting those two boards. In some cases the alarm can also be triggered by a real overtemperature condition that damages the sensor circuit, such as clogged filters, blocked airflow, or a failed heatsink fan.

[Jump to Fix](#fix)

## Common Causes

- **Defective power card** The power card where the IGBT thermal sensor signal terminates has failed and cannot process the temperature feedback.
- **Defective gate drive card** The gate drive card that interfaces with the power card has failed, interrupting the sensor signal path.
- **Loose or damaged ribbon cable** The ribbon cable between the power card and gate drive card is not seated properly or has physical damage that breaks the sensor circuit.
- **Blocked airflow or clogged filters** Restricted cooling airflow causes actual overheating that can damage the sensor circuit or trigger the alarm alongside the real thermal condition.
- **Failed heatsink fan** The heatsink cooling fan has stopped, leading to high temperatures that affect the sensor or its wiring on the power card.
- **Dirty heatsink or high ambient temperature** A fouled heatsink or ambient temperature outside specification can cause the sensor to read too hot or fail outright.

## Step-by-Step Fix {#fix}

1. Power down the drive completely and follow lockout/tagout procedures before opening the enclosure.
2. Inspect cooling conditions by checking that ambient temperature is within the drive's rated range, filters are clean, and airflow paths around the heatsink are unobstructed.
3. Check heatsink fan operation by verifying the fan spins freely and runs when the drive is powered (if safe to observe), and clean any dust or debris from the heatsink fins.
4. Inspect the ribbon cable between the power card and gate drive card by removing and reseating both ends, looking for bent pins, cracks, or contamination on the connector.
5. Test or replace the power card if cooling and cabling are confirmed good, since Danfoss indicates the sensor signal is not available on the power card in most Alarm 39 cases.
6. Test or replace the gate drive card if the power card and ribbon cable have been ruled out, as it is the other interface point in the sensor signal path.
7. Clear the alarm and run the drive under load to confirm that Alarm 39 does not return and that heatsink temperature readings appear normal in the drive's diagnostics menu.

## Parts Often Needed

| Part | Notes |
|------|-------|
| FC 302 power card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-39-fault-code&k=FC+302+power+card&tag=errorcodefixes-20) \| Replace if the IGBT thermal sensor signal is not available and the ribbon cable is intact. |
| FC 302 gate drive card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-39-fault-code&k=FC+302+gate+drive+card&tag=errorcodefixes-20) \| Replace if the power card tests good but the sensor circuit remains open. |
| Power card to gate drive ribbon cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-39-fault-code&k=Power+card+to+gate+drive+ribbon+cable&tag=errorcodefixes-20) \| Replace if the cable shows physical damage, bent pins, or does not seat firmly at both ends. |
| Heatsink cooling fan (FC 302 frame size matched) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-39-fault-code&k=Heatsink+cooling+fan+%28FC+302+frame+size+matched%29&tag=errorcodefixes-20) \| Replace if the fan does not spin or if cooling is inadequate and contributing to sensor failure. |

## When to Call a Pro

Call a qualified Danfoss service technician or drive specialist if you are not comfortable working inside energized industrial equipment or if you lack lockout/tagout procedures for your facility. If you have replaced the ribbon cable and cleaned the cooling system but Alarm 39 persists, the fault is on the power card or gate drive card, both of which require board-level diagnosis and proper ESD handling. A technician with Danfoss-specific training can also interrogate the drive's internal diagnostics to confirm which board is at fault and can source the correct revision of power or gate drive card for your drive's serial number and firmware version.

## See Also

- [Danfoss FC302 Alarm 17 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-17-fault-code/)
- [Danfoss VLT Alarm 14 - Earth Fault: What It Means and How to Fix It](/posts/danfoss-vlt-alarm-14/)
- [Danfoss VFD Fault UL — Causes & Fix](/posts/danfoss-vfd-fault-ul/)
- [Danfoss FC302 ALARM 26 - Causes & Fix](/posts/danfoss-fc302-alarm-26-fault-code/)
