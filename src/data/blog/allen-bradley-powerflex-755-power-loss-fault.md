---
title: "Allen-Bradley PowerFlex 755 Power Loss Fault Fix"
description: "PowerFlex 755 Power Loss Fault (F3 Power Loss, sometimes paired with F2 Aux Power Loss in the same event) means the drive detected loss of one or more input..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: allen-bradley-powerflex-755-power-loss-fault
featured: false
draft: false
tags:
  - allen-bradley
  - vfd
  - industrial-maintenance
  - drives
  - power-loss-f2-f3-series
---
## Quick answer

PowerFlex 755 Power Loss Fault (F3 Power Loss, sometimes paired with F2 Aux Power Loss in the same event) means the drive detected loss of one or more input phases, or the DC bus collapsed below the operating threshold while the drive was running. The most common field cause I find is a blown branch fuse — usually one phase of a Class J or Class T fuse set that opened on a transient and the drive correctly detected the resulting phase loss. A close second is a contactor with one pole that's not fully closing (mechanical wear, contamination, or undersized coil voltage) leaving the drive running on two phases for a few cycles before the bus collapses.

## What PowerFlex 755 Power Loss Fault means

The 755 distinguishes between **F2 Aux Power Loss** (loss of the auxiliary control supply that powers the cassette and option cards) and **F3 Power Loss** (loss of one or more input phases or DC bus collapse during operation). They're related but trip on different conditions and call for different troubleshooting.

**F3 Power Loss** specifically: the drive monitors input voltage on R, S, T terminals via the precision divider on the power module and the rectified DC bus on the bus capacitor bank. When the drive detects either (a) one or more input phases dropped below 65% of nominal for more than 6 cycles (100 ms at 60 Hz), or (b) DC bus dropped below the undervoltage threshold (310 VDC on a 480V class) with sufficient sustained duration, it latches F3 and coasts the motor.

The 755 is more sophisticated than the older PowerFlex 70 generation in its detection. The 755 looks at each input phase individually via per-phase voltage feedback, so it can tell you which phase dropped via parameter **412 Input Phase Status** — that parameter encodes which phase or phases were lost in a bit-field readable from the panel or from Studio 5000.

Distinguish F3 from related faults: **F4 Undervoltage** is the same magnitude trip but specifically references the DC bus during continuous running. **F5 Overvoltage** is the high-side trip. **F12 HW Overcurrent** is an unrelated short-circuit trip. If the fault log shows F3 immediately followed by F4 (or vice versa), the events are linked — typically a phase loss caused the bus to collapse.

## Read the fault history first

Read the fault log before pressing Clear Faults. The 755 keeps the last 32 faults with full snapshot data, and the snapshot of the active fault is critical for diagnosing F3.

**Via Studio 5000 Logix Designer (preferred for 755 on EtherNet/IP):**

1. Open project, expand I/O tree, right-click PowerFlex 755 drive → **Properties**
2. Navigate to **Drive → Faults** tab
3. Most recent 32 faults appear with code, descriptor, and timestamp
4. Click the most recent F3 entry to see the snapshot
5. Read **parameter 412 Input Phase Status** — bit 0 = phase R, bit 1 = phase S, bit 2 = phase T; a set bit indicates that phase was below threshold at the moment of trip
6. Read **parameter 11 DC Bus Voltage** and **parameter 7 Output Frequency** snapshot values

**Via Connected Components Workbench or the HIM (Human Interface Module):**

1. From the run screen, press **Esc** to reach the main menu
2. Navigate to **Diagnostics → Fault Queue**
3. Most recent 32 faults appear in a scrollable list
4. Highlight the most recent F3 entry, press **Enter** to see snapshot details
5. Pull parameters:
   - **N002** — Last Stop Source (look for value 7 "Power Loss")
   - **N003** — Last Fault Code (will read 3)
   - **N005** — Fault 1 Bus Voltage
   - **N011** — Fault 1 Drive Status
   - **412** — Input Phase Status (which phase or phases were lost)
   - **413** — Input Voltage R-S, **414** — S-T, **415** — T-R (continuous monitoring values)

Rockwell documents this in PowerFlex 750-Series Programming Manual publication 750-PM001 chapter 4 and the Diagnostic Code Reference 750-RD001.

**Field insight — the F3 history trap:** parameter 412 (Input Phase Status) is captured at the moment of trip detection, which can be 100 ms or more after the actual phase loss began. If the lost phase recovered quickly (typical for a momentary contactor bounce or a fuse holder with a fretting contact), 412 may read 0 by the time you read it. The trip happened, the drive remembered it happened, but the bit field shows current state. Use parameter 416 Input Phase Loss Time (cumulative count of phase-loss events) to see whether this is chronic — if 416 is incrementing daily, you have a recurring intermittent issue, not a single event.

