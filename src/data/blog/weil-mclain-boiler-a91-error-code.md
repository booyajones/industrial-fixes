---
title: "Weil-McLain A91 Error Code - Causes & Fix"
description: "A91 means ignition failure: the boiler tried to light but did not prove flame. Check gas supply open and flame sensor clean first."
pubDatetime: 2026-06-15T11:47:13Z
modDatetime: 2026-06-15T11:47:13Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - boiler
  - weil-mclain
money_part: "Flame sensor / flame rod"
most_likely_cause: "dirty or failed flame sensor"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Confirm the gas cock on the supply line to the boiler is fully open"
  - "Verify the thermostat is calling for heat and the boiler control shows a demand signal"
  - "Check that no rollout or safety limit switches are tripped and need manual reset"
part_price: "$30–60"
no_buy_pct: "40%"
---

## Weil-McLain A91 Error Code — What It Means

The A91 fault code on Weil-McLain boilers indicates an ignition failure or failed light-off condition. The control module attempted to start the burner and light the flame, but the flame was not proven within the allowed trial time. When this happens the boiler locks out and requires a reset after the underlying problem is corrected.

Because Weil-McLain uses different control platforms across product lines, the exact label and behavior of A91 can vary by model and control family. Always verify the fault definition in your specific boiler's service manual or by retrieving the stored fault history from the diagnostics menu on the control board. The core issue is the same: no flame was established when the control expected it.

## Before You Replace Anything

Many people replace the gas valve or ignitor before checking the flame sensor. Clean the flame rod with fine emery cloth or sandpaper first, then verify it proves flame during startup before ordering any parts.

[Jump to Fix](#fix)

## Common Causes

- **Dirty or failed flame sensor (~40%)** Soot, oxidation, or mineral buildup on the flame rod prevents the control from detecting flame current, so the boiler locks out even if the burner did light briefly.
- **Gas supply closed or insufficient (~25%)** A closed manual shutoff, a tripped upstream regulator, or low inlet pressure means no gas reaches the burner during the trial for ignition.
- **Failed ignitor or electrode (~15%)** A cracked, contaminated, or improperly gapped ignition electrode will not produce a spark strong enough to light the gas.
- **Gas valve not opening (~12%)** The control may command the valve but the valve coil, wiring, or internal mechanism fails to open and deliver gas to the burner.
- **Grounding or wiring fault in flame-sense circuit (~5%)** A broken, corroded, or poorly grounded wire in the flame-sense path causes intermittent or no flame current signal even when flame is present.
- **Control board fault (~3%)** The ignition control module itself can fail and report A91 even when the flame train is healthy.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is the manual gas shutoff cock on the supply line fully open?</summary>
<div class="dtree-body"><strong>Yes:</strong> Gas is available to the boiler. Move on to checking the flame sensor and ignition components.<br><strong>No:</strong> Open the gas cock fully and reset the boiler. If it lights and runs normally the problem is solved.</div>
</details>

<details class="dtree"><summary>Does the burner light briefly and then drop out after a few seconds?</summary>
<div class="dtree-body"><strong>Yes:</strong> The ignition system is working but flame sensing is failing. Clean or replace the flame sensor.<br><strong>No:</strong> No ignition at all suggests a problem with gas delivery, the ignitor, or the gas valve. Check for spark and gas flow at the burner.</div>
</details>

<details class="dtree"><summary>Can you see or hear a spark at the ignitor during a call for heat?</summary>
<div class="dtree-body"><strong>Yes:</strong> Ignition voltage is present. Verify gas is flowing to the burner and that the valve is opening when commanded.<br><strong>No:</strong> No spark means the ignitor, its wiring, or the control output is faulty. Inspect the electrode and connections.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off power and gas.** Shut off the boiler circuit breaker or switch and close the manual gas shutoff valve before opening the cabinet or touching any components.
2. **Verify a heat call.** Confirm the thermostat is calling for heat and that the boiler control display shows a demand or call status. Check that no safety limits or rollout switches are open.
3. **Inspect the gas supply.** Open the manual gas cock fully if it was closed. If your system has an upstream shutoff or a sediment trap, confirm those are clear and that inlet pressure is adequate.
4. **Check and clean the flame sensor.** Locate the flame rod (a thin stainless probe in the burner area). Remove it and gently clean the sensing surface with fine emery cloth or sandpaper until shiny. Reinstall snugly and check that the wire connection is tight and not corroded.
5. **Inspect the ignitor and electrode.** Look for cracks, heavy carbon buildup, or incorrect spacing between the electrode and ground. Clean or replace the ignitor if damaged. Consult your model's service manual for the correct gap specification.
6. **Test gas valve operation.** Restore power and gas and initiate a call for heat. Listen or use a multimeter to confirm the control is sending voltage to the gas valve during trial for ignition. If voltage is present but no gas flows, the valve or upstream supply is suspect.
7. **Retrieve fault history from the control.** Use the diagnostics menu or contractor access buttons on the control board to view stored fault codes and timestamps. This can confirm whether A91 was a one-time event or a pattern.
8. **Reset and observe a full cycle.** After addressing the fault, reset the boiler per the manual (power cycle or press the reset button). Watch the entire ignition sequence to verify stable flame establishment and that the code does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Flame sensor / flame rod | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a91-error-code&k=Flame+sensor+%2F+flame+rod&tag=errorcodefixes-20) \| Match the probe length and thread to your model. Universal rods are available but OEM parts make sure correct fit. |
| Ignitor / ignition electrode | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a91-error-code&k=Ignitor+%2F+ignition+electrode&tag=errorcodefixes-20) \| Verify voltage rating and mounting style. Measure the gap spec in your manual before installing. |
| Gas valve | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a91-error-code&k=Gas+valve&tag=errorcodefixes-20) \| Must match your boiler model and gas type (natural or LP). Confirm voltage and pressure ratings before ordering. |
| Ignition control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a91-error-code&k=Ignition+control+board&tag=errorcodefixes-20) \| Specific to the control family installed on your boiler. Record the existing board part number and firmware revision. |

## When to Call a Pro

Call a licensed HVAC or boiler technician for any work involving the gas train, gas valve replacement, or combustion testing. Professionals have the tools to measure flame current, verify gas pressure at the valve inlet and manifold, and safely diagnose control board faults. If you have cleaned the flame sensor and verified the gas supply is open but the A91 code persists, a technician can retrieve detailed fault logs from the control, test ignition voltage and continuity in the flame-sense circuit, and perform a full combustion analysis to rule out venting or air-supply problems that can prevent stable flame proving. Gas appliance work requires proper permitting and inspection in most jurisdictions, and incorrect repairs can create carbon monoxide hazards or fire risk.

**Rough cost:** A pro service call runs about $150–350.
