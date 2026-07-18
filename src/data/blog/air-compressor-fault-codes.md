---
title: "Air Compressor Fault Codes: Atlas Copco, Kaeser, IR"
description: "Decode air compressor fault codes for Atlas Copco, Kaeser, and Ingersoll Rand. Real controller codes, likely causes, and how to fix each one."
pubDatetime: 2026-04-22T23:00:00Z
modDatetime: 2026-04-22T23:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - industrial
  - compressors
  - troubleshooting
---

## Air Compressor Fault Codes — How to Use This Guide

Air compressor fault codes vary by brand, but the root causes are usually familiar: high discharge temperature, low oil pressure, motor overload, sensor failure, or drive faults. This page is a hub designed to help technicians narrow the problem before diving into the model-specific manual.

[Jump to Fix](#fix)

## Common Air Compressor Fault Categories

| Fault Type | Typical Meaning |
|---|---|
| [High discharge temperature](https://www.amazon.com/s?ascsubtag=ecf-air-compressor-fault-codes&k=High+discharge+temperature&tag=errorcodefixes-20) | Cooling issue, low oil, dirty cooler |
| [Low oil pressure](https://www.amazon.com/s?ascsubtag=ecf-air-compressor-fault-codes&k=Low+oil+pressure&tag=errorcodefixes-20) | Oil pump issue, low oil, pressure switch fault |
| [Motor overload](https://www.amazon.com/s?ascsubtag=ecf-air-compressor-fault-codes&k=Motor+overload&tag=errorcodefixes-20) | High mechanical load, voltage issue, starter/VFD problem |
| [Sensor fault](https://www.amazon.com/s?ascsubtag=ecf-air-compressor-fault-codes&k=Sensor+fault&tag=errorcodefixes-20) | Pressure, temperature, or transducer out of range |
| [Emergency stop / safety trip](https://www.amazon.com/s?ascsubtag=ecf-air-compressor-fault-codes&k=Emergency+stop+%2F+safety+trip&tag=errorcodefixes-20) | E-stop chain, high pressure, separator issue |
| [VFD fault](https://www.amazon.com/s?ascsubtag=ecf-air-compressor-fault-codes&k=VFD+fault&tag=errorcodefixes-20) | Overcurrent, undervoltage, overtemperature |

## Common Causes Across Brands

- **High temperature** — Dirty aftercooler, blocked inlet filter, failed cooling fan, or low oil.
- **Low pressure / low output** — Air leak, inlet valve failure, worn airend, or wrong pressure setpoint.
- **Motor overload** — Tight airend, bad bearings, unbalanced voltage, or blocked separator.
- **Frequent shutdowns** — Short cycling due to poor pressure band settings or undersized storage.

## Step-by-Step Fix {#fix}

1. **Read the exact code and subsystem** — Controller display plus any starter or VFD alarms.
2. **Check basics first** — Oil level, inlet filter, coolers, ventilation, and supply voltage.
3. **Verify load/unload behavior** — Make sure the compressor is not hunting between states.
4. **Inspect sensors and transducers** — Many modern compressor faults are bad feedback, not true mechanical failure.
5. **Review trend data if available** — Controller history often shows temperature rise or pressure drift before shutdown.

## Brands Covered on ErrorCodeFixes

- Atlas Copco
- Ingersoll Rand
- Kaeser
- Sullair
- Gardner Denver
- Boge
- CompAir
- FS-Elliott

## When to Call a Pro

If the compressor shows repeated airend, oil pressure, or drive faults, stop resetting it and bring in a compressed air technician. Running a screw compressor through repeated trips can turn a manageable repair into a full airend failure.

## Related Articles

- [Atlas Copco Air Compressor Fault Codes — Complete Guide](/posts/atlas-copco-compressor-fault-codes/)
- [BOGE Air Compressor Error Codes - Complete Guide](/posts/boge-compressor-error-codes/)
- [Chicago Pneumatic Compressor Fault Codes — Complete Guide](/posts/chicago-pneumatic-compressor-faults/)
- [CompAir Air Compressor Fault Codes - Complete Guide](/posts/compair-compressor-fault-codes/)
- [Copeland Compressor Error Code 1 — High Pressure Cutout Fix](/posts/copeland-compressor-error-code-1/)

## More Air Compressor fault codes

Compiled from manufacturer service manuals and authorized documentation.

| Code | What it means | Likely cause | How to fix |
| --- | --- | --- | --- |
| 0004 A | Kaeser SIGMA CONTROL 2: EMERGENCY STOP control device actuated (shutdown). | The emergency-stop push-button has been pressed, or the E-stop safety chain is broken. | Clear the hazard, then unlatch/reset the emergency-stop push-button and acknowledge the fault on the controller before restarting. |
| 0013 A | Kaeser SIGMA CONTROL 2 'Motor I': Overload shut-down of the compressor drive motor. | The drive-motor overload tripped from excessive current (tight airend, clogged separator, low voltage, or a failing motor). | Investigate the cause of the shutdown, reset the overload, and check the oil separator cartridge and supply voltage before restarting (manual specifically calls out changing the oil separator cartridge). |
| 0015 A | Kaeser SIGMA CONTROL 2 'ADT': Maximum permissible airend discharge temperature (ADT) exceeded. | Cooling is inadequate: low cooling-oil level, a dirty/blocked cooler, or high ambient temperature. | Keep ambient conditions within specified limits, clean the cooler, and check the cooling-oil level before resetting. |
| 0038 A | Kaeser SIGMA CONTROL 2 'PD T': Package discharge (PD) temperature too low. | Package/compressed-air temperature dropped below the allowable minimum (e.g. cold ambient). | The Kaeser manual directs you to contact an authorized KAESER service representative; check the temperature sensor and its wiring if the reading looks implausible. |
| 0039 A | Kaeser SIGMA CONTROL 2 'PD T': Package discharge (PD) temperature too high. | Insufficient package cooling: low cooling-oil level, dirty radiator/cooler, or a failing fan motor. | Check the cooling-oil level, clean the radiator, and verify the fan motor operates. |
| 0043 A | Kaeser SIGMA CONTROL 2 'ADT dT/dt': The rate of rise of the airend discharge temperature (ADT) is too fast. | A sudden loss of cooling or lubrication is driving the airend temperature up abnormally quickly. | Check the cooling-oil level and cooler; inspect for loss of oil flow before restarting. |
| ERR.01 | Ingersoll Rand X-series (X8i) controller: Pressure Sensor Fault. | The control pressure-sensor signal is out of range (below 3.5 mA or above 21.8 mA), typically a failed transducer or wiring fault. | Inspect the pressure-sensor wiring and connector, then test or replace the transducer to bring the signal back within range. |
| ERR.05 | Ingersoll Rand X-series (X8i) controller: Emergency Stop. | The wire link between terminals '+C' and 'C1' of the controller is open circuit (E-stop pressed or safety chain broken). | Clear the hazard, release the E-stop, and restore the +C to C1 link/safety-chain continuity. |
| SYS.01 | Ingersoll Rand X-series (X8i) controller: Excess Pressure (PM) - system pressure exceeded the maximum limit. | System pressure rose above the configured maximum, e.g. a stuck-loaded compressor or a failed inlet/blowdown valve. | Check for a compressor stuck on load, verify inlet and blowdown valve operation, and confirm the pressure setpoints. |
| SYS.02 | Ingersoll Rand X-series (X8i) controller: Min Pressure (Pm) - system pressure fell below the minimum limit. | Demand exceeds supply or a compressor failed to load, so pressure dropped under the minimum setpoint. | Check for air leaks, confirm compressors are loading, and verify capacity meets demand. |
| 0x1111 | Atlas Copco GA VSD (Neos drive) Main Motor Converter Alarm: Undervoltage. | Main power-supply voltage too low or missing links in the control panel. | Check the main supply voltage against specification and inspect panel fuses and control-panel links/connectors. |
| 0x2312 | Atlas Copco GA VSD (Neos drive) Main Motor Converter Alarm: Motor Overcurrent (overcurrent detected at motor side). | Overcurrent on the motor side of the converter, often loose control connectors or a drive/motor fault. | Check for loose connectors at the converter control unit and the Elektronikon, and inspect the motor and drive. |


## How to troubleshoot Air Compressor

## How to diagnose an air compressor fault the right way

Rotary screw and reciprocating compressors trip for a small number of recurring reasons, and the controller code almost always points at one of them: temperature, pressure, motor/drive current, or a sensor out of range. Work the problem in order rather than resetting and hoping.

**1. Read the exact code and its class first.** Most industrial controllers (Kaeser SIGMA CONTROL, Atlas Copco Elektronikon, Ingersoll Rand X-series) separate messages into warnings (keep running, attention needed) and shutdowns/trips (machine stopped for protection). Note the code, whether it warned or tripped, and any starter/VFD alarm shown separately from the main controller.

**2. Check the cooling and lubrication basics.** High discharge or airend temperature is the single most common shutdown. Before touching electronics, verify oil/coolant level, clean or inspect the cooler and aftercooler, confirm the cooling fan runs, check the inlet air filter, and make sure the room has adequate ventilation and is not too hot.

**3. Confirm load/unload behavior and pressure band.** Short-cycling, "hunting," and low-output complaints often trace to a wrong pressure setpoint, undersized storage, an air leak, or a failing inlet/blowdown valve rather than a broken part.

**4. Suspect the sensor before the mechanism.** Many modern trips are bad feedback, not true failure. A pressure or temperature reading that is out of range, implausible, or open-circuit usually means a failed transducer/thermistor or a wiring/connector fault. Compare the displayed value against an independent gauge before condemning the airend or motor.

**5. Respect motor and drive trips.** An overload or converter fault (overcurrent, undervoltage) can come from supply voltage/phase imbalance, loose connectors, a clogged separator loading the airend, or bearing wear. Fix the root cause and reset the overload; do not jumper it out.

**Safety and when to call a pro.** Always lock out and de-pressurize before opening panels or the separator tank. Stop resetting repeated airend, low-oil-pressure, or drive faults. Running a screw compressor through repeated high-temperature or overload trips can turn a manageable repair into a full airend or motor failure, so bring in a qualified compressed-air technician for anything involving the airend, motor windings, VFD internals, or the pressure vessel.


## Frequently asked questions

### What is the most common air compressor fault code?

High discharge or airend temperature is the most frequent shutdown across brands (for example Kaeser 0015 A 'ADT' or an Atlas Copco Elektronikon high-temperature shutdown). It almost always means a cooling or lubrication problem: low oil, a dirty cooler, a failed cooling fan, high ambient temperature, or blocked airflow.

### Why does my compressor keep tripping on motor overload?

An overload trip (e.g. Kaeser 0013 A 'Motor I') means the drive motor drew too much current. Common causes are a tight or seizing airend, a clogged oil separator raising internal pressure, unbalanced or low supply voltage, or worn motor bearings. Investigate the cause and reset the overload relay rather than repeatedly resetting the controller.

### My controller shows an emergency stop code but the E-stop isn't pressed. What now?

Emergency-stop faults (Kaeser 0004 A, Ingersoll Rand ERR.05) trip on any break in the safety chain, not just the button. Check that the E-stop is fully released, then inspect the safety-circuit wiring and terminals. On the IR X8i, ERR.05 specifically flags an open link between terminals '+C' and 'C1'.

### Should I reset a compressor fault myself or call a technician?

Basic checks are DIY: oil level, filters, coolers, ventilation, supply voltage, and clearing a genuine E-stop. Call a pro for repeated airend, low-oil-pressure, or VFD/converter faults. Cycling a screw compressor through repeated high-temperature or overload trips risks a full airend or motor failure.

### Is a temperature or pressure fault always a real mechanical failure?

No. Many trips are bad sensor feedback rather than a true failure. If a reading is out of range or implausible (for example an IR ERR.01 pressure-sensor fault, where the signal is outside 3.5-21.8 mA), check the transducer and its wiring against an independent gauge before replacing expensive mechanical parts.

