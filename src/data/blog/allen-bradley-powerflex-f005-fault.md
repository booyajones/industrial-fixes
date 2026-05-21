---
title: "Allen-Bradley PowerFlex F005 Fault — Overvoltage Fix"
description: "PowerFlex F005 (DC Bus Overvoltage) means the bus exceeded the drive's ceiling — about 810 VDC on a 480V-class PowerFlex 525, around 405 VDC on a..."
pubDatetime: 2026-05-20T17:00:00Z
modDatetime: 2026-05-20T17:00:00Z
author: "Dana Kowalski"
slug: allen-bradley-powerflex-f005-fault
featured: false
draft: false
tags:
  - allen-bradley
  - vfd
  - industrial-maintenance
  - drives
  - overvoltage
---
## Quick answer

PowerFlex F005 (DC Bus Overvoltage) means the bus exceeded the drive's ceiling — about 810 VDC on a 480V-class PowerFlex 525, around 405 VDC on a 240V-class. The dominant cause in the field is regenerative energy from a decelerating load with no place to go: either decel time is too aggressive for the load inertia, or the dynamic brake resistor is missing, undersized, or open.

## What PowerFlex F005 means

When you tell a VFD to decelerate, the motor becomes a generator. The mechanical energy in the rotating mass of the load (motor rotor + driven equipment) flows backward through the inverter IGBTs, gets rectified by the IGBT body diodes, and dumps onto the DC bus. The bus capacitors absorb a small amount of it, but they're sized to filter ripple, not store kinetic energy. Once the bus rises above the overvoltage threshold, the drive must trip — letting it climb higher would punch through the IGBT collector-emitter voltage rating (typically 1200V parts in a 480V drive) and short the power module instantly.

The exact threshold on a PowerFlex 525 480V-class is 810 VDC. On a 240V-class it's 405 VDC. On a 600V-class drive (less common in the US) it's 1010 VDC. The 750-class drives use the same thresholds for the same voltage classes but allow you to read the peak bus voltage at trip via parameter 11 (DC Bus Memory).

The trip is fast — under 5 milliseconds from threshold crossing — because at the rate the bus is rising in a hard regen event you have no margin to dawdle.

Three architectural facts worth remembering:
- A PowerFlex drive has **no internal brake transistor on most ratings** — you must order it as an option or use an external dynamic brake module. The 525 series adds a brake transistor on frames B and larger as a standard feature.
- A drive **cannot regenerate to the line** unless you have an active front-end (PowerFlex 755TR or 755TM). A standard 6-pulse diode bridge is one-way: line to bus, never bus to line.
- The bus voltage sag from a brake resistor depends on resistor ohms, not just wattage. An undersized-by-resistance resistor will allow the bus to keep rising even though the chopper is firing.

## Read the fault history first

Before you clear F005, capture the diagnostic record. F005 trips erase the bus-voltage-at-trip value once cleared — that number is gold, because it tells you whether you came in just over the threshold (812 VDC, a marginal regen event) or whether you blasted through it (1050 VDC, suggesting a line transient or a runaway regen).

On a PowerFlex 525 with the 22-HIM-A3 keypad:

1. **Esc** to main menu, **Diagnostics**, **Enter**
2. Read parameter **D361 Fault 1 Code** — most recent fault
3. Read **D362**, **D363**, **D364**, **D365** in turn — older faults
4. Each fault parameter stores the fault code plus the **DC bus voltage at the moment of trip** in the companion display parameter

In Studio 5000 for a PowerFlex 755: drive properties, **Faults** tab, look at the Last Fault block and prior faults. Note the **Peak Bus Volts** in parameter 11.

In CCW for a 525: USB connection, **Drive → Faults & Alarms** — same data, friendlier presentation.

**Field insight on hoist and unwind applications:** F005 on a hoist, unwind, downhill conveyor, or any sustained-regen load — 9 times out of 10 the dynamic brake resistor failed open. Check the resistor with a meter *before* you touch decel parameters. Open the brake-resistor enclosure, disconnect leads from the chopper terminals, and measure resistance across the resistor. Compare to the stamped ohms value. An open resistor reads OL; a partial failure reads 2–3× the stamped value. I've seen techs spend half a shift tuning decel times on a hoist drive only to find the resistor element burned through six months ago and nobody noticed because the application never caught the fault until that day's heavier load.

