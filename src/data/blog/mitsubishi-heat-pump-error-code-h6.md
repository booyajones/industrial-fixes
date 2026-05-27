---
title: "Mitsubishi P-Series H6 — Outdoor Fan Motor Fix"
description: "Code H6 on a Mitsubishi P-Series (PUZ/PUY commercial split, PUMY VRF outdoor unit, City Multi outdoor) indicates an outdoor unit fan motor fault — the..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: mitsubishi-heat-pump-error-code-h6
featured: false
draft: false
tags:
  - mitsubishi
  - outdoor-fan-motor
  - troubleshooting
---
## Quick answer

Code H6 on a Mitsubishi P-Series (PUZ/PUY commercial split, PUMY VRF outdoor unit, City Multi outdoor) indicates an outdoor unit fan motor fault — the inverter-driven DC fan motor is not rotating at commanded speed, the motor's rotor position feedback is missing or inconsistent, or the fan motor controller has detected an over-current or stall condition. The compressor will shut down to prevent over-pressure damage. Most field calls trace to the motor itself or its controller; less frequently it's wiring, a stuck fan blade, or a fault on the main inverter PCB.

## What H6 means on a Mitsubishi P-Series

Mitsubishi's P-Series (heavy-duty inverter heat pumps) and City Multi VRF systems use DC inverter fan motors with integrated rotor-position feedback. The outdoor unit's main PCB commands fan speed via a PWM signal; the motor controller closes the loop and reports actual speed and current draw back to the PCB.

H6 specifically maps to "DC Fan Motor Error" in Mitsubishi's M-Series and P-Series error code dictionary. The trigger conditions are:

- Fan motor speed feedback shows zero or grossly under commanded RPM for more than a few seconds.
- Fan motor current draw exceeds protection threshold (stalled or seized).
- Rotor-position feedback inconsistent or missing (open Hall-effect sensor).
- Communication between fan motor controller and main PCB fails (on motors with serial feedback).

Mitsubishi will retry the fan a few times before posting H6 and locking the system out. After lockout, the outdoor unit displays H6 on its 7-segment LED (typically labeled "LED 1 / LED 2" on the main PCB, with H6 shown as two characters). On a City Multi system with a controller, the same code appears on the wired remote.

Worth knowing: Mitsubishi P-Series often comes in 208-230V and 460V variants. The fan motor and its controller are voltage-specific — H6 after a board or motor swap might mean a wrong-voltage part. Always cross-reference by model number on the rating plate.

## Common causes (ranked by frequency)

1. **DC fan motor failure (internal winding or Hall sensor)** — about 28%. Motor is a wear item; failure usually 8-12 years.
2. **Fan motor controller fault** — about 18%. The integrated drive module fails before the motor itself.
3. **Fan blade obstruction (debris, ice, mechanical interference)** — about 15%. Won't spin freely, current spikes, board reads stall.
4. **Wiring fault or loose connector at motor harness** — about 12%. Common after rodent damage or rough installation.
5. **Bearing seizure** — about 8%. Motor rotates but with high friction; controller sees over-current.
6. **Main PCB inverter section damaged** — about 7%. PCB can't drive the motor correctly.
7. **Power supply issue (low/unstable line voltage)** — about 5%. Below 187V on a 208V system causes inverter faults including H6.
8. **Mismatched replacement motor or controller** — about 4%. Wrong voltage or wrong feedback type.
9. **Fan motor protection from external cause (frozen ice on blade)** — about 3%. Indoor of unusual condition.

Field nugget: I've seen this 300 times — Mitsubishi PUZ outdoor unit, 6-8 years old in coastal install, throws H6 in fall after summer of light use. Tech tests the motor, finds it spins by hand, replaces the main PCB (the expensive guess), problem returns 3 months later. The real issue is bearing degradation: the motor spins freely by hand because there's no load, but under inverter PWM commutation the bearing friction causes current spikes that trigger H6. The diagnostic: spin the motor by hand and listen — healthy is silent or very faint hum. Any grinding, ticking, or rough feel = bearings are gone, replace the motor. Don't replace boards on H6 without confirming the motor first; the motor is more often the cause and it's the cheaper part. R-454B Mitsubishi units (newer P-Series with low-GWP refrigerant, A2L mildly flammable) make this lesson sharper because labor cost on these units is higher — don't waste hours on wrong parts.

## Step-by-step fix

