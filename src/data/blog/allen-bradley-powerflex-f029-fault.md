---
title: "Allen-Bradley PowerFlex F029 Fault — Analog Loss Fix"
description: "PowerFlex F029 (Analog Input Loss) means the 4-20mA reference signal on the drive's analog input dropped below the threshold set by parameter T091 Analog In..."
pubDatetime: 2026-05-20T17:00:00Z
modDatetime: 2026-05-20T17:00:00Z
author: "Dana Kowalski"
slug: allen-bradley-powerflex-f029-fault
featured: false
draft: false
tags:
  - allen-bradley
  - vfd
  - industrial-maintenance
  - drives
  - analog-loss
---
## Quick answer

PowerFlex F029 (Analog Input Loss) means the 4-20mA reference signal on the drive's analog input dropped below the threshold set by parameter **T091 Analog In 1 Loss** (525 series) — typically 4mA minus the configured deadband. The most common cause in the field is a broken or corroded wire on the signal pair, not a dead PLC or sensor. Second most common: somebody changed the analog input parameter from 4-20mA to 0-10V or back and didn't notice the loss-detection threshold no longer matches the wiring.

## What PowerFlex F029 means

The drive's analog input has built-in signal-loss detection on the 4-20mA range only. A 0-10V input cannot lose signal — 0 V is a valid commanded zero. So when the drive is configured for 4-20mA and the live signal drops below the loss threshold (default 3.2 mA, configurable via T091), the drive recognizes that the transmitter or wiring has failed and trips F029. This is industry-standard fail-safe behavior — without it, a broken sensor wire would command zero speed silently, which on many applications is more dangerous than a controlled stop.

On a PowerFlex 525, the relevant parameters are:
- **T090 Analog In 1 Loss Action** — what the drive does on loss (0=disabled, 1=fault, 2=stop, 3=zero ref, 4=min freq, 5=max freq, 6=hold last)
- **T091 Analog In 1 Loss** — threshold for declaring loss (default 0 = 3.2 mA on the 4-20mA scale)
- **T092 Analog In 1 Hi** — sets the 20mA-equivalent reference value
- **T093 Analog In 1 Lo** — sets the 4mA-equivalent reference value
- **T094 Analog In 2 Loss Action** — same as T090 but for analog input 2

On a 750-class, the parameters are in a different numbering range (parameters 261, 262, 263 for AI 0 loss handling) but the logic is identical.

The 4-class drives use parameter A065 for analog input loss configuration with similar logic.

The trip is intentionally slow — typically 1.5 to 2 seconds below threshold — to ride through brief transients (PLC scan stutter, EMI dropout) without nuisance tripping. If you're seeing F029 trips that come and go quickly, the signal is bouncing in and out of the loss threshold, not failing outright.

## Read the fault history first

F029 is one of the easier faults to misdiagnose because clearing it loses the most useful clue: the analog input value at trip. The 525 logs the input mA reading alongside the F029 code in D361.

PowerFlex 525 with 22-HIM-A3:

1. **Esc** → **Diagnostics** → **Enter**
2. **D361 Fault 1 Code** — record code and accompanying analog value
3. **D362** through **D365** — older faults. Multiple F029s with the same analog value at trip (say, always 0.8 mA) point to a complete signal loss — broken wire or dead transmitter. F029s at varying values (sometimes 2.5 mA, sometimes 3.0 mA, sometimes 0 mA) point to an intermittent — corroded terminal, damaged shield, or signal bouncing across the threshold

In Studio 5000 for a 755: Faults tab plus parameter 260 (Analog In 0 Value) — you can trend this live during a run to catch intermittents.

In CCW for a 525: **Drive → Faults & Alarms**, plus live read of parameter T088 (Analog In 1 Value) when reconnected.

**Field insight on shield grounding:** F029 trips that come and go on a long signal run (over 50 ft, particularly running near VFD output cables) are almost always a shield-grounding problem. The signal pair shield must be bonded at *one end only* — typically the drive end, never the transmitter end. A shield bonded at both ends creates a ground loop, and 60 Hz current flowing on the shield modulates the analog signal enough to push it below the loss threshold during VFD switching transients. I've fixed dozens of "intermittent F029" calls in two minutes by lifting the shield bond at the transmitter end. If you have access to it, run the signal pair in metal conduit or use Belden 8761-type instrumentation cable, and keep it physically separated from motor leads by at least 12 inches.

