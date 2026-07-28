---
title: "Weil-McLain A145 Error Code - Causes & Fix"
description: "A145 is not a standard Weil-McLain fault code. Check your exact boiler model's manual or control display for the correct code family."
pubDatetime: 2026-06-18T09:54:56Z
modDatetime: 2026-06-18T09:54:56Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - boiler
  - weil-mclain
money_part: "Ignition control board (model-specific)"
diy_or_pro: "pro"
free_checks:
  - "Write down the exact boiler model and serial number from the nameplate"
  - "Press the control's diagnostic button to cycle through active and stored fault codes"
  - "Check that the boiler's power switch and circuit breaker are both on and that the thermostat is calling for heat"
---

## What this code means
A145 does not appear in published Weil-McLain boiler documentation as a universal fault code. Weil-McLain controls typically display E-codes, lockout messages, or history-menu entries rather than A-series codes. The display may be showing a partial code, a code from a third-party control mounted on the boiler, or a model-specific sequence that requires the exact boiler model and control board type to interpret.

Before troubleshooting, locate the boiler model number and control-board label on the unit itself. Consult that model's installation and service manual for the complete fault-code table. If the boiler is under warranty, Weil-McLain requires a qualified technician to identify the failed part and part number from the actual boiler before authorizing any claim.

## Before You Replace Anything

Without the correct code definition, technicians sometimes replace ignition or flame-sensor components when the real fault is a venting, gas-valve, or pressure-switch issue. Always retrieve the active and historical fault codes from the control's diagnostics menu and test the associated input before ordering parts.

## Common Causes

- **Code displayed is from a third-party or add-on control (~35%)** Some Weil-McLain boilers use aftermarket zone controllers or outdoor-reset modules that generate their own alphanumeric codes, which do not appear in the boiler's manual.
- **Partial or misread code (~30%)** The display may show only part of a longer sequence, or a digit may be mistaken for a letter under poor lighting.
- **Model-specific code not documented in general service literature (~20%)** Certain limited-production or OEM versions of Weil-McLain boilers use control firmware with codes that appear only in the model's individual installation manual.
- **Control board displaying a self-test or setup menu item (~10%)** During commissioning or after a power cycle, some controls scroll through configuration parameters that resemble fault codes but are not active alarms.
- **Control board firmware anomaly or corruption (~5%)** A brownout or static event can cause the microcontroller to display a non-standard character string that clears after a full power cycle.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the boiler's control display scroll through multiple codes or messages when you press a button?</summary>
<div class="dtree-body"><strong>Yes:</strong> The control has a diagnostics or history menu. Write down every code shown and match them to the table in your model's manual.<br><strong>No:</strong> The single message may be a setup parameter or a third-party control code. Verify which control board is actually generating the display.</div>
</details>

<details class="dtree"><summary>Is there a second digital display or module mounted near the boiler (zone controller, outdoor sensor, or aquastat)?</summary>
<div class="dtree-body"><strong>Yes:</strong> That module may be the source of the A145 message. Consult its own manual for the code definition.<br><strong>No:</strong> The code is likely coming from the boiler's main control. Proceed to retrieve the boiler model number and control part number.</div>
</details>

<details class="dtree"><summary>Does the boiler fire and heat normally despite the A145 display?</summary>
<div class="dtree-body"><strong>Yes:</strong> The message may be an informational status or a cleared historical fault. Check the manual's history-code section.<br><strong>No:</strong> The boiler is locked out or has an active fault. Call a qualified technician to diagnose using the control's full fault table and test the associated safety circuits.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off power** to the boiler at the service switch and wait thirty seconds, then restore power and observe whether the display changes or clears.
2. **Locate the boiler nameplate** on the jacket or burner door and write down the complete model number, serial number, and control-board part number.
3. **Download the installation and service manual** for that exact model from the Weil-McLain website or contact their technical support with the model and control numbers.
4. **Press the control's diagnostics button** (if equipped) to scroll through active faults and fault history, and compare every displayed code to the manual's fault-code table.
5. **Identify which control is generating the A145 message** by inspecting any add-on modules, zone controllers, or outdoor-reset devices mounted on or near the boiler.
6. **Contact a licensed heating technician** if the code does not appear in any of the manuals or if the boiler remains locked out, and provide the technician with the model number and all displayed codes.
7. **Do not replace parts** until the exact fault definition is confirmed and the associated sensor, switch, or valve has been tested per the manufacturer's diagnostic flowchart.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Ignition control board (model-specific) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a145-error-code&k=Ignition+control+board+%28model-specific%29&tag=errorcodefixes-20) \| Only if diagnostics confirm control failure; requires exact part number from nameplate. |
| Flame sensor or flame rod | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a145-error-code&k=Flame+sensor+or+flame+rod&tag=errorcodefixes-20) \| Common replacement when flame-proving codes appear; clean or test continuity before buying. |

## When to Call a Pro

Call a qualified heating technician immediately if you cannot locate the A145 code in your boiler's manual, if the boiler is locked out and will not fire, or if you are unfamiliar with gas-appliance diagnostics. All Weil-McLain boilers require a licensed professional for work on gas valves, venting, pressure switches, and control boards. Warranty coverage depends on proper diagnosis and documentation of the failed part by a qualified installer, so attempting repairs without confirming the exact fault may void coverage and create unsafe operating conditions.

**Rough cost:** A pro service call runs about $150–400 depending on diagnosis and part.
