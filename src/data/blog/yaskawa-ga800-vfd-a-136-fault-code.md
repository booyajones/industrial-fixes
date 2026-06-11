---
title: "Yaskawa GA800 A.136 Fault - Causes & Fix"
description: "A.136 on a Yaskawa GA800 means motor thermistor or thermal protection circuit is open or tripped. Most often a broken thermistor wire."
pubDatetime: 2026-06-09T11:25:50Z
modDatetime: 2026-06-09T11:25:50Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "Motor thermistor or thermal protector"
most_likely_cause: "open or disconnected thermistor wiring"
likelihood: "the most common cause"
diy_or_pro: "pro"
---

## Yaskawa GA800 A.136 Fault — What It Means

The A.136 fault code on a Yaskawa GA800 variable frequency drive indicates the drive has detected a problem with the motor temperature protection circuit. This alarm is triggered when the thermistor or thermal protection device monitoring motor temperature reads as open, disconnected, or tripped. The drive sees the thermal input circuit as abnormal and stops operation to protect the motor from potential overheating damage. This is not an overcurrent or power fault. It specifically relates to the physical thermal sensor circuit between the motor and the drive control board.

The fault occurs when the drive expects to see a continuous resistance path through the motor's thermal protection device but instead detects an open circuit or out-of-range reading. Common triggers include a thermistor wire that has broken or come loose at a terminal, incorrect parameter setup telling the drive to monitor an unused thermal input, or a legitimate motor overheating condition that has opened the thermal protector. Occasionally the motor's internal thermal device itself has failed open, or the drive's thermal input circuit on the control board is faulty.

## Before You Replace Anything

Technicians sometimes replace the drive or motor when the real problem is a loose terminal block connection or incorrect thermal-input parameter assignment. Always verify wiring continuity and parameter settings before ordering expensive hardware.

[Jump to Fix](#fix)

## Common Causes

- **Broken or disconnected thermistor wire (~40%)** The most frequent cause is a thermistor lead that has broken, pulled loose from a terminal block, or disconnected at the motor junction box or drive control terminals.
- **Incorrect drive parameter for thermal input (~20%)** The drive may be configured to monitor a thermal input that is not wired or does not match the actual motor protection device installed.
- **Failed motor thermistor or thermal protector (~15%)** The temperature sensor or thermal switch inside the motor has failed open or degraded, sending no signal or an out-of-range reading to the drive.
- **Actual motor overheating (~15%)** The motor has legitimately overheated from overload, locked rotor, poor ventilation, blocked cooling fan, high ambient temperature, or mechanical binding, causing the thermal device to trip.
- **Faulty drive thermal input circuit (~10%)** The control board input that reads the thermistor signal is damaged or has failed, causing the drive to see an open circuit even when external wiring and motor thermal device are good.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the motor feel excessively hot to the touch or show signs of overheating (discoloration, burning smell, blocked fan)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The thermal device may have tripped legitimately. Allow the motor to cool, check for overload or mechanical binding, clear any blockages to ventilation, then reset and retest.<br><strong>No:</strong> The fault is likely electrical rather than thermal. Proceed to check wiring and parameter settings.</div>
</details>

<details class="dtree"><summary>Can you verify continuity through the thermistor circuit with a multimeter from motor thermal leads to the drive thermal input terminals?</summary>
<div class="dtree-body"><strong>Yes:</strong> The wiring is intact. Check the drive parameter assignment for the thermal input and confirm it matches the motor protection device type. If correct, the motor thermistor or drive input may be faulty.<br><strong>No:</strong> You have found an open circuit. Inspect terminals, connectors, and cable for breaks or loose connections and repair before retesting.</div>
</details>

<details class="dtree"><summary>After reconnecting any loose wiring and cycling power, does the A.136 alarm clear and stay off during a test run?</summary>
<div class="dtree-body"><strong>Yes:</strong> The problem was intermittent wiring or a temporary condition. Monitor the system and verify all thermal connections are secure.<br><strong>No:</strong> The fault persists. Isolate whether the problem follows the motor, cable, or drive by substituting known-good components or testing the thermal device separately.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Record the alarm history** from the drive operator display and note any recent changes to load, environment, or wiring before clearing the fault.
2. **Inspect the motor physically** for signs of overheating, binding, locked rotation, blocked cooling fan, or unusual temperature, and check that the load is not overloaded or jammed.
3. **Trace and test the thermistor wiring** from the motor junction box or thermal leads to the drive control terminals, checking for continuity with a multimeter and inspecting every terminal block, connector, and splice for looseness or damage.
4. **Verify the drive thermal-input parameter** in the GA800 programming menu to confirm it is set for the correct type and channel of motor thermal protection device actually installed on your motor.
5. **Power down the drive completely**, reseat or repair any loose or broken thermistor connections, then power up and attempt a test run to see if the alarm clears.
6. **Isolate the fault location** by disconnecting the thermistor circuit at the drive and measuring the resistance of the motor thermal device alone, or by substituting a known-good motor or cable to determine whether the fault follows the motor, wiring, or drive input.
7. **Replace the failed component** only after confirming which part is defective: repair or replace the thermistor wiring harness if open, replace the motor thermistor or thermal protector if the motor device tests bad, or replace the drive control board or entire drive if the thermal input circuit is proven faulty with good external components.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor thermistor or thermal protector | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-136-fault-code&k=Motor+thermistor+or+thermal+protector&tag=errorcodefixes-20) \| Match the type and resistance curve to your motor manufacturer's specification; consult the motor nameplate or wiring diagram for the correct thermal device model. |
| Thermistor cable or wiring harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-136-fault-code&k=Thermistor+cable+or+wiring+harness&tag=errorcodefixes-20) \| Shielded multi-conductor cable rated for the environment, with the correct connector or terminal ends for your motor and drive. |
| Drive control board or complete VFD replacement | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-136-fault-code&k=Drive+control+board+or+complete+VFD+replacement&tag=errorcodefixes-20) \| Only if external wiring and motor thermal device test good but the thermal input still reads open; confirm part availability and cost before ordering. |

## When to Call a Pro

Call a qualified industrial electrician or drive technician if you are not trained to work safely around high-voltage VFD circuits, if you cannot safely access motor wiring or drive terminals, or if your testing shows the drive control board or motor internal components need replacement. Professional diagnosis is also recommended when the fault persists after you have verified wiring continuity and parameter settings, because isolating a faulty drive input versus a failed motor thermal device requires specialized test equipment and experience with Yaskawa drive troubleshooting. Many facilities require certified technicians to service VFD equipment under warranty or safety policy.

**Rough cost:** A pro service call runs about $150-400 depending on whether repair involves rewiring, thermistor replacement, or motor/drive component swap.
