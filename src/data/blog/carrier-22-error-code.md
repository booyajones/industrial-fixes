---
title: "Carrier 22 Error Code — Causes & Fix"
description: "What Carrier error code 22 means, what causes the LSOM stall fault on single-stage furnaces, and how to fix it."
pubDatetime: 2026-04-22T10:00:00Z
modDatetime: 2026-04-22T10:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - carrier
---

## Carrier 22 Error Code — What It Means

Carrier fault code 22 indicates a limit device lockout on a single-stage furnace — sometimes described in older Carrier documentation as an LSOM (Limit Switch Open Multiple times) stall. The control board has detected that the high-limit switch opened three or more times during a single heating cycle. After repeated limit trips, the board locks out and displays code 22 to signal that the system cannot safely continue heating until the root cause is resolved.

[Jump to Fix](#fix)

## Common Causes

- **Restricted airflow** — A clogged filter, blocked return grille, or closed supply registers prevents adequate airflow across the heat exchanger, causing it to overheat and repeatedly open the limit.
- **Oversized furnace / short cycling** — If the furnace is significantly oversized for the space, short run cycles can cause rapid heat buildup with insufficient blower time to dissipate it.
- **Weak or failed blower motor** — A motor running below rated RPM due to a bad capacitor or worn bearings moves less air, leading to heat exchanger overtemperature.
- **Faulty or stuck high-limit switch** — A limit switch that opens at too low a temperature (due to calibration drift or physical damage) will trigger code 22 even with proper airflow.

## Step-by-Step Fix {#fix}

1. **Replace the air filter** — Confirm the filter is the correct size and MERV rating. A filter that is too restrictive is as problematic as a dirty one.
2. **Check all supply and return registers** — Open any registers that are closed. Ensure furniture, rugs, and debris are not blocking return air grilles.
3. **Inspect the blower motor and capacitor** — Power off the furnace. Spin the blower wheel by hand to confirm it rotates freely. Test the run capacitor with a capacitor meter; replace if the reading is more than 10% below the rated µF value.
4. **Test the high-limit switch** — With power off, use a multimeter on continuity mode across the limit switch terminals. It should show continuity (closed) at room temperature. If it is open at room temperature, replace the switch.
5. **Reset the lockout** — Cut 120V power to the furnace for 30 seconds to clear the code 22 lockout. Restore power and run a full heat cycle while monitoring for limit trips.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Air filter | [Amazon](https://www.amazon.com/dp/B0CLBFXLYJ?ascsubtag=ecf-carrier-22-error-code&tag=errorcodefixes-20) \| Most common fix; replace first |
| Blower run capacitor | [Amazon](https://www.amazon.com/dp/B01M05L7B3?ascsubtag=ecf-carrier-22-error-code&tag=errorcodefixes-20) \| Match µF and voltage exactly to OEM spec |
| High-limit switch | [Amazon](https://www.amazon.com/dp/B0BN3TRG9R?ascsubtag=ecf-carrier-22-error-code&tag=errorcodefixes-20) \| Verify OEM part number; temperature rating varies by model |
| Control board | [Amazon](https://www.amazon.com/s?k=Control+board&tag=errorcodefixes-20) \| Replace only if board relay is confirmed faulty |
## When to Call a Pro

If the limit switch resets but opens again within one heating cycle and airflow is verified good, a cracked heat exchanger may be allowing combustion gases to recirculate. This is a carbon monoxide hazard — do not operate the furnace until a licensed technician inspects the heat exchanger.

## Related Articles

- [Carrier 11 Error Code — Causes & Fix](/posts/carrier-11-error-code/)
- [Carrier 12 Error Code — Causes & Fix](/posts/carrier-12-error-code/)
- [Carrier 13 Error Code — Limit Switch Lockout Fix](/posts/carrier-13-error-code/)
- [Carrier 13 Soft Lockout — What's Different from Hard Lockout](/posts/carrier-13-soft-lockout/)
- [Carrier 14 Error Code — Causes & Fix](/posts/carrier-14-error-code/)

## See Also

- [Carrier VRF System Error Codes Guide](/posts/carrier-vrf-error-codes/)
- [Carrier 21 Error Code — Gas Heating Lockout Fix](/posts/carrier-21-error-code/)
- [Carrier 58CVA Furnace Error Codes — Fault Code Diagnostic Guide](/posts/carrier-58cva-error-codes/)
- [Carrier Heat Pump E4 Error Code — Causes & Fix](/posts/carrier-heat-pump-e4-error-code/)
