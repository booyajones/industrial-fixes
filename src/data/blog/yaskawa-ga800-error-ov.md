---
title: "Yaskawa GA800 oV Fault — DC Overvoltage Fix"
description: "Yaskawa GA800 oV (DC Overvoltage) means the internal DC bus climbed above approximately 820 VDC on a 480V-class drive (or 410 VDC on a 240V-class) while the..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: yaskawa-ga800-error-ov
featured: false
draft: false
tags:
  - yaskawa
  - vfd
  - industrial-maintenance
  - drives
  - dc-overvoltage
---
## Quick answer

Yaskawa GA800 oV (DC Overvoltage) means the internal DC bus climbed above approximately 820 VDC on a 480V-class drive (or 410 VDC on a 240V-class) while the drive was running. By far the most common cause I see is a too-fast decel time C1-02 on an overhauling or high-inertia load — the motor regenerates back into the bus faster than the bus can dissipate, and no dynamic braking resistor is installed or the resistor is sized too small. A close second: utility overvoltage events from capacitor switching on the upstream distribution, especially on plants near substations.

## What Yaskawa GA800 oV means

The GA800 monitors the DC bus continuously between the bus capacitor bank and the IGBT inverter section. Trip threshold is fixed in firmware: 820 VDC ±10 VDC for a 480V-class drive (CIMR-GA4A models), 410 VDC for a 240V-class (CIMR-GA2A), 1040 VDC for a 690V-class (CIMR-GA5A). The drive samples the bus at the PWM rate and trips oV when the measurement exceeds threshold for more than a couple of samples in a row — it's not a true instantaneous hardware latch like oC, but it's faster than the firmware can ramp output to compensate.

There are three mechanisms that drive the bus up: rectified line voltage too high (input AC over 528 VAC line-to-line on a 480V drive), regenerative energy from the motor (an overhauling load or aggressive decel), or external charge injection (shared bus tie from another drive). The drive itself reports them all as oV in U2-01. You have to read U2-08 (DC bus voltage at trip) and U2-03 (reference frequency at trip) to figure out which one.

The GA800 includes the Stall Prevention During Deceleration function — parameter L3-04 — which automatically extends decel time when bus voltage approaches the oV threshold. If you set L3-04 = 1 (Enabled), the drive will *not* trip oV during normal decel, it will simply slow down the ramp. If you're still tripping oV with L3-04 enabled, you have a hardware-class problem, not a recipe problem.

## Read the fault history first

Read the history before pressing Reset. On a GA800 with the JVOP-KPLCC04 or JVOP-KPLCA04 keypad:

1. Press **ESC** to the main menu
2. Navigate to **U Monitor → U2** for the most-recent fault snapshot
3. Read these parameters in order:
   - **U2-01** — fault code (should show oV)
   - **U2-02** — previous fault code (look for a pattern — oV preceded by Uv1 suggests bus regulation issue)
   - **U2-03** — reference frequency at trip
   - **U2-04** — output frequency at trip
   - **U2-05** — output current at trip
   - **U2-07** — output voltage at trip
   - **U2-08** — DC bus voltage at trip — this is the critical reading for oV
   - **U2-09** — input terminal status word
4. Then **U3-01** through **U3-10** for the rolling fault log of the last ten events
5. Cross-reference with **U3-11** through **U3-20** for the cumulative operating hours at each fault — clusters of oV at similar hour-marks suggest a recurring shift-related cause (a specific operator, a specific recipe, a specific batch)

The technical manual TOEPC71061800F section 6.2.3 walks through the oV-specific monitor parameters.

**Field insight — the oV history trap:** the GA800 logs U2-08 (DC bus voltage at trip) at the *exact sample* the trip latched, which is typically 5–15 VDC *higher* than the trip threshold because the bus was still rising at trip detection. So if U2-08 reads 845 VDC, the trip was textbook. If U2-08 reads 920 VDC or higher on a 480V drive, you have a serious upstream event (capacitor bank switching transient, lightning surge through the line reactor, or a regen pulse from a paralleled drive on a common bus tie) — investigate beyond just the recipe.

## Common causes (ranked by frequency)

