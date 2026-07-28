---
title: "Siemens Micromaster F0221 - Causes & Fix"
description: "F0221 means PI controller feedback is below the minimum value. Most often caused by incorrect parameter P2268 setting or missing sensor signal."
pubDatetime: 2026-06-22T10:04:44Z
modDatetime: 2026-06-22T10:04:44Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Analog feedback sensor (speed or pressure transducer)"
most_likely_cause: "Incorrect parameter P2268 setting"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Read parameter P2268 and compare it to the minimum expected sensor output voltage during normal operation"
  - "Check that the external feedback sensor has power at its supply terminals (typically 10V or 24V)"
  - "Inspect the sensor wiring for loose connections or visible breaks between the sensor and drive input terminals"
part_price: "$80-250"
no_buy_pct: "60%"
---

## What this code means
The F0221 fault code on Siemens Micromaster drives (MM420 and MM440 models) signals that the proportional-integral (PI) controller feedback has fallen below the minimum acceptable threshold. This fault appears in closed-loop control systems where the drive expects a continuous feedback signal from a speed sensor, encoder, or pressure transducer to maintain a setpoint. The drive compares the received feedback value against parameter P2268 (PID Feedback below min. value), and when the signal drops below that configured limit, the drive throws F0221 and stops the motor to protect the process.

In practical terms, the drive cannot verify that the process variable (speed, pressure, or flow) is being maintained within the expected range. The fault does not necessarily mean a hardware failure. Configuration errors, such as setting P2268 too high for the actual sensor output range, account for many instances. Other times the sensor is disconnected, powered off, or outputting a near-zero voltage due to wiring problems or sensor failure.

## Before You Replace Anything

Technicians sometimes replace the feedback sensor before checking parameter P2268 or verifying sensor wiring. Always read P2268 and measure the actual sensor output voltage at the drive terminals before ordering a new sensor.

## Common Causes

- **Parameter P2268 set too high (~40%)** The minimum feedback threshold in P2268 is above the actual sensor output range, triggering the fault even when the sensor is working correctly.
- **Missing or disconnected feedback signal (~25%)** The drive receives no signal from the sensor because the sensor is powered off, a wire is disconnected, or a terminal connection is loose.
- **Faulty feedback sensor (~20%)** The external speed encoder, pressure transducer, or analog sensor has failed and outputs a voltage near zero or no signal at all.
- **Broken or shorted sensor wiring (~10%)** Wires between the sensor and the drive input terminals are broken, cut, or shorted, preventing the drive from reading the feedback value.
- **Incorrect feedback gain or scaling (~5%)** The feedback gain (related to parameters such as P2253) is set too low, so the drive sees a scaled value below the P2268 threshold even though the raw sensor signal is normal.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is the drive configured for PID closed-loop control (parameter P2200 set to 1)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is legitimate and you need to check sensor feedback and P2268 settings.<br><strong>No:</strong> The drive should not throw F0221 if PID is disabled. Check P2200 and reset the parameter to match your control strategy.</div>
</details>

<details class="dtree"><summary>Does the feedback sensor have power at its supply terminals (measure with a multimeter)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The sensor has power, so check the signal output voltage at the drive input terminals next.<br><strong>No:</strong> Restore power to the sensor (check fuses, power supply, and wiring) and retest.</div>
</details>

<details class="dtree"><summary>Does the sensor output voltage at the drive input terminals read above 0V when the process is running?</summary>
<div class="dtree-body"><strong>Yes:</strong> The sensor is working. Lower the value of P2268 to a level below the minimum expected sensor output.<br><strong>No:</strong> The sensor or wiring is faulty. Check wiring continuity and replace the sensor if wiring is intact.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Identify the control mode.** Check parameter P2200 on the drive keypad or via the BOP (Basic Operator Panel). If P2200 is set to 1, the drive is in PID closed-loop control mode and expects a feedback signal. If P2200 is 0, PID is disabled and the fault should not occur.
2. **Read parameter P2268.** Access P2268 (PID Feedback below min. value) and note the configured threshold. Compare this value to the minimum output voltage or signal level your feedback sensor is expected to produce during normal operation. If P2268 is higher than the sensor's minimum output, lower P2268 to a value slightly below the sensor's minimum expected signal.
3. **Check sensor power supply.** Use a multimeter to measure the voltage at the sensor's power terminals (often 10V or 24V depending on sensor type). If the sensor has no power, trace the supply wiring back to the drive or an external power supply and repair any broken connections or blown fuses.
4. **Measure the feedback signal at the drive input.** Locate the analog input terminals (commonly terminals 5 and 6) or encoder input terminals where the sensor connects. With the process running, measure the voltage or signal level. If the reading is 0V or near 0V, the sensor or wiring is faulty.
5. **Inspect and test sensor wiring.** Power down the drive and check continuity on each wire between the sensor and the drive input terminals. Look for broken wires, loose terminal screws, or damaged cable insulation. Repair or replace any damaged wiring.
6. **Verify or adjust feedback gain and scaling.** If the sensor outputs a signal but the drive reads a low value, check the feedback gain parameter (often P2253 or related scaling parameters). Adjust the gain so the drive's internal scaled value matches the actual sensor output range.
7. **Perform a test run.** After correcting P2268, restoring sensor power, or repairing wiring, clear the fault (press the reset button or cycle power) and start the drive. Monitor the feedback value on the display to confirm it stays above the P2268 threshold during operation. If the fault persists, replace the feedback sensor and retest.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Analog feedback sensor (speed or pressure transducer) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-vfd-f0221-fault-code&k=Analog+feedback+sensor+%28speed+or+pressure+transducer%29&tag=errorcodefixes-20) \| Choose a sensor with the correct output range (e.g. 0-10V or 4-20mA) that matches your drive's analog input configuration. |
| Encoder or tachometer | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-vfd-f0221-fault-code&k=Encoder+or+tachometer&tag=errorcodefixes-20) \| If using pulse feedback, make sure the encoder voltage and PPR (pulses per revolution) match the drive's encoder input specifications. |

## When to Call a Pro

Call a qualified technician or automation specialist if you are unfamiliar with VFD parameter programming, closed-loop PID tuning, or sensor wiring. Incorrect parameter settings can cause motor instability or damage the drive. A professional can verify sensor compatibility, calibrate the feedback loop, and make sure the PID controller is properly tuned for your application. If the fault persists after parameter adjustments and sensor replacement, the drive's analog input circuit may be damaged and require repair or drive replacement.

**Rough cost:** A pro service call runs about $150-400.
