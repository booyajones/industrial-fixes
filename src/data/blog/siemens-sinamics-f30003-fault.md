---
title: "Siemens SINAMICS G120 F30003 Fault — DC Link Undervoltage Fix"
description: "SINAMICS G120 F30003 (DC Link Undervoltage) means the bus voltage dropped below the Power Module's minimum threshold while in Run state — about 360 VDC on a..."
pubDatetime: 2026-05-20T17:00:00Z
modDatetime: 2026-05-20T17:00:00Z
author: "Dana Kowalski"
slug: siemens-sinamics-f30003-fault
featured: false
draft: false
tags:
  - siemens
  - vfd
  - industrial-maintenance
  - drives
  - dc-link-undervoltage
---
## Quick answer

SINAMICS G120 F30003 (DC Link Undervoltage) means the bus voltage dropped below the Power Module's minimum threshold while in Run state — about 360 VDC on a 400V-class PM240-2. The most common cause is a line-side sag from a coincident high-current load starting somewhere nearby (another VFD across-the-line starting, large compressor kicking on, welder duty cycle), not a drive failure. Loose input terminals and undersized branch circuits are close behind.

## What F30003 means

The G120 monitors DC link voltage at the bus capacitor terminals continuously. When the drive is in Run state and bus voltage falls below the Vdc_min threshold for a debounce window (typically 5–10 ms), F30003 fires. Below Vdc_min the Power Module cannot guarantee correct PWM output — gate-drive supplies droop, IGBT switching gets sloppy, and the firmware loses confidence in current control.

The Vdc_min threshold on a 400V-class G120 sits around 360 VDC (you can read the firmware-default in the Function Manual for your CU/PM combo). The drive does *not* measure line voltage directly to declare undervoltage — the bus reading is the source. Three things make this important:

- A perfectly normal line that sags briefly during a coincident load start can pull the bus through Vdc_min in milliseconds. Your handheld DMM at the input terminals will show nominal voltage long after the event.
- A single-phased input (blown fuse, open contactor pole) pulls the bus down hard the moment the drive draws load. F30003 will trip almost immediately.
- An aged bus capacitor with reduced capacitance can't ride through normal line sags it handled when new.

The Vdc_min controller (**p1240 = 1** enables both Vdc_min and Vdc_max controllers) can extend ramp times during a sag to keep the bus above Vdc_min, but this only helps during commanded acceleration; it can't recover from a true line failure.

## Read the fault history first

This is the step that separates a 20-minute diagnosis from a parts swap. **Do not clear the fault before you read the history.**

Open STARTER or TIA Portal with Startdrive. Connect via PROFINET or USB. Drive object → Diagnostics → Faults and alarms.

Capture:

- **r0945** entries showing F30003
- **r0948** timestamps
- **r0949** — DC link voltage at trip. A trip at 355 VDC tells a different story than a trip at 200 VDC.
- **r0026** current DC link voltage
- **r2122** alarm history — A07911 (Vdc_min controller active) preceding the trip means the controller saw it coming but couldn't recover.

**Field insight on F30003:** the trip happens *after* the line voltage has already recovered. The drive logs the fault based on a 50–200 millisecond dip you will never see on a handheld DMM. If the r0949 value at trip is below 250 VDC on a 400V drive but your standing measurement at the input terminals shows nominal 400V three-phase, you are chasing a transient — put a Fluke 1748 on the branch for 24–72 hours.

## Common causes (ranked by frequency)

1. **Line voltage sag from a coincident load starting** — another VFD on the same branch starting at full load, a large motor across-the-line start, welder duty cycle, utility sag from a fault clearing upstream.
2. **Loose input terminal** — L1, L2, or L3 lug not torqued to spec. Frame FSC torque spec on G120 PM240-2 is approximately 1.5 Nm. A loose connection creates a high-impedance phase that drops voltage under load.
3. **Blown branch fuse or open contactor pole** — drive runs on two phases for a few cycles before the bus collapses far enough to trip. r0949 in this case is usually very low (200–250 VDC).
4. **Aged bus capacitors** — drives older than 8–10 years in high-ambient panels lose capacitance and can't ride through a normal sag.
5. **Undersized branch circuit** — wire run is technically code-compliant but voltage drop at full motor current pulls the drive into trip range during acceleration.
6. **Failed pre-charge contactor** — drive starts on the pre-charge path but never transitions to main bus, so under load the bus sags.

## Step-by-step diagnosis

Before you touch anything: lock and tag the disconnect, wait 5 minutes minimum, verify zero DC link energy with a CAT-IV meter.

1. **Read r0945, r0949, r2122 before clearing.** Record DC voltage at trip. Note any precedent A07911 alarms.

2. **Categorize by r0949.** A trip at 340–360 VDC = marginal sag, likely transient. A trip at 250–340 VDC = significant sag, likely a coincident load or single-phase event. A trip below 250 VDC = severe — single-phase input, internal fault, or capacitor failure.

3. **Check input voltage at the drive terminals.** True-RMS meter on L1-L2, L2-L3, L3-L1. Standing voltage should be within ±10% of nameplate (360–440 VAC for a 400V drive). Phase imbalance above 3% will eventually cause F30003 even when average looks fine.

