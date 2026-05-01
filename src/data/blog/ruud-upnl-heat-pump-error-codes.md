---
title: "Ruud UPNL Heat Pump Error Codes - What It Means and How to Fix It"
description: "Ruud UPNL Prestige variable-speed heat pumps use communicating diagnostics to report pressure, sensor, fan, reversing valve, and control board faults. This guide explains the most common UPNL error codes and the repair steps that usually solve them."
pubDatetime: 2026-04-25T00:00:00Z
author: "Dana Kowalski"
tags:
  - hvac
  - error-codes
---

The Ruud UPNL Prestige series is one of the most capable variable-speed heat pump lines on the market, but like any sophisticated communicating system, it generates fault codes when something goes wrong. These codes appear on the thermostat display or EcoNet controller and can seem cryptic without a proper reference. This guide covers every major fault code for the UPNL platform, explains what the system is actually telling you, and gives you actionable steps to resolve each one.

## What Does Ruud UPNL Heat Pump Error Codes Mean?

The UPNL (Ultra Performance Non-communicating/communicating Low ambient) heat pump uses Ruud's communicating EcoNet platform. Unlike older systems that relied on LED blink codes alone, the UPNL reports numerical and alphanumeric fault codes through the thermostat or EcoNet Wi-Fi module. These codes are stored in fault history and can be retrieved even after the unit resets.

The communicating system means the outdoor unit, air handler, and thermostat are all sending data to each other constantly. When the outdoor control board detects an abnormal condition, it transmits the fault code to the thermostat display and logs it internally. This is important to understand because the fault code often points to the *detecting* component, not always the *failed* component.

### Common Ruud UPNL Fault Code Reference

**Code 1 / Fault 01 - High Pressure Lockout**
The system detected refrigerant pressure above the safe operating limit on the high side. This trips the high-pressure switch (HPS) and shuts down the compressor.

Causes: dirty condenser coil, failed condenser fan motor, refrigerant overcharge, blocked airflow around the outdoor unit, failed high-pressure switch.

**Code 2 / Fault 02 - Low Pressure Lockout**
Low-side refrigerant pressure dropped below the cutout threshold. The low-pressure switch (LPS) tripped.

Causes: refrigerant leak, dirty indoor evaporator coil (restricted airflow), failed TXV or expansion device, low ambient temperature startup without low-ambient kit.

**Code 3 / Fault 03 - Outdoor Ambient Sensor Fault**
The outdoor ambient temperature thermistor is reading out of range. The control board cannot accurately determine operating conditions.

Causes: failed thermistor (open or shorted circuit), damaged wiring harness, moisture intrusion into the sensor connector.

**Code 4 / Fault 04 - Discharge Temperature Sensor Fault**
The discharge line thermistor is reading out of normal range. The system uses this sensor to protect the compressor from overheating.

Causes: failed discharge thermistor, wiring fault between sensor and control board.

**Code 5 / Fault 05 - Suction Temperature Sensor Fault**
The suction line thermistor is reporting an out-of-range value.

Causes: failed suction thermistor (part number 62-103189-01 for compatible Ruud/Rheem sensors), damaged harness connector.

**Code 6 / Fault 06 - Communicating System Fault / Loss of Communication**
The outdoor unit has lost communication with the air handler or thermostat. This is one of the most common codes on the UPNL platform.

Causes: loose or damaged communication wiring (the 4-wire communication bus between indoor and outdoor units), failed indoor control board, failed outdoor control board, power interruption to either component.

**Code 7 / Fault 07 - Reversing Valve Fault**
The reversing valve failed to shift from heating to cooling mode or vice versa. This is a critical fault that prevents mode switching.

Causes: failed reversing valve solenoid coil, stuck reversing valve spool, low refrigerant charge (the valve needs sufficient pressure differential to shift), wiring fault to the solenoid.

**Code 8 / Fault 08 - Outdoor Fan Motor Fault**
The variable-speed ECM outdoor fan motor reported a fault or failed to reach commanded speed.

Causes: failed ECM fan motor, failed capacitor (on PSC motors in some configurations), blocked fan blade, failed motor control module.

**Code 9 / Fault 09 - Compressor High Temperature**
The discharge temperature exceeded the safe limit for the compressor. This is a protective lockout.

Causes: low refrigerant charge (most common), dirty coils reducing heat transfer, failed discharge thermistor, failed TXV causing refrigerant flooding.

