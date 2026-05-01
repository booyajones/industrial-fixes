---
title: "DMG Mori CNC Fault Codes Guide — CELOS / Siemens 840D"
description: "DMG Mori CNC machine fault codes for CELOS and Siemens 840D SL controls: alarm descriptions, servo and spindle faults, and troubleshooting steps."
pubDatetime: 2026-04-22T21:00:00Z
modDatetime: 2026-04-22T21:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - dmg-mori
  - cnc
  - siemens-840d
  - celos
  - fault-codes
---

## DMG Mori CNC Fault Codes — Quick Reference

DMG Mori machining centers and lathes (NLX, NHX, DMC, CTX, DMU series) typically run Siemens SINUMERIK 840D sl, 828D, or Fanuc controls under the CELOS user interface. Alarms come from both the Siemens NC system and DMG-specific PLC alarms.

## Alarm Types on DMG Mori Machines

| Alarm Range | Source |
|------------|--------|
| 1–999 | Siemens NC alarms (channel) |
| 300000–399999 | Siemens SINAMICS drive alarms (A3xxxxx) |
| 380000–380999 | Servo drive alarms |
| 700000–799999 | PLC alarms (DMG machine-specific) |

See also: [Siemens SINUMERIK Alarm Guide](/siemens-sinumerik-840d-alarm-25000) for detailed Siemens NC alarm coverage.

## Most Common DMG Mori Faults

### Alarm 380500 / 380600 — SINAMICS Drive Fault
These alarms on the 840D indicate the SINAMICS S120 servo or spindle drive has faulted. The SINUMERIK Alarm 380xxx always corresponds to a specific SINAMICS fault code. To find it:
1. On CELOS: go to SERVICE → DRIVE DIAGNOSTICS
2. Check the drive's fault buffer on the NCK panel
3. Look up the F-number in the SINAMICS alarm list

Common SINAMICS faults on DMG machines:
- **F07805** — Drive: encoder fault
- **F30003** — Motor: overheat (NTC monitoring)
- **F07010** — Drive: overcurrent

### PLC Alarm 700xxx — Machine-Specific Alarms
DMG uses 700000–799999 for machine-specific PLC alarms (hydraulics, lubrication, ATC, pallet changer). These require the machine-specific alarm text documentation from DMG Mori. Common DMG PLC alarms include:
- **700001** — Hydraulic unit fault — check hydraulic pressure
- **700045** — Lubrication fault — check lubrication pump and oil
- **700100** — ATC fault — inspect tool changer mechanism

### Emergency Stop / Safety Faults
CELOS-equipped DMG machines use safety integrated functions (SIL). If an SIL fault occurs, the machine goes to a controlled stop and requires safety system verification before restart.

## CELOS Alarm Navigation

1. On the CELOS touchscreen: tap the RED alarm indicator in the header
2. Select ALARMS to see the current active alarm list
3. Each alarm shows: number, description, and cancel button (if allowed)
4. ALARM HISTORY shows past events with timestamps

## Maintenance Alarms (M Alarms)

DMG Mori machines generate maintenance alarms for:
- Spindle load history intervals
- Lubrication oil change
- Hydraulic filter service
- Annual calibration reminders

These appear as advisory alarms (yellow) and do not prevent machine operation but should be addressed promptly.

## Parts Often Needed

| Part | Notes |
|------|-------|
| SINAMICS encoder cable | [Amazon](https://www.amazon.com/s?k=SINAMICS+encoder+cable&tag=errorcodefixes-20) \| Replace on F07805 encoder faults |
| Hydraulic filter | [Amazon](https://www.amazon.com/s?k=Hydraulic+filter&tag=errorcodefixes-20) \| Replace on lubrication/hydraulic alarms |
| Tool changer cam followers | [Amazon](https://www.amazon.com/s?k=Tool+changer+cam+followers&tag=errorcodefixes-20) \| Inspect on ATC faults |
| Lubrication pump | [Amazon](https://www.amazon.com/s?k=Lubrication+pump&tag=errorcodefixes-20) \| Replace on lubrication alarms |
## Jump to Fix

- **380xxx drive fault** → Check SINAMICS fault buffer → Diagnose F-code → Address root cause
- **700xxx PLC alarm** → Reference alarm text → Check specified subsystem → Clear fault
- **ATC fault** → Inspect ATC mechanism → Check position sensors → Verify hydraulics

## When to Call a Pro
DMG Mori has a nationwide service organization in North America. Contact 1-800-362-4891. CELOS and SINUMERIK configuration changes require factory training.
