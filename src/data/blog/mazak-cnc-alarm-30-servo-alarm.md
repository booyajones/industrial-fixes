---
title: "Mazak CNC Alarm 30 — Servo Alarm Fix"
author: "Dana Kowalski"
pubDatetime: 2024-03-15T08:00:00Z
modDatetime: 2024-03-15T08:00:00Z
slug: mazak-cnc-alarm-30-servo-alarm
featured: false
draft: false
tags:
  - cnc
  - mazak
  - servo
  - alarm
description: "Mazak CNC alarm 30 means a servo amplifier fault on Quick Turn, Variaxis, and Integrex series machines — here's how to diagnose and fix it."
---

## Error Code: Mazak CNC Alarm 30

**What it means:** Alarm 30 on Mazak CNC machines (Quick Turn lathes, Variaxis and Integrex machining centers, and other MAZATROL-controlled platforms) indicates a servo amplifier fault. The CNC's servo control system detected an abnormal condition in one of the machine's servo axis amplifiers — the drive that converts the control board's position commands into motor current. The machine halts all motion and cannot be restarted until the fault is cleared.

Alarm 30 is a category alarm that can originate from any servo axis (X, Y, Z, B, C, or turret). The specific axis and sub-code must be read from the alarm detail screen on the MAZATROL display to know which amplifier is involved.

## Common Causes

- **Servo amplifier internal fault** — The amplifier's drive circuit, IGBT module, or internal fault detection has tripped. The amplifier's own LED display (visible inside the cabinet) will show a specific fault code that narrows the diagnosis.
- **Encoder feedback fault** — The encoder mounted on the servo motor has lost signal, is outputting incorrect data, or has a cable connection problem. The amplifier detects the discrepancy between commanded position and encoder feedback and faults.
- **Servo motor overtemperature** — The motor's built-in thermal switch (PTC) has opened due to overloading, a blocked cooling fan, or contamination on the motor windings. Alarm 30 may clear after the motor cools.
- **Servo motor winding fault** — A shorted or open motor winding causes the amplifier to detect current imbalance and trip.
- **Power supply voltage anomaly** — Low or unstable DC bus voltage from the servo power supply (PSM — Power Supply Module in Fanuc-based Mazak systems) causes the amplifier to fault.
- **Damaged or contaminated servo drive cable** — The cable harness between the amplifier and servo motor (both power and encoder cables) can be damaged by coolant, chips, or mechanical abrasion.

## Step-by-Step Fix {#step-by-step-fix}

1. **Read the alarm detail screen on the MAZATROL.** On MAZATROL T-plus and Matrix systems, press the ALARM button (or navigate to Alarm → Servo Alarm). The detail screen shows the axis name (X, Z, C, etc.) and an amplifier sub-code. Write this down — it's the key to diagnosis.

2. **Open the electrical cabinet and read the amplifier's front panel display.** Mazak machines equipped with Fanuc servo amplifiers (SVU, SVPM, or Alpha-series SVMs) have an LED or 7-segment display on the amplifier face showing a numeric fault code. Common Fanuc amplifier codes include: 1 (current abnormal), 4 (overvoltage), 8 (motor overheat), 9 (overcurrent). Mazak-branded Mitsubishi amplifiers display similar codes on their front panel.

