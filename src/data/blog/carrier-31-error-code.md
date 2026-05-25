---
title: "Carrier 31 Error Code — Pressure Switch Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-03-04T08:00:00Z
modDatetime: 2024-03-04T08:00:00Z
slug: carrier-31-error-code
featured: false
draft: false
tags:
  - hvac
  - carrier
  - furnace
  - pressure-switch
  - inducer
description: "Carrier error code 31 means the pressure switch is stuck open or failed. This step-by-step guide walks you through diagnosing the inducer, hoses, and switch itself."
---

## Error Code: Carrier 31

**What it means:** Code 3-1 indicates the pressure switch didn't close (or opened unexpectedly) during the inducer pre-purge phase. The pressure switch is a safety device that confirms the draft inducer motor is running and creating sufficient negative pressure to safely remove combustion gases. If the switch doesn't see adequate draft, the control board won't open the gas valve — and the furnace shuts down with code 31.

## Common Causes

- **Blocked or collapsed pressure switch hose** — The small rubber or vinyl tubing that connects the inducer housing to the pressure switch is the most common failure point. Condensation, debris, or kinking can block it entirely.
- **Water in the pressure switch** — In high-efficiency (90%+) furnaces, condensate can back up into the pressure switch port and hold it open permanently. This is especially common after a blocked condensate drain.
- **Failed or weak draft inducer motor** — An inducer that runs but doesn't develop adequate suction (worn impeller, bad bearings) won't create enough negative pressure to close the switch.
- **Pressure switch set point drift or diaphragm failure** — The switch diaphragm can develop a pinhole or lose elasticity, causing it to fail at rated pressure. Common on furnaces over 10 years old.
- **Blocked flue or vent pipe** — A partially blocked flue increases static resistance, reducing the draft at the pressure switch sensing port.
- **Cracked inducer housing** — A crack in the inducer housing allows air to leak, reducing the negative pressure at the switch port.

## Step-by-Step Fix {#step-by-step-fix}

1. **Verify the draft inducer starts during the heat call.** Initiate a heat cycle and listen for the inducer motor (the smaller motor on top/side of the heat exchanger) to start and ramp up within 5–10 seconds. If it doesn't start, the problem is upstream of the pressure switch — check inducer motor wiring and control board output.

2. **Inspect the pressure switch hose.** With the furnace OFF, locate the small rubber hose running from the inducer housing port to the pressure switch (usually 1/4" to 3/8" diameter, 3–12 inches long). Disconnect both ends. Look for cracks, kinks, water inside the hose, or debris in either port. Blow through it to confirm it's clear. Replace with matching ID/OD tubing if blocked or cracked — it's less than $2 of material.

3. **Check for water in the pressure switch.** Disconnect the hose at the pressure switch inlet and tip the switch port down. If water drips out, condensate has been accumulating in the switch. Shake it dry (or replace), then fix the root cause — check the condensate drain line for blockage (blow it clear or pour water through it).

4. **Test the pressure switch directly.** With the furnace off, use a multimeter on continuity mode across the switch terminals. An open-style pressure switch (normally open) should show NO continuity at rest and continuity when you apply suction to the inlet port (use your mouth to apply gentle suction while watching the meter). If it won't close under suction, the diaphragm is dead — replace the switch.

5. **Measure the actual draft pressure.** With a magnehelic gauge or manometer, tap into the inducer housing and measure draft pressure while the inducer runs. Compare to the switch rating (printed on the switch — typically -0.50" to -1.70" W.C. depending on the model). If draft is low but the inducer runs, check the flue for blockage and the inducer impeller for debris.

6. **Inspect the flue pipe end cap and termination.** Go outside and look at the PVC vent termination. Spiders, wasp nests, and ice buildup in winter are documented causes of flue obstruction that trigger pressure switch faults.

7. **Clear and retest.** After repair, restore power and run 3 complete heat cycles. Confirm code 31 does not return. If it returns intermittently (only when cold, only in rain), the problem is likely moisture/condensate-related and requires fixing the drainage system.

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Where to Buy | Typical Cost |
|------|-------------|-------------|
| Pressure switch (Carrier #HK06WC085 or HK06WC064) | [Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-carrier-31-error-code&tag=errorcodefixes-20) \| Carrier dealer, Johnstone Supply | $20–$50 |
| Draft inducer assembly (Carrier #HC21ZE120A) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-carrier-31-error-code&k=Draft+inducer+assembly+%28Carrier+%23HC21ZE120A%29&tag=errorcodefixes-20) \| RepairClinic, Carrier OEM | $120–$280 |
| Condensate drain line kit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-carrier-31-error-code&k=Condensate+drain+line+kit&tag=errorcodefixes-20) \| Home Depot, HVAC Supply | $10–$25 |
| Pressure switch hose (3/8" ID vinyl, sold by foot) | [Amazon](https://www.amazon.com/dp/B0CPTHML1N?ascsubtag=ecf-carrier-31-error-code&tag=errorcodefixes-20) \| Any hardware store | $2–$5 |
## When to Call a Professional

If you've cleared the hose, dried the switch, confirmed the inducer runs strongly, and the switch still won't close — you need a tech with a manometer to measure actual draft. A furnace that produces too little draft for its pressure switch rating usually means either the inducer is failing internally (impeller wear) or there's a major flue restriction. Both require hands-on diagnosis. Tell your tech: "Code 31, pressure switch won't close. I've already cleared the hose and the switch tests good at rest. I need you to measure draft on the inducer."

> **Pro tip:** On 90%+ efficiency Carrier furnaces, always check the condensate drain trap for blockage before replacing the pressure switch. A blocked trap creates a positive pressure inside the inducer housing that can hold the pressure switch open even when everything else is working perfectly. It's a 5-minute fix that saves a $40 part.

## Related Articles

- [Carrier 11 Error Code — Causes & Fix](/posts/carrier-11-error-code/)
- [Carrier 12 Error Code — Causes & Fix](/posts/carrier-12-error-code/)
- [Carrier 13 Error Code — Limit Switch Lockout Fix](/posts/carrier-13-error-code/)
- [Carrier 13 Soft Lockout — What's Different from Hard Lockout](/posts/carrier-13-soft-lockout/)
- [Carrier 14 Error Code — Causes & Fix](/posts/carrier-14-error-code/)

## See Also

- [Carrier 25 Error Code — Causes & Fix](/posts/carrier-25-error-code/)
- [Carrier 22 Error Code — Causes & Fix](/posts/carrier-22-error-code/)
- [Carrier Infinity Series 24ACC6 Error Codes — Fault Code Diagnostic Guide](/posts/carrier-infinity-24acc6-error-codes/)
- [Carrier Greenspeed A3 — Defrost Fault Fix](/posts/carrier-heat-pump-error-code-a3/)
