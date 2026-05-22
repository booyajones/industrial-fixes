---
title: "Yaskawa GA800 Uv1 Fault — DC Undervoltage Fix"
description: "Yaskawa GA800 Uv1 (DC Bus Undervoltage) means the DC bus dropped below the L2-05 threshold (default 380 VDC for a 480V-class drive, 190 VDC for a..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: yaskawa-ga800-error-uv1
featured: false
draft: false
tags:
  - yaskawa
  - vfd
  - industrial-maintenance
  - drives
  - dc-undervoltage
---
## Quick answer

Yaskawa GA800 Uv1 (DC Bus Undervoltage) means the DC bus dropped below the L2-05 threshold (default 380 VDC for a 480V-class drive, 190 VDC for a 240V-class) for longer than L2-02 (default 2 seconds) while the drive was in a Run state. In the field, the cause I see most often is a coincident load on the same branch circuit pulling line voltage into a sag — another VFD soft-starting, an air compressor across-the-line start, or a welder duty cycle. A close second is a loose lug on R/L1, S/L2, or T/L3 producing a high-impedance phase that sags under load.

## What Yaskawa GA800 Uv1 means

The GA800 actually has three undervoltage codes that confuse people: Uv1 (DC bus undervoltage while running), Uv2 (control power supply undervoltage — internal 24V or 5V rail collapsed), and Uv3 (pre-charge contactor not closing or pre-charge fault). Most of the time you'll see Uv1 because it's the running fault. Uv2 and Uv3 mean different things and lead to different parts swaps.

Uv1 trips on bus voltage falling below L2-05 (default 380 VDC on 480V class) sustained longer than L2-02 (default 2.0 seconds). Both parameters are adjustable. The drive looks at bus voltage continuously through a precision divider feeding the control board ADC, not at line voltage directly. By the time bus voltage drops to 380 VDC, line voltage has been sagging significantly for some time — usually for 200 ms or longer at 350 VAC or below.

The GA800 includes a function called Kinetic Energy Buffering (KEB) — parameter L2-29 — that responds to bus undervoltage by reducing output frequency to harvest the load's kinetic energy and keep the bus alive through short utility sags. If you have a high-inertia load and an unreliable utility, KEB is the right answer instead of just raising L2-02. KEB is configured in L2-06 (Kinetic Energy Buffering Time), L2-07 (Kinetic Energy Buffering Decel Time), and L2-29 (Kinetic Energy Buffer Method).

## Read the fault history first

**Read the history before pressing Reset.** Yaskawa documents this in Technical Manual TOEPC71061800F section 6.2.4 (Undervoltage diagnostics). On the JVOP-KPLCC04 or JVOP-KPLCA04 keypad:

1. From the run screen, press **ESC** until you reach the main menu
2. Navigate to **U Monitor → U2** (most recent fault snapshot)
3. Read these parameters in order:
   - **U2-01** — fault code (the parameter the user manual calls "Current Fault")
   - **U2-02** — previous fault code (look for a pattern — Uv1 preceded by Uv3 means pre-charge issue)
   - **U2-03** — reference frequency at trip
   - **U2-04** — output frequency at trip
   - **U2-05** — output current at trip
   - **U2-07** — output voltage at trip
   - **U2-08** — DC bus voltage at trip — the critical number for Uv1
   - **U2-11** — input terminal status word at trip
4. Then **U3** for the rolling history:
   - **U3-01** through **U3-10** — last ten faults, newest to oldest
   - **U3-11** through **U3-20** — operating hours at each of those faults

If U2-08 (DC bus at trip) reads near 380 VDC, that's a textbook Uv1 — line sag pulled the bus to threshold. If U2-08 reads much lower (say 250 VDC or below), you have either a single-phased input (one phase missing for several cycles) or a collapsing pre-charge — different problems entirely.

**Field insight — the Uv1 history trap:** the GA800 records U2-08 at the *moment of fault detection*, not at the bottom of the bus sag. The bus may have already started recovering by the time the L2-02 timer expires (default 2.0 seconds). So if U2-08 reads 405 VDC and you think "the bus didn't really sag," look at U3-11 (operating hours at the most recent fault). Correlate that timestamp with plant logs — you'll find a coincident event. The drive isn't wrong, you're reading the moment the timer expired, not the depth of the sag.

## Common causes (ranked by frequency)

