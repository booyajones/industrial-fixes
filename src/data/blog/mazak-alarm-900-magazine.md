---
title: "Mazak Alarm 900 Tool Magazine Index Fault - Causes & Fix"
description: "What Mazak Alarm 900 (Tool Magazine Index Fault) means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - cnc
  - mazak
---

## Mazak Alarm 900 - What It Means

Mazak Alarm 900 is a tool magazine index fault - the MAZATROL control commanded the tool magazine to index to a specific pocket number, but the magazine didn't reach or confirm the target position within the required time. On Mazak machining centers with drum or chain-type tool magazines, Alarm 900 stops all operation until the magazine is returned to a known position.

[Jump to Fix](#fix)

## Common Causes

- **Magazine drive motor or transmission fault** - The servo or stepper motor that drives the magazine rotation has failed or stalled under load.
- **Tool pocket sensor not reading correctly** - The position sensor (encoder or proximity switch) that tracks which pocket is at the exchange position has failed or is misaligned.
- **Heavy tool causing imbalance** - On drum-type magazines, a very heavy tool (large boring bar, face mill) creates enough imbalance to stall the magazine drive on small Mazak models.
- **Magazine mechanical interference** - A tool that's not fully seated in its pocket, or a damaged pocket, catches on the machine frame during rotation.

## Step-by-Step Fix {#fix}

1. **Power cycle and re-home the magazine** - Cycle main power. During re-homing, the magazine returns to its home position. If it completes homing without Alarm 900, attempt a manual tool change in MDI at low speed.
2. **Inspect the magazine physically** - With E-stop engaged, check all tool pockets for properly seated tools. Look for any pocket that's damaged or has a tool that extends past the pocket opening.
3. **Check magazine position sensor** - In the Mazak diagnostic screen, monitor the magazine position output as the magazine rotates. If the count doesn't increment for each pocket, the sensor has failed.
4. **Check magazine drive** - Attempt a manual magazine index (via the Mazak's service/maintenance mode if accessible) and listen for the motor effort. Unusual noise or grinding indicates mechanical interference.
5. **Contact Mazak service** - Alarm 900 that doesn't clear after power cycle and re-home requires Mazak field service for magazine calibration.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Magazine position proximity switch | [Amazon](https://www.amazon.com/s?i=industrial&k=Magazine+position+proximity+switch&tag=errorcodefixes-20) \| Replace if position count is unreliable |
| Magazine drive motor | [Amazon](https://www.amazon.com/s?i=industrial&k=Magazine+drive+motor&tag=errorcodefixes-20) \| Replace if stalling confirmed |
| Tool pocket | [Amazon](https://www.amazon.com/s?i=industrial&k=Tool+pocket&tag=errorcodefixes-20) \| Replace damaged pockets |
## When to Call a Pro

Mazak tool magazine mechanical work requires factory-trained service to maintain precise pocket-to-spindle alignment.

## Related Articles

- [CNC Alarm Reset Guide: How to Clear Alarms Safely](/posts/cnc-alarm-reset-guide/)
- [CNC Machine Error Codes: Complete Troubleshooting Guide](/posts/cnc-error-codes-guide/)
- [Doosan CNC Alarm Codes Guide — Fanuc / Fanuc i Series Controls](/posts/doosan-cnc-fault-codes/)
- [Fanuc 0i-MD Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-0i-md-alarm-codes/)
- [Fanuc 30i/31i/32i Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-30i-alarm-codes/)
