---
title: "MRCOOL Mini Split EH 10 Error - Causes & Fix"
description: "EH 10 on a MRCOOL mini split typically indicates an electric heater fault. Check the auxiliary heat strip and thermal cutout first."
pubDatetime: 2026-07-09T08:28:15Z
modDatetime: 2026-07-09T08:28:15Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - mrcool
money_part: "Auxiliary heat strip"
most_likely_cause: "Tripped thermal cutout on the auxiliary heat strip"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power-cycle the system by switching off the breaker for two minutes, then restoring power to see if the fault clears."
  - "Inspect the air filter and coil for blockage that may have caused the heater to overheat and trip the safety."
---

## MRCOOL Mini Split EH 10 Error — What It Means

The EH 10 error code on MRCOOL mini split systems generally points to a problem with the electric auxiliary heating element or its safety circuitry. This code appears when the control board detects that the supplemental heat strip is not operating correctly, a thermal safety has tripped, or the circuit supplying power to the heater has failed.

Because heat-pump mini splits rely on auxiliary electric heat during very cold weather or defrost cycles, a fault in this system will prevent the unit from maintaining temperature in heating mode. The exact meaning can vary slightly by model, so consult your owner's manual or the wiring diagram on the air handler to confirm the specific fault condition.

## Before You Replace Anything

Many technicians replace the heat strip itself when the real issue is a tripped thermal safety or a blown fuse in the low-voltage control circuit. Test continuity across the thermal cutout and check for 24 V at the heat relay before ordering a heater element.

[Jump to Fix](#fix)

## Common Causes

- **Tripped thermal cutout (~40%)** The safety switch on the heat strip opens when airflow is restricted or the element overheats, and it may not auto-reset.
- **Failed auxiliary heat strip (~25%)** The resistance element itself burns out or develops an open circuit, preventing current flow.
- **Low-voltage control relay failure (~15%)** The relay or contactor that energizes the heat strip fails to close, so no power reaches the element.
- **Blown fuse on the control board (~10%)** A fuse protecting the auxiliary heat circuit opens due to a short or overload, cutting power to the heater.
- **Loose or corroded wiring (~10%)** Connections to the heat strip or thermal safety become oxidized or vibrate loose, breaking the circuit.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the outdoor unit run and provide cooling, but heating fails?</summary>
<div class="dtree-body"><strong>Yes:</strong> The compressor and reversing valve are working, so the fault is isolated to the auxiliary heat circuit. Focus on the heat strip, thermal cutout, and control relay.<br><strong>No:</strong> The problem may be upstream in the power supply or main control board. Check that both indoor and outdoor units receive power and that the thermostat is calling for heat.</div>
</details>

<details class="dtree"><summary>Is the air filter clean and airflow from the indoor unit strong?</summary>
<div class="dtree-body"><strong>Yes:</strong> Airflow is adequate, so the thermal cutout likely tripped due to an electrical fault rather than overheating. Test the cutout for continuity.<br><strong>No:</strong> Restricted airflow can cause the heat strip to overheat and trip the safety. Clean or replace the filter, then reset the breaker and test again.</div>
</details>

<details class="dtree"><summary>Can you hear or see the relay click when the thermostat calls for auxiliary heat?</summary>
<div class="dtree-body"><strong>Yes:</strong> The control signal is reaching the relay, so check for voltage at the heat strip terminals and verify the element has continuity.<br><strong>No:</strong> The control board may not be sending the signal, or the relay coil has failed. Measure 24 V across the relay coil terminals when heat is demanded.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off power** at the breaker and at the disconnect switch near the air handler to eliminate shock hazard.
2. **Remove the front cover** of the indoor unit and locate the auxiliary heat strip assembly, usually mounted in the airstream behind the evaporator coil.
3. **Inspect the thermal cutout** attached to the heat strip or its mounting bracket. Use a multimeter set to continuity (ohms) and probe across the cutout terminals; a reading of infinite resistance means it has tripped.
4. **Check the heat strip element** by measuring resistance across its terminals. A good element will show a few ohms to a few tens of ohms, depending on wattage; an open circuit indicates a failed heater.
5. **Test the control relay** by setting your multimeter to AC volts and measuring across the relay coil when the thermostat calls for heat. You should see approximately 24 V if the board is sending the signal.
6. **Inspect all wire connections** at the heat strip, thermal cutout, relay, and control board for corrosion, burns, or loose crimps. Clean terminals with contact cleaner and tighten screws.
7. **Replace the failed component** (thermal cutout, heat strip, relay, or fuse) with an exact replacement specified in your model's service manual, then restore power and test the system in heat mode.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Auxiliary heat strip | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mrcool-mini-split-eh-10-error-code&k=Auxiliary+heat+strip&tag=errorcodefixes-20) \| Match the kW rating and voltage stamped on the original element. |
| Thermal cutout / limit switch | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mrcool-mini-split-eh-10-error-code&k=Thermal+cutout+%2F+limit+switch&tag=errorcodefixes-20) \| Verify the trip temperature and mounting style for your air handler model. |
| Control relay or contactor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mrcool-mini-split-eh-10-error-code&k=Control+relay+or+contactor&tag=errorcodefixes-20) \| Check coil voltage (usually 24 V) and contact amperage rating before ordering. |

## When to Call a Pro

Call a licensed HVAC technician if you are uncomfortable working with line-voltage wiring or if diagnostic tests do not clearly identify a single failed part. Auxiliary heat circuits carry 208 or 240 V and draw significant current, so mistakes can damage the control board or create a fire hazard. A professional has the meters and experience to trace low-voltage control signals, verify proper relay operation, and safely replace high-current components. If the error persists after replacing obvious parts, the main control board may have failed, and a technician can flash firmware or swap the board without voiding your warranty.

**Rough cost:** A pro service call runs about $150-400.
