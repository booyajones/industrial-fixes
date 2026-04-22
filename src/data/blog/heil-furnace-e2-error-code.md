---
title: "Heil Furnace E2 Error Code — Causes & Fix"
description: "What Heil furnace error code E2 means, why the pressure switch sticks closed, and how to fix it step by step."
pubDatetime: 2026-04-22T15:00:00Z
modDatetime: 2026-04-22T15:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - heil
---

## Heil Furnace E2 Error Code — What It Means

E2 on a Heil furnace indicates the pressure switch is stuck in the closed position before the inducer motor has started. Heil furnaces (an ICP/Carrier brand) verify that the pressure switch is open at system startup as a safety check. If the switch is already closed at that moment, the board assumes a fault and locks out with E2. This is a reversal of the more common "pressure switch open" fault — here the switch is welded shut or mechanically stuck closed when it should be open.

[Jump to Fix](#fix)

## Common Causes

- **Welded or stuck pressure switch contacts** — A pressure switch that has cycled thousands of times can develop contacts that fuse together, leaving the switch permanently closed regardless of inducer status.
- **Water-logged pressure switch** — Condensate that migrates up the pressure hose into the switch body can hold the diaphragm in the closed position, mimicking a stuck switch.
- **Shorted wiring to the pressure switch** — A wiring fault in the harness between the control board and the pressure switch can present as a permanently closed circuit.
- **Wrong replacement switch installed** — A replacement pressure switch with a lower opening set-point than the original can close at atmospheric conditions and never open at startup.

## Step-by-Step Fix {#fix}

1. **Power off the furnace** — Turn off the disconnect and thermostat before any inspection.
2. **Disconnect the pressure hose from the switch** — With the hose off, check if the switch is still registering closed with a multimeter across its terminals. If it reads closed with no suction applied, the switch has failed.
3. **Drain condensate from the hose and switch port** — Tilt the switch and hose to let any trapped water drain out. Blow through the hose to confirm it is clear, then reconnect and test.
4. **Check the wiring harness** — Inspect the wires from the control board to the pressure switch for pinched insulation, staple damage, or corrosion at the connector pins that could create a short.
5. **Replace the pressure switch** — If the switch tests closed at rest with no vacuum applied, replace it with the OEM-specified switch (match the water column rating).
6. **Reset and test** — Restore power and cycle the thermostat. The furnace should start its inducer, confirm the pressure switch closes properly during inducer operation, and light the burners.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [Pressure switch](https://www.amazon.com/s?k=Pressure%20switch&tag=errorcodefixe-20) | Use the OEM water column rating; aftermarket switches must match exactly |
| [Pressure switch hose](https://www.amazon.com/s?k=Pressure%20switch%20hose&tag=errorcodefixe-20) | Replace if cracked or if condensate was present |

## When to Call a Pro

If the wiring harness shows signs of rodent damage or burn marks, or if replacing the pressure switch does not clear E2, call a technician — there may be a control board fault misinterpreting the circuit.
