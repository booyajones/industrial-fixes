---
title: "Goodman EE2 Error Code: Control Board Communication Fault Fix"
description: "Goodman EE2 error code means a control board communication fault. Diagnose wiring, power surges, and failed boards on Goodman, Amana, and Coleman HVAC systems."
pubDatetime: 2026-04-26T17:30:00Z
modDatetime: 2026-04-26T17:30:00Z
author: "ErrorCodeFixes"
slug: goodman-ee2-error-code
featured: false
draft: false
tags:
  - goodman
  - hvac
  - error-code
  - control-board
  - air-conditioner
---

## Goodman EE2 Error Code: What It Means

The **Goodman EE2 error code** signals a **control board communication fault** — the system's main control board cannot reliably exchange data with another module in the system, or the board itself has lost its internal operating state.

EE2 shows up on Goodman communicating systems where the outdoor unit, indoor unit, and thermostat share a data bus rather than simple 24VAC control signals. If that communication link breaks for any reason, the system throws EE2 and shuts down. The same control board platform appears in **Amana** and some **Coleman** products, so EE2 applies across those brands as well.

The error code has been trending on r/hvacadvice as more Goodman communicating systems age into their first major service cycle. Most threads resolve with one of three repairs: re-seating communication wiring, clearing a fault after a power surge, or replacing the control board. Homeowners who replace the board without confirming the wiring is correct often find the new board throws EE2 as well.

[Jump to Fix](#fix)

## Common Causes

- **Power surge or lightning.** A nearby surge can scramble the control board's processor state or damage the communication drivers on the board. The board may appear to run but cannot complete a valid communication handshake.
- **Communication wiring fault.** Loose, pinched, or incorrectly wired communication connections between the outdoor unit, air handler, and thermostat break the data loop and produce EE2.
- **Failed control board.** After a surge, chronic overheating, or just age, the control board's communication circuitry can fail outright. The board may power on but cannot establish the protocol handshake required to run the system.
- **Low or unstable 24VAC transformer supply.** Some Goodman communicating systems use the control voltage for both power and data transport. A weak transformer producing low or fluctuating 24VAC can cause intermittent EE2 faults that look like wiring problems.
- **Thermostat compatibility or firmware issue.** Installing an incompatible third-party thermostat or a communicating thermostat with old firmware can cause EE2 on communicating Goodman systems.
- **Moisture or corrosion on board connectors.** Condensation in the air handler cabinet or a pinhole leak in a refrigerant line can deposit moisture on control board connectors, increasing resistance and disrupting communication.

## Step-by-Step Diagnosis {#fix}

1. **Reset the system completely.** Turn off the thermostat, then turn off both the indoor and outdoor breakers. Wait 5 minutes. Restore power to the indoor unit first, then the outdoor, then turn on the thermostat. Many EE2 faults from momentary surges or glitches clear with a clean power cycle.

2. **Inspect all communication wire connections.** Find the communication terminal block on the indoor control board and the outdoor unit. Confirm each wire is fully seated under its terminal screw. Look for any wire that pulled out or has a damaged connector. Also check the thermostat base — a slightly loose wire there can produce intermittent EE2.

3. **Verify wiring against the installation diagram.** On communicating Goodman systems, the communication wires must land on specific terminals (often labeled A, B, C, or by color). Confirm the color-to-terminal assignment matches the installation manual, not a generic HVAC wiring reference.

4. **Check the 24VAC transformer output.** Measure transformer secondary voltage under load. It should read 24–28VAC. Below 22VAC under load suggests a weak or failing transformer that may be causing communication voltage to drop below the board's threshold.

5. **Inspect the control board for physical damage.** Look for burn marks, swollen capacitors, cracked solder joints, or moisture residue on the board. Any visible damage points to board replacement.

6. **Test with a known-good communicating thermostat.** If you have access to a compatible replacement stat, swap it in temporarily. If EE2 clears with the test stat, the original thermostat is the failure point.

7. **Confirm which board is at fault.** Some Goodman communicating systems will display which module is failing on the diagnostic LED pattern or the thermostat screen. A fault pointing specifically to the outdoor board, indoor board, or thermostat narrows the replacement to one component.

## How to Fix It

**Power surge or glitch** — A full power cycle (as described in step 1) clears this in many cases. If the system runs after a clean reset and EE2 does not return, no additional repair is needed. Watch for recurrence over the next week.

**Communication wiring fault** — Re-seat all connections at every termination point. Clip back and re-strip any wire end that looks oxidized or has a poor crimp. Confirm terminal screw torque. On longer runs, check for a staple or conduit fitting that may have damaged the cable.

**Weak transformer** — Replace the 24VAC transformer. These are universal parts and cost $15–$30. Match the VA rating on the original.

**Thermostat incompatibility or firmware** — Install only Goodman-compatible communicating thermostats listed in the system's installation manual. If using an approved stat, check the manufacturer's website for a firmware update.

**Failed control board** — If wiring is confirmed correct and EE2 persists, replace the control board. Source the exact board for your Goodman model — Amana-branded and Coleman-branded counterparts may use the same part number. Boards typically run $80–$200. Photograph all existing wiring before removing the old board.

## Parts You May Need

- [Goodman HVAC control board replacement](https://www.amazon.com/s?k=Goodman+HVAC+control+board&tag=errorcodefixes-20)
- [Amana furnace control board](https://www.amazon.com/s?k=Amana+furnace+control+board&tag=errorcodefixes-20)
- [24VAC transformer HVAC replacement](https://www.amazon.com/s?k=24VAC+transformer+HVAC+40VA&tag=errorcodefixes-20)
- [Communicating thermostat wire 4-conductor](https://www.amazon.com/s?k=thermostat+wire+4+conductor+18+gauge&tag=errorcodefixes-20)
- [Multimeter for HVAC voltage testing](https://www.amazon.com/s?k=multimeter+HVAC+voltage+testing&tag=errorcodefixes-20)

## When to Call a Technician

Call a licensed HVAC technician if the system reset and wiring inspection did not clear EE2, or if you confirmed a board failure but are not certain which board in the system failed. Replacing the wrong board wastes money and leaves the system down. A technician with a Goodman communicating system diagnostic tool can pull fault history and identify the failed component directly, saving the cost of a misdiagnosed repair.

## Related Error Codes

- [Goodman Furnace 4 Flashes: Open High Limit Device](/posts/goodman-furnace-4-flashes/)
- [Goodman Furnace 3 Flashes: Pressure Switch Fault](/posts/goodman-furnace-3-flashes/)
- [Goodman Complete HVAC Error Code Guide](/posts/goodman-furnace-error-codes/)
