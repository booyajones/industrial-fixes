---
title: "Carrier Error Code 17 - Causes & Fix"
description: "Carrier error code 17 often means VFD System Fault - High Line Voltage on inverter models. Learn causes, diagnostic steps, and repair."
pubDatetime: 2026-05-25T00:04:44Z
modDatetime: 2026-05-25T00:04:44Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - hvac
  - carrier
money_part: "VFD inverter module"
---

## Carrier Error Code 17 — What It Means

Carrier error code 17 is not universal across all Carrier equipment. On many inverter and variable-speed models, particularly the 24VNA6 and 25VNA4 families, code 17 appears as fault 82-17: VFD System Fault - High Line Voltage. The variable frequency drive monitors incoming line voltage and trips this fault when it detects voltage above the acceptable range. The exact meaning of code 17 depends on your model family and control platform, so always confirm the fault definition in your specific service manual before starting repairs.

On inverter-equipped units, this fault protects the VFD power electronics from damage due to overvoltage conditions. The drive shuts down the compressor and logs the fault. In the field, the root cause is usually a supply voltage problem or a wiring issue, though failed inverter components can also trigger the fault even when line voltage is normal.

[Jump to Fix](#fix)

## Common Causes

- **High incoming line voltage** Supply voltage at the disconnect exceeds the VFD's upper tolerance, triggering the high-voltage lockout.
- **Loose or corroded line-voltage connections** Poor contact at lugs, the disconnect, or line-side connectors creates intermittent voltage spikes or measurement errors.
- **Failed VFD or inverter module** Internal faults in the drive's power stage or voltage-sensing circuit cause false high-voltage readings or actual overvoltage events.
- **Outdoor control board fault** The main board that communicates with the VFD may send incorrect signals or fail to regulate voltage sensing correctly.
- **High ambient temperature affecting inverter** Excessive heat around the outdoor unit can stress inverter components and contribute to voltage-related faults.

## Step-by-Step Fix {#fix}

1. **Verify the exact fault code** by checking your model number and service manual, because Carrier uses code 17 differently across product lines.
2. **Measure incoming line voltage** at the unit disconnect with a multimeter while the fault is present or just after it occurs, and compare to the voltage range in your model's installation manual.
3. **Inspect all line-voltage wiring** including lugs at the disconnect, the outdoor unit's terminal block, and every connector between the power supply and the VFD for tightness, corrosion, and damage.
4. **Check for proper wire gauge and routing** to rule out voltage drop or interference, and confirm that the disconnect and circuit breaker match the unit's electrical specifications.
5. **Clear the fault** using the thermostat or control interface, then monitor the unit through a full cooling cycle to see if the fault returns.
6. **Test the VFD and outdoor board** if line voltage is within spec and wiring is sound, using a multimeter and the service manual's diagnostic flowchart to isolate the failed component.
7. **Replace the faulty component** (VFD module or outdoor control board) with the correct part number for your model, then retest and log the repair.

## Parts Often Needed

| Part | Notes |
|------|-------|
| VFD inverter module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-carrier-error-code-17&k=VFD+inverter+module&tag=errorcodefixes-20) \| Model-specific drive assembly, consult your service manual for the exact part number. |
| Outdoor control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-carrier-error-code-17&k=Outdoor+control+board&tag=errorcodefixes-20) \| Main board that interfaces with the VFD, replace only if diagnostics confirm board-level fault. |
| Line-voltage wiring harness or connectors | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-carrier-error-code-17&k=Line-voltage+wiring+harness+or+connectors&tag=errorcodefixes-20) \| Use only if inspection reveals damaged or melted wiring between disconnect and VFD. |

## When to Call a Pro

Call a licensed HVAC technician if you are not comfortable working with line voltage, if you lack a multimeter and the service manual for your exact model, or if the fault returns after you have verified correct supply voltage and repaired all wiring issues. VFD and inverter diagnostics require specialized knowledge and tools. Misdiagnosis can lead to expensive part replacements that do not solve the problem, and live electrical work carries serious shock and arc-flash hazards.

## See Also

- [Carrier 32 Error Code — Causes & Fix](/posts/carrier-32-error-code/)
- [Carrier 33 Error Code — Causes & Fix](/posts/carrier-33-error-code/)
- [Carrier Zone Controller Error Codes — Complete Guide](/posts/carrier-zone-controller-error-codes/)
- [Carrier Heat Pump E4 Error Code — Causes & Fix](/posts/carrier-heat-pump-e4-error-code/)
