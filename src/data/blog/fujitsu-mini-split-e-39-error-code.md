---
title: "Fujitsu E:39 Error Code - Causes & Fix"
description: "E:39 means communication failure between indoor and outdoor units. Check wiring and connectors first-usually a loose plug or bad PCB."
pubDatetime: 2026-05-31T01:07:30Z
modDatetime: 2026-05-31T01:07:30Z
author: "Marcus Webb"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - fujitsu
money_part: "Fujitsu outdoor main PCB (control board)"
---

## Fujitsu E:39 Error Code — What It Means

The E:39 error code on Fujitsu mini-splits indicates a communication or transmission fault between the indoor evaporator unit and the outdoor condenser unit. At startup, the two units are not exchanging data correctly. This prevents the system from operating because the control boards cannot coordinate compressor speed, fan operation, and refrigerant flow.

Fujitsu's troubleshooting material describes this as a communication error where the evaporator and condenser are not communicating. The system fault can stem from field wiring problems, connector issues, incompatible unit pairing, or failed control boards. Because communication must be established before the system runs, this code typically appears immediately after power-up or when attempting to start a cooling or heating cycle.

[Jump to Fix](#fix)

## Common Causes

- **Loose or disconnected wiring connectors** The most common cause is a loose molex plug or connector between the indoor and outdoor units, or at the PCB terminals themselves.
- **Damaged or miswired interconnect cable** The low-voltage control cable between indoor and outdoor units may have damaged insulation, an open conductor, or incorrect polarity at the terminal blocks.
- **Incompatible or incorrectly paired indoor unit** Fujitsu systems require matching indoor and outdoor models, and an incorrect indoor unit type or addressing error will prevent communication.
- **Failed outdoor main PCB** The main control board in the outdoor condenser unit may have a failed communication circuit or microprocessor.
- **Failed indoor controller PCB** The indoor unit's controller board can fail in its communication section, preventing it from sending or receiving data.
- **Power interruption during startup sequence** A brief power loss or voltage sag during the initial handshake between units can leave the system in a communication fault state that persists until reset.

## Step-by-Step Fix {#fix}

1. **Power-cycle the system** by turning off the breaker or disconnect for at least two minutes, then restore power and attempt to restart. Many transient communication faults clear after a full reset.
2. **Inspect all field wiring** between the indoor and outdoor units. Look for damaged insulation, pinched cables at wall penetrations, loose terminal screws, or reversed polarity on the low-voltage control wires.
3. **Check every connector and molex plug** at both the indoor controller PCB and the outdoor main PCB. Reseat each connector firmly and inspect pins for corrosion, bent contacts, or backing-out from the housing.
4. **Verify indoor and outdoor unit compatibility** by checking model numbers against Fujitsu's pairing charts. Confirm that any DIP switches or addressing jumpers on the indoor unit are set correctly for multi-zone or single-zone operation.
5. **Test communication wiring continuity** using a multimeter. With power off, measure resistance across each conductor of the control cable from indoor to outdoor terminals. An open or high-resistance reading indicates a break in the cable.
6. **Isolate the failed PCB** by swapping the indoor unit with a known-good unit (if available on a multi-zone system) or by consulting Fujitsu's board-level diagnostics. If the fault follows the indoor unit, replace the indoor controller PCB. If it stays with the outdoor unit, replace the outdoor main PCB.
7. **After any wiring or board repair**, restore power and monitor the system through several startup cycles to confirm stable communication and normal operation.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Fujitsu outdoor main PCB (control board) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-39-error-code&k=Fujitsu+outdoor+main+PCB+%28control+board%29&tag=errorcodefixes-20) \| Match the exact board part number printed on your current outdoor unit PCB. Varies by model and tonnage. |
| Fujitsu indoor controller PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-39-error-code&k=Fujitsu+indoor+controller+PCB&tag=errorcodefixes-20) \| Specific to your indoor unit model. Verify compatibility with your remote control type and wireless module if equipped. |
| Low-voltage interconnect cable (shielded multi-conductor) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-39-error-code&k=Low-voltage+interconnect+cable+%28shielded+multi-conductor%29&tag=errorcodefixes-20) \| Use Fujitsu-approved communication cable if replacing the field wiring. Length and conductor count depend on your installation. |

## When to Call a Pro

Call a licensed HVAC technician if you are not comfortable working with low-voltage control wiring or printed circuit boards. Communication faults require methodical isolation of wiring, connectors, and control boards, and misdiagnosis can lead to unnecessary part replacement. A qualified technician has the tools to test communication signals, verify unit pairing, and access Fujitsu's service documentation for board-level diagnostics. If the fault persists after a power reset and basic connector inspection, professional diagnosis will save time and money. Refrigerant-side work is not typically involved in E:39 faults, but verifying correct indoor/outdoor pairing and replacing control boards should be done by someone trained on Fujitsu inverter systems.