## Common causes (ranked by frequency)

1. **Blown branch fuse on one phase** — Class J, Class T, or Class CC fuse opened on a transient (often a phase-to-ground motor fault elsewhere on the same branch), leaving the drive on two phases until trip
2. **Contactor with one pole not closing** — mechanical wear on the contact bridge, contamination, undersized coil voltage causing chatter, or a damaged auxiliary contact giving false "closed" feedback
3. **Loose lug on R, S, or T input terminal** — high-impedance phase that drops voltage under load; classic finding after a panel was serviced and lug torque wasn't verified
4. **Single-phasing from upstream** — an upstream fuse, breaker pole, or transformer fuse on the utility primary; drive correctly detects what the system did
5. **DC bus capacitor degradation** — aged caps lose capacitance, can't hold the bus through normal sags or pre-charge dips that healthy caps would ride through
6. **Pre-charge circuit failure** — pre-charge resistor open or bypass relay welded; drive starts but bus collapses under first load
7. **Severe line voltage imbalance** — phases differ by more than 5–8%, drive detects one as effectively "lost"

## Step-by-step diagnosis

Before opening the cabinet: lock and tag the upstream disconnect. Wait the rated capacitor discharge — PowerFlex 755 frames 1–4 require **5 minutes**, frames 5–8 require **15 minutes**. Verify zero DC bus at DC+ and DC- terminals with a CAT-IV meter rated 1000 VDC. Stay outside the NFPA 70E arc-flash boundary on the cabinet label until zero energy is confirmed and you are in the proper PPE.

1. **Read the fault history before clearing.** Pull N002, N003, N005, N011, and parameters 412 through 416. Note which phase (or phases) parameter 412 shows lost at trip. If 416 shows multiple recent power-loss events, this is chronic — different diagnostic path than a one-time trip.

2. **Verify branch fuses.** Pull each upstream fuse cartridge with the disconnect locked open. Use a continuity meter — open fuses read OL (overload, infinite resistance). A blown fuse on the phase that parameter 412 identified is your smoking gun. Replace fuses as a *matched set* of the same Class, ampere rating, and manufacturer — never mix Bussmann FRS-R with Mersen AJT, even at the same rating.

3. **Inspect upstream contactor.** With drive de-energized, manually actuate the contactor (most modern motor-control contactors have a manual test button on the armature) and watch for all three poles to close simultaneously. Inspect each contact bridge for pitting, welding, or one bridge sitting noticeably higher than the others. A worn contactor frequently shows up first as one pole not closing reliably under cold ambient conditions.

4. **Check input lug torque.** With drive de-energized, verify torque on R/L1, S/L2, T/L3 lugs. PowerFlex 755 frame 2 spec is 4.5 Nm (40 in-lb) on M6 lugs; verify against the chart on the inside of the drive front cover for your specific frame. A loose lug discolors over time — look for browned insulation around the terminal or a cooked appearance on the lug barrel.

5. **Measure input voltage with drive running.** Re-energize the drive (after dead-state confirmation, in proper PPE). With drive at idle (run command not asserted), measure R-S, S-T, T-R with a true-RMS meter. All three should read within 3% of each other and within ±10% of nameplate. Then issue a run command and re-measure under load — significant voltage drop on one phase under load indicates a loose connection or undersized branch wire.

6. **Verify parameter 372 Power Loss Mode.** Read **parameter 372 Power Loss Mode**:
   - 0 = Coast (drive trips F3 immediately on power loss)
   - 1 = Decel (drive uses regenerative braking to decel as long as possible before tripping — masks momentary events)
   - 2 = Continue (drive attempts to ride through using residual bus energy)
   For most applications, 0 or 1 is appropriate. Setting to 2 can mask real problems — only use 2 if you have a thoroughly characterized power-quality environment.

7. **Check pre-charge circuit if drive is older than 5 years.** Power up with no run command. Watch parameter **11 DC Bus Voltage** ramp from zero. Healthy 480V drive should ramp to approximately 670 VDC in 1–2 seconds and hold. Slow ramp, stalled ramp, or oscillation means pre-charge resistor or bypass relay has failed — not field-repairable on most 755 frames, requires drive or power-module replacement.

8. **Capture power quality data if standing voltage looks fine.** Install a Fluke 1748 or 1735 logger on the drive input for 7 days. Trigger threshold: 10% below nominal for 100 ms on any phase. Single-phasing events from upstream are often invisible to standing measurements but obvious on a logger trace.

