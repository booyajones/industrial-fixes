---
title: "Carrier 32 Error Code — Causes & Fix"
description: "What Carrier error code 32 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T09:00:00Z
modDatetime: 2026-04-22T09:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - carrier
money_part: "Pressure switch"
---

## Carrier 32 Error Code — What It Means

Carrier fault code 32 indicates a pressure switch stuck in the closed (satisfied) position when it should be open. On startup, the control board checks that all pressure switches are open before energizing the inducer. If a pressure switch reads closed before the inducer starts, the board interprets this as a fault — either the switch has failed closed, there's a wiring short, or water in the pressure switch tubing is holding the diaphragm in the closed position. This is a safety check that prevents the furnace from running with a potentially blocked venting path.

[Jump to Fix](#fix)

## Common Causes

- **Waterlogged pressure switch tubing** — Condensate can back up into the rubber pressure switch hose, weighting the diaphragm and keeping the switch closed even without inducer pressure. Very common on high-efficiency 90%+ furnaces.
- **Failed pressure switch (stuck closed)** — The diaphragm or internal spring fails and the switch contacts weld closed. The switch reads closed regardless of inducer status.
- **Wiring short between pressure switch terminals** — A pinched or shorted wire creates a closed circuit the board misreads as a satisfied switch.
- **Incorrectly adjusted or wrong switch** — If a field-replaced switch has the wrong setpoint (too low), it closes at atmospheric pressure before the inducer creates any draft.

## Step-by-Step Fix {#fix}

1. **Check pressure switch hose for water** — Disconnect the small rubber tube from the pressure switch port. Tip it toward a rag and check for water. If water comes out, blow out the tube and the condensate drain path to clear the blockage.
2. **Test switch continuity before inducer starts** — With the furnace off, disconnect the wires from the pressure switch and use a multimeter to check continuity. A healthy switch should be open (OL) at rest. If it reads closed, the switch has failed and needs replacement.
3. **Inspect wiring for shorts** — Check the two wires going to the pressure switch. Look for pinch points near sheet metal edges or harness routing through tight areas. A short between the two terminals mimics a stuck-closed switch.
4. **Verify switch setpoint matches spec** — Cross-reference the pressure switch part number against the furnace model. An incorrect switch installed during a prior repair is a common cause of this fault.
5. **Reset and verify** — Restore wiring, cycle power, and confirm the furnace completes a full heat cycle without returning code 32.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-carrier-32-error-code&tag=errorcodefixes-20) \| Match exact part number — setpoint varies by model and BTU rating |
| Pressure switch tubing (rubber) | [Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-carrier-32-error-code&tag=errorcodefixes-20) \| Replace if cracked, kinked, or contaminated with residue |
| Inducer motor | [Amazon](https://www.amazon.com/dp/B00FDZ90B2?ascsubtag=ecf-carrier-32-error-code&tag=errorcodefixes-20) \| If inducer fails to create adequate draft, switch may never open |
## When to Call a Pro

If clearing the condensate path and replacing the pressure switch doesn't resolve the fault, the issue may be a blocked flue, failed inducer assembly, or cracked inducer housing — all of which require professional diagnosis and venting inspection.

## Related Articles

- [Carrier 11 Error Code — Causes & Fix](/posts/carrier-11-error-code/)
- [Carrier 12 Error Code — Causes & Fix](/posts/carrier-12-error-code/)
- [Carrier 13 Error Code — Limit Switch Lockout Fix](/posts/carrier-13-error-code/)
- [Carrier 13 Soft Lockout — What's Different from Hard Lockout](/posts/carrier-13-soft-lockout/)
- [Carrier 14 Error Code — Causes & Fix](/posts/carrier-14-error-code/)

## See Also

- [Carrier Error Code 58 — Causes & Fix](/posts/carrier-58-error-code/)
- [Carrier 13 Soft Lockout — What's Different from Hard Lockout](/posts/carrier-13-soft-lockout/)
- [Carrier Geothermal Heat Pump Error Codes Guide](/posts/carrier-geothermal-error-codes/)
- [Carrier Error Code 24 — Secondary Voltage Fuse Open](/posts/carrier-24-soft-lockout/)
