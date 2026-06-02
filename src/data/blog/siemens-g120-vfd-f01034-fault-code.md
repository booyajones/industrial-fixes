---
title: "Siemens G120 F01034 - Causes & Fix"
description: "F01034 means parameter recalculation failed after a reference value change. Most likely fix: correct incompatible parameters or clear buffer memory."
pubDatetime: 2026-05-31T11:17:15Z
modDatetime: 2026-05-31T11:17:15Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - siemens
---

## Siemens G120 F01034 — What It Means

F01034 on a Siemens SINAMICS G120 is a parameterization fault, not a hardware failure. The official fault text is 'Units changeover: Calculation parameter values after reference value change unsuccessful.' This means the drive tried to recalculate dependent parameters after you (or a fieldbus) changed a reference or scaling parameter, but the new values were incompatible or out of range, so the drive rejected the change and restored the previous value. The reaction is listed as NONE and acknowledgment is IMMEDIATELY, which tells you the drive treats this as a parameter-setting error rather than a trip requiring shutdown. Siemens internal notes mark this fault value as 'Only for internal Siemens troubleshooting,' meaning it is resolved by fixing parameter logic, not by replacing power components.

[Jump to Fix](#fix)

## Common Causes

- **Incompatible reference or scaling parameter change** A reference value was changed while other dependent parameters remained out of range or inconsistent with the new scaling.
- **Buffer memory active during repeated parameter writes** Buffer memory was enabled (p0014 = 1) and parameters were changed repeatedly via fieldbus, causing recalculation conflicts.
- **Transfer or scaling value outside valid range** A transfer value or scaling value was outside what the drive could convert correctly after the reference change.
- **Parameter set corrupted or incomplete** The parameter set became inconsistent after partial writes or interrupted configuration, leaving dependent values invalid.
- **Fieldbus communication writing conflicting values** A PROFINET, PROFIBUS, or USS fieldbus wrote parameters that could not coexist with the current reference settings.
- **Control Unit parameter memory issue** The Control Unit could not store or recalculate the parameter change due to internal memory or processing fault.

## Step-by-Step Fix {#fix}

1. **Read the fault buffer** using the BOP or STARTER software to identify which reference or scaling parameter change triggered F01034 and note the parameter number and value.
2. **Review the changed parameters** and any dependent parameters in the drive's parameter list, then restore values to a consistent set that matches the reference scaling.
3. **Check if buffer memory is active** by reading p0014, and if it is set to 1, deactivate and clear buffer memory by setting p0014 = 0 or clear it with p0014 = 2.
4. **Transfer buffer entries to ROM** if the buffer is normally used by setting p0971 = 1, which clears the buffer and saves the entries permanently.
5. **Power down the Control Unit** completely, wait 10 seconds, then power back up and re-check the parameterization to confirm the fault is cleared.
6. **Verify fieldbus communication** if parameters are written over PROFINET, PROFIBUS, or USS, and confirm that no conflicting writes are occurring during operation.
7. **Replace the Control Unit** if the fault persists after correcting all parameters and performing a full power cycle, as Siemens internal notes list Control Unit replacement as the final corrective measure.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens G120 Control Unit (CU) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f01034-fault-code&k=Siemens+G120+Control+Unit+%28CU%29&tag=errorcodefixes-20) \| Required only if fault persists after parameter correction and power cycling, consult your drive model for exact CU variant. |
| STARTER commissioning software license | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f01034-fault-code&k=STARTER+commissioning+software+license&tag=errorcodefixes-20) \| Helpful for detailed parameter diagnosis and buffer memory management if BOP is insufficient. |

## When to Call a Pro

Call a qualified drives technician or Siemens-certified service partner if you are not comfortable reading the fault buffer, interpreting parameter dependencies, or using STARTER software to diagnose the exact parameter conflict. Also call if the fault returns after you have corrected all parameters and completed a full power cycle, as this may indicate a Control Unit memory fault requiring replacement. If your system uses complex fieldbus communication (PROFINET, PROFIBUS, or USS) and the fault occurs during automated parameter writes, professional commissioning support is recommended to verify bus configuration and parameter logic.
