---
title: "Daikin E6 Error Code - Causes & Fix"
description: "E6 on Daikin heat pumps means compressor motor overcurrent or lock. Most often a failed compressor or outdoor control PCB."
pubDatetime: 2026-06-20T12:44:12Z
modDatetime: 2026-06-20T12:44:12Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - hvac
  - mini-split
  - daikin
money_part: "Daikin outdoor unit compressor"
most_likely_cause: "compressor mechanical failure or lock"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify all stop valves (service valves) on the outdoor unit refrigerant lines are fully open"
  - "Check supply voltage at the outdoor disconnect for proper phase balance if the system is three-phase"
---

## What this code means
E6 on most Daikin heat pump systems indicates a compressor motor overcurrent or compressor lock fault. Daikin describes this code as STD compressor motor overcurrent/lock or faulty compressor start up, depending on the product family. The error appears when the outdoor unit's compressor cannot start properly, draws excessive current, or experiences a mechanical lock condition. Because Daikin uses the same code letter across different model families with slightly different meanings, always confirm the exact definition in your model's service manual.

This is an outdoor-unit protection fault, not a room sensor or indoor-unit issue. The system shuts down to prevent damage to the compressor drive circuit, inverter PCB, or compressor windings. Common triggers include a mechanically locked compressor, shorted compressor windings, inverter or control PCB failure, supply voltage imbalance on three-phase systems, wiring or connector faults between the outdoor PCB and compressor, or service valves left closed after installation or maintenance.

## Before You Replace Anything

Homeowners and some techs replace the outdoor control PCB first, but a locked or shorted compressor is often the real cause. Always isolate the compressor from the board and measure winding resistance and insulation before condemning the PCB.

## Common Causes

- **Compressor mechanical lock or internal seizure (~40%)** Bearings or internal components bind, preventing the motor from turning and triggering overcurrent protection.
- **Compressor winding short or defect (~25%)** Shorted or damaged motor windings cause excessive current draw during start or run, immediately tripping the inverter.
- **Inverter PCB or outdoor control board failure (~20%)** Failed drive transistors, current sensors, or control circuits on the outdoor board send incorrect signals or fail to regulate compressor current.
- **Wiring, connector, or contact fault between PCB and compressor (~10%)** Loose, corroded, or burned connections between the outdoor board, inverter section, and compressor terminals create high resistance or intermittent contact.
- **Stop valve or service valve not opened (~5%)** Refrigerant valves left closed after installation or service starve the compressor and cause abnormal current draw.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Did the E6 error appear immediately after installation or recent service work?</summary>
<div class="dtree-body"><strong>Yes:</strong> Check that all stop valves and service valves on the outdoor unit are fully opened. A closed valve is a known cause Daikin lists for this code.<br><strong>No:</strong> The fault is likely internal to the compressor or outdoor PCB. Proceed to voltage and resistance checks.</div>
</details>

<details class="dtree"><summary>Does the error return immediately every time you power-cycle the system?</summary>
<div class="dtree-body"><strong>Yes:</strong> A hard electrical fault (shorted winding, locked compressor, or failed inverter) is present. Professional diagnosis with winding-resistance and insulation testing is required.<br><strong>No:</strong> An intermittent wiring or connector issue may be present. Inspect all connections at the outdoor PCB, compressor terminals, and inverter section for corrosion or looseness.</div>
</details>

<details class="dtree"><summary>Is the outdoor unit on a three-phase power supply?</summary>
<div class="dtree-body"><strong>Yes:</strong> Measure phase-to-phase voltage at the outdoor disconnect. A difference of 14 V or more between any two phases indicates supply imbalance, which can trigger overcurrent faults.<br><strong>No:</strong> Focus diagnostic work on the compressor windings, inverter PCB, and wiring between them.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Record the fault state** before resetting anything. Note whether the outdoor fan runs, any unusual sounds or smells, and whether the fault returns immediately or after a delay.
2. **Confirm your exact model and series** using the nameplate on the outdoor unit and locate the matching Daikin error-code chart. E6 meanings vary across product families.
3. **Check all stop valves and service valves** on the refrigerant lines at the outdoor unit. Fully open any valve that was left closed during installation or service.
4. **Measure supply voltage** at the outdoor disconnect. For three-phase systems, verify that phase-to-phase voltage differences are below 14 V. Correct any supply imbalance before proceeding.
5. **Inspect wiring and connectors** between the outdoor control PCB, inverter section, and compressor terminals. Look for burn marks, corrosion, loose screws, or melted insulation.
6. **Isolate the compressor from the inverter board** (following the model-specific procedure) and measure compressor winding resistance and insulation to ground using a megohmmeter. Compare readings to the service manual's table.
7. **Test the inverter PCB separately** if compressor windings test good. Check for failed drive transistors, broken current-sensor circuits, or shorted components on the outdoor board.
8. **Replace the confirmed failed component** (compressor or PCB) and verify operation under load. Clear the error code, monitor for at least one full heating or cooling cycle, and confirm stable current draw.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Daikin outdoor unit compressor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-heat-pump-e6-error-code&k=Daikin+outdoor+unit+compressor&tag=errorcodefixes-20) \| Match the exact model and capacity. Confirm the old compressor is mechanically locked or electrically shorted before ordering. |
| Daikin outdoor control PCB / inverter board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-heat-pump-e6-error-code&k=Daikin+outdoor+control+PCB+%2F+inverter+board&tag=errorcodefixes-20) \| Verify the board part number from the outdoor-unit nameplate. Isolate the compressor first to rule out a compressor fault. |

## When to Call a Pro

E6 is a compressor-drive protection fault that requires refrigerant-system knowledge, high-voltage electrical diagnosis, and specialized test equipment. The repair involves isolating the compressor from the inverter, measuring winding resistance and insulation, testing drive circuits on the outdoor PCB, and potentially recovering refrigerant and replacing a sealed compressor. Supply-voltage testing on three-phase systems and interpreting current-sensor feedback also require professional tools and training. Call a licensed HVAC technician with Daikin experience. The only homeowner-safe check is verifying that service valves are open if the error appeared after recent work.

**Rough cost:** A pro service call runs about $800-2,500.
