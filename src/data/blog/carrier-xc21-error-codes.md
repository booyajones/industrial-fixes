---
title: "Carrier Infinity XC21 Error Codes — Most Common Faults and Fixes"
description: "Complete guide to Carrier Infinity XC21 error codes, what each fault means, and how to diagnose and fix the most common failures."
pubDatetime: 2026-04-22T14:00:00Z
modDatetime: 2026-04-22T14:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - carrier
money_part: "Low-pressure switch"
most_likely_cause: "Code 11 - Communication loss"
---

## Carrier Infinity XC21 Error Codes — What They Mean

The Carrier Infinity XC21 is a variable-capacity heat pump that communicates with the Infinity control (thermostat) via the ABCD four-wire bus. Unlike simple flash-code systems, the XC21 reports detailed fault codes through the thermostat display. Faults appear as two-digit codes on the Infinity thermostat under the diagnostics menu. The most common codes encountered in the field are covered below.

[Jump to Fix](#fix)

## Most Common XC21 Fault Codes

| Code | Meaning |
|------|---------|
| 11 | No communication from outdoor unit |
| 22 | Low pressure switch open |
| 24 | High pressure switch open |
| 25 | Discharge temp sensor fault |
| 31 | High discharge line temperature |
| 41 | Low-ambient lockout |
| 45 | Control board failure |
| 58 | Compressor protection — high amps |

## Common Causes

- **Code 11 — Communication loss** — Damaged ABCD bus wiring, failed outdoor control board, or failed Infinity thermostat. Check all four ABCD terminals at the outdoor unit and air handler before replacing boards.
- **Code 22 — Low pressure fault** — Low refrigerant charge (leak), restricted filter drier, or failed low-pressure switch. Requires refrigerant gauges to diagnose. Do not ignore — running a heat pump with low charge destroys the compressor.
- **Code 24 — High pressure fault** — Dirty condenser coil, failed condenser fan motor, refrigerant overcharge, or refrigerant flow restriction. High pressure faults on the XC21 are often dirty-coil problems.
- **Code 31 — High discharge temperature** — Compressor working too hard due to low refrigerant, dirty coil, or failed discharge sensor. If discharge temp exceeds ~270°F (132°C), the board locks out.
- **Code 58 — Compressor overamp** — Voltage issues, failing compressor, or inverter drive fault. Measure supply voltage at the contactor; should be within ±10% of nameplate.

## Step-by-Step Fix {#fix}

1. **Read the full fault history** — On the Infinity thermostat, navigate to Menu > Diagnostics > Equipment Faults. Note all active and historical codes — the pattern tells the story (intermittent vs. persistent, indoor vs. outdoor).
2. **For Code 11** — Inspect ABCD wiring at both the outdoor unit terminal block and the air handler board. Confirm no reversed wires, no corrosion, and firm seating. Power cycle both units with a 60-second wait.
3. **For Code 22 or 24** — Connect refrigerant manifold gauges (certified technician required for refrigerant handling). Check subcooling and superheat to confirm charge level and flow. Code 22 on a fully charged system with normal temperatures suggests a failed low-pressure switch.
4. **For Code 31** — Check condenser coil cleanliness from the inside out with a garden hose. Verify condenser fan is spinning at proper speed. Confirm discharge line sensor is seated in its well and not damaged.
5. **For Code 58** — Check supply voltage at the disconnect under load. Low voltage (below 208V on a 230V unit) causes the compressor to draw excess amps. If voltage is good, measure compressor amp draw with a clamp meter — compare to nameplate RLA.
6. **Clear faults and retest** — After repairs, clear the fault history from the Infinity thermostat diagnostics menu and run a complete heating/cooling cycle to confirm no recurrence.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Low-pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-carrier-xc21-error-codes&tag=errorcodefixes-20) \| Replace if Code 22 persists with correct refrigerant charge |
| High-pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-carrier-xc21-error-codes&tag=errorcodefixes-20) \| Replace if Code 24 persists with clean coil and correct charge |
| Condenser fan motor | [Amazon](https://www.amazon.com/dp/B0D2L5NSMM?ascsubtag=ecf-carrier-xc21-error-codes&tag=errorcodefixes-20) \| Replace if not spinning or spinning slow; test capacitor first |
| Outdoor unit control board | [Amazon](https://www.amazon.com/s?k=Outdoor+unit+control+board&tag=errorcodefixes-20) \| For persistent Code 11 or Code 45 after wiring confirmed |
| Discharge temperature sensor | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-carrier-xc21-error-codes&tag=errorcodefixes-20) \| For Code 25 or Code 31 with correct refrigerant conditions |
## When to Call a Pro

Refrigerant diagnosis and handling on the XC21 requires EPA 608 certification. The variable-capacity compressor inverter also requires specialized knowledge — do not attempt to measure inverter output with a standard multimeter. An Infinity-trained Carrier technician can connect to the system via the thermostat diagnostics to see real-time compressor speed, pressures, and temperatures without opening the refrigerant circuit.

## Related Articles

- [Carrier 11 Error Code — Causes & Fix](/posts/carrier-11-error-code/)
- [Carrier 12 Error Code — Causes & Fix](/posts/carrier-12-error-code/)
- [Carrier 13 Error Code — Limit Switch Lockout Fix](/posts/carrier-13-error-code/)
- [Carrier 13 Soft Lockout — What's Different from Hard Lockout](/posts/carrier-13-soft-lockout/)
- [Carrier 14 Error Code — Causes & Fix](/posts/carrier-14-error-code/)

## See Also

- [Carrier 44 Error Code — Causes & Fix](/posts/carrier-44-error-code/)
- [Carrier 24ANA Heat Pump Error Codes — Performance Series Diagnostic Guide](/posts/carrier-24ana-heat-pump-error-codes/)
- [Carrier E22 Error Code - Causes & Fix](/posts/carrier-heat-pump-e22-error-code/)
- [Carrier Error Code 58 — Causes & Fix](/posts/carrier-58-error-code/)
