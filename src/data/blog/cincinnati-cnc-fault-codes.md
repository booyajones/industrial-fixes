---
title: "Cincinnati CNC Fault Codes — Complete Troubleshooting Guide"
description: "Cincinnati Milacron and Cincinnati Machine fault codes for Maxim, Arrow, and Sabre series. What each code means and how to fix it."
pubDatetime: 2026-04-27T22:00:00Z
modDatetime: 2026-04-27T22:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - cnc
  - cincinnati
---

Cincinnati Milacron VMCs — the Arrow, Sabre, Maxim, and Dart series — are common fixtures in North American job shops and manufacturing facilities. Most machines from the 1990s through the 2000s run the **Acramatic 2100 or 2100E CNC control**, a PC-based system running on a Windows NT or embedded OS platform. Some earlier machines used the Acramatic 850SX control.

Cincinnati machines use servo drives from multiple vendors depending on the year: Fanuc red-cap servos, Siemens/Indramat drives, or ViCkers/Servostar drives. Alarms can originate from the CNC control itself, from the servo drives, from the Cincinnati PLC ladder (machine-specific alarms), or from peripheral systems (lube, hydraulic, coolant, ATC). This guide covers all four categories.

---

## Jump to Fix

- [How Alarms Work on Acramatic 2100](#how-alarms-work-on-acramatic-2100)
- [Alarm 39-x — Drives Not Ready / Axis Not Ready](#alarm-39-x--drives-not-ready--axis-not-ready)
- [Axis Overtravel Alarms](#axis-overtravel-alarms)
- [Spindle Fault Alarms](#spindle-fault-alarms)
- [ATC / Tool Changer Fault Alarms](#atc--tool-changer-fault-alarms)
- [Lube System Alarms](#lube-system-alarms)
- [Hydraulic System Alarms](#hydraulic-system-alarms)
- [Coolant System Alarms](#coolant-system-alarms)
- [Machine Start Inhibit / E-Stop Conditions](#machine-start-inhibit--e-stop-conditions)
- [Acramatic 850SX Controls](#acramatic-850sx-controls)
- [Accessing Alarm History](#accessing-alarm-history)
- [Cincinnati-Specific Parameter Notes](#cincinnati-specific-parameter-notes)
- [Parts Table](#parts-table)

---

## How Alarms Work on Acramatic 2100

The Acramatic 2100 displays alarms on the CRT/LCD pendant screen as numbered messages in the format **XX** (alarm number) or **XX-Y** (alarm number, axis or subcategory). The alarm text also appears as a plain English description.

**Alarm origin categories:**

| Number Range | Source |
|-------------|--------|
| 1–2256 | CNC control alarms (interpolation, axis, communication) |
| Above 2256 | Machine Builder (MTB) alarms — Cincinnati PLC ladder |

MTB alarms above 2256 are Cincinnati-specific and require the Cincinnati machine maintenance manual for the specific model. The PLC ladder logic on Arrow/Sabre/Maxim machines generates these alarms when machine peripherals (lube, hydraulic, coolant, ATC) report faults to the CNC via M/I signals.

**Understanding the alarm format:**
- `39-6` → Alarm 39, sub-type 6 (Drives not ready, Z axis)
- `18530` → MTB alarm 18530 (axis-level alarm, machine-specific)
- `1025` → MTB alarm 1025 (spindle lube — machine-specific)
- `1066` → MTB alarm 1066 (lube air pressure — machine-specific)

**Servo drive fault codes** appear separately on the servo drive front panel LEDs or 7-segment displays, not on the CNC screen. When an axis goes "not ready," look at the servo drive LED for a specific error code.

---

## Alarm 39-x — Drives Not Ready / Axis Not Ready

**Alarm text:** "DRIVES NOT READY" or "X/Y/Z AXIS NOT READY"

**What it means:** The CNC control expected the servo drive(s) to signal "ready" but did not receive that signal within the timeout period. This is one of the most common alarm types on Arrow and Sabre machines.

**On ViCkers/Servostar drives (common on late-1990s Arrow):**
When this alarm fires, look at the Servostar drive front panel — the alphanumeric display shows a brief error code before returning to "u" (undervoltage/not enabled). Have an assistant push the machine Start button while you watch the drive display — the error code flashes for about 2 seconds.

Common Servostar codes:
- **u** — Drive not enabled (no enable signal present on C3 connector pin 6/7, requires 24V)
- **F** codes — Faults (F01 overcurrent, F02 overvoltage, etc.)
- **1** on X/Z with flashing decimal point — Drive enabled, attempting to initialize
- **1** on Y without decimal point — Drive enabled but missing enable signal detail

**On Fanuc α-series drives:**
Alarm 39 with Fanuc drives typically indicates SV alarms on the servo amplifier. Check the servo amplifier LED:
- **SV401** — Axis not ready (servo ready signal missing)
- **SV004** — Overheat alarm
- **SV421** — Speed feedback error
- **SV430/431** — Encoder feedback error

**Fix steps for Alarm 39:**
1. Check all servo drive front panels for specific drive-level error codes
2. Verify servo cabinet air cooling fan is operating — overheated drives will not enable
3. Check DC bus capacitors are charged: after powering on, wait 60 seconds before pushing machine start
4. Check axis enable signal: on ViCkers drives, 24V DC must be present at C3 connector pin 6 (positive) and 7 (common) for drive to enable. No 24V = control is not issuing enable
5. Check the emergency stop circuit — an active E-stop prevents drive enable
6. Check axis drive enable relay in the control cabinet — relay should close when machine start is pressed
7. If only one axis is not ready, focus on that axis drive and its feedback cable

---

## Axis Overtravel Alarms

**Alarm text:** "X/Y/Z AXIS OVERTRAVEL" or "HARDWARE OVERTRAVEL"

Cincinnati VMCs have two layers of overtravel protection:
1. **Software limits** — CNC prevents motion beyond configured soft limits
2. **Hardware limit switches** — Physical switches at each axis end of travel

**Common alarms:**
- "POSITIVE OVERTRAVEL" or "NEGATIVE OVERTRAVEL" — axis hit a hardware limit switch
- "SOFT LIMIT EXCEEDED" — motion command would exceed software limits

**Fix steps:**
1. Jog the axis away from the limit switch using the MPG (manual pulse generator) or jog keys. On some machines, you must hold a "Limit Override" button while jogging to release a hardware limit condition
2. Check for crashed tooling or fixture fouling the axis travel
3. On Acramatic 2100: check that the machine zero/home position is correctly set after a crash — if the machine lost position, soft limits may be wrong
4. Re-home all axes (press Reference Point button) after any drive power cycle or battery-backed RAM issue
5. If the machine repeatedly overtravel in one direction, check encoder cable for intermittent connection — encoder losing pulses causes the control to think the axis is in a different position than it actually is

---

## Spindle Fault Alarms

**Common spindle alarm formats:**
- `SPINDLE NOT READY`
- `SPINDLE FAULT` or `SPINDLE DRIVE FAULT`
- `SPINDLE OVERHEAT` (MTB alarm — typically 1024 or similar)
- `SPINDLE LUBE ALARM` (MTB alarm 1025 on many Arrow models)
- `SPINDLE ORIENT FAILED`

### Spindle Drive Fault

**What it means:** The spindle drive (separate from the servo drives — usually Fanuc spindle drive, Siemens, or Magnetek/Stober) detected an internal fault.

**Fix steps:**
1. Note the spindle drive fault code on the drive's own display panel — different from the Acramatic alarm number
2. Power off the entire machine at the main disconnect, wait 2 minutes (DC bus discharge), then power back on — many spindle drive faults clear on a full power cycle
3. If fault returns: common causes include encoder feedback cable damage, spindle motor winding failure, drive DC bus capacitor degradation, and cooling fan failure inside the spindle drive

### Spindle Overheat (MTB Alarm 1024 / CR16)

**What it means:** The spindle motor or drive overtemperature thermostat has opened. On Arrow machines, CR16 relay in the machine cabinet is associated with the spindle overheat thermostat circuit.

**Fix steps:**
1. Allow spindle to cool — typically 15–20 minutes
2. Do not cycle power immediately after overtemperature — wait for the machine to indicate normal temperature
3. Check the spindle cooling fan (external fan mounted on top/back of spindle motor) — fan failure is the most common cause
4. Check spindle duty cycle — heavy cuts, particularly with large face mills, can overheat the spindle motor if the machine is undersized for the application
5. On VMCs with liquid-cooled spindles: check coolant flow and temperature

### Spindle Lube Alarm (MTB Alarm 1025)

**What it means:** The Dropsa or similar spindle lube (oil-air lubrication) unit has not confirmed lube delivery. Some machines use an oil-mist oiler; others use a timed lube pump with flow confirmation.

**Fix steps:**
1. Check the Dropsa oiler indicator light — it should flash with each lube pulse during spindle operation
2. Check oil level in the Dropsa reservoir — low oil will cause a lube alarm
3. Check the air supply to the lube unit — Dropsa oil-air units require clean dry air at the specified pressure (typically 60–80 psi)
4. Check the lube confirmation sensor — a flow sensor or proximity switch confirms oil delivery. If the oiler is working but the alarm persists, check the sensor and its wiring
5. Note: The Dropsa will not operate if the machine is in E-stop or drives-not-ready state — do not diagnose lube alarms while the machine is in alarm condition

### Spindle Orient Failed

**What it means:** The CNC commanded spindle orient (for ATC tool change) but the spindle did not reach the correct angular position within the timeout.

**Fix steps:**
1. Check spindle encoder feedback — orient relies on the spindle position encoder. If the encoder is slipping or the coupling is loose, orient will fail
2. Check the spindle orient target position parameter — if changed accidentally, the spindle may be trying to orient to an incorrect position
3. Check for a mechanical issue: gearbox binding or belt slippage preventing the spindle from decelerating to orient speed
4. Jog the spindle manually (low speed) and verify the encoder feedback is incrementing correctly on the diagnostic screen

---

## ATC / Tool Changer Fault Alarms

**Common alarm texts:**
- `ATC FAULT` or `TOOL CHANGER FAULT`
- `TOOL NOT IN SPINDLE`
- `ATC ARM NOT IN HOME`
- `MAGAZINE NOT INDEXED`
- `TOOL IN SPINDLE AND MAGAZINE`
- `ATC DOOR NOT OPEN / NOT CLOSED`

The ATC (Automatic Tool Changer) on Arrow and Sabre machines uses a combination of proximity switches and pneumatic/hydraulic actuators. PLC alarms in the ATC group are among the most parameter-sensitive faults on these machines.

### ATC Arm Not in Home

**What it means:** The ATC arm is not in its home/parked position when the CNC tried to execute a tool change.

**Fix steps:**
1. Do not attempt to run the machine with ATC in unknown position — a tool crash can damage the ATC, spindle, and workpiece simultaneously
2. Access the ATC manual/jog controls (typically in the Machine Control area of the Acramatic pendant) and manually step the ATC through its cycle
3. Check all ATC proximity switches: each position in the ATC sequence has a prox switch. Check diagnostic screen to see which switch is and is not confirming
4. Check air supply to the ATC pneumatic cylinders — most Cincinnati ATC systems use pneumatics for arm extension/retraction

### Tool Not in Spindle / Tool in Spindle and Magazine

**What it means:** The draw bar sense switch indicates no tool is in the spindle when there should be one (or the opposite — a tool is detected in both spindle and magazine simultaneously after a failed change).

**Fix steps:**
1. Visually inspect the spindle — is a tool holder present? Is the draw bar clamped?
2. Check draw bar sense switch (prox switch on the spindle head confirming tool clamp) — adjust sensitivity or replace if worn
3. On pneumatic draw bar machines: check air pressure to the draw bar unclamping cylinder. Low air pressure causes incomplete tool release
4. If a tool is stuck: use the spindle air blast and draw bar unclamping button to release the tool manually. Do not attempt to pull a tool holder by hand — the draw bar spring force will cause injury

### Magazine Not Indexed

**What it means:** The tool magazine (carousel or chain) did not confirm position after an index command.

**Fix steps:**
1. Check the magazine index prox switch — typically one prox switch per pocket that confirms the pocket is aligned with the ATC arm
2. Check the magazine drive motor — drive chain or belt, gear teeth
3. Verify magazine air supply (pneumatically driven magazines)
4. Check PLC parameters for magazine position — if parameters were corrupted, the PLC may think the wrong pocket is in position

---

## Lube System Alarms

**Common alarm texts:**
- `LUBE FAULT` or `LUBE ALARM`
- `LUBE AIR PRESSURE ALARM` (MTB Alarm 1066)
- `WAY LUBE ALARM`
- `LUBE LEVEL LOW`

Cincinnati Arrow and Sabre machines use a central way lube system (Dropsa or equivalent) that lubricates the ball screws, linear guides, and other way surfaces. The system runs on a timer and sends air-actuated oil pulses to each lube point.

### Lube Air Pressure Alarm (MTB Alarm 1066)

This is one of the most commonly discussed Cincinnati lube alarms. Two pressure sensors monitor the lube system: one confirms oil pressure is reached at the distributor, another confirms the air-oil mixture is at pressure.

**Fix steps:**
1. Check air supply pressure to the lube unit — requires clean, dry air at 60–80 psi. Check the in-line air filter/regulator for the lube system
2. Check the two proximity sensors (cube-shaped pressure sensors) in the lube air circuit — these sensors can read erratically when their internal contacts corrode or the pressure diaphragm weakens
3. Verify oil level in the lube reservoir — some systems have a low-level float switch that triggers lube alarms before the tank is completely empty
4. Clear air lines: disconnect lube output lines at the distributor to check for blockages
5. If sensors read fine but alarm persists intermittently, replace both pressure sensors (common on machines over 15 years old)

### Way Lube Not Confirmed

**What it means:** The lube system ran a lube cycle but the flow confirmation sensor did not detect oil flow.

**Fix steps:**
1. Check lube lines for kinks, blockages, or disconnected tubing
2. Check lube distributor block — these progressive distributors have internal pistons that can seize with old or contaminated oil
3. Flush the lube system with fresh way lube oil and cycle manually

---

## Hydraulic System Alarms

**Common alarm texts:**
- `HYDRAULIC FAULT` or `HYDRAULIC PRESSURE FAULT`
- `HYDRAULIC UNIT NOT READY`
- `CLAMP PRESSURE FAULT`
- `COUNTERBALANCE PRESSURE FAULT`

Most Cincinnati Arrow and Sabre VMCs use a small hydraulic unit for draw bar actuation and counterbalance (Z-axis weight counterbalance). The hydraulic unit is typically in the base of the machine.

**Fix steps:**
1. Check hydraulic fluid level in the reservoir — hydraulic systems lose fluid slowly through seals and fitting connections
2. Check hydraulic unit motor is running — listen for the pump motor; check its circuit breaker
3. Check hydraulic system pressure gauge on the hydraulic unit — compare to the spec on the machine hydraulic schematic
4. Check hydraulic pressure switch: this switch tells the PLC that correct system pressure is present. A failed switch will cause a hydraulic alarm even if pressure is correct
5. Check for hydraulic leaks at cylinder connections, hose fittings, and solenoid valve block

### Counterbalance Pressure Fault

**What it means:** The Z-axis counterbalance pressure is outside acceptable range. The counterbalance pneumatic or hydraulic cylinder offsets the weight of the spindle head so the Z-axis servo only handles dynamic forces.

**Fix steps:**
1. Check counterbalance pressure setting — there is an adjustment valve, typically accessible in the left side panel of the machine. The correct pressure is specified in the machine maintenance manual
2. Check for leaking counterbalance cylinder — if the cylinder is bypassing, counterbalance pressure will drift down during machining

---

## Coolant System Alarms

**Common alarm texts:**
- `COOLANT FAULT`
- `COOLANT LEVEL LOW`
- `CHIP CONVEYOR FAULT`
- `THROUGH SPINDLE COOLANT PRESSURE FAULT`

**Fix steps:**
1. **Low coolant level:** Refill coolant tank. Check for leaks in coolant lines and enclosure seals
2. **Coolant pump fault:** Check coolant pump motor circuit breaker. Check pump for clogging (chips fouling the impeller)
3. **Through spindle coolant pressure:** TSC pump delivers high-pressure coolant through the spindle/tool. Check TSC pump pressure setting, filter element, and high-pressure hose connections
4. **Chip conveyor fault:** Check conveyor drive motor, check for chip overloading or jammed chips at the conveyor intake

---

## Machine Start Inhibit / E-Stop Conditions

When the machine will not start and the alarm message says `MACHINE START INHIBIT` or `E-STOP ACTIVE`, use the PLC diagnostic screen to find which machine signal is holding the start inhibit.

**Acramatic 2100 PLC diagnostics:**
1. Press the diagnostic softkey on the Acramatic pendant
2. Navigate to the PLC I/O (Input/Output) status screen
3. Look for any input signal that should be HIGH (active) but is LOW, or vice versa
4. Machine safety signals include: all axis drives ready, spindle ready, hydraulic pressure OK, lube OK, ATC home, doors closed, E-stop loop closed

The CR relay numbers in the machine wiring diagram correspond to named functions. Key relays on Arrow machines: CR12 (machine ready), CR16 (spindle overheat), CR17 (axis enable), CR46 (intermittent faults/startup sequence). Flashing CR46 during startup indicates the startup sequence has not completed.

---

## Acramatic 850SX Controls

Older Cincinnati machines (circa 1985–1995) used the Acramatic 850SX control, which displays alarms differently from the 2100. The 850SX uses:

- 4-digit alarm codes displayed on a small LED panel on the pendant
- Axis alarms appear as codes in the 18xxx range (e.g., 18530 = axis alarm)
- The 850SX does not have a full graphical interface — alarms appear as numbers with brief text on the small display

**Key 850SX alarm ranges:**
- **18000–18999:** Servo/axis alarms
- **11000–11999:** ATC/magazine alarms
- **12000–12999:** Spindle alarms
- **13000–13999:** Coolant/auxiliary alarms

For 850SX machines, the machine maintenance manual is the primary alarm reference. These manuals are available from specialty dealers and some online archives.

---

## Accessing Alarm History

**Acramatic 2100:**
1. Press the **Diagnostics** softkey from the main CNC screen
2. Select **Alarm History**
3. The control stores the last 100 alarms with timestamp and operating mode at the time of alarm
4. Use alarm history to correlate alarms — a sequence of ATC fault → drives not ready → estop often indicates the ATC crashed and triggered the E-stop chain

**Acramatic 2100 extended diagnostics:**
Some parameters control extended diagnostic logging. Access via the maintenance parameter screens (password required — default maintenance password varies by machine; check the documentation in the machine's original binder). Extended diagnostics can log PLC signals at the time of alarm.

---

## Cincinnati-Specific Parameter Notes

The Acramatic 2100 separates CNC parameters (interpolation, axis tuning) from machine builder (MTB) parameters (Cincinnati PLC logic, ATC sequences, lube timing).

**Critical parameter areas:**

| Parameter Group | Function | Notes |
|----------------|----------|-------|
| Axis servo tuning | P, I, D gains for each axis | Do not adjust unless following Cincinnati service procedure. Wrong tuning causes hunting and drive faults |
| ATC pocket table | Associates tool numbers with pocket positions | If corrupted, ATC will index to wrong pockets. Backup before any ATC-related repairs |
| Spindle orient position | Angular position for tool change orient | Must be set during spindle/encoder replacement |
| Software travel limits | Max/min travel for X, Y, Z | Check these after machine crash or re-homing |
| Lube timer | Interval between lube cycles | Too long causes way wear; too short wastes oil |
| Control word (Pr 87 on 850SX) | Determines if machine uses stored or default parameters | Per community: if Pr 87 = 0, machine will use embedded defaults — reload from backup binder |

**Backing up parameters:** The Acramatic 2100 stores parameters on the internal hard drive. Back up parameter files to a USB drive or network drive regularly — hard drives on these machines are typically 15–25 years old and are a single-point failure. Some machines have been retrofitted with solid-state drives (SSD or CompactFlash via an IDE adapter).

---

## Parts Table

| Component | Fits | Part Notes |
|-----------|------|------------|
| **ATC pot (tool pocket cam follower)** | Arrow, Sabre ATC carousel | Plastic or steel cam followers that locate each tool pocket. Wear item. Specify machine model |
| **Draw bar retention knob** | All Cincinnati VMC spindles | BT40 or CAT40 pull studs (retention knobs). Standard DIN or ANSI dimensions — not machine-specific |
| **Spindle draw bar spring pack** | Arrow, Sabre, Maxim | The spring pack that applies clamping force to the tool holder. Wears over time, especially on high-cycle machines. Measured spring force should match spec |
| **Way lube distributor block** | Arrow, Sabre series | Progressive distributor (usually Dropsa or Norgren brand). Specify number of outlets and flow rate. Replace piston kit or full block |
| **Lube oil-air pressure sensor** | Arrow, Sabre series | Cube-style pneumatic pressure switch, typically 40–100 psi range. Standard component — match pressure range and electrical output |
| **Proximity switch (general)** | ATC, lube, axes | NPN or PNP 3-wire prox switch. Specify sensing range and M12 or M18 thread size. Common on Arrow/Sabre: M12×1, 4 mm range, NPN NC |
| **Axis encoder cable** | Arrow, Sabre (Fanuc drives) | Shielded multi-conductor cable from servo motor to drive. Replace full assembly if any conductor damaged |
| **Servo motor (X/Y/Z)** | Arrow 750/1000 | Fanuc αi series or older AC servo motors. Match encoder type and flange size to original |
| **Hydraulic pump unit** | Arrow base cabinet | Small hydraulic power unit, typically 1–3 GPM, 1000–1500 PSI. Match fluid port size and motor voltage |
| **Dropsa lube reservoir / pump** | Arrow, Sabre way lube | Dropsa MDD or equivalent progressive lube pump. Specify reservoir capacity and outlet count. Oil specification: ISO VG 68 way oil |
| **Counterbalance cylinder** | Arrow/Sabre Z axis | Pneumatic or hydraulic counterbalance cylinder. Measure bore and stroke from machine drawings or existing cylinder |
| **ATC cam/motor** | Arrow chain magazine | Cam motor drives the magazine index. Motor and gearbox assembly |

---

## Common Misdiagnoses on Cincinnati VMCs

**"The machine keeps faulting out but the drives look fine."**
Check the backup battery in the Acramatic 2100 control. The battery maintains parameter RAM — a weak battery allows parameters to corrupt gradually, causing random alarms. Battery replacement requires parameter backup before and restore after.

**"The ATC worked fine, then all faults started."**
An ATC crash — tool holder not released, arm collision — can corrupt the ATC pocket table parameters. Before troubleshooting further, verify the ATC pocket table is intact and the ATC arm is truly in home position (not just indicated as home by a stuck proximity switch).

**"Machine starts fine but axes hunt or vibrate."**
Axis servo tuning parameters may have shifted, or an encoder cable is intermittent. Run the Cincinnati diagnostic servo test (found in the Acramatic diagnostics menu) to check axis response before assuming a mechanical issue.

## Where to Buy Replacement Parts

Find replacement parts for Cincinnati CNC machines on Amazon:

- [Cincinnati CNC Machine Parts](https://www.amazon.com/s?i=industrial&k=Cincinnati+CNC+machine+parts&tag=errorcodefixes-20)
- [CNC Proximity Switch Replacement](https://www.amazon.com/s?i=industrial&k=CNC+proximity+switch+M12+NPN&tag=errorcodefixes-20)
- [CAT40 Pull Stud Retention Knobs](https://www.amazon.com/s?i=industrial&k=CAT40+pull+stud+retention+knob&tag=errorcodefixes-20)