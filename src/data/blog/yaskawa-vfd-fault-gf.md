---
title: "Yaskawa VFD Fault GF — Causes & Fix"
description: "What Yaskawa GF means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T08:00:00Z
modDatetime: 2026-04-22T08:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
---

## Yaskawa VFD Fault GF — What It Means

Yaskawa fault GF means ground fault — the drive detected that output current is flowing to ground rather than returning through the motor windings normally. On Yaskawa V1000, A1000, and GA700 drives, GF is detected by comparing the sum of currents on all three output phases; in a normal motor circuit, they sum to zero. When a ground fault exists, current leaks to ground and the three-phase sum is non-zero. The drive trips immediately to protect both the motor and personnel from dangerous ground current. GF is almost always caused by damaged motor winding insulation or a damaged output cable.

[Jump to Fix](#fix)

## Common Causes

- **Failed motor winding insulation** — The most common cause. Heat cycling, moisture, and age cause motor winding insulation to break down. When insulation fails between a winding and the motor frame, current flows to ground.
- **Damaged output cable** — A motor cable with nicked or worn insulation at a conduit entry point, a cable tray edge, or a bend radius violation can short a conductor to the conduit or cable tray.
- **Moisture ingress into motor or junction box** — Water in the motor terminal box bridges the winding terminals to ground. Common on outdoor or wash-down applications.
- **High capacitive leakage current** — Very long motor cable runs (over 100 feet) with VFD switching frequencies can produce enough capacitive leakage current to false-trigger GF. Reduce switching frequency or install an output reactor.

## Step-by-Step Fix {#fix}

1. **Disconnect the motor cable at the drive output** — Isolate the drive from the motor. Reset the fault and attempt to run the drive with no output connected (if the drive allows no-load operation). If GF disappears, the fault is in the motor or cable.
2. **Test motor insulation** — With the motor disconnected, use a 500V megohm meter to test each winding lead to ground. Minimum acceptable: 1 MΩ. Below 100 kΩ = failed insulation, replace motor.
3. **Inspect the output cable** — Trace the motor cable from drive to motor. Look for pinch points, conduit entry damage, or any location where the outer jacket shows damage.
4. **Test the cable insulation** — With motor disconnected, test each conductor of the output cable to ground with a megohm meter. Any conductor below 1 MΩ to ground = damaged cable.
5. **Reset the system** — After replacing the faulty component, reconnect, reset the fault, and run the drive with load monitoring. Confirm current on all three phases is balanced.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor (replacement) | [Amazon](https://www.amazon.com/s?i=industrial&k=Motor+%28replacement%29&tag=errorcodefixes-20) \| Required if winding insulation tests below acceptable threshold |
| VFD-rated output cable (shielded) | [Amazon](https://www.amazon.com/s?i=industrial&k=VFD-rated+output+cable+%28shielded%29&tag=errorcodefixes-20) \| Replace if any conductor shows insulation damage |
| Output reactor (line choke) | [Amazon](https://www.amazon.com/s?i=industrial&k=Output+reactor+%28line+choke%29&tag=errorcodefixes-20) \| Install if GF is caused by long cable capacitive leakage |
## When to Call a Pro

Megohm meter testing and motor insulation analysis requires proper equipment and safety procedures. If the motor tests marginal (500 kΩ to 1 MΩ), a motor shop can do a more thorough surge test and rewinding assessment.

## Related Articles

- [Yaskawa A1000 OC Fault — Overcurrent](/posts/yaskawa-a1000-fault-oc/)
- [Yaskawa A1000 Fault UV1, DC Bus Undervoltage Causes & Fix](/posts/yaskawa-a1000-fault-uv1/)
- [Yaskawa A1000 Fault Code OC — Overcurrent Diagnosis & Fix](/posts/yaskawa-a1000-oc-fault-code/)
- [Yaskawa GA700 OC Fault — Overcurrent Fix](/posts/yaskawa-ga700-fault-oc/)
- [Yaskawa GA700 Fault UV1 — Main Circuit Undervoltage Causes & Fix](/posts/yaskawa-ga700-fault-uv1/)
