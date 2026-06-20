---
title: "Yaskawa A1000 Uv2 - Causes & Fix"
description: "Uv2 means control power supply undervoltage on the A1000 VFD. Check incoming power phases and parameter L2-02 setting first."
pubDatetime: 2026-06-11T09:59:16Z
modDatetime: 2026-06-11T09:59:16Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Yaskawa A1000 control board (model-specific)"
most_likely_cause: "Input power disturbance or phase loss"
likelihood: "the most common cause"
diy_or_pro: "pro"
---

## Yaskawa A1000 Uv2 — What It Means

The Uv2 fault on a Yaskawa A1000 variable frequency drive indicates that the voltage supplying the drive's control circuits has dropped below the minimum threshold the drive needs to operate. This is not a main power or output stage problem. The control power supply feeds the internal logic, display, and control board. When that supply voltage sags or disappears, the drive protects itself by throwing Uv2 and shutting down. The fault is documented for certain smaller A1000 models (2A0004 to 2A0056 and 4A0002 to 4A0031) and is often linked to incoming power disturbances, phase loss, or incorrect settings in parameter L2-02, which governs ride-through and undervoltage behavior.

In most cases the fault points to a real event: a momentary brownout, a loose wire on the input terminals, or a missing phase. Less often, someone has changed L2-02 from its factory default without installing the optional momentary power loss ride-through hardware, and the drive now trips on normal grid fluctuations. If external power and parameters check out but the fault keeps coming back, the control board or its internal power supply circuit has failed and needs replacement.

## Before You Replace Anything

Technicians sometimes replace the entire drive or control board before checking incoming line voltage and parameter L2-02. Measure all three input phases under load and verify L2-02 matches the installed options before ordering boards.

[Jump to Fix](#fix)

## Common Causes

- **Input power disturbance or phase loss (~50%)** Loose terminals, a missing phase, or momentary brownouts on the incoming supply drop the control voltage below threshold.
- **Incorrect parameter L2-02 setting (~25%)** Someone changed the ride-through or undervoltage parameter without the optional momentary power loss unit, and the drive now trips on normal grid sags.
- **Damaged or loose control power wiring (~15%)** Control circuit wiring has corroded, vibrated loose, or been nicked, interrupting the supply to the control board.
- **Failed control board or control power supply circuit (~10%)** The internal power supply section or control board itself has failed and can no longer regulate voltage for the logic circuits.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault clear after a power cycle and stay cleared during normal operation?</summary>
<div class="dtree-body"><strong>Yes:</strong> The event was a one-time power disturbance. Monitor incoming voltage and check for loose connections.<br><strong>No:</strong> The fault recurs, so move to checking parameters and control power wiring next.</div>
</details>

<details class="dtree"><summary>Is parameter L2-02 set to something other than the factory default for your drive model and installed options?</summary>
<div class="dtree-body"><strong>Yes:</strong> Restore L2-02 to the correct default or install the optional ride-through unit if required by your application.<br><strong>No:</strong> The parameter is correct, so focus on incoming power quality and control board health.</div>
</details>

<details class="dtree"><summary>Do all three input phases measure within 5% of each other under load?</summary>
<div class="dtree-body"><strong>Yes:</strong> Incoming power is balanced. Suspect the control board or internal control supply circuit.<br><strong>No:</strong> You have phase imbalance or loss. Repair loose terminals, damaged cables, or upstream breaker issues.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify incoming power.** Measure voltage on all three input phases (L1, L2, L3) at the drive terminals with the motor running. Look for phase loss, imbalance greater than 5%, or voltage sags during motor start.
2. **Inspect input terminals and wiring.** Shut off and lock out the disconnect. Check that all input lugs are tight, wires are not nicked or corroded, and terminal blocks show no burn marks.
3. **Check parameter L2-02.** Connect a keypad or programming software and read L2-02. Compare the value to the factory default listed in the A1000 manual for your exact model and capacity. If it has been changed and you do not have the optional momentary power loss ride-through unit installed, restore the default.
4. **Cycle power and test.** Close the disconnect and observe the drive through a few start-stop cycles. If Uv2 does not return, the fault was a transient event and you are done. If it trips again, move to the next step.
5. **Inspect control power wiring.** Look at any control-circuit terminal strips, auxiliary contacts, or external control transformers that feed the drive's control terminals. Tighten loose connections and replace damaged wire.
6. **Test or replace the control board.** If external power and parameters are correct and the fault persists, the control power supply section or control board has failed. Consult Yaskawa technical support or your distributor for board-level diagnostics, or replace the board.
7. **Consider the optional ride-through unit.** For models 2A0004 to 2A0056 or 4A0002 to 4A0031, if your application requires immunity to momentary power loss, install the Yaskawa optional momentary power loss ride-through accessory and adjust L2-02 accordingly.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa A1000 control board (model-specific) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-uv2-fault-code&k=Yaskawa+A1000+control+board+%28model-specific%29&tag=errorcodefixes-20) \| Order by exact A1000 model and serial number to match firmware and hardware revision. |
| Yaskawa optional momentary power loss ride-through unit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-uv2-fault-code&k=Yaskawa+optional+momentary+power+loss+ride-through+unit&tag=errorcodefixes-20) \| For models 2A0004 to 2A0056 or 4A0002 to 4A0031 that need ride-through capability. |

## When to Call a Pro

Diagnosing and repairing Uv2 on an A1000 involves working inside a live high-voltage cabinet, reading drive parameters, and interpreting three-phase voltage under load. If you are not trained in VFD service and do not have the tools to safely measure line voltage and diagnose control circuits, call a qualified electrician or automation technician. Also call a pro if the fault persists after you have verified incoming power and parameters, because at that point the control board or internal power supply needs replacement and the drive may need factory calibration afterward.

**Rough cost:** A pro service call runs about $200-800 depending on whether it is wiring, a control board, or drive replacement.

## See Also

- [Yaskawa GA800 E25 Fault Code - Causes & Fix](/posts/yaskawa-ga800-vfd-e25-fault-code/)
- [Yaskawa GA800 E88 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-e88-fault-code/)
- [Yaskawa V1000 OC Fault — Overcurrent](/posts/yaskawa-v1000-fault-oc/)
- [Yaskawa A1000 CPF03 - Causes & Fix](/posts/yaskawa-a1000-vfd-cpf03-fault-code/)