3. **Check all electrical connections at the amplifier.** With machine power off and capacitors discharged (wait 5 minutes after power off), inspect the servo motor power cable connector (the multi-pin circular connector at the amplifier's CN1 or CX axis port). Check for: pulled-back pins, corrosion, coolant ingress into the connector housing, or damaged cable insulation near the connector.

4. **Check the encoder cable separately.** The encoder cable (typically smaller diameter, often with a separate cable clamp) runs from the motor's encoder connector to the amplifier's encoder input (CN2 or CZ). Inspect for the same defects as the power cable. Encoder cable failures are a very common cause of Alarm 30 on machines that are several years old.

5. **Attempt to clear the alarm and observe amplifier behavior.** With all connections verified, restore power. Press RESET on the MAZATROL. If the alarm immediately recurs without any machine motion, the fault is in the amplifier's internal hardware or the power supply. If it clears temporarily but returns after a specific axis movement, the encoder or motor is likely the culprit.

6. **Swap the suspect amplifier with a spare or known-good axis amplifier (if identical).** On machines with multiple identical amplifier units (common on multi-axis machining centers where X, Y, and Z use the same amplifier model), swapping the suspect amplifier to a different axis and observing whether the fault follows the amplifier or stays on the original axis is the fastest diagnostic method. Fault follows the amplifier = bad amplifier. Fault stays on original axis = motor, encoder, or wiring problem.

7. **Test servo motor insulation and winding balance.** Disconnect the motor power cable at the amplifier. Megger each motor power lead to the motor frame (500V). Minimum 1 MΩ. Measure resistance phase-to-phase at the motor cable end — values should be equal within 5%.

8. **Contact Mazak service or a Fanuc-certified repair center for amplifier replacement.** IGBT module replacement in a Fanuc servo amplifier is a component-level repair requiring specialized equipment. Most shops either replace the whole amplifier unit or send it to an authorized repair center for board-level service.

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Part Number | Typical Cost | Where to Buy |
|------|------------|-------------|-------------|
| Fanuc Servo Amplifier (Alpha-series) | A06B-6140-H006 (axis-specific) | $1,500–$4,000 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mazak-cnc-alarm-30-servo-alarm&k=A06B-6140-H006+%28axis-specific%29+Fanuc+Servo+Amplifier+%28Alpha-series%29&tag=errorcodefixes-20) \| Fanuc America / repair centers |
| Servo Motor Encoder Cable | A66L-0001-0284 (size-specific) | $80–$250 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mazak-cnc-alarm-30-servo-alarm&k=A66L-0001-0284+%28size-specific%29+Servo+Motor+Encoder+Cable&tag=errorcodefixes-20) \| Fanuc America / Mazak parts |
| Fanuc Servo Motor (if motor failed) | A06B-0205-B100 (model-specific) | $1,200–$3,500 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mazak-cnc-alarm-30-servo-alarm&k=A06B-0205-B100+%28model-specific%29+Fanuc+Servo+Motor+%28if+motor+failed%29&tag=errorcodefixes-20) \| Fanuc America / repair centers |
| Power Supply Module (PSM) | A06B-6150-H030 (size-specific) | $2,000–$5,000 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mazak-cnc-alarm-30-servo-alarm&k=A06B-6150-H030+%28size-specific%29+Power+Supply+Module+%28PSM%29&tag=errorcodefixes-20) \| Fanuc America |
## When to Call a Professional

Mazak CNC servo systems operate at high voltages (200–600VDC bus) and require Fanuc-certified or Mazak-certified service technicians for amplifier replacement and parameter verification. After any amplifier replacement on a Mazak, the servo parameters (gain, velocity loop gains, position loop gains) must be verified against the machine's parameter backup and may require tuning to prevent axis oscillation or following error alarms. Attempting to run a machine after servo amplifier replacement without parameter verification can cause axis runaway. Always keep a current parameter backup on a USB drive stored with the machine.

> **Pro tip:** Mazak Alarm 30 caused by encoder cable failure often appears intermittently at first — the alarm triggers only during rapid traverse moves or when the machine is cold, then disappears after warm-up. The thermal expansion of a damaged cable connector slightly improves continuity as it warms. If your Alarm 30 clears on its own after 20–30 minutes of warm-up, pull and inspect the encoder cable connector for the affected axis immediately — you're a few weeks from a hard failure that stops the machine mid-cut.

## Related Articles

- [CNC Alarm Reset Guide: How to Clear Alarms Safely](/posts/cnc-alarm-reset-guide/)
- [CNC Machine Error Codes: Complete Troubleshooting Guide](/posts/cnc-error-codes-guide/)
- [Doosan CNC Alarm Codes Guide — Fanuc / Fanuc i Series Controls](/posts/doosan-cnc-fault-codes/)
- [Fanuc 0i-MD Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-0i-md-alarm-codes/)
- [Fanuc 30i/31i/32i Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-30i-alarm-codes/)

## See Also

- [Mazak Integrex Error Codes Guide — Common Mazatrol and Servo Faults](/posts/mazak-integrex-error-codes/)
- [Mazak Matrix/Matrix 2 Fault Code Guide — Complete Reference](/posts/mazak-matrix-fault-codes/)
- [Mazak Alarm 218 — Spindle Motor Overheat Fix](/posts/mazak-alarm-218/)
- [Mazak CNC Alarm 200 Parameter Fault — Causes & Fix](/posts/mazak-cnc-alarm-200-parameter/)
