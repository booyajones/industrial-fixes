---
title: "WEG CFW11 Fault Codes - What It Means and How to Fix It"
description: "WEG CFW11 drives use fault and alarm codes to flag power, current, temperature, feedback, and communication problems. This guide explains the most common codes and the checks technicians use to clear them."
pubDatetime: 2026-04-25T00:00:00Z
author: errorcodefixes.com
tags:
  - hvac
  - error-codes
---

The WEG CFW11 is one of the most common variable frequency drives in industrial plants, pumping skids, fan arrays, and OEM equipment. If you work around motors long enough, you will see one. When a CFW11 trips, the display gives you an F-code for a fault or an A-code for an alarm. The drive is telling you exactly where to start.

This guide gives you a field-first approach. It focuses on the codes technicians actually burn time on: undervoltage, overvoltage, overcurrent, overtemperature, ground fault, communication failure, and encoder trouble. It also explains how to think about the larger code ranges so you can move faster even when your exact code is not listed on the door of the panel.

## What Does a WEG CFW11 Fault Code Mean?

On a CFW11, a **fault code** usually appears as **Fxxx**. A fault trips the drive and stops the motor. An **alarm code** appears as **Axxx**. An alarm warns you that the drive has detected an abnormal condition, but the drive may keep running depending on configuration.

In practice, the codes break into six big families:

1. **Power quality faults** such as undervoltage and overvoltage
2. **Motor current faults** such as overcurrent, short circuit, and overload
3. **Thermal faults** in the drive heat sink, IGBTs, or motor model
4. **Feedback faults** such as encoder loss or speed mismatch
5. **Communication faults** on Modbus, CANopen, Profibus, EtherNet/IP, or option cards
6. **Parameter and hardware faults** caused by bad programming, failed boards, or memory problems

If you do not have the exact manual in front of you, start with the code family first. A CFW11 that shows F002 wants a different diagnosis path than one showing A128.

## How to Fix It

### Step 1: Separate faults from alarms

If the display starts with **F**, the drive tripped and stopped. If it starts with **A**, the drive is warning you. That changes your urgency and your reset strategy. Do not keep hammering RESET until you know what failed. Repeated restarts can destroy a motor, trip upstream breakers, or turn a minor insulation fault into a dead short.

### Step 2: Check the three basics first

Before chasing parameters, check the three things that solve the most calls:

1. **Input voltage** at L1/L2/L3
2. **Output wiring** from the drive to the motor
3. **Cooling path** through the drive heat sink and cabinet

If line voltage is low, phase-to-phase is imbalanced, the motor leads are nicked, or the drive is packed with dust, the fancy diagnostics will not save you time.

### Step 3: Common CFW11 F-codes and what they mean

#### F002 / undervoltage

This is one of the most common nuisance trips on lightly maintained systems. The DC bus dropped below the safe operating threshold.

**Typical causes**
1. Low incoming utility voltage
2. Loose line terminals at contactor, breaker, or drive input
3. Single phasing upstream
4. A transformer tap set incorrectly
5. Large motor load starting on the same feeder

**What to do**
1. Measure line-to-line voltage at the drive input while the system is trying to run
2. Compare all three phases. A 3–5% imbalance is already a problem
3. Check fuse clips, disconnect lugs, and line reactor terminals for heat discoloration
4. Tighten terminals to the WEG torque spec on the nameplate/manual
5. If the drive trips only during heavy load transitions, check feeder sizing and upstream voltage sag

#### F003 / overvoltage

The DC bus rose too high. You see this on high inertia loads that regenerate energy during deceleration, like large fans with aggressive stop ramps.

**Typical causes**
1. Deceleration time set too short
2. No braking resistor where one is required
3. Utility voltage too high
4. Regen energy from overhauling load

**What to do**
1. Increase decel time and retest
2. Check whether the application needs a dynamic braking resistor
3. Verify mains voltage is inside drive limits
4. Look for repeated trips during stop, not start. That points to regeneration

#### F004 / overcurrent

The drive saw current above its safe threshold. This is a high-risk trip because it can point to a real short.

**Typical causes**
1. Short circuit or insulation damage in motor leads
2. Mechanical jam in the driven load
3. Acceleration ramp too aggressive
4. Incorrect motor nameplate parameters
5. Output reactor missing on long motor lead run

**What to do**
1. Meg the motor and leads if plant policy allows
2. Disconnect the motor from the driven load and check if it turns freely
3. Compare motor FLA, voltage, base frequency, and RPM parameters to the nameplate
4. Increase accel time and retest
5. If leads exceed about 100 feet, check WEG guidance for dv/dt filter or output reactor

#### F005 / ground fault

Current is leaking from the drive output to ground. This often points to motor insulation breakdown or damaged cable.

**What to do**
1. Lock out power
2. Inspect motor leads at the drive, motor peckerhead, and conduit entries
3. Test insulation to ground on each phase
4. If the motor tests clean, inspect the drive output section for contamination or failed power module

#### F007 / heat sink overtemperature

The drive got too hot. In dirty electrical rooms, this shows up constantly.

**Typical causes**
1. Cooling fan failure
2. Blocked air path through heat sink fins
3. High ambient cabinet temperature
4. Drive undersized for the load
5. Carrier frequency set too high for the application

**What to do**
1. Check internal fan operation
2. Blow out the heat sink with dry compressed air
3. Verify panel ventilation and filter condition
4. Reduce carrier frequency if the application allows it
5. Compare actual motor current to drive size. A drive running at 95% load in a hot cabinet will trip