1. **Decel time C1-02 too short for the load inertia** — drive decelerates the motor faster than the bus can absorb regenerative energy; no dynamic braking resistor in circuit, or resistor under-sized
2. **Utility overvoltage / capacitor bank switching** — distribution substation switches a power factor cap bank, line voltage spikes to 540+ VAC for several cycles
3. **Overhauling load** — a gravity load (hoist, conveyor downhill, web rewinder) actively drives the motor backward, pumping current into the bus
4. **Dynamic braking resistor failure** — DBR open-circuit, dynamic braking IGBT (the chopper) failed, or DBR thermal switch tripped open
5. **Stall Prevention disabled** — parameter L3-04 set to 0 (Disabled) by someone trying to force precise stop timing
6. **Input voltage genuinely too high** — long-term overvoltage from a transformer tap set wrong, or a generator running unloaded
7. **Bus tie or common DC bus** — paralleled drives sharing a bus, one drive's regen pushes another into oV

## Step-by-step diagnosis

Lock and tag the upstream disconnect. Wait the GA800 capacitor discharge time — **5 minutes** for frames smaller than 4030, **10 minutes** for 4030 and above. Verify zero DC bus at terminals B1/+ and ⊖ with a CAT-IV meter. Stay outside the NFPA 70E arc-flash boundary indicated on the cabinet label until you have proved zero energy and you are wearing the PPE specified.

1. **Read the history before clearing.** Capture U2-01 through U2-09 and U3-01 through U3-20. U2-08 (DC bus at trip) tells you the magnitude of the event. A reading near 830 VDC is a normal regen overshoot. A reading near 900 VDC or higher is a hardware-class problem.

2. **Measure incoming line voltage at the drive input terminals R/L1, S/L2, T/L3.** Use a true-RMS meter, all three line-to-line readings. Standing voltage should be 432–528 VAC for a 480V-class drive. Anything above 510 VAC standing puts you within a normal regen event of tripping oV. If standing voltage is high, check the upstream transformer tap setting — you may need to drop one tap.

3. **Verify the dynamic braking circuit if installed.** With drive de-energized and bus confirmed at zero, ohm-out the dynamic braking resistor from terminal B1/+ to B2 on the drive (or from the external DBR's terminals if mounted remotely). Expected resistance depends on motor and drive size, typically 16–100 ohms for a 480V GA800 in the 5–25 HP range. An open or shorted DBR will produce repeated oV trips on every decel.

4. **Test the dynamic braking chopper (IGBT).** This is internal to the GA800 on frames up through 4055. With drive powered and the motor coupled to a flywheel or other inertia load, run a normal forward ramp to full speed, then issue a stop command. Watch DC bus voltage in U1-07 on the keypad. If the bus climbs above 750 VDC and stays there during decel, the chopper isn't firing. The chopper turn-on threshold is approximately 750 VDC on a 480V drive.

5. **Confirm L3-04 is enabled.** Read parameter L3-04 (Stall Prevention Selection During Deceleration). Settings:
   - 0 = Disabled
   - 1 = General Purpose (default — drive extends decel to keep bus below 770 VDC)
   - 2 = Intelligent (drive optimizes decel ramp shape)
   - 3 = Stall Prevention with Braking Resistor (use when DBR is installed and you want fast decel)
   - 4 and 5 = Application-specific
   For a drive with no DBR, set L3-04 = 1. For a drive with DBR, L3-04 = 3.

6. **Lengthen decel time C1-02.** If the bus voltage at trip (U2-08) was right at threshold and the drive has no DBR, extend C1-02. Rule of thumb: a fan or pump can use C1-02 = C1-01 + 50%. A high-inertia centrifuge needs C1-02 set to allow free-coast decel time, which can be 2–5 minutes.

7. **Check for utility events.** If standing voltage is fine but oV trips happen at random clock times not correlated to drive starts/stops, install a Fluke 1748 or 1735 power quality recorder on the drive input for 7 days. Trigger threshold: 10% above nominal for 100 ms or more. Coordinate with the utility — capacitor switching transients are a known cause and the utility can adjust their switching strategy.

8. **Confirm motor isn't being driven by load.** With the drive de-energized, manually rotate the motor shaft in the normal direction of travel. If the load drives the motor in the reverse direction (gravity, web tension, fluid head), that energy goes into the bus during operation. You need a DBR or, for continuous regen applications, a regenerative drive (CIMR-GA4R series active front-end).

9. **For common-bus or shared-DC applications:** verify each inverter on the bus has a properly sized DBR or that one central DBR is sized for the *worst-case simultaneous regen* of all drives, not just one. This is a design error I find on at least one job a year.

## Parts that may need replacement

| Part | Catalog Number | Typical Cost | Where to Buy |
|---|---|---|---|
| GA800, 480V, 5HP (ND) | CIMR-GA4A0011FAA | $1,650–$1,950 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=yaskawa-ga800-error-ov), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=yaskawa-ga800-error-ov), [Wolf Automation](https://www.wolfautomation.com) |
| GA800, 480V, 15HP (ND) | CIMR-GA4A0023FAA | $2,750–$3,200 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=yaskawa-ga800-error-ov), [Wolf Automation](https://www.wolfautomation.com) |
| GA800, 480V, 50HP (ND) | CIMR-GA4A0072FAA | $5,800–$6,900 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=yaskawa-ga800-error-ov), [Wolf Automation](https://www.wolfautomation.com) |
| Dynamic braking resistor, 16 ohm 1500W | Yaskawa CDBR-4022D | $385–$520 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=yaskawa-ga800-error-ov), [Wolf Automation](https://www.wolfautomation.com) |
| Dynamic braking resistor, 30 ohm 750W | Yaskawa LKEB-4015 | $295–$380 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=yaskawa-ga800-error-ov) |
| External DB unit (large frames) | CDBR-4045D | $1,250–$1,550 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=yaskawa-ga800-error-ov), [Wolf Automation](https://www.wolfautomation.com) |
| Fluke 1748 power quality logger | FLUKE-1748/BASIC | $7,400–$8,800 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=yaskawa-ga800-error-ov), [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| Fluke 87V industrial multimeter | FLUKE-87-5 | $480–$580 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=yaskawa-ga800-error-ov) |

