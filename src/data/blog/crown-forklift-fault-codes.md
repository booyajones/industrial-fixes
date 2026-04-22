---
title: "Crown Forklift Fault Codes - Complete Guide"
description: "Crown forklift fault codes for RC, RR, SC, and FC series electric forklifts: error codes, causes, and troubleshooting steps."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - crown
  - forklift
  - material-handling
---

## Crown Forklift Fault Codes - Quick Reference

Crown forklifts (RC, RR reach trucks, SC stand-up, FC counterbalanced, and ESR order pickers) display fault codes on the InfoLink or Crown Access 1 2 3 display. Codes are accessible via the Crown Diagnostic Analyst software.

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Meaning | Quick Fix | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------ |---------|-----------|
| 01 xx | [Drive system fault](https://www.amazon.com/s?k=Drive%20system%20fault&tag=errorcodefixe-20) | Check drive motor and controller |
| [02 xx](https://www.amazon.com/s?k=02%20xx&tag=errorcodefixe-20) | Lift system fault | Check lift motor and pump | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 03 xx | Steer system fault | [Check steer motor and sensor](https://www.amazon.com/s?k=Check%20steer%20motor%20and%20sensor&tag=errorcodefixe-20) |  | 04 xx | [Brake system fault](https://www.amazon.com/s?k=Brake%20system%20fault&tag=errorcodefixe-20) | Check brake system |
| [05 xx](https://www.amazon.com/s?k=05%20xx&tag=errorcodefixe-20) | Battery/charger fault | Check battery and charger | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 06 xx | Display/communication fault | [Check harness and display](https://www.amazon.com/s?k=Check%20harness%20and%20display&tag=errorcodefixe-20) |  | 07 xx | [Main controller fault](https://www.amazon.com/s?k=Main%20controller%20fault&tag=errorcodefixe-20) | Connect Diagnostic Analyst |
| [08 xx](https://www.amazon.com/s?k=08%20xx&tag=errorcodefixe-20) | Temperature fault | Allow cooling, check environment | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 09 xx | I/O fault | [Check sensor and harness](https://www.amazon.com/s?k=Check%20sensor%20and%20harness&tag=errorcodefixe-20) |  | 10 xx | [System warning](https://www.amazon.com/s?k=System%20warning&tag=errorcodefixe-20) | Read specific subcode |

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
| [Steer potentiometer](https://www.amazon.com/s?k=Steer%20potentiometer&tag=errorcodefixe-20) | Replace on 03-xx fault |
| [Motor thermal sensor](https://www.amazon.com/s?k=Motor%20thermal%20sensor&tag=errorcodefixe-20) | Replace on overheat fault |
| [Encoder (drive motor)](https://www.amazon.com/s?k=Encoder%20(drive%20motor)&tag=errorcodefixe-20) | Replace on 01-03 fault |
| [Drive controller](https://www.amazon.com/s?k=Drive%20controller&tag=errorcodefixe-20) | Replace on persistent 01-xx fault |
| [Battery indicator/display](https://www.amazon.com/s?k=Battery%20indicator%2Fdisplay&tag=errorcodefixe-20) | Replace on 06-xx fault |

## When to Call a Pro
Crown forklifts require Crown-authorized service for mast and hydraulic repairs. The Diagnostic Analyst software is dealer-only - internal fault codes and calibration procedures are not published for general use.

