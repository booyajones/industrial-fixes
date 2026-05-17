---
title: "Carrier Error Code 24 — Secondary Voltage Fuse Open"
description: "Carrier fault code 24 means the 3-amp secondary fuse on the IFC board has blown. Here's what caused it and how to replace it without burning through another fuse."
pubDatetime: 2026-04-22T18:00:00Z
modDatetime: 2026-04-22T18:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - carrier
  - furnace
  - hvac
  - error-code
---

## Carrier Fault Code 24 — Secondary Voltage Fuse Open

Carrier fault code 24 indicates the **secondary circuit fuse on the Integrated Furnace Control (IFC) board has blown open**. The IFC uses a small 3-amp automotive-style fuse to protect the 24V control circuit. When this fuse blows, the furnace shuts down completely and won't restart.

## What the Secondary Circuit Powers

The 24V secondary circuit (powered by the furnace transformer) runs:
- Thermostat wiring
- Gas valve
- Contactor coils (on some systems)
- Zone controllers
- Humidifiers and other accessories

Any short circuit on these wires will blow the fuse.

## Why Fuse 24 Blows

| Cause | How Common |
|---|---|
| Wiring short on thermostat wire (bare wire touching metal) | Very common |
| Shorted humidifier control board | Common |
| Shorted zone controller or relay board | Common |
| Shorted gas valve coil | Occasional |
| Wiring pinched by furnace door | Occasional |
| Faulty IFC board (rare internal short) | Rare |

## How to Find and Fix the Short

**Step 1 — Replace the fuse first.** Locate the 3-amp ATC/ATO automotive fuse on the IFC board (usually near the transformer wiring). Replace with an identical 3-amp fuse. Do not upsize.

**Step 2 — Disconnect accessories before restarting.** Unplug the humidifier, disconnect zone controllers, and remove the thermostat wire from the "R" and "C" terminals on the IFC. Leave only the furnace's own internal wiring connected.

**Step 3 — Power on the furnace.** If the fuse holds with accessories disconnected, the short is in your accessories or thermostat wiring. Reconnect one device at a time, powering on after each, until the fuse blows again — that's your culprit.

**Step 4 — Inspect thermostat wiring.** Run the thermostat wire through conduit? Check where it enters and exits. Bare copper touching a metal stud or edge will short immediately.

**Step 5 — Test the gas valve coil.** Disconnect the two wires going to the gas valve and measure resistance. A shorted coil will read very low (below 10 ohms). Normal is 40–80 ohms.

## Parts Needed

| Part | Cost |
|---|---|
| 3-amp ATO/ATC fuse (pack) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-carrier-24-soft-lockout&k=3-amp+ATO%2FATC+fuse+%28pack%29&tag=errorcodefixes-20) \| $3–8 |
| Gas valve | [Amazon](https://www.amazon.com/dp/B0015KAHHA?ascsubtag=ecf-carrier-24-soft-lockout&tag=errorcodefixes-20) \| $80–200 |
| Humidifier control board | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?ascsubtag=ecf-carrier-24-soft-lockout&tag=errorcodefixes-20) \| $30–80 |
| IFC board (if internal fault) | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?ascsubtag=ecf-carrier-24-soft-lockout&tag=errorcodefixes-20) \| $100–300 |
## Pro Tip

Fuses don't blow for no reason. Every time you replace a fuse without finding the short, you risk burning out the transformer or the IFC board. Spend the extra 15 minutes tracing the short before you close the furnace back up — it will save you a $200+ board replacement.

## Difference from Code 14

Code 24 is **secondary fuse open** (24V control circuit). Code 14 is **ignition lockout** (failed to light after multiple tries). Don't confuse them — code 24 is always an electrical/wiring issue, never a gas or ignition issue.

## Related Articles

- [Carrier 11 Error Code — Causes & Fix](/posts/carrier-11-error-code/)
- [Carrier 12 Error Code — Causes & Fix](/posts/carrier-12-error-code/)
- [Carrier 13 Error Code — Limit Switch Lockout Fix](/posts/carrier-13-error-code/)
- [Carrier 13 Soft Lockout — What's Different from Hard Lockout](/posts/carrier-13-soft-lockout/)
- [Carrier 14 Error Code — Causes & Fix](/posts/carrier-14-error-code/)