4. **Verify input torque on every lug.** Power off, verified dead, calibrated torque screwdriver to the published spec (Siemens lists it on the drive's terminal cover label). A discolored lug or melted insulation around a terminal is a smoking gun.

5. **Check branch fuses and upstream disconnect.** A single-phased input is the classic F30003 producer with very low r0949 values. Pull each fuse, check continuity. Replace as a matched set — same I²t rating, same brand.

6. **Compare fault time to operating conditions.** Was the drive accelerating? Was a second piece of equipment starting simultaneously? Walk the panel and the surrounding area. Studio's fault timestamp lined up against process trends almost always reveals the coincident event.

7. **Set up a power quality monitor.** If standing measurements and connections check out, install a Fluke 1748 or 1735 on the drive input for 24–72 hours. Trigger threshold: 10% below nominal for 100ms or more.

8. **Check Vdc_min controller configuration.** Confirm **p1240 = 1** (controllers enabled). The Vdc_min controller automatically extends decel and can adjust accel to ride through sags. If disabled, you lose ride-through capability.

9. **Verify motor and supply voltage match.** **p304 Motor rated voltage** should match the connected motor nameplate and reflect the supply voltage. A 400V drive parameterized for 230V motor operation will mis-control and can trip F30003 under load.

> **Field knowledge nugget:** On Siemens G120 drives feeding hydraulic power units in metal-fabrication shops, F30003 trips that happen specifically when a press cycle starts are almost always voltage sags from the press's main motor inrush, not a drive problem. The press motor across-the-line start pulls 6× FLA for a half second, the supply transformer sags 8-12%, and the VFD on the cooling pump or coolant pump sees a 100ms dip that pulls its bus below 360 VDC. The fix is rarely a bigger drive — it's a 5% line reactor on the press to limit inrush, or a soft-start on the press motor. I solved chronic F30003 problems at a Wisconsin stamping plant by adding soft-starts to two 75 HP press motors. Three VFDs in adjacent panels stopped tripping. Coincident-load engineering matters more than drive size.

## Parts that may need replacement

The G120 Power Modules are sold as complete units — bus capacitors and pre-charge circuits are not field-replaceable below frame FSF.

| Part | Order Number | Typical Cost | Where to Buy |
|---|---|---|---|
| PM240-2 Power Module, 7.5kW, 400V | 6SL3210-1PE22-8UL0 | $1,200–$1,600 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30003-fault), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30003-fault) |
| PM240-2 Power Module, 15kW, 400V | 6SL3210-1PE24-5UL0 | $1,900–$2,400 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30003-fault), [Wolf Automation](https://www.wolfautomation.com) |
| CU240E-2 PN Control Unit | 6SL3244-0BB12-1PA1 | $480–$640 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30003-fault), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30003-fault) |
| Line reactor, 5%, 400V, 18A | 6SL3203-0CD22-2AA0 | $290–$420 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30003-fault), [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30003-fault) |
| Line reactor, 5%, 400V, 36A | 6SL3203-0CD24-4AA0 | $420–$580 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30003-fault) |
| Isolation transformer, 480V/400V, 15kVA | (varies by mfr) | $1,800–$2,600 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30003-fault) |
| Fluke 1748 power quality logger | FLUKE-1748/BASIC | $7,400–$8,800 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30003-fault), [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |

## When to call Siemens or a controls engineer

Call senior support when: the fault history shows multiple F30003 events with r0949 values spread across a wide range (suggests intermittent power quality problem); a power quality monitor logged transients but the utility denies upstream events; you have an S120 system on a regenerative line module and the undervoltage is appearing on only one inverter; or when F30003 only happens during specific upstream coincident events you can't isolate from on-site evidence alone.

## FAQs

**Can I just clear F30003 and keep running?** You can clear it, and the drive will reset. But you've lost the diagnostic data from r0949 and r2122 if you didn't pull them first. Always read the fault history before clearing.

**Will a UPS prevent F30003?** Only a true online double-conversion UPS sized for the full drive load (which is huge for any non-trivial VFD). Drive bus capacitors *are* a small UPS — a few cycles of ride-through. What you actually need is impedance to absorb sags: a 5% line reactor on the drive input, or an isolation transformer. Most plants solve this with a line reactor for a few hundred dollars.

**My drive trips F30003 every morning at 7:15 AM. What's happening?** Almost certainly an upstream coincident load — another piece of equipment starting on the same branch or service at 7:15. Walk the floor at 7:15 with an ear out for what's energizing. Compressors, HVAC startup, furnace soft-starts, neighboring shop loads — all common.

**Difference between F30003 and F07802 (Power supply phase missing)?** F30003 is bus undervoltage, regardless of cause. F07802 specifically detects that one of the three input phases is missing for a defined period — a more specific diagnosis. They can occur together; pull both codes from the history.

**Should I disable the Vdc_min controller?** Almost never. The default **p1240 = 1** is correct. The only reason to disable would be a specific application requiring constant ramp times that cannot be extended, and in that case you should be working with a Siemens application engineer to design the system properly.

## Related guides

- [Siemens SINAMICS F30001 Fault — Power Module Overcurrent Fix](/posts/siemens-sinamics-f30001-fault)
- [Siemens SINAMICS F30002 Fault — DC Link Overvoltage Fix](/posts/siemens-sinamics-f30002-fault)
- [Siemens SINAMICS F30011 Fault — Phase Loss Fix](/posts/siemens-sinamics-f30011-fault)

## See Also

- [Siemens SIPROTEC Protective Relay Faults: Complete Guide](/posts/siemens-siprotec-relay-faults/)
- [Siemens G120C VFD Fault Code Guide — Complete Diagnostic Reference](/posts/siemens-g120c-fault-codes/)
- [Siemens SINUMERIK Alarm 25000 — Drive Fault Fix](/posts/siemens-sinumerik-alarm-25000-drive-fault/)
- [Siemens VFD F1 Fault (SINAMICS V20 Overcurrent): Causes, Codes, Fix](/posts/siemens-sinamics-v20-f1-overcurrent/)
