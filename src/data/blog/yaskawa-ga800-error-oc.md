---
title: "Yaskawa GA800 oC Fault — Overcurrent Fix"
description: "Yaskawa GA800 oC (Overcurrent) means the output current sensors on at least one of the U, V, or W phases saw current exceed roughly 200% of the drive's..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: yaskawa-ga800-error-oc
featured: false
draft: false
tags:
  - yaskawa
  - vfd
  - industrial-maintenance
  - drives
  - overcurrent
---
## Quick answer

Yaskawa GA800 oC (Overcurrent) means the output current sensors on at least one of the U, V, or W phases saw current exceed roughly 200% of the drive's rated output for more than about 10 microseconds — a hardware-level trip the gate-drive logic latches before software can react. The most common field cause I find on a GA800 is a phase-to-phase or phase-to-ground short in the motor cable run after a maintenance crew pulled new conductors, not an actual motor fault. Second most common: an accel time (C1-01) too short for the load inertia after someone "optimized" the recipe.

## What Yaskawa GA800 oC means

The GA800 uses Hall-effect current transducers on the inverter output between the IGBT module and the motor terminals. The drive samples those currents every PWM cycle (typically 2 or 8 kHz on a GA800 depending on C6-02 Carrier Frequency Selection). The oC trip threshold is hardcoded in firmware at approximately 200% of the drive's rated output current shown on the nameplate and parameter o2-04 Drive Model Selection — not adjustable, not maskable.

Two events cause oC: a desaturation event in the IGBT (Vce above the gate-drive threshold while gated on, indicating the device cannot carry the demanded current), or an instantaneous current measurement above the trip band. The GA800 firmware distinguishes these internally but reports both as oC in the operator display. You read the difference in U2-15 (Output Current at fault) and U2-16 (DC Bus Voltage at fault) — a desat with a healthy bus voltage points to a hard short, a current limit trip with a bus sag points to a motor or cable issue pulling the drive into limit.

The GA800 platform shares its overcurrent logic with the GA500 and the older U1000 industrial matrix drives, but the GA800 adds a finer-grained pre-charge bus monitor and stores ten faults deep in the history register, not five like the V1000 generation. Take advantage of the depth — patterns matter.

## Read the fault history first

Do not press Reset on the keypad until you have pulled the fault history. The GA800 keeps the most recent fault details in U2 parameters and the rolling history of the last ten faults in U3 parameters. Once you press Reset, only the U3 list survives — U2 captures clear.

On a GA800 with the standard LED operator (JVOP-KPLCC04) or LCD operator (JVOP-KPLCA04):

1. From the run screen, press **ESC** to reach the menu tree
2. Arrow down to **U Monitor** and press **ENTER**
3. Select **U2** for the most-recent fault snapshot, then read:
   - **U2-01** — fault code of the most recent trip (this is the parameter the user manual calls "Current Fault")
   - **U2-02** — previous fault code
   - **U2-03** — reference frequency at trip
   - **U2-04** — output frequency at trip
   - **U2-05** — output current at trip (the number that matters most for oC)
   - **U2-06** — motor speed at trip
   - **U2-07** — output voltage at trip
   - **U2-08** — DC bus voltage at trip
   - **U2-11** — input terminal status word at trip
4. Then go to **U3** for the rolling fault log:
   - **U3-01** through **U3-10** — last ten faults, newest to oldest
   - **U3-11** through **U3-20** — cumulative operating time at each of those faults

Yaskawa documents this in Technical Manual TOEPC71061800F section 6.2 (Fault Diagnostics) and the Quick Start TOEPC71061840A appendix B.

**Field insight — the trap on GA800 oC:** the drive reports U2-05 in amps RMS but the actual trip happens on a single peak sample. If U2-05 reads, say, 145% of rated and you assumed the drive runs cool — remember that 145% RMS represents over 200% peak on a non-sinusoidal motor current, which is exactly the trip band. The drive isn't lying; you're reading an averaged metric for an instantaneous event.

## Common causes (ranked by frequency)

