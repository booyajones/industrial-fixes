---
title: "ABB ACS580 Fault 3210 — DC Overvoltage Fix"
description: "ABB ACS580 fault 3210 DC Link Overvoltage means the intermediate DC bus exceeded 820 VDC on a 380–480V drive (or 1100 VDC on a 525–690V drive) and the..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: abb-acs580-fault-3210
featured: false
draft: false
tags:
  - abb
  - vfd
  - industrial-maintenance
  - drives
  - dc-link-overvoltage
---
## Quick answer

ABB ACS580 fault **3210 DC Link Overvoltage** means the intermediate DC bus exceeded 820 VDC on a 380–480V drive (or 1100 VDC on a 525–690V drive) and the firmware latched the fault. The single most common field cause I find on ACS580 installations is a too-aggressive decel time in parameter 23-13 with no brake chopper module or brake resistor installed — the load regenerates into the bus faster than the bus can absorb. A close second is utility-side overvoltage from capacitor bank switching at the distribution substation, especially on plants near substations with daily switching schedules.

## What ABB ACS580 fault 3210 means

The ACS580 monitors DC link voltage continuously through a precision divider on the control unit (CCU-25 board on the standard ACS580). The trip threshold for the 380–480V class is 820 VDC ±10 VDC, and for the 525–690V class is approximately 1100 VDC. The threshold is hardcoded in firmware and not user-adjustable. When measured DC link voltage exceeds threshold for two consecutive samples (at the firmware sampling rate of approximately 200 microseconds), fault 3210 latches and the drive coasts the motor to stop.

The ACS580 has a feature called **Overvoltage Control** — parameter **30-30** (Overvoltage Control, default On). When enabled, the drive automatically limits decel ramp by reducing braking torque demand as DC bus voltage approaches the trip threshold. If 30-30 is On and you're still tripping 3210, you have a hardware-class problem or a continuous overhauling load and you need a brake chopper plus brake resistor.

Distinguish 3210 from related faults: **3220 DC Link Undervoltage** is the low-side trip. **2310 Short Circuit** is the IGBT desat trip. **2330 Earth Leakage** is the ground-fault trip. Each lives at a different point in the power-path monitoring chain, and the alarm history will tell you which one came first if the drive logged a sequence.

## Read the fault history first

The ACS580 keeps the most recent 16 faults in a fault log accessible from the control panel or from Drive Composer Pro. **Do not press Reset until you've recorded the log** — clearing the active fault retains the log entries, but you want to read the active fault's parameter snapshot before that snapshot rolls off.

On the ACS-AP-W or ACS-AP-I assistant control panel:

1. Press **Menu**, then arrow to **Diagnostics** and press **Enter**
2. Select **Fault & event log** — the most recent fault appears at the top of the list
3. Each entry shows the fault code, descriptive name (3210 DC link overvoltage), and timestamp
4. Highlight the most recent 3210 entry and press **Enter** to open the snapshot
5. Read the snapshot parameter group **04 Warnings and faults**:
   - **04.01** — Tripping fault (the most recent fault code, will show 3210)
   - **04.02** — Active warning 1
   - **04.03** — Active warning 2
   - **04.06** — Previous fault 1
   - **04.07** — Previous fault 2
   - **04.08** — Previous fault 3 (and so on through 04.16 for older history)
6. Cross-reference with **01.11** (DC Voltage at trip), **01.07** (Motor current at trip), **01.06** (Output frequency at trip)

In Drive Composer Pro (PC software connected via USB or Ethernet), open **Diagnostics → Event Logger** for a more detailed view with operating-data captures around the trip event.

ABB documents this in the ACS580 Firmware Manual 3AXD50000016097 chapter 9 (Fault Tracing) and the Hardware Manual 3AXD50000018826 chapter 12.

**Field insight — the 3210 history trap:** parameter 01.11 (DC Voltage) is sampled at the firmware control loop rate, which on the ACS580 is approximately 5 ms. So the value captured by the fault log is the bus voltage at the *first sample after* the hardware comparator latched the trip — typically 5–20 VDC higher than the actual threshold crossing because the bus was still rising. If 01.11 reads 835 VDC at trip on a 480V drive, that's textbook regen overshoot. If 01.11 reads 900 VDC or higher, you have a sharp transient — investigate the utility, not the recipe.

## Common causes (ranked by frequency)

