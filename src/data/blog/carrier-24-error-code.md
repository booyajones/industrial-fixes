---
title: "Carrier 24 Error Code — Causes & Fix"
description: "What Carrier 24 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T08:00:00Z
modDatetime: 2026-04-22T08:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - carrier
money_part: "3A mini blade fuse (AGC-3 or ATC-3)"
most_likely_cause: "Short circuit in the thermostat wiring"
---

## Carrier 24 Error Code — What It Means

Carrier fault code 24 means the secondary voltage fuse is open. The control board flashes 2 long, 4 short. The furnace control operates on 24VAC (step-down from the 120V line through a transformer). A 3-amp fuse on the board protects this secondary circuit. When the fuse blows, the board loses its control voltage and shuts everything down. Code 24 tells you the fuse blew — not why it blew. Finding the root cause before replacing the fuse is the entire job.

[Jump to Fix](#fix)

## Common Causes

- **Short circuit in the thermostat wiring** — The most common cause. A wire that has worn through its insulation and shorted to the metal chassis grounds the 24V circuit and blows the fuse. Check the R and C wires at the thermostat and at the furnace terminals.
- **Miswired zone valve or accessory** — Zone valves, humidifiers, and UV systems all tap into the 24V circuit. A wiring error on any of these can pull enough current to blow the fuse.
- **Shorted transformer secondary** — Less common, but if the transformer itself has a winding fault, its internal current exceeds 3A and blows the fuse at startup.
- **Stuck contactor or relay coil** — An HVAC accessory relay with a shorted coil can draw enough current to blow the control fuse.

## Step-by-Step Fix {#fix}

1. **Locate the fuse on the control board** — The 3A fuse is usually a mini automotive blade type mounted in a visible holder on the board. Confirm it's blown (filament broken, or reads open on a multimeter).
2. **Do NOT replace it yet** — Replacing the fuse without finding the short just blows the new fuse immediately. Skip to the next steps first.
3. **Disconnect all thermostat wires and accessories** — Unplug the thermostat wire bundle from the board terminals. Disconnect any humidifier, zone valves, or UV light from the 24V circuit. Now replace the fuse.
4. **Restore power and observe** — If the new fuse holds, you've isolated the short to the thermostat wiring or an accessory. Reconnect accessories one at a time until the fuse blows again to identify the culprit.
5. **Reset the system** — Once the short is repaired, the fuse should hold indefinitely. Power cycle the furnace and confirm code 24 is gone.

## Parts Often Needed

| Part | Notes |
|------|-------|
| 3A mini blade fuse (AGC-3 or ATC-3) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-carrier-24-error-code&k=3A+mini+blade+fuse+%28AGC-3+or+ATC-3%29&tag=errorcodefixes-20) \| Carry a pack of 5; cheap insurance |
| Thermostat wire (18/5 or 18/8) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-carrier-24-error-code&k=Thermostat+wire+%2818%2F5+or+18%2F8%29&tag=errorcodefixes-20) \| Replace if the old run has any worn insulation |
| 40VA furnace transformer | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-carrier-24-error-code&k=40VA+furnace+transformer&tag=errorcodefixes-20) \| Replace if the transformer itself is shorted (measure secondary: should be ~28VAC no-load) |
## When to Call a Pro

If you've disconnected everything and the fuse still blows immediately on power-up, the transformer or control board has an internal fault. At that point the diagnostics get component-level and a tech with the right meter is faster than trial-and-error.

## Related Articles

- [Carrier 11 Error Code — Causes & Fix](/posts/carrier-11-error-code/)
- [Carrier 12 Error Code — Causes & Fix](/posts/carrier-12-error-code/)
- [Carrier 13 Error Code — Limit Switch Lockout Fix](/posts/carrier-13-error-code/)
- [Carrier 13 Soft Lockout — What's Different from Hard Lockout](/posts/carrier-13-soft-lockout/)
- [Carrier 14 Error Code — Causes & Fix](/posts/carrier-14-error-code/)

## See Also

- [Carrier Infinity 24VNA6 Heat Pump Error Codes - Greenspeed Fault Reference](/posts/carrier-24vna6-error-codes/)
- [Carrier Infinity Zoning System Error Codes — Complete Guide](/posts/carrier-infinity-zoning-error/)
- [Carrier Heat Pump E5 Error Code — Defrost Fault: Causes & Fix](/posts/carrier-heat-pump-e5-error-code/)
- [Carrier 23 Error Code — Draft Safeguard Switch Fault](/posts/carrier-23-error-code/)
