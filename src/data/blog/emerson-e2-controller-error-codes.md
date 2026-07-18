---
title: "Emerson E2 Controller Fault & Error Codes: Causes + Fixes"
description: "Emerson (Copeland) E2 refrigeration controller alarm and advisory codes for supermarkets and cold storage, with real causes and step-by-step fixes."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - emerson
  - copeland
  - refrigeration
  - e2-controller
money_part: "E2 temperature sensor (NTC)"
---

## Emerson E2 Controller Error Codes - Quick Reference

The Emerson E2 (formerly Alerton, now Emerson Climate Technologies) is a refrigeration and HVAC supervisory controller used in supermarkets, convenience stores, and cold storage. Alarms display on the E2 touchscreen and via the Emerson Store Connect cloud platform.

| Alarm | Device | Meaning | Quick Fix |
|-------|--------|---------|-----------|
| Sensor Failure | Case/Rack | Sensor open, short, or out of range | Check sensor wiring |
| Temperature High | Refrigerated case | Case temp above setpoint | Check defrost, door seals, evap fan |
| Discharge Pressure High | Compressor rack | High head pressure | Check condenser, refrigerant |
| Suction Pressure Low | Rack | Low suction pressure | Check expansion valve, refrigerant |
| Low Superheat | Circuit | Flood-back condition | Check TXV or EEV |
| High Superheat | Circuit | TXV/EEV starving | Check TXV setting or EEV stepper |
| Compressor Fault | Rack | Compressor failure or alarm | Check compressor controller |
| Defrost Fail | Case | Defrost didn't complete | Check defrost heater and termination |
| Communication Fault | I/O board | E2 cannot reach I/O node | Check RS-485 wiring |
| Oil Failure | Compressor | Low oil pressure | Check oil level and crankcase |

## Most Common Faults

### Temperature High Alarm (Case)
Check defrost schedule first - a missed defrost causes ice buildup on the evaporator coil, which blocks airflow and raises case temperature. Also check: door gaskets, evaporator fan motors, and the case curtains overnight. If all defrost cycles are running normally, suspect refrigerant charge or a failed expansion valve.

### Discharge Pressure High
High discharge pressure (head pressure) indicates: dirty or failed condenser coil, failed condenser fan motors, high ambient temperature, or refrigerant overcharge. Check condenser coil cleanliness and fan operation. On air-cooled systems, condenser pressure should be 15–25°F above ambient.

### Sensor Failure
E2 sensors are typically NTC thermistors (10K Ohm at 77°F/25°C). A failed sensor reads as an open circuit (very high resistance) or short circuit (zero resistance). Test the sensor resistance at the E2 I/O board terminal with the sensor wires disconnected. Replace the sensor if resistance is outside the expected curve.

### Defrost Fail
E2 defrost fail alarms occur when a defrost cycle doesn't terminate within the maximum time limit. Causes include: failed defrost termination sensor, failed defrost heater element, or tripped defrost heater safety fuse. Check the termination sensor location and reading in the E2 defrost parameters.

## Parts Often Needed

