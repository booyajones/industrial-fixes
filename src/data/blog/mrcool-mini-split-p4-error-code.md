---
title: "MRCOOL P4 Error Code - Causes & Fix"
description: "P4 signals an inverter/compressor fault in the outdoor unit. Most often caused by closed service valves or loose refrigerant lines."
pubDatetime: 2026-05-31T07:59:00Z
modDatetime: 2026-05-31T07:59:00Z
author: "James Rutherford"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - mrcool
---

## MRCOOL P4 Error Code — What It Means

The P4 (or PC04) error code on a MRCOOL mini split indicates an inverter or compressor-related fault in the outdoor unit. The system has detected an abnormal condition in the compressor drive circuit, which may be caused by refrigerant line problems, electrical issues, or a failure in the outdoor control board or compressor itself. This code is a protective shutdown to prevent further damage.

The fault typically involves either the physical refrigerant circuit (line connections, service valves) or the electrical path powering the compressor (inverter board, wiring, voltage supply). MRCOOL's own troubleshooting protocol points technicians to verify line-set connections, communication wiring, and then the outdoor board and compressor circuit if the code persists.

[Jump to Fix](#fix)

## Common Causes

- **Closed or partially open service valves** The king valves at the outdoor unit condenser were not fully opened after installation or service, restricting refrigerant flow and triggering compressor protection.
- **Loose or improperly torqued refrigerant line connections** Flare or compression fittings at the condenser or air handler are not fully tightened, causing pressure loss or allowing air into the system.
- **Miswired or damaged communication cable** The low-voltage wiring between indoor and outdoor units is reversed, misrouted, or has a loose terminal, preventing proper control signals to the inverter.
- **Supply voltage out of specification** The incoming line voltage to the outdoor unit is abnormally high or low, causing the inverter drive to fault or the compressor to draw unsafe current.
- **Failed outdoor inverter board or IPM module** Components on the outdoor control board, including the intelligent power module that drives the compressor, have burned out or become damaged.
- **Compressor winding fault or internal failure** The compressor windings show unequal resistance, a short to ground, or mechanical seizure, making it electrically or mechanically out of specification.

## Step-by-Step Fix {#fix}

1. **Confirm the fault code** at the indoor air handler display or outdoor unit screen to verify you are seeing P4 or PC04, not a different error.
2. **Turn off power** to both the indoor and outdoor units at the breaker or disconnect before opening any electrical compartments or touching wiring.
3. **Check the outdoor service valves.** Locate the two king valves on the refrigerant lines at the condenser and turn each stem counterclockwise with a hex key until fully seated open, then back off slightly per the installation manual.
4. **Inspect and tighten all refrigerant line connections** at both the outdoor condenser ports and the indoor unit flare fittings, using two wrenches to avoid twisting the tubing.
5. **Verify communication wiring** between indoor and outdoor units by tracing the low-voltage control cable, checking that terminals are tight, wires are not reversed, and insulation is intact with no nicks or burns.
6. **Perform a CE reset** if wiring or valve changes were made: with power restored, press and hold the black button on the outdoor unit until the display reads CE, then wait about 20 minutes without adjusting settings to allow the system to self-configure.
7. **Measure supply voltage** at the outdoor unit's line terminals with a multimeter while the unit is powered, comparing the reading to the nameplate specification to rule out utility or wiring voltage problems.
8. **Test compressor windings** if the code persists: disconnect power, unplug the compressor connector from the outdoor board, and use an ohmmeter to check resistance between each pair of compressor pins and from each pin to the compressor shell (ground). Unequal resistances or any continuity to ground indicate a failed compressor.
9. **Inspect the outdoor control board and inverter module** for burn marks, bulging capacitors, loose connectors, or signs of water intrusion, and replace the board if damage is visible or if all other checks pass but the fault remains.

## Parts Often Needed

| Part | Notes |
|------|-------|
| MRCOOL outdoor control board (inverter board) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mrcool-mini-split-p4-error-code&k=MRCOOL+outdoor+control+board+%28inverter+board%29&tag=errorcodefixes-20) \| Match the exact model number printed on your existing board or listed in your outdoor unit's service manual. |
| MRCOOL compressor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mrcool-mini-split-p4-error-code&k=MRCOOL+compressor&tag=errorcodefixes-20) \| Order by outdoor unit model and serial number. Confirm winding fault with ohmmeter test before purchasing. |
| Mini split flare nut wrench set | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mrcool-mini-split-p4-error-code&k=Mini+split+flare+nut+wrench+set&tag=errorcodefixes-20) \| Thin-wall wrenches sized for refrigerant line fittings, typically 3/8", 1/2", 5/8", and 3/4". |

## When to Call a Pro

Call a licensed HVAC technician if you are not comfortable working with live electrical circuits, handling refrigerant lines, or using a multimeter. Compressor winding tests and inverter board diagnosis require specialized tools and EPA 608 certification if refrigerant recovery is needed. If you have opened the service valves, tightened all line connections, corrected the communication wiring, and performed a CE reset but the P4 code returns immediately on startup, the fault is likely internal to the outdoor board or compressor and requires professional replacement and refrigerant handling. Do not attempt to disassemble the sealed refrigerant circuit or replace the compressor without proper licensing and evacuation equipment.
