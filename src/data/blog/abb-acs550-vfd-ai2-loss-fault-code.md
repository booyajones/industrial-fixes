---
title: "ABB ACS550 VFD AI2 LOSS - Causes & Fix"
description: "AI2 LOSS means the drive lost the analog input 2 signal. Check wiring connections at the AI2 terminal block first."
pubDatetime: 2026-07-19T07:29:13Z
modDatetime: 2026-07-19T07:29:13Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - abb
money_part: "Shielded analog signal cable"
most_likely_cause: "loose or broken wiring at the AI2 terminal"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Inspect the AI2 terminal block for loose, corroded, or broken wire connections and reseat all terminals"
  - "Check the drive parameter settings for AI2 signal type and range to confirm they match your input device"
  - "Measure the input signal voltage or current at the AI2 terminals with a multimeter to verify the source device is working"
no_buy_pct: "65%"
---

## ABB ACS550 VFD AI2 LOSS — What It Means

The AI2 LOSS fault on an ABB ACS550 variable frequency drive indicates that the drive has detected a loss of signal or an out-of-range condition on analog input 2 (AI2). Analog inputs are used to provide reference signals for speed, torque, or process control from external devices such as potentiometers, pressure transducers, or process controllers. When the drive cannot read a valid signal within the expected range, it triggers this fault to prevent incorrect operation.

The fault typically occurs when the wiring to AI2 is open, shorted, or loose, or when the input signal falls outside the configured range. The drive's parameter settings define what signal type and range AI2 expects, so a mismatch between the actual input device and the programmed parameters can also cause this fault. Review your drive manual for the specific AI2 parameter group to verify signal type, scaling, and fault threshold settings for your model.

## Before You Replace Anything

Technicians sometimes replace the entire control board when the real issue is a damaged signal wire or incorrect parameter setting. Always verify wiring continuity and check parameter configuration before ordering a new board.

[Jump to Fix](#fix)

## Common Causes

- **Loose or broken wiring (~40%)** The wire connecting the analog input device to the AI2 terminal is loose, corroded, or broken, interrupting the signal path.
- **Failed input device (~25%)** The potentiometer, transducer, or controller sending the signal to AI2 has failed or lost power.
- **Incorrect parameter configuration (~20%)** The AI2 parameters are set for a different signal type or range than what the connected device provides, causing the drive to reject the signal as out of range.
- **Shielded cable fault (~10%)** The shielded cable carrying the analog signal has damage or poor grounding, allowing electrical noise to corrupt the signal below the fault threshold.
- **Control board analog input circuit failure (~5%)** The analog input circuitry on the drive control board has failed and cannot read the AI2 signal correctly.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is there voltage or current present at the AI2 terminals when measured with a multimeter?</summary>
<div class="dtree-body"><strong>Yes:</strong> The input device is likely working. Check the drive parameters to confirm AI2 is configured for the correct signal type and range, then verify cable shielding and grounding.<br><strong>No:</strong> The input device may have failed or lost power, or the wiring is open. Trace the cable back to the source and check for breaks or loose connections at both ends.</div>
</details>

<details class="dtree"><summary>Does the fault clear when you disconnect the AI2 input wires and jumper a known good test signal to the terminals?</summary>
<div class="dtree-body"><strong>Yes:</strong> The drive AI2 circuit is working. The problem is in the external wiring or the input device itself. Replace or repair the cable and check the input device.<br><strong>No:</strong> The drive analog input circuit may be damaged, or the parameters are still incorrect. Verify all AI2 settings match your test signal, and if correct, the control board may need service.</div>
</details>

<details class="dtree"><summary>Has the AI2 input been used previously without this fault, or is this a new installation?</summary>
<div class="dtree-body"><strong>Yes:</strong> Something has changed in the wiring or the input device. Inspect for physical damage, corrosion, or a device that has drifted out of calibration.<br><strong>No:</strong> This is likely a configuration issue. Review the drive manual for AI2 setup and confirm every parameter matches the specifications of your analog input device.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive** and lock out the disconnect switch following your facility lockout-tagout procedure.
2. **Remove the front cover** of the ACS550 to access the control terminal block where AI2 is connected.
3. **Inspect the AI2 terminals** (consult your wiring diagram for the exact terminal numbers) for loose wires, corrosion, or signs of arcing and tighten or clean as needed.
4. **Use a multimeter** to measure the signal at the AI2 input with power restored to the input device but the drive still off. Verify the voltage or current matches the expected range for your device (commonly 0-10 V or 4-20 mA).
5. **Check the drive parameters** for AI2 configuration. Navigate the keypad menu to the analog input group and confirm signal type, minimum and maximum scaling, and any fault threshold settings match your input device specifications.
6. **Test with a known good signal source** if available. Disconnect the field wiring and connect a calibrated signal generator or potentiometer to AI2, then power the drive and check if the fault clears.
7. **Replace damaged wiring or shielding** if continuity tests reveal an open or intermittent connection, or if the cable jacket is cut or the shield is broken. Use shielded twisted-pair cable and ground the shield at one end only per the drive manual.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Shielded analog signal cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs550-vfd-ai2-loss-fault-code&k=Shielded+analog+signal+cable&tag=errorcodefixes-20) \| Use cable rated for industrial analog signals, typically 18 or 20 AWG shielded twisted pair for long runs |
| Replacement analog input device (potentiometer, transducer, or controller) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs550-vfd-ai2-loss-fault-code&k=Replacement+analog+input+device+%28potentiometer%2C+transducer%2C+or+controller%29&tag=errorcodefixes-20) \| Match the signal type and range to the existing device and verify compatibility with the drive parameters |

## When to Call a Pro

Call a qualified industrial electrician or automation technician if you are not trained to work on variable frequency drives or if your facility requires certified personnel for electrical troubleshooting. A professional should handle the repair if the wiring is inside conduit or cable trays that require pulling new cable, if the fault persists after checking all external wiring and parameters, or if you suspect the control board analog input circuit is damaged and needs board-level repair or replacement. Professionals have the calibrated test equipment and software tools to verify drive parameters and diagnose internal faults accurately.

**Rough cost:** A pro service call runs about $150-400.

## See Also

- [ABB ACS580 VFD E0020 Fault Code - Causes & Fix](/posts/abb-acs580-vfd-e0020-fault-code/)
- [ABB VFD Fault 5010 — Causes & Fix](/posts/abb-vfd-fault-5010/)
- [ABB ACS580 VFD E0034 Fault - Causes & Fix](/posts/abb-acs580-vfd-e0034-fault-code/)
- [ABB ACS580 VFD E0030 Fault - Causes & Fix](/posts/abb-acs580-vfd-e0030-fault-code/)