1. **Decel ramp 23-13 too short for load inertia** — drive decelerates faster than DC link can absorb regenerative energy; no brake chopper / brake resistor fitted
2. **Brake resistor failed or never installed** — required for ACS580 with regenerative applications; standard frames R0–R5 have a brake chopper built in, but the resistor is an external accessory
3. **Overhauling load** — gravity loads (hoists, downhill conveyors, web rewind, elevators) actively driving the motor backward
4. **Overvoltage Control 30-30 disabled** — someone turned it off attempting to enforce a precise stop time
5. **Utility transient overvoltage** — substation capacitor bank switching, lightning faults clearing, large load shedding upstream
6. **Input voltage genuinely high** — wrong transformer tap, generator running unloaded with poor voltage regulation
7. **Brake chopper failure** — internal brake chopper IGBT shorted or open, drive can't dissipate regen energy

## Step-by-step diagnosis

Before opening the cabinet: lock and tag the upstream disconnect. Wait the rated capacitor discharge time — ABB specifies a minimum of **5 minutes** for ACS580 frames R0 through R5, **10 minutes** for R6 through R9, and **15 minutes** for the larger R10 and R11 frames. Confirm zero DC bus at terminals UDC+ and UDC- with a CAT-IV meter rated 1000 VDC. Stay outside the NFPA 70E arc-flash boundary marked on the cabinet label until zero energy is confirmed and you are in the PPE specified.

1. **Read the fault log before clearing.** Capture parameters 04.01 through 04.16 and the snapshot data: 01.11 DC voltage at trip, 01.07 motor current at trip, 01.06 output frequency at trip. The DC voltage reading tells you the severity — near 825 VDC is normal regen, near 900+ VDC is transient overvoltage and a different problem.

2. **Measure input line voltage.** With drive re-energized and in proper PPE, use a true-RMS meter on input terminals U1, V1, W1 — all three line-to-line readings. Standing voltage on a 480V class drive should be within ±10% of nominal: 432 to 528 VAC. Above 510 VAC standing puts you within one normal regen event of tripping. Above 528 VAC standing means the bus rectifies to over 745 VDC at no load — drop one tap on the upstream transformer.

3. **Confirm parameter 30-30 Overvoltage Control is On.** Read **30-30 Overvoltage control**:
   - 0 = Disable (drive trips immediately on bus overvoltage)
   - 1 = Enable (default — drive auto-extends decel)
   Set 30-30 = 1 unless you have a specific commissioning reason to disable. Also check **30-31 Voltage limit** which sets the active limit point for OVC (default value matches the trip threshold minus margin).

4. **Inspect brake resistor and chopper.** ACS580 frames R0–R5 have an integrated brake chopper. Larger frames may use an external NBRA-6XX brake unit. With drive de-energized and bus confirmed at zero, ohm-test the brake resistor from terminals R+ and R- (or UDC+ to R- if your terminal labeling is the older variant). Expected resistance is on the brake resistor nameplate — for an ACS580-01-12A6-4 with the JBR-08 brake resistor it's 22 ohms ±5%. An open reading means a blown resistor or open thermal switch.

5. **Test the brake chopper.** With drive powered and motor coupled to inertia load, run normal acceleration to full speed and issue stop. Monitor **01.11 DC Voltage** in real time via Drive Composer or the panel monitor screen. Threshold for chopper firing is approximately 780 VDC on a 480V drive. If bus rises above 800 VDC and brake resistor stays cold, the chopper IGBT has failed. On standard ACS580 frames this means drive replacement.

6. **Verify parameter 43-06 Brake chopper enable.** Should be:
   - 0 = Disabled (no brake chopper / brake function)
   - 1 = Enabled with overload protection (use this when JBR or NBRA brake resistor is installed)
   - 2 = Enabled without overload protection (rare, custom installations)
   If brake resistor is fitted and 43-06 = 0, the chopper isn't engaged. Fix that.

7. **Lengthen decel time 23-13.** If bus voltage at trip was at threshold and no brake circuit is fitted, extend **23-13 Acceleration time 1** and **23-14 Deceleration time 1**. Rule of thumb: decel = 1.5× accel for typical loads, 2× for high-inertia. For ACS580 in pump or fan applications, 30–60 second decel is normal and safe.

8. **Set up power quality monitoring if standing voltage and recipe check out.** A Fluke 1748 or 1735 logger on the drive input for 7 days will capture utility transients. Trigger threshold: 10% above nominal for 100 ms or more. Capacitor bank switching at the substation is the most common cause of intermittent 3210 with no apparent operational trigger.

9. **Check common DC bus configurations.** If the ACS580 is on a shared DC bus with multiple inverters, verify the brake chopper(s) are sized for the *combined worst-case regen* of all drives on the bus. A common DC bus with a single brake chopper sized for one drive will trip 3210 when multiple drives regenerate simultaneously.

## Parts that may need replacement

