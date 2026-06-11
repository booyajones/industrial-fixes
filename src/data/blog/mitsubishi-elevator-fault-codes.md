---
title: "Mitsubishi Elevator Fault Codes - Complete Guide"
description: "Mitsubishi elevator fault codes for NEXIEZ, ELENESSA, and MELCO systems: common alarms, causes, and diagnostic steps."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - mitsubishi
  - elevator
  - lift
money_part: "Door contact (dual-channel)"
---

## Mitsubishi Elevator Fault Codes - Quick Reference

Mitsubishi Electric elevators (NEXIEZ, ELENESSA, GRANDEUR, Sigma series) use the Mitsubishi VFEM and proprietary control platforms. Fault codes are accessible via the Mitsubishi service tool (MELTRAC) or the controller's LED/LCD panel.

| Fault | System | Meaning | Quick Fix |
|-------|--------|---------|-----------|
| Safety Circuit Open | All | Safety chain open | Check door contacts and limits |
| Door Fault | All | Door open/close failure | Check door operator |
| Drive Fault (E-xx) | NEXIEZ | Drive/inverter alarm | Read inverter fault code |
| Brake Fault | All | Brake monitoring error | Check brake coil |
| Encoder Fault | All | Speed feedback error | Check encoder cable |
| Overload | All | Car overloaded | Check weighing device |
| Terminal Limit | All | Travel limit switch active | Check limits |
| Car Top Emergency Stop | All | Car roof E-stop activated | Reset and inspect |
| PIT Emergency Stop | All | Pit stop activated | Reset and inspect pit |
| UCM | NEXIEZ | Unintended car movement | Safety-critical: call technician |

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
| Door contact (dual-channel) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-elevator-fault-codes&k=Door+contact+%28dual-channel%29&tag=errorcodefixes-20) \| Replace when worn |
| Door operator card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-elevator-fault-codes&k=Door+operator+card&tag=errorcodefixes-20) \| Replace on door logic fault |
| Brake monitoring switch | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-elevator-fault-codes&k=Brake+monitoring+switch&tag=errorcodefixes-20) \| Replace on brake fault |
| FR-series inverter board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-elevator-fault-codes&k=FR-series+inverter+board&tag=errorcodefixes-20) \| Replace on persistent E-faults |
| Encoder | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-elevator-fault-codes&k=Encoder&tag=errorcodefixes-20) \| Replace on encoder fault |
## When to Call a Pro
**Mitsubishi elevator systems require licensed elevator mechanics.** MELTRAC software and programming are proprietary to Mitsubishi Electric authorized service personnel. Never bypass safety circuits or ignore UCM faults.

## Related Articles

- [Mitsubishi City Multi P8 / E6 Error Codes — Causes & Fix](/posts/mitsubishi-city-multi-error-codes/)
- [Mitsubishi PEX City Multi Error Codes (Indoor Unit): Complete Guide](/posts/mitsubishi-city-multi-pex-error/)
- [Mitsubishi CNC Alarm 500 — Causes & Fix](/posts/mitsubishi-cnc-alarm-500/)
- [Mitsubishi CNC Alarm Y96 — Causes & Fix](/posts/mitsubishi-cnc-alarm-y96/)
- [Mitsubishi E1 Error Code — Indoor/Outdoor Communication Fault Fix](/posts/mitsubishi-e1-error-code/)

## See Also

- [Mitsubishi E5 Error Code — Causes & Fix](/posts/mitsubishi-e5-error-code/)
- [Mitsubishi P3 Error Code — Outdoor Coil Thermistor Fix](/posts/mitsubishi-p3-error-code/)
- [Mitsubishi U6 Error Code — Causes & Fix](/posts/mitsubishi-u6-error-code/)
- [Mitsubishi Mini-Split U0 Error Code — Refrigerant Shortage Fix](/posts/mitsubishi-mini-split-u0-error-code/)
