---
title: "Panasonic Mini-Split H97 Error Code — Causes & Fix"
description: "What Panasonic mini-split H97 means, why communication fails, and how to fix it step by step."
pubDatetime: 2026-04-22T10:00:00Z
modDatetime: 2026-04-22T10:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - mini-split
  - panasonic
---

## Panasonic Mini-Split H97 Error Code — What It Means

H97 on a Panasonic mini-split system indicates a communication error between the indoor and outdoor units. Panasonic systems use a serial data line over the interconnecting wire to continuously exchange status, commands, and sensor data between units. When this communication link fails or becomes intermittent, the indoor unit displays H97 and shuts down to prevent operating in an unknown state.

[Jump to Fix](#fix)

## Common Causes

- **Broken or miswired interconnecting cable** — The signal conductor (terminal S on most Panasonic systems) carries the serial data. A break, loose terminal, or wrong wiring connection stops communication.
- **Outdoor unit not powered** — If the outdoor unit breaker is tripped or the disconnect is open, the outdoor board is off and cannot respond to the indoor unit, causing H97.
- **Indoor or outdoor control board failure** — A board with a damaged communication circuit cannot send or receive serial frames.
- **Electrical noise interference** — Running the signal wire alongside high-power wiring without separation can corrupt the serial data and cause intermittent H97 faults.

## Step-by-Step Fix {#fix}

1. **Verify outdoor unit power** — Check the outdoor unit dedicated circuit breaker and disconnect switch. Confirm the outdoor unit is receiving power and the main power LED is on.
2. **Inspect interconnecting wiring** — With both units powered off, check terminals 1, 2, and 3 (or L1, L2, S) at both the indoor and outdoor terminal blocks. Confirm each wire is on the correct terminal and seated firmly.
3. **Test wire continuity** — With power off, use a multimeter to check end-to-end continuity of each conductor. Infinite resistance on the signal wire indicates a break — replace the wire run.
4. **Check for wiring routing issues** — Confirm the interconnecting cable is not run alongside 240VAC power wiring for extended distances. Separate signal wiring from power wiring by at least 6 inches or use shielded cable.
5. **Power cycle in sequence** — Restore outdoor unit power first, wait 60 seconds for the outdoor board to initialize, then restore indoor unit power. If H97 clears and stays clear, the power sequencing was the issue.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Interconnecting cable (3-conductor) | [Amazon](https://www.amazon.com/s?k=Interconnecting+cable+%283-conductor%29&tag=errorcodefixes-20) \| 18 AWG minimum; run separately from high-voltage lines |
| Indoor control board | [Amazon](https://www.amazon.com/s?k=Indoor+control+board&tag=errorcodefixes-20) \| Replace if board communication section is confirmed failed |
| Outdoor control board | [Amazon](https://www.amazon.com/s?k=Outdoor+control+board&tag=errorcodefixes-20) \| Replace after confirming power and wiring are not the cause |
## When to Call a Pro

If wiring is verified correct and power is present at both units but H97 persists through power cycling, a Panasonic-authorized technician with service software can read internal communication fault logs to identify which board is the source of the failure.
