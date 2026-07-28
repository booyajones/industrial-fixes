---
title: "Hoshizaki EE(E5) Error Code - Causes & Fix"
description: "EE(E5) means high voltage. Most likely cause: utility overvoltage or wiring on wrong leg. Measure incoming voltage and check supply."
pubDatetime: 2026-06-19T10:29:06Z
modDatetime: 2026-06-19T10:29:06Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - refrigeration
  - hoshizaki
money_part: "Main control board"
most_likely_cause: "Utility overvoltage or incorrect high-leg wiring"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Read the error log on the controller to confirm the stored fault is E5, not another code displayed as EE."
  - "Measure incoming voltage at the machine's supply terminals with a multimeter while the compressor is running."
---

## What this code means
On Hoshizaki ice machines, **EE** is a generic error display. The actual fault code is stored in the controller's error log. When your service manual or error history shows **E5**, that specific code means **high voltage** — the voltage supplied to the machine is too high. Many Hoshizaki models display only EE on the live screen when errors other than E1 or E2 occur, so a technician must read the log to confirm the E5 event.

For machines on the 115 V platform, high-voltage alarms typically trip when incoming voltage exceeds roughly 147 volts (± 5%). Once correct voltage is restored, the alarm resets automatically. The error can be caused by utility overvoltage, incorrect wiring on a high-leg or split-phase supply, or less commonly a control-board sensing issue.

## Before You Replace Anything

Technicians sometimes replace the main control board before measuring supply voltage. Always measure incoming voltage at the machine under load and verify correct phase-to-neutral wiring first.

## Common Causes

- **Utility overvoltage (~50%)** The incoming line voltage at the branch circuit or supply transformer is too high and exceeds the machine's acceptable range.
- **High-leg or stinger supply (~30%)** The machine is connected to the wrong leg of a split-phase or three-phase system, delivering higher than rated voltage.
- **Incorrect wiring or line connections (~15%)** Phase-to-neutral or phase-to-phase wiring is mislanded at the machine or panel, resulting in overvoltage.
- **Control board voltage-sensing fault (~5%)** The control board or voltage-sensing circuit misreports normal supply voltage as too high.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the error log in the controller show code E5?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is high voltage. Proceed to measure incoming voltage and check wiring.<br><strong>No:</strong> The live EE display may represent a different fault code. Consult the service manual to decode the actual stored error.</div>
</details>

<details class="dtree"><summary>Is the measured voltage at the machine's supply terminals above the nameplate range (typically above 127 V for 115 V units)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Incoming voltage is too high. Trace the supply upstream to the panel and transformer and verify correct phase wiring.<br><strong>No:</strong> Voltage is normal. Inspect the control board and voltage-sensing circuit for a false-trigger fault.</div>
</details>

<details class="dtree"><summary>After restoring correct voltage, does the EE display clear when you cycle power?</summary>
<div class="dtree-body"><strong>Yes:</strong> The alarm was correct and auto-resets. Confirm stable voltage and monitor for recurrence.<br><strong>No:</strong> The fault persists. Check the control board, wiring harness, and voltage-sensing components for damage or drift.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Access the error log** on the controller to confirm that the stored fault code is E5, because the live display shows only EE for most errors.
2. **Measure incoming voltage** at the machine's supply terminals using a multimeter while the compressor is running and compare the reading to the nameplate voltage and acceptable range (for example, 104–127 V on some 115 V models).
3. **Trace the supply upstream** if voltage is high. Check the branch circuit, panel wiring, and transformer. Verify that the machine is not connected to a high leg or incorrect phase on a split-phase or three-phase system.
4. **Verify phase-to-neutral and phase-to-phase wiring** at the machine and panel. Correct any mislanding of conductors that delivers higher than rated voltage.
5. **Restore correct voltage** and cycle power to the machine. The E5 high-voltage alarm is an automatic-reset error and should clear once voltage returns to the acceptable range.
6. **Inspect the control board and voltage-sensing circuit** if voltage is normal but the fault persists. Look for damaged components, loose connectors, or drift in the sensing circuit.
7. **Monitor the machine** after repair to confirm stable voltage and no recurrence of the EE(E5) alarm.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Main control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-hoshizaki-ice-machine-ee-e5-error-code&k=Main+control+board&tag=errorcodefixes-20) \| Only if voltage-sensing circuit is faulty and voltage supply is confirmed correct. |
| Wiring harness or connectors | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-hoshizaki-ice-machine-ee-e5-error-code&k=Wiring+harness+or+connectors&tag=errorcodefixes-20) \| Replace if damaged or corroded at the supply terminals or control board. |

## When to Call a Pro

Call a qualified commercial refrigeration technician for any Hoshizaki EE(E5) error. Diagnosing high-voltage faults requires measuring live AC voltage under load, tracing panel and transformer wiring, and verifying correct phase connections on split-phase or three-phase supplies. Misdiagnosis can result in repeated nuisance trips or damage to the control board and compressor. If the cause is incorrect utility wiring or a transformer problem, you may also need an electrician to correct the upstream supply before the ice machine can run safely.

**Rough cost:** A pro service call runs about $150-350.
