---
title: "Daikin VRV / VRF U4 Error Code — Communication Fault Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-03-19T08:00:00Z
modDatetime: 2024-03-19T08:00:00Z
slug: daikin-vrv-vrf-u4-error-code
featured: false
draft: false
tags:
  - hvac
  - daikin
  - vrf
  - communication
  - commercial
description: "Daikin VRV/VRF U4 error code means a communication fault between indoor and outdoor units. This guide covers wiring, PCB, and configuration fixes for U4 on commercial Daikin VRF systems."
---

## Error Code: Daikin VRV/VRF U4

**What it means:** U4 on a Daikin VRV (Variable Refrigerant Volume) or VRF (Variable Refrigerant Flow) system indicates a communication fault. The outdoor unit and one or more indoor units have lost their data communication signal. Daikin's VRV systems continuously exchange operational data between all units on the refrigerant circuit — temperatures, valve positions, compressor speeds, modes. When that communication breaks, the affected units shut down and display U4.

This guide is specific to commercial Daikin VRV/VRF systems (REYQ, REYYQ, RXMQ, and similar multi-unit commercial configurations), which differ from residential mini-split installations in wiring topology, PCB complexity, and termination resistor requirements. The residential Daikin U4 code shares the same name but involves different diagnostic procedures.

VRF systems with U4 are genuinely complex to diagnose — a single wiring error or a single PCB failure can knock out all indoor units simultaneously. Systematic diagnosis, rather than component replacement, is the only efficient path.

## Common Causes

- **Broken, reversed, or disconnected communication wiring** — The F1/F2 (or S, S1/S2) communication bus wires running between the outdoor unit and all indoor units form a daisy-chain network. A single wire break, reversal, or open connection anywhere in the chain silences all downstream units.
- **Missing or incorrect termination resistors** — Daikin VRF systems require a termination resistor (typically 110–120 ohm) at the last indoor unit in each refrigerant branch. Without proper termination, signal reflections on the communication bus cause data errors. Many installers skip or misplace these resistors.
- **Incorrect wiring topology** — Daikin VRF systems require daisy-chain wiring, not star (home run) wiring. If communication wiring was installed in a star configuration from the outdoor unit to each indoor unit, communication errors are inevitable.
- **Failed outdoor unit PCB (main control board)** — The outdoor PCB is the communication master. A failed outdoor PCB causes U4 on every indoor unit simultaneously, because no master means no communication.
- **Failed indoor unit PCB** — A failed indoor PCB at one unit can disrupt communication to all downstream units on that branch. The disruption pattern (which units are affected) helps identify the faulty board.
- **Power supply issue at outdoor or indoor unit** — Some Daikin VRF architectures power the communication bus from the outdoor unit's internal 24V supply. A failed power supply board inside the outdoor unit drops the communication bus voltage, causing U4 across all units.
- **Interference or grounding issue** — Long communication wire runs near high-voltage cables, ungrounded equipment, or variable frequency drives can introduce noise that disrupts serial communication.

## Step-by-Step Fix {#step-by-step-fix}

1. **Map which units are showing U4 and which are not.** On a VRF system with multiple indoor units, note exactly which units display U4. If all units on a single refrigerant branch show U4 but units on other branches are fine, the problem is either in that branch's wiring or in the indoor unit at the head of that branch. If all units everywhere show U4, the outdoor PCB or its power supply is suspect.

2. **Verify all power supplies are correct.** Confirm the outdoor unit has full 3-phase power at the correct voltage (typically 208V or 460V 3-phase for commercial VRV). Confirm each indoor unit has correct single-phase power. An indoor unit with no power cannot communicate, and on some Daikin topologies, a de-powered indoor unit creates an open in the communication bus that affects all downstream units.

3. **Inspect the communication wiring at the outdoor unit terminal block.** Open the outdoor unit's electrical compartment. Locate the F1/F2 (or S terminal) communication bus connections. Verify the wires are: (a) securely terminated with no loose strands, (b) connected to the correct terminals (F1 to F1, F2 to F2 consistently throughout), and (c) not shorted to ground or to L1/L2/L3 power wires. A wiring photo taken before any changes is valuable here.