1. **Line voltage sag from coincident load on the same branch** — another VFD starting, a large motor across-the-line, a welder striking, a chiller compressor inrushing
2. **Loose input lug** — R/L1, S/L2, or T/L3 not torqued to spec creates a high-impedance phase that drops voltage under load
3. **Single-phased input** — a branch fuse blew, a disconnect pole isn't fully closed, or one phase of the contactor pulled in is welded open
4. **Pre-charge circuit problem** — pre-charge resistor open, pre-charge bypass relay failing to close (will usually log Uv3 first, then Uv1 when load is applied)
5. **Aged bus capacitors** — drives older than 7–10 years lose capacitance, can't ride through normal sags they handled when new
6. **Undersized branch circuit or transformer** — voltage drop under full motor load pulls bus into trip range during acceleration
7. **L2-05 or L2-02 set wrong** — someone tightened the parameters thinking they were "improving sensitivity" when the application actually needs ride-through

## Step-by-step diagnosis

Before opening the cabinet: lock and tag the upstream disconnect, wait the rated capacitor discharge — **5 minutes** for GA800 frames smaller than 4030, **10 minutes** for 4030 and above. Verify zero DC bus at B1/+ and ⊖ with a CAT-IV meter rated 1000 VDC. Respect the NFPA 70E arc-flash boundary marked on the cabinet label until you've confirmed zero energy and you are in the PPE the label calls for.

1. **Read the fault history before clearing.** Capture U2-01 through U2-11 and U3-01 through U3-20. Note U2-08 (bus voltage at trip) — a number near 380 VDC tells a different story than a number near 200 VDC.

2. **Measure incoming line voltage at the drive input terminals R/L1, S/L2, T/L3.** Use a true-RMS meter. Measure all three line-to-line pairs both standing and during the next start cycle. Standing voltage should be within ±10% of nameplate — 432 to 528 VAC for a 480V drive. Imbalance greater than 3% will produce intermittent Uv1 even when average voltage looks fine. Yaskawa specifies max 2% imbalance for full-output operation.

3. **Hunt the loose connection.** De-energize and verify zero. Check torque on every input lug, output lug, and ground. The GA800 frame-3 spec for the M5 motor terminal screws is 4.1 Nm (36 in-lb); the R/L1, S/L2, T/L3 input terminals on the same frame are 4.5 Nm. Look for discoloration, melted insulation, or fretting on stranded copper. A torque screwdriver from Wera or Wiha is the right tool — don't guess.

4. **Verify branch fuses and disconnect.** Open the upstream disconnect, pull each fuse cartridge, ohm-test for continuity. A single-phased input is the classic Uv1 producer. Replace fuses as a matched set, same I²t rating and same manufacturer.

5. **Walk the surrounding equipment.** Was another VFD starting? An air compressor cycling? The fault timestamp from U3-11 plotted against your plant SCADA trend will almost always show a coincident event. This is the step that turns "the drive is broken" into "the drive is correctly detecting an upstream problem."

6. **Verify L2-02 and L2-05 parameters are at OEM defaults.** L2-05 (Undervoltage Detection Level) should be 380 VDC for 480V class — confirm someone hasn't raised it trying to compensate for chronic sags. L2-02 (Momentary Power Loss Ride-Thru Time) defaults to 2.0 sec for 480V class. Extending L2-02 up to 25 seconds is allowed and can ride through utility events, but extends only as long as bus capacitance and load inertia permit.

7. **Enable Kinetic Energy Buffering for ride-through.** If the load is a fan, pump, centrifuge, or any high-inertia application, set L2-29 = 1 (Single Drive KEB). The drive will harvest the motor's kinetic energy on a bus dip to keep itself alive. Set L2-06 = 0.1 s (Buffering Decel Time short — fast frequency drop to harvest energy) and L2-07 = 5.0 s (Acceleration Time After Buffering — recover gracefully after voltage returns).

8. **Test pre-charge if drive is older than 5 years.** Power up the drive with no run command. Watch bus voltage on U1-07 (DC Bus Voltage monitor). On a healthy 480V GA800, you should see the bus ramp from 0 VDC to approximately 670 VDC in 1–2 seconds, then hold steady. If the bus ramps slowly, stops below 600 VDC, or oscillates, the pre-charge resistor is open or the bypass relay isn't closing. The drive will eventually log Uv3 — and you cannot fix this in the field. The drive is replaced.

9. **Megger motor and motor leads if you suspect a load-side fault.** A line-to-ground motor fault can pull the bus down on start. Disconnect U/V/W from the drive, megger each phase to ground at 1000 VDC. Below 1 megohm is a definite ground fault — fix the motor before re-energizing the drive.

## Parts that may need replacement

Yaskawa does not sell the bus capacitor bank, pre-charge resistor, or pre-charge relay as separate field parts on the GA800. A drive with a confirmed pre-charge or capacitor failure is replaced as a complete unit.

