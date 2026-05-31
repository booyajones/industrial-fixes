---
title: "Carrier Furnace Error Codes — Complete Guide"
description: "Carrier furnace error codes: all flash codes with meanings, causes, and fixes for every Carrier gas furnace."
pubDatetime: 2026-04-22T16:00:00Z
modDatetime: 2026-04-22T16:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - carrier
---

## Carrier Furnace Error Codes — Quick Reference

Carrier gas furnaces use a blinking LED on the control board to communicate fault codes. Count the flashes in a repeating pattern — the number of blinks identifies the fault. Single-digit codes are common on older IFC boards; newer Carrier Infinity and Performance series use two-digit codes. Pull the furnace door and look through the sight glass or remove the lower access panel to see the LED.

| [Code](https://www.amazon.com/s?ascsubtag=ecf-carrier-furnace-error-codes&k=Code&tag=errorcodefixes-20) | Meaning | Quick Fix |
|------|---------|-----------|
| 11 | No previous fault stored | Normal after power cycle |
| 12 | Blower on after power up / prior to heat | Check blower wheel; verify prior call |
| 13 | Limit device lockout (retries exceeded) | Check filter, airflow, heat exchanger |
| 14 | Ignition lockout (retries exceeded) | Check gas, igniter, flame sensor |
| 21 | Gas heating lockout | Manual reset; check gas pressure |
| 22 | Abnormal flame-proving signal | Clean flame sensor rod |
| 24 | Secondary voltage fuse open | Check for short in low-voltage wiring |
| 25 | Model plug missing or incorrect | Replace/reseat model plug |
| 31 | Pressure switch stuck open | Check inducer, hose, pressure switch |
| 32 | Pressure switch stuck closed | Check pressure switch hose routing |
| 33 | Limit or flame roll-out switch open | Check filter, ducts, roll-out switch |
| 34 | Ignition proving failure | Clean flame sensor; check gas valve |
| 40 | Inducer high-speed fault | Inducer motor issue |
| 41 | Inducer motor fault | Replace inducer motor |
| 42 | Inducer motor fault (secondary) | Verify inducer RPM feedback |
| 43 | Low-voltage control fault | Check transformer and 24V circuit |
| 44 | Blower motor fault | Check blower motor and capacitor |
| 45 | Control board fault | Replace IFC board |
| 46 | Check IFC | Board self-diagnosis fault |
| 52 | Duplicate serial number | IFC/comm setup issue |
| 54 | Soft lockout — low pressure switch open | Pressure switch or inducer fault |
| 58 | Indoor air quality sensor fault | Check IAQ sensor wiring |

## Most Common Codes

### Code 13: Limit Device Lockout
The furnace tried to heat multiple times but the high-limit switch tripped each time. Most often caused by a clogged air filter, closed supply/return registers, or a failing blower motor. Replace the filter first. If that doesn't solve it, check for blocked ducts and verify the blower wheel spins freely.

### Code 14: Ignition Lockout
The furnace failed to establish a flame after the maximum number of ignition attempts. Check that the gas supply valve is open, verify gas pressure (3.5" WC minimum for natural gas), inspect the hot-surface igniter for cracks, and clean the flame sensor rod with fine steel wool or 400-grit sandpaper.

### Code 31: Pressure Switch Stuck Open
The inducer motor started but the pressure switch never closed. Most common causes: cracked pressure switch hose, a clogged condensate drain trap (on 90%+ furnaces), weak inducer motor, or a failed pressure switch itself. Start by inspecting the rubber hose between the inducer and the pressure switch.

### Code 33: Limit or Roll-Out Switch Open
A safety limit opened during operation. On 80% furnaces this usually means airflow is restricted — check the filter and blower. On 90%+ furnaces, also check the secondary heat exchanger. If the roll-out switch tripped, do not reset it until you find the cause — that switch protects against flue gas spillage.

### Code 34: Ignition Proving Failure
The igniter lit the burner but the flame sensor didn't confirm a flame reliably. Clean the flame sensor rod (the single metal rod that sits in the burner flame). If cleaning doesn't fix it, check the microamp signal; healthy flame signal is typically 2–8 µA.

### Code 45: Control Board Fault
The IFC board has diagnosed itself as faulty. Before replacing, verify all wiring connections are tight, there are no shorted low-voltage wires, and the 3-amp fuse on the board is intact.

## When to Call a Pro
If you've reset the furnace and the same code returns immediately, or if codes 21 or 33 involve a tripped roll-out switch, contact a licensed HVAC technician — these situations can indicate cracked heat exchangers or flue gas spillage, which are safety hazards.

## Related Articles

- [Carrier 11 Error Code — Causes & Fix](/posts/carrier-11-error-code/)
- [Carrier 12 Error Code — Causes & Fix](/posts/carrier-12-error-code/)
- [Carrier 13 Error Code — Limit Switch Lockout Fix](/posts/carrier-13-error-code/)
- [Carrier 13 Soft Lockout — What's Different from Hard Lockout](/posts/carrier-13-soft-lockout/)
- [Carrier 14 Error Code — Causes & Fix](/posts/carrier-14-error-code/)

## See Also

- [Carrier 58UX Furnace Error Codes — Flash Code Diagnostic Guide](/posts/carrier-58ux-error-codes/)
- [Carrier Greenspeed Heat Pump Error Codes: Complete Guide](/posts/carrier-greenspeed-heat-pump-codes/)
- [Carrier 33 Error Code — Causes & Fix](/posts/carrier-33-error-code/)
- [Carrier WeatherMaker Rooftop Unit Error Codes: Complete Guide](/posts/carrier-weatheramaker-error-codes/)
