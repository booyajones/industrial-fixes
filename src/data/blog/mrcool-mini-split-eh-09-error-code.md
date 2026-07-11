---
title: "MRCOOL Mini Split EH 09 Error - Causes & Fix"
description: "EH 09 on a MRCOOL mini split signals an auxiliary electric heater problem. Check your manual for the exact fault definition."
pubDatetime: 2026-07-09T08:27:32Z
modDatetime: 2026-07-09T08:27:32Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - mrcool
money_part: "Auxiliary heater relay or contactor"
diy_or_pro: "pro"
free_checks:
  - "Power-cycle the system by turning off the breaker for two minutes, then turning it back on to clear transient faults."
  - "Inspect the indoor unit's wire harness and connectors for loose or corroded terminals, especially those leading to the auxiliary heater."
---

## MRCOOL Mini Split EH 09 Error — What It Means

The EH 09 error code on MRCOOL mini split systems typically relates to the auxiliary electric heating element or its control circuit. Because error code definitions can vary between MRCOOL model families and firmware versions, consult your owner's manual or the wiring diagram on the indoor unit for the exact meaning on your specific model. In general, codes beginning with EH point to issues with electric heat strips, their relays, or the sensors and wiring that protect them from overheating.

The system may continue to provide cooling and heat-pump heating but will disable the auxiliary electric heat function until the fault is cleared. This code is most often seen during cold weather when the heat pump calls for supplemental heat.

## Before You Replace Anything

Homeowners sometimes replace the main control board when the real problem is a failed heater relay or a loose connector at the auxiliary heat element. Check continuity and connections before ordering expensive boards.

[Jump to Fix](#fix)

## Common Causes

- **Faulty heater relay or contactor (~35%)** The relay that switches power to the auxiliary heat element can fail closed, open, or develop arcing contacts that the control board detects as an over-current fault.
- **Failed auxiliary heating element (~25%)** The electric heat strip itself can develop an open circuit or a short to ground, triggering a safety shutdown.
- **Over-temperature sensor trip (~20%)** A high-limit thermostat mounted near the heater element will open if airflow is restricted or the element overheats, and the control board logs an EH fault.
- **Wiring or connector fault (~15%)** Loose, corroded, or damaged wiring between the control board and the heater assembly can create intermittent open circuits or high resistance that the board reads as a heater fault.
- **Control board memory or sensor input error (~5%)** The main control board may log an EH 09 code if it receives out-of-range signals from temperature sensors or if firmware becomes corrupted.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the system still cool and provide normal heat-pump heating without shutting down?</summary>
<div class="dtree-body"><strong>Yes:</strong> The problem is isolated to the auxiliary electric heater circuit. Proceed with checking the heater relay, element, and wiring.<br><strong>No:</strong> The fault may have caused a broader shutdown or there is a separate issue. Call a technician to diagnose the refrigerant circuit and main controls.</div>
</details>

<details class="dtree"><summary>Does the error clear after a full power cycle (breaker off for two minutes, then on)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault may have been transient. Monitor for recurrence and check air filters and airflow to prevent overheating.<br><strong>No:</strong> The fault is persistent. A component in the heater circuit has failed or the board detects a real problem that requires professional diagnosis.</div>
</details>

<details class="dtree"><summary>Can you hear or see the auxiliary heater relay clicking when heat is called for?</summary>
<div class="dtree-body"><strong>Yes:</strong> The relay is attempting to close. Test the heater element for continuity and check for proper voltage at the element terminals.<br><strong>No:</strong> The relay may be stuck open or the board is not sending the close signal. Inspect relay coil voltage and replace the relay if necessary.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off power** at the circuit breaker serving both the indoor and outdoor units and verify no voltage is present at the indoor unit's terminal block.
2. **Remove the front cover** of the indoor air handler to access the control board, wiring harness, and auxiliary heater assembly.
3. **Locate the auxiliary heater element** and its relay or contactor, usually mounted in the lower plenum or a separate heater box downstream of the evaporator coil.
4. **Check all wire connections** to the heater element, relay, and any over-temperature sensors for tightness, corrosion, or burn marks.
5. **Use a multimeter** to test continuity across the heater element terminals (should read a few ohms when cold) and verify the high-limit thermostat is closed at room temperature.
6. **Test the heater relay** by measuring coil resistance and checking for continuity across the load contacts when the relay is energized.
7. **Inspect the control board** for error code history or fault indicators, and consult the service manual to determine if the board requires replacement or if a sensor needs adjustment.
8. **Reassemble the unit**, restore power, and monitor operation through a full heating cycle to confirm the fault is cleared and the auxiliary heat engages properly.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Auxiliary heater relay or contactor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mrcool-mini-split-eh-09-error-code&k=Auxiliary+heater+relay+or+contactor&tag=errorcodefixes-20) \| Match the coil voltage and contact rating to your model's wiring diagram. |
| Electric heating element | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mrcool-mini-split-eh-09-error-code&k=Electric+heating+element&tag=errorcodefixes-20) \| Order by your indoor unit's model and serial number to make sure correct wattage and mounting. |
| High-limit thermostat (over-temperature switch) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mrcool-mini-split-eh-09-error-code&k=High-limit+thermostat+%28over-temperature+switch%29&tag=errorcodefixes-20) \| Verify the trip temperature matches your original sensor. |

## When to Call a Pro

Call a licensed HVAC technician if you are not comfortable working with line-voltage wiring or if the error persists after basic checks. Troubleshooting electric heater circuits requires testing live voltage at relay contacts and heater terminals, which poses a shock hazard. A technician has the tools to measure current draw, verify proper staging of the heat strips, and interpret fault logs stored in the control board. If the control board itself is suspect, professional diagnosis will save the cost of replacing a board that may not be the root cause.

**Rough cost:** A pro service call runs about $180-400.
