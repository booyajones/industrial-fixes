---
title: "CompAir Compressor Fault Codes: DELCOS XL Code List"
description: "CompAir DELCOS XL fault codes decoded: E400, E403, E504, F008 and more, with real causes and fixes for L, D and H series screw compressors."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - compressor
  - compair
  - industrial
money_part: "Oil separator element"
---

## CompAir Compressor Fault Codes - Quick Reference

CompAir (Gardner Denver brand) rotary screw compressors use the Delcos XL and Delcos Pro controllers on L, D, and B series machines. Alarms fall into warnings (continue running) and shutdowns (compressor stops).

| Fault | Meaning | Quick Fix |
|-------|---------|-----------|
| High Discharge Temp | Air/oil temperature exceeded | Check cooler, oil level, fan |
| Low Oil Level | Oil level sensor triggered | Add oil, check for leaks |
| Motor Overload | Motor current too high | Check phases, load, voltage |
| High Pressure | System pressure exceeded set point | Check pressure relief, regulator |
| E-Stop | Emergency stop circuit open | Reset E-stop, inspect wiring |
| Service Due | Maintenance interval reached | Perform PM, reset counter |
| Oil Separator DP High | Separator restricted | Replace separator element |
| Sensor Fault | Sensor signal out of range | Check sensor and wiring |
| Phase Fault | Phase loss or imbalance | Check supply voltage |
| Blowdown Valve | Valve not operating correctly | Inspect valve actuator |

## Most Common Faults

### High Discharge Temperature
Clean the cooler bundle and verify fan operation first. CompAir oil coolers are often cooled by a fan driven by the main motor belt or a separate motor - check that the fan runs at full speed. Also check oil type and level; synthetic oil is strongly preferred.

### Oil Separator DP High
Separator element typically needs replacement every 2,000–6,000 hours depending on operating conditions. Running dusty environments accelerates clogging. A blocked separator increases energy consumption and causes oil carryover into the air system.

### Phase Fault
CompAir machines are sensitive to supply voltage quality. Missing phase, voltage imbalance above 3%, or frequent dips trigger this fault. Verify at the incoming terminal block under load, not just at the disconnect.

### Motor Overload
Check current draw on all three phases with a clamp meter. Unbalanced loading, incorrect motor rotation on initial setup, or a sticking inlet valve can all cause nuisance overloads.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Oil separator element | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-compair-compressor-fault-codes&k=Oil+separator+element&tag=errorcodefixes-20) \| Main PM part |
| Air filter element | [Amazon](https://www.amazon.com/dp/B0CLBFXLYJ?ascsubtag=ecf-compair-compressor-fault-codes&tag=errorcodefixes-20) \| Replace per service schedule |
| Oil filter cartridge | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-compair-compressor-fault-codes&k=Oil+filter+cartridge&tag=errorcodefixes-20) \| Replace with separator |
| Temperature sensors (NTC) | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-compair-compressor-fault-codes&tag=errorcodefixes-20) \| Common fault after heat cycles |
| Inlet valve repair kit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-compair-compressor-fault-codes&k=Inlet+valve+repair+kit&tag=errorcodefixes-20) \| Sticking causes overloads |
## When to Call a Pro
If the compressor shuts down on high temperature after cooler cleaning and oil service, suspect airend discharge valve or screw wear. CompAir airend rebuilds require factory tooling and specifications.

## Related Articles

- [Air Compressor Fault Codes: Complete Guide](/posts/air-compressor-fault-codes/)
- [Atlas Copco Air Compressor Fault Codes — Complete Guide](/posts/atlas-copco-compressor-fault-codes/)
- [BOGE Air Compressor Error Codes - Complete Guide](/posts/boge-compressor-error-codes/)
- [Chicago Pneumatic Compressor Fault Codes — Complete Guide](/posts/chicago-pneumatic-compressor-faults/)
- [Copeland Compressor Error Code 1 — High Pressure Cutout Fix](/posts/copeland-compressor-error-code-1/)

