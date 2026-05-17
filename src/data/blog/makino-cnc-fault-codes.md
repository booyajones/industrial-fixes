---
title: "Makino CNC Fault Codes — Complete Troubleshooting Guide"
description: "Makino CNC fault codes for a51, a61, D500, F5, and V56 series. What each code means and how to fix it."
pubDatetime: 2026-04-27T21:00:00Z
modDatetime: 2026-04-27T21:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - cnc
  - makino
---

Makino machining centers throw alarms from three layers at once. You may see a **Makino PMC alarm**, a **Fanuc or Mitsubishi servo/spindle alarm**, and a **Makino Pro message** on the same stop. If you clear the wrong layer first, the machine just faults again. This guide covers the alarm families maintenance techs see most on **a51**, **a61**, **D500**, **F5**, and **V56** machines, with the alarm number, what it means, what usually causes it, and how to recover without making the problem worse.

## Jump to Section

- [How Makino alarms are structured](#how-makino-alarms-are-structured)
- [How to access alarm history](#how-to-access-alarm-history)
- [Servo alarm 401](#servo-alarm-401)
- [Servo alarm 414](#servo-alarm-414)
- [Servo alarm 417](#servo-alarm-417)
- [Spindle alarm 12](#spindle-alarm-12)
- [ATC and tool magazine faults](#atc-and-tool-magazine-faults)
- [APC and pallet changer faults](#apc-and-pallet-changer-faults)
- [Makino PMC oil and support system alarms](#makino-pmc-oil-and-support-system-alarms)
- [Coolant and lube faults](#coolant-and-lube-faults)
- [Axis overtravel faults](#axis-overtravel-faults)
- [Common Makino PMC alarm table](#common-makino-pmc-alarm-table)
- [Parts reference table](#parts-reference-table)

---

## How Makino alarms are structured

Most Makino machines in this range use **Makino Professional 5 or Professional 6** on top of a **Fanuc** or **Mitsubishi** CNC platform.

That means an alarm can come from:

1. **Servo or spindle drive layer**  
   These are the Fanuc or Mitsubishi alarms such as **401 Servo Alarm**, **414 Servo Not Ready**, **417 Servo Disconnected**, or spindle amplifier alarms.

2. **Makino PLC / PMC layer**  
   These are machine-built sequence alarms for the tool changer, pallet changer, lube system, hydraulics, coolant, guards, and other machine functions. These alarms often use five-digit numbers such as **13035**, **13063**, or **13207**.

3. **Makino Pro operator layer**  
   These messages point you to the sequence that failed. They usually tell you which confirmation never arrived, for example pallet seated, clamp complete, shutter open, spindle oriented, or arm home.

The fastest rule on Makino is simple: **do not treat every alarm like an electrical problem**. On these machines, contamination, pressure instability, poor sensor feedback, and incomplete sequence conditions cause a high percentage of stoppages.

---

## How to access alarm history

Exact screen names vary by control generation, but the workflow is consistent.

### Makino Professional 5 / 6

1. Open the **Alarm** screen from the operator panel.
2. Review the active alarm list first.
3. Open the **History** or **Log** view to see earlier alarms in sequence order.
4. For tool changer, pallet changer, and utility faults, open the **Maintenance** or **Recovery** screens and watch the related I/O bits while reproducing the fault.
5. For Pro5/Pro6 machines with **ProVis Remote Diagnostics**, you can mirror the control to Makino support for live troubleshooting.

### Fanuc diagnostics on Makino

1. Open the alarm page and note the servo or spindle alarm number.
2. Open the drive diagnostics or detail page to find the affected axis or spindle amplifier.
3. Check the PMC or ladder diagnostics if the alarm is blocking a machine sequence such as ATC or APC.

### Practical rule

If the alarm happened during a tool change or pallet change, go to the Makino recovery or maintenance screen before cycling power. The screen usually shows which confirmation is missing. That saves time and avoids making the sequence position harder to recover.

---

## Servo alarm 401

**Alarm:** Fanuc Servo Alarm 401  
**Meaning:** Servo amplifier or axis fault

### What triggers it

The CNC received a fault signal from a servo amplifier. On Makino this is usually the umbrella alarm. The real cause sits in the axis detail or the amplifier status.

### Common causes in order of frequency

1. Axis mechanical bind or crash load
2. Encoder or feedback cable fault
3. Low or unstable incoming power
4. Contaminated connectors in the cabinet or at the motor
5. Amplifier hardware failure

### Diagnosis steps

1. Identify which axis faulted. Do not stop at the 401 umbrella alarm.
2. Check if the alarm occurred during motion, at power-up, or after a stop. Motion-related faults often point to load or feedback issues.
3. Inspect the axis mechanically. Check ballscrew, linear guides, covers, lube delivery, and signs of collision.
4. Check encoder and motor power connectors for looseness, oil ingress, or pin damage.
5. If multiple axes faulted together, check the incoming three-phase power and cabinet contactors first.

### Reset procedure

Clear the underlying cause, then reset the servo alarm from the control. If 401 returns immediately at power-up, do not keep resetting. You likely have a power, amplifier, or feedback failure.

---

## Servo alarm 414

**Alarm:** Fanuc Servo Alarm 414  
**Meaning:** Servo not ready

### What triggers it

The CNC tried to enable the servo system, but the amplifier did not enter ready state.

### Common causes in order of frequency

1. Safety chain still open after E-stop or guard event
2. Drive power supply not established
3. Cabinet contactor or fuse fault
4. Amplifier internal readiness fault
5. Communication issue inside the drive chain

### Diagnosis steps

1. Confirm all E-stop buttons are released and all interlocks are satisfied.
2. Check the machine ready chain and safety relay status.
3. Verify cabinet contactors pull in and hold.
4. Check amplifier LEDs or diagnostic codes for the affected axis.
5. Measure incoming power at the amplifier and upstream fuse block.

### Reset procedure

Restore the safety and power condition, then power the machine down and back up cleanly. If the amplifier still will not report ready, move to amplifier-level diagnostics.

---

## Servo alarm 417

**Alarm:** Fanuc Servo Alarm 417  
**Meaning:** Servo disconnected or serial communication loss

### What triggers it

The CNC lost communication with the servo amplifier over the serial or fiber link.

### Common causes in order of frequency

1. Loose or damaged communication cable
2. Amplifier module fault
3. Noise or grounding problem in the cabinet
4. Power interruption to one amplifier in the chain
5. Recently disturbed cabling after service work

### Diagnosis steps

1. Power down and reseat communication cables end-to-end.
2. Inspect routing near high-current lines, especially spindle or chiller power wiring.
3. Check grounding and shield terminations.
4. If the fault follows a module swap, suspect the amplifier.
5. If one amplifier loses power, downstream amplifiers may also report link errors. Check the first failed node.

### Reset procedure

Repair the communication or power issue and reboot the machine. If 417 returns on the same node, isolate that amplifier and its cable.

---

## Spindle alarm 12

**Alarm:** Fanuc Spindle Alarm 12  
**Meaning:** Overcurrent in DC link or spindle amplifier current fault

### What triggers it

The spindle amplifier detected abnormally high current in the DC link or power stage during spindle start, orientation, acceleration, or braking.

### Common causes in order of frequency

1. Spindle amplifier degradation
2. Spindle motor lead insulation damage
3. Mechanical spindle drag or bearing failure
4. Crash or heavy cut load spike
5. Cabinet cooling problem causing amplifier stress

### Diagnosis steps

1. Run the spindle at low RPM with no tool load. Listen for bearing noise or drag.
2. Check if the alarm occurs on start, on orient, or during decel. The event point matters.
3. Inspect spindle motor leads and connectors for contamination or insulation damage.
4. Check cabinet filters and fans. Heat drives spindle trips.
5. If orientation fails and ATC faults follow, solve spindle orientation first. Do not force ATC recovery around a spindle problem.

### Reset procedure

Reset after the spindle system cools and after you correct the load, wiring, or amplifier fault. If the spindle trips on every start command, stop and isolate the spindle motor and amplifier.

---

## ATC and tool magazine faults

Makino ATC faults usually stop because a condition did not confirm in time. The machine expected shutter open, pot vertical, arm home, tool clamped, or spindle oriented, and never saw the input.

### Common ATC fault class

**Typical message:** Tool changer sequence timeout, pot not confirmed, arm not home, clamp not confirmed, shutter fault

### Common causes in order of frequency

1. Spindle orientation not achieved
2. Dirty or misaligned proximity sensors
3. Low air pressure under motion
4. Sticky cylinder or worn shock absorber
5. Magazine mechanical bind or chip contamination

### Diagnosis steps

1. Open the ATC maintenance or recovery screen and watch the sensor inputs live.
2. Verify air pressure during an actual ATC attempt, not just static regulator pressure.
3. Clean targets and proximity sensors, then confirm repeatable switching.
4. Check the spindle orientation state before stepping the ATC sequence.
5. Inspect the pot, arm, shutter, and magazine pocket for chips or bent hardware.

### Reset procedure

Use Makino's ATC recovery screen, not brute force. Step the mechanism in the correct direction until the tool changer returns to a known state. Then clear the alarm and verify spindle tool data if the interruption happened mid-cycle.

---

## APC and pallet changer faults

On **a51** and **a61** horizontal machining centers, APC faults are common because the pallet system depends on several clean confirmations happening in sequence.

### Common APC fault class

**Typical message:** Pallet not seated, clamp not complete, APC arm home timeout, receiver not ready

### What triggers it

The pallet sequence timed out waiting for a position, clamp, door, or pressure confirmation.

### Common causes in order of frequency

1. Chip contamination on pallet cones or locating faces
2. Clamp sensor not switching reliably
3. Hydraulic or pneumatic pressure below threshold under load
4. Axes or spindle not in safe condition when APC started
5. Receiver, arm, or shuttle mechanism binding

### Diagnosis steps

1. Confirm all prerequisites, spindle stopped, axes safe, doors/interlocks satisfied.
2. Clean pallet locating surfaces, cones, receivers, and clamp faces thoroughly.
3. Watch clamp and seat sensors on the I/O page while cycling the pallet mechanism.
4. Check hydraulic or pneumatic pressure while clamping, not just at idle.
5. Inspect clamp cylinders, sensors, and targets for wear or looseness.

### Reset procedure

Recover the APC from the Makino maintenance screen. Do not force pallet clamp with contamination still present. The machine will come back to the same fault.

---

## Makino PMC oil and support system alarms

Makino maintenance manuals include real PMC alarm lists for support systems. The V55 manual's oil controller section includes these alarms:

### Alarm 13035

**Message:** FLOW QUANTITY OF SPINDLE LUBRICANT IS ABNORMAL  
**Meaning:** The spindle lube flow rate is outside the expected range.

**Common causes:**
1. Restricted lube line
2. Air in the lube circuit
3. Failing metering unit
4. Pump problem

**Diagnosis:**
Check lube pump output, inspect the metering units, and verify the flow sensor changes state during a lube cycle.

### Alarm 13063 / 13064 / 13205

**Message:** OILMATIC FILTER IS CLOGGED  
**Meaning:** The oil controller filter differential has reached the warning or alarm threshold.

**Common causes:**
1. Dirty filter element
2. Contaminated oil supply
3. Pump working against restriction

**Diagnosis:**
Replace the filter, inspect oil condition, and confirm pressure returns to normal after service.

### Alarm 13086

**Message:** COOLANT LEVEL IS TOO LOW  
**Meaning:** Coolant tank level sensor is below minimum.

**Common causes:**
1. Low tank level
2. Level switch fault
3. Excessive leak or washdown loss

### Alarm 13093

**Message:** SPINDLE LUBRICANT FLOW SENSOR ABNORMAL  
**Meaning:** Flow switch or sensor feedback is invalid.

**Common causes:**
1. Failed flow sensor
2. Wiring fault
3. No real lubricant flow

### Alarm 13201

**Message:** SPNDL OILMATIC THERMAL IS TRIPPED  
**Meaning:** The oil controller thermal overload has tripped.

**Common causes:**
1. Pump motor overload
2. Jammed pump
3. Wrong voltage or single-phasing

### Alarm 13204

**Message:** OILMATIC ALARM  
**Meaning:** General oil controller alarm. Check the oil controller panel for the specific subcondition.

### Alarm 13207

**Message:** COMMUNICATION WITH OILMATIC IS ILLEGAL  
**Meaning:** Communication with the oil controller failed.

**Common causes:**
1. Controller power loss
2. Communication cable fault
3. Oil controller board failure

### Reset procedure for PMC support alarms

Fix the support-system fault, then reset from the Makino control. For overloads, correct the cause before resetting breakers or thermal relays.

---

## Coolant and lube faults

Makino coolant faults often look simple, but a low coolant or lube alarm can block spindle warm-up, ATC sequence, or prolonged cycle operation.

### Common causes in order of frequency

1. Low coolant or lube level
2. Pump overload trip
3. Clogged strainers or filters
4. Failed flow or level sensor
5. Wiring fault to support equipment

### Diagnosis steps

1. Check reservoir level first.
2. Reset and test the pump overload only after checking for a mechanical jam.
3. Clean strainers and replace filters.
4. Verify sensor state on the I/O page and at the device.
5. Inspect support equipment panel alarms before assuming the CNC is the source.

---

## Axis overtravel faults

**Alarm class:** Axis overtravel, positive or negative limit

### What triggers it

An axis hit the hardware limit switch or exceeded a soft travel limit.

### Common causes in order of frequency

1. Wrong work offset or program zero
2. Machine not referenced after power-up
3. Tool or fixture interference forcing unexpected stop
4. Failed or misadjusted limit switch
5. Servo following error after collision

### Diagnosis steps

1. Confirm the machine is referenced.
2. Jog the axis off the limit in the safe direction.
3. Check work offsets and active program coordinates.
4. Inspect the limit switch and actuator dog.
5. If the overtravel followed a crash, inspect the axis mechanically before resetting.

### Reset procedure

Move off the limit, re-reference if needed, and clear the alarm. If the axis cannot move cleanly, stop and inspect the mechanics before trying recovery again.

---

## Common Makino PMC alarm table

| Alarm | Description | Primary action |
|------|-------------|----------------|
| 13035 | Flow quantity of spindle lubricant is abnormal | Check lube flow, pump, metering units |
| 13063 | Oilmatic filter is clogged | Replace filter, inspect oil condition |
| 13064 | Oilmatic filter is clogged warning | Service filter before it becomes a hard stop |
| 13086 | Coolant level is too low | Refill tank, check level switch |
| 13093 | Spindle lubricant flow sensor abnormal | Check sensor and actual lube flow |
| 13201 | Spindle Oilmatic thermal is tripped | Check pump overload and power supply |
| 13204 | Oilmatic alarm | Inspect oil controller panel for detail |
| 13205 | Oilmatic filter clogged warning | Replace filter and confirm pressure |
| 13207 | Communication with Oilmatic is illegal | Check controller power and comm wiring |
| 30087 | Stop after M02 due to Oilmatic clog alarm | Service oil controller before restart |
| 30088 | Stop after M30 due to Oilmatic clog alarm | Service oil controller before restart |
| 30089 | Stop after M06 due to Oilmatic clog alarm | Service oil controller before next tool change |
| 401 | Servo alarm | Open axis detail and inspect load/feedback |
| 414 | Servo not ready | Check safety chain and drive power |
| 417 | Servo disconnected | Check serial/fiber communication chain |
| 12 | Spindle overcurrent in DC link | Inspect spindle motor, drive, cooling |
| APC timeout | Pallet sequence did not complete | Check contamination, sensors, clamp pressure |
| ATC timeout | Tool change confirmation missing | Check orientation, air pressure, sensor state |

---

## Parts reference table

| Part | Application | Notes |
|------|-------------|-------|
| Servo amplifier module | Axis drive system | Match by control generation and axis rating |
| Spindle amplifier | Spindle drive system | Order by machine serial and spindle option |
| Spindle encoder / orientation feedback | ATC and spindle orientation faults | Feedback failure often blocks tool change |
| APC clamp proximity sensor | a51 / a61 pallet systems | Verify target gap and mounting rigidity |
| APC hydraulic or pneumatic pressure switch | Pallet clamp confirmation | Check under load, not only static |
| ATC shutter sensor | Tool changer sequence | Common contamination failure point |
| ATC arm home sensor | Tool changer sequence | Check alignment after any jam |
| Tool clamp / unclamp sensor | Spindle drawbar confirmation | Essential for recovery after interrupted tool change |
| Lube flow sensor | V-series and D-series support systems | Used in alarms 13035 and 13093 |
| Oilmatic filter element | Oil controller | Replace on clog alarms |
| Coolant level switch | Coolant support system | Check float movement and wiring |
| Cabinet cooling fan / filter | Servo and spindle cabinet | Heat causes recurring drive faults |

Always order Makino parts by machine serial number and control generation. The same model family may use different drive and sensor hardware across production years.

---

## Technician notes

- On Makino, a sequence fault usually means the machine missed a condition, not that the PLC logic failed.
- Cleanliness matters. Chip contamination on pallet faces, pot targets, shutters, and sensors causes many repeat alarms.
- Solve spindle orientation before forcing ATC recovery. Orientation faults create downstream tool changer alarms.
- Check pressure and sensor status during motion. Static checks miss a lot of Makino faults.
- If a Pro5 or Pro6 machine supports **ProVis Remote Diagnostics**, use it. Sharing the live control screen with Makino support is often faster than guessing from alarm text alone.

## Where to Buy Replacement Parts

Find replacement parts for Makino CNC machining centers on Amazon:

- [Makino CNC Machine Parts](https://www.amazon.com/s?ascsubtag=ecf-makino-cnc-fault-codes&k=Makino+CNC+machine+parts&tag=errorcodefixes-20)
- [CNC Pallet Changer Sensor & Proximity Switch](https://www.amazon.com/s?ascsubtag=ecf-makino-cnc-fault-codes&k=CNC+pallet+changer+proximity+switch&tag=errorcodefixes-20)
- [CNC Spindle Coolant Through-Spindle Filter](https://www.amazon.com/s?ascsubtag=ecf-makino-cnc-fault-codes&k=CNC+through+spindle+coolant+filter&tag=errorcodefixes-20)