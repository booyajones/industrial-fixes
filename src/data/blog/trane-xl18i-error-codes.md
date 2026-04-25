---
title: "Trane XL18i Heat Pump Error Codes: Flash Codes and ComfortLink II Faults"
description: "Complete Trane XL18i heat pump error code guide covering LED flash codes and ComfortLink II communicating faults from the 2012–2022 production era."
pubDatetime: 2026-04-25T00:00:00Z
author: errorcodefixes.com
tags:
  - hvac
  - error-codes
---

The Trane XL18i was a flagship two-stage heat pump produced from roughly 2012 through 2022. Built around Trane's Climatuff compressor and designed to work with the ComfortLink II communicating system, the XL18i offered 18 SEER efficiency and a long track record of reliability. Millions of units are still in service, and when they fault, owners need clear answers.

The XL18i uses a dual diagnostic approach: a single-LED flash code system on the outdoor control board for standalone diagnostics, and the full ComfortLink II fault code library when paired with a communicating thermostat (XL950, XL850, or XL824). This guide covers both.

## What Does the Trane XL18i Flash Code System Mean?

The outdoor control board on the XL18i has a single amber LED. The LED blinks in sequences separated by a pause. Count the blinks between pauses to identify the fault.

**ComfortLink II codes** appear as four-digit alphanumeric codes on compatible Trane communicating thermostats. Access them through Menu → System → Diagnostics on the thermostat screen.

### LED Flash Code Reference

| Flash Sequence | Fault | Notes |
|---|---|---|
| 2 blinks | High-pressure trip | Most common fault |
| 3 blinks | Low-pressure trip | Second most common |
| 4 blinks | Outdoor coil sensor fault | Usually a wiring issue |
| 5 blinks | Discharge temperature limit | High refrigerant temp |
| 6 blinks | Compressor over-temperature | Thermal protector activated |
| 7 blinks | Low supply voltage | Check disconnect and wiring |
| 8 blinks | Reversing valve fault | Heat/cool mode confusion |
| 9 blinks | Outdoor fan motor fault | Capacitor or motor |
| 10 blinks | Communication fault | ComfortLink II bus issue |
| 11 blinks | Compressor start failure | Capacitor, contactor, or compressor |

### ComfortLink II Fault Code Reference

| Code | Description |
|---|---|
| 179 | High-pressure switch open |
| 180 | Low-pressure switch open |
| 181 | High discharge temperature |
| 182 | Outdoor coil sensor out of range |
| 183 | Low ambient temperature lockout |
| 185 | Compressor over-temperature |
| 186 | Compressor start failure |
| 189 | Outdoor fan motor fault |
| 191 | Reversing valve fault |
| 193 | Low supply voltage lockout |
| 195 | Outdoor board communication loss |
| 198 | Defrost sensor fault |

## How to Fix It

### Flash Code 2 / ComfortLink 179, High-Pressure Trip

High discharge pressure typically means the outdoor coil can't shed heat fast enough, or refrigerant is overcharged.

1. **Clean the outdoor coil.** The XL18i's coil uses a tight fin spacing that traps cottonwood, grass, and debris. Use a coil cleaning spray (no-rinse type) and rinse from the inside out with a garden hose at low pressure.
2. **Check outdoor fan blade and motor.** The fan should run at full speed during cooling and continue running during heating unless in defrost mode. A slow fan = capacitor failure (see Parts table).
3. **Verify clearance around the unit.** Trane requires a minimum of 18 inches of clearance on all sides. Fences, shrubs, and patio furniture blocking airflow can trigger high-pressure faults in summer.
4. **Don't attempt refrigerant adjustment yourself.** If the coil is clean and the fan is good and the fault persists, have a technician check the refrigerant charge.

### Flash Code 3 / ComfortLink 180, Low-Pressure Trip

1. **Replace the indoor air filter.** A filter that hasn't been changed in 3+ months restricts airflow, causes the indoor coil to freeze, and drops suction pressure.
2. **Check for indoor coil ice.** Look through the blower access panel or air handler cabinet. Ice on the coil = shut system off, run fan-only for 2–3 hours.
3. **Check the suction line service valve.** Located on the larger of the two copper lines at the outdoor unit. Fully open = counterclockwise until it stops.
4. **If the fault returns after the filter is clean and the coil is clear**, refrigerant leak is likely. Call a technician.

### Flash Code 4 / ComfortLink 182, Outdoor Coil Sensor Fault

The coil sensor controls defrost initiation and prevents the compressor from running when the outdoor temperature is below the low-ambient cutoff.

1. **Locate the sensor.** It clips onto the lower outdoor coil near the base. On the XL18i, it's typically at the 6 o'clock position on the coil.
2. **Inspect the sensor harness.** This small two-wire harness runs from the sensor back to the control board. It frequently chafes on the coil frame or gets pinched by the access panel.
3. **Check sensor resistance.** At 77°F: approximately 10,000–12,000 ohms. At 32°F: approximately 32,000–35,000 ohms. Open or shorted = replace.
4. **Secure the replacement sensor firmly** against the coil and cable-tie the harness away from moving parts.

### Flash Code 8 / ComfortLink 191, Reversing Valve Fault

The reversing valve is what makes a heat pump switch between heating and cooling. When it fails to shift, the unit either heats in cooling mode or cools in heating mode, neither of which goes unnoticed for long.

1. **Listen for the shift.** When you switch between modes, you should hear a distinct thump or click from the reversing valve.
2. **Check solenoid voltage.** On a call for cooling (or heating depending on wiring convention), the solenoid coil should have 24VAC.
3. **Test solenoid resistance.** 10–30 ohms = healthy. 0 = shorted, infinite = open coil. Replace solenoid (see Parts table).
4. **If the solenoid is good but the valve won't shift**, the valve is mechanically stuck. This requires a certified technician to replace via brazing.

