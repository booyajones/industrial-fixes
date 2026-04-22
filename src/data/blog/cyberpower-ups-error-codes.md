---
title: "CyberPower UPS Error Codes — Complete Guide"
description: "CyberPower UPS error codes and fault indicators for OL, PR, and Smart App series: LED alerts, beep codes, causes, and fixes."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - cyberpower
  - ups
  - power-systems
---

## CyberPower UPS Error Codes — Quick Reference

CyberPower UPS systems (OL series online, PR series, Smart App series, and CP series) communicate faults via LED indicators, LCD displays, and CyberPower PowerPanel software.

| Fault / LED | Series | Meaning | Quick Fix |
|------------|--------|---------|-----------|
| On Battery LED | All | Utility power lost | Check power input |
| Overload LED | All | Load exceeds UPS capacity | Reduce load |
| Replace Battery LED | All | Battery end of life | Replace battery |
| Fault LED | OL | Internal UPS fault | Contact support |
| Bypass LED | OL | UPS in bypass mode | Check for internal fault |
| Site Wiring Fault | OL/PR | Building wiring issue | Call electrician |
| Battery Low Beeps | All | Runtime below threshold | Connect to utility or reduce load |
| Constant Alarm | All | Critical fault — battery very low | Connect to power immediately |
| Input Out of Range | OL | Utility voltage exceeds transfer range | Check supply voltage |
| F01 — Fan Fault | OL3000RT+ | Cooling fan failure | Replace fan module |

## Most Common Faults

### Replace Battery
CyberPower batteries last 3–5 years under normal conditions. Heat and frequent discharges shorten life significantly. CyberPower uses standard VRLA (AGM) batteries — replacements are available from CyberPower or third-party suppliers. Match voltage, AH rating, and physical dimensions.

### Overload
Check the load with a watt meter. CyberPower UPS systems are rated in both VA and watts — make sure both ratings are not exceeded. Laser printers create large inrush currents on startup that can trip overload protection. Connect printers to surge-only outlets rather than battery-backed outlets.

### Bypass (OL Series)
The OL series (true online double-conversion) transfers to static bypass when the inverter faults or overheats. A bypass alarm means load is running unprotected. Check the LCD for the specific fault code that caused the bypass transfer. Common causes: overtemperature from blocked vents, inverter fault, or output overload.

### Input Out of Range
OL series models have configurable input voltage windows. If utility voltage fluctuates outside the configured range, the UPS switches to battery. In areas with poor power quality, widen the input voltage window in PowerPanel software before assuming a fault.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Replacement battery | Match OEM part or equivalent VRLA |
| Fan module (OL3000RT+) | Replace on fan fault |
| Network management card | Replace on communication fault |
| Output fuse | Replace on blown output fuse |

## When to Call a Pro
CyberPower OL (online) series internal inverter and rectifier failures require factory service. Do not attempt capacitor or power board replacement without proper training and safety precautions.
