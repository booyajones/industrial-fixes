---
title: "Allen-Bradley PowerFlex F091 Fault — Encoder Loss Fix"
description: "PowerFlex F091 (Encoder Loss) means the drive lost the feedback signal from the motor encoder while running in closed-loop vector or position mode — the..."
pubDatetime: 2026-05-20T17:00:00Z
modDatetime: 2026-05-20T17:00:00Z
author: "Dana Kowalski"
slug: allen-bradley-powerflex-f091-fault
featured: false
draft: false
tags:
  - allen-bradley
  - vfd
  - industrial-maintenance
  - drives
  - encoder-loss
---
## Quick answer

PowerFlex F091 (Encoder Loss) means the drive lost the feedback signal from the motor encoder while running in closed-loop vector or position mode — the firmware was expecting pulses on channels A and B, didn't get them, and dropped to fault rather than spin the motor open-loop. The single most common cause is a damaged or pinched encoder cable, not a bad encoder. Second most common: 24VDC encoder supply dropped. Drive failure is a distant third.

## What PowerFlex F091 means

F091 only appears on PowerFlex drives configured for encoder-feedback operation — that's PowerFlex 755 with a 20-750-ENC-1 or 20-750-DENC-1 feedback option card, PowerFlex 753 with the same options, or PowerFlex 525 with the optional 25-COMM-D or 25-ENC encoder kit. A drive in sensorless vector or V/Hz mode will never throw F091 because it isn't expecting encoder pulses.

The fault logic: in closed-loop mode the firmware monitors A and B channels of the quadrature encoder at a kilohertz-class rate. It expects pulses proportional to commanded speed. If commanded frequency is above a threshold (default ~5 Hz) but encoder counts per scan drop to zero or below a sanity threshold, F091 fires after a debounce window. The drive trips because running closed-loop vector without feedback is dangerous — the firmware would lose torque control, the motor could runaway or stall, and worst case the drive overcurrents into a hard fault.

PowerFlex 525 stores encoder loss diagnostic info in parameter **A560 Pulse Input Mode** state and the standard fault history at D361. PowerFlex 755 with 20-750-ENC-1 surfaces detailed encoder diagnostics including channel-A pulse count, channel-B pulse count, and marker pulse count under the feedback option's configuration parameters. Pull those before clearing.

## Read the fault history first

This is the step that separates a 20-minute diagnosis from chasing your tail. **Do not clear the fault before you read the history.** Clearing wipes the diagnostic record on every PowerFlex series.

On a PowerFlex 525 with the optional encoder kit and a 22-HIM-A3 keypad:

1. From the run screen, press **Esc** to the main menu
2. Arrow to **Diagnostics** and **Enter**
3. Read **D361** (most recent) through **D365**
4. Check **A560 Pulse Input Mode** to confirm the encoder configuration matches the wiring

On a PowerFlex 755 in Studio 5000: expand the drive in the I/O tree, right-click, **Properties → Drive → Faults**. Then go to the feedback option card properties — the 20-750-ENC-1 exposes counters that show whether one channel, both channels, or only the marker was lost.

**Field insight on F091:** the fault almost always happens at a specific commanded speed or under a specific load. Pull the operating data captured at the trip. If F091 fires only above 30 Hz, you have an encoder cable problem that's only manifesting at higher pulse rates (capacitive coupling losses get worse with frequency). If F091 fires at startup the moment the drive commands motion, you have a wiring problem or a dead encoder. If F091 only fires under load, you have a coupling problem — the encoder is mechanically slipping on the shaft.

## Common causes (ranked by frequency)

