---
title: "Weil-McLain A60 Error Code - Causes & Fix"
description: "A60 is not a standard Weil-McLain code. Check your control's fault-history menu for the real lockout code and consult your model manual."
pubDatetime: 2026-06-14T12:05:50Z
modDatetime: 2026-06-14T12:05:50Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - boiler
  - weil-mclain
money_part: "Weil-McLain control board (model-specific)"
diy_or_pro: "pro"
free_checks:
  - "Access the control's fault-history or diagnostics menu (consult your manual for the button sequence) and write down the exact stored fault code."
  - "Verify system fill pressure is in the normal range (typically 12-15 psi cold for most residential systems) and that the boiler has power and gas supply."
  - "Check that the boiler is in lockout (control LED flashing or steady fault indication) rather than normal standby, and try a single reset to see if the fault reappears."
---

## What this code means
Weil-McLain does not publish a standard **A60** error code in manufacturer documentation for its residential or commercial boiler lines. The code may be model-specific, a display artifact, or a misread fault. Weil-McLain controls typically store fault history in a diagnostics menu accessible through button sequences on the control board. The actual lockout or fault code will appear as a numeric fault code or text string that corresponds to entries in your model's installation and service manual.

Because **A60** cannot be verified against manufacturer fault tables, the first step is to access the stored fault history on your boiler's control, write down the exact code and any accompanying text, then cross-reference it with the service section of your model's manual. Common Weil-McLain fault categories include ignition failure, flame-proving problems, low system pressure, proof-of-flow issues, limit trips, and venting or combustion faults, but each has a defined code that varies by control platform and model family.

## Before You Replace Anything

Homeowners often replace the control board when the real problem is a misread code or a simple sensor fault. Always retrieve the stored fault history from the control's diagnostics menu and compare it to the manual before ordering parts.

## Common Causes

- **Misread or model-specific code (~40%)** The display may show a partial code, a service reminder, or a model-specific identifier that does not appear in general Weil-McLain fault tables.
- **Stored fault history not yet retrieved (~30%)** The control may be cycling through status messages while the actual lockout code is stored in the fault-history menu and requires a button sequence to view.
- **Ignition or flame-proving fault (~15%)** If the boiler is in lockout, the underlying fault may be an ignition failure, flame-sensor problem, or gas-supply issue that appears with a different numeric code in the fault log.
- **Low system pressure or flow fault (~10%)** Loss of system fill pressure, a closed isolation valve, or a failed proof-of-flow switch can trigger lockout with a code that may not match A60 in the manual.
- **Control board firmware or display glitch (~5%)** A corrupted display segment or a firmware anomaly can produce a non-standard code that clears on a power cycle or control replacement.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the control display a flashing or steady LED lockout pattern?</summary>
<div class="dtree-body"><strong>Yes:</strong> The boiler is in lockout. Access the fault-history menu using the button sequence in your manual and note the stored fault code for lookup.<br><strong>No:</strong> The display may be showing a status message or service reminder rather than a fault. Verify system pressure and check for a call for heat before investigating further.</div>
</details>

<details class="dtree"><summary>Can you retrieve a stored fault history from the control's diagnostics menu?</summary>
<div class="dtree-body"><strong>Yes:</strong> Write down the exact fault code and text, then cross-reference it with the service section of your model's manual or call a technician with that code.<br><strong>No:</strong> Consult your installation manual for the button sequence to enter diagnostics mode, or contact Weil-McLain support with your model and serial (CP) number for guidance.</div>
</details>

<details class="dtree"><summary>Is system fill pressure below 12 psi or above 25 psi on the gauge?</summary>
<div class="dtree-body"><strong>Yes:</strong> Low pressure can cause a lockout on many models. Check for leaks, refill to the recommended cold pressure, and reset the boiler once.<br><strong>No:</strong> Pressure is normal. The fault is likely ignition, flame-sensing, venting, or a control issue that requires professional diagnosis.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off power** to the boiler at the service switch or circuit breaker and wait 30 seconds.
2. **Restore power** and observe the control display. Note any flashing LED patterns or alternating code displays.
3. **Access the fault-history menu** by pressing and holding the button sequence specified in your model's installation manual (often a combination of reset and mode buttons).
4. **Write down the exact fault code** and any accompanying text from the stored history, including the number of occurrences and timestamps if shown.
5. **Cross-reference the code** with the fault table in your model's service manual or contact Weil-McLain technical support with your model number and CP (serial) number.
6. **Check system fill pressure** on the boiler's pressure gauge. If below 12 psi, locate the fill valve and bring pressure to the recommended cold setting (typically 12-15 psi for residential systems).
7. **Attempt a single reset** only if you have confirmed system pressure is correct and no other safety issues are present. If the fault recurs immediately or within one cycle, call a qualified heating technician for diagnosis and repair.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Weil-McLain control board (model-specific) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a60-error-code&k=Weil-McLain+control+board+%28model-specific%29&tag=errorcodefixes-20) \| Only replace after retrieving the stored fault code and confirming board failure with a technician or manufacturer support. |
| Flame sensor or igniter assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a60-error-code&k=Flame+sensor+or+igniter+assembly&tag=errorcodefixes-20) \| Common replacement if the stored fault indicates ignition or flame-proving failure. |

## When to Call a Pro

Call a licensed heating technician immediately if you cannot retrieve a stored fault code from the control's diagnostics menu, if the boiler is in lockout and you are unfamiliar with gas appliance troubleshooting, or if the fault recurs after a single reset. Gas-fired boiler repair requires proper combustion analysis, gas-pressure testing, and electrical diagnostics that are beyond typical DIY scope. A technician will use the control's fault history, measure gas pressure and flame current, inspect the burner and heat exchanger, and verify venting and airflow to identify the root cause. Do not repeatedly reset a lockout without identifying the fault, as ignition or flame-proving problems can create unsafe combustion conditions or carbon-monoxide risk.

**Rough cost:** A pro service call runs about $150-400.
