---
title: "Cooper & Hunter Mini Split E1 Error - Causes & Fix"
description: "E1 on Cooper & Hunter mini splits means the indoor and outdoor units cannot communicate. Check wiring first, then test boards."
pubDatetime: 2026-05-31T14:48:45Z
modDatetime: 2026-05-31T14:48:45Z
author: "Marcus Webb"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - cooper-and-hunter
money_part: "Outdoor main control board (PCB)"
---

## Cooper & Hunter Mini Split E1 Error — What It Means

The E1 error code on Cooper & Hunter mini split systems indicates a communication failure between the indoor and outdoor units. The two halves of your system cannot exchange control signals, so the unit shuts down to protect itself. This is not a refrigerant pressure fault. Instead, it points to a break or fault in the low-voltage control wiring that links the indoor head to the outdoor condenser, or to a failed circuit board in one of the units.

[Jump to Fix](#fix)

## Common Causes

- **Loose or incorrect interconnect wiring** The communication wires between indoor and outdoor terminal blocks are not fully seated, were connected to the wrong terminals, or have corroded spade connectors.
- **Broken or shorted communication cable** The control wire running through the line-set or conduit has a nick, short, or open circuit that stops data from passing between units.
- **Failed outdoor PCB** The main control board in the outdoor condenser has a burned component or failed communication circuit and can no longer send or receive signals.
- **Failed indoor PCB** The control board inside the wall-mounted head has a fault in its communication driver or power supply and cannot talk to the outdoor unit.
- **Outdoor reactor wiring or resistance problem** The reactor (inductor) on the outdoor board has loose connections or measures outside the expected 0 to 1 ohm range, disrupting the communication signal.

## Step-by-Step Fix {#fix}

1. {'number': 1, 'text': '**Power off the system** at the breaker or disconnect switch, wait two minutes, then restore power and check if the E1 clears after the units restart.'}
2. {'number': 2, 'text': '**Remove the covers** from both the indoor head and outdoor condenser to expose the terminal blocks where the interconnect wiring lands.'}
3. {'number': 3, 'text': "**Inspect and re-seat every wire** at the indoor and outdoor terminal strips, confirming each conductor matches your unit's wiring diagram and that spade connectors are tight and free of corrosion."}
4. {'number': 4, 'text': '**Set your multimeter to DC voltage** and measure across the communication terminals (usually labeled S or COM) with the unit powered on and attempting to run.'}
5. {'number': 5, 'text': '**Look for an alternating positive and negative reading** on your meter. Normal communication shows the voltage swinging back and forth. A fixed voltage that does not change indicates a fault on whichever side (indoor or outdoor) shows the stuck value.'}
6. {'number': 6, 'text': '**Check the outdoor reactor** if your model has one. Disconnect power, remove the reactor leads, and measure resistance. Replace the reactor if it reads outside 0 to 1 ohm or if the wiring to it is loose.'}
7. {'number': 7, 'text': '**Replace the PCB** indicated by your voltage test. If the outdoor side shows a fixed voltage or the reactor is fine, swap the outdoor board first. If the indoor side is stuck or the error persists, replace the indoor board.'}

## Parts Often Needed

| Part | Notes |
|------|-------|
| Outdoor main control board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-cooper-and-hunter-mini-split-e1-error-code&k=Outdoor+main+control+board+%28PCB%29&tag=errorcodefixes-20) \| Match the board part number printed on your existing outdoor unit PCB. Verify your model and serial number before ordering. |
| Indoor main control board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-cooper-and-hunter-mini-split-e1-error-code&k=Indoor+main+control+board+%28PCB%29&tag=errorcodefixes-20) \| Confirm the exact part number on the indoor head's existing board. Different tonnages use different boards even within the same series. |
| Outdoor reactor (inductor) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-cooper-and-hunter-mini-split-e1-error-code&k=Outdoor+reactor+%28inductor%29&tag=errorcodefixes-20) \| Only required if resistance measures outside 0 to 1 ohm. Check your outdoor board layout to confirm your model uses a reactor. |

## When to Call a Pro

Call a licensed HVAC technician if you are not comfortable working inside energized equipment or if you do not own a multimeter and basic hand tools. Communication faults require live voltage tests and careful tracing of control wiring across both units. If you have already verified that all wiring is correct and seated but the E1 persists, a technician can isolate which board has failed and source the correct replacement part for your specific Cooper & Hunter model. Board-level troubleshooting and refrigerant-side work both require EPA certification and specialized tools.
