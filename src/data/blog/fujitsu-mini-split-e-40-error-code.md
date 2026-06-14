---
title: "Fujitsu E:40 Error Code - Causes & Fix"
description: "E:40 on a Fujitsu mini split means the indoor and outdoor units lost communication. Check wiring and connectors first."
pubDatetime: 2026-05-31T01:41:17Z
modDatetime: 2026-05-31T01:41:17Z
author: "James Rutherford"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - fujitsu
money_part: "Indoor controller PCB"
most_likely_cause: "Loose or disconnected interconnect wiring"
---

## Fujitsu E:40 Error Code — What It Means

The E:40 code signals a DC communication fault between your indoor evaporator unit and outdoor condenser. The two halves of the system cannot exchange control signals at startup, so the system shuts down to protect itself. This belongs to Fujitsu's communication-error family, where the indoor controller PCB and outdoor PCB have lost their data link.

[Jump to Fix](#fix)

## Common Causes

- **Loose or disconnected interconnect wiring** The low-voltage control cable running between the indoor and outdoor unit has come loose, been nicked, or was miswired during installation.
- **Loose connector plugs on PCBs** Push-on connectors at the indoor controller board, outdoor board, or external I/O board have backed out or corroded.
- **Failed controller or inverter PCB** The main board in either the indoor or outdoor unit has failed and can no longer send or receive communication signals.
- **Voltage drop or poor grounding** Inadequate power supply or a missing or corroded ground connection disrupts the DC communication path.
- **Open sensor wiring** On some platforms, a break in sensor wiring can prevent the board from reading expected signals and trigger a communication fault.
- **Reversed or shorted control conductors** Installation errors that swap communication wires or create a short will block the signal between units.

## Step-by-Step Fix {#fix}

1. **Power off the system** at the breaker or disconnect, wait thirty seconds, then restore power and observe whether the E:40 returns after a full boot cycle.
2. **Consult your model's service manual** to confirm the exact definition and any sub-code variations, since Fujitsu fault displays differ across platform families and multi-split configurations.
3. **Inspect the interconnect cable** between indoor and outdoor units for cuts, pinches, loose terminations, or reversed wiring, and verify that all conductors are landed on the correct terminals.
4. **Check every connector** on the indoor controller PCB, outdoor main or inverter PCB, and any external I/O board by unplugging and reseating each connector to remove corrosion or partial insertion.
5. **Measure supply voltage and ground continuity** at both the indoor and outdoor boards to confirm proper power delivery and that the ground path is intact.
6. **Substitute the suspected PCB** if all wiring and connections test good, starting with the indoor controller board or outdoor inverter board depending on which side the manual flags for your model.
7. **Restore power and run a test cycle** to verify that communication resumes and the error clears, then monitor for twenty-four hours to confirm the repair is stable.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Indoor controller PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-40-error-code&k=Indoor+controller+PCB&tag=errorcodefixes-20) \| Required when the indoor unit's main board has failed. Match the full model and serial number to the parts list. |
| Outdoor inverter PCB or main PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-40-error-code&k=Outdoor+inverter+PCB+or+main+PCB&tag=errorcodefixes-20) \| Required when the outdoor unit's control board cannot communicate. Confirm the board type from your model's schematic. |
| External I/O PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-40-error-code&k=External+I%2FO+PCB&tag=errorcodefixes-20) \| Used on certain multi-split or zoned systems. Replace if this intermediate board is loose or damaged. |
| Interconnect wiring harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-40-error-code&k=Interconnect+wiring+harness&tag=errorcodefixes-20) \| Needed if the control cable between units is cut, pinched, or has damaged connectors. Use Fujitsu OEM cable for compatibility. |

## When to Call a Pro

Call a licensed HVAC technician if the error persists after reseating connectors and checking wiring, or if you are not comfortable working inside 240 V equipment and diagnosing low-voltage control circuits. PCB replacement and communication troubleshooting require a multimeter, the factory service manual, and familiarity with Fujitsu's board architecture. A pro can also verify that your installation meets code for grounding and power supply, which are common external causes of communication faults.
