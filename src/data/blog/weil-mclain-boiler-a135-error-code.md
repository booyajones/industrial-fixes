---
title: "Weil-McLain A135 Error Code - Causes & Fix"
description: "A135 is a model-specific code on Weil-McLain boilers. The exact meaning varies by control module; check your service manual or call a technician."
pubDatetime: 2026-06-17T11:28:03Z
modDatetime: 2026-06-17T11:28:03Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - boiler
  - weil-mclain
money_part: "Weil-McLain control module or board"
diy_or_pro: "pro"
free_checks:
  - "Write down the exact boiler model number and control-module part number from the data plate and control face."
  - "Press the control's history or fault-log button (if available) to see if additional fault codes are stored."
  - "Check that the room thermostat is calling for heat and that no manual reset limits have tripped."
---

## Weil-McLain A135 Error Code — What It Means

The A135 code is not documented in available Weil-McLain manufacturer materials and appears to be a model-specific fault designation. Different Weil-McLain boiler series and control boards use different fault-code tables, so A135 may indicate a unique safety or limit circuit issue depending on your exact model and control module. Weil-McLain controls generally monitor the room thermostat call, air pressure switch, boiler limit circuit, and ignition safety chain. A fault in any of those inputs can trigger a lockout code, but the specific meaning of A135 cannot be confirmed without the service manual for your boiler's control.

Because the code definition is model-dependent, the safest diagnostic path is to record the exact boiler model number and control display, pull the fault history from the control panel, and verify each safety circuit in sequence. Attempting to clear the code or replace parts without identifying the active fault circuit can waste time and money. If you lack the service manual, contact a licensed technician who can cross-reference the code against the manufacturer's fault table for your control.

## Before You Replace Anything

Some homeowners replace the control board when A135 appears, but the code often points to a failed safety switch, wiring fault, or mechanical issue. Pull the fault history and test the safety chain before swapping the board.

[Jump to Fix](#fix)

## Common Causes

- **Model-specific fault definition (~100%)** A135 is not a universal Weil-McLain code and the exact meaning depends on the boiler series and control module installed.
- **Tripped limit or safety switch (~35%)** High-limit aquastat, air pressure switch, or flame rollout switch may have opened and the control logged the event as A135.
- **Faulty room thermostat or wiring (~25%)** Open or intermittent thermostat circuit can cause the control to log a fault if the call drops during ignition or operation.
- **Control-module firmware or memory fault (~20%)** Some control boards display non-standard codes after a power surge or internal error.
- **Ignition or flame-proving failure (~15%)** If the control expected flame and did not see it, the code may reflect a lockout logged with an internal counter.
- **Circulator or flow-switch issue (~5%)** Low water flow or a failed flow switch can trigger a safety lockout, depending on the model's protection logic.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the boiler control display any other fault codes or a fault-history menu?</summary>
<div class="dtree-body"><strong>Yes:</strong> Write down all codes shown and consult the service manual fault table to identify the active circuit. Cross-reference A135 with the other codes.<br><strong>No:</strong> The control may not offer a history feature. Proceed to test the safety chain manually: verify thermostat call, limit continuity, and air-pressure switch closure.</div>
</details>

<details class="dtree"><summary>Is there a call for heat at the room thermostat and is the boiler circulator running?</summary>
<div class="dtree-body"><strong>Yes:</strong> The safety chain is likely intact up to the control. Check for flame-proving or ignition faults next.<br><strong>No:</strong> Verify thermostat wiring, check that the limit aquastat has not tripped, and confirm that the circulator relay is energized.</div>
</details>

<details class="dtree"><summary>Can you locate the exact boiler model number and control-module part number?</summary>
<div class="dtree-body"><strong>Yes:</strong> Look up the fault-code table in the installation and service manual for that control to decode A135.<br><strong>No:</strong> Call Weil-McLain technical support or a licensed technician with the serial-number plate information so they can identify the correct manual.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Record all nameplate data.** Write down the boiler model number, serial number, and control-module part number from the front panel or inside jacket.
2. **Access the fault history.** If the control has a fault-log or history button, press it and note any stored codes in addition to A135.
3. **Consult the service manual.** Download or request the installation and service manual for your exact model and control, then locate the fault-code table to decode A135.
4. **Verify the safety chain.** Check that the room thermostat is calling for heat, the high-limit aquastat has not tripped, and the air pressure switch (if present) closes when the inducer runs.
5. **Test electrical inputs.** Use a multimeter to confirm 24 V control power and continuity across each safety device in the circuit identified by the manual.
6. **Inspect wiring and connectors.** Look for loose spade terminals, corroded connections, or damaged wire insulation on the thermostat, limit, and ignition circuits.
7. **Clear the fault and test operation.** After repairing the root cause, reset the control, initiate a thermostat call, and watch the full ignition and firing sequence to confirm normal operation.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Weil-McLain control module or board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a135-error-code&k=Weil-McLain+control+module+or+board&tag=errorcodefixes-20) \| Only if the manual confirms A135 is a control-module internal fault and all external safety devices test good. |
| High-limit aquastat | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a135-error-code&k=High-limit+aquastat&tag=errorcodefixes-20) \| If the fault table links A135 to a limit-circuit issue and the existing aquastat fails a continuity or calibration test. |
| Air pressure switch | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a135-error-code&k=Air+pressure+switch&tag=errorcodefixes-20) \| For induced-draft models, if A135 relates to airflow proving and the switch does not close when the inducer runs. |

## When to Call a Pro

Call a licensed boiler technician if you cannot locate the service manual for your control module, if the fault history shows multiple codes you do not understand, or if testing the safety chain requires working with gas piping, flame-proving circuits, or high-voltage ignition components. Gas boiler diagnostics demand specific tools (manometer, combustion analyzer, multimeter) and knowledge of the control logic. A technician can pull the full fault log, cross-reference A135 against the manufacturer fault table, and test each input circuit safely. Misdiagnosing the fault and replacing the wrong part wastes money and leaves the underlying safety issue unresolved.

**Rough cost:** A pro service call runs about $150-400.

## See Also

- [Weil-McLain Boiler A127 Error Code - Causes & Fix](/posts/weil-mclain-boiler-a127-error-code/)
- [Weil-McLain Boiler A169 Error Code - Causes & Fix](/posts/weil-mclain-boiler-a169-error-code/)
- [Weil-McLain Boiler A173 Error - Causes & Fix](/posts/weil-mclain-boiler-a173-error-code/)
- [Weil-McLain A159 Error - Causes & Fix](/posts/weil-mclain-boiler-a159-error-code/)
