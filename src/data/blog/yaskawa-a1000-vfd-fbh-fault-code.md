---
title: "Yaskawa A1000 FbH Fault - Causes & Fix"
description: "FbH means Excessive PID Feedback: the process signal exceeded the threshold in parameter b5-36. Check PID limits and feedback wiring first."
pubDatetime: 2026-06-12T10:10:40Z
modDatetime: 2026-06-12T10:10:40Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "PID feedback sensor or transmitter"
most_likely_cause: "PID setpoint or limit parameters set incorrectly for the application"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Review parameters b5-12, b5-36, and b5-37 on the keypad to confirm they match the application requirements and that fault detection is intentionally enabled"
  - "Check the fault history on the drive monitor to confirm FbH is the active alarm and note when it occurs in the process cycle"
  - "Inspect the feedback wiring from sensor to drive control terminals for loose, corroded, or mislanded connections"
no_buy_pct: "60%"
---

## Yaskawa A1000 FbH Fault — What It Means

FbH on a Yaskawa A1000 drive indicates Excessive PID Feedback. The drive has detected that the PID feedback signal stayed above the threshold configured in parameter b5-36 for longer than the time delay set in parameter b5-37. This fault only appears when parameter b5-12 is set to 2 or 5 to enable PID fault detection.

The fault points to a problem with the process control loop rather than the power stage. Either the feedback sensor is sending a signal that genuinely exceeds the expected range, the feedback wiring has an open or short, the sensor itself has failed, or the PID limit parameters are set incorrectly for the actual application. The drive is protecting the process by shutting down when it detects the feedback is out of the expected operating band.

## Before You Replace Anything

Technicians sometimes replace the drive itself when the real problem is a faulty feedback sensor or incorrect parameter b5-36/b5-37 settings. Always verify the feedback signal at the terminals and review the PID parameters before swapping the VFD.

[Jump to Fix](#fix)

## Common Causes

- **PID limit parameters set too low or incorrectly (~40%)** Parameter b5-36 (feedback threshold) or b5-37 (time delay) does not match the actual process signal range, so normal operation triggers the fault.
- **Faulty or failed feedback sensor or transmitter (~30%)** The sensor on the process side is sending an out-of-range, erratic, or absent signal to the drive's PID input.
- **Incorrect or damaged feedback wiring (~20%)** Open, shorted, loose, or mislanded wiring between the sensor and the drive control terminals causes the drive to see an abnormal signal.
- **PID fault detection unintentionally enabled (~10%)** Parameter b5-12 is set to 2 or 5 when the application does not require PID fault monitoring, causing nuisance trips.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault history on the keypad show FbH occurring repeatedly at the same point in the process cycle?</summary>
<div class="dtree-body"><strong>Yes:</strong> The process signal genuinely exceeds the threshold at that point. Review b5-36 and b5-37 to confirm they are set correctly for the application, or check if the sensor is reading high due to a real process condition.<br><strong>No:</strong> The fault is intermittent or random. Inspect the feedback wiring for loose connections or check the sensor for instability or failure.</div>
</details>

<details class="dtree"><summary>Is parameter b5-12 set to 2 or 5?</summary>
<div class="dtree-body"><strong>Yes:</strong> PID fault detection is enabled. Confirm this is intentional for your application. If not needed, change b5-12 to disable the fault.<br><strong>No:</strong> The fault should not be active. Verify you are looking at the correct drive and that the parameter has not been changed accidentally.</div>
</details>

<details class="dtree"><summary>Does the feedback signal at the drive's control terminals measure within the expected range when tested with a meter?</summary>
<div class="dtree-body"><strong>Yes:</strong> The sensor and wiring are delivering a normal signal. The problem is likely incorrect b5-36 or b5-37 settings. Adjust the parameters to match the actual signal range.<br><strong>No:</strong> The signal is out of range, absent, or erratic. Check the sensor and wiring for faults, open circuits, or shorts, and replace the sensor if defective.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify the fault** by checking the drive keypad or monitor history to confirm FbH is the active alarm and note the conditions when it occurs.
2. **Review PID parameters** by navigating to b5-12, b5-36, and b5-37 on the keypad. Confirm b5-12 is intentionally set to 2 or 5 and that b5-36 (feedback threshold) and b5-37 (time delay) match the application's sensor range and process requirements.
3. **Inspect the feedback wiring** from the sensor or transmitter to the drive's control terminals. Look for loose, corroded, open, shorted, or mislanded connections and correct any faults.
4. **Test the feedback sensor** at the process side by measuring the output signal with a multimeter or process meter. If the signal is unstable, out of range, or absent, replace the sensor or transmitter.
5. **Adjust parameters** if the sensor and wiring are good but the limits are set incorrectly. Increase b5-36 or b5-37 to match the actual operating range, or disable PID fault detection by changing b5-12 if not required.
6. **Re-test the process** after making corrections. Run the system through a full cycle and monitor the drive to confirm the feedback signal stays within the configured band and the fault does not return.
7. **Use the drive's monitor functions** and auto-tuning tools to verify the PID control loop is configured correctly and stable under load.

## Parts Often Needed

| Part | Notes |
|------|-------|
| PID feedback sensor or transmitter | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-fbh-fault-code&k=PID+feedback+sensor+or+transmitter&tag=errorcodefixes-20) \| Replace if the sensor output is out of range, erratic, or absent when tested. Match the sensor type and signal range (voltage, current, or resistance) to the original specification for your process application. |
| Feedback signal cable or shielded wire | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-fbh-fault-code&k=Feedback+signal+cable+or+shielded+wire&tag=errorcodefixes-20) \| Use shielded twisted-pair cable rated for the control voltage and environment if the existing wiring is damaged, shorted, or incorrectly installed. |

## When to Call a Pro

Call a qualified industrial controls technician or VFD specialist if you are not familiar with PID loop tuning, drive parameter programming, or control wiring. The FbH fault requires verifying the feedback signal against the drive's configuration, and incorrect settings can cause process instability or damage to equipment. A technician can measure the feedback signal at the terminals, verify the sensor is working correctly, adjust b5-12, b5-36, and b5-37 to match your application, and use the drive's diagnostic and auto-tuning features to stabilize the control loop. If the drive itself has failed (rare with FbH), a specialist can also test the control board and arrange factory repair or replacement.

**Rough cost:** A pro service call runs about $150-400 for service call, wiring repair, sensor replacement, and parameter adjustment.

## See Also

- [Yaskawa GA800 E81 Fault Code - Causes & Fix](/posts/yaskawa-ga800-vfd-e81-fault-code/)
- [Yaskawa GA800 E11 Fault Code - Causes & Fix](/posts/yaskawa-ga800-e11-fault-code/)
- [Yaskawa GA800 oV Fault — DC Overvoltage Fix](/posts/yaskawa-ga800-error-ov/)
- [Yaskawa VFD Fault OH — Causes & Fix](/posts/yaskawa-vfd-fault-oh/)
