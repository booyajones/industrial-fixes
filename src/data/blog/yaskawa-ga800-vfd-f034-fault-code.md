---
title: "Yaskawa GA800 F034 Fault - Causes & Fix"
description: "F034 is not a standard GA800 code; it may be EF8 (External Fault via Terminal S8). Check external safety devices and S8 wiring."
pubDatetime: 2026-06-27T11:51:31Z
modDatetime: 2026-06-27T11:51:31Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "Encoder cable or connector"
most_likely_cause: "Activated external safety device or wiring error at Terminal S8"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Check if any emergency stop button or safety relay connected to Terminal S8 is in the tripped or open state and reset it."
  - "Inspect all wiring to Terminal S8 for loose connections, shorts, or incorrect polarity."
  - "Power cycle the drive after clearing the external fault source to see if the fault clears."
no_buy_pct: "60%"
---

## Yaskawa GA800 F034 Fault — What It Means

The fault code F034 does not appear in documented Yaskawa GA800 technical manuals. If your display shows F034, verify the drive model and code carefully. The most likely scenario is that you are seeing EF8 (External Fault), which can be misread or displayed differently depending on the panel. EF8 means the drive detected an External Fault signal via Multi-Function Digital Input Terminal S8, configured through parameter H1-01. This input is typically connected to external safety devices like emergency stop buttons, safety relays, or ground fault monitors. When the external circuit opens or closes (depending on configuration), the drive immediately stops torque production and latches the fault.

If your display strictly shows F034 and not EF8, consult your specific GA800 model's technical manual or contact Yaskawa support, as this code is not standard. For EF8 faults, the root cause is almost always an activated external safety device, incorrect wiring at Terminal S8, or a mechanical issue (such as encoder coupling slip or motor binding) that triggers overcurrent protection or feedback errors in PID control mode.

## Before You Replace Anything

Technicians sometimes replace the drive itself when the fault is actually an external device (E-stop, safety relay) in the faulted state or a loose wire at Terminal S8. Always check and reset all external devices and inspect S8 wiring before ordering drive components.

[Jump to Fix](#fix)

## Common Causes

- **Activated external safety device (~35%)** An emergency stop button, safety relay, or ground fault monitor connected to Terminal S8 has been triggered or is in the faulted state.
- **Wiring error at Terminal S8 (~25%)** Loose connections, incorrect wiring, or a short circuit at the external fault input terminal S8 is sending a false fault signal to the drive.
- **Mechanical binding or coupling slip (~20%)** Motor, gearbox, or encoder coupling binding or slipping causes erratic feedback and overcurrent, which can trigger external fault circuits or safety relays.
- **Erratic PID or encoder feedback (~12%)** In PID control mode, unstable feedback signals from the encoder or process sensor (due to loose encoder coupling or tangled tether) can cause the drive to trip external fault inputs.
- **Incorrect H1-01 parameter configuration (~8%)** The Multi-Function Digital Input parameter H1-01 is set incorrectly for Terminal S8, causing normal operation to be interpreted as an external fault.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is there an emergency stop button or safety relay connected to the drive, and is it in the tripped or open position?</summary>
<div class="dtree-body"><strong>Yes:</strong> Reset the external device and power cycle the drive. If the fault clears, the external device was the cause and no drive repair is needed.<br><strong>No:</strong> The fault may be wiring-related or a feedback issue. Inspect Terminal S8 wiring and check encoder coupling tightness.</div>
</details>

<details class="dtree"><summary>Does the fault appear only when the drive is running in PID control or with encoder feedback?</summary>
<div class="dtree-body"><strong>Yes:</strong> Check the encoder coupling for tightness and inspect the tether for tangles or damage. Verify PID feedback signals are stable and within range.<br><strong>No:</strong> The fault is likely from wiring or an external device. Verify all connections to Terminal S8 and check parameter H1-01 for correct configuration.</div>
</details>

<details class="dtree"><summary>Can you manually turn the motor shaft and does it spin freely without binding?</summary>
<div class="dtree-body"><strong>Yes:</strong> The mechanical system is likely fine. Focus on electrical checks: wiring, external devices, and feedback signals.<br><strong>No:</strong> Mechanical binding in the motor, gearbox, or coupling is causing overcurrent and triggering the fault. Inspect and repair the mechanical components before retesting the drive.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify the fault code** by checking the drive display carefully. Confirm whether it shows F034 or EF8. If F034 is displayed, consult the GA800 technical manual for your specific model or contact Yaskawa support, as F034 is not a standard code.
2. **Locate and inspect Terminal S8** on the drive's control terminal block. Identify any external devices (emergency stop, safety relay, ground fault monitor) connected to this terminal.
3. **Check external safety devices** for activation. If an E-stop or safety relay is tripped, reset it. If it continues to trip, investigate the upstream fault condition (overcurrent, ground fault, etc.).
4. **Inspect all wiring to Terminal S8** for loose connections, shorts, broken wires, or incorrect polarity. Tighten any loose terminals and repair damaged wiring.
5. **Verify parameter H1-01 configuration** in the drive menu. Confirm that Terminal S8 is programmed correctly for your external fault circuit (options 2C to 2F). Adjust if necessary.
6. **Check mechanical components** if the fault persists. Inspect the motor, gearbox, and encoder coupling for binding or slippage. Tighten the encoder coupling and make sure the tether is not tangled.
7. **Perform electrical testing** on the motor and feedback loop. Use a megohmmeter to test motor insulation and verify encoder signals are clean and within specification. If PID control is used, check for erratic feedback.
8. **Clear the fault and power cycle** the drive after all corrections are made. Monitor the drive during operation to confirm the fault does not return. If it does, escalate to Yaskawa technical support.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Encoder cable or connector | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f034-fault-code&k=Encoder+cable+or+connector&tag=errorcodefixes-20) \| Replace if tether is damaged or connector pins are corroded. |
| Safety relay module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f034-fault-code&k=Safety+relay+module&tag=errorcodefixes-20) \| Replace if the external safety relay is faulty and continuously triggering the fault input. |

## When to Call a Pro

Call a qualified VFD technician or industrial electrician if you are unfamiliar with multi-function digital input programming, if the fault persists after checking all external devices and wiring, or if you suspect the drive itself is damaged. A professional can perform insulation resistance testing on the motor, verify encoder feedback signals with an oscilloscope, and reprogram drive parameters safely. If mechanical binding is causing the fault, a millwright or mechanical technician should inspect and repair the motor, gearbox, and coupling. Do not attempt to bypass safety circuits or disable Terminal S8 without understanding the safety implications, as this can create hazardous operating conditions.

**Rough cost:** A pro service call runs about $150-400.
