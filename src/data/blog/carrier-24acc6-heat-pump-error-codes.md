---
title: "Carrier 24ACC6 Heat Pump Error Codes: Complete Diagnostic Guide"
description: "Decode every Carrier 24ACC6 Comfort series heat pump flash code and fault. Step-by-step diagnostics, parts, and when to call a pro."
pubDatetime: 2026-04-25T00:00:00Z
author: "Marcus Webb"
tags:
  - hvac
  - error-codes
---

The Carrier 24ACC6 is a mid-tier Comfort series heat pump that homeowners and technicians trust for reliable year-round performance. When something goes wrong, the unit communicates through a series of LED flash codes on the control board. Knowing how to read those codes cuts your diagnostic time in half and helps you decide whether a DIY fix will do or if it's time to call a technician.

This guide covers every flash code the 24ACC6 produces, what each one means, and exactly how to address it.

## What Does the Carrier 24ACC6 Flash Code System Mean?

The 24ACC6 control board uses a single amber LED to communicate fault conditions. The LED blinks a sequence of short and long pulses, pauses, then repeats. You count the blinks to identify the fault code. The unit also stores the last three fault codes in memory, which you can retrieve even after the fault clears.

**How to read flash codes:**
1. Locate the control board, it sits in the electrical compartment behind the access panel.
2. Count the number of blinks before the long pause. That number is your fault code.
3. Cross-reference with the table below.

If the LED is solid on, the board has power but no call for operation. If it's solid off, you have a power or board failure.

| Flash Code | Fault Description | Priority |
|---|---|---|
| 1 flash | Normal operation / standby | None |
| 2 flashes | High-pressure trip | High |
| 3 flashes | Low-pressure trip | High |
| 4 flashes | Outdoor coil defrost sensor fault | Medium |
| 5 flashes | Discharge temperature sensor fault | Medium |
| 6 flashes | Compressor over-temperature | High |
| 7 flashes | Low voltage to control board | Medium |
| 8 flashes | Reversing valve fault (stuck or failed) | High |
| 9 flashes | Outdoor fan motor fault | Medium |
| 11 flashes | Communication fault (to air handler/furnace) | Medium |
| 12 flashes | Compressor start failure | High |

## How to Fix It

### Code 2, High-Pressure Trip

High pressure usually means restricted airflow across the outdoor coil or an overcharge of refrigerant.

1. **Check the outdoor coil for debris.** Grass clippings, cottonwood, and dirt block airflow and spike discharge pressure. Rinse the coil with a garden hose from the inside out.
2. **Verify outdoor fan operation.** The fan should run during both cooling and heating. If the blade spins slowly or not at all, test the capacitor first (see Parts table).
3. **Check refrigerant charge.** If coil is clean and fan is good, call a certified technician, only a licensed HVAC pro can legally handle refrigerant.
4. **Reset the fault.** Cut power to the unit at the disconnect box for 30 seconds, restore power, and watch for recurrence.

### Code 3, Low-Pressure Trip

Low pressure points to refrigerant loss, a dirty indoor coil, or a frozen evaporator.

1. **Check the indoor air handler filter.** A clogged filter starves the indoor coil and causes evaporator freeze-up, which reads as low suction pressure.
2. **Look for ice on the indoor coil or lineset.** If you see frost, shut the system off and run fan-only mode for 2–3 hours to thaw.
3. **Inspect service valve positions.** Both the suction and liquid line valves must be fully open (counterclockwise).
4. **If neither step resolves the code**, refrigerant leak is likely, call a technician.

### Code 4, Outdoor Coil Defrost Sensor Fault

The defrost sensor tells the board when the outdoor coil gets too cold in heating mode.

1. **Locate the sensor.** It clips onto the outdoor coil fin near the base of the coil.
2. **Check the wire harness.** Disconnected, chafed, or corroded wires cause false sensor faults more often than actual sensor failure.
3. **Test sensor resistance.** At 32°F the sensor should read approximately 10,000 ohms. At 77°F it should read around 5,000 ohms. A reading of 0 or infinite ohms means the sensor is bad.
4. **Replace the sensor** if resistance is out of range (see Parts table).

### Code 6, Compressor Over-Temperature

This fault protects the compressor from heat damage. It triggers when the discharge line thermistor reads above approximately 270°F.

1. **Check refrigerant charge.** Low refrigerant causes high compression ratios and extreme discharge temps.
2. **Inspect the discharge line insulation.** Missing insulation on the hot gas line contributes to heat buildup.
3. **Verify head pressure.** If pressure is normal and the code keeps returning, the thermistor itself may be faulty.

### Code 7, Low Voltage

The control board needs 24VAC to operate reliably. Low voltage can cause random lockouts.

