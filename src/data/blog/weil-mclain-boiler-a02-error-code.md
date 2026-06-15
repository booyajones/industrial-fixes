---
title: "Weil-McLain A02 Error Code - Causes & Fix"
description: "A02 means false flame detected when there should be none. Most often caused by a dirty or misaligned ignition electrode. Clean or replace it."
pubDatetime: 2026-06-13T12:52:51Z
modDatetime: 2026-06-13T12:52:51Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - boiler
  - weil-mclain
money_part: "Ignition/detection electrode assembly"
most_likely_cause: "Dirty or misaligned ignition/detection electrode"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power-cycle the boiler and document the fault code from the diagnostic history before resetting"
  - "Visually inspect the ignition electrode and cable for obvious damage, contamination, or loose connections"
part_price: "$40-80"
---

## Weil-McLain A02 Error Code — What It Means

The A02 code on a Weil-McLain Aqua Balance boiler indicates a false flame fault. The control is detecting flame when there should not be any flame present, typically during the pre-purge or standby phase before ignition is commanded. This is different from the A01 code, which signals a failure to ignite.

The A02 fault points to a problem in the flame-sensing and ignition circuit. The control uses an electrode to sense flame current, and if that electrode is contaminated, misaligned, or its wiring is faulty, the control may see a false signal and lock out to prevent unsafe operation. The fault can also occur if the gas valve leaks slightly or if the ignition cable has developed a short or ground path.

## Before You Replace Anything

Technicians sometimes replace the gas valve or control board before inspecting the electrode assembly. A visual inspection of the electrode for contamination, proper gap, and secure connections will identify the real cause in most cases and costs nothing.

[Jump to Fix](#fix)

## Common Causes

- **Contaminated or dirty electrode (~45%)** White deposits, soot, or mineral buildup on the ignition/detection probe create a false ground path that the control reads as a flame signal.
- **Misaligned or damaged electrode (~25%)** The electrode may be bent, have an incorrect gap (field reports mention 5/32 in. as a reference), or be physically cracked, causing intermittent false flame detection.
- **Faulty ignition cable or connection (~15%)** A loose, corroded, or internally shorted ignition cable can create a ground path or allow voltage leakage that mimics a flame signal.
- **Gas valve leak or internal fault (~10%)** A gas valve that allows gas to seep into the combustion chamber before the ignition sequence can produce a real flame or flame-like signal at the wrong time.
- **Damaged electrode gasket or seal (~5%)** If the gasket at the electrode access point is damaged or missing, combustion gases can interfere with the electrode's signal or allow moisture ingress.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the boiler lock out immediately on startup without attempting to ignite?</summary>
<div class="dtree-body"><strong>Yes:</strong> The control is detecting false flame before ignition is commanded. Inspect the electrode and cable for contamination or damage.<br><strong>No:</strong> The fault may occur during or after ignition. Check for gas valve leakage or electrode misalignment after the burner fires.</div>
</details>

<details class="dtree"><summary>Is there visible contamination, white residue, or soot on the electrode when you remove it?</summary>
<div class="dtree-body"><strong>Yes:</strong> Clean the electrode carefully with fine steel wool or replace it if cleaning does not restore proper operation.<br><strong>No:</strong> Check the electrode gap and alignment, then test the ignition cable for continuity and insulation integrity.</div>
</details>

<details class="dtree"><summary>Does the ignitor produce a strong spark when removed and tested (with power off to reposition safely)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The ignition system and control board are likely working. Focus on gas delivery, valve operation, and electrode cleanliness.<br><strong>No:</strong> Replace the ignition cable or electrode assembly and verify connections are tight and corrosion-free.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off power and gas** to the boiler at the service switch and manual gas shutoff valve.
2. **Access the diagnostic menu** on the Aqua Balance control and record the A02 fault from the stored history before resetting the code.
3. **Remove the burner door or igniter/electrode cover** and carefully extract the ignition/detection electrode assembly, noting the position and gap.
4. **Inspect the electrode** for contamination (white deposits, soot), physical damage, bending, or improper gap, and clean it with fine steel wool if the manual permits, or replace if damaged.
5. **Check the ignition cable** for looseness at both ends, visible cracking or fraying, and continuity from the electrode terminal to the control board connection.
6. **Reinstall the electrode** with a new gasket if the old one is damaged, ensuring correct alignment and gap, then reconnect the ignition cable securely.
7. **Restore power and gas**, initiate a heat call, and observe the ignition sequence to confirm the boiler fires normally without the A02 fault returning.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Ignition/detection electrode assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a02-error-code&k=Ignition%2Fdetection+electrode+assembly&tag=errorcodefixes-20) \| Match the part number for your Aqua Balance model; includes the probe and ceramic insulator. |
| Ignition cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a02-error-code&k=Ignition+cable&tag=errorcodefixes-20) \| High-voltage cable from the electrode to the control board; check length and terminal type. |
| Electrode gasket | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a02-error-code&k=Electrode+gasket&tag=errorcodefixes-20) \| Seal for the electrode mounting point; replace if damaged during removal to prevent combustion gas leakage. |

## When to Call a Pro

Call a licensed heating technician for any A02 fault on a gas boiler. Diagnosis requires safe access to live ignition components, the ability to verify gas supply pressure (3.5 to 11 in. w.c. at the valve inlet for ignition troubleshooting), and proper testing of the flame-sensing circuit. If cleaning or realigning the electrode does not clear the fault, the technician will test the gas valve for leakage, verify control-board operation, and replace defective components with the correct factory parts. Working on gas-fired equipment without proper training and tools is dangerous and may violate local codes or void your warranty.

**Rough cost:** A pro service call runs about $150-350.

## See Also

- [Weil-McLain E02 Error Code — Causes & Fix](/posts/weil-mclain-e02-error-code/)
- [Weil-McLain 019 Error Code - Causes & Fix](/posts/weil-mclain-boiler-a19-error-code/)
- [Weil-McLain A37 Error Code - Causes & Fix](/posts/weil-mclain-boiler-a37-error-code/)
- [Weil-McLain Boiler Error Code E02 — Ignition Failure Fix](/posts/weil-mclain-e02-ignition-failure/)
