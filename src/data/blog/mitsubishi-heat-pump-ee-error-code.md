---
title: "Mitsubishi EE Error Code - Causes & Fix"
description: "EE means indoor-outdoor communication fault on Mitsubishi heat pumps. Most likely fix: check wiring between units and power-cycle the system."
pubDatetime: 2026-05-31T08:49:53Z
modDatetime: 2026-05-31T08:49:53Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - hvac
  - mini-split
  - mitsubishi
---

## Mitsubishi EE Error Code — What It Means

On Mitsubishi Electric heat pumps and mini-splits, the EE error code almost always indicates an indoor-outdoor communication fault. This means the control boards in your indoor and outdoor units have lost the ability to talk to each other over the interconnecting wiring. The code is particularly common on Ecodan-style systems after a power cut or brownout, where the controllers fail to re-establish their handshake when power returns.

In rare cases on certain model families, EE can indicate a drive memory chip or EPROM fault on the outdoor inverter board, but that interpretation is less common and must be confirmed against your exact model's service manual before ordering parts. The vast majority of EE faults trace back to wiring issues or control board failures on the communication circuit.

[Jump to Fix](#fix)

## Common Causes

- **Loose or damaged communication wiring** The most common cause is a loose, open, reversed, or physically damaged wire in the interconnecting harness between indoor and outdoor units.
- **Power interruption or brownout** A recent outage or voltage dip can cause the control boards to lose their communication state and fail to re-sync when power returns, especially on Ecodan systems.
- **Failed indoor or outdoor control board** A failed communication circuit on either the indoor controller PCB or the outdoor main board will prevent handshaking between units.
- **Corroded or poorly terminated connectors** Water intrusion, oxidation, or loose terminals at the control board connectors or terminal blocks disrupt the low-voltage communication signal.
- **Corrupted memory or drive PCB fault** On models where EE actually indicates an EPROM or EEPROM issue, the outdoor inverter drive board or its memory chip has failed or become corrupted.

## Step-by-Step Fix {#fix}

1. **Confirm the exact code and model family** by checking the indoor controller display, outdoor PCB LED indicators, and your unit's service manual before starting diagnosis or ordering parts.
2. **Power-cycle the entire system properly** by shutting off power to both the indoor and outdoor units at their dedicated breakers, waiting at least five minutes, then restoring power in sequence and checking whether the fault clears.
3. **Inspect the communication wiring** between indoor and outdoor units for continuity, correct landing at terminal blocks, tight connections, and any signs of physical damage, pinching, or rodent damage.
4. **Check all connectors and terminal blocks** on both the indoor controller board and the outdoor main PCB for corrosion, loose pins, oxidation, or water intrusion, and clean or reseat connections as needed.
5. **Test by substitution if the fault persists** after wiring checks by temporarily swapping the indoor or outdoor control board (starting with whichever is easier to access) to isolate the failed communication circuit.
6. **Do not repeatedly reset the fault** if the code returns immediately after clearing, because a recurring EE code almost always indicates a hard wiring or board failure that requires repair, not just a reset.
7. **Consult your model's service manual** if your unit uses EE for a drive memory or EPROM fault, and follow the manufacturer's procedure for testing or replacing the outdoor inverter PCB and its memory components.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Indoor control board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-heat-pump-ee-error-code&k=Indoor+control+board+%28PCB%29&tag=errorcodefixes-20) \| Order by exact model number if communication diagnostics point to the indoor controller. |
| Outdoor main control board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-heat-pump-ee-error-code&k=Outdoor+main+control+board+%28PCB%29&tag=errorcodefixes-20) \| Most common replacement for persistent EE faults after wiring is verified intact. |
| Interconnecting communication harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-heat-pump-ee-error-code&k=Interconnecting+communication+harness&tag=errorcodefixes-20) \| Replace if wiring is physically damaged, corroded, or shows signs of shorts or opens. |
| Outdoor inverter drive PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-heat-pump-ee-error-code&k=Outdoor+inverter+drive+PCB&tag=errorcodefixes-20) \| Only needed if your exact model uses EE for EPROM/memory faults, confirmed by service literature. |

## When to Call a Pro

Call a qualified Mitsubishi technician if you are not comfortable working with low-voltage control wiring or live electrical panels, if the fault returns after a proper power cycle and visual wiring inspection, or if you need to test or replace control boards. Communication faults require methodical electrical diagnosis and often board-level troubleshooting that is difficult without the correct service manual and diagnostic tools. Do not keep resetting the code if it recurs, because repeated communication failures can sometimes cause secondary faults or prevent the system from running safely. Use Mitsubishi's installer lookup to find a factory-trained service provider for your exact model family.