1. **Measure the transformer secondary voltage.** Should read 24–28VAC at the board R and C terminals.
2. **Check for shorted control wiring.** A short pulls voltage down across the transformer.
3. **Replace the transformer** if it reads below 20VAC under load.

### Code 8, Reversing Valve Fault

The reversing valve shifts the refrigerant flow between heating and cooling modes. A stuck valve means you get heat when you want cooling, or vice versa.

1. **Listen at the outdoor unit.** You should hear a distinctive click when the valve shifts.
2. **Check the solenoid coil.** Verify 24VAC is reaching the solenoid during a mode switch.
3. **Test solenoid resistance.** Most reversing valve solenoids read 10–30 ohms. Open or shorted = replace solenoid or full valve.

### Code 11, Communication Fault

The 24ACC6 communicates with the indoor unit over a two-wire bus.

1. **Inspect the communication wire** (typically labeled T and T or W1/W2) for damage, staple punctures, or loose connections.
2. **Verify both indoor and outdoor boards have power.**
3. **Swap communication wires at one end** to check for a wiring polarity issue.

### Code 12, Compressor Start Failure

1. **Check the run capacitor.** A weak or failed capacitor is the most common cause of start failure (see Parts table).
2. **Test compressor windings** with a multimeter. Common to start, common to run, and start to run should all show low resistance. Open or shorted = failed compressor.
3. **Verify supply voltage** at the contactor, should be within 10% of nameplate voltage.

## Parts You May Need

| Part | Use | Link |
|---|---|---|
| Dual Run Capacitor (45+5 µF, 370/440V) | Fan motor and compressor start issues | [View on Amazon](https://www.amazon.com/dp/B01M05L7B3?tag=errorcodefixes-20) |
| Defrost/Coil Temperature Sensor | Code 4 defrost sensor fault | [View on Amazon](https://www.amazon.com/dp/B09FFFPF5L?tag=errorcodefixes-20) |
| Contactor 2-Pole 30A | Pitted contacts causing voltage drops | [View on Amazon](https://www.amazon.com/dp/B0CJFZQVPT?tag=errorcodefixes-20) |
| 24V HVAC Control Board Transformer | Low voltage fault (Code 7) | [View on Amazon](https://www.amazon.com/s?i=industrial&k=hvac+24v+transformer+40va&tag=errorcodefixes-20) |
| Reversing Valve Solenoid Coil | Code 8 reversing valve fault | [View on Amazon](https://www.amazon.com/s?i=industrial&k=reversing+valve+solenoid+coil+hvac&tag=errorcodefixes-20) |

## When to Call a Pro

Handle these yourself: coil cleaning, filter changes, capacitor and contactor swaps, sensor replacements, and wiring checks.

Call a licensed HVAC technician for:
- **Any refrigerant-related code** (Codes 2 and 3 that don't clear after cleaning and resetting). Refrigerant handling requires an EPA 608 certification.
- **Compressor failure** (Code 12 that persists after capacitor replacement). Compressor replacement on a mid-tier heat pump often approaches the cost of a new unit, get a quote on both.
- **Reversing valve replacement** (Code 8 after solenoid swap). The valve requires nitrogen purging and brazing, not a DIY job.
- **Repeated high-pressure trips** that return within hours of a reset. This usually signals an overcharge that needs professional gauges.

## FAQ

**How do I clear stored fault codes on the Carrier 24ACC6?**
The last three fault codes are stored in the board's memory and display automatically on startup. To clear them, power the unit off at the disconnect, wait 30 seconds, and restore power. The board will reset. If the underlying problem hasn't been fixed, the code will return quickly.

**My 24ACC6 is short-cycling. Is there a specific error code for that?**
Short cycling doesn't always generate its own flash code, it often shows up as repeated Code 2 (high pressure) or Code 3 (low pressure) faults. Check the timestamps if your thermostat logs runtimes. Cycles under 5 minutes are a red flag. Dirty coil, low refrigerant, and oversizing are the most common causes.

**The outdoor fan runs but the compressor doesn't start. What code should I see?**
You'll most likely see Code 12 (compressor start failure). First thing to test: the run capacitor. A capacitor test using a multimeter's capacitance function takes under two minutes and resolves the problem roughly 40% of the time. If the capacitor tests good, move on to compressor winding resistance.

**Can I run my 24ACC6 in emergency heat while I wait for a repair?**
Yes. If your system is paired with an air handler or furnace that has backup electric or gas heat, switch your thermostat to Emergency Heat mode. This bypasses the heat pump compressor entirely and runs backup heat only. It's less efficient but keeps you comfortable while you wait.

**What does it mean if the LED never blinks, it's just solid amber?**
A solid amber LED means the board has 24VAC power but is not receiving a call from the thermostat. Check your thermostat settings and wiring first. If the thermostat is calling for heat or cooling and the LED stays solid, you likely have a wiring break between the thermostat and the outdoor unit.