**Code 10 / Fault 10 - Defrost Thermostat / Sensor Fault**
The defrost control thermostat or outdoor coil temperature sensor is not reading correctly, which prevents proper defrost cycle initiation.

Causes: failed defrost thermostat (clip-on type), damaged wiring.

**Code 11 / Fault 11 - Compressor Overcurrent / IPM Fault**
The inverter power module (IPM) that drives the variable-speed compressor detected an overcurrent condition or internal fault.

Causes: failed compressor (winding fault), failed IPM/inverter board, voltage imbalance from the utility, loose power connections.

**Code 12 / Fault 12 - Low Voltage Fault**
Control voltage (24VAC) dropped below minimum threshold.

Causes: failed transformer in air handler, overloaded 24V circuit (too many accessories), failed thermostat wiring.

**Code 13 / Fault 13 - Anti-Short Cycle Lockout**
The system is in a protective delay after a rapid cycling event. This is a timer-based lockout, not a hardware failure.

Action: Wait 5 minutes. If the code clears and the unit runs normally, investigate what caused the original short cycle (pressure faults, power interruptions).

**Code 17 / Fault 17 - EcoNet Communication Fault**
The EcoNet Wi-Fi module lost communication with the control board.

Causes: failed EcoNet module, Wi-Fi configuration issue, firmware mismatch.

**Code 25 / Fault 25 - Defrost Demand Defrost Fault**
System entered demand defrost but did not complete the cycle within expected time limits.

Causes: severely iced coil (underlying low-charge issue), failed defrost relay, failed outdoor coil sensor.

## How to Fix It

**Step 1: Retrieve and record the full fault history.**
On the EcoNet thermostat, navigate to Menu > Equipment Status > Fault History. Write down all active and historical faults. Multiple codes stored together often tell a story - for example, Fault 02 followed by Fault 09 suggests a refrigerant leak that then caused compressor overheating.

**Step 2: Power cycle the system.**
Turn the thermostat to OFF. Shut off the outdoor disconnect switch. Wait 5 full minutes. Restore power. Some transient faults (communication errors from a power flicker, anti-short cycle lockouts) will clear on their own.

**Step 3: For Code 6 (communication fault), inspect the communication wiring.**
Check the 4-wire bus between the air handler and outdoor unit. Look for wires pinched in the door panel, loose terminals at the control board, or wires that have been chewed by rodents. The bus typically runs on terminals C, R, Y, and a dedicated communication wire labeled "C" or "Comm" depending on the thermostat wiring. Measure resistance between terminals - an open circuit (infinite resistance) confirms a broken wire.

**Step 4: For Code 7 (reversing valve), test the solenoid.**
With the unit powered down, disconnect the solenoid coil leads and measure resistance with a multimeter. A healthy solenoid coil reads 20-30 ohms. An open circuit (OL) or shorted reading (less than 5 ohms) confirms coil failure. Replacement coils are available without replacing the entire valve body. If the coil tests good, check for adequate refrigerant charge - a severe undercharge prevents the valve from shifting.

**Step 5: For pressure faults (Code 1, Code 2), inspect coils and airflow.**
A high-pressure fault (Code 1) in cooling mode almost always means either a dirty condenser coil or a failed outdoor fan. Wash the condenser coil with a garden hose from the inside out. Verify the outdoor fan runs at correct speed. For a low-pressure fault (Code 2), look for ice on the suction line or indoor coil, which indicates low refrigerant or severely restricted airflow. Check the indoor filter first.

**Step 6: For Code 11 (IPM / inverter fault), check power quality.**
Measure voltage at the outdoor unit disconnect with the unit running. Voltage should be within ±10% of nameplate (typically 208-230VAC). Voltage sag below 195V during startup can trip the IPM fault. If voltage is normal and the fault persists, the IPM board (inverter drive) requires replacement - this is a refrigerant-system-adjacent repair that should be done by a licensed technician.