1. **Phase-to-phase or phase-to-ground short in motor cable** — most often where a contractor pulled new conductors through conduit and nicked the insulation on a sharp edge or at a 90° bend
2. **Accel time C1-01 too short for the connected load** — recipe tweaked by a process engineer chasing cycle time, drive can't ramp the inertia inside the current limit
3. **Motor winding short** — turn-to-turn fault in a stator coil that pulls excessive current under load; usually shows up as oC during accel or under sudden torque demand
4. **Loose output lug or terminal** — high-impedance connection creates arcing during PWM transitions, generates current transients
5. **V/f curve mismatch** — E1-04 (Max Output Frequency) or E1-05 (Max Voltage) set wrong for the motor, drive over-fluxes the iron and saturates
6. **IGBT module failure** — gate-drive board damage, bus capacitor dried up causing ringing, or a failed snubber — usually preceded by intermittent oC trips at random load points
7. **Auto-tuning never performed or done improperly** — drive's internal motor model is wrong, current regulator overshoots

## Step-by-step diagnosis

Before you open the cabinet: lock and tag the upstream disconnect, wait the rated capacitor discharge time — the GA800 manual specifies a minimum of **5 minutes** for frames smaller than 4030, and **10 minutes** for 4030 and larger. Verify zero DC bus voltage at terminals B1/+ and ⊖ (or DC+ and DC-) with a CAT-IV meter rated for at least 1000 VDC. Stay outside the NFPA 70E arc-flash boundary marked on the panel until you have confirmed zero energy and you are wearing the PPE called for on the arc-flash label.

1. **Read the fault history before clearing.** Capture U2-01 through U2-08 and U3-01 through U3-10. The output current at trip (U2-05) tells you whether you're hunting a hard short (number near 200% or higher) or a softer overload (110–160%).

2. **Disconnect U/V/W motor leads from the drive output.** Use the lugs at the bottom of the GA800, not the disconnect at the motor — you want to isolate the drive from the cable and the motor as separate test items.

3. **Megger the motor cable to ground.** With the cable disconnected at both drive and motor ends, use a 1000V megohmmeter from each conductor (U, V, W) to the cable's ground conductor and to the conduit. Acceptable reading: above 100 megohms. Below 5 megohms means moisture or insulation damage; below 1 megohm is a definite fault. Mark the cable and replace.

4. **Megger the motor itself.** Reconnect cable to motor, leave cable disconnected from drive. Megger U-V, V-W, U-W (phase-to-phase) and each phase to motor frame ground. A balanced motor reads similar values phase-to-phase, all above 100 megohms to ground when cold. A 10× difference between phases is a turn-to-turn fault — pull the motor for service.

5. **Run a no-load auto-tune.** Reconnect motor leads. With the motor coupling broken (drive turning a free motor shaft only), execute parameter **T1-01 = 2** (Rotational Auto-Tuning) or T1-01 = 1 (Stationary Auto-Tuning if you cannot decouple). Enter motor nameplate data in T1-02 through T1-06 first. The tune will fail loudly if there's a winding asymmetry the megger missed.

6. **Inspect output lugs.** Check torque on the U/V/W lugs against the GA800 manual — frame-3 spec is 4.1 Nm (36 in-lb) for the M5 motor terminal screws. Look for discoloration, melted lug barrels, or fretting corrosion on stranded copper.

7. **Re-examine accel/decel.** Parameter C1-01 (Acceleration Time 1) and C1-02 (Deceleration Time 1) should match the connected inertia. For a high-inertia fan or centrifuge, anything under 30 seconds is suspect. Lengthen C1-01 by 50% and try again — if oC clears, the recipe was the problem.

8. **Verify the V/f curve or vector model.** Confirm E1-04 = motor nameplate max frequency, E1-05 = motor nameplate voltage at that frequency, E1-06 = base frequency (60 Hz typically), E1-07 = mid frequency, E1-08 = mid voltage. A wrong curve forces the drive to push too much voltage at low speed, saturating the motor iron and pulling current.

9. **If everything checks and oC still trips:** swap the drive into a spare-drive socket if you have one, or substitute a known-good GA800 of the same model and confirm the fault follows the drive (hardware) or stays with the motor/cable (load-side).

## Parts that may need replacement

