---
title: "Lennox XP20 Heat Pump Error Codes - Full iComfort Fault Reference"
description: "Complete Lennox XP20 variable-capacity heat pump error code guide. Covers all iComfort-reported fault codes, communicating system diagnosis, and control board replacement."
pubDatetime: 2026-04-25T00:00:00Z
author: "Marcus Webb"
tags:
  - hvac
  - heat-pump
  - lennox
  - error-codes
---

## Lennox XP20 Heat Pump Error Codes

The Lennox XP20 (model series XP20-024 through XP20-060) is a variable-capacity heat pump that runs on the iComfort communicating platform. Every XP20 requires an iComfort Wi-Fi or iComfort S30 thermostat and a communicating indoor unit to operate. The outdoor control board displays fault codes on a 7-segment LED, and those same codes appear on the iComfort thermostat screen.

Fault and lockout codes override normal status codes. If the 7-segment display shows an "E" followed by a number, the system has detected a problem. The table below covers every documented alert code from the XP20 installation and service manual (Corp. 1408-L10).

[Jump to Fix](#fix)

## Complete XP20 Alert Code Table

### Communication Faults

| Code | Severity | Meaning |
|------|----------|---------|
| E 105 | Moderate | Outdoor control lost communication with the thermostat or indoor unit. Typically caused by electrical noise on the RS-bus or loose low-voltage wiring. |
| E 120 | Moderate | Delay in the outdoor unit responding to a system call. Usually clears on its own. |
| E 124 | Critical | iComfort thermostat lost communication with the outdoor unit for more than 3 minutes. All HVAC operations stop until communication returns. |
| E 434 | Critical | Outdoor control lost communication with the inverter board for more than 3 minutes. |

### Control Board and Software Faults

| Code | Severity | Meaning |
|------|----------|---------|
| E 125 | Critical | Hardware failure on the outdoor control board. Replace the board if the fault prevents operation. |
| E 131 | Critical | Outdoor unit control parameters corrupted. Reconfigure the system through the iComfort thermostat. Replace the control if heating or cooling stays unavailable. |
| E 132 | Critical | Internal software error on the outdoor control. Board replacement required. |
| E 443 | Critical | Incorrect appliance unit size code selected during configuration. Reconfigure to match the actual unit tonnage. |

### Sensor Faults

| Code | Severity | Meaning |
|------|----------|---------|
| E 180 | Critical | Outdoor ambient temperature sensor failed. The control board cannot perform low-ambient lockout protection without this sensor. |
| E 416 | Moderate | Outdoor coil sensor failed. Defrost function will not work. The unit keeps running but cannot protect the outdoor coil from ice buildup. |
| E 424 | Moderate | Liquid line temperature sensor failed. Check wiring first, then replace the sensor. |
| E 437 | Critical | Inverter heat sink temperature sensor fault. |

### Reversing Valve Fault

| Code | Severity | Meaning |
|------|----------|---------|
| E 345 | Critical | The "O" relay on the outdoor board failed. The pilot relay contacts did not close, the relay coil did not energize, or the confirmation circuit cannot verify the relay position. This fault prevents the system from switching between heating and cooling modes. A known manufacturing issue involved MOV2 bending into resistor R50 on early production boards, making the control think the reversing valve output was always off. |

### Pressure Switch and Refrigerant Faults

| Code | Severity | Meaning |
|------|----------|---------|
| E 409 | Moderate | Secondary control voltage dropped to 18 VAC or below. Check the transformer and low-voltage wiring. |
| E 410 | Moderate | Low pressure switch opened. The system cycled off on low refrigerant pressure. Check charge level, indoor airflow, and filter condition. |
| E 411 | Critical | Low pressure switch opened 5 times in one hour. System locked out. Almost always a refrigerant leak or severe airflow restriction. Power-cycle to reset, but the underlying cause needs repair. |
| E 412 | Moderate | High pressure switch opened. System shut down on high head pressure. Check for a dirty outdoor coil, failed condenser fan, stuck reversing valve, or overcharge. |
| E 413 | Critical | High pressure switch opened 5 times in one hour. System locked out. Clears only after a power reset. |
| E 422 | Moderate | Compressor top cap thermal switch tripped. The compressor is overheating. |
| E 442 | Critical | Top cap thermal switch tripped 5 times in one hour. System locked out. |

### Inverter Faults

| Code | Severity | Meaning |
|------|----------|---------|
| E 423 | Critical | Inverter detected a circuit-level problem. |
| E 426 | Critical | 10 inverter faults within one hour. Full inverter lockout. |
| E 427 | Critical | DC peak fault detected by the inverter. |
| E 428 | Critical | High main input current detected. Check incoming line voltage. |
| E 429 | Critical | DC link power did not rise high enough on a call for operation. |
| E 430 | Critical | Compressor failed to start. |
| E 431 | Critical | PFC over-current (100A threshold). |
| E 432 | Critical | DC link high voltage detected. |
| E 433 | Critical | Compressor over-current detected. |
| E 435 | Critical | Inverter internal error. |
| E 436 | Critical | Inverter heat sink temperature exceeded its limit. |
| E 438 | Critical | PFC over-current condition detected. |
| E 439 | Moderate | Compressor slowed down because of high input current. System still runs at reduced capacity. |
| E 440 | Moderate | Heat sink temperature approaching its limit. Compressor speed reduced. |
| E 441 | Moderate | Compressor slowed down because of high compressor current. |

### System Protection Codes

| Code | Severity | Meaning |
|------|----------|---------|
| E 600 | Critical | Compressor cycled off by utility load-shedding signal. Normal behavior during demand response events. |
| E 601 | Critical | Outdoor unit cycled off on low-temperature protection. The ambient temperature dropped below the heating operating range. |

## How to Read and Clear Codes {#fix}

1. **Check the 7-segment display.** Open the outdoor unit control panel. The display shows the active code with an "E" prefix. If no fault exists, the display shows the compressor operating percentage or defrost status.
2. **Check the iComfort thermostat.** Navigate to the system alerts screen. The thermostat shows the same fault codes with a plain-language description.
3. **Clear moderate codes.** Most moderate codes clear on their own once the underlying condition resolves. No manual reset needed.
4. **Clear critical lockouts.** Turn off the system at the breaker for 30 seconds, then restore power. The lockout counter resets. If the fault returns within an hour, the root cause still exists.
5. **Recall stored codes.** Press and hold the push-button on the outdoor control board to scroll through the last five stored fault codes. This helps identify intermittent problems.

## Communicating System Diagnosis

The XP20 only works with the iComfort communicating bus. If you see E 105 or E 124 repeatedly, the problem sits in the communication wiring between the thermostat, indoor unit, and outdoor unit.

Check these in order:

- **Wire routing.** The RS-bus communication wire must run separately from high-voltage power wiring. Parallel runs create electrical noise that corrupts data on the bus.
- **Connections.** Inspect every wire nut, terminal block, and plug connector between the three system components. One loose connection drops the whole bus.
- **Line polarity.** The XP20 outdoor control verifies line polarity. Reversed hot and neutral lines generate communication errors. Verify with a multimeter at the disconnect.
- **Software version.** The iComfort Wi-Fi thermostat must run software version 2.1 or higher to communicate with XP20 units. Older firmware versions cause intermittent bus faults.

## Parts Reference

| Part | Where to Find | Notes |
|------|---------------|-------|
| Outdoor control board (103686-06 / 1184-510) | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?ascsubtag=ecf-lennox-xp20-heat-pump-error-codes&tag=errorcodefixes-20) | Fixes E 125, E 131, E 132, E 345. Requires reconfiguration through iComfort after install. |
| Inverter board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lennox-xp20-heat-pump-error-codes&k=Lennox+XP20+inverter+board&tag=errorcodefixes-20) | Fixes E 423 through E 438 inverter faults. Match to unit size (024/036/048/060). |
| Outdoor ambient temperature sensor | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-lennox-xp20-heat-pump-error-codes&tag=errorcodefixes-20) | Fixes E 180. 10K ohm thermistor. |
| Outdoor coil temperature sensor | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-lennox-xp20-heat-pump-error-codes&tag=errorcodefixes-20) | Fixes E 416. Check resistance against spec before replacing. |
| Liquid line temperature sensor | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-lennox-xp20-heat-pump-error-codes&tag=errorcodefixes-20) | Fixes E 424. |
| High pressure switch | [Amazon](https://www.amazon.com/dp/B013IHQ8CU?ascsubtag=ecf-lennox-xp20-heat-pump-error-codes&tag=errorcodefixes-20) | Related to E 412, E 413. Verify the switch itself before assuming a refrigerant problem. |
| Low pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-lennox-xp20-heat-pump-error-codes&tag=errorcodefixes-20) | Related to E 410, E 411. Test switch continuity before replacing. |
| Reversing valve solenoid coil | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lennox-xp20-heat-pump-error-codes&k=Lennox+reversing+valve+solenoid+coil&tag=errorcodefixes-20) | Related to E 345. The relay may be the actual failure point, not the valve itself. |

