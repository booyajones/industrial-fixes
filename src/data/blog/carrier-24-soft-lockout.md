---
title: "Carrier Error Code 24 — Secondary Voltage Fuse Open"
description: "Carrier fault code 24 means the 3-amp secondary fuse on the IFC board has blown. Here's what caused it and how to replace it without burning through another fuse."
pubDatetime: 2026-04-22T18:00:00Z
modDatetime: 2026-04-22T18:00:00Z
author: "ErrorCodeFixes"
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

| [Cause](https://www.amazon.com/s?k=Cause&tag=errorcodefixe-20) | How Common |
|---|---|
| [Wiring short on thermostat wire (bare wire touching metal)](https://www.amazon.com/s?k=Wiring%20short%20on%20thermostat%20wire%20(bare%20wire%20touching%20metal)&tag=errorcodefixe-20) | Very common |
| [Shorted humidifier control board](https://www.amazon.com/s?k=Shorted%20humidifier%20control%20board&tag=errorcodefixe-20) | Common |
| [Shorted zone controller or relay board](https://www.amazon.com/s?k=Shorted%20zone%20controller%20or%20relay%20board&tag=errorcodefixe-20) | Common |
| [Shorted gas valve coil](https://www.amazon.com/s?k=Shorted%20gas%20valve%20coil&tag=errorcodefixe-20) | Occasional |
| [Wiring pinched by furnace door](https://www.amazon.com/s?k=Wiring%20pinched%20by%20furnace%20door&tag=errorcodefixe-20) | Occasional |
| [Faulty IFC board (rare internal short)](https://www.amazon.com/s?k=Faulty%20IFC%20board%20(rare%20internal%20short)&tag=errorcodefixe-20) | Rare |

## How to Find and Fix the Short

**Step 1 — Replace the fuse first.** Locate the 3-amp ATC/ATO automotive fuse on the IFC board (usually near the transformer wiring). Replace with an identical 3-amp fuse. Do not upsize.

**Step 2 — Disconnect accessories before restarting.** Unplug the humidifier, disconnect zone controllers, and remove the thermostat wire from the "R" and "C" terminals on the IFC. Leave only the furnace's own internal wiring connected.

**Step 3 — Power on the furnace.** If the fuse holds with accessories disconnected, the short is in your accessories or thermostat wiring. Reconnect one device at a time, powering on after each, until the fuse blows again — that's your culprit.

**Step 4 — Inspect thermostat wiring.** Run the thermostat wire through conduit? Check where it enters and exits. Bare copper touching a metal stud or edge will short immediately.

**Step 5 — Test the gas valve coil.** Disconnect the two wires going to the gas valve and measure resistance. A shorted coil will read very low (below 10 ohms). Normal is 40–80 ohms.

## Parts Needed

| Part | Cost |
|---|---|
| [3-amp ATO/ATC fuse (pack)](https://www.amazon.com/s?k=3-amp%20ATO%2FATC%20fuse%20(pack)&tag=errorcodefixe-20) | $3–8 |
| [Gas valve](https://www.amazon.com/s?k=Gas%20valve&tag=errorcodefixe-20) | $80–200 |
| [Humidifier control board](https://www.amazon.com/s?k=Humidifier%20control%20board&tag=errorcodefixe-20) | $30–80 |
| [IFC board (if internal fault)](https://www.amazon.com/s?k=IFC%20board%20(if%20internal%20fault)&tag=errorcodefixe-20) | $100–300 |

## Pro Tip

Fuses don't blow for no reason. Every time you replace a fuse without finding the short, you risk burning out the transformer or the IFC board. Spend the extra 15 minutes tracing the short before you close the furnace back up — it will save you a $200+ board replacement.

## Difference from Code 14

Code 24 is **secondary fuse open** (24V control circuit). Code 14 is **ignition lockout** (failed to light after multiple tries). Don't confuse them — code 24 is always an electrical/wiring issue, never a gas or ignition issue.
