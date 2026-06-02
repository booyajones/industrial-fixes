---
title: "Mitsubishi E6 Error Code - Causes & Fix"
description: "E6 means a communication fault between indoor and outdoor units. Most often caused by loose or miswired S1/S2/S3 control wiring."
pubDatetime: 2026-05-31T08:49:13Z
modDatetime: 2026-05-31T08:49:13Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - mini-split
  - mitsubishi
---

## Mitsubishi E6 Error Code — What It Means

On Mitsubishi Electric heat pumps, the E6 code indicates a serial communication error between the indoor and outdoor control boards. The outdoor unit cannot see or properly exchange data with the indoor unit. This is not a compressor or refrigerant problem. It is an electrical signal fault in the control wiring or one of the two circuit boards.

The fault usually appears at startup or after a power event like a storm or tripped breaker. The exact meaning can vary slightly by model family, so always check your service manual for your specific model number.

[Jump to Fix](#fix)

## Common Causes

- **Loose or corroded terminal connections** The S1, S2, and S3 field wiring screws on the indoor or outdoor terminal board are not tight or have corroded over time.
- **Miswired communication conductors** The S1, S2, or S3 wires are landed on the wrong numbered terminals or the polarity does not match between units.
- **Indoor disconnect turned off or missing power** If the indoor unit has a disconnect switch and it is off when the outdoor unit powers up, the outdoor unit cannot see the indoor unit and throws E6.
- **Broken or shorted field wire** A communication conductor in the control cable between the units is open, shorted, or damaged by rodents or installation work.
- **Failed indoor control board** The indoor PCB is no longer sending a valid communication signal to the outdoor unit.
- **Failed outdoor control board** The outdoor PCB cannot properly receive or decode the signal from the indoor unit.

## Step-by-Step Fix {#fix}

1. **Turn off all power** to both the indoor and outdoor units at the breaker or disconnect. Wait a full three to five minutes to clear any stored faults, then restore power.
2. **Verify the startup sequence** by making sure the indoor disconnect (if present) is turned on before turning on the outdoor disconnect. Powering the outdoor unit first can trigger a communication fault.
3. **Inspect all terminal wiring** at the indoor and outdoor units. Verify that S1, S2, and S3 conductors are landed on the matching numbered terminals at both ends, that colors match, that screws are tight, and that no stray wire strands are touching adjacent terminals.
4. **Measure communication voltage** between terminals S2 and S3 with a multimeter set to DC volts. You should see a fluctuating DC voltage in the range of 10 to 24 VDC when the system is communicating normally. If the voltage is absent or steady, there is a communication failure.
5. **Check for line voltage** at the S1, S2, and S3 terminals to ground. Each should show approximately 120 VAC to ground. If any are missing, trace back for open wiring or a tripped breaker.
6. **Isolate the fault** by swapping or simulating one side of the communication link if you have a Mitsubishi checker tool. If the fault appears when simulating the indoor unit, suspect the outdoor board. If it appears when simulating the outdoor unit, suspect the indoor board. If neither reproduces the code, suspect the field wiring.
7. **Replace the failed component** once you have proven which board or wire segment is at fault. If voltage is correct and wiring is good but the code persists, replace the defective indoor or outdoor control board.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Indoor control board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-heat-pump-e6-error-code&k=Indoor+control+board+%28PCB%29&tag=errorcodefixes-20) \| Match the part number printed on your existing board or consult your model number. |
| Outdoor control board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-heat-pump-e6-error-code&k=Outdoor+control+board+%28PCB%29&tag=errorcodefixes-20) \| Match the part number printed on your existing board or consult your model number. |
| Communication cable (multi-conductor control wire) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-heat-pump-e6-error-code&k=Communication+cable+%28multi-conductor+control+wire%29&tag=errorcodefixes-20) \| Use Mitsubishi-approved or equivalent multi-conductor cable rated for the application if field wiring is damaged. |

## When to Call a Pro

E6 involves both line voltage (120 VAC at the terminals) and low-voltage control circuits. Misdiagnosing or miswiring these connections can damage expensive control boards or create a shock hazard. If you are not comfortable working with live AC voltage, measuring DC signals with a multimeter, or interpreting wiring diagrams, call a Mitsubishi-certified HVAC technician. A technician will have the proper test equipment and access to model-specific service manuals and communication checkers to isolate the fault quickly and replace only the failed component.
