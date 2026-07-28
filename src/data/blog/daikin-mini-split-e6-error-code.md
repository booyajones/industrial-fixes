---
title: "Daikin E6 Error Code - Causes & Fix"
description: "E6 means compressor overcurrent or mechanical lock. Usually a failed inverter board or power supply voltage imbalance. Requires testing."
pubDatetime: 2026-06-30T09:51:23Z
modDatetime: 2026-06-30T09:51:23Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - hvac
  - mini-split
  - daikin
money_part: "Daikin outdoor unit inverter board (PCB)"
most_likely_cause: "defective outdoor unit PCB (inverter board)"
likelihood: "often cited as the weak link in modern Daikin systems"
diy_or_pro: "pro"
---

## What this code means
The Daikin E6 error code indicates the standard compressor has detected an overcurrent condition or a mechanical lock during operation. The system measures compressor current draw (typically 5.1 A to 15 A for standard compressors) and throws E6 when the current exceeds the normal range or the compressor cannot rotate freely. This is strictly a compressor power or lock fault, not a communication error (unlike some other brands where E6 means communication failure).

The fault can stem from a mechanical problem inside the compressor itself, a defective outdoor inverter board misreading the current sensor, or an unbalanced power supply causing one phase to spike. In rare cases on VRF systems it can also indicate refrigerant shortage or expansion valve issues, but on standard mini-splits it is almost exclusively a compressor overcurrent or lock fault.

## Before You Replace Anything

Many technicians replace the compressor when the inverter board is actually at fault. The isolation test (disconnecting the wire on the secondary side of the magnetic switch and powering on) shows whether the board or the compressor is responsible. If E6 persists with the compressor disconnected, the board is defective.

## Common Causes

- **Outdoor unit PCB (inverter board) failure (~40%)** The inverter board is defective and failing to supply the correct drive signal or is misreading the current sensor circuit, falsely reporting overcurrent.
- **Voltage unbalance between phases (~25%)** The power supply has an unbalanced voltage (difference of 14 V or more between phases), causing current to spike on one phase and trigger the overcurrent protection.
- **Compressor mechanical seizure or motor coil short (~20%)** The compressor is locking up due to mechanical failure inside the unit or has a shorted motor winding, drawing excessive current.
- **Earth fault or short circuit in compressor wiring (~10%)** A ground fault or short in the wiring between the magnetic switch and the compressor is causing current leakage or a false reading.
- **Refrigerant shortage or stop valve not opening (~5%)** Low refrigerant charge or a closed stop valve causes the compressor to overwork and draw excessive current (less common in standard mini-splits).

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Do the indoor unit lights flicker or is voltage unstable at your breaker panel?</summary>
<div class="dtree-body"><strong>Yes:</strong> A voltage unbalance or supply problem may be the cause. Call an electrician to measure phase voltage at the outdoor unit before replacing any HVAC parts.<br><strong>No:</strong> The fault is likely internal to the outdoor unit. Proceed with the isolation test to separate the inverter board from the compressor.</div>
</details>

<details class="dtree"><summary>Does the outdoor unit fan spin and hum but the compressor stays silent?</summary>
<div class="dtree-body"><strong>Yes:</strong> The compressor may be mechanically locked. A technician must perform a mega test and check compressor windings for shorts or opens.<br><strong>No:</strong> The system may be shutting down on overcurrent before the compressor starts. The inverter board or current sensor is the likely culprit.</div>
</details>

<details class="dtree"><summary>Has the error appeared immediately after installation or service work?</summary>
<div class="dtree-body"><strong>Yes:</strong> Check that the stop valves are fully open and that all wire connections at the magnetic switch and compressor terminals are tight. A missed valve or loose wire is a common installer error.<br><strong>No:</strong> The fault developed during normal operation. Focus on the inverter board and power supply voltage checks.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off power** to the outdoor unit at the breaker and wait 5 minutes for the compressor to fully stop and capacitors to discharge.
2. **Measure voltage** on the primary side of the magnetic switch with a multimeter. Compare all three phases (if three-phase) or line-to-line and line-to-neutral (if single-phase). If the voltage difference between any two phases is 14 V or greater, the power supply is unbalanced. Contact the utility company to repair the grid supply before proceeding.
3. **Check for earth faults** by turning the outdoor unit back on and measuring voltage on the secondary side of the magnetic switch. If voltage is balanced but the error persists, perform a mega test (insulation resistance test) on the wiring and compressor windings to detect ground faults.
4. **Isolate the PCB from the compressor** by turning the outdoor unit off, disconnecting the wire on the secondary side of the magnetic switch, then turning the unit back on. If the E6 code still appears with the compressor disconnected, the fault is in the operating current sensor circuit or the outdoor unit PCB. Replace the inverter board.
5. **Test compressor windings** (if E6 cleared in the previous step) by measuring resistance between the three compressor terminals. Check for balanced resistance (usually within 1-2 ohms of each other) and verify no terminal reads zero ohms to ground. An open, shorted, or grounded winding means compressor replacement.
6. **Verify refrigerant charge and stop valves** if all electrical tests pass. Confirm the stop valves are fully open (stems backed out) and check suction and discharge pressures against the manufacturer's table for your outdoor temperature. Low charge can cause the compressor to labor and draw high current.
7. **Replace the identified component** (inverter board, compressor, or repair wiring) and restore power. Clear the error code from the indoor unit controller and run the system through a full heating and cooling cycle to confirm the repair.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Daikin outdoor unit inverter board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-mini-split-e6-error-code&k=Daikin+outdoor+unit+inverter+board+%28PCB%29&tag=errorcodefixes-20) \| Match the exact model number stamped on your existing board. Often labeled as the power module or IPM board. |
| Daikin compressor (replacement) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-mini-split-e6-error-code&k=Daikin+compressor+%28replacement%29&tag=errorcodefixes-20) \| Required only if windings test open, shorted, or grounded. Must match tonnage and refrigerant type. Includes oil charge. |

## When to Call a Pro

Call a licensed HVAC technician immediately. The E6 error involves high-voltage work, refrigerant system diagnostics, and compressor testing that require EPA certification and specialized tools (mega tester, inverter analyzer, refrigerant gauges). The isolation test and voltage checks are not safe for homeowners without electrical training. Misdiagnosis is common because the symptoms of a bad inverter board and a locked compressor overlap. A qualified tech will perform the step-by-step isolation protocol to avoid replacing a working compressor when the board is at fault, or vice versa. If the power supply is unbalanced, coordinate with an electrician before any HVAC repairs.

**Rough cost:** A pro service call runs about $200-600.
