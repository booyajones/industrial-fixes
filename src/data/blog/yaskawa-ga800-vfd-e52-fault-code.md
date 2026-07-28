---
title: "Yaskawa GA800 E52 Fault - Causes & Fix"
description: "E52 is an undervoltage fault: the drive detected DC bus voltage fell below safe limits. Most often caused by unstable incoming power or a failing main-circuit contactor."
pubDatetime: 2026-06-06T11:39:17Z
modDatetime: 2026-06-06T11:39:17Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
most_likely_cause: "Unstable incoming utility voltage or a failing main-circuit magnetic contactor"
likelihood: "the most common causes"
diy_or_pro: "pro"
money_part: "Magnetic contactor (main circuit)"
---

## What this code means
E52 on a Yaskawa GA800 VFD is an undervoltage fault. The drive has detected that the DC bus voltage or incoming supply dropped below the allowable operating range, so it trips to protect itself and the motor from damage. In practical terms, the drive did not see sufficient input voltage to continue normal operation and issued a protective stop.

This fault is tied to unstable or insufficient input power voltage reaching the drive. It can happen during acceleration, under heavy load, or when upstream power components fail or cycle intermittently. The drive will not restart until the underlying power problem is corrected and the fault is cleared.

## Before You Replace Anything

Technicians sometimes replace the drive itself without checking upstream power. Always verify incoming line voltage under load and inspect the main-circuit contactor for chatter or weak coil voltage before considering drive replacement.

## Common Causes

- **Incoming power sag or brownout** Unstable utility voltage or voltage dips during motor start or load can cause the DC bus to fall below the trip threshold.
- **Failing or chattering main-circuit contactor** A magnetic contactor on the main circuit side with burned contacts, weak coil voltage, or intermittent dropout will cycle power to the drive and trigger undervoltage.
- **Loose or poor line connections** Intermittent supply wiring, loose terminals, or open phase conditions can cause the bus to collapse under load.
- **Upstream disconnect or fuse issues** Corroded disconnects, blown fuses, or poor contact in the feed path can reduce available voltage to the drive.
- **Power instability during acceleration** Heavy motor load or rapid acceleration can pull the supply voltage down if the incoming circuit is undersized or weak.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault occur immediately at power-up or only during motor start or load?</summary>
<div class="dtree-body"><strong>Yes:</strong> Likely a steady undervoltage condition or upstream power problem. Check incoming line voltage with a meter at the drive terminals under no-load and compare to nameplate ratings.<br><strong>No:</strong> Fault during operation suggests voltage sag under load or an intermittent contactor. Monitor line voltage during a start cycle and inspect the main-circuit contactor for chatter or dropout.</div>
</details>

<details class="dtree"><summary>Is the main-circuit contactor chattering, buzzing, or cycling on and off?</summary>
<div class="dtree-body"><strong>Yes:</strong> Contactor is likely failing or has weak coil voltage. Measure coil voltage and compare to the contactor's rated control voltage. Replace the contactor if contacts are burned or coil voltage is low.<br><strong>No:</strong> Contactor is probably OK. Focus on incoming line voltage stability and termination quality. Check for loose connections, corroded terminals, or voltage imbalance at the drive input.</div>
</details>

<details class="dtree"><summary>Are all three incoming phases present and balanced within a few volts of each other?</summary>
<div class="dtree-body"><strong>Yes:</strong> Phase balance is good. Check for voltage sag under load, inspect the upstream disconnect and fuses, and verify the supply circuit is sized correctly for the motor.<br><strong>No:</strong> Open phase, imbalanced supply, or poor connection detected. Inspect all terminals, fuses, and disconnects in the feed path. Repair or replace damaged components and verify voltage balance before resetting the drive.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Record the fault and operating conditions** from the drive keypad or LED operator before resetting anything, noting when the fault occurred and what the motor was doing.
2. **Measure incoming line voltage** at the drive input terminals with a multimeter, both under no-load and while the drive is attempting to start or run, and compare readings to the drive nameplate voltage rating.
3. **Inspect the main-circuit magnetic contactor** for chatter, buzzing, burned contacts, or intermittent dropout, and measure the coil voltage to confirm it matches the contactor's rated control voltage.
4. **Check all terminations and connections** in the upstream power path, including disconnects, fuses, terminals, and any line reactor or transformer, tightening and repairing any loose or corroded points.
5. **Monitor voltage during a start cycle** to see if the line voltage dips significantly under load, which points to an undersized supply circuit or weak utility feed.
6. **Replace the main-circuit contactor** if it is chattering, has burned contacts, or shows weak coil voltage, and verify the control circuit supplying the coil is stable.
7. **Reset the drive and test** only after the upstream power problem is corrected, because a reset alone will not fix an undervoltage condition, and document the fault history for future reference or escalation to Yaskawa technical support if the fault recurs.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Magnetic contactor (main circuit) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e52-fault-code&k=Magnetic+contactor+%28main+circuit%29&tag=errorcodefixes-20) \| Match coil voltage and current rating to the original contactor on the drive's input side. Required if contacts are burned or the contactor chatters. |
| Line terminals or terminal blocks | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e52-fault-code&k=Line+terminals+or+terminal+blocks&tag=errorcodefixes-20) \| Replace if corroded, cracked, or loose connections are found in the upstream power feed. |
| Fuses or disconnect switch | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e52-fault-code&k=Fuses+or+disconnect+switch&tag=errorcodefixes-20) \| Replace blown fuses or a damaged disconnect in the main circuit path if they are causing intermittent or low voltage. |

## When to Call a Pro

Call a qualified electrician or VFD technician if you are not comfortable working with three-phase power, measuring line voltage under load, or diagnosing contactor and upstream wiring issues. If incoming power and the contactor are confirmed good but the fault persists, the problem may be internal to the drive and requires Yaskawa technical support or a certified service center with access to the GA800 maintenance manual and parts list. High-voltage troubleshooting and drive-level repair should always be performed by trained personnel with proper test equipment and safety procedures.

**Rough cost:** A pro service call runs about $200–600 depending on whether repair is upstream wiring, contactor replacement, or drive-level service.
