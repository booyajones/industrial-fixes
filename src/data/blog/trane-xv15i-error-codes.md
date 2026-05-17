---
title: "Trane XV15i Heat Pump Error Codes: Complete Variable-Speed Fault Guide"
description: "Every Trane XV15i variable-speed heat pump fault code explained with diagnostics, DIY fixes, parts, and when to call a pro."
pubDatetime: 2026-04-25T00:00:00Z
author: "Marcus Webb"
tags:
  - hvac
  - error-codes
---

The Trane XV15i is a variable-speed heat pump that uses an inverter-driven compressor to match heating and cooling output to actual home demand. Unlike single or two-stage units, the XV15i can run at speeds anywhere between about 30% and 100% capacity, which results in more consistent temperatures, lower humidity, and significantly reduced energy consumption during moderate weather.

The trade-off for this sophistication is a more complex fault code system. The XV15i combines LED diagnostics on the outdoor control board with the full ComfortLink II communicating system when paired with a compatible Trane thermostat. This guide covers every fault code in both systems and tells you what to do about each one.

## What Does the Trane XV15i Fault Code System Mean?

The XV15i uses a single-LED system on the outdoor board for standalone diagnostics and full alphanumeric ComfortLink II codes when connected to a compatible thermostat (XL950, XL850, or XL824).

**Reading LED codes:** Count amber LED blinks, wait for the pause, then count again. On the XV15i, some codes use a pause-then-resume pattern to indicate the second digit.

**Accessing ComfortLink II codes:** On your thermostat, navigate to Menu → System → Diagnostics → Active Faults or Fault History.

### Complete Fault Code Reference

| LED Flashes | ComfortLink Code | Fault Description | Priority |
|---|---|---|---|
| 2 | 179 | High-pressure switch open | High |
| 3 | 180 | Low-pressure switch open | High |
| 4 | 182 | Outdoor coil sensor out of range | Medium |
| 5 | 181 | High discharge temperature | High |
| 6 | 185 | Compressor over-temperature | High |
| 7 | 193 | Low supply voltage | Medium |
| 8 | 191 | Reversing valve fault | High |
| 9 | 189 | Outdoor fan motor fault | Medium |
| 10 | 195 | Communication bus fault | Medium |
| 11 | 186 | Compressor start failure | High |
| 12 | 200 | Inverter drive fault | High |
| 13 | 201 | Inverter over-temperature | High |
| 14 | 202 | Inverter DC bus under-voltage | Medium |
| 15 | 203 | Inverter DC bus over-voltage | Medium |
| 16 | 198 | Defrost sensor fault | Medium |
| 17 | 183 | Low ambient temperature lockout | Low |
| 18 | 204 | Variable-speed compressor current limit | High |

## How to Fix It

### Code 12 / ComfortLink 200, Inverter Drive Fault

This is the code most unique to the XV15i's variable-speed operation. The inverter drive controls compressor speed and is the heart of what makes this unit different from standard heat pumps.

1. **Cut power at the outdoor disconnect.** Wait 5 full minutes before restoring power. The inverter's DC bus capacitors hold charge after power loss, a full 5-minute wait allows them to discharge completely and gives the drive a full reset.
2. **Check outdoor coil airflow.** The inverter module runs hot. Blocked coil fins or a failed outdoor fan motor causes inverter over-temperature faults (Code 13) that can cascade into Code 12.
3. **Check supply voltage.** The XV15i requires 208/230VAC ±10%. Voltage below 187V stresses the inverter and triggers under-voltage faults (Code 14) that can damage the drive over time.
4. **Inspect the inverter module** in the outdoor electrical compartment for visible damage: bulged capacitors, burn marks, or corrosion.
5. **A Code 12 that returns within 30 minutes of reset** almost always indicates inverter module failure. This is a warranty repair on units within the 10-year parts coverage period.

### Code 13 / ComfortLink 201, Inverter Over-Temperature

1. **Clean the outdoor coil immediately.** Dirty coils force higher head pressure, which generates more heat in the inverter.
2. **Verify outdoor fan operation.** The fan must run any time the compressor runs.
3. **Check inverter heat sink.** Some XV15i inverter modules have a dedicated heat sink. Verify it isn't blocked with dirt or debris.
4. **If temperature is extreme** (outdoor ambient above 110°F), the over-temperature fault may be temporary, restart after the hottest part of the day passes.

