---
title: "Hoshizaki Ice Machine E1 Error Code — Water Inlet Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-03-13T08:00:00Z
modDatetime: 2024-03-13T08:00:00Z
slug: hoshizaki-e1-error-code
featured: true
draft: false
tags:
  - commercial-refrigeration
  - hoshizaki
  - ice-machine
  - water-inlet
  - food-service
description: "Hoshizaki E1 error code means the ice machine has a water inlet problem. This guide covers float switch, inlet valve, and water supply fixes for Hoshizaki commercial ice makers."
---

## Error Code: Hoshizaki E1

**What it means:** The E1 error code on a Hoshizaki commercial ice machine indicates a water supply or water inlet malfunction. Specifically, the machine's control board detected that the water trough did not fill to the correct level within the allotted fill time. Hoshizaki's board starts timing when it opens the water inlet valve — if the float switch inside the reservoir doesn't signal "full" before the timer expires, it halts the freeze cycle and displays E1.

This code is extremely common in commercial kitchens, particularly in high-use environments where mineral scale builds up quickly in the water system. E1 can also appear after water supply work, filter changes, or any service that interrupts the water line to the ice machine.

## Common Causes

- **Partially closed or restricted water supply valve** — The ball valve or saddle valve feeding the ice machine may be partially closed after service or maintenance. Even 20% restriction can prevent fill within the timer window.
- **Clogged water inlet valve strainer** — Hoshizaki water inlet valves have a small mesh strainer at the inlet port. In areas with hard water or sediment, this strainer clogs and drastically reduces flow. The strainer is cleanable without replacing the valve.
- **Failed water inlet valve solenoid** — The solenoid coil in the inlet valve can burn out or the plunger can stick from mineral deposits. When the valve doesn't open fully on command, the trough doesn't fill.
- **Stuck or scaled float switch** — The float switch in the water reservoir rises with the water level to signal "full." Mineral scale can freeze the float in the down position, causing the board to never receive the fill confirmation even when the trough is full.
- **Low water pressure from supply** — Hoshizaki machines require a minimum of 20 PSI (and recommend 20–80 PSI) of incoming water pressure. Pressure below 20 PSI causes slow fill. This is common in upper-floor restaurant installations or during high-demand periods.
- **Kinked or pinched water supply line** — The supply line behind or under the machine can kink, especially after the machine is moved for cleaning.

## Step-by-Step Fix {#step-by-step-fix}

1. **Check the water supply valve first.** Locate the shutoff valve on the water supply line feeding the ice machine. Confirm it is fully open — handle parallel to the pipe. This is the first thing any tech checks after E1 appears, because it's a zero-cost fix that resolves a surprising percentage of calls.

2. **Verify incoming water pressure.** Attach a water pressure gauge to the supply line (most techs use a gauge threaded to the inlet valve port after removing the supply line). Pressure should be between 20–80 PSI. Pressure below 20 PSI requires either a booster pump or a pressure regulator adjustment upstream.

3. **Inspect and clean the inlet valve strainer.** Turn off the water supply. Disconnect the water supply line at the inlet valve on the back of the machine. Use needle-nose pliers to remove the small mesh strainer from the inlet port. Rinse it under running water and use a stiff brush to remove scale. If the strainer is severely corroded or collapsed, replace it. Reinstall, reconnect the supply line, and restore water.

4. **Test the water inlet valve solenoid.** With the machine unplugged, disconnect the wiring harness from the inlet valve solenoid. Using a multimeter set to ohms, measure resistance across the two solenoid terminals. A healthy Hoshizaki inlet valve solenoid reads approximately 200–500 ohms. An open circuit (OL) confirms a failed solenoid — the valve assembly needs replacement. Hoshizaki water inlet valve **4A5375-02** is the correct OEM replacement for most KM and KML series machines (~$85 at commercial refrigeration suppliers).

5. **Inspect and free the float switch.** Open the front panel and locate the water trough reservoir. The float switch is a small buoyant plastic arm or ball connected to a microswitch. Look for visible scale deposits locking the float in place. With the machine unplugged, manually lift and lower the float — it should move freely. If it's seized, clean the pivot point with a descaling solution or vinegar. Use a multimeter to verify the float switch changes state when manually activated: continuity in the down position, no continuity (or vice versa, depending on model) when lifted.

6. **Replace the float switch if stuck or unresponsive.** Hoshizaki float switch **4A2734-01** fits most KM series machines (~$45 at parts suppliers). This is a straightforward swap — disconnect the wire leads, remove the mounting screw, and install the new unit.

7. **Check the water supply line for kinks.** Pull the machine forward (use a floor dolly — these units are heavy) and inspect the entire length of the supply line from wall valve to inlet valve. Any kink or sharp bend reduces flow significantly. Replace kinked sections with new braided stainless supply line.

8. **Run a full freeze cycle after repair.** After resolving the water supply issue, run the machine through a complete freeze and harvest cycle. Monitor the first 10 minutes to confirm the trough fills without E1 recurring. Hoshizaki's normal fill time is typically 3–5 minutes depending on machine size.

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Part Number | Typical Cost | Where to Buy |
|------|-------------|--------------|--------------|
| Water inlet valve | 4A5375-02 | $75-$100 | [Amazon](https://www.amazon.com/dp/B0CNFHW1ZJ?ascsubtag=ecf-hoshizaki-e1-error-code&tag=errorcodefixes-20) \| Parts Town |
| Float switch | 4A2734-01 | $40-$55 | [Amazon](https://www.amazon.com/dp/B005D4RFEM?ascsubtag=ecf-hoshizaki-e1-error-code&tag=errorcodefixes-20) \| Parts Town |
| Inlet valve strainer | 4A3237-01 | $8-$15 | Parts Town |
| Water supply line (braided SS, 6ft) | — | $12-$20 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-hoshizaki-e1-error-code&k=braided+stainless+water+supply+line+6ft&tag=errorcodefixes-20) \| Home Depot |

## Related Articles

- [Hoshizaki C-101BAH / C-201BAH Countertop Ice Maker Error Codes — Full Fault Guide](/posts/hoshizaki-c-101bah-error-codes/)
- [Hoshizaki DKM-500 Cube Dispenser Error Codes — Fault Code Diagnostic Guide](/posts/hoshizaki-dkm-500-error-codes/)
- [Hoshizaki E2 Error Code — Harvest Fault Fix](/posts/hoshizaki-e2-error-code/)
- [Hoshizaki E3 Error Code — Causes & Fix](/posts/hoshizaki-e3-error-code/)
- [Hoshizaki E4 Error Code — Causes & Fix](/posts/hoshizaki-e4-error-code/)
