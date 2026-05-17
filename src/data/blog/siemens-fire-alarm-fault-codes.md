---
title: "Siemens Cerberus/MXL Fire Alarm Fault Codes — Troubleshooting Guide"
description: "Siemens Cerberus PRO and MXL fire alarm system fault codes: trouble conditions, ground faults, communication errors, and reset procedures."
pubDatetime: 2026-04-22T21:00:00Z
modDatetime: 2026-04-22T21:00:00Z
author: "Dana Kowalski"
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

| Fault | Meaning | Quick Fix |
|-------|---------|-----------|
| Ground Fault | System DC ground fault detected | Use ground fault locator to isolate circuit |
| Supervisory Trouble | Supervisory input changed state | Check sprinkler, tamper, or flow switch |
| Open Circuit | Loop or zone wiring open | Inspect wiring for breaks or loose connections |
| Short Circuit | Loop or zone wiring shorted | Check for damaged cable insulation |
| Device Comm Failure | Addressable device not responding | Check device wiring, address, and power |
| Battery Fault | Battery not charging or low voltage | Test battery, replace if weak |
| Loss of AC Power | AC power supply failed | Check supply breaker and wiring |
| Printer Fault | Printer not communicating | Check printer connection and paper |

## Most Common Faults

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

## Parts Often Needed

| Part | Notes |
|------|-------|
| Sealed lead-acid battery | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-fire-alarm-fault-codes&k=Sealed+lead-acid+battery&tag=errorcodefixes-20) \| 12V or 24V depending on model |
| Smoke detector head | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-fire-alarm-fault-codes&k=Smoke+detector+head&tag=errorcodefixes-20) \| Replace on dirty or failed detector |
| End-of-line resistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-fire-alarm-fault-codes&k=End-of-line+resistor&tag=errorcodefixes-20) \| Required on Class B circuits |
| Loop card / SLC module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-fire-alarm-fault-codes&k=Loop+card+%2F+SLC+module&tag=errorcodefixes-20) \| Replace on persistent loop communication faults |
## Jump to Fix

- **Ground fault** → Isolate circuits systematically → Use ground fault locator → Repair insulation
- **Device comm failure** → Check device address → Inspect base connection → Replace device
- **Open circuit** → Trace wiring → Check junction boxes → Use multimeter

## When to Call a Pro
Fire alarm systems are life-safety equipment. All repairs must comply with NFPA 72 and local AHJ (Authority Having Jurisdiction) requirements. Licensed fire alarm technicians are required in most jurisdictions.

## Related Articles

- [Siemens Sinumerik 828D Alarm Codes Guide — Complete Diagnostic Reference](/posts/siemens-828d-alarm-codes/)
- [Siemens 840D Alarm 380000 — Causes & Fix](/posts/siemens-840d-alarm-380000/)
- [Siemens Circuit Breaker Fault Codes - Complete Guide](/posts/siemens-circuit-breaker-fault-codes/)
- [Siemens Desigo BMS Fault Codes - Complete Guide](/posts/siemens-desigo-fault-codes/)
- [Siemens G120C VFD Fault Code Guide — Complete Diagnostic Reference](/posts/siemens-g120c-fault-codes/)
