---
title: "Yaskawa A1000 FbL Fault - Causes & Fix"
description: "FbL means PID feedback loss: the feedback signal fell below the set threshold. Usually caused by faulty wiring or a bad sensor."
pubDatetime: 2026-06-11T10:12:42Z
modDatetime: 2026-06-11T10:12:42Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "PID feedback sensor or transducer"
most_likely_cause: "Incorrect or loose PID feedback wiring"
likelihood: "the most common cause"
diy_or_pro: "pro"
---

## Yaskawa A1000 FbL Fault — What It Means

The FbL fault on a Yaskawa A1000 drive stands for PID Feedback Loss. It trips when the PID feedback input stays below the level programmed in parameter b5-13 for longer than the time set in b5-14, and only when feedback-loss detection is enabled by setting parameter b5-12 to 2 or 5. This is not a general drive output fault. It is specific to the PID feedback circuit and sensor loop used in closed-loop process control applications.

The drive monitors the feedback signal from a sensor or transducer (such as a pressure sensor, flow meter, or temperature sensor) and compares it to the threshold you configured. When the signal is too low for too long, the drive assumes the feedback loop has failed and shuts down to protect the process.

## Before You Replace Anything

Technicians sometimes replace the drive control board before checking the feedback sensor and wiring. Always verify sensor output with a multimeter and inspect every terminal in the feedback loop before swapping boards.

[Jump to Fix](#fix)

## Common Causes

- **Incorrect or loose PID feedback wiring (~40%)** Open connections, reversed polarity, or loose terminals in the feedback loop prevent the drive from seeing a valid signal.
- **Failed feedback sensor or transducer (~30%)** A damaged or malfunctioning pressure, flow, or temperature sensor stops producing the correct output signal.
- **Inappropriate parameter settings (~20%)** Parameters b5-12, b5-13, or b5-14 are set too aggressively or do not match the application, causing nuisance faults.
- **Damaged feedback input circuit (~10%)** The feedback input stage on the drive control board has failed, even though wiring and sensor are good.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is parameter b5-12 set to 2 or 5?</summary>
<div class="dtree-body"><strong>Yes:</strong> Feedback-loss detection is enabled. Proceed to check wiring and sensor.<br><strong>No:</strong> The fault should not occur. Verify drive parameters and reset the fault.</div>
</details>

<details class="dtree"><summary>Does the feedback sensor produce a signal when tested with a multimeter?</summary>
<div class="dtree-body"><strong>Yes:</strong> Sensor is working. Check wiring from sensor to drive for opens or loose connections.<br><strong>No:</strong> Sensor is faulty or unpowered. Replace the sensor or restore its power supply.</div>
</details>

<details class="dtree"><summary>Are b5-13 and b5-14 values appropriate for your application?</summary>
<div class="dtree-body"><strong>Yes:</strong> Parameters are correct. Suspect the feedback input circuit on the drive control board.<br><strong>No:</strong> Adjust threshold and delay parameters to match your process requirements and reset.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Confirm the fault code** by viewing the drive display and noting that FbL is active.
2. **Check parameter b5-12** to verify feedback-loss detection is enabled (value 2 or 5). If it is not enabled, the fault should not occur and you may have a different issue.
3. **Review parameters b5-13 and b5-14** and compare them to your application requirements. make sure the feedback-loss threshold and delay match the sensor range and process dynamics.
4. **Inspect all feedback wiring** from the sensor or transducer to the drive feedback input terminals. Look for loose screws, broken wires, reversed polarity, or oxidized connections and repair any problems.
5. **Test the feedback sensor** with a multimeter or process simulator. Verify it produces the expected voltage, current, or resistance signal. Replace the sensor if it is dead or out of spec.
6. **Swap the control board** if wiring and sensor are confirmed good but the fault persists. The feedback input circuit may be damaged.
7. **Cycle power and reset the fault** after repairs. Run the system and monitor for recurrence. If the fault returns immediately, recheck all steps or consult Yaskawa technical support.

## Parts Often Needed

| Part | Notes |
|------|-------|
| PID feedback sensor or transducer | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-fbl-fault-code&k=PID+feedback+sensor+or+transducer&tag=errorcodefixes-20) \| Match type (voltage, current, pressure, flow) and range to your application. |
| Yaskawa A1000 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-fbl-fault-code&k=Yaskawa+A1000+control+board&tag=errorcodefixes-20) \| Order by exact drive model and serial number if feedback input circuit is damaged. |
| Shielded feedback cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-fbl-fault-code&k=Shielded+feedback+cable&tag=errorcodefixes-20) \| Use if existing wiring is damaged or not properly shielded. |

## When to Call a Pro

Call a qualified drive technician or controls integrator if you are not familiar with PID control loops, parameter programming, or multimeter testing of analog signals. Work on VFD feedback circuits requires understanding of low-voltage analog signals, proper grounding, and shielding practices. If you have verified the sensor and wiring but the fault persists, the drive control board or internal circuitry may be damaged and should be diagnosed by someone with VFD repair experience. Always follow lockout/tagout procedures and consult the A1000 technical manual before working inside the drive enclosure.

**Rough cost:** A pro service call runs about $200-600.

## See Also

- [Yaskawa GA800 E03 Fault Code - Causes & Fix](/posts/yaskawa-ga800-e03-fault-code/)
- [Yaskawa GA800 E99 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-e99-fault-code/)
- [Yaskawa GA700 OC Fault — Overcurrent Fix](/posts/yaskawa-ga700-fault-oc/)
- [Yaskawa A1000 CPF03 - Causes & Fix](/posts/yaskawa-a1000-vfd-cpf03-fault-code/)
