---
title: "LG Mini Split CH74 Error Code - Causes & Fix"
description: "CH74 on LG mini splits typically signals a communication fault between indoor and outdoor units. Power cycle first, then check wiring."
pubDatetime: 2026-05-31T00:57:13Z
modDatetime: 2026-05-31T00:57:13Z
author: "Dana Kowalski"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - lg
money_part: "LG outdoor unit main PCB"
---

## LG Mini Split CH74 Error Code — What It Means

CH74 is not a standard code in LG's published residential mini split error guides for the U.S. market. It most likely indicates a communication or control board fault, similar to other LG communication codes like CH05 or CH53. On some LG Multi V and VRF systems, codes in this range point to problems with the data line between the indoor and outdoor units or a controller issue. Because CH74 does not appear in the common LG mini split fault tables, you should verify the exact meaning in your model-specific service manual or contact LG technical support with your full model number.

In general, LG communication faults mean the indoor and outdoor units cannot exchange control signals. This can prevent the system from starting, cause erratic operation, or trigger a shutdown. The fault is usually in the low-voltage communication wiring, a loose terminal connection, a failed PCB, or an addressing mismatch after a board replacement.

[Jump to Fix](#fix)

## Common Causes

- **Loose or disconnected communication wiring** The signal cable between indoor and outdoor units is not fully seated at the terminal blocks or has pulled free during installation or service.
- **Damaged or mis-terminated 485 communication cable** The data line conductors are pinched, corroded, or connected to the wrong terminals on the indoor or outdoor board.
- **Faulty local modem or communication interface PCB** The small communication board on the outdoor unit has failed and can no longer relay signals to the main controller.
- **Defective indoor or outdoor main PCB** The main control board on either unit has a fault in its communication circuit, even when wiring and voltage are correct.
- **Addressing mismatch after PCB replacement** If a main board was recently replaced, the system may not have been re-addressed and the indoor unit is not recognized by the outdoor controller.

## Step-by-Step Fix {#fix}

1. **Power-cycle the entire system** by switching off the circuit breaker or disconnect for at least 60 seconds, then restore power and check whether the fault clears on its own.
2. **Inspect all communication wiring** between the indoor and outdoor units, focusing on the terminal blocks marked for the signal line (often terminals 3 and N, or 3 and 4 on Multi V platforms).
3. **Re-terminate any loose connections** at both the indoor and outdoor terminal blocks, making sure conductors are fully inserted and screw terminals are tightened to the torque specified in your installation manual.
4. **Measure the communication line voltage** with a multimeter set to DC volts, probing the signal terminals (one LG guide lists a typical range of 0 to 65 V DC for split and multi systems, and about 4 V DC for certain Multi V checks).
5. **Check status LEDs** on the outdoor main PCB or local modem board to confirm the board is powered and communicating (refer to your service manual for LED meanings).
6. **Perform auto-addressing** if a PCB has been replaced by holding the red button on the outdoor main PCB for 5 seconds until the display shows 88, then verify that indoor units receive their addresses.
7. **Replace the suspect PCB or local modem** if wiring, voltage, and addressing are all correct but the code persists, starting with the communication interface board on the outdoor unit before replacing the main control board.

## Parts Often Needed

| Part | Notes |
|------|-------|
| LG outdoor unit main PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-mini-split-ch74-error-code&k=LG+outdoor+unit+main+PCB&tag=errorcodefixes-20) \| Order by your outdoor model number and serial prefix to make sure board revision matches. |
| LG indoor unit main control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-mini-split-ch74-error-code&k=LG+indoor+unit+main+control+board&tag=errorcodefixes-20) \| Verify the part number from the label on your existing board before ordering. |
| LG local modem / communication interface board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-mini-split-ch74-error-code&k=LG+local+modem+%2F+communication+interface+board&tag=errorcodefixes-20) \| Small PCB on the outdoor unit that handles data line signals, often mounted near the main board. |

## When to Call a Pro

Call a licensed HVAC technician if you are not comfortable working with low-voltage wiring or if the code returns after you have checked all connections and power-cycled the system. Because CH74 does not appear in standard LG residential mini split documentation, a technician with access to LG's service portal or your model-specific manual can confirm the exact fault definition and perform board-level diagnostics. Professional help is also required if you need to replace a main PCB or local modem, because those repairs involve refrigerant-circuit access, addressing procedures, and warranty considerations that are best handled by a certified LG installer.
