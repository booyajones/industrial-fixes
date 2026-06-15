---
title: "Electrolux Washer E23 Error Code - Causes & Fix"
description: "E23 is a drain-pump triac fault: the control board sees an abnormal state from the pump circuit. Most common fix: replace the drain pump."
pubDatetime: 2026-06-13T22:39:58Z
modDatetime: 2026-06-13T22:39:58Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - appliance
  - washer
  - electrolux
money_part: "Electrolux washer drain pump"
most_likely_cause: "failed drain pump"
likelihood: "the most common cause"
diy_or_pro: "diy"
free_checks:
  - "Unplug the washer, remove and clean the drain-pump filter and inspect the pump inlet for debris or obstruction."
  - "Inspect the pump wiring connector at both the pump and the main board for corrosion, loose pins, or visible damage."
  - "Check the drain hose and trap for kinks or blockages that could place extra mechanical load on the pump."
part_price: "$35–75"
---

## Electrolux Washer E23 Error Code — What It Means

The E23 code on an Electrolux washer is a drain-pump triac sensing or triac status fault. In plain terms, the main control board is detecting an unexpected electrical relationship between the command it sends to the drain pump and the feedback it receives from that circuit. This is primarily an electrical control-circuit fault in the pump output path, not a simple blockage or water-level error.

The fault points to three areas: the drain pump itself (failed or electrically weak), the wiring harness and connectors between the pump and the control board, or the main PCB's triac output stage that drives the pump. While a mechanical obstruction or pump blockage can sometimes accompany or precede the electrical fault, E23 itself signals that the board cannot confirm proper pump operation through its internal circuit monitoring.

## Before You Replace Anything

Some owners replace the main control board first, assuming the board has failed. Always test or swap the drain pump and inspect the pump wiring harness and connector for damage or corrosion before replacing the PCB, since a failing pump or loose connector is far more common than a board triac fault.

[Jump to Fix](#fix)

## Common Causes

- **Failed or electrically weak drain pump (~60%)** The pump motor or its internal winding has failed, preventing the triac circuit from seeing the expected load and feedback.
- **Damaged or loose pump wiring harness or connector (~20%)** Corrosion, a pulled pin, or a broken wire between the pump and the main board interrupts the triac sensing circuit.
- **Defective main PCB drain-pump triac output (~15%)** The control board's triac stage that drives the pump has failed, even though the pump and wiring are good.
- **Mechanical pump obstruction or seized impeller (~5%)** A blockage or jammed impeller can cause the pump to draw abnormal current or fail to start, triggering the triac fault.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the drain pump make any noise or attempt to run when the washer tries to drain?</summary>
<div class="dtree-body"><strong>Yes:</strong> The pump is receiving power but may be mechanically jammed or electrically weak. Remove and inspect the pump for blockage and test its resistance with a multimeter. If the pump tests open or very high resistance, replace it.<br><strong>No:</strong> The pump is silent, so either it is not receiving power (wiring or board fault) or it is completely failed. Check the pump connector and harness first, then test the pump directly with a bench power supply or swap in a known-good pump to isolate the fault.</div>
</details>

<details class="dtree"><summary>Is the pump wiring connector fully seated and free of corrosion or burn marks?</summary>
<div class="dtree-body"><strong>Yes:</strong> The connector is good. Move on to testing the pump itself for electrical continuity and mechanical freedom. If the pump passes, the fault is likely in the main control board's triac circuit.<br><strong>No:</strong> Clean or repair the connector, reseat it firmly, and retry. A poor connection can cause intermittent triac faults and is a simple fix before replacing any parts.</div>
</details>

<details class="dtree"><summary>Can you manually spin the pump impeller freely by hand (with power off and pump removed)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The pump is not mechanically seized, so the fault is electrical. Test the pump coil for continuity and compare to a known-good pump. If the pump tests bad, replace it. If it tests good, suspect the main board.<br><strong>No:</strong> The impeller is jammed or the pump bearing is seized. Clear any debris and retry. If it remains stuck, replace the pump.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect power** by unplugging the washer or switching off the circuit breaker. Do not proceed until the machine is completely de-energized.
2. **Access the drain pump** by removing the front lower panel or the rear service panel, depending on your model. Consult your owner's manual for the exact location and access method.
3. **Inspect the pump filter and inlet** for debris, coins, or fabric. Remove and clean the filter, and check the pump inlet chamber for obstructions that could jam the impeller.
4. **Check the pump wiring connector** at both the pump terminals and the main control board. Look for corrosion, loose pins, burn marks, or broken wires. Clean or repair any damaged connections.
5. **Test the drain pump** by disconnecting it from the harness and measuring its resistance across the motor terminals with a multimeter. Consult your model's service documentation for expected values. If the pump reads open, infinite resistance, or extremely high resistance, replace it.
6. **Verify pump mechanical operation** by attempting to spin the impeller by hand. It should turn freely without excessive drag. If it is seized or very stiff, replace the pump.
7. **Replace the drain pump** if it fails electrical or mechanical tests. Install the new pump, reconnect the harness, and secure all fasteners. If the pump and wiring both test good, the remaining fault is the main control board's triac output, and board replacement is the next step.
8. **Reassemble and test** by restoring power and running a drain or spin cycle. The E23 code should clear if the pump circuit is now functioning correctly.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Electrolux washer drain pump | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-electrolux-washer-e23-error-code&k=Electrolux+washer+drain+pump&tag=errorcodefixes-20) \| Match your model number; most pumps are universal across several Electrolux and Frigidaire front-load models. |
| Main control board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-electrolux-washer-e23-error-code&k=Main+control+board+%28PCB%29&tag=errorcodefixes-20) \| Required only if the pump and wiring test good but the E23 persists; verify your exact model and board part number before ordering. |

## When to Call a Pro

Call a qualified appliance technician if you are uncomfortable working with electrical components, if the fault persists after replacing the pump and inspecting all wiring, or if you suspect the main control board triac has failed. Board-level diagnosis often requires service documentation, a schematic, and test equipment to confirm the triac output. A pro can also verify that no other fault (such as a ground leak or intermittent short) is causing the triac to trip, and can handle PCB replacement with the correct programming or firmware for your model.

**Rough cost:** DIY runs about $40–80 in parts, 45–90 min. A pro service call runs about $150–300.