## Common causes (ranked by frequency)

1. **Broken or damaged signal wire** — pulled out of a terminal, broken at a strain point, severed in a cable tray
2. **Loose terminal at the drive or transmitter end** — vibration over months loosens a screw terminal until the connection becomes intermittent
3. **Failed transmitter / sensor** — the field device that should produce 4-20mA stopped producing it (power loss, internal failure, blown fuse)
4. **PLC analog output card failure or unpowered** — common after a controls cabinet power event
5. **Wrong analog input mode set on the drive** — somebody changed T087 (Analog In 1 Sel) from 4-20mA to 0-10V or vice versa without changing the field wiring
6. **Shield ground loop or shield not bonded** — intermittent F029 on long signal runs near VFD output cables
7. **Reversed polarity at the analog input** — signal connected with + and - swapped. Drive reads 0 mA on a healthy 16 mA loop
8. **Burnt-out 250 Ω burden resistor inside the drive** — uncommon but happens if 24 V got applied to the analog input

## Step-by-step diagnosis

Safety first, even though analog circuits are low energy: lock and tag if you'll open the drive cover or disconnect wiring from energized terminals. The bus capacitors still hold lethal voltage; stay away from power terminals. Arc-flash boundary applies until proven dead.

1. **Pull the fault history before clearing.** D361 and the analog value at trip. Note whether multiple F029s show the same value (consistent loss) or varying values (intermittent).

2. **Verify the analog input is configured for 4-20mA.** On a 525, check parameter **T087 Analog In 1 Sel** = **1 (4-20mA)** if you're using current loop, or **0 (0-10V)** if voltage. If T087 says 0-10V but the field is wired for 4-20mA, the drive sees 4 mA as 0.4 V (via the 100 ohm internal voltage burden), reads zero reference, and depending on T090 may or may not trip F029.

3. **Verify the analog input current with a meter.** Put a DMM in series with the 4-20mA loop at the drive terminals (or use a clamp meter rated for DC current loops, like a Fluke 773). At minimum process setpoint you should see 4 mA; at maximum 20 mA. Anywhere outside that range during running operation is a problem.

4. **Check the wiring continuity end to end.** Power down the loop or use a non-energized DMM continuity test. Probe from the drive terminal block to the transmitter terminal block. Resistance should be near zero for the conductors plus the transmitter's internal impedance (typically reads as 250 Ω plus a few ohms of wire).

5. **Inspect the terminals at both ends.** Look for green corrosion (common in food plants, dairies, wastewater), discoloration from heat, signs that the wire has backed out from a screw terminal. Use a flat-blade screwdriver and put gentle tension on each conductor — if it pulls free easily, that's your problem.

6. **Verify shield bonding.** Trace the signal cable shield. It should be bonded to ground at the drive end (parameter T085 grounding terminal or the cabinet ground bar) and lifted at the field device end. If bonded at both ends, lift the field end and retest.

7. **Power-cycle the transmitter or PLC analog output card.** A common silent failure is an analog output card that locks up; a power cycle restores it. If the card is healthy after a cycle but fails again in hours or days, it's degrading — replace it.

8. **Substitute the field signal with a known-good calibrator.** Use a current calibrator (Fluke 705 or 773) at the drive terminals, sourcing 4 mA then 12 mA then 20 mA. The drive's parameter **T088 Analog In 1 Value** should track. If it does, the drive is fine and the problem is upstream of the drive terminals.

9. **Adjust T090 Loss Action only as a last resort.** Setting T090 to **6 (Hold Last Reference)** stops the fault but creates a dangerous condition — the drive will keep running at whatever speed it was at when signal failed. Only acceptable on processes where holding last speed is safer than tripping (uncommon). Default T090 = **1 (Fault)** is almost always correct.

## Parts that may need replacement