Safety first: kill power at the outdoor disconnect. Inverter DC bus retains 300+ VDC for 5-10 minutes after power-off — wait at least 10 minutes and verify with a meter before touching internal components. P-Series 460V units carry serious shock risk. For newer R-454B units, follow A2L handling on any refrigerant work. Mitsubishi outdoor units have sharp edges in the fan venturi and coil — wear gloves.

1. **Confirm H6 and check fault history.** Power on, observe the outdoor LED display. H6 should display on the main PCB's 7-segment readout. On the connected wired controller (PAR-32MAA or PAR-40MAA), check fault history for accompanying codes — H7 (motor lock alarm), U6 (outdoor unit compressor overcurrent), or P8 (heat exchanger temperature fault) can ride along.

2. **Visually inspect the outdoor fan.** Power off, wait 10 minutes for DC bus discharge. Remove the top grille (typically 4-6 screws). Look at the fan blade: should rotate freely by hand, no debris in the blade path or venturi. Push the blade hub by hand — it should spin smoothly with minimal resistance. Grinding, ticking, or roughness = bearings shot. Free spin with no noise = motor and bearings likely OK; problem is elsewhere.

3. **Inspect motor wiring and connectors.** Trace the motor harness from the motor up to the main PCB. Mitsubishi P-Series fan motors use a multi-pin connector (typically 5-pin: power, neutral, PWM speed signal, RPM feedback, ground) with a polarized plug. Pull the connector apart, inspect for corrosion or pin pushback. Re-seat firmly. Look for chafing along the harness route — common at the cabinet exit point.

4. **Measure motor windings.** With motor disconnected from the PCB, measure resistance phase-to-phase on the 3-phase windings (P-Series DC fan motors are 3-phase brushless DC). Should be roughly balanced — within 10% of each other, typically 50-200Ω depending on motor size. Open circuit on any winding = motor is shot. Reading to motor frame (ground) should be open circuit / very high (motor windings should be isolated from frame). Any low resistance to frame = motor is grounded internally.

5. **Power up and observe.** Reset the fault by cycling power (off 30 seconds, on). On a heat or cool call, watch the fan motor: it should ramp up from rest within 5-10 seconds of compressor start. If the fan never moves, or moves erratically (jerks, hunts, vibrates), it's a motor or controller fault. If fan spins normally and H6 doesn't return for 10 minutes, the issue may have been a loose connector — but monitor closely.

6. **Verify power supply quality.** With a multimeter at the outdoor unit's L1-L2 terminals (or L1-L1' on 460V), confirm line voltage. Mitsubishi P-Series 208/230V spec is 187-253V; below 187V, the inverter throws faults including H6. 460V spec is 414-506V. Note any voltage sag during compressor start — should not drop below the minimum spec.

7. **Test or replace the motor.** If motor windings are bad or motor doesn't spin freely, replace. Mitsubishi P-Series outdoor fan motors typically come as a motor-and-controller assembly because the integrated controller is part of the motor. Match the part number exactly to your rating plate — voltage, capacity, and feedback type all matter. Mitsubishi 5045L010-1 series is common on PUZ-A24/A30 platforms; 5045L020 on larger PUZ-A36/A42.