**Step 7: For sensor faults (Codes 3, 4, 5), test thermistors.**
Disconnect the suspect sensor and measure resistance with a calibrated ohmmeter at known temperature. At 77°F (25°C), most Ruud NTC thermistors read approximately 10,000 ohms (10kΩ). At 32°F (0°C), resistance rises to roughly 32,000 ohms. A reading of 0 ohms or OL (open) confirms sensor failure.

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|-------------|
| [Ruud/Rheem Outdoor Control Board (Part # 62-25338-01)](https://www.amazon.com/dp/B0CNZGZ1HS?tag=errorcodefixes-20) | Replaces failed main outdoor control board causing communication or sensor faults | $180-$320 |
| [Reversing Valve Solenoid Coil (Part # 62-101684-04)](https://www.amazon.com/s?k=Ruud+reversing+valve+solenoid+coil&tag=errorcodefixes-20) | Replaces failed solenoid coil on reversing valve without replacing full valve | $35-$65 |
| [NTC Thermistor Sensor (Part # 62-103189-01)](https://www.amazon.com/s?k=Ruud+Rheem+NTC+thermistor+10k+HVAC+sensor&tag=errorcodefixes-20) | Replaces failed outdoor ambient, discharge, or suction temperature sensors | $15-$30 |
| [EcoNet Wi-Fi Control Module (Part # RWFIO-W01B)](https://www.amazon.com/s?k=Ruud+EcoNet+WiFi+module+RWFIO&tag=errorcodefixes-20) | Replaces failed EcoNet communicating module | $95-$145 |
| [Defrost Control Thermostat (Part # 47-102038-01)](https://www.amazon.com/s?k=Ruud+Rheem+defrost+thermostat+47-102038&tag=errorcodefixes-20) | Replaces failed clip-on defrost thermostat on outdoor coil | $12-$25 |
| [ECM Outdoor Fan Motor](https://www.amazon.com/dp/B0D2L5NSMM?tag=errorcodefixes-20) | Replaces failed variable-speed outdoor condenser fan motor | $220-$450 |

## When to Call a Pro

Some UPNL faults are straightforward DIY fixes - cleaning coils, replacing a sensor, or checking wiring. Others require a licensed HVAC technician with EPA 608 certification:

- **Any refrigerant-related fault** (Codes 1, 2, 9): Adding or recovering refrigerant requires EPA 608 certification and proper equipment.
- **Compressor fault (Code 11) with IPM failure**: The inverter drive board is expensive and adjacent to refrigerant components - improper handling risks additional damage.
- **Reversing valve body replacement**: Requires refrigerant recovery, brazing, and recharge.
- **Persistent Code 6 after wiring inspection**: Board-to-board communication failures may require factory-level diagnostics through the EcoNet portal.

If the fault history shows more than 3 different codes logged in a short period, have a technician perform a full system evaluation before replacing individual parts.

## Frequently Asked Questions

**Q: My Ruud UPNL shows Code 6 every morning but clears on its own. Is this serious?**
A: Morning communication faults that self-clear often trace to the outdoor unit losing 24VAC power briefly at night due to a marginal transformer or a loose low-voltage connection that expands and contracts with temperature. Check all communication wire terminals at both the air handler and outdoor control board. Intermittent Code 6 that goes on for months without resolution can eventually damage the control boards from repeated power cycling.

**Q: The reversing valve fault (Code 7) appeared right after a cold snap. Could it be temperature-related?**
A: Yes. Reversing valves rely on the pressure differential between high and low sides to shift the spool. In very cold weather (below 15°F), some units don't build enough pressure for a clean shift. If your UPNL doesn't have a low-ambient kit and you're in a cold climate, this is worth addressing with your HVAC contractor. Also verify the solenoid coil has correct 24VAC voltage at the terminals during a mode-change command.

**Q: How do I clear the fault history on the EcoNet thermostat?**
A: Navigate to Menu > Equipment Status > Fault History and select "Clear Fault History." Note that clearing faults before a technician diagnoses the issue can make diagnosis harder - screenshot or write down all fault codes first.

**Q: Can I replace the outdoor control board myself?**
A: The control board itself doesn't contain refrigerant and is a swap-and-go replacement in most cases. Power down the unit at the disconnect, photograph all wiring connections before removal, and match the replacement board part number exactly. However, if the board failure was caused by a compressor fault or voltage spike, replacing the board without finding the root cause means the new board may fail too.

**Q: The unit runs fine in cooling but shows Code 7 only in heating mode. What does that mean?**
A: This is a classic reversing valve symptom. In cooling mode, the valve sits in its un-energized (default) position - there's no coil activation needed. In heating mode, 24VAC must energize the solenoid coil to shift the valve spool to the heating position. If Code 7 only appears in heating, test the solenoid coil resistance and verify 24VAC is present at the solenoid terminals when the thermostat calls for heat.
