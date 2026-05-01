---
title: "Lennox SL297NV Error Codes: iComfort Fault Code Diagnostic Guide"
description: "Full guide to Lennox SL297NV top-efficiency furnace error codes, iComfort fault codes, variable-speed blower faults, and DIY fixes."
pubDatetime: 2026-04-25T00:00:00Z
author: "Marcus Webb"
tags:
  - hvac
  - error-codes
---

The Lennox SL297NV is among the highest-efficiency gas furnaces on the market, achieving up to 97.5% AFUE through a two-stage gas valve, variable-speed ECM blower motor, and modulating inducer. It integrates natively with the iComfort S30 and iComfort E30 smart thermostats to provide rich diagnostic data, far more detail than you'd get from most furnaces.

When the SL297NV faults, it logs codes accessible from the iComfort thermostat AND blinks them on the control board LED. This guide decodes both systems and tells you exactly what to check.

## What Does the Lennox SL297NV Fault Code System Mean?

The SL297NV uses a two-LED system on the control board: a green LED for power/status and an amber LED for fault indication. Read the amber LED only.

**Blink pattern:** Count blinks, pause, count again. First number = fault category, second number = specific fault within that category (e.g., 3 blinks, pause, 2 blinks = fault 3-2).

If you have an iComfort thermostat, navigate to Menu → Diagnostics → Fault History for full alphanumeric codes, timestamps, and recommended actions.

### Fault Code Reference

| LED Sequence | iComfort Code | Description |
|---|---|---|
| 1-1 | E001 | Ignition failure, no flame established |
| 1-2 | E002 | Ignition lockout (repeated failure) |
| 1-3 | E003 | Flame signal lost during run |
| 2-1 | E021 | Pressure switch stuck open |
| 2-2 | E022 | Pressure switch stuck closed |
| 2-3 | E023 | Secondary pressure switch fault |
| 3-1 | E031 | High-limit switch open |
| 3-2 | E032 | Rollout switch open |
| 3-3 | E033 | Auxiliary limit switch open |
| 4-1 | E041 | Inducer motor fault |
| 4-2 | E042 | Variable-speed blower motor fault (ECM) |
| 4-3 | E043 | Blower motor communication fault |
| 5-1 | E051 | Gas valve fault |
| 5-2 | E052 | Hot surface igniter circuit fault |
| 6-1 | E061 | Control board internal fault |
| 6-2 | E062 | EEPROM fault |
| 7-1 | E071 | iComfort communication fault |

## How to Fix It

### E001 / E002, Ignition Failure / Ignition Lockout

These are the most common faults on the SL297NV. The furnace attempts to light, the flame sensor doesn't confirm a flame, and the board shuts the gas valve.

1. **Check the hot surface igniter.** The SL297NV uses a silicon nitride igniter. Inspect it visually for cracks. A cracked igniter won't glow hot enough to light the burner. Test resistance: a good igniter reads 15–75 ohms depending on model.
2. **Check the flame sensor.** The flame sensor is a metal rod that extends into the burner flame. Carbon deposits on the rod prevent it from reading the flame. Clean it gently with fine steel wool or an emery cloth, do not use sandpaper.
3. **Verify gas supply.** Check that the manual shutoff valve on the gas line is fully open and that other gas appliances in the home are working.
4. **Check inducer operation.** The furnace will not attempt ignition if the inducer hasn't proven pressure. Watch the startup sequence, the inducer should run for 15–30 seconds before the igniter lights.
5. **Reset from lockout.** After lockout (E002), cut power to the furnace at the breaker for 30 seconds to reset.

### E021, Pressure Switch Stuck Open

The pressure switch confirms the inducer is creating adequate draft before allowing the gas valve to open.

1. **Check the inducer motor.** Listen for the inducer running during a call for heat. If it's not running or is running slowly, see E041 below.
2. **Inspect the pressure switch hose.** The small rubber tube connecting the inducer housing to the pressure switch frequently cracks or disconnects. A broken hose = no pressure = open switch.
3. **Check for a blocked flue or condensate drain.** A blocked flue or backed-up condensate line creates back-pressure that prevents the switch from closing.
4. **Test the switch directly.** Disconnect the hose and apply gentle suction with your mouth, the switch should click. If it doesn't, the switch is faulty.

### E022, Pressure Switch Stuck Closed

A switch that reads closed before the inducer starts prevents furnace operation.

1. **Check for a stuck switch diaphragm.** Condensate can cause the diaphragm to stick closed. Remove the switch and tap it gently, then retest.
2. **Verify there's only one hose on the switch inlet.** On some installations, a mis-routed hose creates false pressure.
3. **Replace the pressure switch** if it reads closed with no inducer running (see Parts table).

### E031, High-Limit Switch Open

The high-limit switch cuts the gas valve when the heat exchanger exceeds a safe temperature (typically around 180°F on the SL297NV).

1. **Check the air filter.** A clogged filter is responsible for the majority of high-limit trips. Replace it if it's been in service more than 90 days.
2. **Check all supply and return registers.** Closed or blocked registers reduce airflow and cause heat exchanger overheating.
3. **Verify the blower motor runs after ignition.** The ECM blower should come on within 45 seconds of burner ignition. A delayed or failed blower is the second most common cause of high-limit trips.
4. **Reset the switch.** Many high-limit switches auto-reset when they cool. If the switch doesn't reset after 30 minutes, it may have failed open, test with a multimeter.

