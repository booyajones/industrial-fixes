---
title: "Danfoss FC302 AL-123 Fault Code - Causes & Fix"
description: "AL-123 does not exist in FC302 documentation. Likely misread Alarm 13 (overcurrent). Check motor load and motor parameters first."
pubDatetime: 2026-06-24T10:19:34Z
modDatetime: 2026-06-24T10:19:34Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 IGBT power board module"
most_likely_cause: "mechanical overload on the motor shaft or incorrect motor nominal current parameter"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify the exact alarm code on the drive display (confirm it is not AL-13 instead of AL-123)"
  - "Check for mechanical binding by rotating the motor shaft by hand with power off"
  - "Inspect all motor cable connections at drive and motor terminals for looseness or corrosion"
---

## Danfoss FC302 AL-123 Fault Code — What It Means

The Danfoss FC302 does not use an AL-123 fault code. Official alarm codes range from AL-1 through AL-50 and do not reach 123. The most probable explanation is that Alarm 13 (AL-13) was misread or the digit was duplicated. Alarm 13 indicates overcurrent during normal operation or acceleration, meaning the drive output current exceeded its safe threshold (typically 150 to 160% of motor nominal current for several seconds). Unlike an instantaneous short-circuit trip, Alarm 13 occurs when current gradually builds beyond rated capacity during acceleration or steady running. Always verify the exact code displayed on your drive's keypad before troubleshooting.

## Before You Replace Anything

Technicians often replace the IGBT power board or entire drive when the real cause is a jammed load, motor winding short, or wrong parameter 1-24 setting. Disconnect the motor and run the drive unloaded first to isolate internal from external faults.

[Jump to Fix](#fix)

## Common Causes

- **Mechanical overload on motor shaft (~30%)** Jammed pump impeller, stuck conveyor belt, or seized bearing forces the motor to draw excessive current trying to turn the load.
- **Incorrect motor parameter settings (~25%)** Parameter 1-24 (nominal motor current) set too low or motor model mismatch causes the drive to trip on normal current draw.
- **Partial short in motor windings (~20%)** Damaged insulation or degraded stator windings create a current path that raises phase current above safe limits.
- **Loose or corroded cable connections (~15%)** High resistance at terminals or loose crimp connections cause current spikes and voltage drops that trigger overcurrent protection.
- **Aging IGBT modules or power board failure (~10%)** Worn insulated-gate bipolar transistors lose current regulation ability and allow uncontrolled current flow.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the exact alarm code on the drive display show AL-13 rather than AL-123?</summary>
<div class="dtree-body"><strong>Yes:</strong> Proceed with Alarm 13 overcurrent diagnostics below.<br><strong>No:</strong> Consult your FC302 manual alarm table for the actual code or contact Danfoss support if AL-123 appears (it is not a standard code).</div>
</details>

<details class="dtree"><summary>Can you rotate the motor shaft freely by hand with power off and disconnected?</summary>
<div class="dtree-body"><strong>Yes:</strong> Mechanical load is likely okay. Check motor parameters and wiring next.<br><strong>No:</strong> Mechanical binding or seized bearing is forcing overcurrent. Repair or replace the driven equipment or motor bearings.</div>
</details>

<details class="dtree"><summary>Does the drive run without tripping when motor leads are disconnected?</summary>
<div class="dtree-body"><strong>Yes:</strong> Fault is external (motor, wiring, or load). Inspect motor windings and cable.<br><strong>No:</strong> Drive has internal component failure (IGBT, rectifier, or DC bus capacitor). Professional drive repair or replacement needed.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Confirm the exact alarm code** by checking the drive display and cross-reference it in the FC302 manual alarm table to verify whether it is Alarm 13 or another code.
2. **Disconnect motor leads** from the drive output terminals (U, V, W) and run the drive unloaded to isolate internal drive failure from external motor or load problems.
3. **Measure motor winding resistance** between all three phases with a multimeter. Values should be within 5% of each other. Use a megohmmeter to test insulation resistance to ground.
4. **Check parameter 1-24** (nominal motor current) and confirm it matches the motor nameplate rating. Run Automatic Motor Adaptation (parameter 1-29) to optimize motor model matching.
5. **Inspect all cable connections** at drive output terminals and motor terminal box. Tighten any loose connections and clean corrosion. Verify shielding and separation of power and control cables.
6. **Measure input voltage** across all three input phases. Voltage imbalance should be less than 3%. Use a clamp-on ammeter to check current balance on each phase.
7. **Open the drive enclosure** (with power off and lockout/tagout) and inspect for dirt, metal chips, moisture, or corrosion on circuit boards and heat sinks. Look for swollen or leaking capacitors on the DC bus section.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 IGBT power board module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-123-fault-code&k=Danfoss+FC302+IGBT+power+board+module&tag=errorcodefixes-20) \| Order by exact drive frame size and voltage rating from Danfoss or authorized distributor |
| Motor matched to drive rating | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-123-fault-code&k=Motor+matched+to+drive+rating&tag=errorcodefixes-20) \| If motor windings test shorted or insulation resistance is below 1 megohm |

## When to Call a Pro

Call a qualified drives technician or electrical contractor if the drive continues to fault with the motor disconnected, if you lack a megohmmeter or clamp-on ammeter for diagnostic testing, or if internal inspection reveals swollen capacitors or damaged IGBT modules. High-voltage work inside the drive (even with power off, DC bus capacitors can hold lethal charge) requires lockout/tagout procedures and proper discharge tools. Professional drive repair shops can test and replace individual power boards, rectifiers, and capacitors at lower cost than full drive replacement. If the motor tests faulty (winding short or insulation breakdown), a motor shop can rewind or you can source a replacement matched to the drive's output rating.

**Rough cost:** A pro service call runs about $200-800 depending on whether repair involves parameter adjustment, motor replacement, or drive power board service.

## See Also

- [Danfoss VLT Alarm 14 - Earth Fault: What It Means and How to Fix It](/posts/danfoss-vlt-alarm-14/)
- [Danfoss FC302 AL-89 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-89-fault-code/)
- [Danfoss FC302 AL-116 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-116-fault-code/)
- [Danfoss FC302 ALARM 28 - Causes & Fix](/posts/danfoss-fc302-alarm-28-fault-code/)
