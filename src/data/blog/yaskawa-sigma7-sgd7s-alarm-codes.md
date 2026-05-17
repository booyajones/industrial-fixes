---
title: "Yaskawa Sigma-7 SGD7S Servo Drive Alarm Codes — Diagnosis & Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2026-04-24T22:00:00Z
modDatetime: 2026-04-24T22:00:00Z
slug: yaskawa-sigma7-sgd7s-alarm-codes
featured: false
draft: false
tags:
  - yaskawa
  - servo
  - industrial
  - alarm-codes
  - cnc
description: "Yaskawa Sigma-7 SGD7S servo drive alarm codes explained — AL.10 overcurrent, AL.16 encoder error, AL.20 regenerative overload, AL.30 regen circuit, and more. Step-by-step fixes and parts table."
---

## Yaskawa Sigma-7 (SGD7S) Servo Drive Alarm Codes

The Yaskawa Sigma-7 (model series SGD7S, SGD7W) is a high-performance AC servo amplifier used in CNC machine tools, industrial robots, semiconductor equipment, packaging machinery, and precision automation. When the amplifier detects a fault condition, it displays a two-character alarm code (e.g., **AL.10**, **AL.16**) on the front panel LED and halts the servo axis. Understanding what each code means is critical — replacing the servo amplifier unnecessarily costs $1,500–$8,000+, while most alarm conditions are caused by external wiring faults, encoder cable issues, or parameter misconfiguration.

[Jump to Fix](#step-by-step-fix)

## Sigma-7 Alarm Code Quick Reference

| Alarm | Name | Most Likely Cause |
|-------|------|-------------------|
| AL.10 | Overcurrent | Output short circuit, IGBT failure, motor winding fault |
| AL.13 | Overvoltage (main circuit) | Regenerative overload, incorrect regen resistor, braking transistor failure |
| AL.14 | DC bus undervoltage | Input power loss, low supply voltage, fuse blown |
| AL.16 | Encoder error (SEN signal) | Broken encoder cable, damaged connector, shielding failure |
| AL.17 | Encoder failure (internal) | Bad encoder on motor — motor replacement required |
| AL.20 | Regenerative overload | Regen resistor value too high, excessive braking duty cycle |
| AL.24 | Heatsink overtemperature | Blocked airflow, high ambient temperature, cooling fan failure |
| AL.30 | Regenerative circuit error | Shorted regenerative resistor, regenerative transistor failure |
| AL.32 | Main circuit error (IGBT) | Internal IGBT failure — amplifier replacement typically required |
| AL.37 | Parameter storage device error | EEPROM failure in amplifier |
| AL.40 | Maximum speed exceeded | Motor exceeded programmed max speed, parameter Pn385 |
| AL.41 | Encoder data error | Faulty encoder communication (multi-turn data corruption) |
| AL.51 | Overtravel detected | Hardware OT limit switch activated, parameter Pn504 setting |
| AL.74 | Drive inhibit active | /S-ON signal not active, safety relay open, STO triggered |
| AL.8A | Battery warning (absolute encoder) | Encoder backup battery below 3.1 V |
| AL.92 | Regenerative overload warning | Approaching regen overload threshold — precursor to AL.20 |

## Common Causes

- **Encoder cable damage** — AL.16 and AL.41 are almost always caused by a damaged or improperly shielded encoder cable. Flex track applications (where the cable bends repeatedly) are especially prone to internal wire fractures that cause intermittent encoder signal errors.
- **Regenerative circuit issues** — AL.13 and AL.20 occur when the servo system cannot dissipate braking energy fast enough. High-inertia loads (flywheels, large tooling), vertical axes, or frequent high-speed reversals require a correctly sized external regenerative resistor.
- **Motor winding or cable fault** — AL.10 (overcurrent) is triggered by a short circuit at the servo amplifier output. The fault can be in the motor winding, the U/V/W motor cable, or inside the amplifier itself.
- **Inadequate cooling** — The SGD7S requires free airflow over its heatsink. AL.24 (heatsink overtemp) is common when multiple amplifiers are mounted in a tight cabinet without forced ventilation, or when cabinet filters become clogged.
- **Low supply voltage** — AL.14 occurs if the main circuit DC bus drops below the minimum threshold. Check the input L1/L2/L3 voltage and the DC bus fuse inside the amplifier.
- **Safety / inhibit signals** — AL.74 is not a hardware fault; it means the amplifier is waiting for a servo-on (/S-ON) signal or the hardware enable input is open. Check the machine's safety relay chain and SERVOPACK I/O connector.

## Step-by-Step Fix {#step-by-step-fix}

1. **Read the alarm code from the front panel.** The SGD7S displays the alarm as **A.LXX** where XX is the hex fault number. Power cycling clears the alarm display, but the alarm history is stored — navigate to **Fn000** (alarm history) in the parameter panel to view the last 10 alarms with timestamps.

2. **Check the encoder cable first (AL.16 / AL.41).** Disconnect the encoder cable at both the motor and amplifier ends. Inspect the connector pins for bent contacts, contamination, or corrosion. With a multimeter, perform a continuity check on every wire in the encoder cable (typically 10–15 conductors). Flex the cable along its run while measuring — intermittent opens indicate internal fractures. Replace the cable if any conductor fails continuity or shows resistance above 1 Ω.

3. **Verify main circuit power (AL.14).** Measure the incoming supply voltage at the amplifier L1/L2/L3 terminals under load. For a 200V-class amplifier, input should be 170–253 VAC; for a 400V-class, 340–528 VAC. Also check the DC bus fuse inside the amplifier — it is a large fast-blow fuse on the internal power board.

4. **Test the motor and output cable for shorts (AL.10).** Disconnect the motor cable at the amplifier U/V/W terminals. Use a 500V megohm tester:
   - Each phase (U, V, W) to ground: should read >100 MΩ on a healthy motor
   - Phase to phase (U-V, V-W, W-U): should read >1 MΩ
   
   Also measure winding resistance with a precision ohmmeter — all three phase-to-phase readings should be equal within ±5%. A failed winding will show very low resistance or near-zero (shorted turns).

5. **Check the regenerative resistor and circuit (AL.13 / AL.20 / AL.30).** Measure the resistance of the external regenerative resistor — compare to the rated value on the resistor label or in parameter **Pn600/Pn604** settings. A shorted resistor reads near 0 Ω; an open resistor reads infinite. Ensure the resistor wiring is connected to the B1/B2 (or B2/B3) terminals correctly. Verify the duty cycle of the braking application does not exceed the resistor's continuous power rating.

6. **Inspect amplifier cooling (AL.24).** Ensure at least 30 mm of clearance above and below the SGD7S heatsink. Check the internal cooling fan (audible when amplifier is powered). In multi-axis cabinets, add a forced-air cooling fan blowing over the heatsink row. In dusty environments, clean the heatsink fins with compressed air every 3–6 months.

7. **Verify enable and safety signals (AL.74).** In Yaskawa SigmaWin+ software (or via the operator panel), monitor the I/O status to confirm:
   - /S-ON (servo on): active (low) when machine ready
   - /HW-BB (hardware base block): not active
   - /FSTP (forced stop): not active
   - STO (safe torque off) inputs: both +24V present
   
   If using a safety relay module, verify it has closed its output contacts. AL.74 with all signals correct indicates a wiring error in the I/O connector (CN1).

8. **Use SigmaWin+ for data capture.** If the alarm is intermittent, connect a PC running Yaskawa's free **SigmaWin+** software to the USB port on the SGD7S front panel. Use the trace function to capture speed, current, and encoder signals at the moment of trip. This data is invaluable for distinguishing a load/mechanical fault from an electrical fault in the amplifier.

## Parts Often Needed {#parts-often-needed}

| Part | Description | Typical Cost | Where to Buy |
|------|-------------|--------------|--------------|
| Encoder cable (Yaskawa Sigma-7 compatible) | Shielded, flex-rated, 20-pin MDR to 9-pin sub-D | $80–$250 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-sigma7-sgd7s-alarm-codes&k=Yaskawa+Sigma-7+encoder+cable+replacement&tag=errorcodefixes-20) \| Yaskawa distributor |
| External regenerative resistor (JUSP-RA series) | Match to amplifier model and capacity | $120–$400 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-sigma7-sgd7s-alarm-codes&k=Yaskawa+Sigma+regenerative+resistor+JUSP&tag=errorcodefixes-20) \| Yaskawa distributor |
| Absolute encoder battery (3.6V lithium) | Backup power for multi-turn absolute encoder | $15–$30 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-sigma7-sgd7s-alarm-codes&k=Yaskawa+Sigma+encoder+battery+3.6V&tag=errorcodefixes-20) |
| SGD7S replacement amplifier (various capacities) | 100W to 15kW models available | $1,500–$6,000 | Yaskawa America \| Authorized distributor |
| Din-rail power supply 24VDC (for I/O logic) | Ensures stable enable signal voltage | $40–$90 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-sigma7-sgd7s-alarm-codes&k=24VDC+DIN+rail+power+supply+industrial&tag=errorcodefixes-20) |