## More Compair Compressor fault codes

Compiled from manufacturer service manuals and authorized documentation.

| Code | What it means | Likely cause | How to fix |
| --- | --- | --- | --- |
| E400 | Power Supply Failure (fault, compressor stopped) | Power failure, voltage dip, damaged cabling, or loose terminals. Also shown if a power loss exceeded the Max. Power Loss Time set for auto-restart. | Find the supply cause. Check cabling and retighten all connecting terminals and plugs. Acknowledge/reset in the Fault History menu before restarting. |
| E401 | Emergency Stop Activated (fault) | Emergency-stop button pressed, defective E-stop switch, or damaged cabling. | Unlock the emergency-stop pushbutton, check/replace the switch if defective, inspect cabling, then reset. |
| E402 | High Motor Temp. M1 (fault) | Drive motor started too frequently, defective motor cooling, power consumption too high, faulty supply, or a failing motor. | Limit starts per hour, improve cooling-air supply, check supply voltage and current draw, inspect/replace the drive motor. |
| E403 | Compressor Disch. Temp. (airend discharge temperature fault, compressor stopped) | Discharge temperature exceeded set limit: intake/ambient temperature too high, inadequate cooling, or running with the enclosure open. | Find the cause, improve cooling-air or cooling-water supply, and close the enclosure. Verify oil level/grade (per the related A602 warning). |
| E404 | Start Temperature low (fault) | Start attempted at too low a temperature (over-cooled airend), or R2 temperature sensor reading too low/high. | Warm the compressor room, then reset in Fault History. Check/replace the R2 sensor if it reads incorrectly. |
| E405 | Discharge Over Pressure (fault) - rated pressure exceeded by 1.5 bar / 21 psi | System pressure losses too high, line pressure set too high, external pressure demand too high, intake controller not closing, defective blow-off/bypass valve (RS), or a faulty B1/B2 pressure sensor. | Check remote on-load/off-load switch points, verify the intake controller closes, inspect the blow-off/bypass valve, and replace a faulty pressure sensor. |
| E406 | Line Pressure Sensor B1 (fault) | Faulty line pressure sensor B1 or damaged sensor cabling. On a base-load-sequencing master this also disables the BLS group. | Check and renew sensor B1 and its wiring if necessary. |
| E407 | Discharge Pressure Sensor B2 (fault) | Faulty compressor final-pressure sensor B2 or damaged cabling. | Check and renew sensor B2 and its wiring if necessary. |
| E408 | Disch. Temp. Sensor R2 (fault) | Faulty discharge temperature sensor R2 or damaged cabling. | Check and renew the R2 temperature sensor and its wiring if necessary. |
| E409 | Controller Hardware (fault) | Hardware error internal to the DELCOS XL controller. | Replace the DELCOS XL controller (requires the compressor-specific setup code and reference number). |
| E410 | Cooling (fault) | Air-cooled: fan-motor circuit breaker tripped, breaker set wrong, high air-channel resistance, or faulty fan motor. Water-cooled: inadequate/hot/low cooling-water flow, blocked dirt trap, solenoid valve not opening, or air in the system. | Air-cooled: check the fan breaker (set to 110% of rated fan current) and fan motor. Water-cooled: improve water supply, clean the dirt trap, check the solenoid valve, and bleed air. |
| E412 | External Fault (fault) | A device wired to a programmable input signalled a fault (contact opened), e.g. downstream air-treatment equipment. | Find the cause at the external device; see that device's operating instructions. |
| E413 | Dryer (fault) | Fault signal received from an external dryer connected to a programmable input. | Find the cause at the dryer; see the dryer's operating instructions. |
| E415 | No Press. Build-Up (fault) | No pressure build-up during the start-up phase, e.g. the drive motor is turning in the wrong direction. | Find the cause; verify motor rotation direction (phase sequence) on initial installation. |
| E416 | Heavy Startup (fault) | Discharge compression pressure too high during the motor start phase. | Check that the intake regulator is closed and sealing correctly. |
| E419 | Water level min. (fault, water-injected units) | Poor water supply / water pressure too low, faulty water treatment unit, faulty inlet solenoid valve, or faulty water level sensor B10. | Check water pressure and the treatment unit, inspect the inlet solenoid valve, and check level sensor B10 and its wiring. |
| E422 | Phase monitoring (fault) | Incorrect phase sequence or loss of one or more supply phases. | Check and correct phase sequence; check the incoming power supply for a lost phase. |
| E504 | VSD Communication (fault, variable-speed units) | Communication with the frequency converter (VSD) interrupted; the VSD does not respond. | Check the main contactor (PowerFlex 400 VSD only) and the Modbus interface wiring. If no fault found, contact CompAir/Gardner Denver service. |
| E505 | VSD Stop Pressed (fault) | The red Stop button on the frequency converter (VSD) was pressed while the compressor was running. | Always switch the compressor off via the DELCOS XL, not the VSD keypad. |
| E510 | Speed below min. Limit (fault) | Motor speed dropped below the permissible minimum, often from a restricted airend/separator. | Check the fine (oil) separator differential pressure, the oil level, and the water content of the oil. |
| F008 | VSD F008 - Frequency converter overtemperature (variable-speed units) | VSD running too hot: dirty switch-cabinet cooling-air inlet filter, poor cabinet ventilation, blocked VSD cooling path, or dirty cooler fins. | Clean/renew the cabinet air-inlet filter, confirm cabinet and VSD fans run, and clear blockages and dirty fins at the VSD inlet/outlet. |
| F064 | VSD F064 - Frequency converter overload | VSD overloaded, commonly from a restricted airend/separator circuit. | Check the fine-separator differential pressure, the oil level, and the water content of the oil. |
| A600 | Service due (warning, compressor keeps running) | Hours-to-next-service counter has dropped below 200 hours. | Perform the scheduled maintenance per the service instructions, then reset the service interval. |
| A601 | Discharge Over Pressure (warning) - rated pressure exceeded by 1.0 bar / 14 psi | Early over-pressure warning before the E405 shutdown: high system pressure losses, set pressure too high, external demand too high, intake controller not closing, or faulty B1/B2 sensor. | Check remote switching points and the intake controller, correct pressure setpoints, and replace a faulty pressure sensor. |
| A607 | Controller Battery empty (warning) | The DELCOS XL controller backup battery is depleted. | Renew the controller battery (Gardner Denver part no. 100016235). |
| A611 | Air Filter (warning) | Air-filter differential pressure too high (clogged element). | Check and change the air filter element. |
| A616 | Motor lubrication system (warning) | A fault in the automatic motor greasing system, or the grease/LC cartridge is running low. | Service the motor greasing system per the compressor operating instructions; renew the grease cartridge. |
| A623 | SD-Card full (warning) | The data-logger SD card storage space is used up. | Renew the SD card (CompAir part no. ZS1067681). |
| A700 | VSD Temperature High (warning, variable-speed units) | Frequency converter temperature close to its trip point. | Clean/renew the cabinet cooling-air inlet filter, confirm cabinet and VSD fans run, and clear VSD inlet/outlet blockages and dirty fins before it trips to F008. |


