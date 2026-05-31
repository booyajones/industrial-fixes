---
title: "Lennox Harmony III Zoning System Error Codes — Complete Guide"
description: "Lennox Harmony III zoning system error codes: fault codes for the HCC3-8 zone control center, damper issues, thermostat faults, and fixes."
pubDatetime: 2026-04-22T19:00:00Z
modDatetime: 2026-04-22T19:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - lennox
  - zoning
---

## Lennox Harmony III Error Codes — Quick Reference

The Lennox Harmony III zoning system uses the HCC3-8 zone control center (or HCC3-4 for four-zone applications) to manage up to eight conditioned zones. The system communicates with iComfort or conventional thermostats via a 24VAC bus and controls motorized zone dampers. Fault codes appear on the control center LED display or via service mode on connected iComfort thermostats.

| Code | Meaning | Quick Fix |
|------|---------|-----------|
| E01 | Zone 1 thermostat communication fault | Check zone 1 thermostat wiring |
| E02 | Zone 2 thermostat communication fault | Check zone 2 thermostat wiring |
| [E03–E08](https://www.amazon.com/s?ascsubtag=ecf-lennox-harmony-iii-error-codes&k=E03%E2%80%93E08&tag=errorcodefixes-20) | Zone 3–8 thermostat faults | Check individual zone wiring |
| E10 | Zone control center power fault | Verify 40VA transformer; check wiring |
| E20 | Damper actuator fault — zone 1 | Test damper motor; check 24VAC |
| [E21–E28](https://www.amazon.com/s?ascsubtag=ecf-lennox-harmony-iii-error-codes&k=E21%E2%80%93E28&tag=errorcodefixes-20) | Damper actuator faults — zones 2–8 | Test individual damper actuators |
| E30 | Bypass damper fault | Check bypass damper actuator |
| E40 | Equipment output fault | Verify furnace/AHU wiring at HCC3 |
| E50 | Control board internal error | Power-cycle; replace HCC3 if persists |
| E99 | System reset required | Hold RESET button for 5 seconds |

## Most Common Faults

### E01–E08 — Zone Thermostat Communication Faults
Each zone thermostat communicates to the HCC3 over a two-wire bus. A communication fault on any zone typically points to a wiring issue: broken R or C wire, loose terminal connection, or a failed thermostat. Inspect the low-voltage wiring at the thermostat and at the HCC3 terminal block. If one zone consistently faults, swap the thermostat temporarily to isolate whether the issue is the thermostat or the wire run.

### E20–E28 — Damper Actuator Faults
The Harmony III uses 24VAC spring-return damper actuators. An actuator fault means the HCC3 commanded a damper to open or close but didn't receive confirmation within the timeout period. Check the actuator wiring connections at both the damper motor and the HCC3. Apply 24VAC directly to the actuator's power terminals to verify the motor moves. Replace the actuator if it doesn't respond to direct power.

### E30 — Bypass Damper Fault
The bypass damper maintains safe static pressure when only one or two zones are calling. An E30 fault means the bypass damper actuator is not responding. Locate the bypass damper (usually in a main supply trunk near the air handler) and test its actuator independently. A stuck bypass damper can cause dangerously high static pressure and damage the furnace heat exchanger over time.

### E10 — Power Fault
The HCC3 requires a reliable 24VAC supply from a dedicated transformer. If the transformer is undersized (less than 40VA) or if additional damper loads were added to the system, voltage can sag. Measure 24VAC at the HCC3 R and C terminals under full load. If voltage drops below 19VAC, replace or upsize the transformer.

### E40 — Equipment Output Fault
The HCC3 is sending a call for heating or cooling to the equipment (furnace, air handler, or heat pump) but is not receiving confirmation. Check the Y, W, and G wiring at the HCC3 output terminals. Verify the jumper settings on the HCC3 match your equipment type (conventional vs. heat pump, single-stage vs. two-stage).

## System Configuration Notes

- Harmony III supports up to 8 zones with the HCC3-8; up to 4 zones with the HCC3-4
- Works with Lennox iComfort S30/E30 thermostats and conventional 24VAC thermostats
- Requires 40VA minimum transformer; 75VA recommended for 6+ zone systems
- Zone dampers must be Lennox-approved spring-return actuator type

## When to Call a Pro
E50 (internal board error) and persistent E40 faults often require a Lennox-certified technician who can access the iComfort diagnostic interface to read detailed system logs.

## Related Articles

- [Lennox Error Code 292 — Ignition Failure Fix](/posts/lennox-292-error-code/)
- [Lennox EL296V Error Codes — Variable-Speed Furnace Diagnostic Guide](/posts/lennox-el296v-error-codes/)
- [Lennox Elite Series Furnace Error Codes — Fault Code Diagnostic Guide](/posts/lennox-elite-series-furnace-codes/)
- [Lennox 103 Error Code — Causes & Fix](/posts/lennox-error-code-103/)
- [Lennox Error Code 111 — Causes & Fix](/posts/lennox-error-code-111/)

## See Also

- [Lennox Error Code 327 — Causes & Fix](/posts/lennox-error-code-327/)
- [Lennox Error Code 540 — Communicating System Fault (Detailed Guide)](/posts/lennox-error-code-540-communicating/)
- [Lennox Error Code 332 — Causes & Fix](/posts/lennox-error-code-332/)
- [Lennox Error Code 125 — Causes & Fix](/posts/lennox-error-code-125/)
