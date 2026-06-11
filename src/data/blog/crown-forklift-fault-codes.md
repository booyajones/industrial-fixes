---
title: "Crown Forklift Fault Codes - Complete Guide"
description: "Crown forklift fault codes for RC, RR, SC, and FC series electric forklifts: error codes, causes, and troubleshooting steps."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - crown
  - forklift
  - material-handling
money_part: "Steer potentiometer"
---

## Crown Forklift Fault Codes - Quick Reference

Crown forklifts (RC, RR reach trucks, SC stand-up, FC counterbalanced, and ESR order pickers) display fault codes on the InfoLink or Crown Access 1 2 3 display. Codes are accessible via the Crown Diagnostic Analyst software.

| Code | Meaning | Quick Fix |
|------|---------|-----------|
| 01 xx | Drive system fault | Check drive motor and controller |
| 02 xx | Lift system fault | Check lift motor and pump |
| 03 xx | Steer system fault | Check steer motor and sensor |
| 04 xx | Brake system fault | Check brake system |
| 05 xx | Battery/charger fault | Check battery and charger |
| 06 xx | Display/communication fault | Check harness and display |
| 07 xx | Main controller fault | Connect Diagnostic Analyst |
| 08 xx | Temperature fault | Allow cooling, check environment |
| 09 xx | I/O fault | Check sensor and harness |
| 10 xx | System warning | Read specific subcode |

## Most Common Faults

### 01 xx - Drive System Fault
Crown RC and RR series drive faults cover motor overcurrent, motor overtemperature, encoder faults, and controller faults. The two-digit extension (xx) identifies the specific issue. Most common: 01-01 (motor overheat), 01-03 (encoder fault), 01-05 (overcurrent). Check the motor temperature sensor and encoder wiring first - these are the highest-failure items on Crown reach trucks.

### 05 xx - Battery/Charger Fault
Crown's Access 1 2 3 system monitors battery state aggressively. Fault 05-01 is a low battery shutdown - charge immediately. Fault 05-02 indicates battery voltage out of range - check cell equalization. Crown's on-board charger systems can also generate 05-xx codes if the charger has a fault.

### 03 xx - Steer System Fault
Crown uses an electronic steer system (EPS) on most models. Fault 03-01 is the steer motor overtemperature; 03-03 is the steer potentiometer or sensor fault. The steer pot is a common wear item on high-cycle reach trucks. Access the raw sensor value via Diagnostic Analyst to verify the pot reads linearly across the full steering range.

### 08 xx - Temperature Fault
Crown controllers and motors have thermal protection. Temperature faults occur in hot warehouse environments or during sustained high-duty operation. Ensure the truck's motor vents are not blocked by dust buildup. Crown recommends blow-out cleaning of motor vents monthly in dusty environments.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Steer potentiometer | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-crown-forklift-fault-codes&k=Steer+potentiometer&tag=errorcodefixes-20) \| Replace on 03-xx fault |
| Motor thermal sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-crown-forklift-fault-codes&k=Motor+thermal+sensor&tag=errorcodefixes-20) \| Replace on overheat fault |
| Encoder (drive motor) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-crown-forklift-fault-codes&k=Encoder+%28drive+motor%29&tag=errorcodefixes-20) \| Replace on 01-03 fault |
| Drive controller | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-crown-forklift-fault-codes&k=Drive+controller&tag=errorcodefixes-20) \| Replace on persistent 01-xx fault |
| Battery indicator/display | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-crown-forklift-fault-codes&k=Battery+indicator%2Fdisplay&tag=errorcodefixes-20) \| Replace on 06-xx fault |
## When to Call a Pro
Crown forklifts require Crown-authorized service for mast and hydraulic repairs. The Diagnostic Analyst software is dealer-only - internal fault codes and calibration procedures are not published for general use.

