---
title: "Doosan CNC Alarm Codes Guide — Fanuc / Fanuc i Series Controls"
description: "Doosan CNC machine alarm codes for Puma, DNM, and Lynx series with Fanuc 0i and 31i controls: common alarms, causes, and troubleshooting steps."
pubDatetime: 2026-04-22T21:00:00Z
modDatetime: 2026-04-22T21:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - doosan
  - cnc
  - fanuc
  - alarm-codes
---

## Doosan CNC Alarm Codes — Quick Reference

Doosan CNC machines (Puma lathes, DNM machining centers, Lynx lathes) primarily use Fanuc 0iF, 31iA, and 31iB controls. Alarms come from two sources: Fanuc NC alarms and Doosan PLC macro alarms.

## Alarm Sources

| [Alarm Range](https://www.amazon.com/s?k=Alarm%20Range&tag=errorcodefixe-20) | Source |
|------------|--------|
| [1–999](https://www.amazon.com/s?k=1%E2%80%93999&tag=errorcodefixe-20) | Fanuc NC alarms |
| [1000–1999](https://www.amazon.com/s?k=1000%E2%80%931999&tag=errorcodefixe-20) | Fanuc Servo alarms |
| [5000–5999](https://www.amazon.com/s?k=5000%E2%80%935999&tag=errorcodefixe-20) | Fanuc system alarms |
| [9001–9999](https://www.amazon.com/s?k=9001%E2%80%939999&tag=errorcodefixe-20) | Doosan PLC (PMC) macro alarms — machine-specific |

## Common Doosan / Fanuc Alarms

| [Alarm](https://www.amazon.com/s?k=Alarm&tag=errorcodefixe-20) | Meaning | Quick Fix | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------- |---------|-----------|
| 400 — Servo Alarm | [Servo drive fault](https://www.amazon.com/s?k=Servo%20drive%20fault&tag=errorcodefixe-20) | Check drive and motor |
| [460 — Spindle Speed Error](https://www.amazon.com/s?k=460%20%E2%80%94%20Spindle%20Speed%20Error&tag=errorcodefixe-20) | Spindle speed deviation | Check belt, drive, and encoder | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 700 — Overheat | Control unit thermal alarm | [Check cabinet cooling](https://www.amazon.com/s?k=Check%20cabinet%20cooling&tag=errorcodefixe-20) |  | 1000-series | [Servo axis faults](https://www.amazon.com/s?k=Servo%20axis%20faults&tag=errorcodefixe-20) | Check amplifier and motor |
| [9001 — Hydraulic Pressure](https://www.amazon.com/s?k=9001%20%E2%80%94%20Hydraulic%20Pressure&tag=errorcodefixe-20) | Hydraulic pressure low | Check hydraulic pump and pressure | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 9050 — Spindle Oil | Spindle oil level low | [Check spindle oil sight glass](https://www.amazon.com/s?k=Check%20spindle%20oil%20sight%20glass&tag=errorcodefixe-20) |  | 9100 — ATC Fault | [Tool changer alarm](https://www.amazon.com/s?k=Tool%20changer%20alarm&tag=errorcodefixe-20) | Inspect ATC mechanism |
| [9200 — Turret Fault](https://www.amazon.com/s?k=9200%20%E2%80%94%20Turret%20Fault&tag=errorcodefixe-20) | Turret indexing fault | Check turret motor and position | [## Most Common Doosan-Specific Alarms

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

## Doosan Puma vs DNM Differences](https://www.amazon.com/s?k=%23%23%20Most%20Common%20Doosan-Specific%20Alarms%0A%0A%23%23%23%20Alarm%209001%20%E2%80%94%20Hydraulic%20Pressure%20Low%0ADoosan%20machines%20(especially%20Puma%20lathes)%20use%20a%20hydraulic%20system%20for%20the%20chuck%2C%20tailstock%2C%20and%20turret.%20If%20hydraulic%20pressure%20drops%20below%20the%20setpoint%2C%20this%20alarm%20fires.%20Check%3A%0A1.%20Hydraulic%20oil%20level%20in%20the%20tank%20(sight%20glass%20on%20tank)%0A2.%20Hydraulic%20pump%20operation%20%E2%80%94%20is%20it%20running%3F%0A3.%20Hydraulic%20pressure%20switch%20and%20sensor%0A4.%20Hydraulic%20filter%20condition%20(replace%20if%20maintenance%20is%20due)%0A%0A%23%23%23%20Alarm%209050%20%E2%80%94%20Spindle%20Oil%20Low%0AThe%20spindle%20lubrication%20oil%20level%20is%20below%20the%20minimum.%20Check%20the%20spindle%20lubrication%20reservoir%20(typically%20at%20the%20top%20of%20the%20headstock%20or%20separate%20oil%20mist%20unit).%20Add%20the%20correct%20spindle%20oil%20grade.%20Do%20not%20run%20the%20machine%20on%20low%20spindle%20oil%20%E2%80%94%20it%20damages%20spindle%20bearings.%0A%0A%23%23%23%20Alarm%209100%20%E2%80%94%20ATC%20(Tool%20Changer)%20Fault%0AThe%20automatic%20tool%20changer%20did%20not%20complete%20its%20indexing%20cycle.%20Check%20for%3A%0A-%20Tool%20caught%20in%20turret%20or%20arm%20mechanism%0A-%20ATC%20position%20sensor%20misaligned%0A-%20Hydraulic%20pressure%20low%20(if%20hydraulically%20actuated)%0A-%20Drive%20fault%20on%20ATC%20servo%20motor%0A%0A%23%23%20Doosan%20Puma%20vs%20DNM%20Differences&tag=errorcodefixe-20) | Feature | Puma (Lathe) | [DNM (Machining Center)](https://www.amazon.com/s?k=DNM%20(Machining%20Center)&tag=errorcodefixe-20) |  |---------|-------------|----------------------|
| [Typical turret](https://www.amazon.com/s?k=Typical%20turret&tag=errorcodefixe-20) | 12-station hydraulic | 30-tool BT40 ATC | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Hydraulic system | Yes | [Limited or no](https://www.amazon.com/s?k=Limited%20or%20no&tag=errorcodefixe-20) |  | Spindle configuration | [Horizontal, C-axis](https://www.amazon.com/s?k=Horizontal%2C%20C-axis&tag=errorcodefixe-20) | Vertical |
| [Common 9xxx alarms](https://www.amazon.com/s?k=Common%209xxx%20alarms&tag=errorcodefixe-20) | Chuck, turret, tailstock | ATC, pallet, tool length | [## Reading Doosan PMC Alarms

PMC alarms on Doosan machines show as "PMC ALARM" followed by the alarm number. To see the alarm message:
1. Press OFFSET/SETTING → PMC → ALARM
2. The alarm text explains the condition and required action

## Parts Often Needed](https://www.amazon.com/s?k=%23%23%20Reading%20Doosan%20PMC%20Alarms%0A%0APMC%20alarms%20on%20Doosan%20machines%20show%20as%20%22PMC%20ALARM%22%20followed%20by%20the%20alarm%20number.%20To%20see%20the%20alarm%20message%3A%0A1.%20Press%20OFFSET%2FSETTING%20%E2%86%92%20PMC%20%E2%86%92%20ALARM%0A2.%20The%20alarm%20text%20explains%20the%20condition%20and%20required%20action%0A%0A%23%23%20Parts%20Often%20Needed&tag=errorcodefixe-20) | Part | Notes | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------ |-------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Hydraulic filter | Replace on pressure alarm | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Spindle oil | Fill to correct level | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Turret position sensor | Check on turret fault alarms | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ATC servo motor | Check on persistent ATC faults |

## Jump to Fix

- **9001 hydraulic** → Check oil level → Check pump → Check pressure switch
- **9050 spindle oil** → Check and fill reservoir → Identify cause of low level
- **9100 ATC fault** → Inspect mechanism → Check position sensors → Check hydraulics

## When to Call a Pro
Doosan Machine Tools America provides service support at 1-973-618-2500. Fanuc-specific alarms can also be diagnosed by Fanuc-authorized service providers.
