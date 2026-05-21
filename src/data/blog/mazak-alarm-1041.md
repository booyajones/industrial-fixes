---
title: "Mazak Matrix Alarm 1041 — Battery Voltage Drop / Encoder Battery Fix"
description: "Mazak Matrix Alarm 1041 (Battery Voltage Drop) is a warning that the absolute encoder backup battery has dropped below the low-voltage threshold — about..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "James Rutherford"
slug: mazak-alarm-1041
featured: false
draft: false
tags:
  - mazak
  - cnc
  - industrial-maintenance
---
## Quick answer

Mazak Matrix Alarm 1041 (Battery Voltage Drop) is a warning that the absolute encoder backup battery has dropped below the low-voltage threshold — about 3.0V loaded on the standard MR-BAT6V1 pack — but the absolute position is still held. This is a do-it-now-or-pay-later alarm: replace the battery within a week of seeing 1041 or you will eventually hit Alarm 1042 (Battery Alarm), lose absolute position on every affected axis, and spend half a shift re-zeroing everything by the maintenance manual procedure.

## What Mazak Matrix Alarm 1041 means

Mazak Matrix and Matrix Nexus controls (and the same architecture forward through Smooth G/X/Ai) use absolute encoders on every servo axis. The encoder needs continuous low-power memory backup whenever the main control is powered off, so a 3.6V lithium pack at the servo drive (mounted in a clip on the front of each MDS-D or MDS-DH drive in the cabinet) supplies backup current to its associated encoder. When the control reads battery voltage below the warning threshold (typically about 3.0V loaded, 3.2V open-circuit) during the power-on self-test, it posts Alarm 1041 as a warning. The machine can still run — absolute position is not yet lost — but the clock is ticking.

The hard-fail alarm is **1042 (Battery Alarm)**, which fires when voltage drops far enough that the encoder can no longer hold its absolute count between power cycles. Once 1042 lands, the affected axis loses absolute position and you must perform a zero-return procedure per the maintenance manual — for a 5-axis Integrex, that's potentially five axes including the B-axis tilt and C-axis turret, each with its own setup sequence, and on a turn-mill you may also need to re-establish spindle orientation.

The 1041 warning normally appears when the battery has 1–3 months of useful life remaining at typical machine duty cycles. The actual remaining life depends on how often the machine is powered off (more power-off time = more battery drain since the drive's internal capacitor isn't holding the encoder). A machine that runs 24/7 will get more battery life than one that's powered off every weekend.

On older M32 and M-Plus controls, the equivalent alarm is **"Battery"** (no number, or "BATT LOW" depending on PLC version). The threshold and architecture are similar but the battery pack form factor is different — M32 uses an MR-BAT cradle, not MR-BAT6V1.

## Read the alarm history first

This one is short because 1041 is a warning, not a latched fault. But pulling history is still worth the 60 seconds before you change anything.

On Matrix and Matrix Nexus:

