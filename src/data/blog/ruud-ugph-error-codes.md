---
title: "Ruud UGPH Error Codes - What It Means and How to Fix It"
description: "Ruud UGPH gas furnaces use LED blink codes to report ignition, pressure switch, inducer, limit, and rollout faults. This guide explains every 1 through 9 flash code and the fixes that usually get the furnace running again."
pubDatetime: 2026-04-25T00:00:00Z
author: "Marcus Webb"
tags:
  - hvac
  - error-codes
---

The Ruud UGPH is a high-efficiency upflow/horizontal gas furnace used in both residential and light commercial applications. When something goes wrong, the control board communicates the problem through an LED status light on the front of the furnace - typically visible through a small window in the access panel. This LED blinks in distinct patterns, and each pattern maps to a specific fault condition.

This guide covers all LED blink codes for the UGPH series, explains what the control board is actually detecting, and gives you the diagnostic steps to resolve each fault efficiently. Whether you're a homeowner trying to understand why your heat stopped working or an HVAC technician running a service call, this is your complete reference.

## What Does Ruud UGPH Error Codes Mean?

The control board on the UGPH furnace uses a single LED (usually amber or green) to communicate fault codes. When a fault is active, the LED blinks a set number of times, pauses, then repeats. Count the blinks in one complete cycle before the pause - that number is your fault code.

A steady ON light with no blinking means normal operation. A steady OFF means there's no power to the control board. Rapid continuous blinking (sometimes called "heartbeat") means the board is powered and in standby. 

**Important:** The UGPH also stores the last three fault codes in memory. On many control board versions, you can retrieve fault history by pressing the "Recall" or "Diagnostic" button if present, or by shorting the diagnostic pins momentarily as described in the service manual.

### Ruud UGPH LED Blink Code Reference

**1 Blink - Ignition Lockout / Failed to Light**
The furnace attempted to light the burners, the igniter activated, and gas valve opened - but flame was not detected within the trial-for-ignition period. After typically 3 attempts, the board goes to hard lockout.

