---
title: "Yaskawa GA800 VFD AL-33 Fault - Causes & Fix"
description: "AL-33 on a Yaskawa GA800 VFD signals an analog input error. Check input wiring, verify signal range, and inspect for loose connections."
pubDatetime: 2026-07-22T07:27:02Z
modDatetime: 2026-07-22T07:27:02Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "Shielded twisted-pair signal cable"
most_likely_cause: "Loose or broken wiring at the analog input terminals"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Inspect analog input terminal blocks for loose, corroded, or broken wires"
  - "Review analog input parameter settings in the drive menu to confirm they match the signal type being used"
  - "Check if the fault clears after a power cycle and parameter review"
no_buy_pct: "60%"
---

## Yaskawa GA800 VFD AL-33 Fault — What It Means

The AL-33 fault on a Yaskawa GA800 variable frequency drive indicates an analog input signal problem. This alarm typically means the drive has detected an issue with one of its analog input channels, such as a 4-20mA or 0-10V signal used for speed reference or process control. The fault can be triggered by a signal that falls outside the expected range, a broken wire, incorrect parameter settings, or a failed input circuit.

The GA800 monitors analog inputs continuously and will flag AL-33 when it cannot read a valid signal or when the signal deviates from programmed thresholds. This is a protective alarm to prevent the drive from operating with bad data that could cause equipment damage or unsafe operation.

## Before You Replace Anything

Technicians sometimes replace the entire VFD when the actual problem is a simple wiring issue or incorrect parameter setting. Always verify input signal integrity with a multimeter and review parameter settings before replacing the drive.

[Jump to Fix](#fix)

## Common Causes

- **Loose or damaged input wiring (~40%)** Vibration or poor installation can cause wires at the analog input terminals to loosen or break, interrupting the signal path.
- **Incorrect analog input parameter settings (~25%)** The drive's input scaling, signal type selection, or threshold parameters may not match the actual signal being sent.
- **Failed upstream sensor or controller (~15%)** The device sending the analog signal, such as a potentiometer, PLC, or pressure transducer, may have failed or lost power.
- **Noisy or grounded signal cable (~10%)** Electrical noise from nearby power cables or a ground fault in the signal cable can corrupt the analog input and trigger the fault.
- **Failed analog input circuit on the drive (~10%)** Internal damage to the VFD's analog input circuitry, often from a voltage spike or miswiring, can prevent proper signal reading.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault appear immediately on power-up before any signal is applied?</summary>
<div class="dtree-body"><strong>Yes:</strong> The drive may be expecting a signal that is not present, or a parameter is set incorrectly. Check that the analog input is configured for the correct signal type and that any 'loss of signal' detection parameters are appropriate.<br><strong>No:</strong> The fault occurs during operation, so focus on signal integrity, wiring continuity, and upstream device health.</div>
</details>

<details class="dtree"><summary>Can you measure the correct signal voltage or current at the drive input terminals with a multimeter?</summary>
<div class="dtree-body"><strong>Yes:</strong> The signal is arriving at the drive, so the problem is likely internal to the VFD or in the parameter settings. Review input scaling and consider drive circuitry failure.<br><strong>No:</strong> The signal is not reaching the drive. Check the upstream device, inspect cable continuity, and look for breaks or shorts in the wiring.</div>
</details>

<details class="dtree"><summary>Does the fault clear after you disconnect and reconnect the analog input cable?</summary>
<div class="dtree-body"><strong>Yes:</strong> A loose connection or intermittent contact is the likely cause. Clean and tighten all terminals and consider replacing the cable if corrosion is present.<br><strong>No:</strong> The fault is persistent, pointing to a failed upstream device, incorrect parameters, or internal drive damage.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the VFD** and lock out the main disconnect to safely access terminals.
2. **Inspect the analog input terminal block** on the GA800 for loose, corroded, or broken wires and tighten or repair as needed.
3. **Verify the signal type and range** by consulting the wiring diagram and checking that the upstream device is outputting 4-20mA, 0-10V, or the configured signal.
4. **Use a multimeter** to measure the analog signal at the drive input terminals while the upstream device is powered and verify it falls within the expected range.
5. **Review the GA800 parameter settings** for the analog input, confirming signal type, scaling, and any loss-of-signal detection thresholds match the application.
6. **Check for electrical noise** by routing the analog signal cable away from power wiring and using shielded twisted-pair cable with proper grounding if noise is suspected.
7. **Clear the fault** from the drive's display or keypad and test operation; if the fault persists and wiring and parameters are correct, the drive's analog input circuit may be damaged and require factory repair or replacement.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Shielded twisted-pair signal cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-al-33-fault-code&k=Shielded+twisted-pair+signal+cable&tag=errorcodefixes-20) \| For replacing damaged or noisy analog input wiring; match gauge and length to your installation. |
| Analog input module or circuit board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-al-33-fault-code&k=Analog+input+module+or+circuit+board&tag=errorcodefixes-20) \| Factory replacement part for internal analog input circuitry if damaged; contact Yaskawa for your GA800 model and frame size. |

## When to Call a Pro

Call a qualified electrician or VFD technician if you are not comfortable working with industrial control wiring or if the fault persists after verifying wiring and parameters. High-voltage AC power is present inside the VFD enclosure even when the drive is stopped, and incorrect wiring or parameter changes can damage connected equipment. A professional can perform signal tracing, load parameter backups, and coordinate factory repair or replacement of internal circuitry if the drive's analog input has failed.

**Rough cost:** A pro service call runs about $150-400.
