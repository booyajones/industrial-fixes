---
title: "Hussmann Display Case E2 Error Code — Defrost Circuit Fault"
description: "What the Hussmann display case E2 error code means, why the defrost circuit fault triggers, and how to fix it step by step."
pubDatetime: 2026-04-22T14:00:00Z
modDatetime: 2026-04-22T14:00:00Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - refrigeration
  - hussmann
money_part: "Defrost heater assembly"
most_likely_cause: "Failed defrost heater element"
---

## Hussmann Display Case E2 Error Code — What It Means

On Hussmann supermarket display cases (reach-in and open-air merchandisers), E2 indicates a defrost circuit fault — the case controller initiated a defrost cycle, but the defrost heater did not raise the evaporator coil temperature to the defrost termination setpoint within the allowed time. The controller terminates the defrost on time rather than on temperature and logs E2. Repeated E2 faults cause ice buildup on the evaporator coil, eventually reducing refrigeration capacity and product temperature control. E2 is a warning about the defrost system, not an immediate refrigeration lockout.

[Jump to Fix](#fix)

## Common Causes

- **Failed defrost heater element** — The resistance heaters embedded in or attached to the evaporator coil burn out over time, especially in high-cycle applications. A partial heater failure leaves some sections of the coil iced while others clear, and the termination sensor never sees the target temperature.
- **Failed defrost termination thermostat** — The defrost termination thermostat (or sensor) monitors coil temperature during defrost. If it fails open, the controller thinks defrost hasn't terminated even when the coil is warm. If it fails closed, defrost terminates too early.
- **Wiring fault to defrost heaters** — Loose terminal connections or a broken wire to the defrost heater circuit produces the same result as a failed heater.
- **Heavy ice accumulation** — Chronic door seal failures or frequent door openings allow warm, moist air into the case. The resulting ice buildup is too heavy for the heaters to clear in the allotted defrost time.
- **Defrost timer or controller fault** — A failed defrost timer board or corrupted controller program may not energize the heaters correctly even when the defrost relay pulls in.

## Step-by-Step Fix {#fix}

1. **Inspect the evaporator coil for ice buildup** — Remove the case's back panel (power off first). If the coil is heavily iced, perform a manual defrost by applying warm water or a heat gun carefully to the coil. A heavily iced coil indicates the defrost system has been failing for some time.
2. **Test the defrost heater resistance** — With the heater circuit de-energized and disconnected, measure resistance across each heater element with a multimeter. A healthy heater reads 10–100 ohms depending on wattage. An open circuit (OL) means the heater is burned out.
3. **Test the defrost termination thermostat / sensor** — Measure continuity across the termination thermostat when the coil is at room temperature. On a normally-open style (most common), it should show continuity when cold and open when warm. Replace if it doesn't behave as specified.
4. **Inspect wiring connections** — Check all terminal connections in the defrost circuit — at the defrost contactor, heater junction box, and termination thermostat. Loose terminals in a refrigerated environment corrode rapidly.
5. **Manually initiate a defrost cycle** — With repairs made, manually initiate a defrost cycle from the case controller (most Hussmann controllers have a manual defrost button). Watch the coil temperature rise on the controller display. Defrost termination should occur at the setpoint (typically 55–60°F/13–15°C for most medium-temp cases).
6. **Inspect door gaskets** — After clearing E2, inspect all door gaskets for tears or poor sealing. Moisture infiltration from bad gaskets is the most common cause of chronic heavy icing and repeated E2.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Defrost heater assembly | [Amazon](https://www.amazon.com/dp/B07FVP4CY6?ascsubtag=ecf-hussmann-display-case-e2&tag=errorcodefixes-20) \| Match wattage and physical size from case engineering data |
| Defrost termination thermostat | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-hussmann-display-case-e2&tag=errorcodefixes-20) \| Match setpoint temperature and style (normally open/closed) |
| Door gasket set | [Amazon](https://www.amazon.com/dp/B0FPF84HQP?ascsubtag=ecf-hussmann-display-case-e2&tag=errorcodefixes-20) \| Replace if torn or not sealing flat against the door frame |
| Defrost contactor | [Amazon](https://www.amazon.com/dp/B0CJFZQVPT?ascsubtag=ecf-hussmann-display-case-e2&tag=errorcodefixes-20) \| Replace if contactor doesn't pull in during defrost initiation |
## When to Call a Pro

Hussmann display cases are often covered by store maintenance agreements. Refrigerant-side work (if E2 is accompanied by poor temperature performance suggesting a refrigerant issue) requires EPA 608 certification. Hussmann's 24/7 technical support line can provide model-specific defrost wiring diagrams and setpoint data.