Causes:
- Failed hot surface igniter (HSI) - most common cause
- Dirty or faulty flame sensor rod
- Failed gas valve
- Low gas pressure (check manifold pressure: should be 3.5" w.c. for natural gas)
- Cracked or mispositioned burners

**2 Blinks - Pressure Switch Stuck Open**
The pressure switch(es) did not close after the inducer motor started. The inducer creates a negative pressure in the heat exchanger; the pressure switch verifies this negative pressure exists before allowing ignition to proceed.

Causes:
- Failed inducer motor (most likely if inducer doesn't start at all)
- Blocked flue or condensate drain causing back-pressure
- Failed pressure switch
- Cracked or disconnected pressure switch hose (tubing)
- Plugged condensate trap (on 90%+ AFUE models)

**3 Blinks - Pressure Switch Stuck Closed**
The pressure switch is reading closed (indicating negative pressure) even when the inducer is OFF. This is a safety check the board runs before starting the inducer.

Causes:
- Failed pressure switch stuck in closed position
- Pressure switch hose disconnected and touching condensate
- Water in the pressure switch from condensate overflow

**4 Blinks - Open High Limit Device**
The high limit switch or rollout switch has opened, cutting off the gas valve. This is a critical safety event - the furnace detected dangerously high temperatures inside the heat exchanger or burner box.

Causes:
- Dirty air filter (severely restricted airflow - most common residential cause)
- Failed blower motor
- Blocked or closed supply/return registers
- Oversized furnace relative to duct system
- Cracked heat exchanger (causes combustion gases to enter the airstream, triggers rollout switch)

**5 Blinks - Flame Sensed with Gas Valve Closed**
The flame sensor is detecting a flame signal when the gas valve should be closed. This is a safety lockout.

Causes:
- Leaking gas valve (gas leaking past closed valve - this is a gas leak situation, act immediately)
- Faulty flame sensor sending false signal
- Electrical interference on the flame sense circuit

**6 Blinks - Rollout Switch Open**
The rollout switch tripped. This switch is located in the burner compartment and opens when flames roll out of the burners - indicating a serious combustion problem.

Causes:
- Cracked heat exchanger (most serious cause - call a pro immediately)
- Blocked flue - combustion gases have nowhere to go and push flames backward
- Failed inducer motor
- Excessive gas pressure

⚠️ A tripped rollout switch is a red-flag safety event. Do not manually reset the rollout switch and restart the furnace without a thorough inspection. A cracked heat exchanger can allow carbon monoxide into the living space.

**7 Blinks - Low Flame Sense Signal**
The flame sensor is reading an abnormally weak flame current (typically below 0.5 microamps on Ruud UGPH boards, which need 1.5-4 microamps for reliable hold).

Causes:
- Dirty flame sensor rod - this is the most common cause by far
- Corroded flame sensor bracket
- Cracked porcelain insulator on the sensor
- Incorrect gas pressure (lean mixture burns with lower ionization current)

**8 Blinks - Low Inducer Speed / Inducer Fault**
The inducer motor is running but not reaching commanded speed, or the board detected an abnormal tachometer signal from the ECM inducer.

Causes:
- Worn inducer motor bearings (listen for rumbling or squealing during inducer pre-purge)
- Partially blocked flue
- Failing inducer motor - speed dropping off under load
- Failed inducer motor control module

**9 Blinks - Low Stage Pressure Switch Did Not Open (Two-Stage Models)**
On two-stage UGPH furnaces, this code means the low-stage pressure switch failed to open when the system stepped up to high-stage. This indicates the pressure switch is stuck in the closed position during the diagnostic sequence.

Causes:
- Failed two-stage pressure switch
- Wiring short in the pressure switch circuit

## How to Fix It

**Step 1: Read and record the blink code.**
Stand at the furnace and watch the LED through the observation window. Count blinks per cycle. Wait through two or three complete cycles to confirm your count. If the LED is dark, check the main power switch at the furnace and the circuit breaker.

**Step 2: For 2-blink (pressure switch open), check the inducer first.**
Listen when the thermostat calls for heat. You should hear the inducer motor spin up within 10-30 seconds. If you hear nothing, or a brief hum and then silence, the inducer motor may be seized or the starting capacitor has failed. If the inducer runs but the fault persists, inspect the pressure switch hose - disconnect it from the inducer outlet and blow through it to confirm it's not blocked with condensate. Then test the pressure switch with a U-tube manometer or an HVAC manometer: the low-stage switch on most UGPH models closes at approximately -0.35" to -0.65" w.c.

**Step 3: For 4-blink (high limit), check the filter and blower.**
Turn off power. Pull the filter. If it's gray, dense, or visibly clogged, replace it immediately and reset the furnace. If the filter is clean and the fault persists, measure temperature rise across the heat exchanger (supply vs. return air temperature differential). Design temperature rise for the UGPH series is typically 40°F-70°F. A rise above 80°F with a clean filter and running blower suggests a duct restriction or an oversized furnace - check for closed registers.

**Step 4: For 1-blink (ignition failure), test the igniter and flame sensor.**
With power off, remove the hot surface igniter (handle it carefully - finger oils can cause premature failure). Measure resistance across the igniter terminals: a working silicon nitride HSI typically reads 40-90 ohms at room temperature. An open circuit (OL) means the igniter is broken. If the igniter checks out, locate the flame sensor rod on the burner - it's a single metal rod with a porcelain insulator. Remove it and clean it with fine steel wool or light sandpaper. Reinstall and test.

**Step 5: For 6-blink (rollout), inspect heat exchanger before anything else.**
Use a flashlight and mirror to visually inspect the heat exchanger tubes visible through the burner opening. Look for cracks, holes, or corrosion along weld seams. Insert a combustion analyzer probe into each burner tube while the blower is running - a sudden CO spike indicates a crack. Do not reset the rollout switch and run the furnace until you've confirmed the heat exchanger is intact.

**Step 6: For 7-blink (low flame sense), clean the flame sensor.**
This is a simple 10-minute fix that resolves roughly 80% of 7-blink faults. Turn off power and gas. Remove the flame sensor (1/4" hex screw). Clean the rod with fine steel wool - remove any white oxide buildup until the metal is bright and shiny. Reinstall and test. If the fault returns within one heating season, replace the sensor.

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|-------------|
| [Ruud UGPH Hot Surface Igniter (Part # 62-24164-01)](https://www.amazon.com/dp/B00BTLLJ40?ascsubtag=ecf-ruud-ugph-error-codes&tag=errorcodefixes-20) | Replaces failed silicon nitride igniter causing 1-blink lockout | $25-$45 |
| [Ruud Inducer Motor Assembly (Part # 70-24033-03)](https://www.amazon.com/dp/B00FDZ90B2?ascsubtag=ecf-ruud-ugph-error-codes&tag=errorcodefixes-20) | Replaces failed draft inducer motor causing 2-blink or 8-blink faults | $180-$350 |
| [Pressure Switch (Part # 42-103148-01)](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-ruud-ugph-error-codes&tag=errorcodefixes-20) | Replaces failed pressure switch causing 2-blink or 3-blink faults | $18-$40 |
| [Ruud UGPH Control Board (Part # 62-24084-01)](https://www.amazon.com/s?k=Ruud+UGPH+Control+Board+%28Part+%23+62-24084-01%29&tag=errorcodefixes-20) | Replaces failed control/ignition board | $150-$280 |
| [Flame Sensor Rod (Part # 62-23754-92)](https://www.amazon.com/s?k=Flame+Sensor+Rod+%28Part+%23+62-23754-92%29&tag=errorcodefixes-20) | Replaces worn flame sensor causing 7-blink fault | $12-$22 |
| [High Limit Switch (Part # 47-22860-03)](https://www.amazon.com/dp/B0BN3TRG9R?ascsubtag=ecf-ruud-ugph-error-codes&tag=errorcodefixes-20) | Replaces open high limit device causing 4-blink fault | $15-$35 |
| [Rollout Switch (Part # 46-101683-01)](https://www.amazon.com/dp/B0BN3TRG9R?ascsubtag=ecf-ruud-ugph-error-codes&tag=errorcodefixes-20) | Manual reset safety switch - inspect heat exchanger before replacing | $10-$20 |

## When to Call a Pro

Some UGPH repairs are appropriate for a competent DIYer - replacing the flame sensor, igniter, or even the pressure switch is within reach if you're comfortable working around gas appliances and following lockout/tagout procedures. However, these situations require a licensed HVAC technician:

- **6-blink rollout fault**: Do not reset and restart until a tech confirms the heat exchanger is intact. Carbon monoxide from a cracked heat exchanger is odorless and lethal.
- **5-blink flame sensed without gas valve open**: This may indicate a leaking gas valve. Shut off gas, ventilate, and call a pro.
- **Inducer motor replacement on 90%+ AFUE models**: These involve condensate systems and flue connections that need proper sealing.
- **Any repair involving the gas valve itself**: Gas valve replacement requires testing manifold pressure and checking for leaks.

If the LED has no clear blink pattern or flashes in a way not listed in this guide, photograph it and contact Ruud technical support at 1-800-848-7883.

## Frequently Asked Questions

**Q: My Ruud UGPH shows 2 blinks, but I can hear the inducer running. What should I check?**
A: A running inducer that still produces a 2-blink fault almost always points to the pressure switch circuit rather than the inducer motor itself. First check the plastic hose connecting the pressure switch to the inducer - these hoses split, kink, or fill with condensate water on 90%+ models. Disconnect both ends of the hose and blow through it. Then test the pressure switch: apply negative pressure with your mouth on the switch hose connection and listen for a faint click as the diaphragm moves. If no click, the switch is failed or stuck.

**Q: The furnace shows 4 blinks, I replaced the filter, but it still trips. What else could it be?**
A: Check the supply plenum temperature with an HVAC thermometer - it should stay below the limit switch rating (usually 140°F-170°F depending on model). If it's overheating with a clean filter, check that all supply and return registers in the home are open and unobstructed. Also verify the blower wheel isn't clogged with lint, which reduces airflow without affecting the filter. A clogged blower wheel requires removal and cleaning.

**Q: How do I reset the UGPH control board after fixing a fault?**
A: Turn the thermostat to OFF. Shut off the furnace power switch for 30 seconds, then restore power. On hard-lockout faults (particularly 1-blink ignition lockout after 3 failed attempts), some UGPH boards also accept a reset by momentarily shorting the two diagnostic pins on the board with a small jumper wire - check your model's service label on the inside of the access door.

**Q: The 8-blink inducer fault appeared after the furnace ran fine all summer. Why now?**
A: Inducer motors often survive all summer (when they're not used in cooling-only mode) and fail at the start of heating season when they're suddenly asked to run for hours at a time. Bearing wear, dust accumulation in the motor windings, and capacitor degradation all accelerate over time. Early-stage bearing failure often produces a rumbling or grinding sound during the inducer pre-purge phase - listen carefully at the start of each heat call.

**Q: Can a dirty heat exchanger cause pressure switch faults?**
A: Yes, indirectly. A cracked or damaged heat exchanger can disrupt airflow through the combustion chamber, affecting the negative pressure the inducer needs to build. More directly, a severely corroded or partially collapsed heat exchanger tube changes the flow resistance and can cause the pressure switch to read marginal values. If pressure switch issues recur on a furnace that's 15+ years old, heat exchanger inspection is warranted.
