---
title: "Mitsubishi Elevator Fault Codes - Complete Guide"
description: "Mitsubishi elevator fault codes for NEXIEZ, ELENESSA, and MELCO systems: common alarms, causes, and diagnostic steps."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - mitsubishi
  - elevator
  - lift
---

## Mitsubishi Elevator Fault Codes - Quick Reference

Mitsubishi Electric elevators (NEXIEZ, ELENESSA, GRANDEUR, Sigma series) use the Mitsubishi VFEM and proprietary control platforms. Fault codes are accessible via the Mitsubishi service tool (MELTRAC) or the controller's LED/LCD panel.

| [Fault](https://www.amazon.com/s?k=Fault&tag=errorcodefixe-20) | System | Meaning | [Quick Fix](https://www.amazon.com/s?k=Quick%20Fix&tag=errorcodefixe-20) |  |-------|--------|---------|-----------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Safety Circuit Open | All | [Safety chain open](https://www.amazon.com/s?k=Safety%20chain%20open&tag=errorcodefixe-20) | Check door contacts and limits |
| [Door Fault](https://www.amazon.com/s?k=Door%20Fault&tag=errorcodefixe-20) | All | Door open/close failure | [Check door operator](https://www.amazon.com/s?k=Check%20door%20operator&tag=errorcodefixe-20) |  | Drive Fault (E-xx) | [NEXIEZ](https://www.amazon.com/s?k=NEXIEZ&tag=errorcodefixe-20) | Drive/inverter alarm | Read inverter fault code | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Brake Fault | All | [Brake monitoring error](https://www.amazon.com/s?k=Brake%20monitoring%20error&tag=errorcodefixe-20) | Check brake coil |
| [Encoder Fault](https://www.amazon.com/s?k=Encoder%20Fault&tag=errorcodefixe-20) | All | Speed feedback error | [Check encoder cable](https://www.amazon.com/s?k=Check%20encoder%20cable&tag=errorcodefixe-20) |  | Overload | [All](https://www.amazon.com/s?k=All&tag=errorcodefixe-20) | Car overloaded | Check weighing device | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Terminal Limit | All | [Travel limit switch active](https://www.amazon.com/s?k=Travel%20limit%20switch%20active&tag=errorcodefixe-20) | Check limits |
| [Car Top Emergency Stop](https://www.amazon.com/s?k=Car%20Top%20Emergency%20Stop&tag=errorcodefixe-20) | All | Car roof E-stop activated | [Reset and inspect](https://www.amazon.com/s?k=Reset%20and%20inspect&tag=errorcodefixe-20) |  | PIT Emergency Stop | [All](https://www.amazon.com/s?k=All&tag=errorcodefixe-20) | Pit stop activated | Reset and inspect pit | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | UCM | NEXIEZ | [Unintended car movement](https://www.amazon.com/s?k=Unintended%20car%20movement&tag=errorcodefixe-20) | Safety-critical: call technician |

## Most Common Faults

### Safety Circuit Open
Mitsubishi NEXIEZ and ELENESSA controllers monitor individual safety inputs electronically. The MELTRAC service tool identifies the open contact by name. Door contacts (landing and car gate) are the most frequent failure point. Mitsubishi uses a dual-channel door contact system on newer models - both channels must be healthy.

### Drive Fault (E-series codes)
Mitsubishi elevators use proprietary Mitsubishi Electric FR-series derived inverters. Drive faults display as E0x through E99. Common: E01 (overcurrent), E09 (overvoltage on deceleration - check regenerative resistor), E16 (encoder communication lost). Access the full fault history on the inverter's keypad.

### Door Fault
Mitsubishi uses the door zone sensor and door operator control card to manage door timing. A door fault triggers when the door doesn't close within the allowed time or when the light curtain reverses too many times. Check the sill and interlock mechanism. On older SIGMA series, worn door cam rollers cause repeated reversals.

### Brake Fault
Mitsubishi gearless machines use dual electromagnetic brakes. Each brake has a monitoring switch to confirm engagement and release. A brake fault means the monitoring circuit disagrees with the commanded state. Check the brake contactors, monitoring switch adjustment, and brake coil resistance.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [Door contact (dual-channel)](https://www.amazon.com/s?k=Door%20contact%20(dual-channel)&tag=errorcodefixe-20) | Replace when worn |
| [Door operator card](https://www.amazon.com/s?k=Door%20operator%20card&tag=errorcodefixe-20) | Replace on door logic fault |
| [Brake monitoring switch](https://www.amazon.com/s?k=Brake%20monitoring%20switch&tag=errorcodefixe-20) | Replace on brake fault |
| [FR-series inverter board](https://www.amazon.com/s?k=FR-series%20inverter%20board&tag=errorcodefixe-20) | Replace on persistent E-faults |
| [Encoder](https://www.amazon.com/s?k=Encoder&tag=errorcodefixe-20) | Replace on encoder fault |

## When to Call a Pro
**Mitsubishi elevator systems require licensed elevator mechanics.** MELTRAC software and programming are proprietary to Mitsubishi Electric authorized service personnel. Never bypass safety circuits or ignore UCM faults.

