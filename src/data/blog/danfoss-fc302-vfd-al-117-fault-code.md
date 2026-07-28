---
title: "Danfoss FC302 AL-17 Fault - Causes & Fix"
description: "AL-17 means the VFD lost serial communication with the LCP keypad. Most often a loose or faulty keypad cable is the cause."
pubDatetime: 2026-06-24T10:13:47Z
modDatetime: 2026-06-24T10:13:47Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "LCP keypad (Local Control Panel)"
most_likely_cause: "Faulty or loose LCP keypad cable"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power cycle the drive (turn off, wait for DC bus LEDs to go dark, restart) to clear transient errors"
  - "Remove and re-seat the LCP keypad firmly to make sure ribbon-cable pins make full contact"
part_price: "$150-250 for a replacement LCP keypad"
no_buy_pct: "40%"
---

## What this code means
AL-17 (STD Bus Timeout) on a Danfoss FC302 VFD indicates that serial communication with an accessory—typically the LCP keypad—has been lost. The drive's control logic has stopped receiving valid data packets from the Smart Device Bus (STD Bus) device connected to it. When the communication silence exceeds the configured timeout (often set in parameter 8-04, with a default around 2.0 seconds), the alarm triggers.

The drive may remain in a stop state or fail to accept commands from the keypad, though it might still run if pre-programmed or controlled by a functioning fieldbus card. This is a communication fault, not a motor or power problem, so the drive itself may be healthy while the control link is broken.

## Before You Replace Anything

Many technicians replace the entire control board when a simple keypad swap or cable re-seat would fix the issue. Always test with a known-good LCP keypad before ordering an expensive logic card.

## Common Causes

- **Loose or damaged LCP keypad cable (~40%)** The ribbon cable connecting the keypad to the drive is not fully inserted, has bent pins, or is physically damaged.
- **Failed LCP display unit (~30%)** The keypad itself has an internal failure such as a burnt component or firmware crash.
- **Logic board (I/O control PCB) fault (~20%)** The drive's internal control board has a fault in the STD Bus communication circuit.
- **Electrical noise interference (~10%)** Control wiring is routed too close to power or motor cables, corrupting the serial data stream with electrical noise.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the LCP keypad display turn on at all?</summary>
<div class="dtree-body"><strong>Yes:</strong> The keypad has power but communication is broken. Re-seat the keypad and try a known-good spare.<br><strong>No:</strong> The keypad may be dead or the cable is completely disconnected. Check cable connection and swap the keypad.</div>
</details>

<details class="dtree"><summary>Does the fault clear with a different LCP keypad installed?</summary>
<div class="dtree-body"><strong>Yes:</strong> The original keypad is faulty. Replace the LCP display unit.<br><strong>No:</strong> The drive's cable or control board is the problem. Test with a new ribbon cable, then the control board.</div>
</details>

<details class="dtree"><summary>Are control cables run in the same conduit as motor power cables?</summary>
<div class="dtree-body"><strong>Yes:</strong> Noise is likely corrupting the signal. Separate control wiring into its own conduit and verify ground connections.<br><strong>No:</strong> Focus on hardware: swap the keypad, check the cable, and test the control board.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power cycle the drive.** Turn off the VFD, wait for the DC bus capacitors to fully discharge (watch for all LEDs to go dark), then restart. This clears transient communication errors.
2. **Remove and inspect the LCP keypad.** Pull the keypad off the drive front and examine the ribbon cable connector for bent pins, debris, or damage.
3. **Re-seat the keypad firmly.** Push the keypad back onto the drive, making sure the ribbon cable is fully inserted and the unit clicks into place. Restart and check if the fault clears.
4. **Swap in a known-good LCP keypad.** If re-seating does not help, disconnect the current keypad and install a spare or known-working unit. If communication resumes, replace the original LCP display.
5. **Replace the STD Bus ribbon cable.** If a spare keypad also fails, replace the ribbon cable (if it is a separate assembly from the keypad). Re-test with the new cable.
6. **Test the control board.** If the fault persists with a new keypad and cable, the I/O control PCB is likely faulty. Replace the logic board and restore parameter settings from a backup or re-enter them manually.
7. **Check wiring isolation.** Verify that control cables are routed separately from high-voltage power and motor cables. make sure ground connections are tight and free of corrosion to prevent electrical noise.

## Parts Often Needed

| Part | Notes |
|------|-------|
| LCP keypad (Local Control Panel) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-117-fault-code&k=LCP+keypad+%28Local+Control+Panel%29&tag=errorcodefixes-20) \| Replacement display and keypad unit for Danfoss FC302 |
| STD Bus ribbon cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-117-fault-code&k=STD+Bus+ribbon+cable&tag=errorcodefixes-20) \| Connecting cable between keypad and drive logic board (if sold separately) |
| I/O control PCB (logic board) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-117-fault-code&k=I%2FO+control+PCB+%28logic+board%29&tag=errorcodefixes-20) \| Internal control card for the FC302, required if communication circuit has failed |

## When to Call a Pro

Call a professional if you are not comfortable working with VFD control circuits or parameter programming. Replacing the control board requires de-energizing the drive, handling sensitive electronics, and re-entering or restoring all parameters (the drive will lose its configuration). If the fault persists after swapping the keypad and cable, or if the drive is part of a critical process line where downtime is costly, a certified VFD technician can diagnose the control board and minimize downtime. Also call a pro if you suspect electrical noise issues across multiple drives, as that may require a full wiring and grounding audit of the facility.

**Rough cost:** A pro service call runs about $150-400 depending on whether the fix is a keypad, cable, or control board replacement.