## Common causes (ranked by frequency)

1. **Dynamic brake resistor failed open or disconnected** — on any regenerative application this is the first suspect, especially if F005 is new on a drive that previously ran fine
2. **Decel time (P033 Decel Time 1) too aggressive for load inertia** — operator increased throughput, decel didn't get retuned
3. **Dynamic brake resistor undersized in resistance** — common on retrofits where someone reused a brake resistor from a different HP drive
4. **Line voltage too high** — utility running at the upper edge of the band (505 VAC on a 480V system) pushes standing bus voltage to 715 VDC, leaving only 95 V of regen headroom
5. **Brake transistor (chopper) failed** — drive's internal IGBT that fires the brake resistor opened. The drive has no way to dump regen energy
6. **Line transient or capacitor switching event** — utility cap bank switching upstream injects a transient that propagates through the diode bridge to the bus
7. **Motor running above synchronous speed externally** — driven equipment (a conveyor downhill, a centrifuge spinning down) pulls the motor faster than commanded
8. **Bus regulation (A436) disabled or misconfigured** — the drive's built-in bus regulator extends decel automatically when the bus rises, but only if enabled

## Step-by-step diagnosis

Standard safety: lock and tag, verify zero energy at the DC bus and at the brake resistor terminals (the resistor holds no charge but its leads are tied to the bus through the chopper IGBT). Wait 5 minutes minimum after de-energizing a 525, longer on 753/755 frame 3+. Stay outside the arc-flash boundary until verified dead.

1. **Pull the fault history before clearing.** D361–D365 on the 525, faults tab in Studio/CCW on the 755. Write down the bus voltage at trip and any precedent faults.

2. **Identify the application type.** Centrifugal pump or fan? F005 is rare and points to line voltage or a transient. Hoist, unwind, conveyor with downhill section, centrifuge, machine tool spindle? Regen is your default suspect.

3. **Check standing line voltage at the drive input.** L1-L2, L2-L3, L3-L1. If you're seeing 500+ VAC on a 480V system, the drive's standing bus is already at 707+ VDC, and any regen has very little margin. Talk to facilities about taps on the supply transformer.

4. **Inspect the dynamic brake resistor (if equipped).** Power off, verify dead. Disconnect resistor leads at the chopper terminals (BR+ and BR- on a 525, R+ and R- on a 755). Measure resistor ohms with a low-resistance meter or a four-wire kelvin if you have one. Compare to stamped value. Inspect element visually — look for burned wire, blackened ceramic, separated tap-off welds. Replace any resistor outside ±10% of its rating.

5. **Verify the resistor sizing for the application.** Minimum ohms is set by the drive — a PowerFlex 525 frame B 480V drive needs a brake resistor no less than 47 ohms. Lower resistance pulls more current than the chopper IGBT can switch and trips the chopper. Required wattage depends on duty cycle and load inertia — Rockwell publication 520-AT001 has the calculation.

6. **Verify the chopper / brake transistor is firing.** With drive running and decelerating, scope the BR+ to BR- terminals (or use a DC clamp on the brake lead). You should see pulsed DC during decel — typically a PWM waveform at 1–2 kHz. No pulses on the brake terminals during a trip-causing decel means the chopper is bad. On a 525 this means drive replacement; on a 755 you can swap the chopper as part of the power module.

7. **Lengthen decel time as a diagnostic test.** Change parameter **P033 Decel Time 1** to 2× its current value. If F005 stops, the application is regenerating faster than the drive can dump and the brake resistor / decel time / chopper sizing needs revisiting. If F005 still happens, the cause is elsewhere (line transient, runaway load).

8. **Enable bus regulation as a temporary workaround.** Set **A436 Bus Reg Mode** to **1 (Enabled)**. The drive will extend decel automatically when bus voltage approaches the trip threshold. This is not a fix — it's a Band-Aid that gets the line running while you address the root cause. Note: bus reg can cause the load to coast at the end of decel if regen overpowers it.

9. **Look for line-side transients.** Put a power quality logger on the drive input for 24–72 hours. Capacitor-switching transients from the utility commonly produce a 1.2–1.5 per-unit overshoot lasting 10–50 ms, which is enough to spike the bus past 810 VDC. Solution: a 5% line reactor or a properly-sized DC-bus choke (the 525 has one available as 25-RF055).

## Parts that may need replacement

