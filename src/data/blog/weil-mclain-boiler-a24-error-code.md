---
title: "Weil-McLain Boiler A24 Error - Causes & Fix"
description: "A24 means return temperature > supply temperature, a soft lockout. Check sensor wiring and pump direction before resetting the boiler."
pubDatetime: 2026-06-13T13:03:10Z
modDatetime: 2026-06-13T13:03:10Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - boiler
  - weil-mclain
money_part: "Weil-McLain supply or return temperature sensor"
most_likely_cause: "hydronic flow reversal or abnormal circulation pattern"
likelihood: "the most common practical cause"
diy_or_pro: "pro"
free_checks:
  - "Check that the supply and return sensor wires are attached to the correct pipes and not swapped."
  - "Verify pump orientation and confirm it is pumping away from the expansion tank."
  - "Read live sensor values in the control's diagnostic menu to see if return really exceeds supply."
no_buy_pct: "75%"
---

## Weil-McLain Boiler A24 Error — What It Means

The A24 code on Weil-McLain boilers is most consistently reported as a soft lockout triggered when the return-water temperature sensor reads higher than the supply-water temperature sensor. The control interprets this inverted temperature relationship as an abnormal condition and temporarily stops the boiler from firing. Because Weil-McLain code meanings vary by model and control platform, you should verify the exact meaning in your boiler's manual before treating A24 as a universal fault code.

In practice, A24 does not indicate a failed component but rather an unusual flow or sensor condition. The fault can occur during a domestic hot-water call when warmer water returns from the DHW loop and briefly outpaces the supply sensor reading, or when zone piping or pump direction creates a hydraulic reversal. The code is temporary and will clear once the underlying issue is corrected and the boiler is reset.

## Before You Replace Anything

Do not replace the supply or return temperature sensors immediately. First verify the sensors are wired to the correct pipes and read live temperatures during a fault to confirm the reversal is real, not a wiring swap.

[Jump to Fix](#fix)

## Common Causes

- **Hydronic flow reversal or unusual circulation pattern (~40%)** Pump orientation, zone valve location, or piping arrangement causes hotter water to reach the return sensor before the supply sensor equalizes.
- **Domestic hot-water priority or mixing-valve interaction (~30%)** During a DHW call, warm return water from the domestic loop returns to the boiler faster than the supply sensor can track, triggering the fault.
- **Swapped or misplaced sensor wiring (~20%)** The supply and return temperature sensor wires are attached to the wrong pipes, making the control read the temperatures backwards.
- **Faulty supply or return temperature sensor (~10%)** One sensor reads incorrectly, causing the control to see an impossible temperature relationship even when flow is normal.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the A24 code appear only during a domestic hot-water call?</summary>
<div class="dtree-body"><strong>Yes:</strong> The DHW loop or mixing valve is likely returning warm water too quickly. Inspect the DHW aquastat, mixing valve settings, and piping arrangement.<br><strong>No:</strong> The fault occurs during space heating or all the time, so check pump direction, zone piping, and sensor wiring next.</div>
</details>

<details class="dtree"><summary>Are the supply and return sensor wires attached to the correct pipes?</summary>
<div class="dtree-body"><strong>Yes:</strong> Wiring is correct. Verify pump orientation and check live sensor readings in the control's diagnostic menu to confirm the temperature reversal is real.<br><strong>No:</strong> Swap the sensor wires to match the correct pipe locations, reset the boiler, and retest to see if the code clears.</div>
</details>

<details class="dtree"><summary>Does the diagnostic menu show return temperature higher than supply when the fault occurs?</summary>
<div class="dtree-body"><strong>Yes:</strong> The reversal is real. Trace the piping to find where warm water is returning before the supply heats up, and correct the flow or zone arrangement.<br><strong>No:</strong> One sensor may be reading incorrectly. Test each sensor's resistance and compare to the model's specification table to find the faulty sensor.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Identify the exact boiler model and control platform.** Pull the correct service manual from Weil-McLain for your boiler series, because code meanings vary by control family.
2. **Access the control's diagnostic menu.** Read the current supply and return temperatures live to confirm whether the return sensor is actually reading higher than the supply.
3. **Inspect the supply and return sensor locations.** Verify each sensor is attached to the correct pipe and that the wiring has not been swapped or damaged.
4. **Check pump orientation and system piping.** Confirm the circulator is pumping away from the expansion tank and that zone valves or mixing valves are not creating a reverse flow path.
5. **Verify domestic hot-water operation.** If the fault occurs during a DHW call, inspect the DHW aquastat, mixing valve settings, and loop arrangement for conditions that return warm water prematurely.
6. **Test sensor resistance if needed.** Disconnect each sensor and measure its resistance at the current temperature, then compare to the manufacturer's sensor table in the manual.
7. **Correct the hydraulic or sensor issue, reset the boiler, and retest.** Once the underlying cause is fixed, press the reset button and observe the next firing cycle to confirm the code does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Weil-McLain supply or return temperature sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a24-error-code&k=Weil-McLain+supply+or+return+temperature+sensor&tag=errorcodefixes-20) \| Only if testing confirms the sensor is reading incorrectly. Verify the exact part number for your control model. |
| Zone valve or diverter valve | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a24-error-code&k=Zone+valve+or+diverter+valve&tag=errorcodefixes-20) \| If piping inspection reveals a valve stuck or installed backwards, causing flow reversal. |

## When to Call a Pro

Call a heating professional if you are not comfortable reading live diagnostics on the boiler control, tracing hydronic piping to find flow reversals, or testing sensor resistance with a multimeter. The A24 code usually points to a piping, pump, or sensor wiring issue rather than a failed part, so a technician can diagnose the hydraulic arrangement and correct the flow pattern or sensor placement. A pro is also required if you need to relocate sensors, re-pipe zone valves, or adjust domestic hot-water priority logic on the control board.

**Rough cost:** A pro service call runs about $150–350.