1. **Damaged or pinched encoder cable** — most common. Cables get crushed in cable trays, kinked at conduit transitions, or chafed at strain reliefs. Shielded twisted-pair encoder cable is more delicate than people give it credit for.
2. **Loose or back-out encoder coupling** — encoder body is fine, electrical is fine, but the flexible coupling between motor shaft and encoder shaft has slipped. Drive sees commanded motion but no feedback because the encoder physically isn't turning.
3. **24VDC encoder supply lost or sagging** — encoder supply on the option card or external panel supply has failed, fuse blown, or wiring backed out at the encoder terminal.
4. **Failed encoder** — open optical disc, dead LED, failed Hall sensor on a magnetic encoder, water ingress on a non-IP67 unit in a wet environment.
5. **Connector at the option card or encoder pulled out** — vibration loosens the D-sub or terminal block on the option card; same on the encoder end.
6. **Wrong encoder configuration** — quadrature counts-per-revolution parameter mismatched with the actual encoder PPR. Drive sees pulses but the count rate is wrong, can interpret as encoder loss.

## Step-by-step diagnosis

Before you touch anything: lock and tag the disconnect, wait the rated discharge time, and verify zero energy at the DC bus. Encoder feedback wiring is low voltage but the drive output and motor terminals are not.

1. **Read the fault history first.** Record what speed, what direction, what load, and what precedent faults preceded the F091. Multiple F091s at the same commanded speed point to a cable resonance or grounding issue at that frequency.

