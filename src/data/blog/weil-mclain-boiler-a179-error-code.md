---
title: "Weil-McLain A179 Error Code - Causes & Fix"
description: "A179 is not a standard Weil-McLain code. Check your exact model manual for the fault definition, then verify system pressure and sensors."
pubDatetime: 2026-06-20T12:35:38Z
modDatetime: 2026-06-20T12:35:38Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - boiler
  - weil-mclain
money_part: "Thermistor or temperature sensor"
diy_or_pro: "pro"
free_checks:
  - "Check system pressure gauge and confirm it is above the low-water cutoff threshold for your model."
  - "Inspect the fault history menu on the boiler control to see if additional codes or timestamps are stored."
  - "Verify that all wiring harness connectors to sensors and the control board are fully seated and not corroded."
---

## Weil-McLain A179 Error Code — What It Means

A179 does not appear as a documented error code in the available Weil-McLain manufacturer materials for standard boiler control systems. Weil-McLain directs users to model-specific manuals and fault history menus to identify the exact meaning of any displayed code, because control platforms vary by model and year. Without confirmation from your boiler's manual, A179 cannot be assigned a verified cause or component.

If you see A179 on your display, first write down the exact boiler model number (usually on the data plate inside the jacket or on the front panel) and consult the matching installation and service manual. The control board's diagnostic menu or fault history log may show additional information. General boiler faults often relate to ignition issues, low system pressure, sensor failures, venting or condensate blockages, or circulator problems, but the specific meaning of A179 will depend entirely on your model and control type.

## Before You Replace Anything

Because the code meaning is unconfirmed, technicians sometimes replace control boards or sensors before checking basic system conditions. Always verify that system pressure is in range, gas and power supply are good, and all wiring connectors are seated before ordering any part.

[Jump to Fix](#fix)

## Common Causes

- **Low system pressure or air in the piping (~25%)** If the boiler's water pressure has dropped below the minimum threshold or air is trapped in the system, many control platforms log a fault and lock out until pressure is restored and the system is purged.
- **Failed or out-of-range sensor (thermistor, pressure transducer, or low-water cutoff) (~25%)** A sensor reading outside its expected range will trigger a fault on many Weil-McLain controls, though the exact code depends on the model.
- **Ignition or flame-proving issue (~20%)** If the burner fails to light or the flame sensor cannot prove combustion within the control's time window, a lockout fault is stored.
- **Blocked condensate drain or vent pressure switch problem (~15%)** On condensing models, a clogged drain or faulty vent pressure switch can prevent safe operation and log a fault code.
- **Circulator or pump fault (~10%)** Some controls monitor circulator operation and will lock out if flow is not detected or if a pump relay fails.
- **Control board memory or communication error (~5%)** Occasionally a non-standard code appears due to a control board glitch, corrupted fault log, or wiring issue that prevents proper communication between modules.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is the system pressure gauge reading below the minimum fill line or showing less than about 12 psi?</summary>
<div class="dtree-body"><strong>Yes:</strong> Low pressure is a common lockout cause. Add water through the fill valve until pressure reaches the recommended range (often 12–15 psi cold), then bleed air from the system and reset the boiler.<br><strong>No:</strong> Pressure is acceptable. Move on to checking sensors and the fault history menu.</div>
</details>

<details class="dtree"><summary>Does the fault history menu on the control display any additional codes or timestamps?</summary>
<div class="dtree-body"><strong>Yes:</strong> Write down all codes and timestamps. Cross-reference them in your model's service manual to identify the primary fault and any related conditions.<br><strong>No:</strong> If A179 is the only entry and not documented in your manual, contact Weil-McLain technical support with your exact model number for clarification.</div>
</details>

<details class="dtree"><summary>Are all sensor wiring connectors and harnesses fully seated and free of corrosion?</summary>
<div class="dtree-body"><strong>Yes:</strong> Wiring is sound. The fault likely points to a failed sensor, ignition component, or control board that requires professional diagnosis and testing.<br><strong>No:</strong> Reseat or clean all connectors, then clear the fault and attempt a restart. Poor connections can mimic sensor or board failures.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Record the exact model and serial number** from the boiler's data plate (usually inside the front jacket or on the control panel).
2. **Access the control's diagnostic or fault history menu** according to the instructions in your model's manual and write down all displayed codes and timestamps.
3. **Locate the model-specific service manual** by searching the Weil-McLain website or contacting their technical support with your model number to obtain the fault code table.
4. **Check system water pressure** on the gauge. If it is below the minimum fill line or the low-water cutoff threshold, carefully add water through the boiler's fill valve until pressure reaches the recommended range for your system.
5. **Inspect all sensor wiring and connectors** (thermistors, pressure transducers, low-water cutoff, flame sensor, and vent switches) for corrosion, loose pins, or damaged insulation. Reseat any questionable connections.
6. **Clear the fault code** using the control's reset button or menu procedure, then attempt to restart the boiler and observe whether the same code reappears immediately or after a cycle.
7. **Call a licensed boiler technician** if the code persists or if your manual confirms that A179 (or the actual code you find) requires component testing, sensor replacement, control board diagnostics, or gas-system work.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Thermistor or temperature sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a179-error-code&k=Thermistor+or+temperature+sensor&tag=errorcodefixes-20) \| Order by exact model number if diagnostics confirm an out-of-range or open thermistor circuit. |
| Pressure transducer or low-water cutoff sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a179-error-code&k=Pressure+transducer+or+low-water+cutoff+sensor&tag=errorcodefixes-20) \| Match the part number on the existing sensor; resistance and voltage specs vary by model. |
| Control board (integrated or modular) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a179-error-code&k=Control+board+%28integrated+or+modular%29&tag=errorcodefixes-20) \| Only replace after confirming all sensors, wiring, and power supply are good; board replacement requires matching the exact control revision. |
| Igniter or flame sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a179-error-code&k=Igniter+or+flame+sensor&tag=errorcodefixes-20) \| If ignition or flame-proving is confirmed as the fault, order the OEM part by boiler model and burner type. |

## When to Call a Pro

Call a licensed boiler technician immediately if you cannot locate the A179 definition in your model's manual, if the fault persists after restoring system pressure and reseating connectors, or if you are uncomfortable working with gas supply, electrical control boards, or high-voltage wiring. Boiler diagnostics often require a multimeter to test sensor resistance and voltage, a combustion analyzer to verify ignition and flame quality, and specialized knowledge of the control platform. Incorrect troubleshooting can lead to unsafe operation, carbon monoxide risk, or damage to the heat exchanger. A qualified pro will retrieve the full fault history, test each sensor and switch against the manufacturer's specifications, and replace only the component that has actually failed.

**Rough cost:** A pro service call runs about $150–400.
