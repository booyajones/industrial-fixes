---
title: "Vertiv (Liebert) UPS Fault Codes - Complete Guide"
description: "Vertiv Liebert UPS fault codes for GXT, EXS, APM, and 3-phase systems: alarms, causes, and repair guidance."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vertiv
  - liebert
  - ups
  - power-systems
---

## Vertiv (Liebert) UPS Fault Codes - Quick Reference

Vertiv (formerly Liebert, now Vertiv brand) UPS systems include GXT4/5, EXS, APS, APM, NXL, and Trinergy lines. Faults display on the local LCD and are logged via Vertiv Environet or Liebert IntelliSlot network cards.

| Fault | System | Meaning | Quick Fix |
|-------|--------|---------|-----------|
| Battery Fault | All | Battery string failure | Replace battery module |
| Overload | All | Load exceeds UPS capacity | Reduce load |
| On Battery | All | Utility power loss | Check input |
| Replace Battery | GXT/APS | Battery end of life | Replace battery |
| Static Bypass | All | UPS transferred to bypass | Check for internal fault |
| Fan Failure | APM/NXL | Cooling fan failed | Replace fan module |
| Overtemperature | All | Thermal limit exceeded | Check cooling |
| Rectifier Fault | NXL/APM | Rectifier failure | Contact service |
| Inverter Fault | All | Inverter failure | Transfer to bypass, contact service |
| Communication Fault | All | Network card offline | Check IntelliSlot card |

## Most Common Faults

### Battery Fault
Vertiv Liebert GXT and EXS systems monitor battery voltage and impedance. A battery fault on GXT4/5 means one or more batteries in the internal string have failed. Replace the complete battery set - Vertiv recommends replacing all batteries at once, not individual cells. Use Vertiv-approved replacement batteries for warranty compliance.

### Overtemperature
Vertiv UPS systems require adequate airflow. GXT rack-mount units need 1U of clearance above and below. APM and NXL systems have dedicated cooling sections - check that front air intakes are clear and rear exhausts are not blocked by adjacent equipment.

### Inverter Fault
An inverter fault on a Vertiv system causes automatic transfer to static bypass. The load remains powered but unprotected. Contact Vertiv service - inverter module replacement on APM and NXL systems is a field-replaceable procedure but requires factory-trained personnel.

### Fan Failure
Vertiv APM and NXL modular systems have hot-swappable fan modules. Check the Vertiv part number on the fan tray label. Fan failures in these systems generate a critical alarm and should be addressed immediately - insufficient cooling leads to rapid component degradation.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Battery module (GXT/EXS) | [Amazon](https://www.amazon.com/s?i=industrial&k=Battery+module+%28GXT%2FEXS%29&tag=errorcodefixes-20) \| Replace complete set |
| Fan module (APM/NXL) | [Amazon](https://www.amazon.com/s?i=industrial&k=Fan+module+%28APM%2FNXL%29&tag=errorcodefixes-20) \| Hot-swappable |
| IntelliSlot network card | [Amazon](https://www.amazon.com/s?i=industrial&k=IntelliSlot+network+card&tag=errorcodefixes-20) \| Replace on communication fault |
| Bypass module (APM) | [Amazon](https://www.amazon.com/s?i=industrial&k=Bypass+module+%28APM%29&tag=errorcodefixes-20) \| Replace on bypass fault |
| Rectifier module | [Amazon](https://www.amazon.com/s?i=industrial&k=Rectifier+module&tag=errorcodefixes-20) \| Factory service or replacement |
## When to Call a Pro
Vertiv APM, NXL, and Trinergy three-phase systems require Vertiv-authorized service for inverter, rectifier, and capacitor maintenance. Annual preventive maintenance by a Vertiv service partner is recommended for critical infrastructure installations.

