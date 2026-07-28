---
title: "True Refrigeration E4 Error Code — Causes & Fix"
description: "What True Refrigeration error code E4 means, why the defrost heater faults, and how to fix it step by step."
pubDatetime: 2026-04-22T15:00:00Z
modDatetime: 2026-04-22T15:00:00Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - refrigeration
  - true-refrigeration
money_part: "Defrost heater"
most_likely_cause: "Failed defrost heater element"
---

## What this code means
E4 on a True commercial refrigerator or freezer signals a defrost heater fault — the control board detected that the defrost cycle did not terminate within the expected time, or the defrost temperature sensor did not confirm that the evaporator coil reached the defrost termination temperature. True Manufacturing's electronic controls (used on GDM, T, and TFM series units) rely on the defrost heater to clear ice from the evaporator. If the heater is open-circuit or if the termination sensor fails, the defrost cycle runs indefinitely or fails to run at all, and the board logs E4.

## Common Causes

- **Failed defrost heater element** — The defrost heater (a glass or stainless-steel sheathed resistance element) burns open after repeated thermal cycles. A break in the element prevents any defrost heat from being generated.
- **Failed defrost termination thermostat** — The defrost termination thermostat is a bimetallic device that opens the defrost circuit when the coil reaches the defrost termination temperature (typically 45–60°F). A failed-open thermostat prevents defrost from completing; a failed-closed thermostat prevents the board from seeing termination.
- **Defrost timer/control board fault** — The electronic control board may fail to initiate defrost or may incorrectly count defrost time, triggering E4 without any heater failure.
- **Wiring fault** — A broken or shorted wire in the defrost circuit prevents the heater from receiving power or prevents the sensor from returning accurate data to the board.

## Step-by-Step Fix {#fix}

1. **Power off the unit** — Disconnect the unit from power before accessing defrost components inside the refrigerated space.
2. **Locate the evaporator access panel** — Remove the internal rear or ceiling panel to expose the evaporator coil, defrost heater, and termination thermostat.
3. **Test the defrost heater** — Disconnect the heater wires and measure resistance across the heater terminals with a multimeter. A good heater reads a finite resistance (typically 30–100 Ω depending on wattage). Open circuit (infinite resistance) = failed heater.
4. **Test the defrost termination thermostat** — At room temperature, the termination thermostat should be closed (near-zero Ω). If it reads open at room temperature, it has failed open.
5. **Inspect the wiring harness** — Trace the defrost circuit wiring for any visible damage, melted insulation, or disconnected plugs.
6. **Replace faulty components** — Install the OEM True replacement defrost heater and/or termination thermostat for the specific True model number.
7. **Restore power and initiate a forced defrost** — Most True controls allow a manual defrost initiation. Confirm the heater energizes, the coil defrosts, and the termination sensor causes the board to end the defrost cycle normally.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Defrost heater | [Amazon](https://www.amazon.com/dp/B07FVP4CY6?ascsubtag=ecf-true-refrigeration-e4-error-code&tag=errorcodefixes-20) \| True OEM or exact resistance match; match wattage and physical length |
| Defrost termination thermostat | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-true-refrigeration-e4-error-code&tag=errorcodefixes-20) \| Match clip type and temperature rating for the True model |
## When to Call a Pro

If the control board itself is suspected (E4 with a good heater and thermostat), board replacement requires matching the True model and serial number. Commercial refrigeration equipment repair often requires EPA 608 certification if refrigerant work is also needed.