| Part | Notes |
|------|-------|
| E2 temperature sensor (NTC) | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-emerson-e2-controller-error-codes&tag=errorcodefixes-20) \| Replace on sensor failure |
| Defrost heater element | [Amazon](https://www.amazon.com/dp/B07FVP4CY6?ascsubtag=ecf-emerson-e2-controller-error-codes&tag=errorcodefixes-20) \| Replace on defrost fail |
| Defrost termination thermostat | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-emerson-e2-controller-error-codes&tag=errorcodefixes-20) \| Replace on defrost timeout |
| Evaporator fan motor | [Amazon](https://www.amazon.com/dp/B01N0J3ZEH?ascsubtag=ecf-emerson-e2-controller-error-codes&tag=errorcodefixes-20) \| Replace on case temp alarm |
| E2 I/O board | Amazon \| Replace on communication fault |
## When to Call a Pro
Emerson E2 refrigerant circuit diagnostics, EEV calibration, and compressor rack management require EPA Section 608 certification and E2 training. Incorrect setpoint changes can cause food safety violations.

## More Emerson E2 Controller fault codes

Compiled from manufacturer service manuals and authorized documentation.

| Code | What it means | Likely cause | How to fix |
| --- | --- | --- | --- |
| Comb Temp Hi Limit Exceeded | The combined temperature of an entire Standard Circuit or Case Control Circuit has risen above its programmed high temperature setpoint. | Circuit-wide refrigeration loss, suction problem feeding the whole circuit, or a rack/compressor issue rather than a single case fault. | Because this is a circuit-combined value, look upstream: check suction pressure, the feeding compressor group, and refrigerant charge before chasing individual cases. |
| Did Not Defrost | A case circuit did not enter defrost at its scheduled time. | Defrost schedule conflict or inhibit, controller/output failure, or the circuit was locked out of defrost by another condition. | Review the circuit's defrost schedule and any inhibits in the E2 defrost parameters, confirm the defrost output/contactor energizes, and check for schedule overlaps. |
| Did Not Terminate Defrost | Defrost in a standard circuit lasted for its entire programmed time duration and did not terminate. | Failed defrost termination sensor, failed defrost heater, wiring fault to the termination probe, or termination setpoint set too high to ever be reached. | Check the termination sensor reading and location in the E2 defrost parameters, test the defrost heater element and safety, and confirm the termination setpoint is realistic. |
| Did Not Exit Defrost | A CC-100 or CS-100 case controller that entered defrost did not terminate or exit defrost at its programmed time. | Case-controller termination sensor or logic fault, or a communications problem preventing the E2 from receiving the exit. | Check the case controller's termination sensor and defrost config, and verify the RS-485 link between the E2 and the CC-100/CS-100. |
| Checkit Sensor Has Failed | A Checkit sensor is returning an invalid temperature value, indicating a sensor failure. | Open or shorted sensor, damaged lead, or a loose terminal at the input board. | Measure the sensor resistance at the input with leads disconnected and compare to the thermistor curve; replace the sensor if it reads open or shorted. |
| Appl Not Keeping Setpoint | An Air Handling Unit or Heat/Cool application has not achieved setpoint for a prolonged period of time. | Undersized or failing stage, refrigerant/heating capacity loss, stuck damper or valve, or a sensor reading that never lets the application satisfy. | Verify staging outputs energize, check mechanical capacity and airflow, and confirm the control sensor is reading accurately. |
| 50/60 Hz Line Clock Is Bad | E2 is not successfully synchronizing its clock with the 50/60 Hz pulse of its incoming power. | Poor or noisy incoming power, wrong power configuration, or an E2 power-supply/main-board issue. | Verify clean, correct supply power to the E2; if power is good, the main board or power supply may need service. |


## How to troubleshoot Emerson E2 Controller

The Emerson (Copeland) E2 is a supervisory controller, not a single appliance, so the first diagnostic question is always **which application raised the alarm** — a Standard Circuit, a Case Control Circuit (CC-100/CS-100), a Suction Group, a Condenser, or an HVAC/AHU stage. Open the **Alarm Advisory Log** and note the exact alarm name and the application it came from before touching hardware. Many E2 messages are informational "Notice" events (setpoint changes, resets, dial-out logs); real equipment faults show as "Alarm" or "Failure" priorities. Do not clear an alarm until you have read what raised it.

**Sequence for temperature alarms:** work from the case outward. Confirm the last defrost completed and the coil is clear of ice, then verify evaporator fans run and doors and gaskets seal, then check the feeding valve/EEV, and only then suspect refrigerant charge or the compressor group. A **single-sensor** case alarm (Case Temp Hi Limit Exceeded) points at that one case; a **combined** circuit alarm (Comb Temp Hi Limit Exceeded) points upstream at suction pressure or the rack. This distinction saves the most time.

**Sensor faults:** E2 case and product sensors are NTC thermistors. A failed sensor reads as open (very high resistance) or shorted (near zero). Disconnect the sensor at the input board and measure resistance against the thermistor curve rather than guessing at the controller. Reseat suspect terminals; loose RS-485 or sensor terminals cause intermittent "sensor failure" and "device absent" alarms that look like hardware failures.

**Communication faults** (Communication Port Down, Device Absent From Network) are usually wiring, addressing, or a single faulted node dragging an RS-485 segment down — confirm power and address on the missing board and inspect polarity and end-of-line termination before condemning the E2 main board.

**Safety and when to call a pro:** any alarm that involves the refrigerant circuit (Discharge Trip, high/low pressure, superheat, EEV calibration, compressor rack management) requires EPA Section 608 certification and E2 training. Head-pressure and discharge-trip conditions can indicate an unsafe rack — do not repeatedly reset a Discharge Trip without finding the cause. Setpoint changes on food cases carry food-safety consequences, so leave circuit setpoints, defrost schedules, and rack parameters to a qualified refrigeration technician.


## Frequently asked questions

### What is the difference between an E2 Alarm and a Notice?

In the E2's Alarm Advisory Log, an Alarm (and Failure) is a higher-priority event that needs attention, while a Notice is a low-priority informational message that may need no action or only future attention. Many log entries like setpoint changes, resets, and dial-out records are Notices, not equipment faults, so read the alarm name and priority before dispatching anyone.

### My E2 shows a case temperature high alarm but the case looks cold. What should I check first?

Check the last defrost and the evaporator coil for ice before anything else. A missed or non-terminating defrost ices the coil, blocks airflow, and drives the sensor reading up even when the box still feels cold. Then confirm the evaporator fans run and the doors and gaskets seal. If defrost is normal, look at the valve/EEV and refrigerant feed.

### What causes a 'Did Not Terminate Defrost' alarm on the E2?

It means a circuit's defrost ran its full programmed time and never terminated. The usual causes are a failed or mislocated defrost termination sensor, a failed defrost heater, a wiring fault to the termination probe, or a termination setpoint set too high to ever be reached. Check the termination sensor reading in the E2 defrost parameters and test the heater.

### Why does the E2 report 'Communication Port Is Down' or 'Device Absent From Network'?

These point to the E2's network rather than a mechanical fault. A device may be powered down or failed, have the wrong address, or a single faulted node may be pulling an RS-485 segment down. Confirm power and address on the missing board, check RS-485 polarity and end-of-line termination, and isolate devices to find the bad one before assuming the E2 main board failed.

### Is it safe to reset a Discharge Trip on the compressor rack myself?

No. A Discharge Trip is an emergency high-discharge-pressure shutdown of the rack, usually from a dirty or failed condenser, failed condenser fans, high ambient, or overcharge. Repeatedly resetting it without fixing the cause risks the compressors and is unsafe. Refrigerant-circuit work requires EPA Section 608 certification, so have a qualified refrigeration technician diagnose it.


## Related guides

- [Miller Welder Fault Code H1](/posts/miller-welder-fault-code-h1/)
- [Dixell Xr60C P1 Error Code](/posts/dixell-xr60c-p1-error-code/)

