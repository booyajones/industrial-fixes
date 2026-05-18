---
title: "Trane XV20i Error Code 79 — Causes & Fix"
description: "What Trane XV20i error code 79 means, why communication faults occur, and how to diagnose and fix it step by step."
pubDatetime: 2026-04-22T13:00:00Z
modDatetime: 2026-04-22T13:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - trane
---

## Trane XV20i Error Code 79 — What It Means

Trane **error code 79** on the XV20i variable-speed heat pump means a **communication fault** — the outdoor unit is not receiving valid communications from the ComfortLink II thermostat or the air handler/furnace control board. The XV20i uses a proprietary two-wire communicating system (Trane's ComfortLink II or Nexia system). Code 79 indicates the outdoor unit dropped off the communication bus, which typically prevents the system from operating in heating or cooling mode.

[Jump to Fix](#fix)

## Common Causes

- **Damaged or loose communication wiring** — The two-wire communication bus (typically terminals C and AB or the specific terminals per your wiring diagram) is broken, corroded, or improperly terminated.
- **Failed ComfortLink II thermostat** — The thermostat's communication circuit has malfunctioned and is no longer transmitting a valid signal to the outdoor unit.
- **Outdoor control board failure** — The outdoor unit's main control board communication chip has failed, often from a lightning strike or power surge.
- **Air handler/furnace board failure** — On split systems, the air handler board is the communication hub; its failure cascades to code 79 on the outdoor unit.

## Step-by-Step Fix {#fix}

1. **Check all communication wire connections** — Power everything down. Inspect the communication wire terminals at the thermostat, air handler, and outdoor unit. Tighten all screws; look for corroded or broken wire ends.
2. **Verify communication wire integrity** — Use a multimeter to check continuity on each communication wire between units. Any open circuit indicates a wire break that must be repaired.
3. **Reset the entire system** — Shut off all breakers (thermostat, air handler, outdoor unit) for 5 full minutes. Restore in order: air handler first, then outdoor unit, then thermostat. Allow 3 minutes for the network to re-establish.
4. **Check for fault codes at the air handler** — Pull the air handler's fault code LED sequence. A separate fault there helps narrow down whether the problem is in the air handler board or the wiring.
5. **Swap test the thermostat** — If wiring checks out and code 79 persists, temporarily substitute a known-good ComfortLink II thermostat. If code 79 clears, the thermostat's communication board has failed.

## Parts Often Needed

| Part | Notes |
|------|-------|
| ComfortLink II thermostat | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-trane-error-code-79&k=ComfortLink+II+thermostat&tag=errorcodefixes-20) \| Replace when thermostat communication circuit has failed |
| Outdoor unit control board | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?ascsubtag=ecf-trane-error-code-79&tag=errorcodefixes-20) \| Replace after lightning strike or if board shows burn marks |
| Communication wire (18-gauge, 2-conductor) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-trane-error-code-79&k=Communication+wire+%2818-gauge%2C+2-conductor%29&tag=errorcodefixes-20) \| Replace entire run if wire is damaged; don't splice communication wire |
| Air handler control board | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?ascsubtag=ecf-trane-error-code-79&tag=errorcodefixes-20) \| Replace if air handler shows its own separate communication fault |
## When to Call a Pro

Trane ComfortLink II system diagnostics require the Trane proprietary service tool (TechView) to read detailed fault history and communication bus diagnostics. If component swapping doesn't resolve code 79, an authorized Trane dealer with TechView can isolate the exact failure point.

## Related Articles

- [Trane 1 Flash Error Code — Causes & Fix](/posts/trane-1-flash-error-code/)
- [Trane Error Code 126 — Ignition Lockout Fix](/posts/trane-126-error-code/)
- [Trane 2 Flashes Error Code — Causes & Fix](/posts/trane-2-flashes-error-code/)
- [Trane 3 Flashes Error Code — Pressure Switch Fault Fix](/posts/trane-3-flashes-error-code/)
- [Trane 3 Flash Pressure Switch Fault — Detailed Diagnosis Guide](/posts/trane-3-flashes-pressure-switch/)

<!-- INTERNAL-LINK-AUTO -->
**Related:** [Rheem EcoNet A101 error code fix](/posts/rheem-econet-a101-error-code/)

