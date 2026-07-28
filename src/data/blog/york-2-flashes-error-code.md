---
title: "York 2 Flashes Error Code — Causes & Fix"
description: "What York 2 flashes means on a furnace, why the pressure switch is stuck closed, and how to fix it."
pubDatetime: 2026-04-22T10:00:00Z
modDatetime: 2026-04-22T10:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - york
money_part: "Pressure switch"
most_likely_cause: "Pressure switch contacts welded closed"
---

## What this code means
Two flashes on a York furnace diagnostic LED indicates the pressure switch is stuck in the closed position when it should be open. At the beginning of a heat cycle, the control board checks that the pressure switch is open (meaning no draft is present) before starting the induced draft motor. If the switch reads closed before the inducer starts, the board interprets this as a stuck or shorted switch and locks out the ignition sequence.

## Common Causes

- **Pressure switch contacts welded closed** — Electrical arcing over time can fuse the switch contacts in the closed position.
- **Water in the pressure switch hose or switch body** — Condensate from the flue can back up into the rubber hose and into the switch, holding the diaphragm in the closed position.
- **Miswired pressure switch** — An incorrectly wired switch (normally-closed port used instead of normally-open) can appear stuck closed at startup.
- **Inducer running when it shouldn't** — A board with a stuck inducer relay may keep the inducer running, which closes the pressure switch before the board's startup check.

## Step-by-Step Fix {#fix}

1. **Disconnect power and inspect the pressure switch hose** — Remove the rubber hose from the switch port and drain any visible water. Blow through the hose to confirm it is clear.
2. **Test the pressure switch with a multimeter** — With the furnace off and the inducer not running, check continuity across the pressure switch. If it reads closed (continuity), the switch is stuck — replace it.
3. **Check for water in the condensate trap (90+ AFUE furnaces)** — On high-efficiency furnaces, a blocked condensate trap can push water back into the inducer and up the pressure hose. Clear the trap and drain the hose.
4. **Inspect control board for stuck inducer relay** — If the inducer is running with no heat call and no power cycle change, the board relay may be stuck. Replace the board.
5. **Reset and confirm** — Restore power and watch the startup sequence. The pressure switch LED indicator (if equipped) should be off at startup; it closes only after the inducer reaches speed.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-york-2-flashes-error-code&tag=errorcodefixes-20) \| Match York/Johnson Controls part number exactly |
| Pressure switch hose | [Amazon](https://www.amazon.com/dp/B0CPTHML1N?ascsubtag=ecf-york-2-flashes-error-code&tag=errorcodefixes-20) \| 1/4" ID; replace if water-logged or cracked |
| Condensate trap kit | [Amazon](https://www.amazon.com/dp/B077J4Y763?ascsubtag=ecf-york-2-flashes-error-code&tag=errorcodefixes-20) \| Required if condensate is backing up |
| Control board | [Amazon](https://www.amazon.com/s?k=Control+board&tag=errorcodefixes-20) \| Replace only if relay is confirmed stuck |
## When to Call a Pro

If water contamination is recurring, the condensate drainage system needs a thorough inspection by a licensed HVAC technician to prevent repeated lockouts and potential heat exchanger corrosion.
