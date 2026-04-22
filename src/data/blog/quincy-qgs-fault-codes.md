---
title: "Quincy QGS Compressor Fault Codes: Complete Guide"
description: "Quincy QGS rotary screw compressor fault codes and diagnostics. Intellizone II fault codes, causes, and technician-level troubleshooting."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-04-22T23:45:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - compressor
  - quincy
  - industrial
---

# Quincy QGS Compressor Fault Codes

Quincy QGS rotary screw compressors use the Intellizone II controller. Fault codes and messages display on the Intellizone panel LCD. The controller stores fault history with run hours and timestamps.

## QGS Fault Code Table

| [Code/Message](https://www.amazon.com/s?k=Code%2FMessage&tag=errorcodefixe-20) | Fault Description | Common Cause | [Action](https://www.amazon.com/s?k=Action&tag=errorcodefixe-20) |  |-------------|------------------|--------------|--------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | HIGH TEMP | High discharge temperature | [Dirty cooler, low oil, high ambient](https://www.amazon.com/s?k=Dirty%20cooler%2C%20low%20oil%2C%20high%20ambient&tag=errorcodefixe-20) | Clean cooler, check oil |
| [HIGH TEMP WARN](https://www.amazon.com/s?k=HIGH%20TEMP%20WARN&tag=errorcodefixe-20) | Temperature approaching limit | Pre-shutdown warning | [Clean cooler immediately](https://www.amazon.com/s?k=Clean%20cooler%20immediately&tag=errorcodefixe-20) |  | MOTOR OVERLOAD | [Motor thermal trip](https://www.amazon.com/s?k=Motor%20thermal%20trip&tag=errorcodefixe-20) | Excessive current or load | Check motor amps and load | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | HIGH PRESSURE | System pressure too high | [Excessive demand](https://www.amazon.com/s?k=Excessive%20demand&tag=errorcodefixe-20) | Check pressure setting |
| [LOW OIL PRESSURE](https://www.amazon.com/s?k=LOW%20OIL%20PRESSURE&tag=errorcodefixe-20) | Oil pressure insufficient | Low oil or failed pump | [Check oil level and pump](https://www.amazon.com/s?k=Check%20oil%20level%20and%20pump&tag=errorcodefixe-20) |  | PHASE LOSS | [Missing supply phase](https://www.amazon.com/s?k=Missing%20supply%20phase&tag=errorcodefixe-20) | Fuse or supply fault | Check input power | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | INLET RESTRICTION | Dirty inlet filter | [Restricted air intake](https://www.amazon.com/s?k=Restricted%20air%20intake&tag=errorcodefixe-20) | Replace inlet filter |
| [EMERGENCY STOP](https://www.amazon.com/s?k=EMERGENCY%20STOP&tag=errorcodefixe-20) | E-stop active | E-stop circuit open | [Check E-stop wiring](https://www.amazon.com/s?k=Check%20E-stop%20wiring&tag=errorcodefixe-20) |  | CHECK SEPARATOR | [Separator element pressure drop high](https://www.amazon.com/s?k=Separator%20element%20pressure%20drop%20high&tag=errorcodefixe-20) | Dirty separator | Replace separator element | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | SERVICE DUE | Maintenance interval reached | [Hours elapsed](https://www.amazon.com/s?k=Hours%20elapsed&tag=errorcodefixe-20) | Perform scheduled PM |
| [SENSOR FAULT](https://www.amazon.com/s?k=SENSOR%20FAULT&tag=errorcodefixe-20) | Failed temperature sensor | Open or shorted sensor | [Replace thermistor](https://www.amazon.com/s?k=Replace%20thermistor&tag=errorcodefixe-20) |  | AUTO DRAIN FAULT | [Condensate drain valve fault](https://www.amazon.com/s?k=Condensate%20drain%20valve%20fault&tag=errorcodefixe-20) | Solenoid valve failure | Check drain valve | [## Most Common QGS Faults

### HIGH TEMP
Quincy QGS compressors have a high-temperature shutdown at typically 228°F (109°C). The most common cause is a dirty oil cooler or air aftercooler. Blow fins clean with low-pressure air. On larger QGS models, the cooler can be removed for power washing with degreaser.

### MOTOR OVERLOAD
Check that the motor overload relay is set correctly: current setting should be 100–105% of motor nameplate FLA. Verify three-phase voltage balance — more than 3% imbalance causes disproportionate current in one phase.

### CHECK SEPARATOR — Separator Element
When separator differential pressure exceeds design maximum (typically 10 PSI), this alarm triggers. The separator element is a wear item — replace at the scheduled interval (typically 4,000 hours). A clogged separator element increases discharge temperature and reduces compressor efficiency.

### AUTO DRAIN FAULT
Quincy QGS has an electronic auto-drain to remove condensate from the separator tank. If the solenoid valve fails (stuck closed = water in oil; stuck open = air loss), this fault triggers. Check solenoid valve coil resistance and verify 24 VAC at coil during drain cycle.

## Parts Commonly Needed](https://www.amazon.com/s?k=%23%23%20Most%20Common%20QGS%20Faults%0A%0A%23%23%23%20HIGH%20TEMP%0AQuincy%20QGS%20compressors%20have%20a%20high-temperature%20shutdown%20at%20typically%20228%C2%B0F%20(109%C2%B0C).%20The%20most%20common%20cause%20is%20a%20dirty%20oil%20cooler%20or%20air%20aftercooler.%20Blow%20fins%20clean%20with%20low-pressure%20air.%20On%20larger%20QGS%20models%2C%20the%20cooler%20can%20be%20removed%20for%20power%20washing%20with%20degreaser.%0A%0A%23%23%23%20MOTOR%20OVERLOAD%0ACheck%20that%20the%20motor%20overload%20relay%20is%20set%20correctly%3A%20current%20setting%20should%20be%20100%E2%80%93105%25%20of%20motor%20nameplate%20FLA.%20Verify%20three-phase%20voltage%20balance%20%E2%80%94%20more%20than%203%25%20imbalance%20causes%20disproportionate%20current%20in%20one%20phase.%0A%0A%23%23%23%20CHECK%20SEPARATOR%20%E2%80%94%20Separator%20Element%0AWhen%20separator%20differential%20pressure%20exceeds%20design%20maximum%20(typically%2010%20PSI)%2C%20this%20alarm%20triggers.%20The%20separator%20element%20is%20a%20wear%20item%20%E2%80%94%20replace%20at%20the%20scheduled%20interval%20(typically%204%2C000%20hours).%20A%20clogged%20separator%20element%20increases%20discharge%20temperature%20and%20reduces%20compressor%20efficiency.%0A%0A%23%23%23%20AUTO%20DRAIN%20FAULT%0AQuincy%20QGS%20has%20an%20electronic%20auto-drain%20to%20remove%20condensate%20from%20the%20separator%20tank.%20If%20the%20solenoid%20valve%20fails%20(stuck%20closed%20%3D%20water%20in%20oil%3B%20stuck%20open%20%3D%20air%20loss)%2C%20this%20fault%20triggers.%20Check%20solenoid%20valve%20coil%20resistance%20and%20verify%2024%20VAC%20at%20coil%20during%20drain%20cycle.%0A%0A%23%23%20Parts%20Commonly%20Needed&tag=errorcodefixe-20) | Part | Notes | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------ |-------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Inlet air filter | Model-specific | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Oil/separator element | Replace per service schedule | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Quincy QGS oil | Synthetic — match model specification | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Auto-drain solenoid | Check coil resistance | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Temperature thermistor | NTC type — check resistance vs. temp chart | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Motor overload relay | Match FLA setting |

> **Pro tip:** Quincy QGS Intellizone II logs the last 10 faults with run hours. Access via MENU → HISTORY → FAULT LOG on the panel. If HIGH TEMP faults are increasing in frequency, track the interval between faults — progressive reduction in time between faults indicates a degrading cooler before total failure.
