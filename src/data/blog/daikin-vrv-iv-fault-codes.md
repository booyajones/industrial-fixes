---
title: "Daikin VRV IV Fault Codes - Commercial System Diagnostic Guide"
description: "Complete diagnostic guide to Daikin VRV IV fault codes. Covers all major fault categories, zone controller codes, refrigerant circuit diagnosis, and how to use the Daikin service tool for VRF system troubleshooting."
pubDatetime: 2026-04-25T00:00:00Z
author: errorcodefixes.com
tags:
  - hvac
  - error-codes
---

The Daikin VRV IV is one of the most capable commercial variable refrigerant flow (VRF) systems available. It can serve dozens of indoor units from a single outdoor unit bank, providing precise zone-level temperature control in office buildings, hotels, retail spaces, and large residential applications. That complexity comes with a sophisticated diagnostic system — and fault codes that require understanding to use effectively.

This guide covers the Daikin VRV IV fault code system, the most common codes by category, how to read the zone controller display, and how technicians use Daikin's service tool to trace faults to their source.

---

## Understanding the VRV IV Fault Code System

Daikin VRV IV fault codes appear on:
- **Zone controller** (wired remote or BACnet controller)
- **Central controller** (if installed)
- **Daikin Service Tool** (laptop-based diagnostic interface)
- **Outdoor unit LED display** (7-segment codes on the main outdoor unit board)

### Code Format

VRV IV fault codes follow the format: **[Letter][Number]** or **[Number][Letter]**

- **A** series: Indoor unit faults
- **C** series: Sensor faults (thermistors, pressure sensors)
- **E** series: System faults (refrigerant circuit, high/low pressure)
- **F** series: Electrical/inverter faults (outdoor unit)
- **H** series: System operation faults (capacity, startup)
- **J** series: Sensor circuit faults
- **L** series: Control board faults
- **P** series: Protection trip faults (indoor and outdoor unit protection)
- **U** series: System configuration / communication errors

When a fault occurs, all units on the affected refrigerant circuit may display the same code, or only the affected unit will show the code while others display a communication-related secondary code.

---

## Most Common VRV IV Fault Codes by Category

### E-Series — Refrigerant Circuit Faults

**E1** — High Pressure Protection Trip
The discharge pressure has exceeded the high-pressure safety limit (typically 601 PSI / 4.15 MPa for R-410A systems).

*Causes:* Outdoor coil fouled with debris, blocked condenser airflow, non-condensable gases in the refrigerant circuit (air contamination), faulty high-pressure sensor, overcharge.

**E3** — Low Pressure Protection Trip
Suction pressure has dropped below the low-pressure safety limit (typically 43.5 PSI / 0.3 MPa).

*Causes:* Refrigerant undercharge (leak), expansion valve stuck closed, severely restricted liquid line, blocked distributor nozzle.

**E4** — High Pressure Sensor Fault
The high-pressure transducer has failed or gone out of range.

**E5** — Low Pressure Sensor Fault
The low-pressure transducer has failed or gone out of range.

**E6** — Current Sensor Fault
The current sensor monitoring compressor current has failed.

**E7** — Outdoor Fan Motor Fault
The fan motor is not operating within normal parameters. Can indicate bearing failure, motor winding failure, or inverter fault on the fan drive.

**E9** — Electronic Expansion Valve (EEV) Fault
The EEV controlling refrigerant flow to individual indoor units has failed or is not responding to commands.

---

### F-Series — Inverter and Electrical Faults

**F3** — Inverter Discharge Temperature Too High
The inverter module (IPM) has exceeded its thermal limit.

*Causes:* Inadequate heat sink contact, failed thermal paste, blocked ventilation inside outdoor unit, ambient temperature exceeds unit rating.

**F6** — Inverter Board Fault (DC Bus Overcurrent)
The DC bus voltage or current in the inverter circuit is abnormal.

*Causes:* Incoming power quality issue, compressor motor winding fault causing overcurrent, inverter board capacitor failure.

**FA** — Inverter Module (IPM) Fault
The Intelligent Power Module in the inverter has detected an internal fault.

*Causes:* IPM component failure, compressor winding short-circuit, excessive switching frequency under abnormal conditions.

---

### C-Series — Sensor Faults

**C4** — Outdoor Coil Temperature Sensor (Thermistor) Fault
The outdoor unit heat exchanger thermistor is open, shorted, or out of range.

**C5** — Outdoor Discharge Pipe Temperature Sensor Fault
The discharge pipe thermistor has failed.

**C9** — Indoor Unit Thermistor Fault
An indoor unit's return air or pipe thermistor has failed.

---

### L-Series — Control Board Faults

