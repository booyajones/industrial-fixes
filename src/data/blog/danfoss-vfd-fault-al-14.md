---
title: "Danfoss VFD Fault AL 14 — Causes & Fix"
description: "What Danfoss VFD alarm AL 14 means, why ground fault triggers, and how to fix it step by step."
pubDatetime: 2026-04-22T12:00:00Z
modDatetime: 2026-04-22T12:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - danfoss
---

## Danfoss VFD Fault AL 14 — What It Means

Danfoss alarm AL 14 is a **Ground Fault** — the drive detected significant current leaking from one or more output phases to earth ground. On Danfoss FC-series drives (FC51, FC100, FC200, FC300, FC360), the drive monitors the sum of all three output phase currents; in a healthy system, the vector sum equals zero. When the sum is non-zero (current is flowing to ground), AL 14 trips the drive to protect personnel and equipment from ground fault hazards. Ground faults most commonly originate in the motor winding insulation or the output power cable.

[Jump to Fix](#fix)

## Common Causes

- **Deteriorated motor winding insulation** — The most common cause; moisture, heat, or age degrades the stator winding insulation, allowing current to leak to the motor frame/ground.
- **Damaged output cable** — A cable with compromised insulation (rodent damage, mechanical crushing, or UV degradation) leaks current to conduit or earth.
- **Motor contaminated with moisture or conductive debris** — Water intrusion into the motor terminal box or winding causes low-resistance paths to ground.
- **Drive internal fault** — Less commonly, the drive's own output stage has an IGBT with a gate-emitter insulation breakdown; this appears as a persistent AL 14 even with motor disconnected.

## Step-by-Step Fix {#fix}

1. **Isolate the motor** — Apply LOTO. Disconnect the motor cable at the drive's U/V/W output terminals. Attempt to reset the fault (power cycle or reset button).
2. **Test with motor disconnected** — If AL 14 clears with the motor disconnected, the fault is in the motor or the output cable — not the drive itself.
3. **Megger (insulation resistance) test the motor** — With the motor disconnected and cold, use a 500V or 1000V megohmmeter to measure insulation resistance between each motor terminal (U, V, W) and the motor frame/ground. A healthy motor reads >1 MΩ (ideally >100 MΩ). Below 1 MΩ indicates compromised insulation.
4. **Megger test the output cable** — With both ends disconnected, test insulation resistance from each conductor to the cable's outer jacket or shield. Values below 1 MΩ indicate damaged cable insulation.
5. **Test the drive with a different motor/cable** — If available, connect a known-good motor on a short temporary cable. If AL 14 doesn't trip, the original motor or cable is the fault source.
6. **Clear and return to service** — After repairs, reconnect the verified good motor/cable, power cycle the drive, and confirm AL 14 doesn't recur during a low-speed test run.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor (rewound or replacement) | [Amazon](https://www.amazon.com/s?i=industrial&k=Motor+%28rewound+or+replacement%29&tag=errorcodefixes-20) \| If insulation resistance is below 1 MΩ |
| Output power cable | [Amazon](https://www.amazon.com/s?i=industrial&k=Output+power+cable&tag=errorcodefixes-20) \| Shielded, rated for VFD output; replace if megger test shows insulation damage |
## When to Call a Pro

If AL 14 persists with the motor disconnected, the drive itself has a faulty output stage. Danfoss IGBT replacement requires specialized soldering and testing equipment. Contact Danfoss service or a certified drive repair shop — do not attempt internal drive repair without proper training.

## Related Articles

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS310 Fault 3130 — Causes & Fix](/posts/abb-acs310-fault-3130/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)