2. **Visually inspect the encoder cable end-to-end.** Walk it. Look for crushed sections, abrasion at fittings, conductive contamination at terminal points, signs of rodent damage on plant floor runs (more common than you'd guess), and any place the shielded cable is bundled with power conductors (encoder cable should be separated from VFD output cable by at least 6 inches; running them in the same conduit is a no-go).

3. **Verify encoder supply.** With the drive de-energized but control power on, meter the encoder supply at the encoder body's terminal. Most PowerFlex encoder option cards provide 5V or 12V (selectable via configuration); 24V encoder kits are external supply. The encoder supply must be within ±10% of nominal at the encoder's terminal block, not at the panel power supply — voltage drop matters on a 200 ft encoder cable.

4. **Check the encoder coupling.** With the motor de-energized, slowly rotate the motor shaft by hand. The encoder should turn 1:1 with the motor — no slip, no backlash, no wobble. Common failure: the flex coupling set screw has backed out, the encoder body rotates relative to the shaft, and the drive sees a fraction of commanded pulses.

5. **Verify encoder output signals.** With encoder supply restored and motor turning slowly (jog at 1 Hz from the keypad if you must), probe A and B channels at the encoder option card terminal block with a multimeter on Vdc — you should see a value oscillating between near-zero and supply voltage as the encoder turns. Better: use a scope. You want to see clean square waves on A and B, 90° out of phase, with consistent amplitude. Missing or weak channels = bad encoder or bad cable.

6. **Confirm encoder configuration parameters.** On a 525 with the encoder kit, check **A560 Pulse Input Mode** and the encoder PPR (pulses per revolution) parameter — it must match the encoder nameplate. On a 755 with 20-750-ENC-1, the feedback configuration is under the option card's parameter tree. A mismatch produces an effective encoder loss because the count rate doesn't match commanded speed.

7. **Check shielding and grounding.** Encoder cable shield should be grounded at *one end only*, typically at the drive end (the encoder option card has a dedicated shield terminal). Double-grounding the shield creates a ground loop and produces apparent encoder loss as common-mode noise overwhelms the signal. Lifting the shield at the encoder body is usually the fix.

8. **Swap the encoder if everything else checks out.** Encoders are field-replaceable. Order an exact match — PPR, output type (line driver vs. open collector), voltage rating must all match.

> **Field knowledge nugget:** On Allen-Bradley applications with PowerFlex 755s driving paper-machine winder sections — anywhere you have long encoder cable runs (>100 ft) in a high-noise environment — F091 trips that happen specifically when a neighboring high-current contactor fires are almost always common-mode noise pickup on the encoder shield, not actual encoder loss. The fix is not a better encoder; the fix is a properly grounded shielded cable, separation from power conductors, and on really bad installations, ferrite cores on the encoder cable at the drive end. I've solved F091 on a Crown Holdings can line by adding three Würth 74271132 ferrites on the encoder cable. No other change. The drive ran for 4 years without another F091.

## Parts that may need replacement

| Part | Catalog Number | Typical Cost | Where to Buy |
|---|---|---|---|
| 20-750-ENC-1 Single Encoder Option (755) | 20-750-ENC-1 | $580–$720 | [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO), [Wolf Automation](https://www.wolfautomation.com?aff=PLACEHOLDER-WOLF) |
| 20-750-DENC-1 Dual Encoder Option (755) | 20-750-DENC-1 | $890–$1,100 | [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO) |
| 25-ENC Encoder kit for PF525 | 25-ENC | $295–$380 | [AutomationDirect](https://www.automationdirect.com?aff=PLACEHOLDER-ADI), [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO) |
| Allen-Bradley 845H series encoder, 1024 PPR | 845H-SJDN24DDLY4 | $580–$760 | [AutomationDirect](https://www.automationdirect.com?aff=PLACEHOLDER-ADI), [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO) |
| Encoder cable (shielded, 18 AWG, per ft) | Belden 1030A | $3–$5/ft | [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO), [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| Würth ferrite core (large bore) | 74271132 | $4–$8 each | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20), [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO) |
| Encoder flex coupling (1/4" to 3/8") | Lovejoy SX-1 or equivalent | $35–$65 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20), [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO) |

## When to call a controls engineer

Call senior controls support when: F091 returns after encoder, cable, and coupling have all been replaced (suggests a configuration or noise issue beyond simple component failure); the application requires position-mode operation and you need to set up registration or marker-pulse logic; multiple drives on the same line throw F091 in correlated patterns (network grounding issue); or when the application is safety-critical (winder runaway, hoist, anything where loss of speed control creates a hazard).

## FAQs

**Can I run my drive open-loop while I wait for an encoder?** Sometimes. If the application can tolerate sensorless vector or V/Hz operation (you lose tight speed regulation but the motor still spins controllably), you can change the **P047 Speed Reference Mode** and feedback parameter to sensorless and disable encoder feedback temporarily. **You cannot do this** on applications that require position control or tight speed regulation (paper machine drives, lift drives, anything coordinated with another drive).

**Why does F091 sometimes happen only after the drive's been running for hours?** Thermal expansion. An encoder cable connector at the drive end heats up over operating hours and a marginal pin connection becomes intermittent. Or the encoder bearings warm up and a marginal coupling slips. Run the diagnosis with the system hot, not cold.

**What's the difference between F091 and F094 (Function Loss)?** F091 is specifically encoder feedback loss. F094 covers a broader category of "expected feedback function not detected" — it can include hardwired safe-torque-off inputs not behaving, dual encoder mismatch on a 20-750-DENC-1, or analog feedback loss on a process-loop drive. They share similar diagnostic logic but the source signal is different.

**Should I use a magnetic or optical encoder?** For motor feedback on a VFD, magnetic is usually better in industrial environments — more tolerant of dust, vibration, and temperature swings. Optical gives higher resolution but the disc is fragile and contamination kills them. Allen-Bradley's 845H series is magnetic and what I install by default on PowerFlex closed-loop applications.

**Will a faulty encoder damage the motor?** Not directly. The drive's fault response on F091 is to coast-stop the motor. The motor sees no abnormal current during the trip. Risk is on restart — if you keep clearing F091 and restarting with a real fault present, you can get into a state where the drive briefly tries to apply torque without feedback before tripping again. Repeated cycles like that can heat the rotor.

## Related guides

- [Allen-Bradley PowerFlex F004 Fault — Undervoltage Fix](/posts/allen-bradley-powerflex-f004-fault)
- [Allen-Bradley PowerFlex F063 Fault — Phase Short Fix](/posts/allen-bradley-powerflex-f063-fault)
- [Allen-Bradley PowerFlex F122 Fault — I/O Board Failure Fix](/posts/allen-bradley-powerflex-f122-fault)