**L3** — Electric Box High Temperature
Temperature inside the outdoor unit electrical box has exceeded the limit. Can indicate a failed fan within the electrical box or blocked venting.

**L4** — Heat Sink Overheating
The inverter heat sink temperature has exceeded limits.

**L5** — Instantaneous Overcurrent (Compressor)
The compressor has drawn an instantaneous overcurrent. Often happens at startup on a compressor with failing windings or during a low-voltage event.

**L8** — Compressor Overcurrent During Operation
The compressor is drawing sustained overcurrent during operation. Differs from L5 in that this happens mid-cycle, not at startup.

**LA** — Inverter Startup Fault
The compressor failed to start within the permitted window after the inverter energized it.

---

### U-Series — Communication and Configuration Faults

**U0** — Refrigerant Insufficient (System Self-Diagnosis)
The VRV IV outdoor unit's self-diagnosis algorithm has determined the refrigerant charge is likely insufficient. This is a calculated estimate based on pressure and temperature data — not a direct measurement.

**U2** — Power Supply Abnormality
Incoming power is abnormal — voltage too high, too low, or voltage imbalance between phases (on 3-phase systems).

**U3** — Transmission Error (Indoor/Outdoor Communication)
Communication between the indoor units and outdoor unit has failed or is unreliable. Often a wiring fault in the communication cable rather than a component failure.

**U4** — Transmission Error (Zone Controller)
Communication between the zone controller and indoor unit(s) has failed.

**U5** — Transmission Error (Central Controller)
Communication between the central controller and the system has failed.

**UA** — Indoor/Outdoor Unit Combination Error
The outdoor unit and one or more indoor units are incompatible. Occurs when units are mixed from incompatible VRV generations or when piping configuration data has been lost.

---

### P-Series — Protection Trips

**P1** — Indoor Unit Fan Motor Protection
The indoor unit fan motor has tripped its protection. Check for debris in the fan or a failing motor.

**P4** — Drain Level Fault
The drain pan float switch has detected water overflow. Drain line blocked, float stuck, or condensate pump failed.

**P5** — Drain Pump Fault
The condensate pump has failed or is not running.

**P8** — Outdoor Unit Heat Exchanger Temperature Abnormality
The outdoor heat exchanger temperature sensor is detecting an abnormal condition during operation.

---

## Zone Controller Fault Display

When a fault occurs, the Daikin zone controller (wired remote) displays the fault code in the temperature display area, often alternating between the code and the current temperature.

**Reading the display:**
1. The display flashes a letter-number combination (e.g., "E3", "U4")
2. The fault code identifies the category and specific fault
3. The zone controller's CHECK button (if present) can cycle through multiple stored faults
4. Some zone controllers display an additional sub-code — a one or two digit number that identifies the specific indoor unit or circuit within the system that triggered the fault

**Clearing codes from the zone controller:** Most Daikin zone controllers require the fault to be resolved before the code clears. Codes can be reviewed in the fault history via the service menu (typically accessed by pressing and holding specific buttons — see the installation and operation manual for your controller model).

---

## Refrigerant Circuit Diagnosis on VRV Systems

VRF system refrigerant diagnosis is more complex than single-split systems because refrigerant is distributed dynamically to multiple indoor units through a branching pipe network. Key diagnostic points:

**Pressure measurement:** On VRV systems, pressure measurements at the outdoor unit service valves provide system-level data. Low suction pressure (E3) indicates either undercharge or a restriction in the liquid line or expansion circuit.

**Sub-cooling and superheat:** The VRV IV uses electronic expansion valves (EEVs) that adjust independently for each indoor unit. Abnormal subcooling at the liquid header or superheat at individual indoor units points to specific EEV or distributor issues.

**U0 — Low Refrigerant Self-Diagnosis:** When U0 appears, this is the outdoor unit's algorithm estimating low charge. It's not infallible — abnormal ambient conditions or a pipe length configuration issue can trigger a false U0. A technician should verify with pressure measurements before recharging.

**Leak detection on VRF systems:** Finding a refrigerant leak in a VRF system is harder than on a single-split because the lineset can span hundreds of feet through walls, ceiling spaces, and branch boxes. A multi-point electronic leak detector sweep combined with system pressure hold tests (nitrogen) is standard practice.

---

## Parts You May Need

