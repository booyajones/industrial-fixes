---
title: "Weil-McLain A116 Error Code - Causes & Fix"
description: "A116 is not a verified Weil-McLain code. Check your boiler's manual for the exact meaning, then inspect pressure, thermistor, and low-water cutoff."
pubDatetime: 2026-06-16T11:28:23Z
modDatetime: 2026-06-16T11:28:23Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - boiler
  - weil-mclain
money_part: "Thermistor / Temperature Sensor"
diy_or_pro: "pro"
free_checks:
  - "Check system pressure gauge; refill if below 12 psi and look for visible leaks"
  - "Verify power to the boiler and inspect all wire connections for looseness or corrosion"
  - "Enter the fault-history menu (per your manual) and write down all stored codes"
---

## What this code means
A116 is not a documented Weil-McLain fault code in available manufacturer materials. The exact meaning depends on your boiler series and control platform. Weil-McLain boilers store fault history and lockout codes in diagnostic menus, and each series (CGa, CGi, AquaBalance, Ultra, and others) uses its own code table. Without the specific model number and control board type, A116 cannot be reliably mapped to a single fault.

Weil-McLain lockouts commonly involve low system pressure, failed thermistors or temperature sensors, low-water cutoff faults, circulator pump problems, gas-valve issues, or ignition and flame-sensing errors. To diagnose any lockout code, enter the boiler's diagnostic menu, pull the fault history, cross-reference the code in your model's service manual, then test the suspected component with a meter before replacing parts.

## Before You Replace Anything

Technicians sometimes replace the control board when the actual fault is a failed thermistor or low-water cutoff sensor. Test sensor resistance and continuity with a multimeter before ordering any board.

## Common Causes

- **Low system pressure or water level (~30%)** Loss of pressure below the cutoff point triggers a lockout to protect the heat exchanger from overheating.
- **Failed thermistor or temperature sensor (~25%)** An out-of-range or open thermistor prevents the control from reading water temperature and forces a safety lockout.
- **Low-water cutoff sensor fault (~20%)** A stuck, fouled, or failed low-water probe signals insufficient water and stops the burner.
- **Circulator pump not running (~15%)** A seized or unpowered pump stops flow, causing the boiler to overheat and lock out on high limit.
- **Gas valve or ignition fault (~10%)** Failed igniter, flame sensor, or gas-valve coil prevents burner lighting and records a lockout code.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is the system-pressure gauge below 12 psi or in the red zone?</summary>
<div class="dtree-body"><strong>Yes:</strong> Refill the system through the fill valve and bleed radiators, then watch for recurring pressure loss that signals a leak.<br><strong>No:</strong> Pressure is adequate; move to checking sensors and circulation.</div>
</details>

<details class="dtree"><summary>Does the circulator pump hum or spin when the boiler calls for heat?</summary>
<div class="dtree-body"><strong>Yes:</strong> Circulation is working; focus on temperature sensors, low-water cutoff, and flame-sensing components.<br><strong>No:</strong> Check pump power connections and test the pump for a seized rotor or failed motor.</div>
</details>

<details class="dtree"><summary>Can you access the boiler's diagnostic menu and read the stored fault history?</summary>
<div class="dtree-body"><strong>Yes:</strong> Write down every code, match each to your model's service manual, and test the components the codes point to.<br><strong>No:</strong> Consult your owner's manual for button sequences or call a technician to pull the fault log.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Identify your boiler model and control board.** Look for the rating plate on the jacket or inside the front panel, and note the exact series (CGa, CGi, AquaBalance, Ultra, or other).
2. **Enter the diagnostic menu** using the button sequence in your owner's manual, and navigate to fault history or lockout history to retrieve all stored codes.
3. **Cross-reference every code** in your model's service manual or installation guide to determine which component each code implicates.
4. **Inspect system pressure** on the gauge; if below 12 psi, close the boiler shutoff, open the fill valve slowly until pressure reaches the recommended zone (typically 12–15 psi for residential systems), then close the valve and bleed air from radiators.
5. **Test the suspected sensor** with a digital multimeter set to resistance mode; compare the reading at room temperature to the resistance table in your service manual, and replace the sensor if it reads open, shorted, or out of range.
6. **Check circulator operation** by feeling the pump body for vibration and heat when the boiler calls for heat; if silent or cold, verify line voltage at the pump terminals and test the motor.
7. **Clear the fault and reset the boiler** after repairing the root cause, then monitor for 24 hours to confirm the code does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Thermistor / Temperature Sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a116-error-code&k=Thermistor+%2F+Temperature+Sensor&tag=errorcodefixes-20) \| Order the exact part number for your boiler series from the service manual. |
| Low-Water Cutoff Sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a116-error-code&k=Low-Water+Cutoff+Sensor&tag=errorcodefixes-20) \| Verify probe style (float, probe, or electronic) before ordering. |
| Circulator Pump | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a116-error-code&k=Circulator+Pump&tag=errorcodefixes-20) \| Match flange size, voltage, and flow rate to your original pump. |

## When to Call a Pro

Call a licensed heating technician whenever you cannot identify your boiler model, cannot access the diagnostic menu, or retrieve a code you cannot cross-reference in your manual. Gas-fired boiler work requires combustion testing, gas-pressure measurement, and venting inspection that only a qualified technician should perform. If you replace a sensor or pump and the lockout recurs, the control board or a second fault may be involved, and further diagnosis with specialized tools is needed to avoid replacing parts by trial and error.

**Rough cost:** A pro service call runs about $150–400.
