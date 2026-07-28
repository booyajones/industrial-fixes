---
title: "York YXV Heat Pump Error Codes - Fault Code Reference"
description: "Complete York YXV heat pump fault code reference. All iQ Drive fault codes, communication errors, and diagnostic LEDs with step-by-step fixes."
pubDatetime: 2026-04-25T00:00:00Z
author: "Dana Kowalski"
tags:
  - hvac
  - error-codes
---

The York YXV is a mid-tier variable-speed heat pump with York's iQ Drive inverter compressor technology. It delivers variable capacity from approximately 25% to 100% load, which makes it exceptionally efficient , but also means more sophisticated diagnostics than a single-stage unit. When the iQ Drive system detects a problem, it stores fault codes accessible through the system's communicating thermostat or the control board's service LED.

## What Does a York YXV Heat Pump Error Code Mean?

The YXV communicates faults through two channels: the iQ Drive inverter drive module (which controls the variable-speed compressor) and the unit control board (UCB) located in the outdoor cabinet. When paired with a York Affinity or YORK communicating thermostat, fault codes display directly on the thermostat screen. Without a communicating thermostat, the UCB's diagnostic LED blinks a fault pattern.

**Understanding the Fault Code System**
York YXV fault codes use a two-digit format. The first digit (number of short blinks) identifies the fault category; the second digit (number of long blinks after a pause) identifies the specific fault within that category.

### York YXV Fault Code Reference

**Fault 1-1 , iQ Drive Module Fault: Overcurrent**
The inverter detected excess current draw at the compressor. Possible causes: compressor is mechanically seized or starting to fail, motor windings are shorted, or the refrigerant charge is critically low causing liquid floodback. Check refrigerant charge first , running a YXV low on charge is the number one cause of premature inverter and compressor failure.

**Fault 1-2 , iQ Drive DC Bus Undervoltage**
The inverter's DC bus voltage has dropped below the operating threshold. Causes: low supply voltage from the utility (check with a voltmeter , should be 208–240V ±10%), a failing capacitor in the inverter's DC bus, or wiring with inadequate gauge causing voltage drop under load.

**Fault 1-3 , iQ Drive DC Bus Overvoltage**
The DC bus voltage has exceeded safe limits. Most commonly caused by the compressor regenerating voltage during a rapid stop or by supply voltage spikes. A line reactor or surge protector on the supply line prevents recurring overvoltage faults.

**Fault 1-4 , iQ Drive Module Overtemperature**
The inverter's heat sink temperature has exceeded its safe operating limit. Causes: dirty outdoor coil blocking heat dissipation, failed condenser fan motor, debris packing the inverter module's own heat sink fins, or ambient temperatures above the rated operating range.

**Fault 1-5 , Compressor Start Failure**
The compressor failed to start within the allowed time window. Three consecutive start failures trigger a lockout. Causes: low ambient temperature below rated operating range, failed compressor start components, compressor is flooded with refrigerant liquid, or power supply issues. Allow 30 minutes at operating temperature before forcing a restart.

**Fault 2-1 , High-Pressure Switch Open**
The refrigerant high-pressure switch tripped. Causes in cooling mode: dirty condenser coil, failed outdoor fan motor, refrigerant overcharge, or restriction in the liquid line. In heating mode: dirty indoor coil, failed indoor blower, or restriction in the refrigerant circuit. Clean the coil on the side acting as the condenser for the current operating mode.

**Fault 2-2 , Low-Pressure Switch Open**
Low refrigerant pressure detected. In cooling mode this indicates low refrigerant charge, a restriction in the refrigerant circuit (expansion device stuck closed), or very low outdoor ambient. In heating mode it may indicate the outdoor coil is severely iced. Check the defrost cycle operation.

**Fault 2-3 , Discharge Temperature Sensor Fault**
The compressor discharge temperature thermistor is reading out of range or has failed. The iQ Drive uses this sensor to protect the compressor from overheating during high-load operation. Check sensor resistance: should be approximately 10K ohms at 77°F. Replace if out of range.

**Fault 2-4 , Outdoor Ambient Sensor Fault**
The outdoor ambient temperature thermistor has failed or reads out of range. This sensor is critical for the YXV's defrost algorithm. Without accurate ambient data, the heat pump may under-defrost (causing ice buildup) or over-defrost (wasting energy). Replace the sensor.

**Fault 3-1 , Loss of Communication with Thermostat**
The outdoor unit has lost communication with the thermostat or the indoor unit's control board. Check the communication wiring (typically a 24V two-wire bus). The YXV uses conventional 24V control wiring, not a dedicated communication bus like some premium York models.

**Fault 3-2 , Indoor Unit Communication Fault**
The outdoor unit can see the thermostat but cannot communicate with the indoor air handler or coil. Check the indoor unit's control board and wiring connections.

**Fault 4-1 , Defrost Fault: Termination Failure**
The defrost cycle started (reversing valve switched to cooling mode to melt ice) but failed to terminate within the maximum time allowed. The outdoor coil temperature sensor may be faulty, or the coil is so heavily iced that the defrost cycle could not complete. Inspect the outdoor unit for severe ice accumulation , restricted airflow at the base (debris, leaves, snow) is a common cause.

**Fault 4-2 , Reversing Valve Fault**
The reversing valve (which switches the refrigerant circuit direction for heating vs. cooling) is not operating correctly. The outdoor unit's temperature sensor detected that the system is in the wrong operating mode for the command it was given. A failed reversing valve solenoid coil is the most common cause.

