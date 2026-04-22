---
title: "Scotsman HID312 Error Codes — Fault Code Diagnostic Guide"
description: "Complete guide to Scotsman HID312 ice machine error codes, diagnostic display codes, common fault causes, and step-by-step repair procedures."
pubDatetime: 2026-04-22T23:00:00Z
modDatetime: 2026-04-22T23:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - refrigeration
  - scotsman
  - ice-machine
---

## Scotsman HID312 Error Codes — What They Mean

The Scotsman HID312 is a self-contained cube ice machine and dispenser producing approximately 312 pounds of standard dice-style cube ice per day, with an integrated storage and dispensing unit. It is part of Scotsman's Prodigy Elite series, which features Scotsman's SmartBoard control system. The SmartBoard displays error codes on an LCD panel and tracks service data including cycle counts, clean cycles performed, and fault history.

[Jump to Fix](#fix)

## Scotsman HID312 Error Code Reference

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Fault |
|---|---|
| [1](https://www.amazon.com/s?k=1&tag=errorcodefixe-20) | Long freeze — high water temperature or scale |
| [2](https://www.amazon.com/s?k=2&tag=errorcodefixe-20) | Short freeze — freezing too quickly (possible refrigerant overcharge or TXV fault) |
| [3](https://www.amazon.com/s?k=3&tag=errorcodefixe-20) | Long harvest — ice not releasing properly |
| [4](https://www.amazon.com/s?k=4&tag=errorcodefixe-20) | Short harvest — harvest cycle completing too quickly |
| [5](https://www.amazon.com/s?k=5&tag=errorcodefixe-20) | Harvest temperature not reached |
| [6](https://www.amazon.com/s?k=6&tag=errorcodefixe-20) | High-pressure fault |
| [7](https://www.amazon.com/s?k=7&tag=errorcodefixe-20) | Low-pressure fault |
| [8](https://www.amazon.com/s?k=8&tag=errorcodefixe-20) | Water circuit fault — float switch or inlet valve |
| [9](https://www.amazon.com/s?k=9&tag=errorcodefixe-20) | Freeze temperature sensor fault |
| [10](https://www.amazon.com/s?k=10&tag=errorcodefixe-20) | Harvest temperature sensor fault |
| [11](https://www.amazon.com/s?k=11&tag=errorcodefixe-20) | Bin thermostat fault |
| [12](https://www.amazon.com/s?k=12&tag=errorcodefixe-20) | Dispenser mechanism fault |
| [13](https://www.amazon.com/s?k=13&tag=errorcodefixe-20) | Communication fault — SmartBoard |

## Common Causes by Code

- **Code 1 — Long freeze** — Scale is the dominant cause on HID312 machines. The Prodigy Elite uses an Auto-Alert system to notify when cleaning is due — if the cleaning reminder has been dismissed multiple times without actual cleaning, Code 1 will follow.
- **Code 3 — Long harvest** — A contaminated or damaged curtain switch is the most common mechanical cause. The water curtain hanging over the ice slab at harvest must fall away cleanly; if it sticks or the switch fails to detect its movement, the harvest cycle is extended.
- **Code 6 — High pressure** — Clean the condenser coil. The HID312 condenser is accessible from the front or back depending on the installation type. Check condenser fan motor operation — a failed fan on a dispenser-type machine in a kitchen environment causes high-pressure trips quickly in summer.
- **Code 8 — Water circuit** — The SmartBoard monitors water inlet valve operation and the float switch. If the float valve doesn't open within a set time, Code 8 triggers. Check the inlet valve strainer, solenoid coil, and float switch.
- **Code 12 — Dispenser mechanism** — The integrated dispenser uses a motorized drive to move ice to the dispensing chute. Check for an ice jam in the bin-to-dispenser transition area. Also verify the dispenser auger motor is turning (listen for operation when dispense is triggered).

## Step-by-Step Fix {#fix}

1. **Read the display** — The Scotsman SmartBoard displays the fault code number and a brief description. Navigate to the fault history menu to see how frequently each code has occurred.
2. **For Code 1 (long freeze)** — Enter Clean mode by pressing and holding the Clean button for 3 seconds. Add Scotsman Ice Machine Cleaner (Scotsman Part #19-0996-01) when prompted. Run the full clean cycle, then flush with fresh water.
3. **For Code 3 (long harvest)** — Inspect the water curtain — it should hang straight and swing freely. Test the curtain switch by manually moving the curtain and listening for the click. If the switch doesn't actuate, the contacts have worn or corroded.
4. **For Code 6 (high pressure)** — Clean the condenser. If the condenser fan is running and the coil is clean but high pressure persists, connect manifold gauges — a refrigerant overcharge from a previous service event causes persistent high pressure without an obvious external cause.
5. **For Code 9 or 10 (sensor fault)** — Disconnect the sensor and measure resistance at the board connector. The Scotsman thermistor curve is documented in the service manual — compare measured resistance to the temperature-resistance chart for the ambient temperature of the machine location.

## Parts Often Needed

| Part | Notes |
|---|---|
| [Water curtain switch](https://www.amazon.com/s?k=Water%20curtain%20switch&tag=errorcodefixe-20) | Scotsman-specific micro-switch |
| [Float switch / water level sensor](https://www.amazon.com/s?k=Float%20switch%20%2F%20water%20level%20sensor&tag=errorcodefixe-20) | Check for scale before replacing |
| [Condenser fan motor](https://www.amazon.com/s?k=Condenser%20fan%20motor&tag=errorcodefixe-20) | Match HP and rotation direction |
| [Thermistor sensors](https://www.amazon.com/s?k=Thermistor%20sensors&tag=errorcodefixe-20) | Freeze and harvest sensors; sold as a kit |
| [Dispenser auger motor](https://www.amazon.com/s?k=Dispenser%20auger%20motor&tag=errorcodefixe-20) | Check for ice jam before ordering |
| [SmartBoard](https://www.amazon.com/s?k=SmartBoard&tag=errorcodefixe-20) | For Code 13; verify power supply first |

## When to Call a Pro

Scotsman's SmartBoard can be interfaced with the Scotsman Remote Monitoring system (SRM) for cloud-connected diagnostics. A certified Scotsman service agent has access to the full fault log and can remotely adjust configuration parameters. Refrigerant service requires EPA 608 certification.