## How to troubleshoot Compair Compressor

## How to read CompAir DELCOS fault codes

Most current CompAir rotary screw compressors use the DELCOS XL (on DH-series and L/D/H machines) or the older DELCOS Pro controller. On the DELCOS XL a code is a letter plus a number: **"A" is a warning** (the machine keeps running), while **"E" and "F" are faults** that stop the machine. The number tells you where it came from: the frequency converter (VSD) codes on variable-speed units (F000-F399, E500-E531, A700-A731) versus the compressor's own codes (E400-E495, A600-A695). The controller stores its recent alarms in the Fault History menu, and each stored alarm keeps a snapshot of pressures, temperatures and hours at the moment it tripped, which is the fastest way to see what the machine was actually doing when it failed.

## First moves before you open anything

Clear and read the fault first: on the Fault History tab you cannot reset an alarm whose cause is still present, so a code that will not clear is telling you the condition is still live. Start with the cheap, common causes the manual itself lists again and again for these machines: a fouled cooler or blocked cooling-air path, low or wrong-grade oil, a clogged air filter or oil separator, and loose supply terminals. A very large share of DELCOS shutdowns are heat-related (E403/A602 discharge temperature, F008/A700 on the VSD) and trace back to airflow and oil rather than a failed sensor. Verify supply voltage and phase balance under load at the incoming terminal block, not just at the disconnect, because these controllers are sensitive to phase loss and imbalance (E422, VSD F017/F021).

