---
title: "Carrier 44 Error Code — Causes & Fix"
description: "What Carrier error code 44 means, why the igniter circuit opens, and how to fix it step by step."
pubDatetime: 2026-04-22T11:00:00Z
modDatetime: 2026-04-22T11:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - carrier
money_part: "Hot surface igniter"
most_likely_cause: "Failed hot surface igniter"
---

## What this code means
Carrier error code 44 indicates an open igniter circuit. The furnace control board detected that the igniter is not drawing the expected current when energized, which means the igniter is either broken, disconnected, or the circuit supplying it has failed. The furnace will lock out on this fault to prevent unlit gas from accumulating.

## Common Causes

- **Failed hot surface igniter** — The igniter element has cracked or burned out and will not draw current. This is the most common cause on furnaces with more than 5 years of service.
- **Loose or corroded igniter wiring** — A disconnected or oxidized connector at the igniter or control board interrupts the circuit even if the igniter itself is intact.
- **Faulty igniter relay on control board** — The relay that switches 120V to the igniter can fail open, so voltage never reaches the igniter.
- **Wrong igniter installed** — An igniter with incompatible resistance or voltage rating may not satisfy the board's current sensing threshold.

## Step-by-Step Fix {#fix}

1. **Power down the furnace** — Turn the power switch off and set the thermostat to OFF before opening the cabinet.
2. **Locate and visually inspect the igniter** — The hot surface igniter is typically a silicon carbide or silicon nitride rod mounted near the burner assembly. Look for visible cracks, fractures, or burn marks.
3. **Measure igniter resistance** — Use a multimeter set to ohms. Disconnect the igniter harness and measure across the igniter terminals. Silicon carbide igniters should read 40–90 Ω at room temperature; silicon nitride should read 15–75 Ω. An open reading (OL) confirms a failed igniter.
4. **Check the igniter wiring harness** — Inspect the plug at both the igniter and the control board. Reseat loose connectors and look for melted or damaged wire insulation.
5. **Test voltage at the igniter connector** — With power restored and a call for heat, measure AC voltage at the igniter harness during the igniter pre-heat sequence. You should see approximately 120V. No voltage points to the control board relay.
6. **Replace the igniter** — Use a Carrier-compatible igniter for your model. Part numbers vary by series; cross-reference with the furnace model tag.
7. **Reset the system** — Restore power, set the thermostat to Heat, and verify the igniter glows and the burners light normally. Clear any lockout by cycling the power switch.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Hot surface igniter | [Amazon](https://www.amazon.com/dp/B00BTLLJ40?ascsubtag=ecf-carrier-44-error-code&tag=errorcodefixes-20) \| Match to furnace model; silicon nitride is more durable than silicon carbide |
| Igniter wiring harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-carrier-44-error-code&k=Igniter+wiring+harness&tag=errorcodefixes-20) \| Replace if insulation is melted or connector pins are corroded |
| Furnace control board | [Amazon](https://www.amazon.com/s?k=Furnace+control+board&tag=errorcodefixes-20) \| Only if relay confirmed open under load testing |
## When to Call a Pro

If voltage is confirmed at the igniter connector but the board still throws a 44 fault, or if you suspect a gas valve issue is masking the fault, call a licensed HVAC technician. Gas train diagnostics require proper combustion testing equipment.
