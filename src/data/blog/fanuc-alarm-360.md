---
title: "Fanuc Alarm 360 — APC Alarm Battery Low Causes & Fix"
description: "What Fanuc alarm 360 means, why the absolute pulse coder battery alarm fires, and how to fix it step by step."
pubDatetime: 2026-04-22T15:00:00Z
modDatetime: 2026-04-22T15:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - cnc
  - fanuc
money_part: "Fanuc APC battery A06B-6073-K001"
---

## Fanuc Alarm 360 — What It Means

Alarm 360 on a Fanuc CNC system is an APC (Absolute Pulse Coder) alarm — specifically a battery voltage low warning for the absolute encoder battery. Fanuc absolute encoders retain their position data through power outages using a dedicated lithium battery (typically 3V AA or a purpose-built pack). Alarm 360 fires when the battery voltage drops to the warning threshold, indicating the battery must be replaced before the next machine power-off. If the machine is powered off with a dead APC battery, the absolute position data is lost and the machine must be re-referenced (rehomed) on the next startup — a potentially lengthy and costly interruption.

[Jump to Fix](#fix)

## Common Causes

- **Battery at end of service life** — APC batteries typically last 3–5 years. Alarm 360 on a machine that has been in service for several years is a normal maintenance event, not a failure.
- **Battery not replaced during previous warning** — If alarm 360 was acknowledged but the battery not replaced, the machine continued to drain the battery. The alarm will escalate from a warning to a lockout if the battery dies completely.
- **Extended machine downtime with power off** — Absolute encoders continue to draw from the battery whenever machine power is off. Long storage or shutdown periods deplete the battery faster than normal operation.
- **Battery connector issue** — Less commonly, a loose or corroded battery connector can intermittently reduce voltage, triggering alarm 360 on a battery that is not actually depleted.

## Step-by-Step Fix {#fix}

1. **Do not power off the machine** — While alarm 360 is active, keep the machine powered on. The encoder retains position from the CNC's main power supply when the machine is running; the battery is only needed during power-off. Replacing the battery with the machine on prevents position data loss.
2. **Identify the battery location** — On most Fanuc systems, the APC battery is in one of three locations: a dedicated battery box on the back of the machine, a compartment in the servo motor cable junction box, or a holder on the CNC control panel. Refer to the machine's maintenance manual.
3. **Replace the battery while powered on** — Remove the old battery and immediately install the new one. Do not leave the battery connector unplugged for more than 30 seconds, as the encoder's internal capacitor can only hold position data briefly without either the battery or the main supply.
4. **Use the correct battery specification** — Most Fanuc αi and βi series absolute encoders use a 3V lithium battery: Fanuc A06B-6073-K001 (AA type) or the equivalent. Do not substitute alkaline batteries.
5. **Acknowledge and clear the alarm** — After battery replacement, navigate to the CNC alarm screen and clear alarm 360. Power cycle if necessary to confirm the alarm does not return.
6. **Document the replacement** — Log the date and battery part number in the machine maintenance record so the next replacement interval can be planned proactively.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Fanuc APC battery A06B-6073-K001 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-alarm-360&k=Fanuc+APC+battery+A06B-6073-K001&tag=errorcodefixes-20) \| Standard AA lithium, 3V; use genuine Fanuc or a direct equivalent |
| Multi-axis battery pack (where applicable) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-alarm-360&k=Multi-axis+battery+pack+%28where+applicable%29&tag=errorcodefixes-20) \| Some machines use a single pack for multiple axes — replace as a complete unit |
## When to Call a Pro

If alarm 360 escalated to a full position data loss (the machine displays a different alarm code and cannot find home), a Fanuc-certified technician must perform the absolute encoder re-initialization procedure and re-establish the machine zero reference. This is not a DIY procedure on a production machine.

## Related Articles

- [Fanuc 0i-MD Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-0i-md-alarm-codes/)
- [Fanuc 30i/31i/32i Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-30i-alarm-codes/)
- [Fanuc Alarm 1 Overtravel — Causes & Fix](/posts/fanuc-alarm-1-overtravel/)
- [Fanuc Alarm 10 Servo Alarm — Causes & Fix](/posts/fanuc-alarm-10-servo-alarm/)
- [Fanuc Alarm 2 — Overtravel Plus Causes & Fix](/posts/fanuc-alarm-2-overtravel/)

## See Also

- [Fanuc Alarm 460: Spindle Speed Error — Detailed Troubleshooting](/posts/fanuc-alarm-460-spindle/)
- [Fanuc Alarm 506 — Servo Following Error Fix](/posts/fanuc-alarm-506/)
- [Fanuc Alarm 437 — Servo Following Error 4th Axis Causes & Fix](/posts/fanuc-alarm-437/)
- [Fanuc Alarm 10 Servo Alarm — Causes & Fix](/posts/fanuc-alarm-10-servo-alarm/)
