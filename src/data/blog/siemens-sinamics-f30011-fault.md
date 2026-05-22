---
title: "Siemens SINAMICS G120 F30011 Fault — Phase Loss Fix"
description: "SINAMICS G120 F30011 (Line Phase Loss) means the Power Module's input phase-monitoring logic detected that one of the three input phases is missing or..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: siemens-sinamics-f30011-fault
featured: false
draft: false
tags:
  - siemens
  - vfd
  - industrial-maintenance
  - drives
  - line-phase-loss
---
## Quick answer

SINAMICS G120 F30011 (Line Phase Loss) means the Power Module's input phase-monitoring logic detected that one of the three input phases is missing or severely sagged for longer than the configured debounce time. Ninety percent of these are real — blown branch fuse, open disconnect pole, broken conductor at a lug, or a tripped upstream protection clearing one phase. The other ten percent are configuration: drive is fed from a single-phase derated supply but the firmware is configured for three-phase, or a phase-monitoring debounce window is set unreasonably tight.

## What F30011 means

The G120 doesn't directly measure each input phase voltage — it measures the resulting DC bus ripple. A healthy three-phase rectifier produces a 6-pulse ripple on the DC bus with a specific frequency (6× line frequency, so 360 Hz on a 60 Hz line). When one phase is missing, the bus ripple changes character — the frequency drops, the ripple amplitude increases, and the average bus voltage sags. The firmware detects this signature change and posts F30011.

The debounce window is configured by **p0291 Power Module config** and related parameters. By default the firmware waits long enough (typically 100–500 ms) that a one-cycle line glitch won't trip the fault. Sustained phase loss does.

F30011 is a different fault than F30003 (DC link undervoltage), though they can occur together. F30011 specifically identifies *phase loss* as the cause; F30003 just identifies that bus voltage dropped below threshold. On a single-phased input you may see both — F30011 first (detected by ripple signature), then F30003 (as the bus collapses).

The fault is significant because running on two phases will eventually destroy the input diode bridge (single-phasing nearly doubles the current through the remaining two phases) and overheats the DC bus capacitors. The drive trips to protect itself.

## Read the fault history first

This is the step that separates a 20-minute diagnosis from a parts swap. **Do not clear the fault before you read the history.**

Open STARTER or TIA Portal with Startdrive. Connect via PROFINET or USB. Drive object → Diagnostics → Faults and alarms.

Capture:

- **r0945** F30011 entries
- **r0948** timestamps — phase loss events often correlate with weather, time of day (cooling tower starts), or specific neighbor activity
- **r0949** — supplemental fault value, encodes which phase signature was detected as missing
- **r0026** — current DC link voltage
- **r2122** — alarm history, look for A30016 (input voltage out of tolerance) preceding the fault

**Field insight on F30011:** the r0949 value often tells you which phase. The detection is via ripple signature, so the firmware estimates which phase is missing based on the ripple pattern — it's not always perfect, but a consistent r0949 value across multiple events points to a specific phase failure. Walk that phase's path from the drive lug back to the upstream disconnect.

## Common causes (ranked by frequency)

1. **Blown branch fuse on one phase** — fuse cleared on overcurrent, ground fault, or simple end-of-life. Most common F30011 cause.
2. **Loose terminal on one input phase** — lug not torqued to spec or backed off over thermal cycling. The connection becomes high-impedance under load.
3. **Open contactor pole or disconnect contact** — upstream switching gear with one pole that's no longer making contact.
4. **Broken conductor at a connector or splice** — wire failure inside the panel or out in the conduit. Sometimes invisible — the wire looks intact but a strand-by-strand break has dropped current capacity.
5. **Utility phase loss** — utility transformer lost a primary fuse, drive sees the resulting secondary phase loss. Rare in commercial settings but happens.
6. **Single-phase supply with three-phase configuration** — drive is being fed single-phase (typical only for very small G120 ratings) but parameterized for three-phase. F30011 fires on every power-up.
7. **Failed phase-monitoring relay or false trip** — extremely rare on G120; the monitoring is firmware-based, not via a separate relay. Almost never the cause.

## Step-by-step diagnosis

Before you touch anything: lock and tag the disconnect, wait 5 minutes for DC link discharge, verify zero voltage at the DC link terminals with a CAT-IV meter.

1. **Read r0945, r0949 before clearing.** Note the phase indicated by r0949 and any precedent A30016 alarms.

2. **Verify the input fuses.** Power off, remove each input fuse, check continuity with a meter. Replace any open fuse — but find out *why* it opened before re-energizing. A fuse that cleared has a reason.

3. **Check terminal torque at every input lug.** Calibrated torque screwdriver, published spec on the cover label. Look for discoloration (heat-stressed connection), melted insulation around the lug, and any sign of arcing.

4. **Meter input voltage at the drive terminals — with the drive de-energized and locked.** L1-L2, L2-L3, L3-L1. With supply restored upstream (drive still locked out), each pair should read three-phase voltage within ±10% of nominal. A single low reading on one pair points to the missing phase.

5. **Trace the missing phase upstream.** From the drive input terminal, follow that phase back through every connection point: branch disconnect, distribution panel breaker, MCC bucket, utility transformer secondary. The break is somewhere in that path.

