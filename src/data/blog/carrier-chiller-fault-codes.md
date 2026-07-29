---
title: "Carrier Chiller Fault Codes — Complete Troubleshooting Guide"
description: "Carrier chiller fault codes for 30XA, 30XV, 30HXC, and 19XR series. What each code means and how to fix it."
pubDatetime: 2026-04-27T21:00:00Z
modDatetime: 2026-04-27T21:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - hvac
  - carrier
  - chiller
money_part: "High pressure transducer (R-410A)"
---

Carrier chillers are the workhorses of large commercial and industrial cooling systems — hotels, hospitals, data centers, office towers. When one faults, a building heats up fast. This guide covers the most common fault codes across the **30XA air-cooled scroll**, **30XV variable speed**, **30HXC water-cooled**, and **19XR centrifugal** chiller lines. You'll find alarm numbers, what triggers each fault, the most likely causes, diagnosis steps, and how to reset.

## Jump to Section

- [How Carrier Chiller Alarms Work](#how-carrier-chiller-alarms-work)
- [Accessing Alarm History](#accessing-alarm-history)
- [High Pressure Cutout (Alarm 207 / A100)](#high-pressure-cutout)
- [Low Pressure Cutout / Loss of Charge (A101 / A102)](#low-pressure-cutout)
- [High Discharge Temperature (A103)](#high-discharge-temperature)
- [Oil Pressure Fault (A105)](#oil-pressure-fault)
- [Motor Overload / Excessive Motor Amps (Alarm 208 / 217)](#motor-overload)
- [Compressor Fault / Failure to Start (A110)](#compressor-fault)
- [Communication Fault / Loss of CCN (A120)](#communication-fault)
- [Condenser Fault (A130)](#condenser-fault)
- [19XR-Specific Alarms (200–223 Series)](#19xr-specific-alarms)
- [CCN / BACnet Alarm Table](#ccn-bacnet-alarm-table)
- [Parts Reference Table](#parts-reference-table)

---

## How Carrier Chiller Alarms Work

Carrier chillers use a layered alarm system with two categories:

- **Alarms** — latching faults that shut the chiller down and require a manual reset. The compressor(s) stop and cannot restart until the root cause is corrected and the fault is cleared.
- **Alerts** — warnings that log an event but do not stop the chiller. They indicate a developing condition and should be investigated before they escalate.

On **30XA/30XV/30HXC** units, faults display on the **ComfortLink II** controller (touch screen or keypad) with a numeric alarm code and a text description. The chiller also activates the remote alarm relay output if wired.

On **19XR/19XRV** centrifugal units, alarms display on the **CVC (Chiller Visual Control) / ICVC** panel with a primary message, secondary message, and state code (200–223 and above for protective limits).

For **CCN (Carrier Comfort Network)** and **BACnet** integration, both alarm categories broadcast to the BAS. BACnet point names follow a standard object naming convention; CCN uses point list IDs. Always check the controller display first — the BAS may suppress secondary messages.

---

## Accessing Alarm History

### 30XA / 30XV / 30HXC (ComfortLink II)

1. From the **Main Menu**, select **Service** > **Alarm History**.
2. The controller stores the last 25 alarm events with timestamps, alarm code, and setpoint values at time of trip.
3. Use the scroll keys to review. Each entry shows the condition that triggered it (e.g., actual pressure vs. setpoint limit).
4. To clear active alarms after correcting the fault: **Service** > **Reset Alarms**. Some faults require the controller to be powered down for 30 seconds before the reset clears.

### 19XR / 19XRV (CVC / ICVC)

1. Press the **STATUS** key on the CVC panel.
2. Navigate to **Alarm History** (typically softkey 4 or similar depending on firmware version).
3. The ICVC stores up to 25 fault records with the state, primary message, secondary message, and chiller operating data at the time of fault.
4. To clear: correct the fault condition, then press **RESET** on the panel. Alarms that are still active will not clear — the condition must be resolved first.

---

## High Pressure Cutout

**30XA/30XV/30HXC Alarm:** A100 — HIGH PRESSURE CUTOUT  
**19XR Alarm:** State 207 — PROTECTIVE LIMIT / HIGH CONDENSER PRESSURE  
**Display message:** "High Cond Pressure cutout. [VALUE] exceeded limit of [LIMIT]."

### What Triggers It

The high side refrigerant pressure exceeds the safety cutout setpoint. On 30XA air-cooled units, typical cutout is around 400 psig (R-410A) or 300 psig (R-22). On 19XR water-cooled units, the condenser pressure transducer reading triggers at the configured limit.

### Causes (in order of frequency)

1. **Condenser fouling or airflow restriction** (air-cooled) — dirty coils, blocked discharge, debris on coil face.
2. **High condenser water temperature or low flow** (water-cooled) — cooling tower problems, pump failure, partially closed valve.
3. **Fouled tube bundle** (water-cooled) — scale, biological growth, or deposition reducing heat transfer.
4. **Non-condensables in the refrigerant circuit** — air or nitrogen in the system raises head pressure without increasing refrigerant charge.
5. **Division plate / gasket bypass** (water-cooled) — condenser water bypasses the tube bundle.
6. **Overcharge of refrigerant** — excess liquid floods the condenser.
7. **Bad pressure transducer** — reads high when actual pressure is acceptable.

### Diagnosis Steps

1. Check condenser approach temperature. On water-cooled: approach = condenser leaving water temp minus refrigerant condensing temp. Should be under 5°F. Higher indicates fouling.
2. On air-cooled: check leaving air temperature across coil and inlet air temperature. High differential or high inlet temp (recirculation) causes high head.
3. Verify condenser water flow rate with a flow meter or by checking pump differential pressure.
4. Pull pressure readings from the controller history — compare actual pressure at trip to the setpoint. If the value is well below the limit, suspect a transducer wiring or calibration issue.
5. Check for non-condensables: refrigerant temperature at condenser outlet should match condenser water outlet within a few degrees. If refrigerant temp is much higher, suspect non-condensables.

### Reset Procedure

Correct the root cause first. On 30XA: **Service > Reset Alarms**. On 19XR: press **RESET** on CVC panel. A persistent high pressure fault that resets but trips again within minutes means the root cause has not been resolved.

---

## Low Pressure Cutout

**30XA/30XV/30HXC Alarm:** A101 — LOW PRESSURE CUTOUT; A102 — LOSS OF CHARGE  
**19XR Alarm:** STATE — PROTECTIVE LIMIT / LOW SUCTION PRESSURE  
**Display message:** "Low Evap Pressure cutout" or "Loss of refrigerant charge suspected."

### What Triggers It

The suction (low side) pressure falls below the cutout setpoint. This protects the compressor from running in a starved-refrigerant condition and prevents evaporator freezing.

### Causes (in order of frequency)

1. **Low refrigerant charge** — the most common. Leak somewhere in the circuit.
2. **Evaporator fouling** — reduced chilled water flow or dirty tubes decrease heat transfer, dropping suction pressure.
3. **Low chilled water flow** — undersized pump, partially closed valve, air-bound system.
4. **TXV / EXV malfunction** — expansion valve stuck closed or under-feeding.
5. **Liquid line restriction** — plugged filter-drier, partially closed solenoid.
6. **Suction pressure transducer fault** — reads low when system pressure is normal.

### Diagnosis Steps

1. Record suction pressure and compare to saturation temp on a pressure-temperature chart. If suction sat temp is more than 10°F below chilled water supply temp, suspect undercharge or restriction.
2. Check superheat at the compressor suction. Low superheat suggests evaporator flooding; high superheat confirms starvation (undercharge or TXV issue).
3. Measure chilled water flow rate or compare pump differential pressure to design specs.
4. Inspect filter-drier for pressure drop (measure pressure across it — more than 2 psig drop indicates restriction).
5. Check sight glass for bubbles at full load — bubbles confirm low charge.

### Reset Procedure

Add refrigerant or address the restriction/flow problem. Reset alarms via controller after correcting. Do not repeatedly reset and restart without diagnosing — running a chiller on low refrigerant damages compressors.

---

## High Discharge Temperature

**Alarm:** A103 — HIGH DISCHARGE TEMPERATURE  
**Display message:** "Discharge Temp [VALUE] exceeded limit of [LIMIT]."

### What Triggers It

Compressor discharge gas temperature exceeds the setpoint, typically 225–250°F depending on refrigerant and model. This protects the compressor from overheating, oil breakdown, and valve damage.

### Causes (in order of frequency)

1. **Low suction superheat / refrigerant undercharge** — insufficient refrigerant mass flow raises compression ratio and discharge temp.
2. **High compression ratio** — high condenser pressure combined with low suction pressure.
3. **Liquid injection failure** (on equipped models) — oil cooling or economizer injection not functioning.
4. **Worn compressor internals** — leaking discharge valves re-compress hot gas and raise discharge temp.
5. **Refrigerant contamination** — moisture or non-condensables alter compression characteristics.
6. **Discharge temp sensor fault** — verify with a calibrated contact thermometer at the discharge line.

### Diagnosis Steps

1. Check suction and discharge pressures simultaneously. Calculate compression ratio (absolute discharge / absolute suction). Ratios above 7:1 typically produce high discharge temps.
2. Verify liquid injection or economizer operation if equipped.
3. Compare controller temperature reading to a calibrated field thermometer at the sensor location.
4. Review operating history — is high discharge temp a new symptom or recurring? Gradual degradation suggests worn compressor.

### Reset Procedure

Correct the operating condition. Reset via alarm menu. If discharge temp continues rising immediately after reset, stop the machine — continued operation risks compressor failure.

---

## Oil Pressure Fault

**Alarm:** A105 — OIL PRESSURE DIFFERENTIAL FAULT  
**Display message:** "Oil pressure differential below minimum."

### What Triggers It

The differential between oil pressure and suction pressure falls below the minimum required for lubrication (typically 15–25 psid depending on model). This prevents compressor bearing damage.

### Causes (in order of frequency)

1. **Low oil level in the oil separator** — caused by oil migration into the system.
2. **Plugged oil filter** — restricts oil flow.
3. **Oil pump failure** (on models with dedicated oil pumps).
4. **Oil pressure transducer fault** — bad sensor reading.
5. **Excessive refrigerant dissolved in oil** — dilutes oil viscosity.
6. **Worn oil pump or bypass valve** — internal leakage.

### Diagnosis Steps

1. Check the oil sight glass or oil level indicator on the separator. If low, locate migrated oil and recover it.
2. Check oil pressure directly with a calibrated gauge at the test port and compare to transducer reading.
3. Inspect oil filter — replace if overdue per PM schedule or if differential across it is elevated.
4. Check oil temperature. Cold oil (below 100°F at startup) has high viscosity; ensure oil heater is functional and ran pre-start.

### Reset Procedure

Restore oil level and correct any pump or filter issues. Reset alarm. On 30XA, some oil fault conditions require a 5–15 minute wait before the controller will allow a restart.

---

## Motor Overload

**19XR Alarms:** State 208 — EXCESSIVE MOTOR AMPS; State 217 — MOTOR OVERLOAD TRIP; State 218 — MOTOR LOCKED ROTOR TRIP  
**30XA/30HXC:** Motor Overload via ISM or internal protection

### What Triggers It

Motor current exceeds the overload setpoint. The **Integrated Starter Module (ISM)** on 19XR units monitors motor amps and trips on sustained overload or locked rotor conditions.

### Causes (in order of frequency)

1. **High load conditions** — high head pressure combined with high refrigerant flow.
2. **Low supply voltage** — causes higher current draw at same load.
3. **Phase imbalance** — unequal phase voltages cause motor heating and overload.
4. **Inlet guide vane stuck open** at startup — full load at low speed draws excessive amps.
5. **Motor winding degradation** — partial winding fault increases current.
6. **ISM misconfiguration** — incorrect overload setpoint.

### Diagnosis Steps

1. Check motor current at all three phases with a clamp meter. Compare to nameplate FLA.
2. Measure supply voltage at the starter — check all three phases for balance. More than 2% imbalance requires investigation.
3. On 19XR: review ISM fault history (State 209 Line Phase Loss, State 215/216 imbalance faults often accompany overloads).
4. Verify inlet guide vane (IGV) position at startup — should be near-closed.
5. Check motor insulation with a megohmmeter if repeated overloads suggest winding issue.

### Reset Procedure

Correct the power quality or load condition. Reset via controller. ISM locked rotor faults (State 218) require a manual ISM reset in addition to controller reset.

---

## Compressor Fault

**Alarm:** A110 — COMPRESSOR FAULT / FAILURE TO START  
**30XA specific:** Compressor 1/2/3 fault (individual compressor alarms on multi-circuit machines)

### What Triggers It

The compressor failed to start within the allowed time, or an internal compressor protection (motor winding thermostat, internal pressure relief) tripped.

### Causes (in order of frequency)

1. **High differential pressure at startup** — chiller off on a hot day builds high head; compressor can't unload enough to start.
2. **Contactor failure** — compressor contactor stuck open or welded.
3. **Motor winding thermostat tripped** — overheated motor from previous overload.
4. **Control board output fault** — compressor start signal not being generated.
5. **Crankcase heater failure** — refrigerant migration into oil causes liquid slugging at startup.
6. **Compressor mechanical seizure** — locked rotor from liquid slug or bearing failure.

### Diagnosis Steps

1. Verify crankcase heater operation before blaming the compressor — check heater resistance and confirm it was energized during the off period.
2. Check contactor operation: apply voltage to coil and confirm contacts close with an ohmmeter.
3. Measure motor winding resistance phase-to-phase — compare all three phases. Asymmetry indicates winding fault.
4. Check for locked rotor by trying a manual start with an amp clamp — if amps spike immediately and don't ramp, suspect liquid slug or mechanical lockup.
5. Review oil level — a refrigerant-diluted or migrated oil charge causes slug faults.

### Reset Procedure

Correct root cause. For winding thermostat resets, allow compressor to cool (30–60 minutes). Reset controller alarm. If compressor has tripped on internal pressure relief, do not reset until the system pressure has equalized.

---

## Communication Fault

**Alarm:** A120 — COMMUNICATION FAULT / CCN LOSS  
**Display message:** "Loss of communication with [module]" or "CCN Communication Error."

### What Triggers It

The chiller controller loses communication with a remote module (ISM, expansion board, ComfortLink sensor module) or loses contact with the CCN/BACnet network.

### Causes (in order of frequency)

1. **Wiring fault** — damaged or loose RS-485 communications cable.
2. **Termination resistor missing or misplaced** — CCN networks require 100-ohm termination at each end.
3. **Address conflict** — two devices sharing the same CCN address.
4. **Power supply issue to the remote module** — ISM or expansion board lost power.
5. **Failed control board or communications module** — hardware fault.
6. **Noise on the CCN bus** — VFD or other inductive load injecting noise.

### Diagnosis Steps

1. Check CCN cable continuity between modules — measure resistance on each signal wire.
2. Verify 100-ohm termination at both ends of the CCN bus.
3. Check power supply to the remote module (24 VAC or 5 VDC depending on module type).
4. Check for address conflicts using the controller's network diagnostic menu.
5. Substitute a known-good communications module if hardware fault is suspected.

### Reset Procedure

Correct the wiring or hardware issue. The alarm clears automatically once communication is restored. Some boards require a power cycle to reinitialize the communications stack.

---

## Condenser Fault

**Alarm:** A130 — CONDENSER FAULT (air-cooled specific)  
**Common manifestation:** High pressure cutout on air-cooled units with condenser fan staging.

### What Triggers It

On 30XA air-cooled units, condenser fan motor failures, open circuits, or fan cycling faults can trigger condenser fault alarms.

### Causes (in order of frequency)

1. **Fan motor failure** — burned winding or seized bearing.
2. **Fan blade damaged or missing** — reduced airflow with motor running.
3. **Fan cycling board or pressure control fault** — incorrect staging.
4. **Wiring fault to fan motor** — open circuit or poor connection.
5. **Overcurrent trip on fan circuit breaker** — check all condenser fan circuit breakers.

### Diagnosis Steps

1. Physically inspect all condenser fan motors — verify each fan is spinning and in the correct direction.
2. Measure motor winding resistance and compare to spec (typically 5–50 ohms depending on size).
3. Check fan circuit breakers in the control panel — a tripped breaker is often the simplest root cause.
4. Measure voltage at the motor terminals during operation — verify proper voltage and no single-phasing.

### Reset Procedure

Restore fan operation. Reset alarm via controller. On multi-circuit units, the chiller may continue operating on the unaffected circuit while you diagnose.

---

## 19XR-Specific Alarms (200–223 Series)

The 19XR CVC/ICVC uses state codes 200–223 for Protective Limit faults. Key codes beyond those covered above:

| State | Message | What It Means |
|-------|---------|---------------|
| 200 | 1M Contact Fault | Compressor start contactor (1M) auxiliary contact did not confirm close |
| 201 | 2M Contact Fault | Second winding contactor (2M) aux contact fault |
| 202 | Motor Amps Not Sensed | Current transformers not reading — check CT wiring to ISM |
| 203 | Motor Acceleration Time Fault | Motor didn't reach speed in allowed time — check IGV position and starter |
| 204 | 1M/2M Aux Contact Stop Fault | Contactor aux contact didn't open after stop command |
| 205 | Motor Amps When Stopped | Current flowing through stopped motor — check contactors for welded contacts |
| 206 | Starter Fault Cutout | Optional starter (Benshaw RediStart) tripped — read fault code at starter display |
| 209 | Line Phase Loss | One of three supply phases dropped — check ISM fault history for affected phase |
| 210 | Single Cycle Line Voltage Dropout | Momentary voltage sag — check power quality |
| 211 | High Average Line Voltage | Supply voltage too high — check utility supply and step-down transformer |
| 212 | Low Average Line Voltage | Supply voltage too low — same as above |
| 215 | Line Current Imbalance | Phase current unbalanced by more than threshold — check ISM fault history |
| 216 | Line Voltage Imbalance | Phase voltage unbalanced — check upstream feeder |
| 220 | Ground Fault Trip | Ground fault detected — inspect motor and lead insulation |
| 221 | Phase Reversal Trip | Phase sequence reversed — swap two supply phases at the disconnect |
| 222 | Line Frequency Trip | Supply frequency out of range — check power quality |
| 223 | Starter Module Hardware Failure | ISM internal fault — may require ISM replacement |

---

## CCN / BACnet Alarm Table

Carrier CCN broadcasts alarm status through standardized point addresses. BACnet integration uses Binary Input (BI) and Binary Value (BV) objects. Key points:

| CCN Point | BACnet Object | Description |
|-----------|--------------|-------------|
| ALARM | BI-1 | Master alarm status (any active alarm) |
| ALERT | BI-2 | Alert status (non-latching warnings) |
| HPCO | BI-3 | High pressure cutout active |
| LPCO | BI-4 | Low pressure cutout active |
| HDTA | BI-5 | High discharge temp alarm |
| OILP | BI-6 | Oil pressure fault |
| MOTA | BI-7 | Motor overload alarm |
| COMA | BI-8 | Communication alarm |
| FLTA | BI-9 | Compressor fault |
| CFAN | BI-10 | Condenser fan fault (air-cooled) |

On CCN networks, point ALARM.STAT at the chiller's CCN element address (typically bus 0, element 1–239) reflects the current alarm state. Use the CCN Service Tool or Carrier i-Vu building automation platform to read extended alarm data including the specific fault code and timestamp.

---

## Parts Reference Table

| Part | Application | Part Number (typical) |
|------|-------------|----------------------|
| High pressure transducer (R-410A) | 30XA compressor circuit | HK06NB006 / HK06NB010 |
| Low side pressure transducer | 30XA suction circuit | HK06NB005 |
| Discharge temperature sensor | 30XA/30HXC | HH79NZ039 |
| Suction temperature sensor | 30XA/30HXC | HH79NZ031 |
| Oil pressure differential transducer | 30HXC/30XA scroll | HK06NB008 |
| ComfortLink II main control board | 30XA/30XV | CESO110057-XX |
| ISM (Integrated Starter Module) | 19XR | 06DA660157 (verify by serial) |
| CVC/ICVC display module | 19XR | 33CVCPICVC01 |
| Condenser fan motor (typical 30XA) | 30XA air-cooled | HC68GE460 / HC67GE460 |
| Liquid line filter-drier | All models | E38-2103 (verify by tonnage) |

*Verify part numbers against serial tag and Carrier HVAC Pro Parts lookup before ordering. Part numbers vary by production date and refrigerant type.*

---

## Technician Notes

- **Pre-start checklist on 30XA**: Confirm crankcase heater energized for at least 8 hours before startup, especially after extended off periods. Cold oil with dissolved refrigerant causes compressor damage on first-start.
- **19XR IGV calibration**: A high percentage of "motor acceleration" and "excessive amps" faults trace back to a miscalibrated or sticking inlet guide vane actuator. Test IGV movement manually before chasing electrical issues.
- **Refrigerant logging**: Carrier recommends logging system pressures, superheat, subcooling, and approach temperatures at every PM visit. Trending these values over time catches developing faults before they trip alarms.
- **CCN communication wiring**: Use shielded twisted pair (Belden 8760 or equivalent) for CCN wiring. Ground the shield at one end only. Never run CCN cable in the same conduit as power wiring.
- **BACnet integration**: For IP-based BACnet (BACnet/IP), the ComfortLink II gateway module must be installed and configured. For MS/TP, use the RS-485 port and confirm baud rate matching (typically 9600 or 76.8K baud per site requirement).

## Where to Buy Replacement Parts

Find replacement parts for Carrier chillers on Amazon:

- [Carrier Chiller Parts & Controls](https://www.amazon.com/s?ascsubtag=ecf-carrier-chiller-fault-codes&k=Carrier+chiller+parts&tag=errorcodefixes-20)
- [Carrier Pressure Transducer Replacement](https://www.amazon.com/s?ascsubtag=ecf-carrier-chiller-fault-codes&k=Carrier+HVAC+pressure+transducer&tag=errorcodefixes-20)
- [Carrier Condenser Fan Motor](https://www.amazon.com/s?ascsubtag=ecf-carrier-chiller-fault-codes&k=Carrier+Condenser+Fan+Motor&tag=errorcodefixes-20)
