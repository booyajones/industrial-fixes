---
title: "Goodman 1 Flash Error Code — What It Means"
description: "What Goodman 1 flash status LED means, why it indicates normal operation, and what to check if your furnace still isn't heating."
pubDatetime: 2026-04-22T12:00:00Z
modDatetime: 2026-04-22T12:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - goodman
---

## Goodman 1 Flash Error Code — What It Means

On Goodman furnaces, **1 flash on the status LED indicates normal operation with no call for heat**. This is not a fault code — it's a standby indicator. The furnace is powered, the control board is healthy, and the system is simply waiting for a thermostat demand. If you're seeing 1 flash and the furnace is not heating when it should be, the issue is upstream of the board: thermostat, wiring, or the call for heat signal itself.

[Jump to Fix](#fix)

## Why the Furnace Isn't Heating Despite 1 Flash

- **No thermostat demand** — The thermostat isn't sending a heat call (W signal). Could be a temperature setting, wiring, or thermostat fault.
- **Thermostat wiring issue** — A loose or broken wire at the furnace's W terminal means the board never receives the heat command.
- **Open door safety switch** — The furnace cabinet door must be fully closed to engage the interlock switch. Board powers up but won't fire without the door switch closed.
- **Tripped circuit breaker or blown fuse** — The board has power (hence 1 flash), but the gas valve or ignitor circuit may be on a separate fused circuit.

## Step-by-Step Fix {#fix}

1. **Verify thermostat is calling for heat** — Set the thermostat 5°F above room temperature and confirm the display shows a heat demand (flame icon or "Heat On"). If the thermostat shows demand but the furnace doesn't respond, proceed.
2. **Check the W terminal at the furnace** — Remove the thermostat wiring cover at the furnace and confirm the W wire is securely fastened to the W terminal on the control board.
3. **Verify the door switch** — Press and hold the door switch manually with the door open. If the furnace fires, the door isn't fully engaging the switch; adjust the door or the switch bracket.
4. **Check the low-voltage fuse** — Most Goodman boards have a 3A or 5A blade fuse on the board. A blown fuse will keep the board in standby but prevent any outputs from operating.
5. **Test for 24V at the W terminal** — With a thermostat heat call active, measure voltage between W and C at the board. You should see approximately 24V AC. No voltage = thermostat or wiring fault.
6. **Reset and confirm** — After any repairs, restore power and confirm the status LED changes from 1 flash to the normal operating sequence (no flash or continuous on) during a heating cycle.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [Control board fuse (3A or 5A)](https://www.amazon.com/s?k=Control%20board%20fuse%20(3A%20or%205A)&tag=errorcodefixe-20) | Small ATO/ATC blade fuse on the board; always replace with same rating |
| [Door interlock switch](https://www.amazon.com/s?k=Door%20interlock%20switch&tag=errorcodefixe-20) | Push-button switch on the blower compartment; inexpensive and easy to replace |
| [Thermostat](https://www.amazon.com/s?k=Thermostat&tag=errorcodefixe-20) | If thermostat isn't generating the 24V W signal |

## When to Call a Pro

A 1-flash condition means the board itself is healthy — if you've confirmed the thermostat is calling for heat, all wiring is secure, and the door switch closes properly, but the furnace still won't initiate a heating cycle, there may be a soft lockout condition from a prior fault. Have a technician read the full fault history from the board to identify what tripped it.
