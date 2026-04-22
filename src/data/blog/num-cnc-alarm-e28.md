---
title: "NUM CNC Alarm E28 — Causes & Fix"
description: "What NUM CNC Alarm E28 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - cnc
  - num
---

## NUM CNC Alarm E28 — What It Means

Alarm E28 on NUM CNC controls (NUM 1060, 1080, and Axium series) indicates a drive communication error — the NUM control lost communication with one or more of the servo drive modules. NUM uses a high-speed serial link between the NCU (Numerical Control Unit) and drive amplifiers; E28 fires when this communication is interrupted or a drive stops responding.

[Jump to Fix](#fix)

## Common Causes

- **Communication cable fault** — The serial link cable between the NUM control and the drive cabinet has been damaged or disconnected. High vibration and heat exposure can degrade these cables over time.
- **Drive module power supply fault** — If the DC bus or 24V supply to a drive module fails, the drive stops communicating and E28 is generated for that axis.
- **Drive module failure** — A failed servo amplifier module stops participating in the communication bus, causing E28 for the affected axis.
- **Control board (NCU) communication port failure** — The NUM NCU's communication output circuit has failed.

## Step-by-Step Fix {#fix}

1. **Full power cycle** — Turn off main disconnect, wait 60 seconds, power up. A clean power cycle resolves transient communication faults in a significant number of cases.
2. **Check drive module status LEDs** — Each NUM drive module has status indicators. A drive showing a fault LED is the one that's not communicating.
3. **Inspect communication cables** — Check the serial link cabling between the NUM NCU and drive cabinet for visible damage and secure connections at both ends.
4. **Check 24V power supply to drives** — Verify 24V control power to the drive modules is within spec (±5%). A sagging 24V supply causes communication dropouts.
5. **Contact NUM service** — E28 that doesn't clear after power cycle requires NUM-trained service with NUM diagnostic software for drive communication diagnostics.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [Serial link communication cable](https://www.amazon.com/s?k=Serial%20link%20communication%20cable&tag=errorcodefixe-20) | NUM-specific — replace if damaged |
| [24V power supply](https://www.amazon.com/s?k=24V%20power%20supply&tag=errorcodefixe-20) | Replace if voltage is marginal |
| [NUM servo drive module](https://www.amazon.com/s?k=NUM%20servo%20drive%20module&tag=errorcodefixe-20) | Replace if module has internal fault |

## When to Call a Pro

NUM CNC systems are less common in the US than Fanuc or Siemens; NUM-trained service engineers are specialized. Contact NUM directly for authorized service referrals.
