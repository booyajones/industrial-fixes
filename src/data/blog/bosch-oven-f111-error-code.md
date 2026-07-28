---
title: "Bosch Oven F111 Error Code - Causes & Fix"
description: "F111 means your Bosch oven has overheated past safe limits (over 585°F). Most common fix: replace a stuck relay or faulty control board."
pubDatetime: 2026-06-09T12:30:04Z
modDatetime: 2026-06-09T12:30:04Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - appliance
  - oven
  - bosch
money_part: "Bosch oven electronic control board"
most_likely_cause: "stuck heating relay or control board output keeping the element energized"
likelihood: "the most common cause"
diy_or_pro: "pro"
---

## What this code means
The F111 error code on a Bosch oven indicates an overtemperature fault. The control system has detected that the oven cavity has exceeded a safe temperature threshold, often reported as heating beyond 585°F. This typically occurs during self-clean cycles or when the heating element continues to run without proper regulation. The code is a safety shutoff to prevent damage or fire.

Unlike sensor-open or communication faults, F111 signals that the oven has actually become too hot. The control board has measured dangerously high temperatures and shut down operation. This can result from a stuck heating relay that keeps the element energized, a failed cooling fan that allows heat to build up during self-clean, or a temperature sensor and regulation fault that prevents the system from controlling heat output properly.

## Before You Replace Anything

Many people replace the temperature sensor first, but F111 is an actual overheat condition rather than a sensor reading error. Test whether the heating element shuts off properly and whether the cooling fan runs before ordering a sensor or control board.

## Common Causes

- **Stuck heating relay or control board output (~45%)** A relay on the control board has stuck closed or a triac output has failed, keeping the heating element powered continuously so the oven cannot regulate temperature and overheats.
- **Cooling fan failure during self-clean (~25%)** The cooling fan does not run or is obstructed, so heat builds up beyond safe limits during the high-temperature self-clean cycle.
- **Temperature sensor or regulation fault (~20%)** The oven temperature sensor is damaged, has corroded connectors, or is reading incorrectly, so the control cannot track or limit heat properly.
- **Wiring harness damage or loose connector (~10%)** A wire to the sensor, fan, or control board has frayed or a connector has backed out, causing intermittent or incorrect signals that prevent safe operation.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Did the F111 code appear during or immediately after a self-clean cycle?</summary>
<div class="dtree-body"><strong>Yes:</strong> The cooling fan or its circuit is the most likely culprit. Check whether the fan runs during self-clean and inspect the fan motor and wiring.<br><strong>No:</strong> The fault is more likely a stuck relay or temperature regulation issue. Proceed to check whether the heating element stays on after the oven command ends.</div>
</details>

<details class="dtree"><summary>After powering off the oven at the breaker and letting it cool completely, does the F111 code return immediately when you restore power?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is still present and not a one-time thermal spike. The control board, sensor, or fan circuit requires component-level diagnosis and repair.<br><strong>No:</strong> The fault may have been a transient overheat event. Monitor the oven through a full bake and self-clean cycle to see if the code reappears.</div>
</details>

<details class="dtree"><summary>Can you hear the cooling fan running when the oven is on or in self-clean mode?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fan circuit is working. Focus on the heating relay and temperature sensor as the next diagnostic targets.<br><strong>No:</strong> The cooling fan is not operating. Test the fan motor and check the control board output that drives it before replacing other parts.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Shut off power at the circuit breaker** and wait at least 30 minutes for the oven to cool completely before opening the door or touching any internal components.
2. **Inspect the cooling fan** by removing the lower rear panel or interior baffle (consult your model's service manual for access). Check that the fan blade spins freely and that the motor windings are not burned or seized.
3. **Test the temperature sensor resistance** by disconnecting the sensor connector and measuring across the sensor terminals with a multimeter at room temperature. Consult your model's wiring diagram for the expected resistance range (typically 1000–1100 ohms at 75°F for many ovens, but verify your model).
4. **Check for stuck relay or continuous heating** by restoring power briefly, setting a low bake temperature, and observing whether the heating element glows continuously without cycling off. If it stays on, the control board relay or output is stuck closed.
5. **Inspect all wiring and connectors** between the control board, temperature sensor, and cooling fan for signs of heat damage, corrosion, or loose pins.
6. **Replace the faulty component** once you have isolated the cause: the cooling fan if it does not run, the temperature sensor if resistance is out of range, or the control board if the relay is stuck or no other fault is found.
7. **Restore power and run a test bake cycle** at 350°F for 20 minutes, then attempt a short self-clean cycle to verify that the oven regulates temperature properly and the F111 code does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Bosch oven electronic control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-bosch-oven-f111-error-code&k=Bosch+oven+electronic+control+board&tag=errorcodefixes-20) \| Match the board part number printed on the existing board or use your model number to cross-reference the correct replacement. |
| Bosch oven temperature sensor probe | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-bosch-oven-f111-error-code&k=Bosch+oven+temperature+sensor+probe&tag=errorcodefixes-20) \| Verify the connector type and probe length match your model before ordering. |
| Bosch oven cooling fan motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-bosch-oven-f111-error-code&k=Bosch+oven+cooling+fan+motor&tag=errorcodefixes-20) \| Used in self-clean ovens to exhaust heat. Confirm your model uses a separate cooling fan and match the motor mounting style. |
| Wiring harness repair kit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-bosch-oven-f111-error-code&k=Wiring+harness+repair+kit&tag=errorcodefixes-20) \| Includes connectors and heat-shrink terminals for damaged sensor or fan wiring. |

## When to Call a Pro

Call a professional if you are not comfortable working with 240-volt appliance wiring or if you cannot safely access the control board and sensor connections. Diagnosing a stuck relay or control board output requires experience with multimeter testing and understanding of oven control circuits. A qualified appliance technician can perform component-level diagnostics, verify that the cooling fan circuit is operating correctly, and replace the control board or relay assembly safely. If the oven has overheated to the point of visible damage to wiring insulation or internal components, a pro should inspect the entire appliance for hidden damage before it is returned to service.

**Rough cost:** A pro service call runs about $200–450 depending on whether the repair is a relay, fan, or full control board replacement.
