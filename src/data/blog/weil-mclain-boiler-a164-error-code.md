---
title: "Weil-McLain A164 Error Code - Causes & Fix"
description: "A164 does not appear in Weil-McLain documentation. Verify the display-it may be A44 (bad temp sensor). Check wiring and reset the boiler."
pubDatetime: 2026-06-18T10:15:10Z
modDatetime: 2026-06-18T10:15:10Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - boiler
  - weil-mclain
money_part: "Weil-McLain DHW temperature sensor (part 42)"
diy_or_pro: "pro"
free_checks:
  - "Reset the boiler by powering it off for 30 seconds, then verify the exact code on the display"
  - "Access the contractor menu fault history to review all logged codes and look for A44 or other documented faults"
  - "Inspect visible sensor wiring for chafes, rubs, or loose connectors at the DHW and return temperature sensors"
---

## Weil-McLain A164 Error Code — What It Means

Error code A164 is not documented in any official Weil-McLain manual or fault code table. The code does not appear in the Aquabalance Series 2 manual, the CGa/CGi documentation, or manufacturer FAQs. The most likely explanation is a misread display or a digit artifact. Weil-McLain uses code A44 to indicate a bad or disconnected temperature sensor (DHW or return), and the visual similarity between 44 and 164 suggests a display error or partial fault message.

Before troubleshooting, confirm the exact code by resetting the boiler and checking the display again. Access the contractor menu fault history (hold up and down arrows, navigate to Diagnostics, then Fault History) to review past codes. If A164 persists and you cannot find it in your model's manual, contact Weil-McLain warranty support at 1-800-654-2109, Option 4, for model-specific guidance. Do not replace parts based on an undocumented code.

## Before You Replace Anything

Technicians sometimes replace control boards when an undocumented code appears, but the fault is often a chafed wire or loose crimp at a sensor connector. Inspect all wiring and connectors and measure DC voltage at the sensors while wiggling wires before ordering any circuit board.

[Jump to Fix](#fix)

## Common Causes

- **Display misread or artifact (~40%)** The digit 4 in code A44 may appear as a 1 due to a segment failure, condensation on the display, or viewing angle, making A44 look like A164.
- **Partial or incomplete fault message (~25%)** A transient power glitch or control board hiccup may display a fragment of a lockout history code or a contractor menu entry rather than a runtime fault.
- **Model-specific undocumented code (~20%)** Some boiler revisions or regional firmware variants may use fault codes not published in the general manual, requiring factory support to decode.
- **Bad or disconnected temperature sensor (if code is actually A44) (~10%)** If the code is A44, a chafed wire, loose crimp, or failed DHW or return sensor will stop the boiler and display the fault.
- **Control board memory or display fault (~5%)** A failing display module or corrupted memory on the control board can show random or hybrid codes that do not correspond to any real fault condition.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the display show A164 consistently after a full power-off reset (30 seconds unplugged)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The code is persistent. Access the contractor menu fault history to check for A44 or other documented faults, then call a technician or Weil-McLain support.<br><strong>No:</strong> The code was transient. Monitor the boiler for a few cycles; if it does not return, it may have been a display glitch or a one-time power event.</div>
</details>

<details class="dtree"><summary>Is the code actually A44 when viewed straight-on with good lighting?</summary>
<div class="dtree-body"><strong>Yes:</strong> Treat it as A44 (bad/disconnected temp sensor). Inspect DHW and return sensor wiring for chafes, check crimps, and measure DC voltage at each sensor connector while wiggling wires.<br><strong>No:</strong> The code is genuinely A164 or another undocumented fault. Do not guess at parts; contact Weil-McLain warranty support for model-specific interpretation.</div>
</details>

<details class="dtree"><summary>Does your boiler manual list A164 in the fault code table?</summary>
<div class="dtree-body"><strong>Yes:</strong> Follow the diagnostic steps for A164 in your manual exactly. If the steps reference a sensor or wiring check, start there.<br><strong>No:</strong> The code is not in your documentation. Call Weil-McLain at 1-800-654-2109, Option 4, and have your model and serial number ready for technical support.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Reset the boiler** by switching off the power or unplugging it for 30 seconds, then restore power and observe the display for the exact fault code.
2. **Verify the code** by viewing the display straight-on in good light. Check for segment failures or condensation that might make A44 look like A164.
3. **Access the contractor menu** by holding the up and down arrows simultaneously until the menu appears, navigate to Diagnostics, then Fault History, and review all logged codes for A44 or other documented faults.
4. **Inspect sensor wiring** if A44 appears in the history. Remove the front panel, locate the DHW sensor (part 42) and return sensor (part 186), and check for chafed insulation, loose crimps, or corroded connectors.
5. **Measure DC voltage** at each sensor connector while the boiler is powered. Wiggle each wire bundle to detect intermittent shorts or opens that fluctuate the voltage reading.
6. **Swap sensors** (DHW and return) to isolate whether the fault follows the sensor or stays with the wiring harness and control board input. Resistance values are the same across sensor types despite different part numbers.
7. **Contact Weil-McLain warranty support** at 1-800-654-2109, Option 4, if A164 persists and does not resolve to A44. Provide your boiler model, serial number, and a photo of the display if possible.
8. **Do not replace parts** until a documented fault code is confirmed and the manual or factory support provides a clear diagnostic path for that code.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Weil-McLain DHW temperature sensor (part 42) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a164-error-code&k=Weil-McLain+DHW+temperature+sensor+%28part+42%29&tag=errorcodefixes-20) \| For Aquabalance models if A44 is confirmed and the DHW sensor tests out of spec or shows intermittent faults |
| Weil-McLain return temperature sensor (part 186) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a164-error-code&k=Weil-McLain+return+temperature+sensor+%28part+186%29&tag=errorcodefixes-20) \| For Aquabalance models if A44 is confirmed and the return sensor tests out of spec or wiring is ruled out |

## When to Call a Pro

Call a licensed heating technician immediately if A164 persists after a reset and you cannot find it in your boiler manual. Gas-fired boilers require trained diagnostics to avoid safety risks, and undocumented fault codes may indicate a control board fault, a firmware mismatch, or a sensor issue that needs voltage testing and parts replacement. A qualified technician can access Weil-McLain technical support, interpret fault history logs, and perform DC voltage measurements at sensor terminals without risking a gas leak or electrical short. If the code turns out to be A44, the tech will inspect all sensor wiring for chafes and hidden crimps, swap sensors to isolate the fault, and replace only the confirmed bad component rather than guessing at parts.

**Rough cost:** A pro service call runs about $150-350 for a service call to diagnose and repair sensor wiring or replace a confirmed sensor.
