---
title: "Trane 3 Flashes Error Code — Pressure Switch Fault Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-03-24T08:00:00Z
modDatetime: 2024-03-24T08:00:00Z
slug: trane-3-flashes-error-code
featured: false
draft: false
tags:
  - hvac
  - trane
  - furnace
  - pressure-switch
description: "Trane 3 flashes means the pressure switch failed to close or opened during operation. This guide covers diagnosis and fixes for the Trane furnace pressure switch fault."
---

## Error Code: Trane 3 Flashes

**What it means:** Three flashes on the Trane furnace diagnostic LED indicates a pressure switch fault. The pressure switch is a normally-open switch that closes when the inducer motor creates sufficient negative pressure (draft) inside the furnace combustion chamber. When the switch fails to close within a set timeframe after the inducer starts — or opens during operation — the control board shuts down and displays 3 flashes. The board is protecting the furnace from running without proper draft, which would allow combustion gases to back up into the heat exchanger and living space.

## Common Causes

- **Blocked or kinked pressure switch hose** — The small rubber hose connecting the pressure switch to the inducer housing or condensate collector box is the most common cause. Even partial kinks reduce the pressure signal enough to prevent switch closure.
- **Condensate backup in the pressure switch port** — Water collects in the hose or the switch port itself, blocking the pressure signal. Common on high-efficiency (90%+) furnaces where condensate is produced.
- **Failed inducer motor** — If the inducer is not spinning at full RPM, it may not produce enough draft to close the pressure switch. Listen for the inducer — a slow, labored sound or no sound at all points here.
- **Failed pressure switch** — The switch diaphragm can rupture or the contacts can fail. A failed switch won't close even with correct draft pressure.
- **Restricted flue or venting** — Blocked PVC vent pipes on high-efficiency furnaces reduce draft. Ice blockages at exterior vent terminations are common in winter.

## Diagnosis Steps

1. With the furnace door removed, initiate a call for heat. Watch and listen for the inducer motor to start. It should spin up within 30 seconds of the call.
2. While the inducer is running, locate the pressure switch hose (small rubber tube, usually 1/4" diameter). Check the full length for kinks, cracks, or disconnections. Disconnect it and blow through it — it should flow freely.
3. Disconnect the hose from the switch port. Blow through the switch port itself. If you feel resistance or water comes out, clear the blockage with a thin wire and reconnect.
4. With the inducer running, use a digital manometer to measure draft at the pressure switch port. Compare to the switch rating (printed on the switch body — typically -0.50" to -1.80" W.C. depending on model). If measured draft meets or exceeds the switch setpoint but the switch is not closing, replace the switch.
5. Locate and inspect both PVC vent pipes at the exterior of the house. Confirm they are clear and terminate with the proper 12" above ground clearance.

## Fix

Start with the pressure switch hose — remove it, clear any water or debris, and reinstall. On condensing furnaces, run the furnace through a cycle and check if condensate is draining properly from the collector box. A blocked condensate drain will back water up into the pressure switch circuit.

If the hose is clear and draft pressure is correct but the switch is still not closing: replace the pressure switch. Match the pressure rating exactly — Trane uses multiple switch ratings depending on furnace model. The rating is stamped on the switch body (e.g., -1.42" W.C.). Order by the furnace model number to ensure correct specs.

If inducer RPM is low or the motor sounds labored: check inducer motor capacitor (a failed run capacitor causes low torque and reduced RPM). Replace the capacitor before replacing the full inducer assembly.

## Parts

| Part | Where to Buy |
|------|-------------|
| [Pressure switch (match rating and model)](https://www.amazon.com/s?k=Pressure+switch+%28match+rating+and+model%29&tag=errorcodefixes-20) | RepairClinic, SupplyHouse |
| [Pressure switch hose / tubing](https://www.amazon.com/s?k=Pressure+switch+hose+%2F+tubing&tag=errorcodefixes-20) | RepairClinic, Amazon |
| [Inducer motor run capacitor](https://www.amazon.com/s?k=Inducer+motor+run+capacitor&tag=errorcodefixes-20) | Grainger, Amazon |
| [Inducer motor assembly](https://www.amazon.com/s?k=Inducer+motor+assembly&tag=errorcodefixes-20) | RepairClinic, Grainger |

## When to Call a Technician

Pressure switch diagnosis is straightforward for someone comfortable with basic electrical testing. However, if you're seeing 3 flashes on a high-efficiency furnace with a blocked or frozen vent, that's a safety concern — do not operate the furnace until venting is restored. A licensed tech should handle any work involving the inducer or heat exchanger inspection.

## See Also

- [Trane XR80 Error Codes — Flash Code Quick Reference](/posts/trane-xr80-error-codes/)
- [Trane 7 Flashes Error Code — Gas Valve Circuit Fault Fix](/posts/trane-7-flashes-error-code/)
- [Trane XE80 Furnace Error Codes — Fault Code Guide](/posts/trane-xe80-error-codes/)
- [Trane XV20i/XV18 Variable Speed Heat Pump Error Codes](/posts/trane-variable-speed-heat-pump-codes/)

## Related Articles

- [Trane 1 Flash Error Code — Causes & Fix](/posts/trane-1-flash-error-code/)
- [Trane Error Code 126 — Ignition Lockout Fix](/posts/trane-126-error-code/)
- [Trane 2 Flashes Error Code — Causes & Fix](/posts/trane-2-flashes-error-code/)
- [Trane 3 Flash Pressure Switch Fault — Detailed Diagnosis Guide](/posts/trane-3-flashes-pressure-switch/)
- [Trane 4 Flashes Error Code — Open High Limit Fix](/posts/trane-4-flashes-error-code/)
