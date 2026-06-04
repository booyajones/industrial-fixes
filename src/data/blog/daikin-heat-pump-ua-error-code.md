---
title: "Daikin UA Error Code - Causes & Fix"
description: "UA means indoor/outdoor unit combination fault. Most often caused by wrong model pairing or communication wiring errors on VRV/multi-split systems."
pubDatetime: 2026-05-31T14:50:18Z
modDatetime: 2026-05-31T14:50:18Z
author: "James Rutherford"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - daikin
---

## Daikin UA Error Code — What It Means

The UA error code on a Daikin heat pump indicates an indoor/outdoor unit combination fault. The outdoor unit cannot correctly recognize the connected indoor unit(s), or the system configuration is invalid. This code appears most often on VRV, VRF, and multi-split systems when the indoor and outdoor models are incompatible, when too many indoor units are connected, when communication wiring is faulty, or when commissioning settings were never completed after installation. It can also signal a defective control board in either the indoor or outdoor unit.

[Jump to Fix](#fix)

## Common Causes

- **Wrong model combination** The indoor and outdoor units belong to incompatible series, use different refrigerant types, or exceed the allowed capacity pairing per Daikin's compatibility tables.
- **Too many indoor units connected** The number of indoor units exceeds the maximum quantity supported by the outdoor unit for that system configuration.
- **Communication wiring fault** Loose terminals, open circuits, poor contact, or reversed polarity in the communication line between indoor and outdoor units prevent proper recognition.
- **Commissioning not completed** The outdoor PCB settings or system check operation were never performed after installation, leaving the system unconfigured.
- **Incorrect addressing or control settings** Indoor unit addresses are duplicated, missing, or the centralized control configuration does not match the actual equipment installed.
- **Defective PCB** The outdoor unit control board or an indoor unit board has failed and cannot communicate or validate the system combination even when wiring and models are correct.

## Step-by-Step Fix {#fix}

1. **Verify model compatibility** by checking each indoor unit model number and the outdoor unit model number against Daikin's official combination tables for your system series and refrigerant type.
2. **Count connected indoor units** and confirm the total quantity and combined capacity do not exceed the outdoor unit's rated maximum per the installation manual.
3. **Inspect communication wiring** between indoor and outdoor units for loose screws, broken wires, poor contact at terminal blocks, and correct polarity on communication terminals.
4. **Check indoor unit addressing** using the service mode or DIP switches to make sure each unit has a unique address and that no duplicates or gaps exist in the sequence.
5. **Confirm commissioning settings** by reviewing the installation checklist to verify the outdoor PCB settings and system check operation were completed when the system was installed.
6. **Test for PCB faults** by swapping a suspect indoor or outdoor board with a known-good spare if available, or by using a multimeter to check for communication signal presence on the communication terminals.
7. **Clear the error code** after making corrections, run the system for several cycles, and monitor for recurrence before considering the repair complete.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Daikin outdoor unit PCB (control board) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-heat-pump-ua-error-code&k=Daikin+outdoor+unit+PCB+%28control+board%29&tag=errorcodefixes-20) \| Match the exact part number printed on your existing board or consult your model's service manual. |
| Daikin indoor unit PCB (control board) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-heat-pump-ua-error-code&k=Daikin+indoor+unit+PCB+%28control+board%29&tag=errorcodefixes-20) \| Required if diagnostics isolate a fault to a specific indoor unit's communication circuit. |
| Communication wiring and terminal blocks | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-heat-pump-ua-error-code&k=Communication+wiring+and+terminal+blocks&tag=errorcodefixes-20) \| Use factory-spec shielded communication cable if existing wiring is damaged or incorrectly installed. |

## When to Call a Pro

Call a licensed HVAC technician if you are not confident reading wiring diagrams, if you lack access to Daikin's official combination tables and service mode procedures, or if the error persists after checking models and wiring. VRV and VRF systems require specialized tools and software to configure addresses and commissioning settings. Replacing control boards or reconfiguring multi-split systems without proper training can damage expensive components or void warranties. A qualified Daikin service provider has the technical bulletins, diagnostic software, and replacement boards needed to resolve combination faults efficiently.
