---
title: "ABB ACS580 Fault Codes — Complete Diagnosis & Fix Guide"
author: "Industrial Error Code Fixes"
pubDatetime: 2026-04-24T22:40:00Z
modDatetime: 2026-04-24T22:40:00Z
slug: abb-acs580-fault-codes
featured: false
draft: false
tags:
  - abb
  - vfd
  - industrial
  - fault-codes
  - overcurrent
description: "ABB ACS580 fault codes complete guide — 2310 overcurrent, 3130 input phase loss, 3210 DC overvoltage, 4110 heatsink overtemp, 7121 fan feedback fault. Step-by-step fixes and parts table."
---

## ABB ACS580 VFD Fault Codes — Complete Guide

The **ABB ACS580** is ABB's general-purpose all-compatible drive, widely used in water and wastewater (pumps, fans, blowers), HVAC, food and beverage, and general industrial applications. It covers output power from 0.75 to 250 kW (1 to 300 HP) in 208–240V and 380–480V configurations. The ACS580 features ABB's direct torque control (DTC) technology, a built-in panel display (ACS-AP-I), and an Ethernet/IP adapter option.

When the ACS580 detects a fault, it stores the fault code in the **Fault logger** (menu **Primary settings → Reset & diagnostics → Fault logger**) and halts the drive with a coast-to-stop. Faults are numbered using ABB's standard convention — the four-digit code (e.g., **2310**) maps to a specific fault type across most ABB drive families. Alarms (non-tripping warnings) are numbered separately and end in A.

