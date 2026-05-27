---
title: "ABB ACS580 Fault 3220 — DC Undervoltage Fix"
description: "ABB ACS580 fault 3220 DC Link Undervoltage means the intermediate DC bus dropped below approximately 320 VDC on a 380–480V drive (185 VDC on a 200–240V..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: abb-acs580-fault-3220
featured: false
draft: false
tags:
  - abb
  - vfd
  - industrial-maintenance
  - drives
  - dc-link-undervoltage
---
## Quick answer

ABB ACS580 fault **3220 DC Link Undervoltage** means the intermediate DC bus dropped below approximately 320 VDC on a 380–480V drive (185 VDC on a 200–240V drive, 460 VDC on a 525–690V drive) for longer than the firmware ride-through window and the drive can no longer guarantee clean PWM output. By far the most common field cause I find is a coincident load on the same branch circuit pulling line voltage into a momentary sag — another VFD starting, an air compressor across-the-line, or a welder duty cycle. A close second is a loose lug on U1, V1, or W1 producing a high-impedance phase that sags under load current.

## What ABB ACS580 fault 3220 means

The ACS580 measures DC link voltage at the bus capacitor bank through a precision divider on the CCU-25 control unit. The undervoltage trip threshold is 320 VDC ±10 VDC on a 480V class drive (parameter 95-01 / 30-30 family does not adjust this threshold — it is fixed in firmware). The drive trips 3220 when measured bus voltage drops below threshold for longer than the ride-through window in parameter **30-21 Minimum DC voltage** (default 0.65 per-unit = approximately 320 VDC) sustained for the auto-restart timer.

The ACS580 includes a **power loss ride-through** function — parameter **30-01 Local control loss action**, **21-01 Start function**, and especially the **autoreset** features in parameter group 31-12 through 31-16. These can mask intermittent 3220 by automatically restarting, but they don't fix the underlying cause. Find the cause.

Distinguish 3220 (running undervoltage) from related faults: **3211 Charging fault** means the pre-charge circuit didn't complete properly at power-up. **3212 Charging time-out** means pre-charge ran too long. **3213 No control board power** means the auxiliary low-voltage supply collapsed. If the log shows 3211, 3212, or 3213 preceding 3220, the issue is hardware-internal to the drive, not external line sag.

## Read the fault history first

Read the fault log before pressing Reset. The ACS580 keeps the most recent 16 faults in memory, retained across power cycles. On the ACS-AP-W or ACS-AP-I assistant control panel:

1. Press **Menu**, arrow to **Diagnostics**, press **Enter**
2. Select **Fault & event log** — most recent fault appears first
3. Highlight the most recent 3220 entry and press **Enter** for snapshot details
4. Read parameter group **04 Warnings and faults**:
   - **04.01** — Tripping fault (will read 3220)
   - **04.02** — Active warning 1 (look for 30-30 group warnings preceding the trip)
   - **04.03** — Active warning 2
   - **04.06** — Previous fault 1
   - **04.07** — Previous fault 2 (and so on through 04.16)
5. Cross-reference with the parameter group **01 Actual values** snapshot:
   - **01.11** DC Voltage at trip — the critical reading for 3220
   - **01.07** Motor current at trip
   - **01.06** Output frequency at trip
   - **01.14** Output power at trip

In Drive Composer Pro (PC software via USB or Ethernet), open **Diagnostics → Event Logger** for time-series capture of operating data around the trip — Drive Composer's logger captures up to 60 seconds of pre-trip data if it was running.

ABB documents this in the ACS580 Firmware Manual 3AXD50000016097 chapter 9 (Fault Tracing) and the Hardware Manual 3AXD50000018826 chapter 12.

**Field insight — the 3220 history trap:** 01.11 is captured at the firmware control loop rate (approximately 5 ms). The bus may have already started recovering by the time the trip latched. So if 01.11 reads 325 VDC at trip and you think "the bus didn't really sag that hard," remember you're seeing one sample, not the minimum of the dip. Use Drive Composer's event logger or a Fluke 1748 on the input to capture the actual sag depth and duration — the drive's snapshot tells you the trip happened, not the worst point of the dip.

## Common causes (ranked by frequency)