| Part | What It Fixes | Amazon Link |
|------|--------------|-------------|
| Daikin VRV Electronic Expansion Valve (EEV) | E9 EEV fault, refrigerant distribution issues | [View on Amazon](https://www.amazon.com/s?k=daikin+vrv+electronic+expansion+valve+replacement&tag=errorcodefixes-20) |
| High/Low Pressure Transducer (Daikin VRV) | E4 / E5 pressure sensor faults | [View on Amazon](https://www.amazon.com/s?k=daikin+vrv+pressure+transducer+sensor&tag=errorcodefixes-20) |
| NTC Thermistor (Daikin VRV outdoor unit) | C4 / C5 thermistor faults | [View on Amazon](https://www.amazon.com/s?k=daikin+vrv+outdoor+unit+thermistor+sensor&tag=errorcodefixes-20) |
| Daikin Wired Zone Controller (BRC1H62) | U4 / U5 zone controller communication fault | [View on Amazon](https://www.amazon.com/s?k=daikin+vrv+wired+zone+controller+brc1h62&tag=errorcodefixes-20) |
| VRF System Refrigerant Manifold Gauge Set | Refrigerant circuit diagnosis on R-410A VRF | [View on Amazon](https://www.amazon.com/s?k=vrf+vrv+refrigerant+manifold+gauge+set+r410a&tag=errorcodefixes-20) |
| Condensate Drain Pan Float Switch | P4 drain level fault | [View on Amazon](https://www.amazon.com/s?k=condensate+drain+pan+float+switch+hvac&tag=errorcodefixes-20) |
| Electronic Refrigerant Leak Detector | Locating refrigerant leaks in VRF lineset | [View on Amazon](https://www.amazon.com/s?k=electronic+refrigerant+leak+detector+vrf&tag=errorcodefixes-20) |

---

## Using the Daikin Service Tool

For VRV IV diagnosis, Daikin's **Service Tool** (PC-based software) provides a level of diagnostic detail not available from the controller display alone:

- **Real-time data logging:** View live pressures, temperatures, EEV positions, fan speeds, and compressor Hz across all units
- **Fault history:** Stored fault codes with timestamps and operating conditions at time of fault
- **Trial operation mode:** Force the system into specific operating conditions for diagnostic purposes
- **Refrigerant charge check:** The tool's refrigerant check function can guide charging based on subcooling values and piping data
- **System configuration verification:** Verify that indoor unit addresses, piping lengths, and elevation data are entered correctly (incorrect piping data causes refrigerant distribution problems that can appear as refrigerant or EEV faults)

The Service Tool connects via a USB-to-serial adapter to the outdoor unit's service port. It requires Daikin's own software (Daikin Installer App or legacy PC service tool), which is available through Daikin's authorized distributor network.

---

## When to Call a Pro

VRV IV service is strictly professional territory. The system requires:

- **EPA 608 certification** for refrigerant handling on R-410A commercial charges (commercial systems often have 50–200+ lbs of refrigerant)
- **Daikin VRV training** — many Daikin distributors require documented training before selling VRV parts
- **Service Tool access** — commercial-grade diagnosis without the Service Tool is guesswork on a complex multi-zone system
- **Proper recommissioning** after refrigerant work — VRV systems require specific leak testing protocols (nitrogen pressure hold, evacuation to <500 microns, and proper refrigerant charging by weight with subcooling verification)

Call a Daikin-authorized VRV technician for:
- Any E or F series fault (refrigerant circuit or inverter)
- U0 low refrigerant diagnosis
- Any fault that returns after reset
- Annual preventive maintenance (coil cleaning, EEV verification, refrigerant circuit check)

---

## FAQ

**Q: Can I reset a VRV IV fault code from the zone controller?**
A: You can attempt a reset from the zone controller by turning the system off and back on. For persistent codes, the outdoor unit may need to be power-cycled at the breaker. Some codes (like U2 power supply faults) won't clear until the underlying condition is resolved.

**Q: My VRV IV shows U3 on all indoor units simultaneously. Is the outdoor unit failed?**
A: Not necessarily — U3 is a communication error, and a single break in the communication wiring (a loose connection at a branch box, a cut wire, or a failed indoor unit PCB) can take down communication to all units downstream. Trace the communication wiring from the outdoor unit forward.

**Q: The VRV IV shows E3 (low pressure) but the system was just recharged. What's wrong?**
A: If E3 appears shortly after a recharge, suspect an EEV problem (expansion valve stuck closed on one or more indoor units), a restriction in the liquid header or distributor, or an incorrect charge amount. Low pressure after a recharge usually means the charge didn't correct the root cause.

**Q: How often should a VRV IV system be serviced?**
A: Daikin recommends annual preventive maintenance by a qualified technician. On commercial systems, semi-annual service (pre-cooling season and pre-heating season) is standard practice. Filter maintenance should be performed per the indoor unit schedule — typically quarterly.

**Q: What's the refrigerant charge capacity of a typical VRV IV system?**
A: A standard VRV IV outdoor unit (REYQ series) charges approximately 20–40 lbs of R-410A depending on the tonnage and piping length. Additional charge is required for extended pipe runs (piping field charge). Total system charge on a large VRV installation can exceed 100 lbs.
