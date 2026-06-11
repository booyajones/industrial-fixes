---
title: "Daikin U4 Error Code - Causes & Fix"
description: "U4 means the indoor and outdoor units can't communicate. Check loose wiring connections and power to both units first."
pubDatetime: 2026-05-31T08:57:30Z
modDatetime: 2026-05-31T08:57:30Z
author: "Marcus Webb"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - daikin
money_part: "Indoor control PCB"
---

## Daikin U4 Error Code — What It Means

The U4 code indicates a communication fault between your indoor and outdoor units. The control system is not seeing valid signals over the interconnecting wiring that links the two halves of your heat pump. This is not a refrigerant problem. It is a transmission interruption that prevents the units from coordinating their operation.

[Jump to Fix](#fix)

## Common Causes

- **Loose or broken transmission wiring** Disconnected terminals, damaged conductors, reversed polarity, or a severed communication line are the most frequently reported causes of U4.
- **Power supply interruption** One unit may be without proper power due to a tripped breaker, blown fuse, or an open disconnect, which can present as a communication fault.
- **Failed control board** The indoor PCB, outdoor PCB, or inverter board may have failed and can no longer send or receive signals on the communication bus.
- **Installation or configuration error** Incorrect address settings, wrong DIP switch positions, or missing line termination on multi-zone systems can trigger U4, especially after new installs or service work.
- **Component leaking to ground** Field technicians report that a component with an internal short can damage the outdoor board and stop communication, though this is less common than wiring faults.

## Step-by-Step Fix {#fix}

1. **Verify power at both units.** Check breakers, fuses, and disconnects for the indoor and outdoor units, then measure line voltage to confirm both units are receiving supply (typically 208 to 240 V AC).
2. **Inspect interconnect wiring end to end.** Look for loose terminals, corroded connections, reversed conductors, pinched or cut wires, and any signs of damage or miswiring at both the indoor and outdoor terminal blocks.
3. **Confirm system configuration on multi-zone setups.** Verify unit address settings, DIP switches, and any required termination resistors match the installation manual for your model.
4. **Power-cycle the system.** Turn off power at the breakers for both units, wait two minutes, then restore power to clear any transient communication lockup.
5. **Test communication circuit voltage.** With the system powered, measure DC voltage on the communication terminals (one field example shows approximately 53 to 55 V DC from terminal 3 to ground, but consult your model's service manual for the correct reference).
6. **Check interconnect cable resistance.** Disconnect power and measure resistance along the communication wiring, which should read in the megaohm range when healthy; kilohm or lower readings suggest a fault in the cable.
7. **Isolate and replace the failed component.** If wiring and power checks pass, test each board by disconnecting accessories or swapping known-good boards, then replace only the verified faulty part (indoor PCB, outdoor PCB, or interconnect cable).

## Parts Often Needed

| Part | Notes |
|------|-------|
| Indoor control PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-heat-pump-u4-error-code&k=Indoor+control+PCB&tag=errorcodefixes-20) \| Replace if communication voltage is absent at the indoor unit and wiring integrity is confirmed. |
| Outdoor control or inverter PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-heat-pump-u4-error-code&k=Outdoor+control+or+inverter+PCB&tag=errorcodefixes-20) \| Replace if the outdoor unit shows no communication output and power supply is verified; noise filter boards may also be involved in some field cases. |
| Transmission interconnect cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-heat-pump-u4-error-code&k=Transmission+interconnect+cable&tag=errorcodefixes-20) \| Replace if the cable shows low resistance (kilohms or below) or visible damage between indoor and outdoor units. |

## When to Call a Pro

Call a qualified HVAC technician if you are not comfortable working with live 240 V power, if the communication wiring passes all visual and meter checks but the code persists, or if you need to test or replace control boards. Technicians have the tools to measure communication signals, isolate board-level faults, and verify correct multi-zone configurations. Do not replace expensive boards until power, wiring integrity, and system setup have been verified by someone trained in Daikin diagnostics.

## See Also

- [Daikin Mini Split Ice on Coils - Causes & Fix](/posts/daikin-mini-split-ice-on-coils/)
- [Daikin UA Error Code — Mismatched Indoor/Outdoor Unit Fix](/posts/daikin-error-code-uA/)
- [Daikin E7 Error Code — Outdoor Fan Motor Fault Fix](/posts/daikin-e7-error-code/)
- [Daikin L5 Error Code — Compressor Lock Fix](/posts/daikin-error-code-l5/)