### Flash Code 9 / ComfortLink 189, Outdoor Fan Motor Fault

1. **Check the run capacitor first.** On most XL18i units, the outdoor fan motor shares a dual capacitor with the compressor. A weak capacitor causes the fan to start slowly or not at all.
2. **Verify the fan blade isn't obstructed.** Check for debris inside the unit.
3. **Check motor winding resistance.** Typical PSC fan motor windings: 2–20 ohms per winding. Open winding = replace motor.
4. **Check supply voltage** to the motor at the control board output terminals.

### Flash Code 10 / ComfortLink 195, Communication Fault

1. **Inspect the ComfortLink II data cable** (typically two wires labeled A and B). Check for breaks, staple damage, or loose connections at both ends.
2. **Power cycle both indoor and outdoor units** by cutting both disconnects/breakers for 60 seconds.
3. **Verify both boards are powered.** A board without 24VAC will not communicate.
4. **Try swapping A and B wires**, polarity sensitivity varies by board revision.

### Flash Code 11 / ComfortLink 186, Compressor Start Failure

1. **Test the dual run capacitor.** Use a capacitor meter, the capacitor must be within 6% of its rated value. Replace if out of tolerance.
2. **Inspect the contactor.** Look for pitted or burned contact points. A pitted contactor doesn't make full electrical contact, starving the compressor of voltage.
3. **Test compressor windings.** Common, Start, and Run terminals should all show low resistance to each other (typically under 10 ohms). Any open reading = failed compressor.
4. **Check supply voltage at compressor terminals.** Should be within 10% of nameplate.

## Parts You May Need

| Part | Use | Link |
|---|---|---|
| Dual Run Capacitor (45+5 µF, 440V) | Fan and compressor start failures | [View on Amazon](https://www.amazon.com/s?k=dual+run+capacitor+45+5+440v&tag=errorcodefixes-20) |
| 2-Pole 30A Contactor | Pitted contacts, code 11 | [View on Amazon](https://www.amazon.com/s?k=2+pole+30+amp+hvac+contactor&tag=errorcodefixes-20) |
| Outdoor Coil / Defrost Sensor | Flash code 4, ComfortLink 182/198 | [View on Amazon](https://www.amazon.com/s?k=trane+xl18i+coil+temperature+sensor&tag=errorcodefixes-20) |
| Reversing Valve Solenoid Coil | Flash code 8, ComfortLink 191 | [View on Amazon](https://www.amazon.com/s?k=reversing+valve+solenoid+coil&tag=errorcodefixes-20) |
| Outdoor Fan Motor (1/4 HP, 208/230V) | Flash code 9, ComfortLink 189 | [View on Amazon](https://www.amazon.com/s?k=condenser+fan+motor+1%2F4+hp+230v&tag=errorcodefixes-20) |
| ComfortLink II Communication Wire | Flash code 10, ComfortLink 195 | [View on Amazon](https://www.amazon.com/s?k=hvac+communication+wire+18+gauge+2+conductor&tag=errorcodefixes-20) |

## When to Call a Pro

**Homeowner-safe repairs:**
- Coil cleaning
- Capacitor replacement
- Contactor replacement
- Coil/defrost sensor replacement
- Reversing valve solenoid coil replacement
- Communication wire inspection and replacement

**Technician required:**
- **Any refrigerant fault that doesn't clear** with coil cleaning and airflow correction. Adding or removing refrigerant requires EPA 608 certification.
- **Reversing valve body replacement.** Brazed copper connections require specialized equipment.
- **Compressor replacement.** On an XL18i from 2012–2018, compare compressor replacement cost against the cost of a new high-efficiency unit. A compressor failure on a unit over 8 years old often makes replacement the better financial decision.
- **ComfortLink II board replacement.** Diagnosing a board versus a wiring issue requires the Trane service tool.

## FAQ

**My Trane XL18i is 9 years old and just threw code 11 (compressor start failure). Should I repair or replace?**
Test the capacitor first, it costs about $25 and resolves the fault 40% of the time on older units. If the capacitor tests good, have a technician confirm compressor failure before making a decision. A compressor replacement on an 8–10 year old unit typically costs $1,500–$2,800 including labor and refrigerant. A new 18 SEER+ heat pump installed runs $4,500–$8,000+. If the rest of the system is in good shape, a compressor replacement can buy 5–8 more years at less than half the cost of replacement.

**Can I read ComfortLink II codes without a compatible thermostat?**
No, the full alphanumeric ComfortLink II codes require a compatible communicating thermostat (XL950, XL850, XL824) or Trane's field diagnostic service tool. Without one, you're limited to the LED flash codes on the outdoor control board.

**My XL18i makes a loud bang when it starts up in heating mode. Is this a fault?**
A mild thump when the unit switches to heating mode is normal, that's the reversing valve shifting. A loud clank or bang at startup, especially followed by a fault code, more likely indicates a liquid-flooded compressor startup, which happens when refrigerant migrates into the compressor during off cycles. If this happens repeatedly, a technician should check refrigerant charge and crankcase heater operation.

**What is the minimum outdoor temperature for XL18i heat pump operation?**
The XL18i is rated for heating operation down to approximately 0°F (ComfortLink code 183 triggers below this threshold). Below 0°F, the unit locks out and backup heat takes over. If you're seeing lockouts at temperatures above 0°F, check the outdoor ambient sensor for accuracy.

**How do I reset a ComfortLink II fault code?**
Most ComfortLink II faults reset automatically once the underlying condition clears. For hard lockouts (multiple repeated faults in a short window), you need to cycle power at the outdoor disconnect for 30–60 seconds. The fault history remains in memory even after a power cycle, it's accessible through the thermostat diagnostics menu.