| Part | Catalog Number | Typical Cost | Where to Buy |
|---|---|---|---|
| ACS580-01, 480V, 5.5kW (7.5HP) | ACS580-01-12A6-4 | $1,850–$2,200 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=abb-acs580-fault-3210), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=abb-acs580-fault-3210) |
| ACS580-01, 480V, 11kW (15HP) | ACS580-01-026A-4 | $2,850–$3,400 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=abb-acs580-fault-3210), [Wolf Automation](https://www.wolfautomation.com) |
| ACS580-01, 480V, 22kW (30HP) | ACS580-01-046A-4 | $4,200–$5,000 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=abb-acs580-fault-3210), [Wolf Automation](https://www.wolfautomation.com) |
| ACS580-01, 480V, 45kW (60HP) | ACS580-01-088A-4 | $6,500–$7,800 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=abb-acs580-fault-3210), [Wolf Automation](https://www.wolfautomation.com) |
| ABB JBR-08 brake resistor 22Ω 1200W | 68878597 | $385–$525 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=abb-acs580-fault-3210), [Wolf Automation](https://www.wolfautomation.com) |
| ABB JBR-12 brake resistor 16Ω 2400W | 68878598 | $625–$795 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=abb-acs580-fault-3210) |
| External NBRA brake unit 75kW | NBRA-65C | $1,450–$1,750 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=abb-acs580-fault-3210), [Wolf Automation](https://www.wolfautomation.com) |
| ACS-AP-W assistant control panel | 3AUA0000094568 | $385–$485 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=abb-acs580-fault-3210) |
| Fluke 1748 power quality logger | FLUKE-1748/BASIC | $7,400–$8,800 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=abb-acs580-fault-3210), [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| Fluke 87V industrial multimeter | FLUKE-87-5 | $480–$580 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=abb-acs580-fault-3210) |

The ACS580's DC link capacitors and brake chopper IGBT are not field-replaceable on frames R0–R5. A confirmed chopper failure requires drive replacement. ABB's standard warranty is 18 months from delivery / 12 months from commissioning, whichever is shorter — check the production code on the drive nameplate before ordering.

## When to call a controls engineer

Bring in senior support when: 01.11 readings at trip consistently exceed 900 VDC on a 480V drive (transient events outside design envelope); you're on a common DC bus with three or more inverters and 3210 migrates between drives; the application has continuous regen (hoist, crane, web tension) and you need to size for active-front-end (ACS880-04 with IGBT supply unit) rather than dynamic braking; or 3210 trips only at specific speed bands suggesting mechanical resonance is feeding kinetic energy back to the motor.

## FAQs

**Can I disable 30-30 Overvoltage Control to get a faster decel?** Don't. Without OVC the drive will trip 3210 on every aggressive decel. The right way to get fast decel is to install a JBR-series brake resistor and enable 43-06 = 1 brake chopper with overload protection.

**Will an input choke help with 3210?** A 3% line reactor (such as ABB's CHK-A1 series) can dampen transient overvoltage from capacitor switching upstream. It won't help with regen-driven 3210 — that needs a brake resistor. ACS580 drives in standard configurations include a DC link choke as standard, but adding an AC line reactor on top is a common upgrade in noisy power environments.

**My ACS580 trips 3210 only when an upstream load shuts off. Why?** That load was dragging line voltage low under its current draw. When it disconnects, line voltage rebounds high for several cycles — your drive sees it as overvoltage. Add a line reactor or address the upstream source.

**Difference between 3210 and 3220?** Fault 3210 is the high-side overvoltage trip (bus too high). Fault 3220 is the low-side undervoltage trip (bus too low). Different problems, different fixes — but both have their own snapshot data in 04.01 and the parameter group 01.

**Should the brake resistor have a thermal switch wired in?** Yes. Every ABB JBR-series brake resistor includes a normally-closed thermal switch rated 130°C. Wire it to a digital input configured as External Fault (parameter 31-01 = External event 1 source) or in series with the safety chain. A resistor that overheats and isn't disabled will eventually fire and ignite the cabinet.

## Related guides

- [ABB ACS580 Fault 3220 — DC Undervoltage Fix](/abb-acs580-fault-3220/)
- [ABB ACS580 Fault 2310 — Overcurrent Fix](/abb-acs580-2310-fault/)
- [Yaskawa GA800 oV Fault — DC Overvoltage Fix](/yaskawa-ga800-error-ov/)
- [Danfoss FC-302 Alarm 13 — DC Link Overvoltage Fix](/danfoss-fc302-alarm-13/)
- [Allen-Bradley PowerFlex F005 Fault — Overvoltage Fix](/allen-bradley-powerflex-f005-fault/)
