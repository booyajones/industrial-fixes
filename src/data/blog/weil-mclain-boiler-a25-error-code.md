---
title: "Weil-McLain Boiler A25 Error - Causes & Fix"
description: "A25 (or B-25) signals a soft lockout from rapid temperature rise or high limit. Usually a bad supply/return sensor or failing circulator."
pubDatetime: 2026-06-13T13:03:58Z
modDatetime: 2026-06-13T13:03:58Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - boiler
  - weil-mclain
money_part: "Weil-McLain supply temperature sensor"
most_likely_cause: "failed supply or return temperature sensor"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Check that the primary circulator pump is running when the boiler fires"
  - "Inspect for air in the system by opening bleed valves at high points in the piping"
  - "Verify the closely spaced tees are no farther apart than about 12 inches per Weil-McLain specs"
---

## What this code means
A25 is not a universal code across all Weil-McLain models. On Ultra-series controls, the closely related code B-25 (which may be the same fault on your system) is a soft lockout that shuts down the burner for about 10 minutes because the boiler temperature rose too quickly or hit the high-limit safety threshold. This lockout is designed to protect the heat exchanger from thermal stress when normal heat removal is not happening. The boiler will attempt to restart automatically after the lockout period expires, but the fault will recur if the underlying flow or sensor problem is not corrected.

## Before You Replace Anything

Homeowners often assume the control board is at fault and replace it first. Test the supply and return sensors with a multimeter and verify circulator operation before spending money on a new board.

## Common Causes

- **Failed supply or return temperature sensor (~40%)** A sensor that reads incorrectly can make the control think the boiler is overheating when it is not, triggering the soft lockout.
- **Primary circulator pump failure (~30%)** The pump near the boiler may have stopped moving water or has low flow, causing heat to build up faster than the sensor expects.
- **Air trapped in the system (~15%)** Air pockets reduce flow and heat transfer, so the supply temperature spikes even though the system is not removing heat properly.
- **Improperly spaced primary/secondary tees (~10%)** Tees installed too far apart (more than about 12 inches) prevent proper hydraulic separation and cause erratic temperature behavior.
- **Control board misreading history or calibration (~5%)** Less common, but the board itself may have a fault that interprets normal temperature ramps as too fast.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is the primary circulator pump running when the boiler is firing?</summary>
<div class="dtree-body"><strong>Yes:</strong> The pump is working, so focus on sensor accuracy and air in the system.<br><strong>No:</strong> The pump has failed or lost power, and that is why heat is building up. Check wiring and replace the pump if needed.</div>
</details>

<details class="dtree"><summary>Do the supply and return temperatures shown on the control match what you measure with an infrared thermometer on the pipes?</summary>
<div class="dtree-body"><strong>Yes:</strong> The sensors are reading correctly, so the problem is more likely air, low flow, or piping layout.<br><strong>No:</strong> One or both sensors are reading incorrectly and must be replaced.</div>
</details>

<details class="dtree"><summary>Can you bleed air from the high points in the system without a continuous stream of water?</summary>
<div class="dtree-body"><strong>Yes:</strong> Air is present and needs to be purged completely before troubleshooting further.<br><strong>No:</strong> The system is fully purged, so move on to testing sensors and verifying circulator current draw.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Confirm your exact boiler model and control platform** by checking the rating plate and control-panel label, since A25 may have different meanings on different series.
2. **Observe whether the primary circulator runs** when the boiler calls for heat, and listen for pump noise or feel the motor for vibration.
3. **Measure the supply and return pipe temperatures** with an infrared thermometer and compare them to the readings on the boiler control display.
4. **Test the supply and return sensors** with a multimeter by checking resistance at known temperatures and comparing to the manufacturer's curve (consult your service manual for the resistance table).
5. **Purge all air** from the system by opening bleed valves at radiators, air scoops, and high points until you see a solid stream of water with no bubbles.
6. **Inspect the closely spaced tees** on the primary/secondary piping to verify they are no farther apart than about 12 inches and are installed in the correct orientation.
7. **Replace the failed component** identified by testing (sensor or circulator), reset the lockout, and monitor the next few heating cycles to confirm the fault does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Weil-McLain supply temperature sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a25-error-code&k=Weil-McLain+supply+temperature+sensor&tag=errorcodefixes-20) \| Match the part number to your boiler model and control version. |
| Weil-McLain return temperature sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a25-error-code&k=Weil-McLain+return+temperature+sensor&tag=errorcodefixes-20) \| Often sold separately from the supply sensor. |
| Primary circulator pump (e.g. Grundfos, Taco) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a25-error-code&k=Primary+circulator+pump+%28e.g.+Grundfos%2C+Taco%29&tag=errorcodefixes-20) \| Verify flange size, voltage, and flow rating before ordering. |

## When to Call a Pro

Call a professional if you are not comfortable working with 120V or 24V boiler controls, testing sensors with a multimeter, or diagnosing hydronic flow and piping layout. A technician will use a clamp-on ammeter to verify circulator current draw, resistance tables to test sensors accurately, and a digital manometer to check system pressure. Gas-fired boilers also require annual combustion testing and flue analysis, which only a licensed technician should perform. If the fault persists after sensor and pump checks, the control board or wiring may need diagnosis with specialized tools.

**Rough cost:** A pro service call runs about $200-400.
