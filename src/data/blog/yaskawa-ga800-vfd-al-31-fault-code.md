---
title: "Yaskawa GA800 VFD AL-31 Fault Code - Causes & Fix"
description: "AL-31 indicates a ground fault or insulation failure. Check motor cable insulation and motor windings for shorts to ground."
pubDatetime: 2026-07-22T07:25:42Z
modDatetime: 2026-07-22T07:25:42Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "Shielded VFD-rated motor cable"
most_likely_cause: "Damaged motor cable insulation or loose motor terminal connections"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Visually inspect the motor cable for physical damage, pinching, or worn insulation"
  - "Check all motor terminal connections for tightness and signs of arcing or corrosion"
  - "Verify the motor frame and cable shield are properly grounded"
---

## Yaskawa GA800 VFD AL-31 Fault Code — What It Means

The AL-31 fault on a Yaskawa GA800 variable frequency drive signals a ground fault detection event. The drive has identified current leaking to ground somewhere in the motor circuit, which typically means insulation has broken down in the motor windings, motor cable, or connections. This fault protects the drive and motor from damage due to arcing or short-circuit conditions.

The drive continuously monitors for imbalanced current flow that would indicate a path to ground. When the leakage current exceeds the programmed threshold, the AL-31 fault trips and shuts down the drive. This condition can be intermittent or constant depending on whether the fault is moisture-related, mechanical damage, or complete insulation failure.

## Before You Replace Anything

Many technicians replace the VFD itself when the fault is actually in the motor or cable. Always megger-test the motor and cable insulation to ground before condemning the drive.

[Jump to Fix](#fix)

## Common Causes

- **Damaged motor cable insulation (~35%)** Physical damage, moisture intrusion, or age-related cracking in the motor cable allows current to leak to the conduit or ground path.
- **Motor winding insulation failure (~30%)** Overheating, contamination, or mechanical stress causes the varnish insulation inside the motor to break down and short windings to the frame.
- **Moisture or condensation in motor or junction box (~15%)** Water ingress lowers insulation resistance and creates a conductive path between live conductors and grounded metal parts.
- **Loose or corroded motor terminal connections (~10%)** Poor contact at the motor terminal block or grounding lug creates intermittent arcing that mimics a ground fault condition.
- **Improper cable shielding or grounding (~7%)** Ungrounded or incorrectly bonded cable shields cause capacitive coupling that the drive interprets as ground leakage current.
- **Drive ground fault detection circuit failure (~3%)** A fault in the drive's current sensing or detection circuitry generates a false AL-31 alarm even when the motor circuit is sound.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault appear immediately on power-up before the motor runs?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is likely constant and points to a hard short in the cable or motor. Proceed directly to insulation resistance testing.<br><strong>No:</strong> The fault may be load-dependent or intermittent. Check for moisture, vibration-related damage, or thermal cycling that breaks down insulation under load.</div>
</details>

<details class="dtree"><summary>Does megger testing show low insulation resistance (below 1 megohm) from any motor lead to ground?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor or cable insulation has failed. Isolate the motor from the cable and test each separately to identify which component needs replacement.<br><strong>No:</strong> The insulation may be marginal or the drive's detection threshold may be set too sensitively. Review drive parameters and consult your model's manual for ground fault trip level settings.</div>
</details>

<details class="dtree"><summary>Is the motor operating in a wet, humid, or dirty environment?</summary>
<div class="dtree-body"><strong>Yes:</strong> Moisture or contaminants are the likely cause. Dry out the motor, seal the junction box, and consider upgrading to a higher IP-rated enclosure.<br><strong>No:</strong> Focus on physical damage, cable routing issues, and terminal connections as the primary suspects.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect power** to the VFD and lock out the supply according to safety procedures, then wait for DC bus capacitors to discharge.
2. **Disconnect the motor cable** from the drive output terminals and from the motor terminal box to isolate the motor circuit for testing.
3. **Perform insulation resistance testing** using a megohmmeter (megger) set to 500 or 1000 VDC. Test each motor lead (U, V, W) to the motor frame and to ground. Record the readings.
4. **Megger-test the motor cable** separately by measuring insulation resistance from each conductor to the cable shield or armor. Compare readings to acceptable values in your installation standards.
5. **Inspect the motor terminal box** for moisture, dust, tracking marks, or damaged wire insulation. Clean and dry all surfaces if contamination is found.
6. **Check all ground connections** including motor frame ground, cable shield bond at both ends, and drive chassis ground. Tighten any loose hardware and remove corrosion.
7. **Reconnect the motor cable** only after confirming all insulation readings are acceptable (typically above 1 megohm for 460V class motors, but consult your model's table).
8. **Restore power and run a test** at low speed with no load. Monitor the drive display for any recurrence of the AL-31 fault and verify normal operation before returning to service.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Shielded VFD-rated motor cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-al-31-fault-code&k=Shielded+VFD-rated+motor+cable&tag=errorcodefixes-20) \| Use cable rated for variable frequency drive service with properly sized ground and shield conductors. |
| Motor terminal box gasket and seals | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-al-31-fault-code&k=Motor+terminal+box+gasket+and+seals&tag=errorcodefixes-20) \| Replace if moisture intrusion is the root cause to restore weatherproof integrity. |

## When to Call a Pro

Call a qualified electrician or industrial controls technician if you are not trained in high-voltage electrical work or do not own insulation resistance testing equipment. Ground fault diagnosis requires megohmmeter testing at voltages that can be hazardous. A professional will have the tools to isolate the fault quickly and safely, and can also verify that drive parameters are correctly set for your motor and application. If the motor windings have failed, a motor shop can rewind or you may need a replacement motor, which also requires professional sizing and installation.

**Rough cost:** A pro service call runs about $200-800.
