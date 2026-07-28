---
title: "Mori Seiki CNC Fault Codes — Complete Troubleshooting Guide"
description: "Mori Seiki and DMG Mori CNC fault codes for NL, NX, NHX, and DMU series. What each code means and how to fix it."
pubDatetime: 2026-04-27T22:00:00Z
modDatetime: 2026-04-27T22:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - cnc
  - mori-seiki
money_part: "Servo amplifier"
---

Mori Seiki and DMG Mori machines use a layered alarm structure. The MAPPS or MSX operator interface sits on top of a Fanuc, Mitsubishi, or Siemens CNC core, and the machine ladder adds Mori-specific PMC and EX alarms for tool change, spindle orientation, pallet handling, turret indexing, and safety interlocks. That stack is why one fault can show up as a Mori alarm on the MAPPS screen, a Fanuc alarm in the CNC diagnostic page, and a drive alarm in the servo or spindle amplifier.

This guide covers the Mori-specific alarm conditions most shops actually see on NL lathes, NX vertical machining centers, NHX horizontals, and DMU 5-axis machines. It focuses on servo, spindle, turret, steady rest, parts catcher, coolant, and MAPPS communication faults, with practical recovery steps you can use on the machine.

## How to Read Mori Seiki Alarms

On MAPPS and MSX controls, alarm sources usually fall into four groups:

| Alarm type | Where it comes from | Typical examples |
| --- | --- | --- |
| CNC alarms | Fanuc or Mitsubishi core | 401, 408, 414, 417 |
| Mori EX alarms | Machine ladder and machine builder logic | EX0456, EX1449, EX0069 |
| PMC alarms | Mori I/O and sequence logic | PMC-ALARM 202 |
| MAPPS interface alarms | HMI or communication layer | panel, communication, safe test messages |

Start by identifying which layer raised the alarm. A servo drive fault needs a different workflow than a tool changer sequence timeout.

## Alarm History Access in MAPPS

Use alarm history before you clear anything.

### MAPPS / MSX
1. Press **ALARM** on the hard key or soft key row.
2. Open **History** or **Alarm History**.
3. Filter by **NC**, **PMC**, or **Machine** alarm type.
4. Record the first alarm in sequence, not just the one still active.

### Fanuc-based Mori machines
1. Press **SYSTEM**.
2. Open **Alarm** and **Alarm History**.
3. Check **Diagnostics** for matching bits on the ladder side.

### Mitsubishi-based Mori machines
1. Open **Diagnosis** or **Alarm Diagnosis** from the MAPPS maintenance page.
2. Check amplifier status and axis-specific subcodes.

If you clear alarms before recording them, you often lose the sequence that explains the fault.

## Clearing and Recovery Procedure

1. Fix the missing condition first.
2. Reset E-stop and safety chain.
3. Clear the CNC or servo alarm.
4. Return the machine to reference position if required.
5. Use the MAPPS recovery screen for ATC, APC, steady rest, or parts catcher recovery.

Do not force a tool change or turret index while spindle orientation, clamp confirmation, or axis readiness is still missing. That is how minor faults turn into broken dogs, bent forks, and damaged proximity switches.

## Common Mori Seiki Fault Codes

### Alarm 401, Servo Alarm

**Meaning:** A servo amplifier reported a fault. This is a wrapper alarm. The real failure sits underneath it in the drive or axis diagnostics.

**Common causes:**
1. Axis crash or hard mechanical binding
2. Encoder cable oil intrusion or loose connector
3. Servo amplifier overheating
4. Lubrication failure on ballscrew or guideways

**Diagnosis steps:**
1. Identify the affected axis on the alarm detail page.
2. Open drive diagnostics and read the servo subcode.
3. Inspect axis for chips packed in covers, damaged wipers, or seized way lube lines.
4. Reseat motor power and encoder connectors in the cabinet and at the motor.

