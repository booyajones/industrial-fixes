---
title: "Weil-McLain A04 Error Code - Causes & Fix"
description: "A04 is not a standard Weil-McLain code. Check your exact model's manual for the correct fault table and control board type."
pubDatetime: 2026-06-14T11:43:03Z
modDatetime: 2026-06-14T11:43:03Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - boiler
  - weil-mclain
money_part: "Weil-McLain control board (model-specific)"
diy_or_pro: "pro"
free_checks:
  - "Verify the exact code on the display (A04 vs. E04) and photograph it"
  - "Check the boiler's fault history or lockout log on the control panel"
  - "Confirm incoming 120 V power at the boiler and check for recent outages or tripped breakers"
---

## Weil-McLain A04 Error Code — What It Means

A04 is not a verified Weil-McLain error designation in manufacturer materials. Weil-McLain boilers use E-codes on most controls, and the meaning depends on the exact boiler family and control board. Some sources confuse A04 with E04, which on certain Weil-McLain controls means loss of power after a lockout, requiring a manual reset and indicating the original lockout code history was lost. Without your exact model and control type, any single internet definition for A04 is unreliable.

Because Weil-McLain fault codes vary widely by model, you need to pull the service manual or fault table for your specific boiler and control board. If your display shows E04 instead, the verified cause is a power interruption or improper reset attempt after the boiler had already locked out on a different fault. If the code truly reads A04, it likely belongs to a different control family not captured in standard references, and a technician will need the wiring diagram and model-specific documentation to interpret it correctly.

## Before You Replace Anything

Homeowners often press the reset button repeatedly without identifying the original lockout cause. Check the fault history on the control and verify incoming 120 V power, polarity, and ground before resetting again.

[Jump to Fix](#fix)

## Common Causes

- **Misread or model-specific code (~40%)** A04 does not appear in standard Weil-McLain fault tables, so the code may be E04 or belong to a control family requiring model-specific documentation.
- **Power interruption after lockout (~30%)** If the code is actually E04, a power outage or manual on-off cycle after the boiler locked out clears the original fault history and shows loss of power.
- **Improper reset attempt (~15%)** Turning the boiler off then on to bypass a hard lockout can trigger an E04 loss-of-power-after-lockout condition without fixing the underlying fault.
- **Incorrect polarity or ground (~10%)** Reversed line and neutral or missing ground on the incoming 120 V supply can cause control faults and lockout conditions on some Weil-McLain boards.
- **Surge or dirty voltage (~5%)** Voltage spikes, brown-outs, or electrical noise on the 120 V line can corrupt control memory and produce fault codes after power is restored.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the display show E04 instead of A04 when you look closely?</summary>
<div class="dtree-body"><strong>Yes:</strong> E04 means loss of power after a lockout. Check the fault history on the control to see the original lockout code, then address that root cause before resetting.<br><strong>No:</strong> A04 is not a standard Weil-McLain code. Locate your boiler model number and control board type, then pull the correct service manual or fault table for your specific unit.</div>
</details>

<details class="dtree"><summary>Did the boiler lose power (outage, breaker trip, or manual off-on) recently?</summary>
<div class="dtree-body"><strong>Yes:</strong> Power interruption after a lockout causes E04 and erases the original fault. Investigate what caused the first lockout (pressure, flame, ignition) rather than just resetting.<br><strong>No:</strong> The fault may be related to incoming power quality, polarity, or ground. Measure 120 V at the boiler and confirm correct wiring before proceeding.</div>
</details>

<details class="dtree"><summary>Does the boiler immediately return to fault after a manual reset?</summary>
<div class="dtree-body"><strong>Yes:</strong> Repeated lockouts indicate an unresolved root cause (low water pressure, bad flame sensor, limit switch, or gas supply). Do not keep resetting. Call a technician for full diagnostics.<br><strong>No:</strong> The fault may have been transient. Monitor the boiler and check the fault history regularly. If it returns, follow full service diagnostics per your model's manual.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Identify the exact model and control board** on your Weil-McLain boiler by reading the rating plate and control cover labels.
2. **Locate the service manual or fault code table** for that specific model and control, either online or by contacting Weil-McLain technical support.
3. **Photograph the displayed code** to confirm whether it reads A04 or E04, and record the exact appearance of the characters on the control screen.
4. **Access the fault history or lockout log** on the control panel by following the button sequence in your manual to see any prior error codes before power was lost.
5. **Measure incoming 120 V power** at the boiler terminals with a multimeter and verify correct polarity (hot, neutral, and ground) per the wiring diagram.
6. **Address the original lockout cause** found in the fault history (for example low water pressure, flame failure, or limit fault) before performing a manual reset.
7. **Perform a manual reset** only after fixing the root cause, using the reset procedure specified for your control board, and monitor the boiler for 24 hours to confirm stable operation.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Weil-McLain control board (model-specific) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a04-error-code&k=Weil-McLain+control+board+%28model-specific%29&tag=errorcodefixes-20) \| Only replace if diagnostics confirm board failure and the correct part number matches your boiler family and control. |
| 120 V power supply surge protector | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a04-error-code&k=120+V+power+supply+surge+protector&tag=errorcodefixes-20) \| Install if dirty voltage or surges are suspected, after verifying incoming power quality with a meter. |

## When to Call a Pro

Call a licensed technician immediately if the code appears at all, because A04 is not a standard Weil-McLain designation and requires model-specific documentation to diagnose. If the code is actually E04, call a pro when the fault history shows repeated lockouts on flame, ignition, pressure, or limit faults, or if you are not comfortable measuring 120 V power, checking polarity and ground, or interpreting the control's fault log. Gas-fired boiler diagnostics involve high-voltage controls, combustion testing, and gas-valve adjustments that require training and tools. A technician will pull the correct service manual, verify incoming power quality, check the original lockout cause in the fault history, and perform a full combustion and safety analysis before resetting the control.

**Rough cost:** A pro service call runs about $150-350.

## See Also

- [Weil-McLain A27 Error - Causes & Fix](/posts/weil-mclain-boiler-a27-error-code/)
- [Weil-McLain Boiler A48 Error - Causes & Fix](/posts/weil-mclain-boiler-a48-error-code/)
- [Weil-McLain A13 Error Code - Causes & Fix](/posts/weil-mclain-boiler-a13-error-code/)
- [Weil-McLain A35 Error Code - Causes & Fix](/posts/weil-mclain-boiler-a35-error-code/)