#### F014 / motor overload or electronic thermal model trip

The drive model believes the motor has exceeded its thermal capacity.

**What to do**
1. Check the programmed motor current against nameplate FLA
2. Verify service factor assumptions
3. Check for overloading in the driven equipment, especially pumps with blocked discharge or fans with damper issues
4. Review repeated starts per hour

#### F033 / encoder feedback loss

This shows up in closed-loop or vector applications. The drive lost encoder signal integrity.

**Typical causes**
1. Broken encoder cable
2. Loose shield termination
3. Failed encoder power supply
4. Noise from VFD output routed too close to feedback cable

**What to do**
1. Check 5 VDC or 12 VDC supply to the encoder, depending on model
2. Inspect shield grounding at one end only, per WEG practice
3. Separate encoder cable from motor leads
4. If pulses are missing on one channel, replace encoder

### Step 4: Common CFW11 A-codes and what they mean

The A-codes vary by firmware and option card, but the pattern stays consistent.

#### A001 to A010 range

These alarms usually point to setup and operating limits. Examples include command source mismatch, reference source problems, or pre-fault states before a full trip.

**What to do**
1. Verify run command source
2. Verify speed reference source
3. Check digital input logic and parameter mapping

#### A050 to A090 range

These usually involve communication warnings, thermal warnings, and optional accessory states.

**Field rule:** if you see an alarm in this range and the drive is still running, capture the operating condition before it becomes a fault. Trend voltage, current, bus voltage, and heat sink temp.

#### A128 and other communication alarms

These often show up when a PLC or BAS loses control of the drive over a fieldbus network.

**What to do**
1. Check network LEDs on the option card
2. Confirm baud rate, node ID, IP settings, or termination resistors as applicable
3. Verify that the PLC still sees the drive online
4. Check for duplicate node address

### Step 5: Understand the F001-F090 and A001-A090 ranges

WEG uses the code families consistently even when firmware revisions change exact descriptions.

- **F001-F010** usually involve power input, DC bus, and basic output protection
- **F011-F030** usually involve motor model, current, thermal, or hardware protection
- **F031-F060** often include feedback, parameter, memory, and communication option faults
- **F061-F090** often involve specific accessory cards, special modes, or hardware-specific failures

For alarms:

- **A001-A020** usually relate to commands, references, and warning thresholds
- **A021-A050** usually map to thermal, overload, or soft-limit warnings
- **A051-A090** often map to communication, accessory, and process-specific warning states

That means you can work faster even before you find the exact manual page.

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|--------------|
| [WEG CFW11 cooling fan replacement](https://www.amazon.com/s?k=WEG+CFW11+cooling+fan&tag=errorcodefixes-20) | Failed internal fan causes heat sink overtemperature trips like F007 | $25–$60 |
| [3-phase line reactor for VFD](https://www.amazon.com/s?k=3+phase+line+reactor+vfd&tag=errorcodefixes-20) | Helps with undervoltage nuisance trips, line spikes, and input harmonics | $90–$220 |
| [Dynamic braking resistor for VFD](https://www.amazon.com/s?k=dynamic+braking+resistor+vfd&tag=errorcodefixes-20) | Needed when F003 overvoltage happens during deceleration on high inertia loads | $80–$250 |
| [Incremental encoder 1024 PPR industrial](https://www.amazon.com/s?k=incremental+encoder+1024+ppr+industrial&tag=errorcodefixes-20) | Replaces failed feedback device when encoder-related trips occur | $65–$180 |
| [VFD output reactor 3-phase](https://www.amazon.com/s?k=vfd+output+reactor+3+phase&tag=errorcodefixes-20) | Protects motor insulation on long lead runs and reduces overcurrent trips | $110–$280 |
| [Cat6 shielded industrial Ethernet cable](https://www.amazon.com/s?k=shielded+industrial+ethernet+cable&tag=errorcodefixes-20) | Fixes intermittent fieldbus or Ethernet communication alarms from noisy wiring | $18–$45 |

## When to Call a Pro

Call a drive technician or industrial electrician when:

1. The drive trips on overcurrent or ground fault the moment you hit RUN
2. Insulation resistance on the motor is low
3. The DC bus trips on overvoltage and the application needs braking hardware
4. You suspect a failed IGBT power module or control board
5. The system is part of a critical process and you cannot afford blind resets

If the drive controls a fan wall, pump skid, compressor, or HVAC air handler in a live building, capture the parameter backup before anyone swaps hardware. That one step saves hours.

## Frequently Asked Questions

**Q: What is the difference between an F-code and an A-code on a WEG CFW11?**

An F-code is a trip. The drive stops the motor and waits for a reset. An A-code is a warning. The drive is telling you a limit is close or a supporting system is unhappy, but the motor may still run.

**Q: Why does my CFW11 trip on overvoltage only when the motor stops?**

The load is regenerating back into the DC bus during deceleration. Increase decel time first. If the load still throws F003, you likely need a braking resistor or a different stopping strategy.

**Q: Can bad motor parameters cause nuisance trips?**

Yes. Wrong nameplate voltage, current, frequency, or RPM settings can trigger overcurrent, overload, unstable vector control, and poor torque response. Always compare programmed values to the motor nameplate after a board swap or parameter reset.

**Q: Do I need a megger to diagnose a ground fault?**

For a real ground fault diagnosis, yes. A standard multimeter misses insulation problems that only show up under higher test voltage. If plant policy allows it, use an insulation resistance tester on the motor and leads before condemning the drive.
