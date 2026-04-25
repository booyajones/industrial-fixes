---
title: "Mitsubishi MR-J4 Servo Amplifier Alarm Codes — AL.10, AL.16, AL.30, AL.50 Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2026-04-24T22:10:00Z
modDatetime: 2026-04-24T22:10:00Z
slug: mitsubishi-mr-j4-servo-alarm-codes
featured: false
draft: false
tags:
  - mitsubishi
  - servo
  - industrial
  - alarm-codes
  - cnc
description: "Mitsubishi MR-J4 servo amplifier alarm codes — AL.10 undervoltage, AL.16 encoder error, AL.30 regeneration fault, AL.32 overcurrent, AL.50 overload. Causes, step-by-step fixes, and parts table."
---

## Mitsubishi MR-J4 Servo Amplifier Alarm Codes

The Mitsubishi MELSERVO MR-J4 series is a high-performance servo amplifier used in CNC machine tools (Mazak, DMG Mori, Okuma with Mitsubishi control), industrial robots, semiconductor manufacturing, and general-purpose automation. It replaced the MR-J3 series and is one of the most widely installed servo platforms in Asia-Pacific and North American manufacturing facilities. When the MR-J4 detects a fault, it displays an alarm number on its front-panel 7-segment display and typically halts the driven servo motor axis.

Alarm codes appear as **AL.XX** (decimal) on the display. Some faults can be cleared via the **Alarm reset** input (pin 19 on CN1) or via MR Configurator2 software; others require resolving the root cause before the amplifier will restart.