| Part | Catalog Number | Typical Cost | Where to Buy |
|---|---|---|---|
| 4-20mA loop calibrator | Fluke 705 | $610–$780 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f029-fault) |
| 4-20mA process clamp meter | Fluke 773 | $390–$520 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20), [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f029-fault) |
| Belden 8761 instrumentation cable (twisted shielded pair) | 8761 | $0.95–$1.40/ft | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f029-fault), [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| Phoenix Contact UT 2.5 terminal block | 3044102 | $4.50–$6.50 each | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f029-fault), [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| Allen-Bradley 1734-IE2C 4-20mA analog input card | 1734-IE2C | $440–$580 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f029-fault), [Wolf Automation](https://www.wolfautomation.com) |
| Allen-Bradley 1734-OE2C 4-20mA analog output card | 1734-OE2C | $480–$620 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f029-fault), [Wolf Automation](https://www.wolfautomation.com) |
| Endress+Hauser Promag 4-20mA flow transmitter (replacement) | Various | $1,200–$3,500 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f029-fault), [Wolf Automation](https://www.wolfautomation.com) |
| PowerFlex 525 drive replacement (5HP, 480V) | 25B-D010N104 | $1,150–$1,400 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f029-fault), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f029-fault) |

The drive itself almost never causes F029 — the burden resistor on the analog input can fail if overvoltage was applied, but in 15 years I've replaced exactly one drive for an analog input failure.

## When to call a controls engineer

Call for senior support when: F029 trips persist after wiring and field device are verified healthy, suggesting a programming or scaling issue in the PLC; when the application requires reconfiguring the analog input scaling (T092/T093) to match a non-standard transmitter range; when adding a second analog input or a feedback loop (PID control via parameter A458–A464); or when the application is being upgraded from 4-20mA to a fieldbus reference (EtherNet/IP, ControlNet, DeviceNet) and you need to migrate the speed reference architecture.

## FAQs

**Can I disable F029 to keep the line running?** You can, by setting **T090 Analog In 1 Loss Action** to **0 (Disabled)** or **6 (Hold Last Ref)**, but recognize the safety implication: if the signal goes to zero, the drive will keep running at last commanded speed or accept a spurious zero. Only do this if the process can tolerate it and document the change. Default = Fault is the safe choice.

**Why doesn't F029 trigger on a 0-10V input?** Because zero volts is a valid command (commanded zero speed). The drive can't distinguish between "operator wants zero speed" and "signal wire is broken." A 4-20mA loop has a live zero (4 mA) that allows the drive to know the difference between "commanded zero" (4 mA) and "broken loop" (0 mA).

**My drive shows F029 but the PLC tag shows the analog output card is sending 12 mA. What's happening?** The card is sending 12 mA on the *card output*, but something between the card and the drive terminals is breaking the signal — a wire, a terminal, an isolator, or a barrier. Loop-check from the card output terminal all the way to the drive input terminal with a current meter in series.

**Can I use the drive's 10V analog reference output to power my transmitter?** No. The drive's 10V output is a low-current reference (typically 10 mA max) and is voltage, not loop power. 4-20mA transmitters need a separate 24 VDC loop power supply (Phoenix Contact MINI-PS or equivalent).

**Why does F029 happen only when the big motor across the room starts?** Classic EMI coupling. The starting motor radiates a transient that couples into the analog signal pair via shared ground or capacitive coupling. Solutions: shielded cable, single-point shield bond at drive end only, physical separation from VFD output cables, and ferrite cores on the signal pair at the drive terminal.

## Related guides

- [Allen-Bradley PowerFlex F004 Fault — Undervoltage Fix](/allen-bradley-powerflex-f004-fault/)
- [Allen-Bradley PowerFlex F005 Fault — Overvoltage Fix](/allen-bradley-powerflex-f005-fault/)
- [Allen-Bradley PowerFlex F007 Fault — Motor Overload Fix](/allen-bradley-powerflex-f007-fault/)
- [Allen-Bradley PowerFlex F012 Fault — HW Overcurrent Fix](/allen-bradley-powerflex-f012-fault/)
- [Allen-Bradley PowerFlex F081 Fault — Communication Loss Fix](/allen-bradley-powerflex-f081-fault/)

## See Also

- [Allen-Bradley PowerFlex Fault F012 — Causes & Fix](/posts/allen-bradley-powerflex-fault-f012/)
- [Allen-Bradley PowerFlex F005 Fault — Overvoltage Fix](/posts/allen-bradley-powerflex-f005-fault/)
- [Allen-Bradley PowerFlex 525 Fault F003 - What It Means and How to Fix It](/posts/allen-bradley-powerflex-525-fault-f003/)
- [Allen-Bradley PowerFlex 753/755 Control Sync Fault Fix](/posts/allen-bradley-powerflex-753-control-sync-fault/)
