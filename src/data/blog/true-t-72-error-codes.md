---
title: "True T-72 Refrigerator Error Codes - Full Fault Guide"
description: "True T-72 three-door reach-in commercial refrigerator error codes, temperature sensor faults, fan and defrost failures, and step-by-step repair instructions."
pubDatetime: 2026-04-25T00:00:00Z
author: "James Rutherford"
tags:
  - hvac
  - error-codes
---

The True T-72 is a three-door reach-in commercial refrigerator that has been a workhorse in restaurant kitchens, cafeterias, and food service operations for decades. True Manufacturing built these units to last, but when the electronic controller starts displaying an error code or the unit isn't holding temperature, you need to act fast , a fully stocked T-72 represents thousands of dollars of food inventory. This guide covers all T-72 error codes, what each one means, and what to do about it.

## What Does a True T-72 Error Code Mean?

The True T-72 uses an electronic controller mounted inside the cabinet (typically behind the top grille or on the interior wall of the refrigerator section). Depending on production year, the controller is either a basic LED indicator type or an Embraco/Dixell digital controller with an alphanumeric display.

**On older T-72 units** (pre-2010 approximately): the controller uses a simple LED system , a flashing alarm LED and an alarm buzzer indicate a fault condition. Cabinet temperature is displayed on a dial or LED bar.

**On newer T-72 units** with Dixell XR40 or XR60 controllers: alphanumeric codes appear on the digital display.

### True T-72 Dixell Controller Error Codes

**E1 , Probe 1 Fault (Cabinet Temperature Probe Open/Short)**
The main cabinet air temperature probe has failed or its wiring has a fault. This is the most common error code on the T-72 with digital controls. Probe 1 monitors the cabinet's return air temperature , it's what the controller uses to decide when to call for cooling. Without Probe 1, the controller either runs cooling continuously (risks freezing product) or shuts cooling off entirely (risks food safety).

Action: Check the probe connector at the controller board for corrosion. Measure probe resistance with a multimeter , a standard NTC probe should read approximately 10,000 ohms at 77°F. Replace the probe if out of spec.

**E2 , Probe 2 Fault (Evaporator Coil Temperature Probe Open/Short)**
The evaporator temperature probe monitors coil temperature for defrost termination. When this probe fails, the controller cannot determine when the evaporator coil has reached defrost-off temperature. This causes either incomplete defrosts (leading to ice buildup on the evaporator) or excessively long defrost cycles (cabinet temperature rises too high during defrost).

Action: Same diagnostic approach as E1. The Probe 2 sensor is located on the evaporator coil , inspect for physical damage from ice build-up (cracked insulation on the wire) and check the connector.

**E3 , Probe 3 Fault (Condenser Temperature Probe Open/Short)**
On T-72 units equipped with a condenser probe, E3 indicates that probe has failed. The condenser probe is used for high-temperature protection of the condensing unit. Not all T-72 configurations have a Probe 3 , on units without it, E3 may indicate a configuration error.

**AL or HI , High Temperature Alarm**
Cabinet temperature has exceeded the high temperature alarm setpoint (typically set at 45°F). This is a critical food safety alert. The unit is still attempting to cool but cannot maintain safe temperature. Causes: failed condenser fan motor, dirty condenser coil, low refrigerant charge, failed compressor, door gaskets not sealing, or ambient temperature in the kitchen is too high.

Action: Check condenser fan is running. Clean condenser coil. Verify door gaskets seal fully (close a dollar bill in the door , it should not pull out easily). If the unit just had power restored after an outage, allow 2 hours to pull down temperature before alarming.

**LO , Low Temperature Alarm**
Cabinet temperature dropped below the low temperature alarm setpoint. On a refrigerator like the T-72, this typically means the defrost heater, defrost timer, or defrost termination thermostat has failed, causing the unit to run refrigeration without proper defrost cycling , eventually over-freezing the evaporator and then the cabinet itself. Also occurs if the unit is set too cold (setpoint accidentally changed).

Action: Check temperature setpoint first. If setpoint is correct, initiate a manual defrost cycle (hold the defrost button or access the controller menu). If the evaporator completely defrosts and temperature normalizes, the defrost system components need inspection.

**dF , Defrost in Progress**
Not an error , indicates a defrost cycle is actively running. On the T-72, defrost cycles run periodically (typically 2–4 times per day, each lasting up to 30 minutes). Cabinet temperature will rise during defrost; this is normal. If "dF" appears to be on continuously or appears more than 4 times per day, the defrost termination thermostat may have failed.

**EE or Er , EEPROM/Controller Fault**
The controller's internal memory has experienced an error. This is a controller hardware failure. Replace the Dixell controller. Before replacing, try power cycling the unit (unplug for 5 minutes) , some EE faults clear after a full power reset.

### LED-Only Models (Pre-Digital T-72): Alarm Interpretation

On older T-72 units without a digital display, diagnosis relies on:

- **Alarm LED + buzzer:** Cabinet temperature exceeded the alarm threshold (typically 45°F). Check all the same causes as the digital "AL" code above.
- **Continuous compressor run (no cycling off):** Low refrigerant, dirty condenser, or failed condenser fan. The compressor runs but can't pull cabinet temperature down.
- **Compressor not running at all:** Compressor overload tripped, compressor failed, or start relay/capacitor failed.
- **Ice buildup on evaporator visible through interior:** Defrost system failure.

## How to Fix It

