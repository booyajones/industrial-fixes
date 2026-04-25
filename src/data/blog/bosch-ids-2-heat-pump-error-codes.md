---
title: "Bosch IDS 2.0 Heat Pump Error Codes — Full Diagnostic Guide - What It Means and How to Fix It"
description: "Bosch IDS 2.0 heat pumps use active E-codes and stored F-codes to flag communication, sensor, inverter, airflow, and refrigerant problems. This guide breaks down the major Bosch fault families and the repair steps that fix them without wasting time on blind resets."
pubDatetime: 2026-04-25T00:00:00Z
author: errorcodefixes.com
tags:
  - hvac
  - error-codes
---

The Bosch IDS 2.0, short for Inverter Ducted Split, became popular because it delivers variable-capacity performance without the price tag of some communicating systems from the biggest legacy brands. It is quiet, efficient, and forgiving in day-to-day operation. When it does fault, though, the system depends on code logic that blends the outdoor inverter, indoor air handler, temperature sensors, and the thermostat or interface board.

That means the code on the screen is only the first clue. A low-pressure code can come from a refrigerant leak, but it can also come from an airflow problem, a stuck electronic expansion valve, or a sensor reading that no longer matches the actual condition. The goal is to read the code, then prove the cause in order.

## What Does Bosch IDS 2.0 Heat Pump Error Codes Mean?

Bosch IDS 2.0 systems normally use two code families.

**E-codes** are active faults. These are the codes that stop operation or force the unit into protective behavior. If the system is down right now, you are usually working from an E-code.

**F-codes** are stored or historical faults. Depending on the indoor interface, thermostat, and firmware version, F-codes may show up in service history, installer menus, or after the fault has cleared. In practice, the F-code usually points back to the same fault family as the related E-code. Technicians use them to catch intermittent issues that disappear before they arrive.

Bosch firmware can vary by outdoor model, indoor match-up, and control package, but the same trouble categories show up again and again.

**E01 or communication-family faults.** These point to lost communication between the indoor air handler, thermostat interface, and outdoor inverter section. Loose terminals, wrong wiring, weak 24-volt power, or a failed board are common causes.

**E02 or outdoor communication failure.** This usually means the outdoor section stopped answering the indoor controls. Start with line power to the condenser, then inspect the communication conductors and board plugs.

**E03, discharge temperature too high.** The compressor discharge line got too hot, or the board believes it did. Low charge, restricted airflow, a dirty outdoor coil, or a bad discharge sensor can all drive this code.

**E04, low-pressure protection.** The system sees suction pressure lower than expected. Refrigerant loss is common, but frozen indoor coils, plugged filters, weak airflow, or expansion valve trouble can do the same thing.

**E05, high-pressure protection.** The system sees excessive high-side pressure. Outdoor fan failure, a dirty condenser coil, refrigerant overcharge, or non-condensables after poor service work are common triggers.

**E06, inverter or IPM fault.** The outdoor inverter module detected overcurrent, overheat, a shorted component, or DC bus trouble. These faults are serious because they often involve high-voltage electronics or compressor failure.

**E07, low DC bus or input voltage issue.** The inverter is not seeing stable incoming power. Loose disconnect lugs, sagging utility voltage, weak connections, or a failing capacitor bank can cause it.

**E08, defrost sensor fault.** The outdoor coil or defrost thermistor is open, shorted, or reading outside the expected range.

**E09, indoor ambient or return-air sensor fault.** The indoor sensor is no longer giving the board believable temperature data.

**E10, compressor overload or high current.** The compressor is drawing more current than the inverter wants to allow. Locked rotor, failing windings, overcharge, or board trouble can all sit behind this code.

**E11, fan motor fault.** Either the indoor or outdoor fan failed to start, lost feedback, or is drawing abnormal current. On Bosch inverter systems, the fan and coil performance strongly influence refrigerant-side faults, so do not treat this as a simple motor code.

For **F-codes**, think of them as the fingerprint left behind after an event. If you see F03, F04, or F05 in history, the system likely saw the same discharge-temperature, low-pressure, or high-pressure condition earlier even if it is currently running. That is extremely useful on systems that fail only during cold mornings, hot afternoons, or defrost transitions.

## How to Fix It

1. **Start by recording both active and historical codes.** Use the thermostat, indoor interface, or service menu to capture every E-code and F-code you can find. If the unit faults only once a day, the history is more valuable than the live screen.

2. **Verify line voltage and low-voltage control power.** The outdoor unit should see stable high voltage within nameplate range, and the indoor controls should have solid 24VAC. Bosch inverter equipment does not like weak or intermittent power.

3. **Inspect communication wiring before condemning boards.** Re-seat every low-voltage terminal between thermostat, indoor unit, and outdoor section. Look for nicked cable, loose screws, crossed conductors, and splices exposed to moisture. E01 and E02 often turn out to be wiring, not electronics.