4. **Inspect communication wiring at each indoor unit.** At each indoor unit showing U4, check the F1/F2 terminal connections. In a daisy-chain configuration, the communication bus should come in from the previous unit on two terminals and leave to the next unit on the same two terminals. Any break in this chain disrupts all downstream units. Ensure termination resistors are installed only at the last indoor unit on each branch.

5. **Verify termination resistor installation.** Locate the last indoor unit in the communication chain. On that unit's PCB, confirm a jumper or discrete resistor is installed at the termination position (refer to the Daikin installation manual for the specific PCB model — the termination location varies). The resistor value is typically 110 ohms. No resistor at the end of the bus, or resistors installed at multiple points, both cause communication issues.

6. **Use Daikin's diagnostic mode on the outdoor unit.** Most commercial Daikin VRV systems have a built-in self-check routine accessible from the outdoor unit's control board LED display or via the DIP switch settings. Refer to the service manual for the specific outdoor unit model to access communication diagnostics. This mode can identify exactly which indoor unit addresses are not responding.

7. **Isolate sections of the communication bus.** If you cannot identify the fault location by inspection, methodically disconnect indoor units from the communication bus starting from the far end. After each disconnection, reset the system and check if U4 clears. When U4 clears after disconnecting a specific unit, either that unit's PCB is failed or there is a wiring fault at that connection point.

8. **Test PCBs using Daikin's LED diagnostic codes.** Both outdoor and indoor PCBs have LED arrays that display self-diagnostic codes during startup and operation. Power cycle the system and immediately observe the LED patterns on the outdoor PCB — the flash sequence identifies whether the board detected communication errors on initialization. Indoor PCBs similarly have LED status indicators. Consult the specific service manual for your VRV model series.

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Description | Typical Cost | [Where to Buy](https://www.amazon.com/s?k=Where%20to%20Buy&tag=errorcodefixe-20) |  |------|------------|-------------|-------------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Termination resistor (110 ohm) | Communication bus termination | [$2–$8](https://www.amazon.com/s?k=%242%E2%80%93%248&tag=errorcodefixe-20) | Electronics suppliers / Daikin parts |
| [Indoor unit PCB](https://www.amazon.com/s?k=Indoor%20unit%20PCB&tag=errorcodefixe-20) | Varies by indoor unit model | $180–$450 | [Daikin Distributor / Parts Town](https://www.amazon.com/s?k=Daikin%20Distributor%20%2F%20Parts%20Town&tag=errorcodefixe-20) |  | Outdoor unit main PCB | [Varies by outdoor unit model](https://www.amazon.com/s?k=Varies%20by%20outdoor%20unit%20model&tag=errorcodefixe-20) | $400–$1,200 | Daikin Distributor | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Outdoor unit power supply PCB | Internal DC power board | [$250–$600](https://www.amazon.com/s?k=%24250%E2%80%93%24600&tag=errorcodefixe-20) | Daikin Distributor |

## When to Call a Professional

Daikin VRV/VRF systems are among the most complex commercial HVAC systems in the field. PCB replacement on commercial VRF outdoor units requires Daikin factory training and access to their technical service resources. Incorrect PCB handling (ESD damage, wrong replacement board) on a commercial outdoor unit can result in a $10,000+ write-off. If the above diagnostic steps don't isolate the communication fault, contact Daikin's commercial technical support line (1-855-324-5462) or a Daikin-authorized VRF service contractor. Many regions have Daikin factory-authorized service centers with remote diagnostics capabilities via the VRV system's BACnet or Modbus interface.

> **Pro tip:** The most common installation error causing U4 on commercial Daikin VRF is star-wired communication cabling. Installers familiar with residential or light commercial work sometimes run a separate wire from the outdoor unit to each indoor unit, creating a star topology. Daikin VRF requires a true daisy-chain — one continuous bus from the outdoor unit through each indoor unit in sequence, terminating at the last unit. If U4 appeared from day one of commissioning, photograph the communication wiring before touching anything. A star topology is immediately visible in the photo and avoids hours of PCB chasing.
