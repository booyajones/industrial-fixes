---
title: "Daikin U4 Error Code - Causes & Fix"
description: "U4 means indoor and outdoor units can't communicate. Most often improper or loose wiring between the two units or a failed outdoor PCB."
pubDatetime: 2026-06-30T09:47:47Z
modDatetime: 2026-06-30T09:47:47Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - hvac
  - mini-split
  - daikin
money_part: "Daikin outdoor control board (PCB)"
most_likely_cause: "Improper or loose wiring between indoor and outdoor units"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Turn off the system for 5 minutes, then power it back on to clear transient communication errors"
  - "Inspect all wire connections at both indoor and outdoor terminals for loose or corroded contacts"
---

## Daikin U4 Error Code — What It Means

The U4 error code on a Daikin mini split signals a transmission failure between the indoor and outdoor units. The two halves of your system cannot exchange data, which prevents normal operation. You may notice the outdoor unit has no indicator lights at all.

This code is different from other Daikin faults like UA (unit combination error) or U0 (refrigerant shortage). U4 is strictly a communication breakdown, usually caused by wiring problems or a dead outdoor control board.

## Before You Replace Anything

Homeowners often replace the indoor board when the outdoor control board (PCB) is actually dead. Check if the outdoor unit lights come on at all. If the outdoor board shows no lights and wiring is correct, replace the outdoor PCB and noise filter board together.

[Jump to Fix](#fix)

## Common Causes

- **Improper or loose wiring (~40%)** Physically incorrect, loose, or damaged communication cables (F1/F2) between the indoor and outdoor units, especially common in new installations where wires are not landed correctly.
- **Failed outdoor control board (PCB) (~30%)** The outdoor board has died and shows no indicator lights, often with the noise filter board also failing at the same time.
- **Reversed L1/L2 power lines (~15%)** L1 and L2 power wires are reversed on the indoor unit versus the outdoor unit (for example, connected left-to-right on one and right-to-left on the other).
- **Shorted communication wire (~10%)** Short circuit in the F1/F2 transmission wiring or wiring with resistance in the kiloohms or less when it should read megaohms (open circuit).
- **Component issues (~5%)** Occasionally a blocked outdoor fan, faulty capacitor, or damaged expansion valve triggers the fault, though the PCB is the primary suspect.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the outdoor unit show any indicator lights at all?</summary>
<div class="dtree-body"><strong>Yes:</strong> The outdoor board is receiving power. Check communication wiring for loose or reversed connections and measure resistance between F1 and F2 wires (should be in megaohms).<br><strong>No:</strong> The outdoor board is likely dead. Verify AC voltage at the outdoor unit (208-240V L1 to L2) and if power is present, replace the outdoor control board and noise filter board.</div>
</details>

<details class="dtree"><summary>Did the error appear immediately after installation or wiring work?</summary>
<div class="dtree-body"><strong>Yes:</strong> Wiring is probably incorrect, reversed, or loose. Verify L1 and L2 are not swapped between units and check that F1 and F2 communication wires match at both ends.<br><strong>No:</strong> A component has failed. Test communication wire resistance (should be megaohms), check AC voltage at both units, and if wiring is good, replace the outdoor PCB.</div>
</details>

<details class="dtree"><summary>Does the error clear after a 5-minute power reset?</summary>
<div class="dtree-body"><strong>Yes:</strong> It was a transient communication glitch. Monitor the system. If it returns frequently, check wiring connections and tighten any loose terminals.<br><strong>No:</strong> A persistent hardware fault exists. Proceed with voltage checks, wiring resistance tests, and outdoor board diagnosis.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power reset the system.** Turn off the mini split for at least 5 minutes, then turn it back on to clear any transient communication errors.
2. **Verify AC voltage at the outdoor unit.** Measure L1 to L2 at the outdoor unit input. You should see 208-240V AC. Also measure L1 to ground and L2 to ground (both should be around 120V AC).
3. **Inspect all communication wiring.** Check F1 and F2 communication wires at both indoor and outdoor terminals for loose connections, damaged insulation, or incorrect matching.
4. **Test communication wire resistance.** Disconnect both ends of the F1/F2 wires so they float free. Measure resistance wire to wire. It should be in the megaohms (open circuit). If it reads in kiloohms or less, the wire is shorted and must be replaced.
5. **Check for reversed L1/L2 power lines.** Confirm L1 and L2 are not reversed between the indoor and outdoor units (for example, left-to-right on one and right-to-left on the other).
6. **Force pump down test (if wiring is correct).** Put the system into force pump down mode. If the outdoor board remains completely dark with no lights, the board is faulty.
7. **Replace the outdoor control board and noise filter board.** If the outdoor unit shows no lights and wiring checks out, replace the outdoor PCB. Always replace the noise filter board as well since it often fails together with the main board.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Daikin outdoor control board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-mini-split-u4-error-code&k=Daikin+outdoor+control+board+%28PCB%29&tag=errorcodefixes-20) \| Match the exact part number from your outdoor unit label or service manual |
| Daikin noise filter board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-mini-split-u4-error-code&k=Daikin+noise+filter+board&tag=errorcodefixes-20) \| Replace together with the outdoor PCB when it fails |
| Communication wire (F1/F2 cable) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-mini-split-u4-error-code&k=Communication+wire+%28F1%2FF2+cable%29&tag=errorcodefixes-20) \| Use stranded copper rated for outdoor low-voltage control circuits if wire is shorted |

## When to Call a Pro

Call a licensed HVAC technician for a U4 error. Diagnosis requires AC voltage measurements, resistance testing of control circuits, and safely working inside energized high-voltage panels on both the indoor and outdoor units. Replacing the outdoor control board involves disconnecting refrigerant sensors, compressor terminals, and fan connections that must be reassembled correctly. Technicians also have the tools to force pump down mode and verify proper refrigerant pressures after board replacement. Misdiagnosis or improper wiring can damage the new board or create a safety hazard.

**Rough cost:** A pro service call runs about $250-500.
