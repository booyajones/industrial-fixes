---
title: "Danfoss FC302 AL-141 Fault - Causes & Fix"
description: "AL-141 likely refers to Alarm 14 (Earth Fault), meaning current is leaking to ground. Most common fix: tighten output terminals."
pubDatetime: 2026-06-25T09:28:15Z
modDatetime: 2026-06-25T09:28:15Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Motor or motor cable"
most_likely_cause: "Motor or cable insulation breakdown"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power down and check for loose or corroded connections at the drive output terminals (L1, L2, L3) and the motor junction box, then tighten and retry"
  - "Perform a manual initialization procedure (often holding specific keys during power-up for 5 seconds) to clear any current sensor offsets"
  - "Disconnect the motor leads from the drive, power on, reset the alarm, and attempt to run the drive with no motor attached to isolate whether the fault is in the drive or downstream"
no_buy_pct: "60%"
---

## Danfoss FC302 AL-141 Fault — What It Means

The Danfoss VLT AutomationDrive FC 302 does not display a fault code labeled AL-141 in standard documentation. The most likely intended code is Alarm 14 (Earth Fault), which indicates the drive has detected current leaking from the motor or cable to ground instead of returning through the motor phases. This triggers a protective shutdown to prevent equipment damage or electrical hazards. The drive monitors output current balance and trips when it senses an imbalance that suggests a ground leak.

If your display shows a different format or numbering, consult your specific model's manual or wiring diagram, as fault code conventions can vary by firmware version or regional configuration.

## Before You Replace Anything

Technicians often replace the drive itself when the real fault is a damaged motor cable or loose connection. Always disconnect the motor and run the drive unloaded first. If the alarm clears with no motor attached, the drive is fine and the problem is downstream.

[Jump to Fix](#fix)

## Common Causes

- **Motor or cable insulation breakdown (~40%)** A partial short in the motor windings or the motor cable to ground, often caused by aging insulation, moisture, or mechanical damage, allows current to leak to earth.
- **Loose or corroded connections (~30%)** Loose terminals at the drive output or motor junction box create resistance spikes and arcing that can trigger or mimic a ground fault.
- **Incorrect motor parameter settings (~15%)** If the nominal motor current (Parameter 1-24) is set much higher than the actual motor rating, the drive may falsely detect an earth fault due to calibration mismatch.
- **Internal drive failure (~10%)** Failed current sensors, damaged IGBT modules, or faulty gate driver circuits inside the drive can produce Alarm 14 even with the motor completely disconnected.
- **Mechanical overload causing motor heating (~5%)** Severe mechanical overload can overheat the motor and degrade winding insulation, leading to ground leaks over time.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>With power off and the motor leads disconnected from the drive, does the drive power on and clear Alarm 14 when reset?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is downstream in the motor or cable. Perform a megohm test on the motor windings to ground. Readings below 2 megohms indicate insulation failure and the motor or cable needs repair or replacement.<br><strong>No:</strong> The fault is internal to the drive. The drive requires service or replacement of internal components such as current sensors or IGBT modules.</div>
</details>

<details class="dtree"><summary>Are any output terminal connections (L1, L2, L3) at the drive or motor junction box visibly loose or corroded?</summary>
<div class="dtree-body"><strong>Yes:</strong> Tighten all connections, clean any corrosion with contact cleaner, cycle power, and reset the alarm. This often resolves the fault.<br><strong>No:</strong> Proceed to manual initialization and motor disconnect test to isolate the fault location.</div>
</details>

<details class="dtree"><summary>Does Parameter 1-24 (nominal motor current) match the nameplate rating of your motor?</summary>
<div class="dtree-body"><strong>Yes:</strong> The parameter is correct. Continue troubleshooting by checking insulation and connections.<br><strong>No:</strong> Correct Parameter 1-24 to match the motor nameplate current rating, then reset the alarm and test. Incorrect settings can cause false earth fault trips.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down completely** and lock out all AC supply to the drive before touching any terminals or connections.
2. **Inspect and tighten** all output terminals (L1, L2, L3) at the drive and all connections at the motor junction box. Look for discoloration, corrosion, or signs of arcing. Clean corroded terminals with contact cleaner and retry.
3. **Perform manual initialization** by following your drive's procedure (often holding specific keys during power-up for 5 seconds) to clear current sensor offsets that may have drifted over time.
4. **Disconnect the motor leads** from the drive output terminals. Power the drive back on, reset Alarm 14, and attempt to run the drive with no motor attached.
5. **If the drive runs normally** with no motor (LCP shows near-zero current), the fault is in the motor or cable. Use a megohm tester to measure insulation resistance from each motor winding to ground. Readings below 2 megohms indicate insulation failure. Replace or repair the motor or cable.
6. **If Alarm 14 persists** with the motor disconnected, the fault is inside the drive. Open the drive enclosure (power off and locked out) and inspect the heatsink, power module, and current sensor connections for visible damage, burnt components, or loose wiring.
7. **Replace defective internal components** (current sensors, IGBT modules, or gate driver boards) if you have the skills and tools. Otherwise, contact Danfoss or an authorized service center for drive repair or replacement.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor or motor cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-141-fault-code&k=Motor+or+motor+cable&tag=errorcodefixes-20) \| If insulation resistance tests below 2 megohms to ground, replace the damaged component |
| Danfoss FC302 current sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-141-fault-code&k=Danfoss+FC302+current+sensor&tag=errorcodefixes-20) \| For internal drive faults confirmed after motor disconnect test |
| Danfoss FC302 IGBT power module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-141-fault-code&k=Danfoss+FC302+IGBT+power+module&tag=errorcodefixes-20) \| If drive shows physical damage or fault persists after sensor replacement |

## When to Call a Pro

Call a qualified electrician or drive technician if you are not comfortable working with high-voltage industrial equipment, if the drive trips Alarm 14 with the motor disconnected (indicating an internal drive fault), or if insulation testing and parameter checks do not resolve the issue. Internal drive repairs require knowledge of power electronics, access to service manuals, and proper ESD precautions. A technician will have megohm testers, oscilloscopes, and replacement parts to diagnose and repair the drive or motor safely. If the drive is under warranty, contact Danfoss or your distributor before opening the enclosure, as unauthorized service may void coverage.

**Rough cost:** A pro service call runs about $200-600.

## See Also

- [Danfoss FC302 AL-94 - Causes & Fix](/posts/danfoss-fc302-vfd-al-94-fault-code/)
- [Danfoss FC302 Alarm 23 - Causes & Fix](/posts/danfoss-fc302-alarm-23-fault-code/)
- [Danfoss FC302 AL-76 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-76-fault-code/)
- [Danfoss FC302 VFD AL-119 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-119-fault-code/)
