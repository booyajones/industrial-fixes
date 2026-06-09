---
title: "Danfoss FC302 VFD Alarm 37 - Causes & Fix"
description: "Alarm 37 on a Danfoss FC302 means phase imbalance. Check and replace blown fuses or fix loose input wiring first."
pubDatetime: 2026-06-03T10:46:43Z
modDatetime: 2026-06-03T10:46:43Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - danfoss
---

## Danfoss FC302 VFD Alarm 37 — What It Means

Alarm 37 on a Danfoss VLT AutomationDrive FC 302 indicates a phase imbalance, which Danfoss defines as a current imbalance between the power units inside the drive. This fault means one or more of the three incoming power phases is carrying significantly less current than the others, creating uneven load distribution that can damage the drive or upstream equipment.

The imbalance can originate either upstream of the drive (in the mains supply, fuses, or wiring) or inside the drive's power section. Most often the problem is external: a blown or weak input fuse, a loose connection, or a missing phase from the utility or distribution panel. If the incoming supply checks out balanced and clean, the fault points to an internal issue in the drive's power units.

[Jump to Fix](#fix)

## Common Causes

- **Blown or weak input fuses** A blown fuse on one phase or a fuse with high internal resistance will reduce current on that leg and trigger the imbalance alarm.
- **Missing or low incoming supply phase** A fault in the building's electrical panel, transformer, or utility feed can cause one phase to drop out or sag below the others.
- **Loose or corroded input terminals** Poor contact at the line-side terminals of the drive creates resistance on one phase, reducing current and causing imbalance.
- **Damaged input wiring or lugs** Frayed conductors, partially severed strands, or burned lugs increase resistance and unbalance the current draw.
- **Internal power unit fault** If the incoming supply is balanced but the alarm persists, one of the drive's internal power units may have failed or degraded.
- **Faulty contactor or disconnect upstream** A worn or pitted contact in an upstream contactor or switch can introduce resistance on a single phase.

## Step-by-Step Fix {#fix}

1. **Turn off and lock out** the main disconnect feeding the drive, verify zero voltage at the drive's line terminals with a multimeter, and discharge any stored energy per the FC 302 manual.
2. **Inspect and test all input fuses** to the drive using a multimeter in resistance mode (with power off) or by visual inspection for blown elements, then replace any suspect fuses with identical amperage and type.
3. **Measure all three incoming line voltages** (L1-L2, L2-L3, L3-L1) at the line side of the drive with power restored but the drive locked out, and confirm all three phase-to-phase voltages are present and within a few percent of each other.
4. **Check and tighten all line-side power terminals** on the drive, inspect wire insulation and lugs for burn marks or damage, and replace any compromised wiring or connectors.
5. **Verify the upstream supply** by measuring voltage and current balance at the distribution panel or disconnect feeding the drive, and correct any imbalance found there before re-energizing the drive.
6. **Reset the alarm and test** by powering up the drive and running it under normal load, watching for the fault to return.
7. **Contact a Danfoss service center or qualified drive technician** if the alarm reappears with confirmed balanced input supply and tight connections, as this indicates an internal power unit fault requiring drive repair or replacement.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Input fuses for Danfoss FC 302 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-37-fault-code&k=Input+fuses+for+Danfoss+FC+302&tag=errorcodefixes-20) \| Match the amperage and fuse class listed on the drive nameplate and in the installation manual for your frame size. |
| Power terminal lugs and crimp connectors | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-37-fault-code&k=Power+terminal+lugs+and+crimp+connectors&tag=errorcodefixes-20) \| Use lugs rated for the wire gauge and terminal stud size on the FC 302 line terminals, typically copper compression type. |

## When to Call a Pro

Call a qualified electrician or drive technician if you are not comfortable working with three-phase power, if you cannot safely verify and lock out the incoming supply, or if the imbalance persists after you have confirmed the input fuses are good and all wiring is tight and undamaged. Internal power unit faults require specialized knowledge, test equipment, and access to Danfoss service parts, so professional repair or factory service is the correct next step when external causes have been ruled out.

## See Also

- [Danfoss FC302 ALARM 16 - Causes & Fix](/posts/danfoss-fc302-alarm-16-fault-code/)
- [Danfoss FC302 Alarm 48 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-48-fault-code/)
- [Danfoss FC301 Fault AL 14 — Ground Fault Causes & Fix](/posts/danfoss-fc301-fault-al-14/)
- [Danfoss FC302 VFD Alarm 38 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-38-fault-code/)
