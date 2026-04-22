---
title: "York 2 Flashes Error Code — Causes & Fix"
description: "What York 2 flashes means on a furnace, why the pressure switch is stuck closed, and how to fix it."
pubDatetime: 2026-04-22T10:00:00Z
modDatetime: 2026-04-22T10:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - york
---

## York 2 Flashes Error Code — What It Means

Two flashes on a York furnace diagnostic LED indicates the pressure switch is stuck in the closed position when it should be open. At the beginning of a heat cycle, the control board checks that the pressure switch is open (meaning no draft is present) before starting the induced draft motor. If the switch reads closed before the inducer starts, the board interprets this as a stuck or shorted switch and locks out the ignition sequence.

[Jump to Fix](#fix)

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
| [Pressure switch](https://www.amazon.com/s?k=Pressure%20switch&tag=errorcodefixe-20) | Match York/Johnson Controls part number exactly |
| [Pressure switch hose](https://www.amazon.com/s?k=Pressure%20switch%20hose&tag=errorcodefixe-20) | 1/4" ID; replace if water-logged or cracked |
| [Condensate trap kit](https://www.amazon.com/s?k=Condensate%20trap%20kit&tag=errorcodefixe-20) | Required if condensate is backing up |
| [Control board](https://www.amazon.com/s?k=Control%20board&tag=errorcodefixe-20) | Replace only if relay is confirmed stuck |

## When to Call a Pro

If water contamination is recurring, the condensate drainage system needs a thorough inspection by a licensed HVAC technician to prevent repeated lockouts and potential heat exchanger corrosion.
