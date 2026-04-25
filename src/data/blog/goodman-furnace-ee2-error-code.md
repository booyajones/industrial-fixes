---
title: "Goodman Furnace EE2 Error Code — Causes & Fix"
description: "What Goodman furnace EE2 error code means, why it appears, and how to diagnose and fix it step by step."
pubDatetime: 2026-04-22T13:00:00Z
modDatetime: 2026-04-22T13:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - goodman
---

## Goodman Furnace EE2 Error Code — What It Means

The Goodman **EE2 error code** appears on the communicating thermostat or control board display of newer Goodman furnaces using the ComfortNet or similar communicating control system. EE2 indicates a **communication error** — the furnace control board has lost communication with the system (typically the thermostat or the communicating system bus). Unlike the traditional blink codes, EE-series codes appear on digital displays and indicate a system-level control communication problem rather than a mechanical fault.

[Jump to Fix](#fix)

## Common Causes

- **Loose or damaged communication wiring** — The low-voltage communication bus between the thermostat and the furnace control board has a loose terminal, broken wire, or damaged connector.
- **Thermostat firmware or compatibility issue** — A ComfortNet or communicating thermostat that has an incompatible firmware version or a failed communication chipset generates EE2 on the furnace.
- **Control board communication fault** — The furnace's main control board has a failed communication circuit, preventing it from receiving valid data from the thermostat or outdoor unit.
- **Power surge damage** — A voltage spike (lightning, grid transient) can damage the low-voltage communication circuitry on either the thermostat or control board without damaging anything else.

## Step-by-Step Fix {#fix}

1. **Check thermostat wiring connections** — Turn off the furnace breaker. Remove the thermostat from its base and inspect all wire connections. Re-seat any loose wires and confirm terminal screws are snug.
2. **Inspect furnace control board wiring** — At the furnace, check the low-voltage terminal strip. Look for corroded terminals, loose wires, or a cracked connector on the communication port.
3. **Test communication wire continuity** — With a multimeter, check continuity on each low-voltage wire between the thermostat and furnace. An open wire needs to be replaced.
4. **Power cycle the system** — Cut all power (breaker and thermostat) for 5 minutes, then restore. Many EE2 faults after a power surge clear with a full system reset.
5. **Try a conventional wiring mode** — If the thermostat supports it, switch to conventional (non-communicating) wiring mode as a test. If the furnace operates without EE2 in conventional mode, the communication chipset in the thermostat has failed.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Communicating thermostat | [Amazon](https://www.amazon.com/s?k=Communicating+thermostat&tag=errorcodefixes-20) \| Replace when thermostat communication circuit has failed |
| Furnace control board | [Amazon](https://www.amazon.com/s?k=Furnace+control+board&tag=errorcodefixes-20) \| Replace when board communication circuit fails and all wiring tests good |
| Low-voltage wiring (18/5 or 18/8) | [Amazon](https://www.amazon.com/s?k=Low-voltage+wiring+%2818%2F5+or+18%2F8%29&tag=errorcodefixes-20) \| Replace if wire continuity test shows any open conductors |
## When to Call a Pro

If EE2 persists after replacing the thermostat and all wiring tests good, the furnace control board's communication circuit has failed. Board replacement on newer communicating Goodman systems requires verifying firmware compatibility between the new board and the existing thermostat.

## Related Articles

- [Goodman 1 Flash Error Code — What It Means](/posts/goodman-1-flash-error-code/)
- [Goodman 2 Flash Error Code — Causes & Fix](/posts/goodman-2-flash-error-code/)
- [Goodman 3 Flash Error Code — Pressure Switch Stuck Open Fix](/posts/goodman-3-flash-error-code/)
- [Goodman 4 Flash Error Code — Causes & Fix](/posts/goodman-4-flash-error-code/)
- [Goodman 5 Flash Error Code — Causes & Fix](/posts/goodman-5-flash-error-code/)
