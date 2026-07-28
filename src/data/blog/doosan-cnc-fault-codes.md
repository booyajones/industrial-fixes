---
canonicalURL: "https://errorcodefixes.com/posts/doosan-cnc-fault-codes-complete/"
title: "Doosan CNC Alarm Codes Guide — Fanuc / Fanuc i Series Controls"
description: "Doosan CNC machine alarm codes for Puma, DNM, and Lynx series with Fanuc 0i and 31i controls: common alarms, causes, and troubleshooting steps."
pubDatetime: 2026-04-22T21:00:00Z
modDatetime: 2026-04-22T21:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - doosan
  - cnc
  - fanuc
  - alarm-codes
money_part: "Hydraulic filter"
---

## Doosan CNC Alarm Codes — Quick Reference

Doosan CNC machines (Puma lathes, DNM machining centers, Lynx lathes) primarily use Fanuc 0iF, 31iA, and 31iB controls. Alarms come from two sources: Fanuc NC alarms and Doosan PLC macro alarms.

## Alarm Sources

| Alarm Range | Source |
|------------|--------|
| 1–999 | Fanuc NC alarms |
| 1000–1999 | Fanuc Servo alarms |
| 5000–5999 | Fanuc system alarms |
| 9001–9999 | Doosan PLC (PMC) macro alarms — machine-specific |

## Common Doosan / Fanuc Alarms

| Alarm | Meaning | Quick Fix |
|-------|---------|-----------|
| 400 — Servo Alarm | Servo drive fault | Check drive and motor |
| 460 — Spindle Speed Error | Spindle speed deviation | Check belt, drive, and encoder |
| 700 — Overheat | Control unit thermal alarm | Check cabinet cooling |
| 1000-series | Servo axis faults | Check amplifier and motor |
| 9001 — Hydraulic Pressure | Hydraulic pressure low | Check hydraulic pump and pressure |
| 9050 — Spindle Oil | Spindle oil level low | Check spindle oil sight glass |
| 9100 — ATC Fault | Tool changer alarm | Inspect ATC mechanism |
| 9200 — Turret Fault | Turret indexing fault | Check turret motor and position |

## Most Common Doosan-Specific Alarms

### Alarm 9001 — Hydraulic Pressure Low
Doosan machines (especially Puma lathes) use a hydraulic system for the chuck, tailstock, and turret. If hydraulic pressure drops below the setpoint, this alarm fires. Check:
1. Hydraulic oil level in the tank (sight glass on tank)
2. Hydraulic pump operation — is it running?
3. Hydraulic pressure switch and sensor
4. Hydraulic filter condition (replace if maintenance is due)

### Alarm 9050 — Spindle Oil Low
The spindle lubrication oil level is below the minimum. Check the spindle lubrication reservoir (typically at the top of the headstock or separate oil mist unit). Add the correct spindle oil grade. Do not run the machine on low spindle oil — it damages spindle bearings.

### Alarm 9100 — ATC (Tool Changer) Fault
The automatic tool changer did not complete its indexing cycle. Check for:
- Tool caught in turret or arm mechanism
- ATC position sensor misaligned
- Hydraulic pressure low (if hydraulically actuated)
- Drive fault on ATC servo motor

## Doosan Puma vs DNM Differences

| Feature | Puma (Lathe) | DNM (Machining Center) |
|---------|-------------|----------------------|
| Typical turret | 12-station hydraulic | 30-tool BT40 ATC |
| Hydraulic system | Yes | Limited or no |
| Spindle configuration | Horizontal, C-axis | Vertical |
| Common 9xxx alarms | Chuck, turret, tailstock | ATC, pallet, tool length |

## Reading Doosan PMC Alarms

PMC alarms on Doosan machines show as "PMC ALARM" followed by the alarm number. To see the alarm message:
1. Press OFFSET/SETTING → PMC → ALARM
2. The alarm text explains the condition and required action

## Parts Often Needed

| Part | Notes |
|------|-------|
| Hydraulic filter | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-doosan-cnc-fault-codes&k=Hydraulic+filter&tag=errorcodefixes-20) \| Replace on pressure alarm |
| Spindle oil | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-doosan-cnc-fault-codes&k=Spindle+oil&tag=errorcodefixes-20) \| Fill to correct level |
| Turret position sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-doosan-cnc-fault-codes&k=Turret+position+sensor&tag=errorcodefixes-20) \| Check on turret fault alarms |
| ATC servo motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-doosan-cnc-fault-codes&k=ATC+servo+motor&tag=errorcodefixes-20) \| Check on persistent ATC faults |
## Jump to Fix

- **9001 hydraulic** → Check oil level → Check pump → Check pressure switch
- **9050 spindle oil** → Check and fill reservoir → Identify cause of low level
- **9100 ATC fault** → Inspect mechanism → Check position sensors → Check hydraulics

## When to Call a Pro
Doosan Machine Tools America provides service support at 1-973-618-2500. Fanuc-specific alarms can also be diagnosed by Fanuc-authorized service providers.
