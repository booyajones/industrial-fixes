---
title: "Danfoss AKC Controller Fault Codes - Complete Guide"
description: "Danfoss AKC refrigeration controller fault codes for supermarket showcase and cold storage: causes and troubleshooting steps."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - danfoss
  - refrigeration
  - akc-controller
---

## Danfoss AKC Controller Fault Codes - Quick Reference

Danfoss AKC controllers (AKC 15, 22, 24, 55, 114, and the newer AK-CC series) manage refrigerated display cases, walk-in coolers, and rack systems. Alarms appear on the controller display and via the Danfoss AKM or ADAP-KOOL network.

| Alarm / Code | Meaning | Quick Fix |
|-------------|---------|-----------|
| A1 - Temperature High | Case temperature above alarm setpoint | Check defrost, door seals, fans |
| A2 - Temperature Low | Case temp below low alarm setpoint | Check thermostat/thermistor |
| A3 - Defrost Timeout | Defrost exceeded maximum time | Check defrost heater and termination |
| A4 - Sensor Fault | Temperature sensor open or shorted | Check sensor wiring |
| A5 - Defrost Sensor Fault | Defrost termination sensor fault | Check termination sensor |
| A6 - Door Switch Alarm | Door open too long | Check door and switch |
| A7 - Communication Fault | Network communication lost | Check LonWorks/RS-485 wiring |
| A8 - Air Sensor Fault | Air inlet or outlet sensor fault | Check sensor |
| A9 - Power Fail | Supply power was interrupted | Normal after power outage |
| A10 - Controller Fault | Internal controller error | Replace controller |

## Most Common Faults

### A1 - Temperature High
Most common alarm on AKC controllers. First check if a recent defrost cycle completed normally. Ice buildup from a failed defrost blocks evaporator airflow and causes temperature rise within hours. Also check door gaskets and night curtains. If defrost is fine, suspect evaporator fan motor failure.

### A3 - Defrost Timeout
AKC controllers terminate defrost on either temperature (termination sensor reaches setpoint) or time (maximum defrost duration). A timeout means the coil didn't reach the termination setpoint within the time limit. Check the defrost heater with an ohmmeter - open heater elements are common on aging equipment. Also check the safety thermostat.

### A4 - Sensor Fault
Danfoss uses NTC (10K or 20K at 25°C depending on model) temperature sensors. A disconnected or failed sensor causes A4. Test the sensor resistance at the controller terminal. Danfoss AK sensors have a standard curve - any value below 200 Ohms or above 500K Ohms indicates failure.

### A7 - Communication Fault
AKC controllers on LonWorks or RS-485 networks alarm on communication loss. Check LonWorks cable polarity and termination - LonWorks requires twisted-pair with proper termination at each end. RS-485 requires a 120-ohm terminator at each trunk end and correct addressing.

## Parts Often Needed

| Part | Notes |
|------|-------|
| AKC temperature sensor (NTC) | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-danfoss-akc-controller-fault&tag=errorcodefixes-20) \| Replace on A4/A5 fault |
| Defrost heater element | [Amazon](https://www.amazon.com/dp/B07FVP4CY6?ascsubtag=ecf-danfoss-akc-controller-fault&tag=errorcodefixes-20) \| Replace on A3 timeout |
| Defrost safety thermostat | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-akc-controller-fault&k=Defrost+safety+thermostat&tag=errorcodefixes-20) \| Replace on A3 timeout |
| Evaporator fan motor | [Amazon](https://www.amazon.com/dp/B01N0J3ZEH?ascsubtag=ecf-danfoss-akc-controller-fault&tag=errorcodefixes-20) \| Replace on temperature alarm |
| AKC controller | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-akc-controller-fault&k=AKC+controller&tag=errorcodefixes-20) \| Replace on A10 fault |
## When to Call a Pro
Danfoss ADAP-KOOL network configuration and AKM system management require Danfoss-trained refrigeration controls technicians. A misconfigured AKC defrost schedule can cause food safety violations.

## See Also

- [Danfoss VFD Fault AL 14 — Causes & Fix](/posts/danfoss-vfd-fault-al-14/)
- [Danfoss VFD Fault E-Trip — Causes & Fix](/posts/danfoss-vfd-fault-e-trip/)
- [Danfoss VFD Fault W30 — Brake Resistor Overtemperature Fix](/posts/danfoss-vfd-fault-w30/)
- [Danfoss VLT Alarm 14 - Earth Fault: What It Means and How to Fix It](/posts/danfoss-vlt-alarm-14/)
