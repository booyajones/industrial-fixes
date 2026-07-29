---
title: "Carrier VRF Error Codes (38VM/40VM) Fault Code Guide"
description: "Real Carrier VRF fault codes for 38VM outdoor, 40VM indoor and MDC units. Decode 0E, 0H, 0P, SE and E-series errors with likely causes and fixes."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - carrier
  - vrf
  - commercial-hvac
---

# Carrier VRF System Error Codes: Complete Guide

Carrier VRF systems (sold under the Carrier and Midea-sourced product lines) display fault codes on the indoor unit wired remotes, the outdoor unit LED panel, and the i-Vu building automation interface. This guide covers all common Carrier VRF fault codes.

## How Carrier VRF Codes Are Displayed

- **Wired remote (UTY-RNNUM or Carrier branded):** Error code displayed on screen
- **Outdoor unit LED:** Seven-segment display on the main board shows fault code
- **i-Vu / CCN:** Alphanumeric codes in the fault log

## Carrier VRF Error Code Table

### Communication / System Faults

| Code | Description | Common Cause |
|---|---|---|
| E01 | Indoor/outdoor communication fault | Check F1/F2 wiring |
| E02 | Outdoor unit PCB fault | Replace outdoor main board |
| E03 | Phase detection fault | Check 3-phase power supply |
| E04 | High-pressure protection | Dirty condenser, overcharge |
| E05 | Low-pressure protection | Low refrigerant, airflow issue |
| E06 | Discharge temperature high | Low refrigerant, TXV fault |
| E07 | Compressor overload | Check compressor amps |
| E08 | Fan motor fault — outdoor | Fan motor or inverter board |
| E09 | Electronic expansion valve fault | EEV coil or wiring |
| E10 | Heat exchanger sensor fault | Check condenser/evap sensor |

### Indoor Unit Faults

| Code | Description | Common Cause |
|---|---|---|
| I01 | Indoor PCB fault | Replace indoor control board |
| I02 | Indoor communication fault | Check F1/F2 wiring to indoor unit |
| I03 | Indoor fan motor fault | Motor or capacitor |
| I04 | Freeze protection trip | Low refrigerant, dirty filter |
| I05 | Drain level fault | Blocked drain, condensate pump |
| I06 | Indoor temperature sensor fault | Check sensor resistance |
| I07 | Pipe temperature sensor fault | Check liquid/suction pipe sensors |

### Protection / Lockout Faults

| Code | Description | Common Cause |
|---|---|---|
| F01 | Hard lockout — high pressure | 3 HP trips — manual reset |
| F02 | Hard lockout — low pressure | 3 LP trips — manual reset |
| F03 | Hard lockout — discharge temp | 3 high-temp trips — manual reset |
| F04 | Compressor lockout | Compressor protection activated |

## Most Common Carrier VRF Faults

### E01 — Communication Fault
The most common VRF fault. Check:
1. F1/F2 wiring at every indoor unit — ensure tight connections
2. Total wire length does not exceed system maximum (typically 1000m)
3. No reverse polarity in the communication circuit
4. Address switches on all indoor units are unique

### E04 — High Pressure
1. Check condenser coil and clean if dirty
2. Verify all condenser fans are operating
3. Check refrigerant charge (subcooling)
4. Check for non-condensables if system was opened

### I04 — Freeze Protection Trip
1. Replace dirty indoor filter
2. Check indoor fan operation
3. Check refrigerant superheat — should be 8–15°F
4. Inspect indoor coil for ice

### E09 — EEV Fault
Electronic expansion valve faults are common after refrigerant work:
1. Check EEV coil resistance (typically 40–60 ohms per winding)
2. Check wiring harness connections
3. Check for mechanical blockage (debris in EEV)

## Carrier VRF Parts Reference