**Fix:**
- Free the mechanical bind first.
- Restore lubrication.
- Repair or replace damaged encoder cable.
- If the alarm follows the amplifier when swapped, the amplifier is failing.

### Alarm 414, Servo Not Ready

**Meaning:** The servo enable chain is not complete. Drives will not come ready, so all motion stays locked out.

**Common causes:**
1. E-stop or door interlock still open
2. Cabinet contactor not pulling in
3. Power supply or control transformer fault
4. Active drive alarm still present on one axis

**Diagnosis steps:**
1. Check safety chain first. Door switch, E-stop, hydraulic ready, and air pressure must all be true.
2. Confirm main contactor pulled in after power-up.
3. Verify control voltage and incoming three-phase power.
4. Check whether one drive shows a fault and blocks the rest of the system.

**Fix:**
- Restore the open interlock.
- Replace weak contactors or power supplies.
- Clear the underlying drive fault, then reset the machine.

### Alarm 417, Servo Communication Fault

**Meaning:** Communication between the CNC and servo amplifier dropped out.

**Common causes:**
1. Aging amplifier module
2. Loose communication cable or fiber connection
3. Noise or grounding issue in cabinet
4. Low control voltage during machine start

**Diagnosis steps:**
1. Inspect communication cable connections at CNC and amplifier.
2. Check shielding and grounding continuity.
3. Look for repeat faults during spindle acceleration or coolant pump start, which often points to voltage sag or noise.
4. If the alarm follows one amplifier module, replace or repair that module.

**Fix:**
- Reseat connectors.
- Repair shield or ground faults.
- Replace failing amplifier if fault follows the unit.

### Alarm 408, Spindle Overload

**Meaning:** Spindle load exceeded the machine's allowable threshold.

**Common causes:**
1. Dull or chipped tool
2. Spindle bearing wear
3. Excessive feed or depth of cut
4. Poor lubrication on gearbox or spindle chiller fault

**Diagnosis steps:**
1. Review spindle load history if available.
2. Check tool and holder first.
3. Listen for bearing noise during warm-up and at constant RPM.
4. Verify spindle chiller flow and temperature.

**Fix:**
- Replace damaged tooling.
- Reduce cutting load.
- Service spindle chiller or lubrication system.
- Escalate for bearing inspection if load keeps rising on the same program.

### EX0453, Mill Spindle Alarm

**Meaning:** Mori machine ladder detected a spindle amplifier or spindle-ready fault.

**Common causes:**
1. Spindle drive alarm active
2. Spindle orientation not complete
3. Cooling fan or chiller issue at spindle drive
4. Loose spindle feedback cable

**Fix steps:**
1. Open spindle amplifier diagnostics and read the underlying drive code.
2. Confirm spindle ready and orientation complete bits in I/O diagnostics.
3. Check spindle drive cooling and cabinet temperature.
4. Test spindle at low RPM and orientation in maintenance mode.

### EX0456, Spindle Index Time Up

**Meaning:** The spindle failed to orient within the allowed time. This blocks tool change and many pallet operations.

**Common causes:**
1. Orientation encoder or sensor fault
2. Loose coupling or belt slip
3. Spindle brake drag or mechanical resistance
4. Parameter drift after spindle service

**Diagnosis steps:**
1. Run M19 orientation test in maintenance mode several times.
2. Watch for repeatable position error or random failure.
3. Inspect encoder cable and connector for oil ingress.
4. Check spindle brake release and air pressure where fitted.

**Fix:**
- Repair encoder or cable faults.
- Re-tension or replace worn belts and couplings.
- Adjust spindle orientation parameters only after mechanical checks are complete.

### PMC-ALARM 202, Commanded Tool in Spindle

**Meaning:** The ladder received a tool-change command for the tool already in the spindle. Mori logic treats this as a conflict on many machines.

**Common causes:**
1. Tool change macro does not bypass same-tool calls
2. Tool table mismatch between current tool and magazine position
3. Corrupt spindle tool tracking variable

