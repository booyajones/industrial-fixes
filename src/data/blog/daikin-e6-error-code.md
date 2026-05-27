---
title: "Daikin E6 Error Code - Causes & Fix"
description: "Daikin E6 means faulty compressor startup or overcurrent at the outdoor unit. Learn the real causes and step-by-step repair."
pubDatetime: 2026-05-25T20:40:13Z
modDatetime: 2026-05-25T20:40:13Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - hvac
  - daikin
---

## Daikin E6 Error Code — What It Means

E6 on a Daikin system indicates a compressor startup fault detected at the outdoor unit. Daikin's official documentation describes this code as 'faulty compressor start up' or 'compressor motor overcurrent/lock.' The outdoor control board has detected that the compressor either failed to start normally or drew abnormal current during startup or operation. This is not a sensor reading issue. It points to a problem in the compressor itself, the power feed to the compressor, the inverter drive circuit, or the control board that commands the compressor to run.

[Jump to Fix](#fix)

## Common Causes

- **Locked or failing compressor** The compressor motor may be mechanically seized, have internal bearing failure, or suffer from a short circuit or insulation breakdown in the motor windings.
- **Defective outdoor control PCB or inverter PCB** The inverter board may fail to send the correct drive signal to the compressor or the control board may misread operating current, triggering the fault even when the compressor is sound.
- **Faulty magnetic contactor or relay** Poor contact or a failing magnetic switch in the compressor power circuit can prevent full voltage from reaching the compressor or create intermittent connection during startup.
- **Power supply voltage imbalance or fault** On three-phase systems, unbalanced incoming line voltage exceeding the manufacturer's tolerance (such as a phase-to-phase difference of 14 V or more) can prevent proper compressor operation.
- **Wiring faults or earth fault in compressor circuit** Loose connectors, damaged harnesses, or insulation breakdown between the magnetic switch and compressor can create ground faults or open circuits that block startup.
- **Refrigerant shortage or expansion valve defect** In some Daikin systems, low refrigerant charge or a defective electronic expansion valve can create abnormal load conditions that overload the compressor during startup.

## Step-by-Step Fix {#fix}

1. **Stop the system and verify the model.** Confirm the exact Daikin model and system type, as the E6 fault tree and component layout vary across product lines.
2. **Measure incoming line voltage at the primary side of the magnetic switch.** With the unit off and the compressor stopped, check supply voltage on all phases (if three-phase) or line and neutral. On three-phase systems, a phase-to-phase voltage difference of 14 V or more indicates a supply imbalance that must be corrected at the source before proceeding.
3. **Start the unit and measure voltage at the secondary side of the magnetic switch.** If voltage imbalance appears on the load side but not the supply side, inspect the magnetic contactor for poor contact, pitting, or failure. If no voltage imbalance is present but the fault persists, suspect an earth fault in the circuit from the switch to the compressor.
4. **Perform insulation testing on the compressor circuit.** Use a megohmmeter to test for insulation breakdown or ground fault in the wiring and compressor windings. Check compressor motor winding resistance and verify no short, open, or ground condition exists.
5. **Isolate the control side from the load side.** Disconnect the wire on the secondary side of the magnetic switch and attempt startup. If E6 remains, the fault is in the operating current sensor circuit or outdoor PCB. Disconnect the wire from the outdoor PCB to the current sensor and retry; if the code persists, the PCB or sensor circuitry is at fault.
6. **Inspect the inverter PCB and drive output.** If all upstream checks pass, measure the drive signal from the inverter board to the compressor. A missing or incorrect drive waveform points to inverter board failure.
7. **Replace the failed component.** Depending on diagnosis, replace the compressor, inverter PCB, outdoor control board, magnetic contactor, or repair wiring and connections. Clear the error code and verify normal startup and operation.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Daikin outdoor control PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-e6-error-code&k=Daikin+outdoor+control+PCB&tag=errorcodefixes-20) \| Match the part number to your exact outdoor unit model and serial number. |
| Daikin inverter PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-e6-error-code&k=Daikin+inverter+PCB&tag=errorcodefixes-20) \| Verify compatibility with your compressor type and system capacity. |
| Magnetic contactor for compressor circuit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-e6-error-code&k=Magnetic+contactor+for+compressor+circuit&tag=errorcodefixes-20) \| Select contactor rated for your system voltage and compressor full-load current. |
| Daikin scroll or rotary compressor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-e6-error-code&k=Daikin+scroll+or+rotary+compressor&tag=errorcodefixes-20) \| Must match refrigerant type, voltage, and tonnage of your outdoor unit. |

## When to Call a Pro

E6 faults require live electrical diagnosis on high-voltage outdoor equipment and often involve refrigerant circuit work. If you do not have a multimeter, megohmmeter, and experience working safely on outdoor unit power circuits, call a licensed HVAC technician. Compressor replacement and inverter board work require refrigerant recovery, evacuation, and recharge to manufacturer specifications. Misdiagnosis can lead to repeated board or compressor failure and expensive parts replacement. A qualified technician will follow the manufacturer's diagnostic flow, measure drive signals, and test insulation to pinpoint the root cause before replacing components.

## See Also

- [Daikin VRV E7 Error Code — Causes & Fix](/posts/daikin-vrv-e7-error-code/)
- [Daikin UA Error Code — Mismatched Indoor/Outdoor Unit Fix](/posts/daikin-error-code-uA/)
- [Daikin RXQ VRV System Error Codes (Outdoor Unit): Complete Guide](/posts/daikin-vrv-rxq-error-codes/)
- [Daikin E5 Error Code - Causes & Fix](/posts/daikin-e5-error-code/)
