---
title: "ELGi Compressor Fault Codes: Neuron Controller Trips Explained"
description: "ELGi air compressor fault and warning messages for EG, EN, and AB series with Neuron controllers. What each trip means, likely cause, and how to fix it."
pubDatetime: 2026-04-22T21:00:00Z
modDatetime: 2026-04-22T21:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - compressor
  - elgi
  - industrial
money_part: "Oil separator element"
---

## ELGi Compressor Fault Codes — Quick Reference

ELGi compressors (EG, EN, AB series) use an electronic controller that monitors temperature, pressure, motor current, and maintenance intervals. Alarm messages appear on the display with a fault description and recommended action.

| Fault | Meaning | Quick Fix |
|-------|---------|-----------|
| High Discharge Temperature | Air end outlet temp exceeded | Check oil, cooler, fan |
| High Oil Temperature | Oil circuit too hot | Clean oil cooler, check oil level |
| Low Oil Pressure | Oil pressure dropped below setpoint | Check oil level and filter |
| Motor Overload | Motor drew excess current | Check voltage and demand |
| High Pressure | System pressure above limit | Check pressure switch and unloader |
| Air/Oil Separator Choked | Separator element restricted | Replace separator element |
| Sensor Failure | Temp or pressure sensor fault | Inspect sensor and harness |
| Service Required | Scheduled PM due | Perform PM and reset counter |

## Most Common Faults

### High Discharge Temperature
ELGi compressors are known for robust cooling systems but they still trip on high discharge temp when oil is low, coolers are dirty, or ambient temperature is excessive. Begin with the oil sight glass — ensure oil is at the correct level when the machine is stopped. Clean the oil cooler core with compressed air.

### Air/Oil Separator Choked
The separator element removes oil droplets from compressed air. As it loads up with oil and debris, the differential pressure across it rises. When the DP exceeds the setpoint (usually around 10 psi), the controller alarms. Replace the element — do not simply reset and continue.