| Part | Catalog Number | Typical Cost | Where to Buy |
|---|---|---|---|
| GA800, 480V, 3HP (ND) | CIMR-GA4A0008FAA | $1,350–$1,650 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=yaskawa-ga800-error-uv1), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=yaskawa-ga800-error-uv1) |
| GA800, 480V, 7.5HP (ND) | CIMR-GA4A0014FAA | $1,950–$2,300 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=yaskawa-ga800-error-uv1), [Wolf Automation](https://www.wolfautomation.com) |
| GA800, 480V, 20HP (ND) | CIMR-GA4A0031FAA | $3,200–$3,800 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=yaskawa-ga800-error-uv1), [Wolf Automation](https://www.wolfautomation.com) |
| GA800 line reactor 3%, 5HP | LR3-00504 | $310–$420 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=yaskawa-ga800-error-uv1), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=yaskawa-ga800-error-uv1) |
| GA800 line reactor 5%, 10HP | LR5-01005 | $385–$520 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=yaskawa-ga800-error-uv1), [Wolf Automation](https://www.wolfautomation.com) |
| Bussmann FRS-R-30 input fuse (480V) | FRS-R-30 | $14–$22 each | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=yaskawa-ga800-error-uv1), [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| Fluke 1748 power quality logger | FLUKE-1748/BASIC | $7,400–$8,800 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=yaskawa-ga800-error-uv1), [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| Wera 7440 torque screwdriver, 1.2–3.0 Nm | Wera 05074722001 | $185–$240 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |

## When to call a controls engineer

Bring in senior support when: the fault history shows Uv1 trips clustered at consistent times of day (suggests shift-change capacitor switching at the substation); U2-08 reads below 250 VDC on a 480V drive repeatedly (single-phased input or hardware-class pre-charge problem); the drive is on a long branch run from a small transformer and the voltage drop calc shows you're operating near the edge of code-compliant sizing; or when the load is mission-critical and you need to engineer a KEB strategy across multiple coordinated drives.

## FAQs

**Can I just increase L2-02 to ride through the sag?** Up to a point. The default 2.0 sec is conservative. You can extend up to 25 seconds, but at some point bus capacitance and load inertia limit how long the drive can hold the bus above L2-05 with no input power. KEB (L2-29) is usually a better answer for high-inertia loads.

**Will a line reactor help with Uv1?** A 3% or 5% line reactor adds source impedance and *worsens* steady-state voltage at the drive input under load by a small amount, but it dramatically smooths transient sags by adding inductance to filter the dip. On a noisy industrial bus with frequent transients, a line reactor reduces Uv1 frequency. Yaskawa specifically recommends 3% impedance for general purpose, 5% for high-harmonic environments.

**My drive trips Uv1 on cold mornings only. Why?** Bus capacitor ESR (equivalent series resistance) increases at low temperatures. Older capacitors that are marginally OK at 25°C can fail to hold bus voltage under load at 0°C. This is an end-of-life indicator. Replace the drive before it strands you in February.

**Difference between Uv1, Uv2, and Uv3?**
- **Uv1** = DC bus undervoltage while running (380 VDC threshold, sustained 2.0 sec)
- **Uv2** = Control circuit undervoltage (internal 24V or 5V control supply collapsed — usually a damaged control board)
- **Uv3** = Pre-charge / soft-charge fault (pre-charge resistor or bypass relay didn't transition correctly)
Uv2 and Uv3 mean the drive itself has a hardware problem. Uv1 is most often an upstream issue.

**Should I install a UPS in front of the VFD?** Almost never. The GA800's own bus capacitors plus KEB ride through 95% of normal utility events. A real solution to chronic Uv1 is either a 5% line reactor for filtering, an isolation transformer for clean power, or an oversized supply transformer with extra ride-through capacity. A UPS sized for full VFD load is huge, expensive, and adds its own reliability concerns.

## Related guides

- [Yaskawa GA800 oC Fault — Overcurrent Fix](/yaskawa-ga800-error-oc/)
- [Yaskawa GA800 oV Fault — DC Overvoltage Fix](/yaskawa-ga800-error-ov/)
- [Allen-Bradley PowerFlex F004 Fault — Undervoltage Fix](/allen-bradley-powerflex-f004-fault/)
- [ABB ACS580 Fault 3220 — DC Undervoltage Fix](/abb-acs580-fault-3220/)
- [Danfoss FC-302 Alarm 12 — Overcurrent Fix](/danfoss-fc302-alarm-12/)