[Jump to Fix](#step-by-step-fix)

## MR-J4 Alarm Code Quick Reference

| Alarm | Name | Short Description |
|-------|------|-------------------|
| AL.10 | Undervoltage | Main circuit DC bus fell below minimum — check input power and fuse |
| AL.11 | Encoder communication error 1 | Encoder cable disconnected or broken |
| AL.12 | Memory error 1 | EEPROM internal error — amplifier replacement likely required |
| AL.13 | Clock error | Internal oscillator fault — amplifier replacement |
| AL.16 | Encoder communication error 2 | Noisy encoder cable or damaged encoder on motor |
| AL.1E | Encoder communication error 3 | Serial encoder data CRC fault — check cable shielding |
| AL.20 | Encoder normal communication error 1 | Encoder communication lost after startup |
| AL.24 | Main circuit error | DC bus fault, output transistor overvoltage |
| AL.25 | Absolute position lost | Multi-turn absolute encoder lost home position — re-homing required |
| AL.30 | Regeneration error | Regenerative transistor overheated or shorted; regenerative resistor open/shorted |
| AL.31 | Overspeed | Motor exceeded Pr.PB26 overspeed alarm level |
| AL.32 | Overcurrent | Output current exceeded instantaneous peak — short circuit, IGBT failure |
| AL.33 | Overvoltage | DC bus exceeded maximum — excessive regeneration, no regen resistor |
| AL.35 | Command frequency error | Command pulse input frequency exceeded maximum |
| AL.37 | Parameter error | Parameter set out of valid range |
| AL.45 | Main circuit device overheat | IGBT or IPM module overtemperature |
| AL.46 | Servo motor overheat | Motor thermistor detected overtemperature (TH signal) |
| AL.47 | Cooling fan fault | Internal cooling fan failed or speed too low |
| AL.50 | Overload 1 | Sustained overload — motor or amplifier exceeded thermal rating |
| AL.51 | Overload 2 | Instantaneous overload — brief current spike exceeded rating |
| AL.52 | Excessive position error | Actual vs. commanded position difference exceeded droop pulse limit |
| AL.8A | Battery warning | Absolute encoder backup battery below 3.2 V |
| AL.9F | Overload warning | Approaching AL.50 threshold — reduce load or check mechanism |

## Common Causes

- **Encoder cable damage (AL.11, AL.16, AL.1E)** — The most frequent cause of MR-J4 alarms in production environments. Flex-track encoder cables develop internal fractures after repeated bending. Contamination (coolant, oil mist) on the connector pins at the motor end corrodes the signal contacts. The MR-J4 uses a high-speed serial encoder protocol (Mitsubishi SSCNET or local serial); even brief data corruption causes an immediate alarm.
- **Regeneration circuit overload (AL.30, AL.33)** — Vertical axes, high-inertia loads, or servo axes with frequent rapid reversals produce regenerative energy (the motor acts as a generator during deceleration). Without a properly sized external regenerative resistor, this energy charges the DC bus above the safe level or causes the regenerative transistor to overheat.
- **Overload (AL.50, AL.51)** — The motor or amplifier is running beyond its rated torque for too long. Mechanical binding (worn bearings, way lube loss, tight gibs), incorrect tuning (excessive gain causes oscillation and current draw), or an undersized motor/amplifier for the actual load.
- **Undervoltage (AL.10)** — Power supply voltage is too low, a fuse has blown inside the amplifier, or the main circuit contactor is not closing properly. Also triggered by momentary power dips during heavy machine tool cycle starts.
- **Absolute position lost (AL.25)** — The multi-turn encoder in the servo motor lost its reference data, usually because the backup battery was not replaced before it died. The machine's coordinate system must be re-established using the machine tool's home position procedure.

## Step-by-Step Fix {#step-by-step-fix}

1. **Note the alarm number and review history.** Power off and back on; the MR-J4 display will show the current active alarm. Use **MR Configurator2** (free from Mitsubishi) connected via USB to view the **Alarm history** screen — this shows the last 16 alarms with occurrence count and amplifier output current at the moment of trip.

2. **For AL.11 / AL.16 / AL.1E — inspect the encoder cable.** This is the most common fault class on MR-J4. Remove the encoder cable connector at the motor (typically a 10- or 20-pin circular or rectangular connector). Inspect pins for coolant contamination, corrosion, or bent contacts. Straighten or clean with electronics contact cleaner. Check the cable along its entire path — look for kinks, pinch points, or missing conduit in flex-track sections. Perform continuity tests on each wire. **Replace any encoder cable showing intermittent opens, resistance over 1 Ω per conductor, or physical damage.**

3. **For AL.10 — check main circuit power and fuse.** Measure input voltage at L1/L2/L3 (three-phase) or L1/L2 (single-phase) terminals while the machine is cycling. Voltage should be within ±10% of rated. If voltage is correct, the internal main circuit fuse inside the MR-J4 may have blown — this requires opening the amplifier (de-energize first, wait 10 minutes for capacitor discharge) to test with a multimeter.

4. **For AL.30 / AL.33 — check the regenerative resistor.** Disconnect and measure the external regenerative resistor (connected to P+, C terminals or D, P terminals depending on amplifier size). The resistance should match the rated value (typically 10–100 Ω depending on amplifier size). An open resistor = excessive voltage on the DC bus → AL.33. A shorted resistor = regenerative transistor stress → AL.30. Replace if out of spec. Also verify the resistor wiring is connected correctly.

5. **For AL.50 / AL.51 — reduce mechanical load and check tuning.** 
   - Manually rotate the motor shaft by hand with the amplifier disabled — excessive drag indicates a mechanical problem (seized bearing, way lube starvation, interference).
   - In MR Configurator2, open the **Graphing** function and capture motor current during the failing cycle. Compare against the motor's rated current. 
   - If current is continuously near 100%, the motor is undersized for the load. If current oscillates wildly, the servo loop gains (Pr.PB06, Pr.PB08) may be too high.

6. **For AL.25 — replace the battery and re-home the machine.**
   - The MR-J4 uses a 3.6 V lithium battery (ER6V or equivalent) mounted externally on the amplifier or inside the motor connector hood.
   - Replace the battery **with the amplifier powered on** to preserve absolute position data if the battery is merely low (AL.8A warning). If already showing AL.25, position data is lost — proceed with the machine's home position return (ZRN cycle) procedure after battery replacement.

7. **For AL.45 / AL.47 — check cooling.**
   - The MR-J4 internal cooling fan runs continuously when powered. Listen for the fan; a seized or slow fan causes heat buildup. Replace if faulty.
   - Ensure 40 mm minimum clearance above and below the amplifier for airflow. In multi-axis cabinets, verify the forced ventilation fan is working.
   - In dusty environments, clean the heatsink fins with compressed air every 3–6 months.

8. **For AL.52 — check servo tuning and mechanical compliance.** Excessive position error means the motor could not follow the commanded position. This may be caused by:
   - Servo loop gains too low (motor cannot accelerate fast enough)
   - Mechanical slip between motor shaft and load (loose coupling, stripped keyway)
   - Droop pulse limit (Pr.PA10) set too low for the application speed/acceleration

## Parts Often Needed {#parts-often-needed}

| Part | Description | Typical Cost | Where to Buy |
|------|-------------|--------------|--------------|
| MR-J4 encoder cable (Mitsubishi standard) | Flex or standard duty, various lengths | $60–$220 | [Amazon](https://www.amazon.com/s?k=Mitsubishi+MR-J4+encoder+cable+servo&tag=errorcodefixes-20) \| Mitsubishi distributor |
| External regenerative resistor MR-RB series | Match to amplifier capacity (MR-RB032, MR-RB14, etc.) | $120–$500 | [Amazon](https://www.amazon.com/s?k=Mitsubishi+MR-RB+regenerative+resistor&tag=errorcodefixes-20) \| Mitsubishi distributor |
| ER6V 3.6V lithium battery (absolute encoder) | Standard backup battery for MR-J4 absolute encoder | $15–$35 | [Amazon](https://www.amazon.com/s?k=ER6V+3.6V+lithium+battery+servo+encoder&tag=errorcodefixes-20) |
| MR-J4 replacement amplifier (capacity-specific) | 100W, 200W, 400W, 750W, 1kW, 2kW, 3.5kW, 5kW, 7kW, 11kW, 15kW | $1,200–$5,500 | Mitsubishi Electric FA \| Authorized distributor |
| MR Configurator2 USB cable (MR-J3USBCBL3M) | Required for parameter backup and live diagnostics | $40–$80 | [Amazon](https://www.amazon.com/s?k=Mitsubishi+MR-J3USBCBL+servo+USB+cable&tag=errorcodefixes-20) |

## When to Call a Professional

AL.12 (memory error), AL.13 (clock error), and AL.32 (overcurrent/IGBT failure) with a verified-clean motor and cable indicate an internal amplifier fault. The MR-J4 contains capacitors that hold dangerous DC bus voltage (300–750 VDC) for several minutes after power removal; internal service should only be performed by qualified personnel. Mitsubishi Electric FA has a factory service center (Nagoya, Japan and regional hubs) that can repair or exchange MR-J4 amplifiers if parts are unavailable new.

For machine tools where the MR-J4 is the axis servo in a Mazak, DMG Mori, or Mitsubishi M800 CNC system, always back up all CNC parameters and servo parameters before replacing an amplifier — parameter restoration from backup takes minutes; re-commissioning from scratch can take days.

> **Pro tip:** MR-J4 alarms AL.30 and AL.33 are often confused. AL.30 means the regenerative transistor or resistor circuitry failed electrically (a hardware fault). AL.33 means the DC bus actually overvoltaged — which can happen if no regen resistor is installed and the load is decelerating rapidly. Check parameter **Pr.PA02** (regeneration option) — if set to 0 (no option), the amplifier relies on its tiny built-in regenerative resistor only. For any significant dynamic braking application, an external MR-RB series resistor must be installed and Pr.PA02 set accordingly.

## See Also

- [Yaskawa Sigma-7 SGD7S Servo Drive Alarm Codes](/posts/yaskawa-sigma7-sgd7s-alarm-codes/)
- [Mitsubishi FR-A800 VFD Fault E7](/posts/mitsubishi-fr-a800-fault-e7/)
- [Mitsubishi FR-D700 Fault Codes](/posts/mitsubishi-fr-d700-fault-codes/)
- [Fanuc Servo Alarm 400 — Servo Not Ready](/posts/fanuc-alarm-400/)
- [Servo Motor Fault Codes Guide](/posts/servo-motor-fault-codes/)

## Related Articles

- [Mitsubishi City Multi P8 / E6 Error Codes — Causes & Fix](/posts/mitsubishi-city-multi-error-codes/)
- [Mitsubishi PEX City Multi Error Codes (Indoor Unit): Complete Guide](/posts/mitsubishi-city-multi-pex-error/)
- [Mitsubishi CNC Alarm 500 — Causes & Fix](/posts/mitsubishi-cnc-alarm-500/)
- [Mitsubishi CNC Alarm Y96 — Causes & Fix](/posts/mitsubishi-cnc-alarm-y96/)
- [Mitsubishi E1 Error Code — Indoor/Outdoor Communication Fault Fix](/posts/mitsubishi-e1-error-code/)