**Fault 5-1 , Fan Motor Fault**
The outdoor fan motor has failed or is not reaching the commanded speed. The YXV's variable-speed outdoor fan is DC brushless and controlled by a motor module. Check the fan blade for obstructions, check DC voltage to the motor module, and verify the motor module is not in fault.

## How to Fix It

1. **Access fault history through the thermostat.** On the York communicating thermostat, navigate to Menu → Service → Fault Log. This shows fault codes with timestamps.
2. **Read the LED without a communicating thermostat.** Find the UCB's service LED on the outdoor unit control board. Count short blinks, pause, then long blinks. Example: 2 short blinks, pause, 1 long blink = Fault 2-1 (high pressure).
3. **Check and clean the outdoor coil.** Use a garden hose from the inside out to flush debris from the coil fins. Many YXV faults (1-4, 2-1, 4-1) are resolved by coil cleaning alone.
4. **Check supply voltage.** At the outdoor unit disconnect, measure line-to-line voltage with a multimeter. It must be within 10% of nameplate voltage (usually 208–230V). Low voltage causes faults 1-2 and 1-5.
5. **Check refrigerant charge.** Many iQ Drive faults trace back to improper refrigerant charge. The YXV uses R-410A. Charge verification requires manifold gauges and a licensed technician.
6. **Inspect the defrost sensor.** For Fault 4-1, locate the outdoor coil temperature sensor clipped to the coil and check its resistance against the spec chart in the installation manual.
7. **Replace the reversing valve solenoid coil.** For Fault 4-2, the solenoid coil often fails while the valve body is still functional. Coils are inexpensive and field-replaceable without recovering refrigerant.
8. **Clear faults and re-test.** After any repair, clear the fault log through the thermostat or by cycling power, then run a full heating and cooling test cycle.

## Parts You May Need

| Part | Use | Buy on Amazon |
|------|-----|---------------|
| Reversing Valve Solenoid Coil (24V, York compatible) | Replace failed solenoid for Fault 4-2 | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-york-yxv-heat-pump-error-codes&k=reversing+valve+solenoid+coil+24v+heat+pump&tag=errorcodefixes-20) |
| 10K NTC Outdoor Temperature Sensor | Replace ambient or coil sensor for Faults 2-3, 2-4 | [View on Amazon](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-york-yxv-heat-pump-error-codes&tag=errorcodefixes-20) |
| HVAC Digital Manifold Gauge Set (R-410A) | Check refrigerant pressures for low/high pressure faults | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-york-yxv-heat-pump-error-codes&k=r410a+manifold+gauge+set+digital+hvac&tag=errorcodefixes-20) |
| HVAC Coil Fin Comb (multi-pitch) | Straighten bent fins after coil cleaning | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-york-yxv-heat-pump-error-codes&k=hvac+coil+fin+comb+straightener&tag=errorcodefixes-20) |
| Fluke 116 HVAC Multimeter | Measure voltage, amperage, and sensor resistance | [View on Amazon](https://www.amazon.com/dp/B08ZJSN5X3?ascsubtag=ecf-york-yxv-heat-pump-error-codes&tag=errorcodefixes-20) |

## When to Call a Pro

- **Fault 1-1 (overcurrent) or Fault 1-5 (start failure) that return after reset.** Compressor mechanical failure requires professional diagnosis and refrigerant recovery.
- **Any refrigerant-related fault (2-1, 2-2).** Pressure measurement and refrigerant handling require EPA Section 608 certification.
- **Fault 1-2 or 1-3 involving the inverter DC bus.** Inverter module repair/replacement on the YXV requires factory-trained service to avoid voiding the compressor warranty.
- **Fault 4-2 (reversing valve) if the solenoid coil replacement doesn't resolve it.** A stuck reversing valve body requires refrigerant recovery and brazing to replace.

## FAQ

**Q: My York YXV shows no fault codes but is only running at low capacity and not heating well , what's wrong?**
A: The iQ Drive may be in a "soft fault" state , operating in a reduced-capacity fallback mode without storing a hard fault code. Check the inverter module's status LED (separate from the UCB LED). A slow flash on the inverter module indicates it is current-limiting due to low refrigerant, high discharge temp, or power issues.

**Q: How do I clear fault codes on a York YXV without a communicating thermostat?**
A: Cut power to the outdoor unit at the disconnect for 30 seconds. Restore power. The UCB will reset and clear stored faults. Note: this does not fix the underlying problem. If the fault returns, the root cause is still present.

**Q: Can I upgrade my York YXV with a smart thermostat like an ecobee or Nest?**
A: Yes, but you will lose iQ Drive communicating features, including variable-speed capacity control from the thermostat and fault logging on the thermostat screen. The YXV will still operate in variable speed internally based on refrigerant conditions, but the thermostat will only send simple Y/W/G signals. York's own communicating thermostat unlocks the full system potential.

**Q: My York YXV runs fine in cooling but throws a Fault 4-1 every time it tries to defrost in heating mode. How do I diagnose this?**
A: Fault 4-1 during defrost means the cycle starts but doesn't complete. The most likely cause is a faulty defrost termination sensor , the sensor that tells the board the coil is clear of ice. Replace the outdoor coil temperature sensor first. Second cause is low refrigerant charge reducing the system's ability to generate enough heat to melt ice within the defrost window.