## When to Call a Professional

If AL.10 (overcurrent) or AL.32 (IGBT failure) persists after confirming the motor and cable are fault-free, the fault is internal to the amplifier — power stage replacement is required. Yaskawa SGD7S amplifiers contain high-voltage DC bus capacitors that remain charged after power-off; do not open the amplifier unless you are a qualified technician with appropriate PPE and discharge procedures. For machine tool applications where the servo axis is part of an integrated CNC system (Fanuc, Mitsubishi, Mazak, Okuma), Yaskawa recommends their authorized service engineers for parameter backup and restoration.

> **Pro tip:** Before any Sigma-7 service work, always back up the amplifier parameters using **SigmaWin+** (File → Parameter → Save to File). If the amplifier is replaced, you can restore parameters directly — this saves 1–2 hours of re-commissioning time and avoids the risk of manual parameter entry errors on the 300+ parameter set.

## See Also

- [Yaskawa VFD Fault OC — Overcurrent Diagnosis](/posts/yaskawa-vfd-fault-oc-overcurrent/)
- [Yaskawa GA700 Fault UV1](/posts/yaskawa-ga700-fault-uv1/)
- [Mitsubishi MR-J4 Servo Amplifier Alarm Codes](/posts/mitsubishi-mr-j4-servo-alarm-codes/)
- [Fanuc Servo Alarm 400 — Servo Axis Not Ready](/posts/fanuc-alarm-400/)
- [Servo Motor Fault Codes Guide](/posts/servo-motor-fault-codes/)

## Related Articles

- [Yaskawa A1000 OC Fault — Overcurrent](/posts/yaskawa-a1000-fault-oc/)
- [Yaskawa A1000 Fault UV1, DC Bus Undervoltage Causes & Fix](/posts/yaskawa-a1000-fault-uv1/)
- [Yaskawa A1000 Fault Code OC — Overcurrent Diagnosis & Fix](/posts/yaskawa-a1000-oc-fault-code/)
- [Yaskawa GA700 OC Fault — Overcurrent Fix](/posts/yaskawa-ga700-fault-oc/)
- [Yaskawa GA700 Fault UV1 — Main Circuit Undervoltage Causes & Fix](/posts/yaskawa-ga700-fault-uv1/)