### Code 2 / ComfortLink 179, High-Pressure Switch Open

1. **Clean the outdoor coil** using coil cleaner spray and a gentle garden hose rinse (inside to outside, low pressure).
2. **Confirm the outdoor fan is running at correct speed.** On the XV15i, the fan speed modulates with compressor speed, a fan running at significantly reduced speed when the compressor is working hard will cause high pressure.
3. **Check clearances**, minimum 18 inches on all sides and 48 inches above the unit.
4. **Refrigerant overcharge** is the other common cause. Only a certified technician can diagnose and correct this.

### Code 3 / ComfortLink 180, Low-Pressure Switch Open

1. **Check the indoor air filter.** Replace if it's been in service more than 60–90 days.
2. **Look for ice on the indoor coil or lineset.** Shut off the system, run fan-only mode for 2–3 hours to thaw.
3. **Verify suction service valve is fully open** (the larger copper line at the outdoor unit, counterclockwise to open).
4. **Check indoor blower operation.** If the blower isn't running or is running slowly, the indoor coil will ice up quickly.
5. **Refrigerant leak**, if the fault returns after addressing the above, have a technician check for leaks.

### Code 4 / ComfortLink 182, Outdoor Coil Sensor Out of Range

1. **Locate the sensor** on the outdoor coil, usually near the base at the 6 o'clock position.
2. **Inspect the two-wire harness** running from the sensor to the control board. Chafing against the coil frame is the most common failure point.
3. **Test resistance.** At 77°F: ~10,000–12,000 ohms. At 32°F: ~32,000–35,000 ohms. Open or shorted = replace.
4. **Re-clip replacement sensor** firmly against the coil and route harness away from vibration points.

### Code 7 / ComfortLink 193, Low Supply Voltage

1. **Measure voltage at the contactor input terminals**, should be within 10% of nameplate (usually 208/230VAC).
2. **Check the outdoor disconnect** for loose, corroded, or heat-damaged connections. Low voltage at the unit with good voltage at the panel = problem in the disconnect or wiring run.
3. **Check contactor contact resistance.** Pitted contacts add resistance and effectively reduce voltage to the compressor.
4. **Persistent low voltage across all conditions** may indicate an undersized circuit or a utility voltage issue, contact an electrician.

### Code 8 / ComfortLink 191, Reversing Valve Fault

1. **Confirm mode confusion.** Switch from cooling to heating at the thermostat and listen at the outdoor unit for a thump from the valve shifting.
2. **Check solenoid voltage** on a mode change call, should be 24VAC at the solenoid terminals.
3. **Test solenoid resistance**, 10–30 ohms normal, open or shorted = replace solenoid.
4. **If solenoid tests good but valve won't shift**, mechanical valve failure, requires technician and brazing equipment.

### Code 9 / ComfortLink 189, Outdoor Fan Motor Fault

1. **Disconnect power and check blade for obstructions.**
2. **Test the run capacitor**, this is the most common fan motor fault.
3. **Test motor windings**, open winding = replace motor.
4. **On the XV15i**, the fan is also variable speed. If the motor is the variable-speed ECM type, verify the control signal from the inverter board as well.

### Code 10 / ComfortLink 195, Communication Fault

1. **Inspect ComfortLink II data cable** between indoor and outdoor units (two conductors, A and B).
2. **Power cycle both units** simultaneously for 60 seconds.
3. **Check both board power supplies.** No 24VAC = no communication.
4. **Try reversing A and B** at one end, polarity sensitivity varies.

### Code 16 / ComfortLink 198, Defrost Sensor Fault

1. **Locate sensor** clipped to outdoor coil.
2. **Check harness integrity**, two wires from sensor to board.
3. **Measure resistance.** Should read approximately 10K–12K ohms at room temperature.
4. **Replace sensor if out of range** (see Parts table).

### Code 18 / ComfortLink 204, Variable-Speed Compressor Current Limit

This fault indicates the inverter is limiting compressor current due to excessive load or a compressor that's drawing more current than expected.

