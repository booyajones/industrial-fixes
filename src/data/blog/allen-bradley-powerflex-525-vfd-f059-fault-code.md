---
title: "Allen-Bradley PowerFlex 525 F059 - Causes & Fix"
description: "F059 (Safety Open) means the drive's safety inputs are not enabled. Most often caused by missing safety jumpers or an open contact in the external safety chain."
pubDatetime: 2026-06-12T10:19:31Z
modDatetime: 2026-06-12T10:19:31Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - allen-bradley
money_part: "Safety relay or contact block"
most_likely_cause: "missing or incorrect safety jumpers when safety is not used"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify safety jumpers are installed between S1, S2, and S+ if the application does not use an external safety chain"
  - "Check all safety-chain contacts (E-stops, gate switches, permissives) for physical closed position"
  - "Inspect safety terminal connections for loose or broken wires"
no_buy_pct: "80%"
---

## Allen-Bradley PowerFlex 525 F059 — What It Means

F059 on the PowerFlex 525 means Safety Open. The drive is not seeing both safety inputs enabled, so the safety circuit is open and the drive inhibits operation. Both safety inputs must be enabled for the drive to run. If either input is open, the drive faults immediately.

This fault is usually traced to one of three things: the safety inputs are not properly energized, the safety wiring or jumpers are missing or miswired, or the safety function is intentionally configured but not being satisfied through the drive's safety circuit settings. The drive receives its safety enable signal at terminals S1, S2, and S+. When the safety circuit is open at those terminals, the drive will not permit motor operation.

## Before You Replace Anything

Many technicians replace the drive itself when the actual problem is miswired or missing safety jumpers at the S1, S2, and S+ terminals. Always verify the safety circuit wiring and jumper configuration before ordering a replacement drive.

[Jump to Fix](#fix)

## Common Causes

- **Missing safety jumpers (~45%)** Safety terminals S1, S2, and S+ are not wired correctly or the expected jumper is missing when safety is not used in the application.
- **Open contact in external safety chain (~30%)** An external safety relay, gate switch, E-stop, or permissive contact is open, so the drive never sees the safety circuit made.
- **Loose or broken safety wiring (~15%)** Field wiring to the safety terminals has a broken conductor, loose terminal, or mislanding that prevents the safety enable signal from reaching the drive.
- **Incorrect safety parameter configuration (~10%)** Drive parameter t105 (Safety Open Enable) or other safety-related settings are not configured as the application requires.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Are the safety terminals S1, S2, and S+ jumpered together (if no external safety devices are used)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The jumper configuration is correct. Move to checking external safety-chain contacts and wiring.<br><strong>No:</strong> Install the required safety jumpers per the PowerFlex 525 manual wiring diagram. Clear the fault and retest.</div>
</details>

<details class="dtree"><summary>Are all E-stops, gate switches, and safety relays in the closed position?</summary>
<div class="dtree-body"><strong>Yes:</strong> The external devices are closed. Check for broken wiring or loose connections between the safety devices and the drive terminals.<br><strong>No:</strong> Correct the open safety device (reset E-stop, close gate, energize relay). Clear the fault and retest.</div>
</details>

<details class="dtree"><summary>Does the fault clear and stay cleared after correcting the safety circuit?</summary>
<div class="dtree-body"><strong>Yes:</strong> The repair is complete. The safety circuit is now correctly enabled and the drive can operate.<br><strong>No:</strong> The open condition is still present. Trace the safety wiring end-to-end and verify continuity from the field device through to S1, S2, and S+.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive** and verify zero voltage at the input and output terminals before working on any wiring.
2. **Locate the safety terminals** S1, S2, and S+ on the PowerFlex 525 control terminal block.
3. **Verify the safety jumper arrangement** is installed if the drive is not using external safety devices. Consult your model's wiring diagram for the correct jumper configuration.
4. **Inspect the safety loop wiring** for broken conductors, loose terminals, mislanding, or an open contact in the external safety chain (E-stop, gate switch, safety relay).
5. **Check parameter t105** (Safety Open Enable) and other safety-related configuration settings to confirm they match the application requirements.
6. **Correct any wiring or jumper issues**, tighten all connections, and replace any damaged wire runs feeding S1, S2, and S+.
7. **Clear the fault** and power the drive back on. If the fault immediately returns, the open condition is still present and must be found in the field wiring or safety device chain.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Safety relay or contact block | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-525-vfd-f059-fault-code&k=Safety+relay+or+contact+block&tag=errorcodefixes-20) \| Only if the external safety device itself is defective or damaged |
| E-stop switch or gate switch | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-525-vfd-f059-fault-code&k=E-stop+switch+or+gate+switch&tag=errorcodefixes-20) \| Replace if the contact does not close or shows continuity failure when actuated |
| Safety circuit field wiring | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-525-vfd-f059-fault-code&k=Safety+circuit+field+wiring&tag=errorcodefixes-20) \| Replace damaged or broken wire runs between safety devices and S1, S2, S+ terminals |

## When to Call a Pro

Call a qualified industrial electrician or automation technician if you are not familiar with VFD safety circuits, the PowerFlex 525 terminal wiring, or parameter configuration. This fault usually requires tracing field wiring, verifying safety-device operation, and editing drive parameters. If the safety circuit hardware is correct but the fault persists, the drive may have an internal safety-circuit failure that requires manufacturer service or replacement. Never bypass safety inputs to force the drive to run. Safety circuits are designed to protect personnel and equipment.

**Rough cost:** A pro service call runs about $150-400 for diagnosis and wiring correction.