1. Press **Alarm** on the operator panel, then **Alarm History**
2. Find the 1041 entry — note the date/time of first occurrence
3. Page back to see if 1041 has been bouncing in and out (warns at power-on, clears as drive's holdup cap charges, warns again next morning). A bouncing 1041 means the battery is right at threshold; replace this week
4. Check for any 1042 entries — if 1042 has already appeared even once, absolute position has been lost and you need to plan re-zeroing now, not later

On Smooth:

1. **Maintenance → History → Alarm**, filter the type column for Warning
2. The 1041 row shows axis index and date/time
3. **Maintenance → Servo → Battery Voltage** (on later Smooth firmware) shows live voltage per axis for cross-check

**Field insight — the one nugget that traps everyone on Mazak Alarm 1041:** the battery serves the *encoder*, not the control's parameter memory. On Mazak the parameter memory is held by a separate CR2032-style coin cell on the NC card (typically a Maxell CR2032 or Renata CR2032, depending on Matrix board revision). Operators see "battery alarm" and think they need to swap the coin cell on the NC card. That coin cell has its own alarm (different number — typically 1043 or "MEMORY BATTERY" depending on firmware), and it triggers when *NC parameter memory* is at risk. 1041 is exclusively the encoder backup pack at the drive. If you swap the wrong battery, 1041 doesn't clear and you've wasted a shutdown. Confirm by reading the alarm detail: 1041 names the axis (X, Y, Z, etc.), while NC memory battery alarms do not name an axis.

## Common causes (ranked by frequency)

1. **Battery has reached end-of-shelf-life** — MR-BAT6V1 packs are typically rated 2 years in service; many shops let them run 3–5 years and only discover the problem at 1041
2. **Battery installed but not properly seated in the clip** — partial contact reads as low voltage; reseating fixes it
3. **Machine sat powered-off for an extended period** (e.g., shop closed for a multi-week shutdown) — battery drained faster than during run time
4. **Battery cable inside the drive disconnected during a recent service** — service tech pulled the drive, didn't reconnect the battery harness on reinstall
5. **Defective battery pack from new** — rare but does happen; aftermarket Chinese batteries especially
6. **Drive internal hold-up capacitor failed** — drive can no longer maintain encoder backup briefly during the millisecond gap before battery takes over; symptoms similar but persists after battery swap

## Step-by-step diagnosis

Standard CNC safety applies. Lock and tag the main disconnect, wait 5 minutes for the servo drive bus capacitors to discharge, verify zero energy at the drive bus terminals with a CAT-III meter. **Critical: do not power off the machine until you have the replacement battery in hand and confirmed it is the correct part number.** If you cut power with the existing battery already below threshold, you may lose absolute position before you can reconnect the new battery.

1. **Confirm which battery is alarming.** The 1041 detail names the axis (X, Y, Z, A, B, C). Each axis has its own drive in the cabinet, and each drive has its own battery clip on its front face. Trace the cabinet wiring diagram (taped inside the cabinet door on most Mazak machines) to confirm drive location.

2. **Buy the correct battery before you start.** MR-BAT6V1 packs are the Mitsubishi/Mazak-spec part. Galco and Wolf Automation stock genuine units. Amazon and eBay sell both genuine and Chinese clones — the clones are typically a third the price and last about a quarter the time. For production machines, buy genuine.

3. **Plan a hot-swap if possible.** Mazak's MDS-D and MDS-DH drives support hot-swap of the encoder battery — the drive's internal hold-up capacitor maintains encoder backup for typically 30–60 seconds during a swap. **Verify your drive's hold-up time in its spec sheet before relying on this.** Older MDS-A/MDS-B drives on M32/M-Plus controls do NOT support hot-swap reliably.

4. **For hot-swap procedure:** leave the machine powered on. Open the electrical cabinet door (interlock may need bypassed via key switch per maintenance manual — Mazak's procedure is specific). The battery clip is on the front face of the drive. Disconnect the old battery's 2-pin connector, immediately plug in the new battery (have it ready in your hand), then transfer the pack into the clip. Verify the new battery's connector is seated fully. The 1041 alarm should clear within 30 seconds on the next refresh cycle.

5. **For powered-off replacement (if hot-swap is not supported):** finish any running program, retract tooling to a safe position, power down at the main disconnect. Replace battery. Power up. **The first power-up after battery replacement may show 1041 momentarily while the drive measures the new battery voltage — this is normal and clears within 30 seconds.** If 1041 does not clear, the new battery is bad, the connector is not seated, or the drive's hold-up cap has failed.

6. **If 1041 persists with a new known-good battery,** measure battery voltage at the drive's battery connector with a meter (red on positive, black on negative — orientation is marked on the drive face). You should see 3.4–3.6V open circuit. If you see less than 3.0V on a brand-new battery, the drive is loading it improperly — the drive's hold-up cap has failed or there's a short in the encoder backup circuit.

7. **Verify no 1042 has been logged.** If 1042 ever fired, absolute position is lost on that axis and you must re-zero. The reference-return procedure is in the maintenance manual — for most Mazak axes it's Mode Select → ZRN → Cycle Start, but on machines with linear scales or hard stops, follow the documented procedure exactly. Do not improvise.

8. **Document the replacement date.** Stick a label on the battery or the inside of the cabinet door: "Battery installed [date], replace by [date+2 years]." A 2-year replacement interval (regardless of voltage at that point) is industry practice for Mazak; it prevents the 1041 surprise entirely.

9. **Update your PM schedule.** If this machine wasn't on a 2-year battery rotation, add it. Cost of a planned battery swap: $50 in parts, 15 minutes of labor. Cost of losing absolute position on a 5-axis machine in production: half a shift of re-zeroing plus first-article re-inspection.

## Parts that may need replacement

| Part | Part Number (form) | Typical Cost | Where to Buy |
|---|---|---|---|
| MR-BAT6V1 encoder battery pack | Mitsubishi MR-BAT6V1SET | $42–$78 | [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO), [Wolf Automation](https://www.wolfautomation.com?aff=PLACEHOLDER-WOLF), [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| MR-BAT6V1SET aftermarket | various Asian clones | $14–$28 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20), eBay (not recommended for production) |
| NC memory backup coin cell (different alarm — 1043) | Maxell CR2032 or Renata CR2032 | $4–$10 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| Battery clip / holder (if damaged) | Mazak drive PN per maintenance manual | $35–$90 | [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO), Mazak direct |
| Servo drive (MDS-DH) if hold-up cap failed | MDS-DH-V2-xx (size varies) | $4,800–$7,800 used | [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO), eBay (used CNC dealer) |
| CAT-III multimeter for battery voltage | Fluke 87V | $480–$560 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20), [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO) |
| Cabinet interlock defeat key (if your shop uses one) | per maintenance manual | $25–$60 | Mazak direct, [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO) |
| Replacement battery harness, drive-to-clip | Mazak PN per parts list | $70–$140 | Mazak direct, eBay |

## When to call a CNC service engineer

Call when: 1041 persists with a verified-good new battery (drive hold-up cap or backup circuit is the actual problem, drive may need replacement); you've already crossed into 1042 territory and need to re-zero axes whose reference-return procedure is not in your shop's documentation (especially Integrex B-axis or turn-mill C-axis indexing); the machine has been powered off for months and you're starting it cold — Mazak's commissioning procedure for long-stored machines includes battery checks and parameter verification you don't want to skip; or you need to hot-swap on an MDS-A/MDS-B drive and you're not sure the drive supports it.

## FAQs

**Can I run the machine with 1041 active?** Yes — 1041 is a warning, not a fault. Production can continue. But every hour you delay replacement is an hour closer to 1042 and an unplanned re-zero.

**Can I use a generic 3.6V lithium battery?** Not recommended. The MR-BAT6V1 pack is voltage-regulated and current-limited to spec by the drive's backup circuit. Generic packs may have different internal resistance, no thermal fuse, or wrong connector. The cost difference is $30 — not worth the risk on a production machine.

**Will 1041 lose my parameters?** No. 1041 is the encoder absolute backup, which holds position only. NC parameters are held by a separate CR2032 coin cell on the NC board, with its own alarm. Confusing the two has cost more than one tech an unnecessary parameter restore.

**Reference Mazak Maintenance Manual section?** "Maintenance / Electrical Components / Battery Replacement" in the Matrix and Smooth maintenance manuals. Includes the hot-swap procedure, the parameter for battery voltage threshold (do not change without Mazak guidance), and the reference-return procedure for each axis if you do lose position.

**Should I keep a spare battery in stock?** Yes. Buy two with every new machine: one for the 2-year replacement, one as the spare for the next emergency. Lithium primaries shelf-store for years in original packaging. At $50 each, the inventory cost is trivial against the downtime cost.

## Related guides

- [Mazak Alarm 218 — Spindle Motor Overheat Fix](/posts/mazak-alarm-218/)
- [Mazak Alarm 415 — Position Detector Error Fix](/posts/mazak-alarm-415/)
- [Mazak Servo Parameter Error Fix](/posts/mazak-servo-parameter-error/)
- [Fanuc Alarm 300 — APC Battery Voltage Low Fix](/posts/fanuc-alarm-300/)
- [Fanuc Alarm 414 — Servo Digital Alarm Fix](/posts/fanuc-alarm-414/)
- [Haas Alarm 114 — Servo Error Too Large Fix](/posts/haas-alarm-114/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Best multimeter for HVAC techs (2026)](/posts/best-multimeter-for-hvac/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Best clamp meter (2026)](/posts/best-clamp-meter-for-electricians/)

