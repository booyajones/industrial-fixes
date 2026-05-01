---
title: "Mitsubishi Mini Split E6 Error Code — Communication Error Indoor/Outdoor Fix"
author: "Dana Kowalski"
pubDatetime: 2026-04-26T17:00:00Z
modDatetime: 2026-04-26T17:00:00Z
slug: mitsubishi-mini-split-e6-error
featured: false
draft: false
tags:
  - mini-split
  - mitsubishi
  - hvac
  - communication-error
description: "Mitsubishi mini split E6 error means the indoor and outdoor units have lost communication. Learn how to diagnose wiring, control boards, and fix E6 on MSZ and MXZ systems."
---

## Error Code: Mitsubishi Mini Split E6

**What it means:** The E6 error code on Mitsubishi mini split systems signals a communication fault between the indoor and outdoor units. The indoor control board is sending data signals over the inter-unit wiring, but the outdoor unit is not responding — or vice versa. The system shuts down as a safety measure since it cannot coordinate compressor speed, fan speed, and refrigerant flow without a valid communication link.

E6 is one of the most frustrating Mitsubishi fault codes because it can stem from a wide range of causes: simple wiring issues, a blown fuse on the outdoor board, control board failure, or even electromagnetic interference. Mitsubishi's MSZ, MUZ, and MXZ multi-zone systems all share the same S-Bus serial communication protocol, making systematic diagnosis essential.

## Common Causes

- **Loose or reversed inter-unit wiring** — The 3-wire (or 4-wire on multi-zone) communication cable between indoor and outdoor units has come loose at a terminal block, is reversed, or has corroded connections.
- **Blown control board fuse** — A small glass or blade fuse on the outdoor unit's control board has blown due to a transient voltage spike, protecting the board but killing communication.
- **Damaged communication wire** — The communication wire (typically connected to terminals 1, 2, and 3 on both units) has been nicked, pinched, or damaged during installation or by rodents.
- **Failed outdoor control board** — The outdoor PCB has failed, rendering it unable to process or respond to communication signals from the indoor unit.
- **Failed indoor control board** — Less common, but the indoor PCB can also lose its communication output circuitry.
- **Electrical interference or power quality issues** — Poorly grounded electrical systems or nearby variable frequency drives (VFDs) and other high-EMF equipment can corrupt the communication signal.

## Step-by-Step Diagnosis {#step-by-step-fix}

1. **Power cycle the system completely.** Turn off the mini split at the remote, then switch off the breaker to both the indoor and outdoor units. Wait 5 full minutes to allow capacitors to discharge. Restore power to the outdoor unit first, then the indoor unit. Watch for E6 to reappear.

2. **Inspect the inter-unit communication wiring.** With power off, open the electrical access panel on both the indoor and outdoor units. Locate the terminal strip (labeled S1, S2, S3 or 1, 2, 3 depending on model). Check that each wire is:
   - Firmly seated in its terminal (use a small flathead to tighten)
   - Connected to the correct terminal number at both ends
   - Free from corrosion (green or white oxidation on copper = clean or replace the terminal)

3. **Check for a blown fuse on the outdoor board.** Mitsubishi outdoor units have a small fuse on the main PCB, often labeled F1 or FU1. It is typically rated 3.15A or 6.3A. With power off, remove and test with a multimeter set to continuity mode. Replace if blown (use exact rating).

4. **Inspect the communication wire run.** Trace the entire length of the inter-unit wiring from the indoor unit to the outdoor unit. Look for pinch points, areas where wire passes through a wall or conduit, any signs of animal damage or melted insulation. A damaged wire segment can be spliced with proper weatherproof connectors if the run is accessible.

5. **Swap communication wire terminals.** On some installations where E6 followed a DIY repair or accessory install, terminals 2 and 3 may be swapped. Double-check the wiring diagram in your installation manual (or download it from Mitsubishi's technical literature library) and verify the color-coding matches.

6. **Test the outdoor board fuse and control board.** If wiring checks out, the fault is likely in the outdoor PCB. A technician can use a Mitsubishi service tool (SG-K900AT or equivalent) to read active fault codes and board status, which can confirm a board failure.

## How to Fix It

- **Loose or corroded terminals:** Re-terminate wires, apply anti-corrosion electrical grease, and torque terminals to spec. This resolves a large percentage of E6 faults.
- **Blown fuse:** Replace the fuse with an exact match. If the new fuse blows immediately, there is a short circuit downstream — stop and call a technician.
- **Damaged wire:** Replace the inter-unit communication cable. Use the wire gauge and type specified in the Mitsubishi installation manual (typically 14–18 AWG stranded copper).
- **Failed outdoor PCB:** Replace the outdoor control board. This is a moderately expensive part ($150–$400+ depending on model) but a straightforward swap if you document the wiring before removal.
- **Failed indoor PCB:** Less common — confirm via a technician's diagnostic tool before replacing.

## Parts You May Need

- [Mitsubishi Outdoor Control Board PCB](https://www.amazon.com/dp/B0CNZGZ1HS?tag=errorcodefixes-20)
- [Mitsubishi Indoor Control Board PCB](https://www.amazon.com/dp/B0CNZGZ1HS?tag=errorcodefixes-20)
- [Mini Split Inter-Unit Communication Wire 14 AWG](https://www.amazon.com/s?k=mini+split+communication+wire+14+AWG&tag=errorcodefixes-20)
- [PCB Fuse Assortment 3.15A 6.3A Glass Fuse](https://www.amazon.com/s?k=PCB+glass+fuse+3.15A+6.3A+replacement&tag=errorcodefixes-20)
- [Electrical Terminal Corrosion Inhibitor](https://www.amazon.com/s?k=electrical+terminal+corrosion+inhibitor+anti-oxidant&tag=errorcodefixes-20)

## When to Call a Technician

If you have verified all wiring connections, replaced any blown fuses, and the E6 code persists, the fault is almost certainly a failed control board — either indoor or outdoor. Pinpointing which board has failed without a Mitsubishi diagnostic tool is difficult. A certified technician can connect the SG-K900AT or compatible service tool to read board status registers and identify the failed component definitively. Control board replacement is a reasonable DIY task for experienced technicians, but purchasing the wrong board or incorrectly transferring wiring will create new problems. For multi-zone MXZ systems with multiple indoor heads, incorrect communication wiring across multiple units adds further complexity.

## Related Error Codes

- [Mitsubishi Mini Split U4 Error Code — Outdoor Thermistor Fault](/posts/mitsubishi-mini-split-u4-error-code/)
- [Mitsubishi Mini Split P8 Error Code — Outdoor Heat Exchanger Overtemp](/posts/mitsubishi-mini-split-p8-error/)
- [Mitsubishi Mini Split E1 Error Code — Indoor Thermistor Fault](/posts/mitsubishi-mini-split-e1-error/)
