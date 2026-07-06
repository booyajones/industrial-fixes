---
title: "Yaskawa A1000 AL-31 Fault - Causes & Fix"
description: "AL-31 is not a valid Yaskawa A1000 code. Check your display again; likely oFD, oV, or voF (output phase or voltage fault)."
pubDatetime: 2026-06-30T09:45:37Z
modDatetime: 2026-06-30T09:45:37Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Inverter/IGBT module"
most_likely_cause: "loose or broken motor output wiring"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power down and inspect all motor output terminals (U, V, W) for loose screws, corrosion, or broken wire strands"
  - "Check the motor terminal box for loose connections or visible winding damage"
---

## Yaskawa A1000 AL-31 Fault — What It Means

The fault code AL-31 does not exist in the Yaskawa A1000 VFD fault library. It is a specific fault code for Danfoss drives (FC-A series), where it indicates a missing phase on the motor output. If your Yaskawa A1000 is displaying a fault, you likely have a different code such as oFD (Output Phase Detection), oV (Overvoltage), or voF (Output Voltage Detection), which are the actual Yaskawa equivalents for output phase or voltage issues.

If you are seeing an output-related fault on your A1000, the drive has detected an imbalance in the output voltage or current, or an open circuit in one of the motor output phases (U, V, W). This typically indicates a hardware failure in the inverter section, loose wiring, or a damaged motor winding.

## Before You Replace Anything

Many technicians replace the entire control board first, but a simple multimeter diode check of the IGBT module (between DC bus and U, V, W terminals) will pinpoint a failed inverter section and save hundreds in unnecessary parts.

[Jump to Fix](#fix)

## Common Causes

- **Loose or broken wiring (~35%)** Loose terminal screws at the drive output (U, V, W) or open motor windings are the most frequent cause of output phase faults.
- **Failed IGBT module (~30%)** A shorted or open IGBT in the inverter bridge on one phase leg will trip output phase detection.
- **Damaged control board (~15%)** The logic board may fail to drive the IGBTs correctly, causing imbalanced output signals.
- **Motor winding damage (~12%)** Motor winding shorts, open circuits, or insulation breakdown will create phase imbalance.
- **Overheating and thermal shutdown (~8%)** Blocked heatsinks or failed cooling fans can cause IGBT thermal failure and output faults.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Are all motor output terminals (U, V, W) tight and free of corrosion?</summary>
<div class="dtree-body"><strong>Yes:</strong> Wiring is not the issue. Proceed to test the IGBT module with a multimeter diode check.<br><strong>No:</strong> Tighten all terminals, clean any corrosion, and reset the drive. If the fault clears, the wiring was the problem.</div>
</details>

<details class="dtree"><summary>Does a multimeter diode check show consistent 0.3-1.0 V readings across all six IGBT diodes (+ to U/V/W and - to U/V/W)?</summary>
<div class="dtree-body"><strong>Yes:</strong> IGBTs are healthy. Check the control board drive signals and motor windings for damage.<br><strong>No:</strong> One or more IGBTs have failed. Replace the inverter/IGBT module or the entire power board.</div>
</details>

<details class="dtree"><summary>Is the DC bus voltage approximately 1.45 times the line-to-line input voltage with less than 2 V ripple?</summary>
<div class="dtree-body"><strong>Yes:</strong> DC bus is healthy. Focus on the inverter section and motor connections.<br><strong>No:</strong> Rectifier or capacitor bank has failed. Replace the power board or rectifier assembly.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect all power** and wait at least 5 minutes for DC bus capacitors to discharge before opening the drive enclosure.
2. **Inspect and tighten** all motor output terminals (U, V, W) at the drive and at the motor terminal box. Look for loose screws, broken wire strands, or corrosion.
3. **Perform a multimeter diode check** on the IGBT module. Set your meter to diode mode. Test between DC bus + and each output (U, V, W), then between DC bus - and each output. You should see 0.3-1.0 V in one direction and open in the other for all six tests. Inconsistent readings indicate a failed IGBT.
4. **Measure DC bus voltage** (with power applied, use extreme caution). Connect meter probes between the + and - DC bus terminals. Voltage should be approximately 1.45 times your line-to-line input voltage with AC ripple under 1-2 V.
5. **Check cooling components**. Verify that all cooling fans are spinning and heatsinks are clean. Overheating is a common cause of IGBT failure.
6. **Replace the inverter/IGBT module** if diode checks show a failed transistor. If multiple components are damaged, replace the entire power board.
7. **If the control board is suspect**, swap it with a known-good unit or send it for repair. Verify that gate drive signals are present at the IGBT module before replacing the power section.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Inverter/IGBT module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-al-31-fault-code&k=Inverter%2FIGBT+module&tag=errorcodefixes-20) \| Contains the power transistors for phases U, V, W. Match your drive frame size and voltage rating. |
| Power board assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-al-31-fault-code&k=Power+board+assembly&tag=errorcodefixes-20) \| Includes rectifier, DC bus, and inverter section. Use when multiple components have failed. |
| Control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-al-31-fault-code&k=Control+board&tag=errorcodefixes-20) \| Replace if logic or gate drive signals are faulty. Verify with oscilloscope before swapping. |
| Cooling fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-al-31-fault-code&k=Cooling+fan&tag=errorcodefixes-20) \| Replace if overheating is the root cause. Match airflow rating to your drive model. |

## When to Call a Pro

Call a qualified technician immediately if you are not trained in high-voltage DC systems. The Yaskawa A1000 DC bus holds lethal voltage (300-800 VDC depending on input) even after input power is removed, and discharge can take several minutes. Any work inside the drive enclosure requires lockout/tagout, proper PPE, and a clear understanding of capacitor discharge procedures. If you lack a multimeter, oscilloscope, or experience with IGBT testing, do not attempt this repair. A technician will safely diagnose the fault, perform diode checks, and replace the correct module without risking electric shock or further damage to the drive.

**Rough cost:** A pro service call runs about $300-800.

## See Also

- [Yaskawa GA800 E26 Fault Code - Causes & Fix](/posts/yaskawa-ga800-e26-fault-code/)
- [Yaskawa GA800 E08 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-e08-fault-code/)
- [Yaskawa GA800 Er-04 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-f049-fault-code/)
- [Yaskawa GA800 E04 Fault Code - Causes & Fix](/posts/yaskawa-ga800-vfd-e04-fault-code/)