| Part | Notes |
|---|---|
| [Electronic expansion valve](https://www.amazon.com/s?ascsubtag=ecf-carrier-vrf-error-codes&k=Electronic+expansion+valve&tag=errorcodefixes-20) | Model-specific — match kv and connection |
| [Outdoor main PCB](https://www.amazon.com/s?ascsubtag=ecf-carrier-vrf-error-codes&k=Outdoor+main+PCB&tag=errorcodefixes-20) | Match model and firmware version |
| [Indoor PCB](https://www.amazon.com/s?k=Indoor+PCB&tag=errorcodefixes-20) | Indoor unit-specific |
| [Communication wire](https://www.amazon.com/s?ascsubtag=ecf-carrier-vrf-error-codes&k=Communication+wire&tag=errorcodefixes-20) | Unshielded 2-conductor — match gauge for run length |
| [Temperature sensor](https://www.amazon.com/s?ascsubtag=ecf-carrier-vrf-error-codes&k=Carrier+Temperature+sensor&tag=errorcodefixes-20) | 10K NTC thermistor |
| [Inverter module (IPM)](https://www.amazon.com/s?ascsubtag=ecf-carrier-vrf-error-codes&k=Inverter+module+%28IPM%29&tag=errorcodefixes-20) | High-value outdoor part |

> **Note:** Some Carrier VRF product lines are manufactured by Midea. Technical service manuals are available via Carrier's commercial partner portal. Always verify with the model number before ordering parts.

## More Carrier Vrf fault codes

Compiled from manufacturer service manuals and authorized documentation.

| Code | What it means | Likely cause | How to fix |
| --- | --- | --- | --- |
| 0E0 | Communication fault between outdoor units (appears on the slave/follower unit only) | Incorrect ODU address dial setting (ENC1), P/Q communication wiring between outdoor units open, shorted or reversed, or a damaged main board / communication terminal block. | Power off the ODUs. Verify ENC1 addressing (0 header, 1/2 followers). Check and re-land the P/Q bus between outdoor units for continuity and polarity, then re-power. Replace the main board if wiring checks good. |
| 0E1 | Open phase for outdoor unit | Loss of one leg of the 3-phase supply, a blown fuse, loose power terminal, or open circuit breaker feeding the ODU. | Measure all three legs at the ODU power terminal block. Correct the missing phase, tighten terminals and replace any failed fuse or breaker before restarting. |
| 0E2 | HR system: communication fault between outdoor unit and MDC. HP system: communication fault between outdoor unit and indoor units | Break, short or reversed polarity on the P/Q transmission bus to the MDC (heat recovery) or to the indoor units (heat pump), or a loose signal terminal. | Trace the P/Q communication line from the ODU to the MDC or indoor units. Repair opens/shorts, confirm correct polarity, and reseat terminals. |
| 0E4 | Temperature sensor error - T3 / T3A / T3C / T4 (condenser and outdoor ambient sensors) | Open or shorted thermistor, disconnected sensor plug, or out-of-range resistance on the outdoor coil (T3/T3A/T3C) or ambient (T4) sensor. | Locate the flagged sensor, check its resistance against the sensor table, reseat the connector, and replace the thermistor if the reading is open or shorted. |
| 0E5 | Voltage protection | Supply voltage outside the allowed window (high or low), voltage imbalance across phases, or DC bus voltage out of range. | Verify incoming voltage and phase balance against nameplate. Correct utility/wiring issues; do not run until voltage is within spec. |
| 0E6 | DC fan error (outdoor) | Failed outdoor DC fan motor, faulty DC fan drive board, obstructed fan, or a loose motor connector. | Check the fan for free rotation and obstructions, inspect the fan drive board and motor connections, and replace the motor or DC fan drive board as needed. |
| 0E7 | Discharge temperature sensor error - T5 | Open, shorted or dislodged T5 discharge thermistor on the compressor. | Check T5 resistance and connector at the interface (I/F) board; reseat or replace the discharge sensor. |
| 0E8 | Incorrect ODU address | ENC1 outdoor address dial set to an invalid value or duplicated between outdoor units. | Set ENC1 to 0 on the header unit and 1/2 on followers; confirm no duplicates, then power cycle. |
| 0E9 | EEPROM error (outdoor main board) | Corrupt or failed EEPROM / main control board memory. | Power cycle the unit; if the fault persists, replace the outdoor main control board with the correct model/firmware. |
| 0H5 | Low pressure protection | Low refrigerant charge, restricted or closed service valve, EEV stuck closed, dirty filter/coil on indoor units, or evaporator airflow loss. | Confirm all service valves are open, check charge and subcooling, verify indoor airflow and EEV operation, and repair any leak before recharging. |
| 0H6 | Discharge temperature protection | Low refrigerant charge, high compression ratio, EEV problem, or restricted refrigerant flow driving discharge temperature too high. | Check charge and superheat, verify EEV operation and that all valves are open, and inspect for flow restrictions before restarting. |
| 0H7 | Quantity of indoor units found by the ODU/MDC does not match the quantity set at the ODU main board | IDU quantity dialed on the ODU (ENC3 + S12) does not equal the number of indoor units actually communicating, or an indoor unit dropped offline. | Recount connected indoor units and set ENC3 + S12 to match. If an IDU has failed, correct its wiring or temporarily reduce the count until it is repaired. |
| 0H8 | High pressure sensor (H-YL1) error | Open/shorted high-pressure transducer or a loose sensor connection. | Check the H-YL1 transducer wiring and reading against actual pressure; reseat or replace the sensor. |
| 0HB | Low pressure sensor (L-YL1) error | Open/shorted low-pressure transducer or a loose sensor connection. | Check the L-YL1 transducer wiring and reading against actual pressure; reseat or replace the sensor. |
| 0F6 | Fault in electronic expansion valve (outdoor) | Open EEV coil winding, disconnected valve harness, or a mechanically stuck valve. | Check EEV coil resistance and the harness connector; reseat and replace the coil or valve body if the winding is open or the valve is stuck. |
| 0F8 | MDC (multiport distribution controller) malfunction | Fault reported by the MDC or loss of communication/control between the ODU and MDC. | Read the MDC's own display for an SE/SP code, check the MDC power and P/Q wiring, and address the underlying MDC fault. |
| 0P1 | Current leakage, or discharge-temperature switch / high pressure protection | Ground/current leakage detected, or the mechanical discharge temp switch / high-pressure switch has tripped (dirty condenser, overcharge, blocked airflow). | Check for compressor/wiring ground faults; clean the condenser, verify fan operation and charge, and confirm the pressure switch resets before restarting. |
| 0P2 | Low pressure protection | Low charge, closed valve, EEV or airflow restriction, similar to 0H5 but tripped as a hard protection. | Verify open service valves, charge, subcooling and indoor airflow; find and correct the cause of low suction pressure. |
| 0P3 | Over-current protection of compressor | Compressor drawing excessive current from overcharge, high head pressure, mechanical binding, or a failing inverter/compressor. | Measure compressor amps against spec, check charge and head pressure, and inspect the compressor inverter board; replace the failed component. |
| 0P4 | Discharge temperature protection | Discharge temp exceeded the protection limit due to low charge, EEV fault or restricted flow. | Check charge, superheat and EEV operation; clear any restriction before returning the unit to service. |
| 0PL | Inverter module temperature (Tf1, Tf2, or Tf3) protection | IPM/inverter module overheating from poor heatsink contact, high ambient, fan loss, or a failing power module. | Confirm outdoor fans run, clean the heatsink and verify thermal paste/mounting, check ambient conditions, and replace the inverter (IPM) board if it continues to overheat. |
| 0L0 | Fault in compressor module | Inverter/IPM drive fault, compressor winding fault, or loss of the U/V/W connection to the compressor. | Check U/V/W wiring and compressor winding resistance/balance, inspect the inverter module, and replace the failed inverter board or compressor. |
| 0L7 | Phase loss protection for the 3-phase U, V, W cables at the compressor | One of the U/V/W compressor leads is open, loose, or wired incorrectly after board/compressor service. | De-energize, verify all three U/V/W leads are tight and correctly landed, and confirm winding continuity before restarting. |
| SE0 | MDC: communication error with outdoor unit | P/Q transmission wiring between the MDC and ODU is open, shorted or reversed, or the MDC lost power. | Check MDC power and the P/Q bus back to the ODU for continuity and polarity; reseat the signal terminal block. |
| SEP | MDC: float switch error | Condensate float switch tripped or open circuit on the MDC drain float. | Clear the blocked drain, verify the condensate pump, and check/replace the float switch. |
| SCER | MDC: commissioning test failure | Refrigerant piping and communication wiring for a port do not correlate, or a port-check/commissioning test did not complete correctly. | Re-run the MDC commissioning/port-check test, correct any mismatched piping-to-wiring port assignments, then re-commission. |
| E1 | Indoor unit: communication error with outdoor unit | P/Q signal wiring from the indoor unit to the ODU/MDC is broken, shorted or reversed, or the IDU address is unset/duplicated. | Check the indoor P/Q connections and polarity, confirm a unique IDU address, and repair the transmission run. |
| EB | Indoor unit: expansion valve error | Open indoor EEV coil, disconnected valve harness, or stuck valve. | Check the indoor EEV coil resistance and connector; reseat and replace the coil or valve if faulty. |
| EE | Indoor unit: water level alarm (condensate float switch) | Condensate not draining - blocked drain line, failed condensate pump, or stuck float switch. | Clear the drain, confirm the condensate pump runs, and test/replace the float switch. |
| FE | Indoor unit: no address set for the indoor unit | The IDU was powered up without a communication address assigned. | Assign the IDU address from the wired/wireless controller (or let auto-addressing complete), then confirm the count matches the ODU setting. |
| FP | Wired controller: the online number of indoor units overflows (too many IDUs in group control) | More indoor units are grouped to a single wired controller than it supports (group control is typically limited to 16 IDUs). | Reduce the number of indoor units grouped to the wired controller to within its allowed limit. |

## How to troubleshoot Carrier Vrf

Carrier VRF systems (the 38VM outdoor / 40VM indoor family, built on the Toshiba-Carrier / Midea platform) report faults with a letter-plus-number scheme that tells you which device is complaining before you ever open a panel. Read the prefix first: codes shown at the outdoor unit begin with 0 (0E-, 0H-, 0F-, 0P-, 0L-), codes at a heat-recovery MDC begin with S (SE-, SP-) or read as "no"/"CS", and codes at an indoor unit or wired controller are the short E-series (E1-E9), plus FE, DD, EB, ED and EE. The same underlying problem often surfaces as different codes on different displays, so note every device that is alarming, not just the first one you see.

Start with the cheap, common causes before condemning a board. The single most frequent VRF fault family is communication (0E0, 0E2, SE0, E1): these are almost always a P/Q transmission-bus problem, not a dead control board. Check the two-wire signal bus for opens, shorts and reversed polarity, confirm every terminal is tight, verify the outdoor address dials (ENC1) and the indoor-unit quantity dials (ENC3 + S12) match the actual count, and make sure each indoor unit has a unique address. A miscounted or dropped indoor unit shows up as 0H7. Sensor codes (0E4, 0E7, 0F3-0F5, E2-E5) are usually an open or shorted thermistor or an unseated plug - measure resistance against the service-manual sensor table and reseat before replacing.

Pressure and temperature protections (0H5/0P2 low pressure, 0P1 high pressure, 0H6/0P4 discharge temp) point at the refrigeration circuit, not the controls: confirm all service valves are fully open, check charge, subcooling and superheat, clean the condenser coil, verify all outdoor fans spin, and confirm indoor airflow and EEV operation. Inverter and compressor faults (0PL, 0L0, 0L7, 0P3) involve high-voltage IPM/inverter boards and the compressor itself - verify the U/V/W leads are correct and tight, check for overheating and heatsink contact, and measure compressor winding balance. On these systems the fastest diagnosis path is Carrier's Service Technical Tool (STT), which connects to the P/Q bus and displays live pressures, temperatures, EEV positions and the full error history.

Safety and scope: this is commercial three-phase equipment with high-voltage DC bus capacitors that stay charged after power-off. Disconnect power and wait at least ten minutes, then confirm the DC bus voltage has bled down before touching any board. Refrigerant work requires EPA certification and manufacturer training, and the diagnostic and commissioning tools are proprietary. Homeowners and general handypeople should treat any VRF code beyond a blocked condensate drain (EE) or a mis-set address as a call to a Carrier-authorized VRF service technician - a wrong charge or a mis-wired inverter board on these systems is an expensive mistake.

## Frequently asked questions

### What is the most common Carrier VRF error code?

Communication faults are by far the most common. On the outdoor unit these show as 0E0 or 0E2, at the MDC as SE0, and at an indoor unit as E1. They almost always trace to the two-wire P/Q signal bus - an open, short or reversed-polarity connection, a loose terminal, or a wrong/duplicate address dial setting - rather than a failed control board. Check wiring and addressing first.

### My Carrier VRF indoor unit shows E1. What does it mean?

E1 is a communication error between that indoor unit and the outdoor unit. Confirm the P/Q signal wiring to the indoor unit is intact and correctly polarized, that the terminals are tight, and that the indoor unit has a unique address set (an unaddressed unit shows FE instead). Repair the transmission run or re-address the unit.

### What does a low pressure protection code (0H5 or 0P2) point to?

Low-side pressure has dropped below the protection threshold. The usual causes are a low refrigerant charge or a leak, a service valve left closed, a stuck expansion valve, a dirty indoor filter or coil, or loss of indoor airflow. Confirm all service valves are fully open, check charge and subcooling, and verify indoor airflow before recharging - find the leak rather than just topping off.

### Can I clear a Carrier VRF fault code myself?

You can safely handle the simple ones - clear a blocked condensate drain for an EE water-level alarm, or correct an address/quantity dial setting for FE, 0E8 or 0H7. Anything involving refrigerant pressure, the compressor, or the inverter (IPM) boards should go to a Carrier-authorized VRF technician. These are high-voltage, three-phase systems with a charged DC bus, and they require EPA certification and Carrier's Service Technical Tool for proper diagnosis.

### What tool do technicians use to diagnose Carrier VRF systems?

Carrier's Service Technical Tool (STT). It connects to the system's P/Q communication bus and displays live data - pressures, temperatures, EEV positions, compressor speeds - plus a complete error-code history to help pinpoint whether a fault is wiring, a sensor, the refrigeration circuit, or a board.
