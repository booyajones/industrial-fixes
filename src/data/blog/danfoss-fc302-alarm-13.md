---
title: "Danfoss FC-302 Alarm 13 — DC Link Overvoltage Fix"
description: "Danfoss FC-302 Alarm 13 (Over Voltage) means the DC link voltage exceeded the trip threshold — approximately 820 VDC on a 380–500V drive (parameter 14-23..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: danfoss-fc302-alarm-13
featured: false
draft: false
tags:
  - danfoss
  - vfd
  - industrial-maintenance
  - drives
  - dc-link-overvoltage
---
## Quick answer

Danfoss FC-302 Alarm 13 (Over Voltage) means the DC link voltage exceeded the trip threshold — approximately 820 VDC on a 380–500V drive (parameter 14-23 trip level reported in 16-30 DC Link Voltage). The single most common field cause is decel ramp time too short for the load inertia with no brake resistor installed — the motor regenerates into the DC link faster than the link can absorb. A close second is genuine line overvoltage from a transformer tap set wrong or capacitor bank switching at the utility distribution.

## What Danfoss FC-302 Alarm 13 means

The FC-302 measures DC link voltage at the bus capacitor bank via a precision divider feeding the control card ADC. It samples continuously at the PWM rate. Alarm 13 latches when the measured value exceeds approximately 820 VDC on a 380–500V class drive (frame size dependent — the 525–690V class trips around 1090 VDC). The threshold is not user-adjustable. The trip is reported via display, relay output, and the alarm log parameter 15-30.

Three things cause Alarm 13: regenerative energy from the motor (the dominant cause), input line overvoltage (substation issues, wrong transformer tap), or a hardware-class problem in the drive itself (failed brake chopper, leaky bus capacitor producing false high reading). Read parameter 16-30 (DC Link Voltage) and the alarm log value in 15-31 to figure out which one — a number near 825 VDC is a textbook regen overshoot, a number near 900+ VDC is a hardware-class transient and something serious happened upstream.

The FC-302 has a built-in **Overvoltage Control** function — parameter 2-17 — that automatically extends the deceleration time to keep the DC link below the trip threshold. When 2-17 = [2] Enabled, the drive will not trip Alarm 13 on a too-aggressive decel; it will simply slow the ramp. If Alarm 13 is still tripping with 2-17 enabled, you have a hardware-class problem or a continuous overhauling load that needs a brake resistor.

## Read the fault history first

Read the alarm log before pressing Reset on the LCP. The FC-302 keeps the most recent 10 alarms in parameter group 15-3X. On the LCP 102 graphical or LCP 101 numerical display:

1. Press **[Main Menu]** to enter the parameter tree
2. Navigate to **15 Drive Information → 15-3 Alarm Log**
3. Read in order:
   - **15-30** — Alarm Log: Error Code (index 0 = most recent, index 9 = oldest)
   - **15-31** — Alarm Log: Value — for Alarm 13 this is the DC link voltage at trip
   - **15-32** — Alarm Log: Time (operating-hour timestamp)
   - **15-33** — Alarm Log: Date and Time (real-time clock if installed)
4. Read the operating snapshot from the run-up to trip:
   - **16-30** — DC Link Voltage (the real-time bus voltage, useful to monitor during the next attempted decel)
   - **16-14** — Motor Current
   - **16-13** — Frequency
   - **16-11** — Power [hp]

Danfoss documents this in the FC-300 Programming Guide MG33MJ22 section 5.3 (parameter 15-3X) and Operating Instructions MG33AK22 chapter 7 (Troubleshooting and Alarm List).

**Field insight — the Alarm 13 history trap:** 15-31 logs the DC link voltage at the *exact sample* the alarm latched. Because the FC-302 ramps detection on a few-sample debounce, the recorded value is typically 5–15 VDC higher than the trip threshold itself. So 15-31 reading 832 VDC is normal regen overshoot. 15-31 reading 880 VDC or higher means a sharp transient hit the bus — either utility (look for capacitor switching) or a regen pulse from a paralleled drive on common DC. Don't chase the recipe in that case, chase the transient source.

## Common causes (ranked by frequency)