### Low Oil Pressure
Check oil level first. Then check the oil filter — a clogged filter on initial cold startup can drop pressure before oil flow is established. If oil level and filter are fine, inspect the oil pressure sensor and wiring.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Oil separator element | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-elgi-compressor-fault-codes&k=Oil+separator+element&tag=errorcodefixes-20) \| Main periodic wear item |
| Oil filter | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-elgi-compressor-fault-codes&k=Oil+filter&tag=errorcodefixes-20) \| Replace with separator service |
| Temperature sensor | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-elgi-compressor-fault-codes&tag=errorcodefixes-20) \| Common after heat cycling |
| Cooling fan contactor | [Amazon](https://www.amazon.com/dp/B0CJFZQVPT?ascsubtag=ecf-elgi-compressor-fault-codes&tag=errorcodefixes-20) \| Check on temp-related faults |
## Jump to Fix

- **High discharge temp** → Verify oil level → Clean cooler → Check fan
- **Separator choked** → Replace element → Reset alarm
- **Low oil pressure** → Check oil level → Replace filter → Inspect sensor

## When to Call a Pro
ELGi has a global dealer network. If faults persist after parts replacement, contact an ELGi authorized service center for airend diagnostics and controller configuration checks.

## Related Articles

- [Air Compressor Fault Codes: Complete Guide](/posts/air-compressor-fault-codes/)
- [Atlas Copco Air Compressor Fault Codes — Complete Guide](/posts/atlas-copco-compressor-fault-codes/)
- [BOGE Air Compressor Error Codes - Complete Guide](/posts/boge-compressor-error-codes/)
- [Chicago Pneumatic Compressor Fault Codes — Complete Guide](/posts/chicago-pneumatic-compressor-faults/)
- [CompAir Air Compressor Fault Codes - Complete Guide](/posts/compair-compressor-fault-codes/)

## More Elgi Compressor fault codes

Compiled from manufacturer service manuals and authorized documentation.

| Code | What it means | Likely cause | How to fix |
| --- | --- | --- | --- |
| Pr. Probe Failure | Discharge pressure sensor probe failure (analog pressure input open). | Open circuit in the 4-20mA discharge pressure transducer (Pr-1) or its wiring/connector. | Inspect the discharge pressure sensor and harness at the analog input connector X05 for open/broken wiring; check the transducer signal and replace the sensor if the input reads open. |
| Tr. Probe Failure | Temperature sensor probe failure (analog temperature input open). | Open circuit in the KTY10 discharge temperature sensor (Tr-1) or its wiring. | Check the discharge temperature sensor and its wiring at the analog input; replace the sensor if the input is open. |
| Sump Pr. Probe Failure | Sump pressure sensor probe failure. | Open circuit in the sump pressure transducer (Pr-2) or its wiring. | Inspect the sump pressure sensor and connector; replace if the analog input reads open. |
| Trip Temperature | Discharge temperature exceeded the set trip temperature value. | Low oil, dirty oil cooler, failed cooling fan, high ambient, or restricted airflow. | Check oil level with the machine stopped, clean the cooler core, verify fan operation, and confirm adequate ventilation before restarting. |
| HSP (AD) | High discharge pressure: discharge pressure exceeded the set high pressure value. | Faulty or stuck inlet/unloader valve, failed pressure regulation, or plant demand dropping while the machine stays loaded. | Check the load/unload solenoid and inlet valve operation, verify the set high-pressure value, and inspect the minimum-pressure/check valve. |
| HSP (AS) | High sump pressure: sump pressure exceeded the set high pressure value (sump pressure enabled). | Restricted separator, stuck minimum-pressure valve, or unloader not venting the sump. | Inspect the air/oil separator, minimum-pressure valve, and blowdown/vent circuit. |
| Rev Rot / Ph Fail | Reverse rotation or phase failure detected when the motor is running. | Two supply phases swapped, a lost phase, or a phase-monitor relay trip. | Have an electrician verify incoming phase sequence and correct any swapped/lost phase; confirm the phase-sequence relay is healthy. |
| Sump Pressure Not Developing | After start, sump pressure did not reach at least 0.3 bar after the star delay expired. | Sump pressure sensor fault, leaking blowdown valve, or inlet valve not opening/closing correctly. | Check the sump pressure sensor reading, blowdown valve seal, and inlet valve operation. |
| Dis. Pressure Not Developing | After loading, discharge pressure did not reach at least 0.5 bar within 5 minutes. | Machine failing to build pressure: inlet valve not opening, large system leak, or discharge pressure sensor fault. | Verify the inlet valve loads, check for major downstream leaks, and confirm the discharge pressure sensor reads correctly. |
| Power failure | Mains supply was interrupted for more than 20 msec. | Momentary or full loss of incoming power. | Restore stable power and restart; if it recurs, investigate loose connections and supply reliability. Auto Restart, if enabled, resumes after the set delay. |
| Cooler | Cooler fault: the cooler motor overload (digital input) opened. | Cooling fan motor overload trip, seized fan, or overload relay set too low. | Reset and inspect the cooler fan motor and its overload relay; check for a seized or obstructed fan. |
| Dryer Trip | Integrated dryer fault when the dryer is enabled with the Trip option. | Dryer digital input opened on a dryer fault condition. | Inspect the integrated refrigerant dryer for its own fault (high pressure, condenser, etc.) and clear before restarting. |
| Warn Temperature | Warning: discharge temperature exceeded the set warn temperature (default 105 C), below the trip point. | Early sign of cooling degradation: dropping oil level, dirtying cooler, or rising ambient. | Address cooling now (oil level, clean cooler, fan) before it escalates to a Trip Temperature shutdown. |
| DPOF | Warning: differential pressure across the oil filter high (DPOF input open, feature enabled). | Clogged oil filter element. | Replace the oil filter element and reset the service indication. |
| DPAF | Warning: differential pressure across the air filter high (DPAF input open, feature enabled). | Clogged inlet air filter element. | Replace the air filter element and reset the service indication. |


## How to troubleshoot Elgi Compressor

Rotary screw compressors like ELGi's EG and EN series fail in a small number of predictable ways, and the Neuron controller almost always points you at the right one. Start by reading the exact fault text and the machine status recorded with it. The controller stores dated fault reports (up to 99 on the Neuron II), so before you touch anything, pull the fault history to see whether this is a first-time trip or a repeating pattern.

Work the most common failure mode first: heat. The large majority of hard shutdowns on oil-flooded screw compressors trace back to cooling. With the machine stopped and depressurized, check the oil level at the sight glass, then inspect the oil cooler and aftercooler cores for dust and debris and blow them out. Confirm the cooling fan actually runs and that the room has enough ventilation and a reasonable ambient temperature. Low oil, a plugged cooler, or a dead fan will show up first as a high-temperature warning and then as a discharge-temperature trip.

Second, treat pressure and \"not developing\" faults as valve and separator problems. High-pressure trips usually mean the inlet/unloader or minimum-pressure valve is stuck, or the load/unload control is not venting the sump. Rising differential pressure across the air/oil separator is a wear item, not a reset item: when the controller flags high differential pressure, replace the separator element rather than clearing the alarm and continuing. Filter warnings (oil filter, air filter) are routine maintenance prompts and are safe to service and reset.

Third, respect the electrical faults. Reverse rotation, phase failure, low voltage, and power-failure trips are supply and wiring issues that belong to a qualified electrician, and reverse rotation in particular can damage the airend if ignored. Always lock out and tag out before opening panels, never defeat the emergency stop or overload relays, and bleed system pressure before removing any cap or line. If a fault returns immediately after a correct parts replacement, or if you see airend or bearing symptoms (noise, vibration, oil consumption), stop and call an ELGi authorized service center for airend diagnostics and controller configuration checks.


## Frequently asked questions

### What does a Trip Temperature or high discharge temperature shutdown mean on an ELGi compressor?

It means the discharge temperature exceeded the controller's set trip value. The usual causes are low oil, a dirty oil cooler, a failed cooling fan, high ambient temperature, or poor ventilation. Check oil level with the machine stopped, clean the cooler core, and confirm the fan runs before restarting.

### My ELGi controller shows Pr. Probe Failure or Tr. Probe Failure. What is that?

Those are sensor faults, not mechanical faults. Pr. Probe Failure is a discharge pressure sensor open circuit and Tr. Probe Failure is a temperature sensor open circuit. Inspect the sensor and its wiring and connector at the analog input; if the input reads open, replace the sensor. There is also a Sump Pr. Probe Failure for the sump pressure transducer.

### The compressor trips on High Differential Pressure. Can I just reset it?

No. That warning means the air/oil separator element is loading up with oil and debris and the pressure drop across it has climbed past the set point. Resetting and running will only make it worse and can damage the element. Replace the separator element, and it is good practice to change the oil filter at the same service.

### What causes a Sump Pressure Not Developing or Dis. Pressure Not Developing fault?

These are start and load checks. Sump Pressure Not Developing means the sump did not reach about 0.3 bar after the star delay, usually a sump sensor, blowdown valve, or inlet valve issue. Dis. Pressure Not Developing means discharge pressure did not reach about 0.5 bar within five minutes after loading, pointing to an inlet valve not opening, a large system leak, or a discharge pressure sensor fault.

### Should I fix a Reverse Rotation or Low Voltage fault myself?

No. Reverse rotation, phase failure, low voltage, and power-failure trips are electrical supply issues. Reverse rotation especially can damage the airend if the machine runs. Have a qualified electrician verify phase sequence and incoming voltage under load rather than repeatedly resetting the fault.

