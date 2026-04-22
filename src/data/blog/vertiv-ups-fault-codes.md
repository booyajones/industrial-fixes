---
title: "Vertiv (Liebert) UPS Fault Codes - Complete Guide"
description: "Vertiv Liebert UPS fault codes for GXT, EXS, APM, and 3-phase systems: alarms, causes, and repair guidance."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "ErrorCodeFixes"
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

| [Fault](https://www.amazon.com/s?k=Fault&tag=errorcodefixe-20) | System | Meaning | [Quick Fix](https://www.amazon.com/s?k=Quick%20Fix&tag=errorcodefixe-20) |  |-------|--------|---------|-----------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Battery Fault | All | [Battery string failure](https://www.amazon.com/s?k=Battery%20string%20failure&tag=errorcodefixe-20) | Replace battery module |
| [Overload](https://www.amazon.com/s?k=Overload&tag=errorcodefixe-20) | All | Load exceeds UPS capacity | [Reduce load](https://www.amazon.com/s?k=Reduce%20load&tag=errorcodefixe-20) |  | On Battery | [All](https://www.amazon.com/s?k=All&tag=errorcodefixe-20) | Utility power loss | Check input | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Replace Battery | GXT/APS | [Battery end of life](https://www.amazon.com/s?k=Battery%20end%20of%20life&tag=errorcodefixe-20) | Replace battery |
| [Static Bypass](https://www.amazon.com/s?k=Static%20Bypass&tag=errorcodefixe-20) | All | UPS transferred to bypass | [Check for internal fault](https://www.amazon.com/s?k=Check%20for%20internal%20fault&tag=errorcodefixe-20) |  | Fan Failure | [APM/NXL](https://www.amazon.com/s?k=APM%2FNXL&tag=errorcodefixe-20) | Cooling fan failed | Replace fan module | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Overtemperature | All | [Thermal limit exceeded](https://www.amazon.com/s?k=Thermal%20limit%20exceeded&tag=errorcodefixe-20) | Check cooling |
| [Rectifier Fault](https://www.amazon.com/s?k=Rectifier%20Fault&tag=errorcodefixe-20) | NXL/APM | Rectifier failure | [Contact service](https://www.amazon.com/s?k=Contact%20service&tag=errorcodefixe-20) |  | Inverter Fault | [All](https://www.amazon.com/s?k=All&tag=errorcodefixe-20) | Inverter failure | Transfer to bypass, contact service | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Communication Fault | All | [Network card offline](https://www.amazon.com/s?k=Network%20card%20offline&tag=errorcodefixe-20) | Check IntelliSlot card |

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
| [Battery module (GXT/EXS)](https://www.amazon.com/s?k=Battery%20module%20(GXT%2FEXS)&tag=errorcodefixe-20) | Replace complete set |
| [Fan module (APM/NXL)](https://www.amazon.com/s?k=Fan%20module%20(APM%2FNXL)&tag=errorcodefixe-20) | Hot-swappable |
| [IntelliSlot network card](https://www.amazon.com/s?k=IntelliSlot%20network%20card&tag=errorcodefixe-20) | Replace on communication fault |
| [Bypass module (APM)](https://www.amazon.com/s?k=Bypass%20module%20(APM)&tag=errorcodefixe-20) | Replace on bypass fault |
| [Rectifier module](https://www.amazon.com/s?k=Rectifier%20module&tag=errorcodefixe-20) | Factory service or replacement |

## When to Call a Pro
Vertiv APM, NXL, and Trinergy three-phase systems require Vertiv-authorized service for inverter, rectifier, and capacitor maintenance. Annual preventive maintenance by a Vertiv service partner is recommended for critical infrastructure installations.