**Diagnosis steps:**
1. Confirm the actual tool in spindle and the commanded T code.
2. Check tool magazine table and current tool tracking variable.
3. Review the tool change macro if the machine uses one.

**Fix:**
- Correct the tool table.
- Edit the tool-change macro to skip M6 when the requested tool is already in the spindle.
- Re-home the magazine if pocket tracking is off.

### EX1449, Sensing Tool in Spindle

**Meaning:** The machine still sees a tool in spindle during a tool change sequence that expects the spindle to be empty or in a different state.

**Common causes:**
1. Tool clamp unclamp sensor failure
2. Drawbar not releasing fully
3. Chips on pull stud or spindle taper
4. Tool detection sensor out of adjustment

**Fix steps:**
1. Clean spindle taper and toolholder.
2. Verify unclamp air pressure under load.
3. Check tool-in-spindle sensor bit on I/O screen.
4. Inspect drawbar force if problem repeats with multiple holders.

### EX0207, T-Code Not Commanded

**Meaning:** Mori ladder rejected the tool call. The requested tool is missing, unmapped, or not valid for the machine state.

**Common causes:**
1. Pocket mapping error
2. Invalid tool number for current magazine configuration
3. Tool preselect logic out of sync after recovery

**Fix:**
- Reconcile tool table to actual magazine pockets.
- Re-home the tool magazine.
- Re-run tool recovery sequence from the MAPPS maintenance page.

### Turret Clamp or Index Fault, NL and SL Series

These often appear as machine text alarms rather than one universal number.

**Typical messages:**
- TURRET NOT CLAMPED
- TURRET INDEX TIME OVER
- TURRET POSITION ERROR

**Common causes:**
1. Hydraulic pressure low during clamp or unclamp
2. Turret curvic coupling contaminated with chips
3. Index confirmation proximity switch out of position
4. Solenoid valve sticking

**Diagnosis steps:**
1. Check hydraulic pressure during turret motion, not just idle pressure.
2. Verify clamp and unclamp confirmation bits in diagnostics.
3. Inspect turret face for chips or crash damage.
4. Listen for delayed solenoid actuation.

**Fix:**
- Restore hydraulic pressure.
- Clean turret coupling surfaces.
- Replace or adjust proximity switches.
- Replace sticky solenoid valves.

### Steady Rest Fault

**Typical messages:**
- STEADY REST NOT OPEN
- STEADY REST NOT CLOSED
- STEADY REST POSITION ERROR

**Common causes:**
1. Air cylinder or hydraulic cylinder not completing stroke
2. Open and closed limit switches disagree
3. Mechanical drag from contamination or bent arm

**Fix steps:**
1. Check air or hydraulic supply while actuating the steady rest.
2. Watch open and closed confirmation bits on the I/O page.
3. Clean guide surfaces and inspect for bent hardware after crashes.

### Parts Catcher Fault

**Typical messages:**
- PARTS CATCHER NOT IN POSITION
- PARTS CATCHER UP LIMIT OFF
- PARTS CATCHER DOWN LIMIT OFF

**Common causes:**
1. Failed limit switch or prox sensor
2. Cylinder not stroking due to low air pressure
3. Chip buildup at pivot or stop block

**Fix steps:**
1. Cycle the parts catcher in maintenance mode.
2. Confirm sensor transitions on the I/O page.
3. Clean pivot area and stop surfaces.
4. Repair air leaks or replace weak cylinder.

### Coolant Fault

**Typical messages:**
- COOLANT PRESSURE LOW
- COOLANT PUMP OVERLOAD
- THROUGH SPINDLE COOLANT NOT READY

**Common causes:**
1. Clogged coolant intake or chip basket
2. Pump overload relay trip
3. Through-spindle coolant seal leak or pressure switch issue