6. **Verify single-phase vs. three-phase configuration.** If your drive is small enough for single-phase operation (typical limit is around 4 kW on G120 with appropriate part number), confirm **p0205 Application input phases** (or the relevant parameter for your Control Unit firmware revision) matches your supply. A three-phase drive being fed single-phase is misconfigured and will F30011 every time.

7. **Inspect upstream switching gear.** Open every disconnect and contactor between the drive and the utility entrance. Look for: welded contacts, burned arc chutes, broken pole shafts, evidence of arcing across an open pole. A worn motor disconnect with one pole that doesn't fully close on closure is a common F30011 source.

8. **Set up a power quality logger.** If standing measurements are clean and the F30011 is intermittent, install a Fluke 1748 on the drive input for 7 days. Look for momentary phase dropouts during specific events (compressor start, large fault clearing).

> **Field knowledge nugget:** On Siemens G120 drives installed in older industrial facilities with 480V delta supplies and split-bolt taps in the main panel, F30011 trips that appear after years of trouble-free operation are almost always a corroded split-bolt connection deep in the distribution wiring, not a drive problem. The split-bolt sits in a J-box or panel where moisture and dissimilar-metal corrosion (aluminum branch wire to copper main bus) slowly increases the joint resistance. The joint gets hot under load, oxidizes faster, and one day it opens entirely. I traced a chronic F30011 problem at a New Jersey chemical plant to a split-bolt buried in a 25-year-old MCC bucket — the connection had gone from milliohms to over an ohm under load. Heat-thermography is your friend on this; an FLIR scan of distribution gear under load will catch this hours before it becomes a fault.

## Parts that may need replacement

| Part | Order Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Bussmann FRS-R-30 input fuse (480V) | FRS-R-30 | $14–$22 each | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30011-fault), [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| Bussmann FRS-R-60 input fuse (480V) | FRS-R-60 | $22–$32 each | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30011-fault), [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| PM240-2 Power Module, 7.5kW, 400V | 6SL3210-1PE22-8UL0 | $1,200–$1,600 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30011-fault), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30011-fault) |
| CU240E-2 PN Control Unit | 6SL3244-0BB12-1PA1 | $480–$640 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30011-fault), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30011-fault) |
| Square D QO-series 30A 3P breaker | QO330 | $120–$165 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30011-fault) |
| Phoenix Contact terminal torque screwdriver | 1212597 | $190–$240 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30011-fault) |
| FLIR thermal camera (entry pro) | FLIR E54 | $2,800–$3,400 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30011-fault) |
| Fluke 1748 power quality logger | FLUKE-1748/BASIC | $7,400–$8,800 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30011-fault), [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |

## When to call Siemens, an electrician, or a controls engineer

Call a licensed industrial electrician immediately if: the missing phase is not obviously a fuse or terminal issue and the trace points to utility-side or main distribution gear; you see evidence of arc-flash damage in any switching equipment; or the fault correlates with utility transformer activity. Call a controls engineer for: F30011s that persist after all upstream electrical has been verified good (suggests internal drive issue); coordinated multi-drive systems where a single phase event is affecting multiple drives differently; or applications where the phase-monitoring debounce needs custom tuning.

## FAQs

**Can I bypass F30011 to keep running?** No. The G120 firmware does not allow disabling phase-loss detection in any documented way, and bypassing it would mean running a drive on two phases. The diode bridge would survive maybe a few hours at low load before failing — and IGBT modules will follow. Don't try.

**Why does F30011 sometimes show up at night when no one is around?** Two common reasons: ambient temperature drops cause connection contraction, opening a marginal joint; or off-peak utility maintenance creates brief phase events on the distribution feeder. Either way the F30011 is real — the drive isn't imagining it.

**My drive is single-phase rated and is single-phase wired. Why does it think I have phase loss?** Configuration mismatch. **p0205** (or equivalent on your Control Unit firmware) must be set for single-phase operation. Otherwise the firmware looks for three-phase ripple signature, doesn't find it, and reports F30011. Reference your Power Module's manual for single-phase configuration — many G120 frames are not single-phase rated at all and you cannot configure them to operate single-phase.

**What's the difference between F30011 and F07802?** F30011 is detected by ripple analysis on the DC bus and is the Power Module-side phase loss fault. F07802 (Power supply phase missing) is the Control Unit-side equivalent that also considers the regenerative case for Active Line Module drives. On a standard G120 you'll see F30011; on an S120 with ALM you might see F07802.

**Will a line reactor prevent F30011?** No. A line reactor adds impedance and helps with current quality and transient protection, but it can't synthesize a missing phase. If a phase is gone, it's gone — the drive will fault regardless of reactor. Reactors do help with the *upstream* causes (limiting fault currents that blow fuses), so they have indirect value.

## Related guides

- [Siemens SINAMICS F30001 Fault — Power Module Overcurrent Fix](/posts/siemens-sinamics-f30001-fault)
- [Siemens SINAMICS F30003 Fault — DC Link Undervoltage Fix](/posts/siemens-sinamics-f30003-fault)
- [Siemens SINAMICS F30021 Fault — Ground Fault Fix](/posts/siemens-sinamics-f30021-fault)
