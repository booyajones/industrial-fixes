---
title: "ABB ACS580 A2A1 Fault - Causes & Fix"
description: "A2A1 on ABB ACS580 means output phase current measurement fault (aux code 2281). Check motor cable connections and insulation first."
pubDatetime: 2026-05-31T11:07:15Z
modDatetime: 2026-05-31T11:07:15Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - abb
money_part: "VFD-rated motor cable"
most_likely_cause: "Loose or corroded motor cable terminations"
---

## ABB ACS580 A2A1 Fault — What It Means

The A2A1 fault on your ABB ACS580 drive indicates an output phase current measurement problem, not a simple phase loss. ABB lists A2A1 as a current calibration item with the fault text 'Output phase current measurement fault' and auxiliary code 2281. This means the drive cannot correctly sense the current flowing to your motor, either because of a wiring problem at the output terminals or an internal measurement circuit issue. It is different from fault code 3381, which signals a true output phase loss where all three phases are not connected to the motor. When you see A2A1, the drive is telling you its output current sensing chain has failed or seen an unexpected condition. The fault can appear as a warning asking for calibration at next start or as a hard fault that stops operation. Most A2A1 faults in the field trace back to loose or damaged motor cables, poor terminations at the drive output, or motor-side insulation breakdown that confuses the current measurement. Internal drive hardware is less common but possible if external wiring checks out clean.

[Jump to Fix](#fix)

## Common Causes

- **Loose or corroded motor cable terminations** Poor connections at the drive output terminals or motor junction box create intermittent current paths that the drive's measurement circuit cannot track reliably.
- **Damaged or aged motor cable insulation** Insulation breakdown, nicks, or moisture ingress in the motor cable can cause leakage current or intermittent shorts that distort the phase current readings.
- **Motor winding short or ground fault** A developing short circuit or earth fault inside the motor draws unbalanced current that the drive flags as a measurement problem rather than a simple overload.
- **Incorrectly sized or mismatched motor cable** Using cable too long, too small, or not rated for VFD service can introduce noise or voltage drop that interferes with accurate current sensing.
- **Drive output current sensor or control board failure** Internal current transducers, Hall-effect sensors, or the analog measurement circuitry on the drive control board can drift out of calibration or fail outright.
- **Electrical noise or improper grounding** Missing or poor PE ground, nearby high-frequency interference, or shared neutral paths can inject false signals into the current measurement inputs.

## Step-by-Step Fix {#fix}

1. **Check the drive display or event log** to confirm the exact fault text, auxiliary code 2281, and whether the panel shows A2A1 as an informative warning or a hard fault that stopped the drive.
2. **Power down and lock out** the ACS580, then visually inspect all three motor output terminals on the drive for loose hardware, discolored copper, signs of arcing, or cracked terminal blocks.
3. **Inspect the motor cable** along its entire run for physical damage, tight bend radius, moisture, oil contamination, or any sign of insulation wear, and check that cable type and length match ABB's recommendations for your drive rating.
4. **Verify motor terminations** at the motor junction box by removing the cover, checking torque on all lugs, looking for corrosion or blackened strands, and confirming the motor PE ground is clean and tight.
5. **Measure motor winding insulation** with a 500 V or 1000 V megohmmeter from each phase to ground and phase to phase to rule out winding breakdown or moisture ingress that could skew current readings.
6. **Reconnect, restore power, and clear the fault** using the drive keypad reset function, then run the motor under no-load and observe whether A2A1 returns or if the drive logs any new related faults.
7. **If the fault persists with wiring and motor proven good**, contact ABB service or an authorized distributor with your drive serial number, firmware version, and event log to diagnose internal current measurement hardware or request a control board calibration or replacement.

## Parts Often Needed

| Part | Notes |
|------|-------|
| VFD-rated motor cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-a2a1-fault-code&k=VFD-rated+motor+cable&tag=errorcodefixes-20) \| Use shielded or symmetrical three-phase cable sized per ABB ACS580 installation manual for your drive frame and cable length. |
| ABB ACS580 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-a2a1-fault-code&k=ABB+ACS580+control+board&tag=errorcodefixes-20) \| Consult ABB service for the exact replacement module and firmware version if internal current sensing circuitry is confirmed faulty. |

## When to Call a Pro

Call a qualified electrician or ABB-authorized service technician if you are not trained in VFD lockout-tagout procedures, if the fault returns after you have verified and corrected all motor cable and termination issues, or if ABB support indicates the drive requires internal calibration or board-level repair. Also call a pro immediately if you see any signs of arcing, burning, or swollen components on the drive output terminals, or if the motor insulation test fails. VFD current measurement circuits operate at low signal levels and require specialized diagnostic tools and factory training to troubleshoot safely.

## See Also

- [ABB ACS580 FF63 - STO Diagnostics Failure Fix](/posts/abb-acs580-ff63-fault-code/)
- [ABB ACS580 A0 Fault Code - Causes & Fix](/posts/abb-acs580-a0-fault-code/)
- [ABB ACS550 EFB3 Fault - Causes & Fix](/posts/abb-acs550-efb3-fault-code/)
- [ABB ACS550 EFB1 Fault Code - Causes & Fix](/posts/abb-acs550-vfd-efb1-fault-code/)