## When to Call a Pro

Any inverter fault (E 423 through E 443) or repeated pressure switch lockout (E 411, E 413) requires a licensed HVAC technician. Inverter board replacement involves high-voltage DC circuits. Refrigerant leak diagnosis and recharging require EPA Section 608 certification. The XP20 uses R-410A refrigerant with operating pressures that reach 600+ PSI on the high side.

## FAQ

### How do I reset a locked-out Lennox XP20?

Turn off the circuit breaker that feeds the outdoor unit. Wait at least 30 seconds. Restore power. The lockout counter resets and the system attempts to start again. If the same lockout code (E 411, E 413, E 426, or E 442) returns within an hour, the root cause still exists and needs repair before the system will run reliably.

### What does E 345 mean on a Lennox XP20?

E 345 means the reversing valve relay on the outdoor control board failed its self-check. The board energizes the relay and then verifies that the contacts actually closed. If verification fails, the system cannot switch between heating and cooling. Early XP20 production runs had a known issue where a component (MOV2) was bent during factory testing, damaging resistor R50 on the control board. Replacing the outdoor control board fixes this in most cases.

### Can I run the XP20 with a non-communicating thermostat?

No. The XP20 requires an iComfort Wi-Fi or iComfort S30 thermostat. The variable-capacity compressor, defrost logic, and all fault reporting depend on the communicating bus. A standard 24V thermostat cannot control this unit.