[Jump to Fix](#step-by-step-fix)

## ACS580 Fault Code Quick Reference

| Fault Code | Name | Short Description |
|------------|------|-------------------|
| 2310 | Output overcurrent | Output current exceeded 200% of drive rated current |
| 2330 | Earth fault | Ground fault detected on motor or output cable |
| 3130 | Input phase loss | One of the three input phases is missing or severely unbalanced |
| 3210 | DC link overvoltage | DC bus exceeded maximum (usually 800–900 VDC for 480V drives) |
| 3220 | DC link undervoltage | DC bus below minimum operating level |
| 4110 | Heatsink overtemperature | Heatsink exceeded maximum temperature (typically 115°C) |
| 4290 | Overtemperature (internal) | Ambient or internal drive temperature exceeded limit |
| 5010 | DC overvoltage | DC link overvoltage (alternative/legacy code) |
| 6310 | Panel loss | Control panel communication lost (ACS-AP-I disconnected or cable broken) |
| 7121 | Fan feedback fault | Internal cooling fan failed or fan feedback signal lost |
| 7510 | Communication fault | Fieldbus communication loss (EtherNet/IP, PROFIBUS, etc.) |
| 9300 | External fault 1 | Digital input programmed as external fault was activated |
| 9301 | External fault 2 | Second external fault input activated |
| FA81 | Safe Torque Off (STO) | STO function activated — safety circuit opened |

## Common Causes

- **2310 (Overcurrent)** — Typically caused by too-fast acceleration ramp, a motor winding fault, a short in the motor cable, or a mechanically jammed load. The ACS580 also trips 2310 if the motor parameters (motor nominal current, motor type) are set incorrectly — an inflated nominal current setting disables the internal current limit at the wrong level.
- **3130 (Input phase loss)** — A blown input fuse or failed contactor contact on one phase is the most common cause. Also occurs when the utility supply is unbalanced by more than ±3%. The ACS580 monitors input phase balance continuously; even brief phase loss during a thunderstorm or utility event can trigger this fault.
- **3210 (DC link overvoltage)** — Caused by a high-inertia load decelerating into the DC bus faster than the drive can handle. Extending the deceleration ramp (reduce the **Deceleration time** in **Primary settings → Speed control**) resolves most cases. If the application requires fast braking, a **Brake chopper** option (factory-installed or plug-in) with an external braking resistor is required.
- **4110 (Heatsink overtemp)** — The ACS580 is designed for 40°C (104°F) ambient at full load. Above 40°C, the drive must be derated per ABB's derating tables. Common causes: dusty cabinet filter blocking airflow to heatsink, internal cooling fan failure, or stacking multiple drives too close together without adequate forced ventilation.
- **7121 (Fan feedback fault)** — The ACS580 monitors its internal cooling fan speed via a tachometer feedback circuit. If the fan stops or slows below a threshold, 7121 is generated. A failed fan is a serious fault — the drive will overheat within minutes if this is ignored.
- **9300 (External fault)** — One of the digital inputs is configured to act as an external fault input. A field device (motor PTC thermistor, flow switch, level switch) wired to this input has activated. Trace the wiring and check the associated process instrument.

## Step-by-Step Fix {#step-by-step-fix}

1. **Read the fault code and value.** On the ACS-AP-I panel, navigate to **Primary settings → Reset & diagnostics → Fault logger**. This shows the fault code, name, time stamp, and the auxiliary value — a number that encodes additional context (e.g., for fault 2310, the auxiliary value indicates when during the cycle the overcurrent occurred: 0 = acceleration, 1 = constant speed, 2 = deceleration).

2. **For 2310 (Overcurrent):**
   - Check when the fault occurs (acceleration, constant speed, or deceleration) using the fault auxiliary value.
   - **During acceleration:** Increase the acceleration time (parameter **23.12** or via the Quick Setup wizard). Double the current setting as a starting point.
   - **During constant speed:** Check for a sudden load change or mechanical jam. Manually rotate the driven load. Check motor winding resistance and megohm test (see below).
   - **At startup:** Disconnect the motor and test the output terminals (T1/U1, T2/V2, T3/W3) with a megohm tester at 500V. Phase-to-ground should be >1 MΩ; phase-to-phase should be >1 MΩ. Anything lower indicates motor or cable fault.
   - Verify motor data in **Primary settings → Motor → Motor nominal data** — especially **Motor nominal current** (matches motor nameplate FLA exactly).

3. **For 3130 (Input phase loss):**
   - Measure input voltage at R/L1, S/L2, T/L3 terminals with a true-RMS multimeter while the drive is powered.
   - Check that all three input fuses are intact (use a continuity tester or resistance measurement with power off).
   - Check the input contactor — a single chattering contact can cause intermittent 3130 faults that are difficult to replicate.
   - If phase voltages are within 2% of each other, check parameter **30.15** (Phase loss detection mode) — it may be overly sensitive for the supply characteristics. ABB Technical Support can advise on appropriate settings for weak utility areas.

4. **For 3210 (DC link overvoltage):**
   - Extend the deceleration ramp: navigate to **Primary settings → Speed control** (or **Ramps** in the full parameter list, typically 23.13 Decel time 1). Increase the value until 3210 stops tripping.
   - If the application requires fast braking (conveyor with heavy inertia, hoist, winder), a braking resistor is required. The ACS580 has an optional internal brake chopper (suffix **+D150** in the catalog number) — if not present, a separate BCU-02 braking chopper unit is needed.
   - Verify that the DC bus voltage feedback is correct: check parameter **01.11** (DC link voltage). If this reads implausibly high at idle, the voltage measurement circuit may have failed.

5. **For 4110 (Heatsink overtemp):**
   - Check parameter **01.10** (Heatsink temperature) — this is the measured heatsink temperature in °C. A reading at or above the trip limit (typically 115–120°C) confirms a real overtemp event.
   - Power down and inspect/clean the heatsink fins (accessible from the bottom of the drive or via the side air channels). Use compressed air to blow out accumulated dust.
   - Check and, if necessary, **replace the internal cooling fan** — see parts table below. The fan is accessible by removing the drive cover.
   - Verify the drive's installation space: minimum clearances are 75 mm above, 75 mm below, and 50 mm on each side. If drives are side-mounted in a row, check ABB's mounting instructions for shared-wall restrictions.

6. **For 7121 (Fan feedback fault):**
   - Confirm the fault by checking parameter **01.10** (Heatsink temperature) — if rising rapidly, the fan has definitely stopped.
   - Power the drive down safely, wait 15 minutes for cooling, then power it back on in a cool environment. If 7121 returns immediately, the fan has failed.
   - Replace the cooling fan (see parts table). The ACS580 fan is a standard IP54 axial fan that slides out from the bottom of the drive enclosure after removing one or two screws — replacement takes under 10 minutes.

7. **For FA81 (Safe Torque Off):**
   - FA81 is not a hardware failure — it means the machine's safety relay has opened the STO circuit.
   - Verify that both STO input channels (typically XSTO pins 1–4 on the control board) have the correct 24VDC present.
   - If STO is being triggered by a safety PLC or safety relay (e.g., a light curtain or e-stop), identify and resolve the safety event first before resetting the drive.
   - Check parameter **31.22** (STO function mode) to confirm the STO response is set appropriately for your application.

## Parts Often Needed {#parts-often-needed}

| Part | Description | Typical Cost | Where to Buy |
|------|-------------|--------------|--------------|
| ACS580 cooling fan assembly | Frame-specific fan (R0–R9) — match to drive frame size on nameplate | $80–$250 | [Amazon](https://www.amazon.com/s?i=industrial&k=ABB+ACS580+cooling+fan+replacement&tag=errorcodefixes-20) \| ABB distributor |
| ACS-AP-I control panel | Standard operator panel for ACS580 (also fits ACS380, ACS480, ACS880) | $150–$220 | [Amazon](https://www.amazon.com/s?i=industrial&k=ABB+ACS-AP-I+control+panel&tag=errorcodefixes-20) \| ABB distributor |
| Input line fuses (fast-acting, class J) | Size per drive input current rating (A) | $10–$50/set | [Amazon](https://www.amazon.com/s?i=industrial&k=ABB+VFD+input+fuse+class+J+fast+acting&tag=errorcodefixes-20) |
| External braking resistor | Sized per ABB braking resistor selection guide | $100–$500 | [Amazon](https://www.amazon.com/s?i=industrial&k=ABB+VFD+braking+resistor+external&tag=errorcodefixes-20) \| ABB distributor |
| Output dV/dt filter | Protects motor insulation on long cable runs (>50m) — reduces 2310 nuisance trips | $200–$600 | [Amazon](https://www.amazon.com/s?i=industrial&k=ABB+dV+dt+filter+VFD+output&tag=errorcodefixes-20) \| ABB distributor |
| ACS580 replacement drive | Full drive unit — select by catalog number from drive nameplate | $600–$6,000 | ABB local distributor |

## When to Call a Professional

Fault **2310** that returns immediately after clearing, with a confirmed-good motor and cable, indicates a failed output IGBT in the drive's power stage. ABB ACS580 power stages are not field-serviceable — the drive requires replacement or factory repair. ABB's drives business offers an **ABB DriveService** exchange program where a failed drive is replaced with a refurbished unit — this is often faster and less expensive than waiting for a new drive.

For drives managing critical processes (water treatment pumps, hospital HVAC, food production), ABB recommends maintaining a spare drive on the shelf. The ACS580 supports **auto-copy** of parameters to an SD card inserted in the panel — this means a replacement drive can be programmed in under 5 minutes by inserting the parameter SD card and selecting "Restore from SD card."

> **Pro tip:** ABB's free **Drive composer** PC software (downloaded from ABB's website) connects to the ACS580 via a standard USB cable and provides real-time monitoring, trend logging, and full parameter access. For fault analysis, the **Data logger** function in Drive composer captures motor current, voltage, speed, and torque at 1 ms resolution — triggered by a fault event. This waveform data is essential for diagnosing intermittent overcurrent faults and for separating load-induced faults from drive hardware faults.

## See Also

- [ABB ACS580 Fault 3130 — Input Phase Loss](/posts/abb-acs580-fault-3130/)
- [ABB ACS880 Fault 2310 — Overcurrent](/posts/abb-acs880-fault-2310-overcurrent/)
- [ABB ACS550 F0001 Overcurrent](/posts/abb-acs550-f0001-overcurrent/)
- [ABB VFD Fault 3210 — DC Overvoltage](/posts/abb-vfd-fault-3210/)
- [ABB VFD Fault Codes Complete Guide](/posts/abb-vfd-fault-codes/)

## Related Articles

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS310 Fault 3130 — Causes & Fix](/posts/abb-acs310-fault-3130/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)