1. **Decel ramp 3-42 too short for load inertia** — drive decelerates faster than the bus can absorb regen, no brake resistor or undersized brake resistor
2. **Brake resistor failed or never installed** — open-circuit brake resistor, blown brake chopper IGBT, or thermal-trip open
3. **Overhauling load** — gravity load (hoist, elevator, downhill conveyor) actively driving the motor backward
4. **Overvoltage Control parameter 2-17 disabled** — someone turned it off trying to enforce a deterministic decel time
5. **Utility line overvoltage** — long-term high voltage from wrong transformer tap, or transient overvoltage from capacitor bank switching upstream
6. **Common-bus configuration without proper sizing** — paralleled FC-302s sharing DC bus, one drive's regen pushes others into trip
7. **Brake function parameter 2-10 set wrong** — should be [1] Resistor brake when brake resistor is installed, but set to [0] Off

## Step-by-step diagnosis

Lock and tag the input contactor. Wait the FC-302 capacitor discharge time — Danfoss specifies a minimum of **4 minutes** for A1–A3 frames, **15 minutes** for B and C frames, **20 minutes** for D, E, and F frames. Confirm zero DC link at terminals 88 (-) and 89 (+) and across brake terminals 81 (R-) and 82 (R+) if brake is installed, using a CAT-IV meter rated 1000 VDC. Respect the NFPA 70E arc-flash boundary marked on the cabinet and wear the PPE specified.

1. **Read the alarm log before clearing.** Capture 15-30 through 15-33 and note 15-31 (DC link voltage at trip). A reading near 825 VDC is normal regen overshoot. A reading near 880 VDC or higher is transient — different cause, different fix.

2. **Measure input line voltage.** Re-energize the drive (after dead-state confirmation and proper PPE). Use a true-RMS meter on input terminals L1, L2, L3 — all three line-to-line readings. Standing voltage should be within ±10% of nameplate: 342 to 528 VAC for a 380–500V drive. Above 528 VAC standing means the drive sees rectified DC over 745 VDC at no load — one good regen pulse and you trip. Check the upstream transformer tap; drop one tap if standing voltage is consistently high.

3. **Verify Overvoltage Control parameter 2-17 is enabled.** Read parameter **2-17 Over-voltage Control**:
   - [0] Disabled
   - [1] Enabled (not at stop)
   - [2] Enabled (default — works during all decel)
   Set 2-17 = [2] unless you have a specific reason to disable. With 2-17 enabled and no brake resistor, the drive will extend decel time to ride the bus rise.

4. **Check the brake resistor circuit if installed.** With drive de-energized and bus confirmed at zero, ohm-test the brake resistor from drive terminals 81 (R-) to 82 (R+). The expected resistance is published on the brake resistor nameplate — for a typical FC-302 11 kW with a 130B2230 brake resistor it's 22 ohms ±5%. An open reading is a blown resistor or open thermal switch. Inspect the resistor housing for discoloration.

5. **Test the brake chopper.** With drive powered and a motor coupled to a flywheel or other inertia, run a normal forward acceleration to full speed, then issue stop. Monitor **16-30** (DC Link Voltage) on the LCP display. If the bus climbs above 800 VDC and stays there during decel while the resistor stays cold, the brake chopper isn't firing. The chopper turn-on threshold is approximately 770 VDC on a 380–500V FC-302. Brake chopper failure usually requires drive replacement.

6. **Verify parameter 2-10 Brake Function.** Should be set to:
   - [0] Off — no brake circuit (drive decel relies on Overvoltage Control / coast)
   - [1] Resistor brake — external brake resistor connected to 81/82 terminals
   - [2] AC brake — DC injection braking (no external resistor needed, limited capability)
   - [3] Load Sharing — drive is on common DC bus
   If you have a brake resistor installed and 2-10 = [0], the resistor isn't being used. Fix that first.

7. **Lengthen ramp-down time 3-42.** If the bus voltage at trip was right at threshold and no brake resistor is fitted, extend parameter **3-42 Ramp 1 Ramp-down Time**. Rule of thumb: ramp-down should be at least 1.5× ramp-up (3-41) for typical loads, 2× for high-inertia loads. For a centrifuge or large fan, 60–120 seconds of decel is normal.

8. **Capture utility transients if standing voltage and recipe check out.** Install a Fluke 1748 or 1735 on the drive input for 24–72 hours. Trigger threshold: 10% above nominal for 100 ms or more. Capacitor switching at the utility substation is a common cause of intermittent Alarm 13 with no apparent operational trigger.

9. **For common DC bus configurations:** verify each drive's brake resistor is sized for the *worst-case simultaneous regen* of all drives on the bus, not just the single drive that owns the resistor. Common-bus sizing is a design problem I see at least twice a year in retrofit installations.

## Parts that may need replacement