1. **Line voltage sag from coincident load** — another VFD soft-starting, large motor across-the-line, welder striking, chiller compressor inrush — pulls line voltage into the drive's sag-detection threshold
2. **Loose input lug** — U1, V1, or W1 not torqued to spec creates a high-impedance phase that sags under load
3. **Single-phased input** — branch fuse blew, disconnect pole isn't fully closed, contactor pole welded open — drive runs on 2 phases for a few cycles before the bus collapses
4. **Pre-charge circuit problem** — pre-charge resistor open or pre-charge bypass relay failing (will typically log 3211 or 3212 first)
5. **Aged bus capacitors** — drives older than 7–10 years lose capacitance, can't ride through normal sags they handled when new
6. **Undersized branch circuit or transformer** — voltage drop under full motor current pulls bus into trip range during acceleration
7. **Power loss ride-through 30-30 disabled** — someone set parameter 30-30 to 0, disabling automatic ride-through

## Step-by-step diagnosis

Lock and tag the input disconnect. Wait the ACS580 capacitor discharge time — ABB specifies a minimum of **5 minutes** for R0–R5 frames, **10 minutes** for R6–R9, **15 minutes** for R10–R11. Verify zero DC bus at UDC+ and UDC- terminals with a CAT-IV meter rated 1000 VDC. Respect the NFPA 70E arc-flash boundary on the cabinet label and wear the PPE specified before opening the cabinet.

1. **Read the fault log before clearing.** Capture 04.01 through 04.16 and snapshot data 01.11 (DC voltage at trip), 01.07 (current at trip), 01.06 (frequency at trip). A 01.11 reading near 320 VDC is textbook line sag. A reading near 200 VDC or below means single-phased input or hardware-class problem — investigate differently.

2. **Measure input line voltage at U1, V1, W1.** Use a true-RMS meter. Read all three line-to-line pairs both standing and during the next attempted start. Standing voltage should be within ±10% of nameplate: 432 to 528 VAC for a 480V drive. Imbalance greater than 3% will produce intermittent 3220 even when average voltage looks fine — ABB specifies max 3% imbalance for full-output operation.

3. **Hunt the loose connection.** De-energize and verify zero. Check torque on every input lug, output lug, and ground. ACS580-01-12A6-4 (R1 frame) M5 input terminals are spec'd at 2.5 Nm (22 in-lb). The frame-specific torque chart is on the inside of the front cover. Look for discoloration, melted insulation, or fretting corrosion on stranded copper.

4. **Verify branch fuses and upstream disconnect.** Pull each fuse cartridge, ohm-test for continuity. A single-phased input is the classic 3220 producer. Replace fuses as a matched set, same I²t rating and same manufacturer.

5. **Walk the surrounding equipment.** Was another VFD starting at the same timestamp? An air compressor cycling? The fault timestamp from the panel log plotted against your plant SCADA trend will almost always show a coincident event. This is the step that turns "the drive is broken" into "the drive is correctly detecting an upstream problem."

6. **Verify ride-through parameters.** Read parameter **30-30 Overvoltage control** (should be On — yes, this also affects undervoltage ride-through in the ACS580 firmware), **21-01 Start function** (Auto for restart on power return), and **31-12** through **31-16** (Autoreset configuration). The defaults are reasonable; if they've been changed, restore them and re-test.

7. **Enable Power Loss Control via parameter 30-21.** The ACS580 has a kinetic energy buffering function that harvests the motor's inertia to keep the bus alive through short utility sags. For high-inertia loads (fans, centrifuges) this can ride through 300–500 ms dips that would otherwise trip 3220. Configure via parameter group **30-21 Minimum DC voltage** and the **31-12** restart settings.

8. **Test pre-charge if drive is older than 5 years.** Power up the drive with no run command. Watch **01.11 DC Voltage** on the panel. Healthy ACS580 on 480V should ramp from 0 VDC to approximately 670 VDC in 1–2 seconds then hold steady. If the bus ramps slowly, stops below 600 VDC, or oscillates, pre-charge resistor or bypass relay has failed — the drive will log 3211 or 3212 and needs replacement (not field-repairable).

9. **Megger motor and motor leads if you suspect load-side fault.** A motor-to-ground fault can pull the bus down on start. Disconnect U2, V2, W2 from the drive output. Megger each phase to ground at 1000 VDC. Below 1 megohm at 25°C is a definite ground fault — fix the motor before re-energizing the drive.

## Parts that may need replacement

The ACS580's bus capacitor bank, pre-charge resistor, and pre-charge relay are not field-serviceable on frames R0–R5. A confirmed pre-charge or capacitor failure means drive replacement.

