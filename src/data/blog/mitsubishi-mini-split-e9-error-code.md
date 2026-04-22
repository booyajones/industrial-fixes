---
title: "Mitsubishi Mini Split E9 Error Code — Causes & Fix"
description: "What Mitsubishi E9 outdoor thermistor 2 fault means, why it trips, and how to diagnose and fix it step by step."
pubDatetime: 2026-04-22T13:00:00Z
modDatetime: 2026-04-22T13:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - mini-split
  - mitsubishi
---

## Mitsubishi Mini Split E9 Error Code — What It Means

The Mitsubishi mini split **E9 error code** indicates a fault with the **outdoor unit's Thermistor 2** — specifically the outdoor discharge pipe thermistor (also called TH3 or the outdoor liquid pipe thermistor depending on model series). The outdoor unit uses multiple thermistors to monitor refrigerant temperatures during heating and cooling cycles. When E9 fires, the system determines that the thermistor reading is outside the valid operating range — either open (infinite resistance) or shorted (near-zero resistance) — and locks out to protect the compressor.

[Jump to Fix](#fix)

## Common Causes

- **Failed thermistor** — The thermistor element itself has failed — the resistance has drifted far outside the normal temperature-vs-resistance curve, or the probe is physically damaged.
- **Damaged thermistor wire** — The wire from the thermistor to the outdoor PCB connector has been pinched, cut, or has corroded terminals, creating an intermittent open or short.
- **Moisture in the connector** — Water intrusion at the outdoor PCB connector corrodes the thermistor terminals, causing resistance that reads as a fault.
- **Outdoor PCB failure** — Less commonly, the PCB's thermistor input circuit has failed and misreads the thermistor signal even when the thermistor is good.

## Step-by-Step Fix {#fix}

1. **Identify the thermistor location** — Power off the outdoor unit and open the service panel. Locate the TH3 (or Thermistor 2) connector on the outdoor PCB. Consult the unit's service manual for the exact thermistor location and pin assignment.
2. **Disconnect and test the thermistor** — Unplug the thermistor connector and measure resistance across the thermistor terminals with a multimeter. At 25°C (77°F), Mitsubishi outdoor thermistors typically read 10–15 kΩ. Check the service manual for the resistance-vs-temperature chart for your model. Open (OL) or very low resistance = thermistor failure.
3. **Inspect the thermistor wire and connector** — Look for pinched, cut, or damaged wiring. Check the connector pins for green corrosion or push-out pins. Clean corroded contacts with electrical contact cleaner.
4. **Test with a known-good thermistor** — If you have a matching thermistor available, substitute it temporarily. If E9 clears, the original thermistor has failed.
5. **Reset and verify** — After replacing the thermistor, restore power and press the RESET button on the indoor unit, or cycle the breaker. Allow the unit to run through a full operating cycle and confirm E9 does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Outdoor discharge pipe thermistor (TH3) | Verify OEM part number from model number; Mitsubishi thermistors are model-specific |
| Outdoor PCB | Replace if thermistor tests good but E9 persists after connector cleaning |
| Electrical contact cleaner | Use on connector pins before replacing parts if corrosion is visible |

## When to Call a Pro

If E9 persists after thermistor replacement and all connectors test clean, the outdoor PCB's thermistor input circuit has failed. PCB replacement on Mitsubishi outdoor units requires refrigerant system interlock checks — a certified HVAC technician should perform the swap.