| Part | Catalog Number | Typical Cost | Where to Buy |
|---|---|---|---|
| FC-302, 480V, 5.5kW (7.5HP) | 131F0036 | $1,950–$2,350 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=danfoss-fc302-alarm-13), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=danfoss-fc302-alarm-13) |
| FC-302, 480V, 15kW (20HP) | 131F0061 | $3,200–$3,800 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=danfoss-fc302-alarm-13), [Wolf Automation](https://www.wolfautomation.com) |
| FC-302, 480V, 30kW (40HP) | 131F0076 | $4,800–$5,800 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=danfoss-fc302-alarm-13), [Wolf Automation](https://www.wolfautomation.com) |
| Brake resistor, 22 ohm, 1200W for 11 kW drive | 175U3007 (Danfoss MCE 101) | $385–$520 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=danfoss-fc302-alarm-13), [Wolf Automation](https://www.wolfautomation.com) |
| Brake resistor, 16 ohm, 2400W for 22 kW drive | 175U3019 | $625–$795 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=danfoss-fc302-alarm-13) |
| External brake module, large frames | 130B1287 (MCE 152) | $1,450–$1,750 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=danfoss-fc302-alarm-13), [Wolf Automation](https://www.wolfautomation.com) |
| LCP 102 graphical display | 130B1107 | $385–$485 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=danfoss-fc302-alarm-13), [Wolf Automation](https://www.wolfautomation.com) |
| Fluke 1748 power quality logger | FLUKE-1748/BASIC | $7,400–$8,800 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=danfoss-fc302-alarm-13), [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| Fluke 87V industrial multimeter | FLUKE-87-5 | $480–$580 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=danfoss-fc302-alarm-13) |

The FC-302 brake chopper IGBT and DC link capacitors are not field-serviceable. A drive with a confirmed brake-chopper or capacitor failure is replaced as a complete unit. Verify warranty status via the production label before ordering.

## When to call a controls engineer

Bring in senior support when: 15-31 (DC voltage at trip) reads consistently above 880 VDC suggesting transient events outside the drive's design envelope; you're on a common DC bus with three or more inverters and the Alarm 13 migrates between drives unpredictably; the application is a hoist, crane, or web tension where regenerative energy is normal continuous operation and you should consider an active-front-end FC-302 (regen-capable inverter); or when Alarm 13 only triggers at specific speed bands suggesting mechanical resonance is feeding kinetic energy into the motor at sub-synchronous frequencies.

## FAQs

**Can I just disable 2-17 (Overvoltage Control) to get a faster decel?** Don't. Without OVC, the drive will trip Alarm 13 on every decel that isn't slow enough to coast. The proper way to get fast decel is to install a brake resistor sized for the application and set 2-10 = [1] Resistor Brake.

**Will an input reactor help with Alarm 13?** A 3% or 5% input reactor can dampen transient overvoltage from capacitor bank switching upstream, but it won't help with regen-driven Alarm 13. If the trip is during decel of a high-inertia load, a brake resistor is the answer.

**My drive trips Alarm 13 only when a specific upstream load shuts down. Why?** That load was holding the line voltage low under its load current. When it shuts down, line voltage rebounds high for several cycles (and possibly a transient spike from contactor opening) — your drive sees that as an overvoltage event. Add a line reactor or address the source.

**Difference between Alarm 13 and Warning 8?** Warning 8 (DC Link Under-voltage Warning) and the matching Alarm 7 are the *low-side* alarms. Alarm 13 is the high-side overvoltage trip. The FC-302 also has Warning 9 (Inverter Overload) and Warning 12 (Torque Warning) which can shadow the actual fault — read the full log in 15-30 across all indices.

**Should the brake resistor have a thermal switch wired back to the drive?** Yes. Every Danfoss-branded brake resistor (MCE 101 series and similar) ships with a thermal contact. Wire it in series with an external safety circuit or to a digital input configured as External Interlock (parameter 5-1X = [27] Safe Stop Inverse, or [22] Coast Inverse). A resistor that overheats and isn't disabled will eventually ignite the cabinet.

## Related guides

- [Danfoss FC-302 Alarm 12 — Overcurrent Fix](/danfoss-fc302-alarm-12/)
- [Yaskawa GA800 oV Fault — DC Overvoltage Fix](/yaskawa-ga800-error-ov/)
- [ABB ACS580 Fault 3210 — DC Overvoltage Fix](/abb-acs580-fault-3210/)
- [Allen-Bradley PowerFlex F005 Fault — Overvoltage Fix](/allen-bradley-powerflex-f005-fault/)
- [Allen-Bradley PowerFlex F004 Fault — Undervoltage Fix](/allen-bradley-powerflex-f004-fault/)
