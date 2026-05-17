---
title: "Weil-McLain E02 Error Code — Causes & Fix"
description: "What Weil-McLain E02 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T08:00:00Z
modDatetime: 2026-04-22T08:00:00Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - boiler
  - weil-mclain
---

## Weil-McLain E02 Error Code — What It Means

Weil-McLain error code E02 means the high-limit has tripped — the boiler's water temperature exceeded the high-limit setpoint and the limit control opened the burner circuit. On Weil-McLain ECO, Ultra, and GV-series boilers, E02 is a non-latching safety lockout that resets automatically once the water temperature drops below the limit reset point. However, if E02 appears repeatedly, something is driving boiler water temperature above the setpoint consistently. This is not normal operation; the boiler should modulate and maintain temperature within setpoint range.

[Jump to Fix](#fix)

## Common Causes

- **No circulation / failed circulator pump** — If the circulator pump has failed or a zone valve is stuck closed, heat can't leave the boiler. Water temperature climbs rapidly until the high-limit trips.
- **Blocked or air-locked system** — Air pockets in the hydronic distribution system prevent water from circulating properly, trapping heat in the boiler section and causing rapid temperature rise.
- **High-limit setpoint too low** — If the high-limit aquastat or the digital limit setpoint was changed to a value too close to the boiler's normal operating temperature, minor temperature overshoot trips E02.
- **Overfire condition** — Excessive gas input, stuck-open gas valve, or incorrect gas pressure can cause the boiler to fire harder than its heat exchanger can transfer, driving water temps above limit.

## Step-by-Step Fix {#fix}

1. **Confirm circulator pump operation** — With the boiler calling for heat, place your hand on the supply and return pipes. Supply should be significantly warmer than return, indicating flow. Listen for the pump. If no flow, check the pump and zone valves.
2. **Check for air in the system** — Listen for gurgling sounds in radiators or baseboard units. Use the system purge valves (Weil-McLain installs one on most applications) to purge air from the distribution loop.
3. **Verify the high-limit setpoint** — On the ECO series, the limit is adjustable via the control board display. A typical residential boiler runs 160–180°F supply; the high-limit should be set 15–20°F above the normal operating setpoint.
4. **Check gas pressure and input** — If the boiler fires at maximum rate continuously without modulating, gas pressure or gas valve drift may be causing overfire. This requires a licensed tech.
5. **Reset the system** — E02 auto-resets when water temperature falls below the limit reset point. After addressing circulation issues, the boiler should resume normal operation within 10–15 minutes.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Circulator pump | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-e02-error-code&k=Circulator+pump&tag=errorcodefixes-20) \| Match flange size and head pressure to original; Taco 007 is common on Weil-McLain installs |
| Zone valve | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-e02-error-code&k=Zone+valve&tag=errorcodefixes-20) \| Test each zone valve motor with a multimeter; replace if coil is open |
| High-limit aquastat (older models) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-e02-error-code&k=High-limit+aquastat+%28older+models%29&tag=errorcodefixes-20) \| Capillary-bulb type on older GV/WTGO boilers; replace if sensing element is damaged |
## When to Call a Pro

An overfire condition (boiler firing full-rate without modulating) requires a licensed gas tech to inspect the gas valve, check manifold pressure, and verify combustion. Don't diagnose or adjust gas components yourself.

## Related Articles

- [American Water Heater Error Codes — Complete Guide](/posts/american-water-heater-error-codes/)
- [AO Smith Water Heater 3 Flashes — What It Means and How to Fix It](/posts/ao-smith-water-heater-3-flashes/)
- [AO Smith Water Heater 4 Flashes — What It Means and How to Fix It](/posts/ao-smith-water-heater-4-flashes/)
- [A.O. Smith Water Heater Error Codes Guide](/posts/ao-smith-water-heater-error-codes/)
- [Bradford White Water Heater Error Code 1 — Pilot Outage Fix](/posts/bradford-white-error-code-1/)
