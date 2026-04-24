---
title: "Lennox SL280UHV Error Codes — Complete Fault Code Diagnostic Guide"
author: "Industrial Error Code Fixes"
pubDatetime: 2026-04-24T21:00:00Z
modDatetime: 2026-04-24T21:00:00Z
slug: lennox-sl280uhv-error-codes
featured: false
draft: false
tags:
  - lennox
  - furnace
  - hvac
  - variable-speed
  - error-codes
description: "Lennox SL280UHV error codes explained — this two-stage variable-capacity furnace communicates faults via LED blink codes on the control board. Here's how to read and fix each one."
---

## Error Codes: Lennox SL280UHV

**What it means:** The Lennox SL280UHV is a high-efficiency two-stage variable-speed gas furnace that communicates diagnostic faults through a status LED on the control board (located behind the lower access panel). The LED blinks in a repeating pattern: count the flashes in the first group, then the second group — together they form the fault code. For example, 3 flashes, pause, 4 flashes = fault code 34. Single-digit codes blink once with a long pause between groups.

This unit uses the Lennox iComfort or conventional thermostat interface and is common in high-end residential and light-commercial installations from 2010–present.

## Lennox SL280UHV Fault Code Reference

### Code 11 — No Previous Code
Board has been powered with no faults. Normal status on a healthy system.

### Code 12 — Blower On After Power Up
Blower ran at power-up to clear residual heat. Normal operation.

### Code 13 — Limit Switch Fault (Soft Lockout)
The high-temperature limit switch tripped. Furnace locked out after three consecutive trips. **Most common cause on SL280UHV units:** dirty air filter, blocked return, or failed variable-speed blower capacitor.

### Code 14 — Ignition Failure Lockout (Hard Lockout)
The board attempted ignition four times without establishing flame. Possible causes:
- Gas supply interrupted
- Hot surface igniter cracked or failed
- Flame sensor coated with oxidation
- Gas valve not opening

**Reset:** Cycle power off for 30 seconds.

### Code 21 — Gas Valve Fault
Gas valve energized but no flame detected. Usually points to gas valve failure or, less often, an intermittent connection on the valve wiring harness.

### Code 22 — Induced Draft Motor Fault
The inducer motor didn't reach operating speed. Check capacitor first (cheap, fast fix). If motor hums without spinning, the capacitor is almost certainly failed.

### Code 23 — Pressure Switch Did Not Open
The pressure switch didn't open after the inducer shut down. Typically a stuck-closed pressure switch or condensate backup causing the switch to stay in the tripped position.

### Code 24 — Secondary Voltage Fuse Blown
The 3A automotive-style fuse on the control board is blown. Almost always caused by a wiring short downstream — typically a shorted thermostat wire touching bare metal.

### Code 25 — Control Board Fault
The board detected an internal fault. Power cycling often clears it; persistent code 25 = board replacement.

### Code 31 — Pressure Switch Did Not Close
Inducer running but pressure switch won't close. Classic causes: blocked condensate drain, cracked pressure switch hose, weak inducer motor, blocked flue or intake.

### Code 32 — Pressure Switch Stuck Open After Ignition
Pressure switch opened during the heating cycle — usually a flue obstruction, condensate backup, or a pressure switch that's drifted out of calibration.

### Code 33 — Limit Switch Fault
The primary limit or auxiliary limit switch opened during the heating cycle. On the SL280UHV, the variable-speed blower should prevent this — a code 33 here usually means the blower's ECM drive module is failing and not ramping up to full speed.

### Code 34 — Ignition Proving Fault
Flame established but lost during the first heating cycle. Dirty flame sensor (clean with emery cloth), weak gas pressure, or drafting problem causing flame instability.

### Code 41 — Blower Motor Fault
The ECM (electronically commutated motor) reported an error to the control board. Could be a motor winding failure, Hall sensor fault, or ECM drive module failure. This is one of the more expensive repairs on the SL280UHV — the ECM module alone runs $300–$600.

### Code 42 — Inducer Motor Fault
Inducer motor current draw exceeded expected range. Could be a bad capacitor, failing bearings, or a partially blocked flue.

### Code 43 — Low-Fire Pressure Switch Fault
SL280UHV-specific: the low-fire pressure switch failed to close during stage-1 operation. Check the low-fire pressure switch hose and switch.

### Code 44 — High-Fire Pressure Switch Fault
High-fire pressure switch didn't close when the board called for stage-2 operation. Same diagnostic path as code 43 but for the second pressure switch.

### Code 45 — Control Board Memory Error
EEPROM checksum error on the control board. Power cycle first; persistent code = board replacement.

## Common Causes of SL280UHV Faults