The GA800 chopper IGBT and bus capacitors are not field-replaceable. If the chopper is dead the drive is replaced. Yaskawa offers a 24-month manufacturer warranty (verify ship date via the serial number) before considering replacement out-of-warranty.

## When to call a controls engineer

Bring in senior support when: oV trips show U2-08 readings above 900 VDC repeatedly (suggests transient events outside the drive's design envelope and you need a power quality study); you're on a common DC bus configuration with three or more drives and oV migrates between inverters; the application is a hoist, crane, or web tension system where regenerative energy is normal operation and you need to size or commission an active-front-end (regenerative) GA800; or when oV happens only at specific speed bands suggesting resonance feeding mechanical energy back to the motor.

## FAQs

**Can I just disable Stall Prevention to get faster decel?** Don't. With L3-04 = 0, the drive will trip oV on every decel that isn't slow enough to coast. The "right" way to get fast decel is to install a properly sized dynamic braking resistor and set L3-04 = 3.

**My drive shows oV only on power-up before I even start it. Why?** Input voltage too high at the moment the pre-charge circuit closes. Check incoming voltage standing. Also possible: a damaged DC bus snubber or a failed bus capacitor that's leaking — usually shows up with U2-08 abnormally high while the drive is supposedly idle.

**Will an isolation transformer help with oV from utility events?** It will buffer voltage transients but won't reduce steady-state overvoltage from a wrong transformer tap. Sized correctly (1.25× drive kVA minimum) an isolation transformer does help with capacitor-switching transients common at industrial substations.

**Difference between oV and ov1 / ov2 / ov3?** On the GA800, only oV exists as a fault. Older Yaskawa drives (G7, F7) had subcodes ov1/ov2/ov3 for different bus voltage bands. The GA800 logs all overvoltage events as oV and you read the magnitude from U2-08.

**Should the dynamic braking resistor have a thermal switch wired in?** Yes — every Yaskawa DBR ships with a normally-closed thermal switch rated 130°C or 150°C depending on model. Wire it in series with an external e-stop or to a digital input configured as External Fault (H1-0x = 20 to 2F). A DBR that overheats and isn't disabled will eventually fire and ignite the cabinet.

## Related guides

- [Yaskawa GA800 oC Fault — Overcurrent Fix](/yaskawa-ga800-error-oc/)
- [Yaskawa GA800 Uv1 Fault — DC Undervoltage Fix](/yaskawa-ga800-error-uv1/)
- [Allen-Bradley PowerFlex F005 Fault — Overvoltage Fix](/allen-bradley-powerflex-f005-fault/)
- [ABB ACS580 Fault 3210 — DC Overvoltage Fix](/abb-acs580-fault-3210/)
- [Danfoss FC-302 Alarm 13 — DC Link Overvoltage Fix](/danfoss-fc302-alarm-13/)

## See Also

- [Yaskawa V1000 OV Fault - What It Means and How to Fix It](/posts/yaskawa-v1000-fault-ov/)
- [Yaskawa VFD Fault LF — Causes & Fix](/posts/yaskawa-vfd-fault-lf/)
- [Yaskawa VFD Fault ER — Causes & Fix](/posts/yaskawa-vfd-fault-er/)
- [Yaskawa GA800 Uv1 Fault — DC Undervoltage Fix](/posts/yaskawa-ga800-error-uv1/)
