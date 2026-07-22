---
title: "Yaskawa GA800 VFD F0013 Fault - Causes & Fix"
description: "F0013 on a Yaskawa GA800 indicates a ground fault. Most often caused by damaged motor cable insulation or moisture in connections."
pubDatetime: 2026-07-20T07:36:28Z
modDatetime: 2026-07-20T07:36:28Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "VFD-rated shielded motor cable"
most_likely_cause: "damaged or deteriorated motor cable insulation"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Inspect all motor cable connections at the drive and motor for moisture, corrosion, or loose strands touching ground"
  - "Check the motor junction box for water ingress or condensation"
  - "Verify the motor cable routing does not pass through sharp edges or pinch points"
part_price: "$150-400"
---

## Yaskawa GA800 VFD F0013 Fault — What It Means

The F0013 fault on a Yaskawa GA800 variable frequency drive indicates that the drive has detected a ground fault condition in the output circuit. This means current is leaking to ground somewhere between the drive output terminals and the motor, or within the motor itself. The drive monitors for current imbalance and shuts down to protect itself and the motor from damage.

Ground faults typically occur when insulation breaks down and allows current to flow where it should not. The drive will not run until the fault is cleared and the underlying cause is corrected. Simply resetting the fault without repair will cause it to trip again immediately or during motor operation.

## Before You Replace Anything

Technicians sometimes replace the VFD itself when the fault is actually in the motor cable or motor windings. Always perform insulation resistance tests on the cable and motor before condemning the drive.

[Jump to Fix](#fix)

## Common Causes

- **Damaged motor cable insulation (~45%)** Physical damage, wear, or aging of the shielded motor cable allows current to leak to ground through the shield or conduit.
- **Motor winding insulation failure (~30%)** Internal motor winding insulation breaks down due to age, contamination, or thermal stress and creates a path to the motor frame.
- **Moisture or contamination in connections (~15%)** Water, condensation, or conductive debris in the motor terminal box or cable glands creates a ground path.
- **Incorrect grounding or shielding (~7%)** Improperly terminated cable shields or multiple ground points can create ground loops that the drive interprets as a fault.
- **VFD output stage failure (~3%)** Internal drive output transistors or circuit board tracking can fail and create a ground fault condition within the drive itself.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault occur immediately when you apply power to the drive, even before starting the motor?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is likely in the motor cable or motor itself. Disconnect the motor cable at the drive and see if the fault clears.<br><strong>No:</strong> The fault occurs during motor operation, which suggests insulation breakdown under load or a drive output issue. Perform a megger test on the motor and cable.</div>
</details>

<details class="dtree"><summary>After disconnecting the motor cable from the drive output terminals, does the F0013 fault clear?</summary>
<div class="dtree-body"><strong>Yes:</strong> The problem is downstream of the drive in the cable or motor. Test the cable and motor insulation resistance separately.<br><strong>No:</strong> The drive itself has an internal ground fault. The VFD output stage or internal wiring is damaged and requires drive repair or replacement.</div>
</details>

<details class="dtree"><summary>Does a 500V or 1000V insulation resistance (megger) test on the motor show less than 1 megohm to ground?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor winding insulation has failed. The motor needs repair or replacement.<br><strong>No:</strong> The motor passes the test, so focus on the cable, connections, and cable shield termination practices.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down and lock out** the VFD and wait for the DC bus to discharge according to the drive manual before touching any terminals.
2. **Record all fault information** from the drive display and note when the fault occurs (at power-up, during start, or under load).
3. **Inspect all connections** at the drive output terminals, motor terminal box, and any junction boxes for moisture, corrosion, loose strands, or physical damage.
4. **Disconnect the motor cable** from the VFD output terminals U, V, and W and attempt to clear the fault by cycling power to the drive.
5. **Perform insulation resistance testing** using a megohmmeter (500V or 1000V test voltage) on the motor cable with all three phases shorted together, tested to ground and to the shield.
6. **Test the motor windings** separately by disconnecting the cable at the motor and performing the same megohm test on the motor windings to ground.
7. **Examine the cable routing** for sharp bends, pinch points, or areas where the cable may have been crushed or cut, and replace any damaged sections with proper VFD-rated shielded cable.

## Parts Often Needed

| Part | Notes |
|------|-------|
| VFD-rated shielded motor cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f0013-fault-code&k=VFD-rated+shielded+motor+cable&tag=errorcodefixes-20) \| Use cable rated for variable frequency drive applications with continuous-corrugated aluminum shield or braided shield, sized to your motor current. |
| Motor terminal box gasket and cable glands | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f0013-fault-code&k=Motor+terminal+box+gasket+and+cable+glands&tag=errorcodefixes-20) \| Replace if moisture ingress is found to restore environmental sealing. |

## When to Call a Pro

Call a qualified electrician or VFD technician if you are not trained in high-voltage electrical work or do not have insulation resistance testing equipment. Ground fault diagnosis requires a megohmmeter and an understanding of VFD output characteristics. If the motor or cable tests good and the fault persists with the cable disconnected, the VFD itself has failed internally and requires factory-trained service or replacement. Do not attempt to work inside the VFD enclosure without proper lockout/tagout and knowledge of DC bus capacitor discharge procedures.

**Rough cost:** A pro service call runs about $200-800.