| Part | Catalog Number | Typical Cost | Where to Buy |
|---|---|---|---|
| ACS580-01, 480V, 4kW (5HP) | ACS580-01-09A5-4 | $1,650–$1,950 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=abb-acs580-fault-3220), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=abb-acs580-fault-3220) |
| ACS580-01, 480V, 7.5kW (10HP) | ACS580-01-017A-4 | $2,250–$2,650 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=abb-acs580-fault-3220), [Wolf Automation](https://www.wolfautomation.com) |
| ACS580-01, 480V, 18.5kW (25HP) | ACS580-01-038A-4 | $3,800–$4,500 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=abb-acs580-fault-3220), [Wolf Automation](https://www.wolfautomation.com) |
| ACS580-01, 480V, 37kW (50HP) | ACS580-01-073A-4 | $5,600–$6,800 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=abb-acs580-fault-3220), [Wolf Automation](https://www.wolfautomation.com) |
| ABB CHK-A1 line reactor 3% 11kW | 68878601 | $425–$565 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=abb-acs580-fault-3220), [Wolf Automation](https://www.wolfautomation.com) |
| ACS-AP-W assistant control panel | 3AUA0000094568 | $385–$485 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=abb-acs580-fault-3220) |
| Bussmann FRS-R-30 input fuse (480V) | FRS-R-30 | $14–$22 each | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=abb-acs580-fault-3220), [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| Fluke 1748 power quality logger | FLUKE-1748/BASIC | $7,400–$8,800 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=abb-acs580-fault-3220), [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| Fluke 87V industrial multimeter | FLUKE-87-5 | $480–$580 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=abb-acs580-fault-3220) |
| Wera 7440 torque screwdriver 1.2–3.0 Nm | Wera 05074722001 | $185–$240 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |

## When to call a controls engineer

Bring in senior support when: 3220 trips show 01.11 readings consistently below 250 VDC suggesting single-phasing or hardware pre-charge failure; the fault history pairs 3220 with 3211/3212/3213 in any combination (multiple drive-internal issues require ABB factory diagnosis); the drive is on a long branch run from a small transformer and a voltage-drop calculation shows you're operating near the edge of code-compliant sizing; or when 3220 trips happen only at specific times of day (suggests shift-change capacitor switching at the substation that requires utility coordination).

## FAQs

**Can I disable the 3220 trip?** No — it's a fundamental safety trip. If the bus is below 320 VDC the drive cannot produce clean PWM output and the IGBTs would commutate into saturation. The trip protects the drive. What you can adjust is the ride-through window (30-21) and autoreset behavior (31-12).

**Will a line reactor help with 3220?** A 3% or 5% input reactor (ABB CHK-A1 or CHK-A2 series) reduces the depth of transient sags by adding source impedance that filters fast dips. It does slightly worsen steady-state voltage drop under load, but the trade is usually worth it in noisy industrial environments. ACS580 includes a DC link choke as standard — adding an AC line reactor is the next layer.

**My ACS580 trips 3220 on cold mornings only. Why?** Bus capacitor ESR (equivalent series resistance) rises at low temperatures. Older capacitors that work fine at 25°C can fail to hold bus voltage under load at 0°C. This is an end-of-life indicator. Replace the drive before it strands you in February.

**Difference between 3220 and 3211?** Fault 3220 is running-state undervoltage (bus dropped while the drive was operating). Fault 3211 is charging fault — pre-charge circuit failed at power-up, the bus never reached operating voltage. 3211 means the pre-charge resistor or pre-charge relay has failed; 3220 means an external sag pulled the running bus down.

**Should I install a UPS in front of the VFD?** Almost never. The ACS580's bus capacitors plus power-loss ride-through (parameter group 30) handle 95% of normal utility events. Real solutions to chronic 3220: a 5% line reactor for filtering, an isolation transformer for clean power, or an oversized supply transformer. A UPS sized for full VFD load is huge, expensive, and adds its own reliability concerns.

## Related guides

- [ABB ACS580 Fault 3210 — DC Overvoltage Fix](/abb-acs580-fault-3210/)
- [ABB ACS580 Fault 2310 — Overcurrent Fix](/abb-acs580-2310-fault/)
- [Yaskawa GA800 Uv1 Fault — DC Undervoltage Fix](/yaskawa-ga800-error-uv1/)
- [Allen-Bradley PowerFlex F004 Fault — Undervoltage Fix](/allen-bradley-powerflex-f004-fault/)
- [Danfoss FC-302 Alarm 12 — Overcurrent Fix](/danfoss-fc302-alarm-12/)

## See Also

- [ABB ACS880 Fault 2310 Overcurrent — Causes & Fix](/posts/abb-acs880-fault-2310-overcurrent/)
- [ABB ACS580 Fault 3210 — DC Overvoltage Fix](/posts/abb-acs580-fault-3210/)
- [ABB ACS550 F0001 Fault — Causes & Fix](/posts/abb-acs550-f0001-overcurrent/)
- [ABB VFD Fault 5010 — Causes & Fix](/posts/abb-vfd-fault-5010/)