## Sensor vs. real condition

When a code names a specific sensor (B1 line pressure, B2 discharge pressure, R2 discharge temperature, B10 water level), the manual's remedy is almost always "check, renew if necessary" for both the sensor and its cabling. Before condemning a sensor, confirm the physical condition is genuinely normal, because a real over-temperature or over-pressure event will also throw a code. Cross-check the live reading on the Home/pictogram screen against a second gauge or thermometer.

## Safety and when to call a pro

Rotary screw compressors store pressure and, on variable-speed (RS) units, dangerous DC-bus voltage in the VSD capacitors. Before touching anything electrical, isolate at the main switch, depressurise, and on RS machines wait at least 10 minutes for the capacitors to discharge. DIY-appropriate work is cooler cleaning, filter and separator changes, oil service, checking the fan and its breaker, and tightening terminals. Escalate to an authorized CompAir/Gardner Denver technician for: repeated discharge-temperature shutdowns that survive cooler cleaning and oil service (suspect airend/discharge valve wear), any VSD programming fault (E502/E503) or unexplained VSD communication loss, controller hardware faults (E409, which requires the compressor-specific setup code to swap the controller), and airend rebuilds, which need factory tooling and specifications.


## Frequently asked questions

### What does CompAir fault E403 (Compressor Disch. Temp.) mean and can I fix it myself?

E403 is a discharge-temperature shutdown: the airend outlet temperature exceeded its limit. Common causes are a fouled cooler, high intake/ambient temperature, inadequate cooling, low or wrong-grade oil, or running with the enclosure open. Clean the cooler, check the fan runs at full speed, verify oil level and type, and close the enclosure. If it keeps tripping after all that, suspect airend or discharge-valve wear and call a technician.

### My CompAir shows E400 Power Supply Failure but the power is on. Why won't it restart?

E400 latches after any power interruption, voltage dip, damaged cable, or loose terminal, and it also appears if a power loss lasted longer than the Max. Power Loss Time set for auto-restart. It must be acknowledged in the Fault History menu before the machine will run. Find and fix the supply cause and retighten the incoming terminals first, otherwise it will trip again.

### What's the difference between an A-code and an E-code on the DELCOS XL?

On the DELCOS XL controller, an 'A' code is a warning: the compressor keeps running so you can act before it becomes a shutdown. 'E' and 'F' codes are faults that stop the machine. For example A601 warns of over-pressure at 1.0 bar over rated, while E405 shuts the machine down at 1.5 bar over rated.

### How do I reset a fault on a CompAir DELCOS controller?

Clear the underlying cause first, then tap the Fault History tab and press Reset. The controller will not let you reset an alarm whose cause is still present, so a code that refuses to clear means the condition is still live.

### What causes VSD faults like F008 or E504 on a variable-speed CompAir?

These come from the frequency converter on RS (variable-speed) machines. F008 (and the A700 warning) is VSD overtemperature, usually a dirty switch-cabinet air filter, blocked cooling path, or failed cabinet/VSD fan. E504 is a communication loss with the VSD: check the main contactor and Modbus wiring. Remember the VSD holds a lethal DC-bus charge, so isolate and wait 10 minutes before working inside the cabinet.

