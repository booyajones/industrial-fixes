---
title: "Haas Alarm 123 — Causes & Fix"
description: "What Haas Alarm 123 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T18:00:00Z
modDatetime: 2026-04-22T18:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - cnc
  - haas
---

## Haas Alarm 123 — What It Means

Haas Alarm 123 indicates that the ATC arm is not in the home position — the tool changer arm failed to return to its rest/home position after a tool change or was found out-of-position during startup. The Haas control monitors the arm home proximity switch; if that switch isn't activated when expected, Alarm 123 fires and the machine locks out.

[Jump to Fix](#fix)

## Common Causes

- **ATC arm left mid-stroke** — A previous failed tool change left the arm in an extended or partially extended state. The machine was then powered off.
- **Proximity switch misalignment or failure** — The arm home sensor may be positioned incorrectly or has failed, causing it not to trigger even when the arm is physically home.
- **Pneumatic actuator failure** — The cylinder that retracts the arm hasn't fully pulled the arm back to the home position.
- **Mechanical obstruction** — A tool, chip, or debris prevents the arm from fully retracting to the home position.

## Step-by-Step Fix {#fix}

1. **Visually inspect the ATC arm position** — With E-stop engaged, look at the arm. Is it physically home or is it extended/partially extended?
2. **Follow the Haas manual recovery procedure** — If the arm is not home, follow the specific ATC arm recovery steps documented in the Haas Service Manual for your model (EC, VF, VM series have slightly different procedures).
3. **Check the arm home proximity switch** — In the Haas diagnostics display, monitor the ATC arm home input. It should read active when the arm is physically in the home position. A switch that doesn't activate when the arm is home = failed or misaligned switch.
4. **Check air pressure** — Verify shop air is at least 85 PSI at the machine's air inlet. Low air prevents full arm retraction.
5. **Power cycle and re-home** — After returning the arm to home, power cycle the machine and attempt a test tool change at reduced speed via MDI.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [ATC arm home proximity switch](https://www.amazon.com/s?k=ATC%20arm%20home%20proximity%20switch&tag=errorcodefixe-20) | Replace if not triggering when arm is physically home |
| [ATC arm actuator (pneumatic)](https://www.amazon.com/s?k=ATC%20arm%20actuator%20(pneumatic)&tag=errorcodefixe-20) | Replace if cylinder doesn't fully retract |

## When to Call a Pro

ATC arm adjustments and proximity switch calibration on Haas machines should be done by Haas service or a certified dealer to ensure correct arm-to-spindle alignment.