1. **Check outdoor coil cleanliness.** High head pressure increases compressor current.
2. **Verify refrigerant charge is correct.** Overcharge increases compression work.
3. **If the fault appears consistently at startup**, the compressor may be developing mechanical wear. Have a technician check.

## Parts You May Need

| Part | Use | Link |
|---|---|---|
| Dual Run Capacitor (45+5 µF, 440V) | Fan motor start fault (Code 9) | [View on Amazon](https://www.amazon.com/dp/B01M05L7B3?ascsubtag=ecf-trane-xv15i-error-codes&tag=errorcodefixes-20) |
| 2-Pole 30A HVAC Contactor | Low voltage from pitted contacts | [View on Amazon](https://www.amazon.com/dp/B0CJFZQVPT?ascsubtag=ecf-trane-xv15i-error-codes&tag=errorcodefixes-20) |
| Outdoor Coil Temperature Sensor | Codes 4/16, ComfortLink 182/198 | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-trane-xv15i-error-codes&k=trane+outdoor+coil+sensor+thermistor&tag=errorcodefixes-20) |
| Reversing Valve Solenoid Coil | Code 8, ComfortLink 191 | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-trane-xv15i-error-codes&k=reversing+valve+solenoid+24v+coil&tag=errorcodefixes-20) |
| Condenser Fan Motor (1/4 HP, 230V) | Code 9 fan motor replacement | [View on Amazon](https://www.amazon.com/dp/B0D2L5NSMM?ascsubtag=ecf-trane-xv15i-error-codes&tag=errorcodefixes-20) |
| 18/2 ComfortLink Communication Wire | Code 10 communication faults | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-trane-xv15i-error-codes&k=hvac+thermostat+wire+18+gauge+2+conductor&tag=errorcodefixes-20) |

## When to Call a Pro

**Safe for homeowners:** Coil cleaning, capacitor replacement, contactor replacement, sensor replacement, reversing valve solenoid swap, power cycling, communication wire checks.

**Technician required:**
- **Inverter module replacement (Code 12/13).** On a unit within warranty, Trane covers the inverter module under the 10-year parts warranty, require factory service for warranty claim. On an out-of-warranty unit, get a full system quote before approving an expensive inverter module replacement.
- **Any persistent refrigerant code (2 or 3).** EPA 608 certification required.
- **Reversing valve brazing.** Requires nitrogen, torch, and refrigerant handling.
- **Compressor replacement on XV15i.** The variable-speed scroll compressor is a major cost item. On a unit over 8 years old, compare repair vs. replacement costs carefully.

## FAQ

**How is the XV15i different from the XL18i in terms of fault codes?**
Both units share the same ComfortLink II code structure for standard faults (pressure switches, sensors, reversing valve). The XV15i adds the inverter-specific faults (Codes 12–15, 18) that the XL18i doesn't have. The XV15i's inverter drive is more complex to diagnose and more expensive to replace.

**My XV15i runs constantly at very low speed. Is something wrong?**
No, this is normal variable-speed operation. On mild days, the unit modulates down to minimum capacity and runs for extended periods. This is more efficient than short-cycling. It only becomes a problem if the unit can't maintain setpoint at full capacity in extreme weather.

**I see Code 14 (DC bus under-voltage) only on very cold mornings. What's happening?**
Low-voltage faults on cold mornings are often caused by high compressor current draw at startup before the crankcase heater has fully warmed the refrigerant. The crankcase heater runs whenever the compressor is off and the outdoor temperature is low. Check that the crankcase heater is functional, it should be warm to the touch after the unit has been off for an hour in cold weather.

**ComfortLink 204 appeared twice this week, then cleared. Should I do anything?**
Code 204 (current limit) is a soft fault that clears automatically when load drops. Occasional appearances during peak heat (above 95°F outdoor temp) can be normal for a loaded system. Repeated appearances across moderate temperatures suggest an overcharged refrigerant system or early compressor wear. Have a technician check.

**Does the XV15i have a test mode I can use to check operation before calling a technician?**
Yes, from the ComfortLink II thermostat, go to Menu → System → Test Mode. This allows you to run the compressor, indoor fan, and outdoor fan independently to isolate faults. This is extremely useful before a service call because you can confirm whether each component responds to a command.