4. **For E03, E04, and E05, clean airflow paths first.** Replace the filter, inspect the indoor coil, verify blower operation, and wash the outdoor coil. Many Bosch refrigerant-related codes begin with airflow problems that changed system pressures.

5. **Check the outdoor fan on E05 and E11.** A fan that starts late, runs slow, or stops after a few minutes will push head pressure up and trip the system. Spin the blade by hand with power off and inspect the motor harness and module.

6. **Ohm the sensors on E08 and E09.** Bosch commonly uses thermistors that read near 10K ohms around room temperature. An open circuit, short, or wildly incorrect resistance tells you the sensor or its wiring has failed.

7. **Treat E06 and E10 as high-risk faults.** Before you try another restart, inspect the inverter area for overheated terminals, burned board spots, or oil stains that suggest compressor trouble. Measure compressor winding resistance if you know how to do it safely. If winding values are badly unbalanced, stop there.

8. **For E07, check the power path under load.** Measure supply voltage while the unit tries to start, not just when it is sitting idle. A disconnect, breaker lug, or feeder splice can pass a static voltage check and still collapse when the inverter demands current.

9. **If the unit runs in one mode but not the other, look at sensors and refrigerant behavior.** A Bosch system that cools but throws faults in heating often points to defrost logic, outdoor sensor trouble, or refrigerant conditions that only show up during the heating cycle.

10. **After the repair, clear the history and test cooling, heating, and defrost behavior if conditions allow.** If the same E-code returns right away, you still have an active failure. If only the old F-code remains, you likely solved the root cause.

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|-------------|
| [Bosch IDS inverter control board](https://www.amazon.com/s?k=Bosch+IDS+heat+pump+inverter+control+board&tag=errorcodefixes-20) | Replaces failed outdoor inverter electronics behind E06, E07, or repeated communication faults after wiring checks out | $380 to $650 |
| [10K HVAC thermistor sensor](https://www.amazon.com/s?k=10K+HVAC+thermistor+sensor&tag=errorcodefixes-20) | Replaces failed defrost, coil, discharge, or indoor temperature sensors behind E03, E08, and E09 | $15 to $45 |
| [Bosch air handler control board](https://www.amazon.com/s?k=Bosch+air+handler+control+board&tag=errorcodefixes-20) | Replaces indoor electronics that stop communicating with the outdoor section or thermostat | $220 to $420 |
| [ECM condenser fan motor](https://www.amazon.com/s?k=ECM+condenser+fan+motor+heat+pump&tag=errorcodefixes-20) | Replaces a failed outdoor fan motor that contributes to E05 and E11 faults | $180 to $320 |
| [24V HVAC transformer](https://www.amazon.com/s?k=24V+HVAC+transformer&tag=errorcodefixes-20) | Restores stable control voltage when communication or sensor codes appear with random resets | $20 to $50 |
| [Liquid line filter drier](https://www.amazon.com/s?k=liquid+line+filter+drier+refrigerant&tag=errorcodefixes-20) | Used during sealed-system repairs when restriction or contamination contributes to temperature and pressure faults | $20 to $60 |

## When to Call a Pro

Call a licensed HVAC technician for any Bosch IDS 2.0 fault that involves refrigerant pressures, compressor current, or inverter module protection. E03, E04, E05, E06, E07, and E10 can all point to problems that require gauges, amp-draw testing, and safe handling around high-voltage DC components.

You should also call a pro if the unit keeps posting communication faults after you have verified wiring and control voltage. At that point the likely causes are board failure, firmware mismatch, or a system setup issue that needs Bosch service literature and live electrical testing.

## Frequently Asked Questions

**Q: What is the difference between an E-code and an F-code on Bosch IDS 2.0?**  
An E-code is usually an active fault that is affecting operation right now. An F-code is usually a stored or historical fault that tells you what happened earlier.

**Q: Can a dirty filter really cause a Bosch low-pressure code?**  
Yes. Poor indoor airflow can pull evaporator pressure down enough to create a low-pressure style fault even when the refrigerant charge is correct.

**Q: My Bosch system resets, then faults again in ten minutes. Should I keep trying?**  
No. Repeated resets on inverter equipment can turn a marginal board or compressor problem into a larger failure. Record the code and diagnose the cause first.

**Q: Why does the system run in cooling but fault in heating?**  
That pattern often points to defrost sensor trouble, outdoor temperature sensor issues, reversing logic, or refrigerant behavior that only shows up in heat mode.

**Q: Do Bosch IDS 2.0 systems always use the same code list?**  
No. The exact display can vary by thermostat, indoor interface, and firmware revision. The fault families stay consistent, though: communication, sensor, fan, pressure, voltage, and inverter protection.