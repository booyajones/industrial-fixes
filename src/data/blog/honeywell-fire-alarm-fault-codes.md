---
title: "Honeywell NOTIFIER Fire Alarm Fault Codes — IFP-50 / ONYX Guide"
description: "Honeywell fire alarm system fault codes for NOTIFIER IFP-50, ONYX Series NFS2-640, and FlashScan SLC panels: trouble conditions and troubleshooting."
pubDatetime: 2026-04-22T21:00:00Z
modDatetime: 2026-04-22T21:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - fire-alarm
  - honeywell
  - notifier
  - building-management
---

## Honeywell NOTIFIER Fire Alarm Fault Codes — Quick Reference

Honeywell's NOTIFIER brand (IFP-50, NFS2-640, NFS2-3030, ONYX Series) uses FlashScan addressable loop technology. Trouble conditions identify the device address and fault type on the display.

| [Trouble](https://www.amazon.com/s?k=Trouble&tag=errorcodefixe-20) | Meaning | Quick Fix | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | --------- |---------|-----------|
| Ground Fault | [Field wiring grounded](https://www.amazon.com/s?k=Field%20wiring%20grounded&tag=errorcodefixe-20) | Isolate circuit sections systematically |
| [Open SLC](https://www.amazon.com/s?k=Open%20SLC&tag=errorcodefixe-20) | Loop break detected | Trace FlashScan loop wiring | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Device Trouble | Device not responding or failed | [Inspect device at listed address](https://www.amazon.com/s?k=Inspect%20device%20at%20listed%20address&tag=errorcodefixe-20) |  | Dirty Detector | [Detector compensation near limit](https://www.amazon.com/s?k=Detector%20compensation%20near%20limit&tag=errorcodefixe-20) | Clean or replace detector head |
| [Low Battery](https://www.amazon.com/s?k=Low%20Battery&tag=errorcodefixe-20) | Battery below voltage threshold | Load test, replace battery | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | AC Trouble | AC power supply lost | [Check breaker and supply](https://www.amazon.com/s?k=Check%20breaker%20and%20supply&tag=errorcodefixe-20) |  | NAC Open | [Notification circuit open](https://www.amazon.com/s?k=Notification%20circuit%20open&tag=errorcodefixe-20) | Check horn/strobe circuit wiring |
| [Waterflow Alarm](https://www.amazon.com/s?k=Waterflow%20Alarm&tag=errorcodefixe-20) | Sprinkler flow switch activated | Verify false alarm vs real flow | [## FlashScan SLC Loop Technology

Honeywell NOTIFIER's FlashScan protocol polls addressable devices at high speed. The panel identifies which specific device is in trouble by its SLC address. Key advantage: devices can be quickly located using the address-to-location map in the panel programming.

### Reading the Trouble Message
1. Press ACKNOWLEDGE on the panel to silence the trouble sounder
2. The display shows: Trouble type + Loop number + Device address
   - Example: "DEVICE TROUBLE L1 D047" = Loop 1, Device 47
3. Look up Device 47 on the floor plan drawings to find its physical location
4. Walk to the device and inspect

## Most Common Faults

### Dirty Detector
Honeywell NOTIFIER panels display "DIRTY DETECTOR" when an FAPT or FSP series smoke detector reaches its maintenance threshold. The FlashScan system tracks compensation levels — a higher compensation indicates a dirtier chamber. Clean the detector head with compressed air. Replace the head if it has been in service more than 7–10 years.

### Ground Fault
A ground fault on the NOTIFIER SLC loop will cause all devices on the affected section to become unreachable if the fault is severe. Use a ground fault isolator module or systematic disconnection to find the fault.

### Low Battery / Battery Trouble
The NOTIFIER panel performs a battery load test every 24 hours. If the battery voltage drops below the threshold, a low battery trouble appears. Test the battery with a load tester. If it cannot hold 24V under load (or 12V per battery in a 24V series pair), replace both batteries.

## Parts Often Needed](https://www.amazon.com/s?k=%23%23%20FlashScan%20SLC%20Loop%20Technology%0A%0AHoneywell%20NOTIFIER's%20FlashScan%20protocol%20polls%20addressable%20devices%20at%20high%20speed.%20The%20panel%20identifies%20which%20specific%20device%20is%20in%20trouble%20by%20its%20SLC%20address.%20Key%20advantage%3A%20devices%20can%20be%20quickly%20located%20using%20the%20address-to-location%20map%20in%20the%20panel%20programming.%0A%0A%23%23%23%20Reading%20the%20Trouble%20Message%0A1.%20Press%20ACKNOWLEDGE%20on%20the%20panel%20to%20silence%20the%20trouble%20sounder%0A2.%20The%20display%20shows%3A%20Trouble%20type%20%2B%20Loop%20number%20%2B%20Device%20address%0A%20%20%20-%20Example%3A%20%22DEVICE%20TROUBLE%20L1%20D047%22%20%3D%20Loop%201%2C%20Device%2047%0A3.%20Look%20up%20Device%2047%20on%20the%20floor%20plan%20drawings%20to%20find%20its%20physical%20location%0A4.%20Walk%20to%20the%20device%20and%20inspect%0A%0A%23%23%20Most%20Common%20Faults%0A%0A%23%23%23%20Dirty%20Detector%0AHoneywell%20NOTIFIER%20panels%20display%20%22DIRTY%20DETECTOR%22%20when%20an%20FAPT%20or%20FSP%20series%20smoke%20detector%20reaches%20its%20maintenance%20threshold.%20The%20FlashScan%20system%20tracks%20compensation%20levels%20%E2%80%94%20a%20higher%20compensation%20indicates%20a%20dirtier%20chamber.%20Clean%20the%20detector%20head%20with%20compressed%20air.%20Replace%20the%20head%20if%20it%20has%20been%20in%20service%20more%20than%207%E2%80%9310%20years.%0A%0A%23%23%23%20Ground%20Fault%0AA%20ground%20fault%20on%20the%20NOTIFIER%20SLC%20loop%20will%20cause%20all%20devices%20on%20the%20affected%20section%20to%20become%20unreachable%20if%20the%20fault%20is%20severe.%20Use%20a%20ground%20fault%20isolator%20module%20or%20systematic%20disconnection%20to%20find%20the%20fault.%0A%0A%23%23%23%20Low%20Battery%20%2F%20Battery%20Trouble%0AThe%20NOTIFIER%20panel%20performs%20a%20battery%20load%20test%20every%2024%20hours.%20If%20the%20battery%20voltage%20drops%20below%20the%20threshold%2C%20a%20low%20battery%20trouble%20appears.%20Test%20the%20battery%20with%20a%20load%20tester.%20If%20it%20cannot%20hold%2024V%20under%20load%20(or%2012V%20per%20battery%20in%20a%2024V%20series%20pair)%2C%20replace%20both%20batteries.%0A%0A%23%23%20Parts%20Often%20Needed&tag=errorcodefixe-20) | Part | Notes | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------ |-------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | FAPT/FSP detector head | Replace on dirty or failed head | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 12V sealed lead-acid battery | Replace as a pair on 24V systems | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | End-of-line resistor EOLR-1 | Required on NAC circuits | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | SLC isolator module | Install if ground fault isolation needed |

## Jump to Fix

- **Dirty detector** → Walk to address → Clean head with dry air → Reset
- **Ground fault** → Section isolation → Locate damaged cable → Repair
- **Device trouble** → Walk to address → Inspect base connection → Replace device

## When to Call a Pro
Honeywell NOTIFIER-certified technicians handle programming, point-by-point commissioning, and system certifications. Contact a NOTIFIER-authorized service dealer for major repairs.
