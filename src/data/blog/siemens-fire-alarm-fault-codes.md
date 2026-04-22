---
title: "Siemens Cerberus/MXL Fire Alarm Fault Codes — Troubleshooting Guide"
description: "Siemens Cerberus PRO and MXL fire alarm system fault codes: trouble conditions, ground faults, communication errors, and reset procedures."
pubDatetime: 2026-04-22T21:00:00Z
modDatetime: 2026-04-22T21:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - fire-alarm
  - siemens
  - cerberus
  - building-management
---

## Siemens Fire Alarm Fault Codes — Quick Reference

Siemens fire alarm panels (Cerberus PRO, MXL, FC-72x, FC-330) display trouble conditions, ground faults, and system faults on the front display. All faults are logged with timestamp in the event history.

| [Fault](https://www.amazon.com/s?k=Fault&tag=errorcodefixe-20) | Meaning | Quick Fix | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------- |---------|-----------|
| Ground Fault | [System DC ground fault detected](https://www.amazon.com/s?k=System%20DC%20ground%20fault%20detected&tag=errorcodefixe-20) | Use ground fault locator to isolate circuit |
| [Supervisory Trouble](https://www.amazon.com/s?k=Supervisory%20Trouble&tag=errorcodefixe-20) | Supervisory input changed state | Check sprinkler, tamper, or flow switch | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Open Circuit | Loop or zone wiring open | [Inspect wiring for breaks or loose connections](https://www.amazon.com/s?k=Inspect%20wiring%20for%20breaks%20or%20loose%20connections&tag=errorcodefixe-20) |  | Short Circuit | [Loop or zone wiring shorted](https://www.amazon.com/s?k=Loop%20or%20zone%20wiring%20shorted&tag=errorcodefixe-20) | Check for damaged cable insulation |
| [Device Comm Failure](https://www.amazon.com/s?k=Device%20Comm%20Failure&tag=errorcodefixe-20) | Addressable device not responding | Check device wiring, address, and power | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Battery Fault | Battery not charging or low voltage | [Test battery, replace if weak](https://www.amazon.com/s?k=Test%20battery%2C%20replace%20if%20weak&tag=errorcodefixe-20) |  | Loss of AC Power | [AC power supply failed](https://www.amazon.com/s?k=AC%20power%20supply%20failed&tag=errorcodefixe-20) | Check supply breaker and wiring |
| [Printer Fault](https://www.amazon.com/s?k=Printer%20Fault&tag=errorcodefixe-20) | Printer not communicating | Check printer connection and paper | [## Most Common Faults

### Ground Fault
A ground fault means one conductor on the fire alarm circuit has an unwanted connection to ground (conduit, enclosure, or earth). This is a serious trouble condition because it can mask a true alarm. Use a systematic isolation method: disconnect half the circuit, observe if fault clears, and repeat to narrow location. Ground fault locators are available for Class A wiring.

### Device Communication Failure (Addressable Systems)
An addressable device (smoke detector, pull station, module) is not responding on the loop. Check: the device is properly seated in its base, the loop wiring is continuous, the device is not physically damaged. Use the Cerberus PRO HMI or Siemens SIGMASYS software to identify the device address that is offline.

### Open Circuit (Conventional Systems)
On conventional (Class B) circuits, an open break causes all devices beyond the break to go offline. Walk the circuit and inspect junction boxes, detector bases, and pull stations for loose terminals. Use a multimeter to isolate the break point.

## NFPA 72 Requirement
All trouble conditions must be investigated and corrected. Building owners are required under NFPA 72 to maintain the fire alarm system in operational condition. Document and restore the system within a reasonable time or provide a fire watch.

## Reset Procedure

1. Silence the trouble buzzer using the SILENCE/ACKNOWLEDGE button
2. Identify and correct the fault condition
3. Press RESET on the panel
4. Confirm all indicators clear and system returns to NORMAL status
5. Log the event in the system maintenance record

## Parts Often Needed](https://www.amazon.com/s?k=%23%23%20Most%20Common%20Faults%0A%0A%23%23%23%20Ground%20Fault%0AA%20ground%20fault%20means%20one%20conductor%20on%20the%20fire%20alarm%20circuit%20has%20an%20unwanted%20connection%20to%20ground%20(conduit%2C%20enclosure%2C%20or%20earth).%20This%20is%20a%20serious%20trouble%20condition%20because%20it%20can%20mask%20a%20true%20alarm.%20Use%20a%20systematic%20isolation%20method%3A%20disconnect%20half%20the%20circuit%2C%20observe%20if%20fault%20clears%2C%20and%20repeat%20to%20narrow%20location.%20Ground%20fault%20locators%20are%20available%20for%20Class%20A%20wiring.%0A%0A%23%23%23%20Device%20Communication%20Failure%20(Addressable%20Systems)%0AAn%20addressable%20device%20(smoke%20detector%2C%20pull%20station%2C%20module)%20is%20not%20responding%20on%20the%20loop.%20Check%3A%20the%20device%20is%20properly%20seated%20in%20its%20base%2C%20the%20loop%20wiring%20is%20continuous%2C%20the%20device%20is%20not%20physically%20damaged.%20Use%20the%20Cerberus%20PRO%20HMI%20or%20Siemens%20SIGMASYS%20software%20to%20identify%20the%20device%20address%20that%20is%20offline.%0A%0A%23%23%23%20Open%20Circuit%20(Conventional%20Systems)%0AOn%20conventional%20(Class%20B)%20circuits%2C%20an%20open%20break%20causes%20all%20devices%20beyond%20the%20break%20to%20go%20offline.%20Walk%20the%20circuit%20and%20inspect%20junction%20boxes%2C%20detector%20bases%2C%20and%20pull%20stations%20for%20loose%20terminals.%20Use%20a%20multimeter%20to%20isolate%20the%20break%20point.%0A%0A%23%23%20NFPA%2072%20Requirement%0AAll%20trouble%20conditions%20must%20be%20investigated%20and%20corrected.%20Building%20owners%20are%20required%20under%20NFPA%2072%20to%20maintain%20the%20fire%20alarm%20system%20in%20operational%20condition.%20Document%20and%20restore%20the%20system%20within%20a%20reasonable%20time%20or%20provide%20a%20fire%20watch.%0A%0A%23%23%20Reset%20Procedure%0A%0A1.%20Silence%20the%20trouble%20buzzer%20using%20the%20SILENCE%2FACKNOWLEDGE%20button%0A2.%20Identify%20and%20correct%20the%20fault%20condition%0A3.%20Press%20RESET%20on%20the%20panel%0A4.%20Confirm%20all%20indicators%20clear%20and%20system%20returns%20to%20NORMAL%20status%0A5.%20Log%20the%20event%20in%20the%20system%20maintenance%20record%0A%0A%23%23%20Parts%20Often%20Needed&tag=errorcodefixe-20) | Part | Notes | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------ |-------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Sealed lead-acid battery | 12V or 24V depending on model | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Smoke detector head | Replace on dirty or failed detector | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | End-of-line resistor | Required on Class B circuits | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Loop card / SLC module | Replace on persistent loop communication faults |

## Jump to Fix

- **Ground fault** → Isolate circuits systematically → Use ground fault locator → Repair insulation
- **Device comm failure** → Check device address → Inspect base connection → Replace device
- **Open circuit** → Trace wiring → Check junction boxes → Use multimeter

## When to Call a Pro
Fire alarm systems are life-safety equipment. All repairs must comply with NFPA 72 and local AHJ (Authority Having Jurisdiction) requirements. Licensed fire alarm technicians are required in most jurisdictions.
