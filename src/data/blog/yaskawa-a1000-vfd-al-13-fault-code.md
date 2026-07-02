---
title: "Yaskawa A1000 AL-13 Fault - Causes & Fix"
description: "AL-13 means the drive failed to measure motor leakage inductance during auto-tuning. Most often caused by wrong motor current in T1-04."
pubDatetime: 2026-06-28T10:29:27Z
modDatetime: 2026-06-28T10:29:27Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Motor cable assembly"
most_likely_cause: "Incorrect motor rated current entered in parameter T1-04"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify the motor rated current on the nameplate and check that parameter T1-04 matches exactly"
  - "Inspect motor-to-drive cable terminations at both ends for loose, corroded, or broken connections"
  - "Clear the fault and re-run the auto-tuning sequence to see if a transient issue clears"
no_buy_pct: "60%"
---

## Yaskawa A1000 AL-13 Fault — What It Means

The AL-13 fault (sometimes displayed as Er-13) is a **Leakage Inductance Error**. The Yaskawa A1000 drive could not complete auto-tuning of the motor's leakage inductance within the 300-second timeout window. During startup or parameter setup, the drive applies a test current to measure internal motor characteristics needed for accurate vector control. If the drive cannot obtain a stable reading in that time, it trips AL-13 and stops.

This fault is not an encoder or feedback error. It happens during the electrical tuning sequence and means the drive either cannot see the motor correctly (due to wiring problems or wrong parameter values) or the motor itself has damaged windings that prevent a valid measurement.

## Before You Replace Anything

Technicians sometimes replace the entire drive when the real problem is simply a typo in parameter T1-04 or a loose motor terminal. Always verify the motor nameplate current matches T1-04 and inspect all wiring before ordering a new drive or control board.

[Jump to Fix](#fix)

## Common Causes

- **Wrong motor rated current in T1-04 (~40%)** If the current value entered does not match the actual motor nameplate, the tuning algorithm cannot calculate leakage inductance and times out after 300 seconds.
- **Loose or damaged motor-to-drive wiring (~25%)** Corroded terminals, broken conductors, or poor crimps prevent the drive from seeing the motor correctly during the test sequence.
- **Open or shorted motor windings (~20%)** Melted wires in the motor peckerhead, open phases, or internal shorts block the test current and cause the tuning routine to fail.
- **Motor nameplate data mismatch (~10%)** Entering the wrong voltage, frequency, or pole count in drive parameters can make the tuning algorithm select the wrong test conditions.
- **Faulty drive control board (~5%)** In rare cases, damaged drive hardware cannot execute the auto-tuning routine even when wiring and parameters are correct.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the motor rated current in parameter T1-04 exactly match the motor nameplate?</summary>
<div class="dtree-body"><strong>Yes:</strong> The parameter is correct. Move on to check wiring and motor windings.<br><strong>No:</strong> Correct T1-04 to match the nameplate value, clear the fault, and re-run auto-tuning.</div>
</details>

<details class="dtree"><summary>Are all motor-to-drive cable terminations tight and free of corrosion or damage?</summary>
<div class="dtree-body"><strong>Yes:</strong> Wiring is good. Measure motor phase-to-phase resistance to check for open or shorted windings.<br><strong>No:</strong> Repair or replace damaged cables and terminals, then re-run auto-tuning.</div>
</details>

<details class="dtree"><summary>Does a multimeter show balanced phase-to-phase resistance (within 5 percent and no open circuits)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Motor windings are healthy. Suspect a faulty drive control board if the fault persists after correct parameters and wiring.<br><strong>No:</strong> Motor windings are damaged. Replace the motor.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive** completely and verify no hazardous voltages remain before opening any panels or touching terminals.
2. **Read the motor nameplate** and write down the rated current (amps), voltage, frequency, and pole count.
3. **Check parameter T1-04** in the drive menu and confirm the motor rated current matches the nameplate exactly, then verify other motor parameters (voltage, frequency) are also correct.
4. **Inspect all motor-to-drive wiring** at both the drive output terminals and the motor peckerhead, looking for loose bolts, corroded lugs, broken strands, or melted insulation.
5. **Measure motor phase-to-phase resistance** with a multimeter (drive disconnected), confirming all three readings are within 5 percent of each other and none show an open circuit (infinite resistance) or short to ground (zero resistance).
6. **Clear the AL-13 fault** using the drive's reset button or fault-reset menu, then initiate the auto-tuning sequence (typically via parameter T1-01 or T1-09) and observe whether the drive completes tuning within 300 seconds.
7. **Replace damaged components** if the fault returns after correct parameters and good wiring: replace the motor if windings are open or shorted, or replace the drive control board (or the entire A1000 unit) if hardware is faulty.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor cable assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-al-13-fault-code&k=Motor+cable+assembly&tag=errorcodefixes-20) \| Use shielded VFD-rated cable of the correct gauge for your motor current; replace if damaged or corroded. |
| Three-phase AC motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-al-13-fault-code&k=Three-phase+AC+motor&tag=errorcodefixes-20) \| Replace if windings are open, shorted, or melted; verify nameplate matches drive rating. |
| Yaskawa A1000 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-al-13-fault-code&k=Yaskawa+A1000+control+board&tag=errorcodefixes-20) \| Order the specific board for your drive frame size if the drive cannot complete tuning despite correct wiring and parameters. |

## When to Call a Pro

Call a qualified technician or industrial electrician if you are not trained to work on variable-frequency drives or high-voltage equipment. This fault involves live three-phase power, motor winding tests, and drive parameter programming. A technician will have the tools to measure winding inductance, verify cable integrity with a megohmmeter, and safely commission the drive after repairs. Always follow lockout/tagout procedures and consult the A1000 manual before servicing the drive.

**Rough cost:** A pro service call runs about $150-400 for service call and parameter correction or wiring repair; motor or drive replacement costs extra if hardware is damaged.

## See Also

- [Yaskawa GA800 E42 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-e42-fault-code/)
- [Yaskawa GA800 A.128 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-a-128-fault-code/)
- [Yaskawa A1000 VFD AL-20 Fault - Causes & Fix](/posts/yaskawa-a1000-vfd-al-20-fault-code/)
- [Yaskawa GA800 F035 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-f035-fault-code/)