### E032, Rollout Switch Open

A rollout switch opening is serious. It means flames are rolling out of the combustion chamber rather than being drawn through the heat exchanger into the flue.

1. **Do not reset and operate the furnace** until the cause is investigated.
2. **Inspect burners for flame rollout evidence**, scorch marks outside the combustion chamber.
3. **Check heat exchanger integrity.** A cracked heat exchanger can allow combustion gases to escape, causing rollout. This is a safety emergency, call a technician.
4. **Check for blocked flue or inducer failure.** These are the most common causes on an otherwise intact heat exchanger.

### E041, Inducer Motor Fault

1. **Check inducer wheel for debris.** Turn power off and manually spin the wheel, it should spin freely.
2. **Test motor voltage.** The inducer should receive 120VAC from the control board on a call for heat.
3. **Check inducer motor capacitor** if present (some models).
4. **Replace inducer motor assembly** if it hums but doesn't spin (see Parts table).

### E042 / E043, ECM Blower Motor Fault

The variable-speed ECM motor in the SL297NV communicates digitally with the control board. These faults appear when the motor fails to respond or reports an internal fault.

1. **Cycle power.** An ECM motor can lock up and recover after a full power cycle.
2. **Check motor wiring harness.** The ECM motor uses a multi-pin connector. Corrosion or a loose pin causes communication faults.
3. **Verify 120VAC to motor.** The motor needs line voltage to run.
4. **ECM motor replacement** is expensive (typically $400–$800 for the SL297NV motor module). Confirm the motor is faulty before ordering, a technician with ECM diagnostic tools can confirm quickly.

## Parts You May Need

| Part | Use | Link |
|---|---|---|
| Hot Surface Igniter (Silicon Nitride) | E001/E002 ignition faults | [View on Amazon](https://www.amazon.com/dp/B00BTLLJ40?tag=errorcodefixes-20) |
| Flame Sensor Rod | E001 flame sensing failure | [View on Amazon](https://www.amazon.com/dp/B0CZ7M9V4D?tag=errorcodefixes-20) |
| Furnace Pressure Switch | E021/E022 pressure switch faults | [View on Amazon](https://www.amazon.com/dp/B013J2J97A?tag=errorcodefixes-20) |
| Pressure Switch Tubing | E021 hose cracks or disconnects | [View on Amazon](https://www.amazon.com/dp/B013J2J97A?tag=errorcodefixes-20) |
| Furnace High-Limit Switch | E031 persistent high-limit open | [View on Amazon](https://www.amazon.com/dp/B0BN3TRG9R?tag=errorcodefixes-20) |
| Lennox Inducer Motor Assembly | E041 inducer motor fault | [View on Amazon](https://www.amazon.com/dp/B00FDZ90B2?tag=errorcodefixes-20) |

## When to Call a Pro

**DIY-safe repairs on the SL297NV:**
- Air filter replacement
- Flame sensor cleaning
- Hot surface igniter replacement
- Pressure switch hose inspection and replacement
- High-limit switch reset and testing
- Condensate drain clearing

**Call a licensed technician immediately for:**
- **E032 (rollout switch open).** Rollout is a combustion safety fault. The cause must be identified before the furnace runs again.
- **Suspected cracked heat exchanger.** Cracked heat exchangers allow carbon monoxide into living spaces, this is a life-safety issue.
- **ECM blower motor replacement.** While technically DIY-able, diagnosing ECM faults without the proper tool set often results in replacing an expensive motor unnecessarily.
- **Gas valve replacement (E051).** Gas work requires permits and a licensed technician in most jurisdictions.

## FAQ

**How do I access the full fault history on the iComfort S30?**
Go to the thermostat home screen → Menu → Diagnostics → Fault History. You'll see the last 10 faults with dates, times, and detailed descriptions. This is far more useful than the LED codes alone.

**My SL297NV starts, fires for a few seconds, then shuts off. What's happening?**
This is almost always the flame sensor. The igniter lights the burner, but the flame sensor (covered in carbon deposits or failing) can't confirm a flame to the control board, so the board cuts the gas valve as a safety measure. Clean the flame sensor first, it's a 10-minute job with a 90% success rate for this symptom.

**The furnace runs but the ECM blower seems to run slower than normal. Should I be worried?**
The SL297NV's variable-speed ECM is designed to vary speed based on system demand and static pressure. Running at lower speed on mild days is completely normal. It only becomes a fault if the blower can't meet heating demand or if Code E042 appears. If you suspect the motor speed is lower than it should be under load, have a technician check the motor speed profile settings in the control board.

**How efficient is the SL297NV, and does running it in fault-reset mode affect efficiency?**
The SL297NV achieves up to 97.5% AFUE in two-stage operation. Frequent fault resets, especially ignition lockouts, cause the furnace to run in open-loop mode during re-ignition attempts, which is less efficient and stresses components. Repeated lockouts mean a real problem needs to be fixed, not just reset.

**The rollout switch tripped once. Can I just reset it and keep going?**
No. A rollout switch trip is a serious indicator of either a blocked flue, failed inducer, or a cracked heat exchanger. Any of these can result in carbon monoxide intrusion. Reset only after a thorough visual inspection, and if the cause is not obvious, call a technician before running the furnace again.