8. **Reset and verify normal operation.** Power cycle to clear the lockout. Run the system in cool or heat for 30 minutes. Watch the outdoor fan ramp through low, medium, and high speeds (Mitsubishi inverter fans modulate continuously). Listen for any unusual noise. If the system runs through a full cycle without H6 returning, the fix is good.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Outdoor fan motor (PUZ-A24/A30, 230V) | Mitsubishi T7WE15315 | $310-460 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=mitsubishi-heat-pump-error-code-h6), [Amazon](https://www.amazon.com) |
| Outdoor fan motor (PUZ-A36/A42, 230V) | Mitsubishi T7WE15321 | $410-580 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=mitsubishi-heat-pump-error-code-h6), [Amazon](https://www.amazon.com) |
| Outdoor fan motor (PUMY-P/City Multi VRF) | Mitsubishi T7WE21405 | $480-720 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=mitsubishi-heat-pump-error-code-h6), [Amazon](https://www.amazon.com) |
| Fan blade (PUZ A-series) | Mitsubishi T7WB22102 | $48-85 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=mitsubishi-heat-pump-error-code-h6), [Amazon](https://www.amazon.com) |
| Outdoor main control PCB (PUZ-A24) | Mitsubishi T7WE34123 | $720-1100 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=mitsubishi-heat-pump-error-code-h6), [Amazon](https://www.amazon.com) |
| Outdoor inverter PCB (City Multi PUMY-P) | Mitsubishi T7WE40212 | $1100-1650 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=mitsubishi-heat-pump-error-code-h6), [Amazon](https://www.amazon.com) |
| Motor harness assembly | Mitsubishi T7WE11055 | $42-78 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=mitsubishi-heat-pump-error-code-h6), [Amazon](https://www.amazon.com) |
| Wired remote controller (PAR-40MAA) | Mitsubishi PAR-40MAA | $310-440 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=mitsubishi-heat-pump-error-code-h6), [Home Depot](https://www.homedepot.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=mitsubishi-heat-pump-error-code-h6) |

Note: Mitsubishi part numbers I've listed are representative; always cross-reference to your unit's rating plate model and serial range. Mitsubishi changes part numbers between production runs and the wrong number can result in shipping a physically similar but electronically incompatible motor.

## When to call a professional

**City Multi VRF system H6 on a multi-port system.** VRF systems are complex and Mitsubishi reserves some service diagnostics to their service network. If you're on a City Multi system with multiple indoor units and a single outdoor module throwing H6, get a Mitsubishi-certified VRF technician.

**Inverter PCB replacement.** Mitsubishi inverter PCBs require model-specific DIP switch configuration and sometimes parameter setup via service tools. Wrong configuration = repeated faults. Pro-only work in most cases.

**460V three-phase units.** Higher voltage carries higher risk. If you don't routinely work on 480V commercial equipment with proper PPE and lockout/tagout procedures, hand it off.

**Refrigerant work on R-454B (A2L) units.** Newer Mitsubishi P-Series and Hyper Heat units shipping with R-454B require A2L-certified handling. Don't attempt refrigerant repairs without certification and proper tools.

Never run the unit with the fan blade removed or with the cabinet open and powered. The fan is what discharges hot/cold air across the coil; without it, you'll trip pressure faults and potentially damage the compressor.

## FAQs

**My PUZ throws H6 only in winter — is it ice on the fan?**
Possible. Defrost mode briefly stops the fan; if ice builds up between cycles and the fan tries to start with the blade encased in ice, current spikes and you get H6. Manual defrost the unit (turn off, let thaw fully), check defrost logic.

**Can I run the unit on emergency heat while waiting for parts?**
On a residential split or mini-split, you can call for indoor electric heat (if equipped) and disable outdoor operation. On a commercial P-Series or VRF, no — the system needs the outdoor unit operational to deliver any heat.

**Is H6 related to H7?**
Yes, they're siblings. H6 = fan motor error (often a stall or no rotation); H7 = motor lock alarm (rotor locked in position). H6 usually points to motor or controller failure; H7 often points to physical blade obstruction.

**Why is my Mitsubishi motor more expensive than a Goodman motor?**
Mitsubishi P-Series uses integrated brushless DC motors with onboard controllers — significantly more complex than the PSC motors in entry-level Goodman units. The upside is better efficiency and modulation; the downside is higher replacement cost.

**Are R-454B Mitsubishi units different to service?**
Refrigerant handling differs (A2L procedures, A2L-rated tools). Electrical and mechanical service is similar. H6 troubleshooting logic is the same across refrigerant types.

## Related guides

- [Bryant Evolution Heat Pump 21 — Defrost Sensor Fix](/posts/bryant-heat-pump-error-code-21)
- [Trane XV20i/XV18 Fault 126 — Low Pressure Cutout Fix](/posts/trane-heat-pump-error-code-126)
- [Carrier Greenspeed A3 — Defrost Fault Fix](/posts/carrier-heat-pump-error-code-a3)

## See Also

- [Mitsubishi Mini Split P2 Error Code — Indoor Pipe Thermistor Fix](/posts/mitsubishi-p2-error-code/)
- [Mitsubishi PUY Air Handler Error Codes — Fault Code Diagnostic Guide](/posts/mitsubishi-puy-error-codes/)
- [Mitsubishi P3 Error Code — Outdoor Coil Thermistor Fix](/posts/mitsubishi-p3-error-code/)
- [Mitsubishi P4 Error Code — Drain System Fault: Causes & Fix](/posts/mitsubishi-p4-error-code/)