9. **For chronic intermittent F3 with no clear cause:** swap the affected drive into a known-good identical drive socket. If the fault follows, the drive's input voltage sensing or pre-charge circuit has degraded — replace the drive. If the fault stays with the panel, you have an electrical-system problem outside the drive.

## Parts that may need replacement

| Part | Catalog Number | Typical Cost | Where to Buy |
|---|---|---|---|
| PowerFlex 755, 480V, 5HP | 20G11NC011AA0NNNNN | $3,200–$3,800 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-755-power-loss-fault), [Wolf Automation](https://www.wolfautomation.com) |
| PowerFlex 755, 480V, 20HP | 20G11NC030AA0NNNNN | $5,500–$6,600 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-755-power-loss-fault), [Wolf Automation](https://www.wolfautomation.com) |
| PowerFlex 755, 480V, 50HP | 20G11NC072AA0NNNNN | $9,200–$11,000 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-755-power-loss-fault), [Wolf Automation](https://www.wolfautomation.com) |
| Bussmann FRS-R-30 Class RK5 fuse | FRS-R-30 | $14–$22 each | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-755-power-loss-fault), [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| Mersen AJT-30 Class J fuse | AJT30 | $28–$45 each | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-755-power-loss-fault), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-755-power-loss-fault) |
| Allen-Bradley 100-E contactor 30A 480V | 100-E30KJ11 | $385–$485 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-755-power-loss-fault), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-755-power-loss-fault) |
| Auxiliary Power Supply Module | 20-750-APS | $385–$485 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-755-power-loss-fault), [Wolf Automation](https://www.wolfautomation.com) |
| 22-HIM-A6 Full-Numeric HIM | 22-HIM-A6 | $385–$485 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-755-power-loss-fault), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-755-power-loss-fault) |
| Fluke 1748 power quality logger | FLUKE-1748/BASIC | $7,400–$8,800 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-755-power-loss-fault), [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| Klein torque wrench 1/4" drive | Klein TQ235U | $185–$240 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |

## When to call a controls engineer

Bring in senior support when: parameter 416 shows F3 events incrementing daily but standing measurements look clean (suggests upstream utility-quality issue that requires coordination with utility engineering); F3 is co-occurring with F2 Aux Power Loss on the same event (suggests a primary power supply or upstream transformer issue affecting both the main and auxiliary feeds); the drive is part of a common DC bus configuration with multiple PowerFlex inverters; or when F3 only happens during specific seasonal conditions suggesting capacitor temperature dependency or shift-related upstream loading.

## FAQs

**Can I disable F3 to keep running through power events?** Not really. Setting parameter 372 Power Loss Mode to 2 (Continue) extends ride-through but doesn't truly disable the fault — if the bus collapses far enough, the drive will trip F4 instead. The fault exists to protect the drive from operating below safe bus voltage. Address the cause, don't mask the symptom.

**Does F3 mean my drive is dead?** Almost never. F3 is a diagnostic telling you the drive lost input voltage — the drive itself is usually fine. Find the upstream cause: fuse, contactor, breaker, or utility event.

**Why does F3 happen only during a thunderstorm?** Utility faults from lightning clearing on the distribution feeder cause momentary single-phasing as a recloser cycles. The fault clears upstream in a few cycles but your drive saw the dip and tripped F3. Install a line reactor (3% or 5%) to add ride-through, or accept the trip and use auto-restart (parameter 145 Auto Rstrt Tries / 144 Auto Rstrt Delay).

**Difference between F3 and F2?** F2 is Auxiliary Power Loss — the 24VDC control supply (either the integrated supply or the 20-750-APS) collapsed. F3 is Power Loss — the main three-phase input or the DC bus dropped. F2 means the cassette saw its own power fail; F3 means the drive saw its three-phase input fail.

**Should I install auto-restart on F3?** Carefully. Parameter 145 Auto Rstrt Tries sets the number of retry attempts and 144 Auto Rstrt Delay sets seconds between tries. Useful for fan and pump applications where unattended restart is desired. Dangerous for machinery where an unexpected restart could injure personnel — for those, leave auto-restart disabled and require manual reset.

## Related guides

- [Allen-Bradley PowerFlex 755 Aux Input Fault Fix](/allen-bradley-powerflex-755-aux-input-fault/)
- [Allen-Bradley PowerFlex 753/755 Control Sync Fault Fix](/allen-bradley-powerflex-753-control-sync-fault/)
- [Allen-Bradley PowerFlex F004 Fault — Undervoltage Fix](/allen-bradley-powerflex-f004-fault/)
- [Allen-Bradley PowerFlex F081 Fault — Communication Loss Fix](/allen-bradley-powerflex-f081-fault/)
- [Yaskawa GA800 Uv1 Fault — DC Undervoltage Fix](/yaskawa-ga800-error-uv1/)