The GA800 is a sealed-power-stage drive — Yaskawa does not sell IGBT modules, current transducers, or gate-drive boards as field-serviceable parts. A hardware-failed GA800 is replaced as a complete unit. The keypad, communication options, and EMC filter assembly are user-replaceable.

| Part | Catalog Number | Typical Cost | Where to Buy |
|---|---|---|---|
| GA800, 480V, 5HP (ND) | CIMR-GA4A0011FAA | $1,650–$1,950 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=yaskawa-ga800-error-oc), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=yaskawa-ga800-error-oc), [Wolf Automation](https://www.wolfautomation.com) |
| GA800, 480V, 10HP (ND) | CIMR-GA4A0018FAA | $2,300–$2,750 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=yaskawa-ga800-error-oc), [Wolf Automation](https://www.wolfautomation.com) |
| GA800, 480V, 25HP (ND) | CIMR-GA4A0038FAA | $3,800–$4,500 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=yaskawa-ga800-error-oc), [Wolf Automation](https://www.wolfautomation.com) |
| GA800 LCD keypad | JVOP-KPLCA04 | $385–$475 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=yaskawa-ga800-error-oc), [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=yaskawa-ga800-error-oc) |
| GA800 EtherNet/IP option | SI-EN3 | $725–$890 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=yaskawa-ga800-error-oc), [Wolf Automation](https://www.wolfautomation.com) |
| Fluke 1587 FC insulation/multimeter combo | FLUKE-1587 FC | $700–$880 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=yaskawa-ga800-error-oc) |
| Megger MIT420/2 1000V insulation tester | MIT420/2 | $1,250–$1,500 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=yaskawa-ga800-error-oc) |
| Wera torque screwdriver, 1.2–3.0 Nm | Wera 7440 ESD | $185–$240 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |

## When to call a controls engineer

Bring in senior support when: the fault history shows oC trips clustered around the same operating frequency every time (suggests a mechanical resonance or a motor bar problem at a specific slip frequency); you have a regenerative bus configuration with multiple GA800s sharing a DC bus and only one inverter is tripping; the drive is in vector mode and auto-tune fails repeatedly even on a known-good motor; or when oC happens only on cold starts below 5°C cabinet temperature (gate-drive thermal compensation issue, drive is approaching end of life).

## FAQs

**Can I increase the oC trip threshold?** No. It is a hardware-level latch in the gate-drive ASIC, not a software parameter. The L3 series parameters set the *current limit* during acceleration (which slows the ramp), but the absolute oC trip is fixed.

**Will a line reactor help oC trips?** A line reactor (input-side) won't help oC, which is an output-side fault. An **output reactor** or dv/dt filter does help — especially on motor cable runs over 50 meters. The reactor slows the IGBT rise time and reduces reflected wave spikes that contribute to oC at the motor terminals.

**Why does my GA800 trip oC during regenerative deceleration?** Almost always a wiring issue or a load that's actively driving the motor backward (gravity load, web tension). Check B2-01 (DC Injection Braking start frequency) and confirm a dynamic braking resistor is connected and sized per the technical manual TOEPC71061800F appendix C.

**Difference between oC and SC fault?** SC (Short Circuit) is the desaturation-detect fault — IGBT cannot turn off cleanly due to a downstream short. oC is the overcurrent magnitude trip. SC almost always means hard hardware failure or a dead short; oC can be a recipe or load problem.

**Should I increase carrier frequency C6-02 to reduce motor current?** Higher carrier reduces motor losses and audible noise but *increases* drive losses and can push you closer to oC on long cable runs due to higher reflected-wave amplitude. On GA800, the default carrier is fine for 95% of applications. Leave it.

## Related guides

- [Yaskawa GA800 oV Fault — DC Overvoltage Fix](/yaskawa-ga800-error-ov/)
- [Yaskawa GA800 Uv1 Fault — DC Undervoltage Fix](/yaskawa-ga800-error-uv1/)
- [Allen-Bradley PowerFlex F004 Fault — Undervoltage Fix](/allen-bradley-powerflex-f004-fault/)
- [Allen-Bradley PowerFlex F012 Fault — HW Overcurrent Fix](/allen-bradley-powerflex-f012-fault/)
- [ABB ACS580 Fault 2310 — Overcurrent Fix](/abb-acs580-2310-fault/)