**Fix steps:**
1. Clean chip basket and coolant intake screen.
2. Reset and test pump overload relay.
3. Verify coolant pressure switch state and pump current.
4. For through-spindle coolant, check rotary union leakage and filter condition.

### EX0069, Door Lock Time Over

**Meaning:** The door-lock confirmation did not arrive in time.

**Common causes:**
1. Door lock solenoid weak
2. Mechanical drag in lock linkage
3. Lock confirmation switch out of adjustment

**Fix:**
- Check lock output and confirmation input on diagnostics.
- Adjust or replace the switch.
- Service lock linkage.

### Alarm 3000, Emergency Stop Active

**Meaning:** Safety chain is open. This is not always a pressed E-stop button.

**Common causes:**
1. Door interlock open
2. Safety relay dropped out
3. Broken wiring in E-stop loop
4. Hydraulic or pneumatic ready interlock missing

**Fix:**
- Trace the safety chain from the relay outward.
- Confirm each interlock changes state correctly.
- Replace weak safety relays or broken wiring.

## MAPPS Communication and Panel Faults

### EX0098, Panel Test Mode

The machine thinks the panel is in test mode or the mode-select circuit is invalid.

**Check:** operator panel cable, mode selector switch, and panel PCB supply voltage.

### EX0099, Panel Alarm

General panel or operator interface fault.

**Check:** panel power supply, ribbon cables, and HMI board temperature.

### EX5005, Please Execute Safe Test

The safety validation sequence has not completed after startup, service, or maintenance.

**Fix:** run the required MAPPS safety test sequence from maintenance mode before trying motion or spindle functions.

## Parts Reference Table

| Part | Typical application | What to verify before ordering |
| --- | --- | --- |
| Servo amplifier | NL, NX, NHX, DMU axes | Axis designation, drive family, firmware |
| Spindle amplifier | Main spindle or milling spindle | Motor type, voltage, cooling method |
| Turret index prox switch | NL and SL lathes | Sensor style, bracket orientation, cable length |
| Tool-in-spindle sensor | ATC and spindle clamp logic | Mounting thread and connector type |
| Spindle encoder | Orientation and rigid tapping | Shaft size, connector type, pulses per rev |
| Drawbar or clamp sensor | Tool retention monitoring | Open or closed logic, bracket style |
| Door lock switch or solenoid | Guard interlock systems | Voltage, travel, mounting pattern |
| Parts catcher cylinder | Turning centers | Bore, stroke, magnetic piston sensor style |
| Coolant pressure switch | Through-spindle coolant and flood coolant | Pressure range and connector thread |

## What to Check First on Mori Machines

When a Mori Seiki throws repeated machine alarms, start with the basics:
1. Air pressure under motion
2. Hydraulic pressure during clamp or index
3. Sensor feedback on the I/O screen
4. Spindle orientation repeatability
5. Tool table and recovery state after interrupted tool changes

Most recurring Mori faults come from pressure stability, dirty sensors, worn cables, and sequence recovery problems. Shops lose time when they replace boards before checking whether the machine ever received the confirmation bit it was waiting for.

## Where to Buy Replacement Parts

Find replacement parts for Mori Seiki (DMG Mori) CNC machines on Amazon:

- [Mori Seiki DMG CNC Machine Parts](https://www.amazon.com/s?ascsubtag=ecf-mori-seiki-cnc-fault-codes&k=Mori+Seiki+CNC+machine+parts&tag=errorcodefixes-20)
- [Fanuc CNC Battery & Control Parts](https://www.amazon.com/s?ascsubtag=ecf-mori-seiki-cnc-fault-codes&k=Fanuc+CNC+control+battery+replacement&tag=errorcodefixes-20)
- [CNC Way Lube Oil Pump Replacement](https://www.amazon.com/s?ascsubtag=ecf-mori-seiki-cnc-fault-codes&k=CNC+way+lube+oil+pump+replacement&tag=errorcodefixes-20)