### Why does my XP20 keep showing E 410 or E 411?

E 410 (single low-pressure event) and E 411 (five events in one hour, lockout) point to low refrigerant charge in most cases. The R-410A system has a factory charge sized for 15 feet of line set. Longer runs, a slow leak at a flare fitting, or a pinhole in the coil drop the charge below the low-pressure switch setpoint. A technician needs to leak-test the system, repair the leak, evacuate, and recharge to the nameplate specification.

## Related Articles

- [Lennox Furnace Error Codes](/posts/lennox-furnace-error-codes/)
- [Lennox Mini Split Error Codes](/posts/lennox-mini-split-error-codes/)
- [Carrier Heat Pump Error Codes](/posts/carrier-heat-pump-error-codes/)
- [Trane Heat Pump Error Codes](/posts/trane-heat-pump-error-codes/)
- [Goodman Heat Pump Error Codes](/posts/goodman-heat-pump-error-codes/)

## See Also

- [Lennox iHarmony Zoning System Error Codes — Troubleshooting Guide](/posts/lennox-iharmony-zoning-error/)
- [Lennox Error Code 414 — Gas Valve Circuit Fault Fix](/posts/lennox-error-code-414-gas-valve-circuit-fault/)
- [Lennox Error Code 411 — Ignition Proving Fault Fix](/posts/lennox-error-code-411/)
- [Lennox 103 Error Code — Causes & Fix](/posts/lennox-error-code-103/)
