---
title: "LG Mini-Split CH03 Error - Causes & Fix"
description: "CH03 on LG mini-splits means a communication failure between the wired remote controller and indoor unit. Most often fixed by reseating connections or replacing the indoor PCB."
pubDatetime: 2026-05-31T00:51:46Z
modDatetime: 2026-05-31T00:51:46Z
author: "James Rutherford"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - lg
money_part: "LG indoor unit main PCB"
---

## LG Mini-Split CH03 Error — What It Means

CH03 on LG mini-split systems with a wired remote controller indicates a communication error between that controller and the indoor unit. LG's Multi V and wired-controller systems trigger this fault when the indoor PCB cannot talk to the thermostat, usually because of a wiring problem, low voltage supply to the controller, or a failed indoor main board.

This code is specific to systems that use a wired wall controller. If your unit was originally installed with a wired controller that has since been removed, a power cycle may clear the fault. The code does not apply to infrared-remote models and should not be confused with drain-pump or refrigerant faults sometimes listed on third-party sites.

[Jump to Fix](#fix)

## Common Causes

- **Indoor PCB malfunction** The main control board inside the air handler has failed and can no longer send 12 VDC to the wired controller or process its signals.
- **Loose or corroded controller connector** The plug at the indoor unit or at the wall controller has backed out, collected moisture, or developed corrosion on the pins.
- **Broken or shorted communication wire** The low-voltage cable running between the indoor unit and the wired controller has a break, short, or splice that blocks data transmission.
- **Failed wired remote controller** The wall thermostat itself has an internal fault and cannot communicate with the indoor unit even when wiring and voltage are correct.
- **Controller removed after installation** The system was initially configured with a wired controller that has since been unplugged or removed, leaving the indoor unit waiting for a signal that will never arrive.
- **Low control-board supply voltage** The indoor PCB is supplying less than 10 VDC to the controller circuit instead of the nominal 12 VDC, preventing stable communication.

## Step-by-Step Fix {#fix}

1. **Power-cycle the indoor unit** by switching off the breaker or disconnect for three to five minutes, then restore power and check whether CH03 reappears.
2. **Inspect the wired-controller connector** at both the indoor-unit terminal block and the wall thermostat for loose pins, moisture, or poor seating, and reseat firmly.
3. **Test the communication cable** for continuity and shorts using a multimeter, and look for physical damage, splices, or incorrect wire-to-terminal assignments along the entire run.
4. **Measure the controller supply voltage** at the indoor PCB terminals with a DC voltmeter. LG specifies 12 VDC nominal, and readings below 10 VDC indicate a board fault.
5. **Substitute a known-good wired controller** if you have a spare. If the fault clears immediately, replace the original thermostat.
6. **Replace the indoor main PCB** if voltage is low or absent and all wiring checks out. Power down the unit, photograph existing wire positions, swap the board, and run auto-addressing if your Multi V system requires it.
7. **Verify the fix** by running the system in cooling and heating modes for at least 15 minutes each to confirm that CH03 does not return and that the wired controller responds to every command.

## Parts Often Needed

| Part | Notes |
|------|-------|
| LG indoor unit main PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-mini-split-ch03-error-code&k=LG+indoor+unit+main+PCB&tag=errorcodefixes-20) \| Match the board part number printed on your existing PCB or look up by model number in the LG parts catalog. |
| LG wired remote controller / thermostat | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-mini-split-ch03-error-code&k=LG+wired+remote+controller+%2F+thermostat&tag=errorcodefixes-20) \| Confirm compatibility with your indoor-unit model and that it supports the same communication protocol (typically LG PREMTB or PQRCVCL series). |
| Low-voltage communication cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-mini-split-ch03-error-code&k=Low-voltage+communication+cable&tag=errorcodefixes-20) \| Use shielded or twisted-pair cable rated for thermostat wiring if you need to replace or extend the run between the indoor unit and wall controller. |

## When to Call a Pro

Call a qualified HVAC technician if you are not comfortable working with low-voltage DC circuits, if you do not own a multimeter to check the 12 VDC supply, or if the fault persists after reseating connectors and power-cycling. Indoor PCB replacement requires safe electrical isolation, proper wire documentation, and sometimes a laptop with LG's service software to run auto-addressing on Multi V systems. A technician can also verify that the communication protocol and controller model are correct for your specific indoor unit, which is difficult to confirm from model-number stickers alone.