1. **Check the condenser coil first.** Dirty condensers cause the majority of commercial refrigerator service calls. The T-72's condenser is located at the bottom front of the unit behind a removable grille. Pull the grille and inspect , in kitchen environments, the coil loads with grease rapidly. Clean with a condenser brush and commercial coil degreaser monthly.
2. **Verify the condenser fan.** With the unit running, the condenser fan (in the bottom compartment) should be running continuously. A failed condenser fan motor is a quick $30–$60 part replacement and causes immediate high temperature alarms.
3. **Check door gaskets.** Press your hand along each door gasket edge while the door is closed. You should feel no cold air escaping. A torn or compressed gasket on a three-door unit like the T-72 causes significant heat infiltration and is one of the most overlooked causes of temperature problems.
4. **Initiate a manual defrost.** On the Dixell controller, hold the defrost button (varies by model , check label). Watch whether the evaporator coil defrosts completely within 20–25 minutes. If ice remains after a full defrost cycle, the defrost heater may be burned out.
5. **Test defrost heater continuity.** With power OFF, disconnect the defrost heater wires and test continuity with a multimeter. A good heater reads 15–50 ohms. Open reading (OL) = failed heater.
6. **Replace probe sensors (E1, E2, E3).** True T-72 probe sensors are NTC thermistors. Check the True parts catalog for the specific part number by model. Replacement is DIY-friendly , disconnect, remove the probe from its clip, install the new one.
7. **Clean the interior and evaporator.** At least once per quarter, remove interior shelving and clean the evaporator compartment cover. Debris and spilled food on the evaporator cover reduces airflow through the coil.

## Parts You May Need

| Part | Use | Buy on Amazon |
|------|-----|---------------|
| Dixell XR40 or XR60 Replacement Controller | Replace for EE/Er controller faults | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-true-t-72-error-codes&k=dixell+xr40+replacement+controller+commercial+refrigeration&tag=errorcodefixes-20) |
| NTC Temperature Probe (10K, Commercial Refrigeration) | Replace E1, E2, or E3 probe faults | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-true-t-72-error-codes&k=ntc+temperature+probe+dixell+commercial+refrigerator&tag=errorcodefixes-20) |
| True Refrigerator Door Gasket (T-72 spec) | Replace failing door seals causing temperature alarms | [View on Amazon](https://www.amazon.com/dp/B0FPF84HQP?ascsubtag=ecf-true-t-72-error-codes&tag=errorcodefixes-20) |
| Condenser Fan Motor (115V, 3-blade, for True Refrigeration) | Replace failed condenser fan motor | [View on Amazon](https://www.amazon.com/dp/B0D2L5NSMM?ascsubtag=ecf-true-t-72-error-codes&tag=errorcodefixes-20) |
| Defrost Heater (Glass Tube, 115V, commercial reach-in) | Replace burned-out defrost heater | [View on Amazon](https://www.amazon.com/dp/B07FVP4CY6?ascsubtag=ecf-true-t-72-error-codes&tag=errorcodefixes-20) |
| Refrigeration Coil Brush (stainless, 18") | Clean condenser coil in tight bottom compartment | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-true-t-72-error-codes&k=refrigeration+condenser+coil+cleaning+brush+18+inch&tag=errorcodefixes-20) |

## When to Call a Pro

- **Refrigerant-related diagnosis.** If condenser and fan are clean and operating correctly but the unit still can't maintain temperature, low refrigerant charge is likely. R-134a or R-404A work requires EPA Section 608 certification.
- **Compressor replacement.** A failed compressor on the T-72 requires refrigerant recovery, brazing, evacuation, and recharge , a full refrigeration service job.
- **Persistent defrost failure after heater replacement.** If the defrost heater passes continuity but the evaporator still ices up, the defrost timer, defrost termination thermostat, or defrost control logic needs professional diagnosis.

## FAQ

**Q: How cold should the True T-72 run?**
A: True T-72 is designed for 33°F–41°F cabinet temperatures. The optimal setpoint for most food service applications is 36°F–38°F. The factory default setpoint is typically 38°F. For produce storage, 34°F–36°F is preferred. Never set a T-72 below 33°F , you'll freeze product and potentially crack the evaporator drain pan.

**Q: My T-72 is humming but not cooling at all. Is that an error code or something else?**
A: A humming compressor that isn't cooling suggests the compressor is running but not building pressure , a sign of compressor mechanical failure (worn pistons/valves on a reciprocating compressor) or a refrigerant leak that has left the system with insufficient charge. This will not generate a temperature alarm until the cabinet warms. Call a technician immediately.

**Q: The T-72 high temperature alarm went off overnight. I silenced it and it seems fine now. Should I investigate?**
A: Yes. An overnight temperature alarm means the unit lost the ability to maintain temperature at some point , potentially for hours. First, check if food in the cabinet reached unsafe temperatures (above 41°F for more than 4 hours is the USDA guideline). Second, determine why it alarmed , check condenser cleanliness, fan operation, door gaskets, and whether there was a power event overnight.

**Q: Can I replace the Dixell controller on a True T-72 myself?**
A: Yes, Dixell controller replacement is straightforward. Document all the current settings before disconnecting the old controller (photograph the display with each parameter shown). The new controller ships with factory defaults and must be reprogrammed to match the original settings: setpoint, alarm thresholds, defrost schedule, and probe type. The Dixell XR40/XR60 programming manual is available free online.

## See Also

- [True Refrigeration E1 Error Code — Causes & Fix](/posts/true-refrigeration-e1-error-code/)
- [True T-49 Refrigerator Error Codes - What They Mean and How to Fix Them](/posts/true-t-49-error-codes/)
- [True Refrigeration E6 Error Code — High Temperature Alarm Causes & Fix](/posts/true-refrigeration-e6-error-code/)
- [True GDM-49 Glass Door Merchandiser Error Codes - Full Fault Guide](/posts/true-gdm-49-error-codes/)