- **Dirty air filter** — Code 13, 33. SL280UHV has a high-MERV media filter that clogs faster than standard filters. Replace every 6–12 months.
- **ECM blower issues** — Code 41, 13. The variable-speed ECM motor is complex. A failing drive module ramps the motor down, reducing airflow and tripping limits.
- **Condensate drain blockage** — Code 23, 31, 32. This is a 90%+ AFUE condensing furnace that produces significant condensate. Drain line blockages are extremely common, especially in humid climates.
- **Pressure switch hose cracks** — Code 31, 32, 43, 44. The silicone hoses on SL280UHV pressure switches crack with age. A $2 hose causes a no-heat call.

## Step-by-Step Fix {#step-by-step-fix}

1. **Read the fault code.** Remove the lower access panel. The LED is on the left side of the control board. Count flash groups. Write down the two-digit code.

2. **Start with the filter.** Pull the media filter (typically in the return air cabinet above the furnace or in the furnace itself). If it's gray or blocked, replace it. A fresh filter resolves code 13 and 33 about 40% of the time.

3. **Check the condensate drain.** Locate the clear plastic drain line exiting the bottom of the furnace. Disconnect it at the outlet and blow through it — if you meet resistance, it's clogged. Clear it with a wet/dry vacuum or compressed air. This resolves code 23, 31, and 32 in high-humidity installs.

4. **Inspect the inducer and pressure switch hoses.** With power off, trace all small-diameter rubber hoses from the inducer housing to the pressure switch(es). Look for cracks, kinks, or disconnected ends. Replace suspect hoses with matching-diameter tubing.

5. **Clean the flame sensor.** Remove the single screw holding the flame sensor rod in the burner assembly. Lightly polish the rod with #400 emery cloth until shiny. Reinstall. This clears code 34 in most cases.

6. **Test the ECM blower.** For code 41: with the furnace calling for heat, feel the airflow at a supply register during the blower on-delay. Airflow should ramp up smoothly over 30–60 seconds to full speed. Weak, erratic, or absent airflow with the motor energized suggests an ECM drive module failure.

7. **Check the gas valve.** For code 21: with the furnace in ignition attempt, listen for a soft click when the gas valve energizes. No click = bad valve solenoid. Click but no gas flow = stuck valve poppet.

8. **Replace the control board fuse.** For code 24: replace the 3A mini-blade automotive fuse on the board. If it blows again immediately, disconnect the thermostat wire at the furnace and re-energize — if fuse holds, the short is in the thermostat wiring.

## Parts Often Needed {#parts-often-needed}

| Part | Part Number | Typical Cost | Where to Buy |
|------|-------------|--------------|--------------|
| High-limit switch (L195) | SL280UHV varies by model | $25–$45 | [Amazon](https://www.amazon.com/s?k=Lennox+SL280UHV+limit+switch&tag=errorcodefixes-20) \| Lennox dealer |
| Hot surface igniter | LB-90991A | $35–$55 | [Amazon](https://www.amazon.com/s?k=Lennox+LB-90991A+igniter&tag=errorcodefixes-20) \| SupplyHouse |
| Flame sensor rod | H8910EU | $20–$35 | [Amazon](https://www.amazon.com/s?k=Lennox+flame+sensor+H8910EU&tag=errorcodefixes-20) \| Lennox dealer |
| Inducer motor capacitor (5 µF) | — | $8–$15 | [Amazon](https://www.amazon.com/s?k=5+uf+440v+oval+run+capacitor+inducer&tag=errorcodefixes-20) \| HVAC supply |
| ECM blower motor module | 100483-08 | $350–$600 | [Amazon](https://www.amazon.com/s?k=Lennox+100483-08+ECM+module&tag=errorcodefixes-20) \| Lennox dealer |
| Control board | 1097-200 series | $200–$350 | [Amazon](https://www.amazon.com/s?k=Lennox+SL280UHV+control+board&tag=errorcodefixes-20) \| Lennox dealer |
| Media air filter (MERV 11, 20x25x5) | X8791 | $35–$55 | [Amazon](https://www.amazon.com/s?k=Lennox+X8791+media+filter+20x25x5&tag=errorcodefixes-20) \| Home Depot |

## When to Call a Professional

Any fault involving the gas valve (code 21) or a hard lockout on ignition (code 14) that persists after cleaning the flame sensor should be diagnosed by a licensed HVAC tech. Gas valve replacement requires disconnecting the gas line and rechecking for leaks. The SL280UHV's ECM blower system is also complex — drive module failures require specialized diagnostic tools to confirm before spending $400+ on parts.

> **Pro tip:** The SL280UHV has a "last 5 fault codes" memory on the control board. Hold the diagnostic button (small pushbutton next to the LED) for 3 seconds — the board will blink out the last five fault codes in sequence. This is invaluable for intermittent faults that don't repeat during a service call.
