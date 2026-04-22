---
title: "Trane XR95 Furnace Error Codes — Complete Guide"
description: "Trane XR95 furnace error codes: all LED flash codes for the 95% AFUE single-stage XR95, causes, and fixes."
pubDatetime: 2026-04-22T16:00:00Z
modDatetime: 2026-04-22T16:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - trane
---

## Trane XR95 Error Codes — What It Means

The Trane XR95 (model S9X1) is a single-stage, 95% AFUE condensing gas furnace. It uses a standard Trane/American Standard IFC control board with a diagnostic LED that flashes fault codes through the lower access panel. The XR95's high efficiency means it uses a secondary heat exchanger to extract more heat from combustion gases — and that secondary exchanger is a common source of codes not seen on older 80% furnaces.

## Flash Code Quick Reference

| [Flash Code](https://www.amazon.com/s?k=Flash%20Code&tag=errorcodefixe-20) | Meaning | Priority | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ----------- |---------|---------|
| 1 flash | [System lockout (retries exceeded)](https://www.amazon.com/s?k=System%20lockout%20(retries%20exceeded)&tag=errorcodefixe-20) | High |
| [2 flashes](https://www.amazon.com/s?k=2%20flashes&tag=errorcodefixe-20) | Pressure switch stuck open | High | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 3 flashes | High-limit or roll-out switch open | [High](https://www.amazon.com/s?k=High&tag=errorcodefixe-20) |  | 4 flashes | [Ignition failure](https://www.amazon.com/s?k=Ignition%20failure&tag=errorcodefixe-20) | High |
| [5 flashes](https://www.amazon.com/s?k=5%20flashes&tag=errorcodefixe-20) | Flame sensed without call for heat | Critical | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 6 flashes | 115V line voltage fault / bad polarity | [Medium](https://www.amazon.com/s?k=Medium&tag=errorcodefixe-20) |  | 7 flashes | [Gas valve fault](https://www.amazon.com/s?k=Gas%20valve%20fault&tag=errorcodefixe-20) | Critical |
| [8 flashes](https://www.amazon.com/s?k=8%20flashes&tag=errorcodefixe-20) | Low flame sense signal | Medium | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 9 flashes | Igniter circuit fault | [Medium](https://www.amazon.com/s?k=Medium&tag=errorcodefixe-20) |  | Slow blink | [Normal standby](https://www.amazon.com/s?k=Normal%20standby&tag=errorcodefixe-20) | None |
| [Rapid blink](https://www.amazon.com/s?k=Rapid%20blink&tag=errorcodefixe-20) | Normal operation | None | [## Most Common XR95-Specific Issues

### 2 Flashes: Pressure Switch — XR95 Specifics
The XR95 uses a two-stage condensate drain system with a secondary heat exchanger coil. The most common cause of 2-flash codes on XR95 units is a plugged secondary heat exchanger. This shows up as water backing up in the flue trap. The secondary heat exchanger on the XR95 is a coil inside the furnace cabinet — it can plug with mineral scale over 10–15 years of service.

**Check first:** The PVC condensate trap at the bottom of the furnace. If water sits in the trap during operation, the secondary coil drain is restricted. Cleaning the trap and drain tubing resolves most 2-flash faults.

### 3 Flashes: High Limit — XR95 Specifics
The XR95 uses an ECM variable-speed blower motor on some configurations and a standard PSC motor on others. If the blower motor is failing and running at reduced speed, the heat exchanger overheats. On XR95 with ECM motors, a motor that's running but not reaching commanded speed triggers limit faults. Check for a fault code from the ECM motor itself (some have a separate LED or use the board's diagnostic port).

### 4 Flashes: Ignition Failure
The XR95 uses a silicon nitride hot-surface igniter. Typical life is 5–10 years. The igniter glows visible red-orange through the sight glass. If the igniter glows but no flame appears, verify gas pressure and check for a stuck gas valve. If the igniter doesn't glow at all, it's open — measure resistance (should be 40–90 ohms cold).

## Step-by-Step Fix for Code 2 (Most Common)

1. Turn off the furnace at the thermostat and disconnect switch.
2. Locate the condensate trap — white PVC U-trap near the base of the furnace.
3. Disconnect the drain hose from the trap outlet and pour water through. Water should drain freely.
4. If blocked, disassemble the trap by removing the two screws or clips and clean with warm water.
5. Reconnect and restore power. Run a heat cycle and verify the code clears.

## Parts Often Needed](https://www.amazon.com/s?k=%23%23%20Most%20Common%20XR95-Specific%20Issues%0A%0A%23%23%23%202%20Flashes%3A%20Pressure%20Switch%20%E2%80%94%20XR95%20Specifics%0AThe%20XR95%20uses%20a%20two-stage%20condensate%20drain%20system%20with%20a%20secondary%20heat%20exchanger%20coil.%20The%20most%20common%20cause%20of%202-flash%20codes%20on%20XR95%20units%20is%20a%20plugged%20secondary%20heat%20exchanger.%20This%20shows%20up%20as%20water%20backing%20up%20in%20the%20flue%20trap.%20The%20secondary%20heat%20exchanger%20on%20the%20XR95%20is%20a%20coil%20inside%20the%20furnace%20cabinet%20%E2%80%94%20it%20can%20plug%20with%20mineral%20scale%20over%2010%E2%80%9315%20years%20of%20service.%0A%0A**Check%20first%3A**%20The%20PVC%20condensate%20trap%20at%20the%20bottom%20of%20the%20furnace.%20If%20water%20sits%20in%20the%20trap%20during%20operation%2C%20the%20secondary%20coil%20drain%20is%20restricted.%20Cleaning%20the%20trap%20and%20drain%20tubing%20resolves%20most%202-flash%20faults.%0A%0A%23%23%23%203%20Flashes%3A%20High%20Limit%20%E2%80%94%20XR95%20Specifics%0AThe%20XR95%20uses%20an%20ECM%20variable-speed%20blower%20motor%20on%20some%20configurations%20and%20a%20standard%20PSC%20motor%20on%20others.%20If%20the%20blower%20motor%20is%20failing%20and%20running%20at%20reduced%20speed%2C%20the%20heat%20exchanger%20overheats.%20On%20XR95%20with%20ECM%20motors%2C%20a%20motor%20that's%20running%20but%20not%20reaching%20commanded%20speed%20triggers%20limit%20faults.%20Check%20for%20a%20fault%20code%20from%20the%20ECM%20motor%20itself%20(some%20have%20a%20separate%20LED%20or%20use%20the%20board's%20diagnostic%20port).%0A%0A%23%23%23%204%20Flashes%3A%20Ignition%20Failure%0AThe%20XR95%20uses%20a%20silicon%20nitride%20hot-surface%20igniter.%20Typical%20life%20is%205%E2%80%9310%20years.%20The%20igniter%20glows%20visible%20red-orange%20through%20the%20sight%20glass.%20If%20the%20igniter%20glows%20but%20no%20flame%20appears%2C%20verify%20gas%20pressure%20and%20check%20for%20a%20stuck%20gas%20valve.%20If%20the%20igniter%20doesn't%20glow%20at%20all%2C%20it's%20open%20%E2%80%94%20measure%20resistance%20(should%20be%2040%E2%80%9390%20ohms%20cold).%0A%0A%23%23%20Step-by-Step%20Fix%20for%20Code%202%20(Most%20Common)%0A%0A1.%20Turn%20off%20the%20furnace%20at%20the%20thermostat%20and%20disconnect%20switch.%0A2.%20Locate%20the%20condensate%20trap%20%E2%80%94%20white%20PVC%20U-trap%20near%20the%20base%20of%20the%20furnace.%0A3.%20Disconnect%20the%20drain%20hose%20from%20the%20trap%20outlet%20and%20pour%20water%20through.%20Water%20should%20drain%20freely.%0A4.%20If%20blocked%2C%20disassemble%20the%20trap%20by%20removing%20the%20two%20screws%20or%20clips%20and%20clean%20with%20warm%20water.%0A5.%20Reconnect%20and%20restore%20power.%20Run%20a%20heat%20cycle%20and%20verify%20the%20code%20clears.%0A%0A%23%23%20Parts%20Often%20Needed&tag=errorcodefixe-20) | Part | Notes | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------ |-------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Hot-surface igniter | Trane CNT05473 or OEM equivalent | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Condensate trap | Trane CPT0048 or compatible | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Pressure switch | 0.60"–0.80" WC, Trane model-specific | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | IFC control board | CNT05369 or match board label |

## When to Call a Pro
If 3-flash (high limit) or 2-flash codes repeat after cleaning the condensate trap and replacing the filter, a technician should inspect the secondary heat exchanger for scale buildup or damage. Chemical descaling of a plugged secondary coil is a service-level repair.