| Part | Catalog Number | Typical Cost | Where to Buy |
|---|---|---|---|
| PowerFlex 525, 480V, 5HP | 25B-D010N104 | $1,150–$1,400 | [AutomationDirect](https://www.automationdirect.com?aff=PLACEHOLDER-ADI), [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO) |
| PowerFlex 525, 480V, 10HP | 25B-D017N104 | $1,800–$2,100 | [AutomationDirect](https://www.automationdirect.com?aff=PLACEHOLDER-ADI), [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO) |
| Dynamic brake resistor, 100Ω 750W (5HP class) | AK-R2-091P500 | $220–$320 | [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO), [Wolf Automation](https://www.wolfautomation.com?aff=PLACEHOLDER-WOLF) |
| Dynamic brake resistor, 47Ω 1200W (10HP class) | AK-R2-047P1K2 | $380–$520 | [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO), [Wolf Automation](https://www.wolfautomation.com?aff=PLACEHOLDER-WOLF) |
| External brake module (for 4-class drives) | 22-BR-A or 20-750-RA | $550–$1,100 | [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO), [AutomationDirect](https://www.automationdirect.com?aff=PLACEHOLDER-ADI) |
| 5% line reactor, 480V 10HP | 1321-3R18-A | $190–$280 | [AutomationDirect](https://www.automationdirect.com?aff=PLACEHOLDER-ADI), [Wolf Automation](https://www.wolfautomation.com?aff=PLACEHOLDER-WOLF) |
| Fluke 1748 power quality logger | FLUKE-1748/BASIC | $7,400–$8,800 | [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO), [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |

The PowerFlex 525 drive itself is not field-repairable. If the chopper IGBT has failed (you see no pulses on BR+ during decel, or the brake resistor is intact but bus still climbs), replace the drive.

## When to call a controls engineer

Call for senior support when: F005 happens on a multi-drive common-bus system (the energy balance across drives is a system-level problem); when the application is regenerative-by-design (hoist, downhill conveyor, centrifuge) and you need to size or specify a brake resistor and chopper for the duty cycle; when a power quality monitor logs repeated transients and you need to engage the utility; or when you're considering an active-front-end drive (PowerFlex 755TR/TM) to regenerate to the line instead of dissipating in resistors.

## FAQs

**Will a line reactor stop F005?** Only the line-side-caused F005 — transients from capacitor switching or other source impedance issues. A line reactor does nothing for load-side regenerative trips, because the energy is coming from the motor, not the line.

**Can I just disable F005?** No. The fault is a hardware protection; bypassing it (which the drive will not let you do anyway) means the IGBT collector-emitter voltage gets exceeded and you blow the power stage. Replace cost on a 10HP drive is $2,000. Replace cost on a brake resistor is $400. Pick wisely.

**My decel was 5 seconds and worked for years. Now it trips F005. What changed?** Most likely: someone increased process speed (more kinetic energy per stop), the brake resistor degraded (check resistance), or line voltage went up (call facilities and meter it).

**Why does F005 trip during accel, not decel?** Two possibilities: a regenerative load fighting the drive (downhill conveyor that wants to run faster than commanded), or a line transient coincident with starting current pulling the diode bridge into a momentary forward-bias condition. Pull D361 and check the bus voltage at trip — over 950 VDC suggests a transient, near 810 VDC suggests a regen condition.

**Difference between dynamic braking and DC injection braking?** Dynamic braking dissipates regen energy in a resistor — fast, repeatable, generates heat. DC injection (parameter A434 DC Brake Time) applies a DC pulse to the motor windings to stop a coasting motor — slow, no regen, only works at low speeds. You cannot use DC injection to fix F005.

## Related guides

- [Allen-Bradley PowerFlex F004 Fault — Undervoltage Fix](/allen-bradley-powerflex-f004-fault/)
- [Allen-Bradley PowerFlex F007 Fault — Motor Overload Fix](/allen-bradley-powerflex-f007-fault/)
- [Allen-Bradley PowerFlex F012 Fault — HW Overcurrent Fix](/allen-bradley-powerflex-f012-fault/)
- [Allen-Bradley PowerFlex F029 Fault — Analog Loss Fix](/allen-bradley-powerflex-f029-fault/)
- [Allen-Bradley PowerFlex F081 Fault — Communication Loss Fix](/allen-bradley-powerflex-f081-fault/)
