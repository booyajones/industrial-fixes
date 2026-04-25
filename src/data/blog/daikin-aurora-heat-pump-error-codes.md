---
title: "Daikin Aurora Heat Pump Error Codes - Cold Climate Fault Guide"
description: "Complete Daikin Aurora heat pump error code guide. All fault codes, cold climate operating range faults, defrost issues, and step-by-step fixes."
pubDatetime: 2026-04-25T00:00:00Z
author: errorcodefixes.com
tags:
  - hvac
  - error-codes
---

The Daikin Aurora is Daikin's purpose-built cold-climate heat pump, designed to deliver heat at outdoor temperatures as low as -13°F (-25°C). This makes it one of the most capable cold-climate heat pumps on the market, but its sophisticated variable-speed inverter compressor and extended operating range also mean a more complex fault code system than standard heat pumps. When your Aurora stops heating or cooling, the error code it stores is your fastest path to diagnosis.

## What Does a Daikin Aurora Error Code Mean?

The Aurora uses Daikin's standard alphanumeric fault code system, accessible through the thermostat or through the service button on the outdoor unit control board. Error codes use letters and numbers in a two to three character format. The first character indicates the subsystem; the digits indicate the specific fault within that subsystem.

**Accessing codes via thermostat:** On Daikin's communicating thermostat, navigate to Menu → Information → Error History. Codes appear with timestamps.

**Accessing codes via outdoor unit:** Press the service check button on the outdoor unit control board. The LED will flash a pattern: short flashes indicate the first character, long flashes indicate the second.

### Daikin Aurora Fault Code Reference

**A1 , Indoor Unit PCB Fault**
The indoor air handler's printed circuit board (PCB) has detected an internal fault. This code indicates a PCB component failure , check for obvious signs of damage (burnt components, swollen capacitors). If the board is in warranty, Daikin typically replaces it without charge for covered units.

**A3 , Indoor Unit Drain Fault**
The indoor unit's float switch has tripped, indicating the condensate drain pan is full. On the Aurora, this code is more common in cooling season. Clear the condensate drain line immediately using a wet-dry vacuum. Check that the drain line is sloped at least 1/4 inch per foot toward the drain outlet.

**A6 , Indoor Fan Motor Fault**
The indoor blower motor or its driver circuit has faulted. On Aurora air handlers, the ECM (electronically commutated motor) fan can develop issues after 5–8 years. Check the motor connector for corrosion and verify the motor shaft spins freely. The Aurora's indoor fan motor is controlled by the main PCB via a PWM signal , if the board doesn't get the expected tachometer feedback, it logs A6.

**C4 , Indoor Coil Thermistor Open/Short**
The thermistor (temperature sensor) on the indoor coil has failed open or shorted. This sensor is critical for refrigerant control. The Aurora's electronic expansion valve (EEV) uses this data to regulate refrigerant superheat. A failed C4 sensor causes the system to run inefficiently and eventually fault. Replace the sensor.

**C9 , Outdoor Coil Thermistor Open/Short**
Same failure type as C4, but on the outdoor coil sensor. In cold climate heat pump operation, this sensor is critical for defrost timing and compressor protection. A failed C9 sensor may cause excessive icing or insufficient heating at low outdoor temperatures.

**E1 , Outdoor Unit PCB Fault**
The outdoor unit's main control board has detected an internal fault. This often means board replacement. Before replacing, check for water intrusion in the outdoor unit cabinet (check all wiring penetration seals) and check for obvious component damage on the board.

**E3 , High-Pressure Switch Trip**
The refrigerant high-pressure protection switch has tripped. In cooling mode: dirty outdoor coil, failed outdoor fan motor, refrigerant overcharge, or extremely high ambient temperature. In heating mode (more common on cold climate units): dirty indoor coil, indoor fan not running, or restriction in refrigerant circuit. Clean the appropriate coil and verify fan operation.

**E4 , Low-Pressure Protection**
The system has detected low refrigerant pressure. On the Aurora, this code takes on additional significance because cold-climate heat pumps operating at extreme low temperatures inherently run at lower suction pressures. E4 at moderate outdoor temperatures (above 10°F) typically indicates a refrigerant leak or expansion valve problem. E4 at extreme temperatures (below -10°F) may be within normal operation range for some fault detection scenarios , check the installation manual for the Aurora's specific operating limits.

**E7 , Outdoor Fan Motor Fault**
The Aurora's outdoor fan motor has faulted. Cold climate operation puts additional stress on outdoor fan motors due to potential icing and low-temperature operation. Verify the fan blade spins freely (with power off). Check for ice accumulation around the fan , a common issue in heavy snowfall if the unit is improperly sited. Check motor winding resistance: should be within 10% across all winding pairs.

**F3 , Discharge Pipe Thermistor Fault**
The compressor discharge temperature thermistor has failed. This sensor directly monitors compressor outlet temperature and is critical for the Aurora's compressor protection at extreme low ambient temperatures. Without accurate discharge temperature data, the Aurora's inverter cannot properly protect the compressor. Replace the sensor immediately.

**L5 , Power Module Overload (Overcurrent)**
The inverter power module detected an overcurrent condition. On the Aurora, L5 is often associated with cold starts (attempting to run the compressor at full speed in extreme cold without adequate oil return). The Aurora has a low-ambient start sequence, but a failed start procedure or compressor mechanical issue triggers L5. Allow the system to warm for 30 minutes and retry. If L5 appears consistently at normal temperatures, the compressor may be starting to fail.

**U2 , Low Voltage / Power Supply Fault**
Supply voltage to the outdoor unit has dropped below safe operating levels. The Aurora's inverter is voltage-sensitive. Measure supply voltage at the outdoor unit disconnect: should be within 10% of nameplate (208–230V or 240V depending on installation). Low voltage at startup is a common issue on long wire runs from the main panel.

**U4 , Communication Error (Indoor to Outdoor)**
The indoor and outdoor units have lost communication. The Aurora uses a proprietary communication protocol over the S21 signal wire. Check all inter-unit wiring, particularly at the terminal block. The S21 wire must not be in the same conduit as high-voltage wiring.

**UF , Outdoor Fan or Compressor Locked Rotor**
A locked rotor condition detected in either the outdoor fan motor or the compressor. This is a hard fault requiring immediate shutdown. For the outdoor fan, check for physical obstruction (ice, debris). For the compressor, this may indicate mechanical failure , do not continue to attempt restarts.

### Cold Climate Operating Range Notes

The Daikin Aurora is rated to operate down to -13°F for heating. However, several fault codes manifest differently in extreme cold:

- **E4 (low pressure)** may trigger when outdoor temperatures drop below -5°F if refrigerant charge is on the lower end of acceptable , the system is still functioning normally but reaching the protection threshold
- **L5 (overcurrent)** on first morning startup after overnight temperatures below -10°F may represent a normal cold-start protection event rather than a hardware failure
- **Defrost cycle frequency** increases dramatically below 15°F; if defrost appears to run every 30–45 minutes, this is normal for the Aurora in extreme cold

## How to Fix It

1. **Write down the full error code.** Access the error history log rather than just noting the active fault , the Aurora may have stored multiple related faults that tell a clearer diagnostic story.
2. **Clean outdoor coil (E3, E7).** Use a garden hose at moderate pressure from inside the coil outward. Remove the top panel with screws to access the coil top. Flush until water runs clear.
3. **Check condensate drain (A3).** Locate the drain port on the indoor unit. Attach a wet-dry vac and suction for 30 seconds. Pour 1 cup of water into the drain pan to confirm free flow.
4. **Verify supply voltage (U2).** At the outdoor unit disconnect, measure L1 to L2 voltage with a multimeter under load (system attempting to run). Voltage below 208V on a 208/230V system causes repeated U2 faults. An electrician may need to check the supply circuit.
5. **Check communication wiring (U4).** With power off, inspect the S21 signal wire at both indoor and outdoor units. Verify it is not routed with line voltage wiring, is firmly seated in its terminal, and shows no physical damage.
6. **Allow cold-start recovery time.** For L5 or E4 after extreme low-temperature operation, don't force a restart. Allow 30–45 minutes at indoor ambient temperature for oil to return to the compressor and refrigerant to stabilize.

## Parts You May Need

| Part | Use | Buy on Amazon |
|------|-----|---------------|
| Daikin Compatible 10K Coil Thermistor | Replace C4 or C9 sensors | [View on Amazon](https://www.amazon.com/s?k=daikin+heat+pump+coil+thermistor+10k&tag=errorcodefixes-20) |
| Condensate Drain Line Cleaning Tablets (Rectorseal) | Prevent A3 drain faults by keeping drain clear | [View on Amazon](https://www.amazon.com/s?k=condensate+drain+pan+cleaning+tablets+hvac&tag=errorcodefixes-20) |
| 14/4 Multi-Conductor HVAC Wire (50 ft) | Replace communication and control wiring for U4 | [View on Amazon](https://www.amazon.com/s?k=14+4+multi+conductor+wire+hvac+50+feet&tag=errorcodefixes-20) |
| Digital Refrigerant Gauge Set (R-410A) | Check refrigerant pressures for E3, E4 diagnosis | [View on Amazon](https://www.amazon.com/s?k=digital+refrigerant+manifold+gauge+r410a&tag=errorcodefixes-20) |
| HVAC Digital Multimeter (Fluke 116) | Test voltage, motor resistance, and sensor values | [View on Amazon](https://www.amazon.com/s?k=fluke+116+hvac+multimeter&tag=errorcodefixes-20) |
| Outdoor Unit Winter Cover / Wind Baffle | Protect Aurora outdoor unit in extreme cold climates | [View on Amazon](https://www.amazon.com/s?k=heat+pump+outdoor+unit+winter+wind+baffle&tag=errorcodefixes-20) |

## When to Call a Pro

- **E3 or E4 that does not clear after coil cleaning and filter service.** Refrigerant pressure diagnosis and charge adjustment require EPA certification.
- **L5 (power module overcurrent) at normal outdoor temperatures.** Compressor mechanical failure or inverter module failure requires factory-trained diagnosis.
- **UF (locked rotor) on the compressor.** Never continue trying to start a locked rotor , it rapidly destroys the compressor and the inverter module.
- **A1 or E1 (PCB fault).** Circuit board faults on the Aurora's sophisticated inverter system should be diagnosed by an authorized Daikin service technician.
- **F3 (discharge thermistor fault).** Running the Aurora without accurate discharge temperature monitoring risks compressor damage, especially at extreme low ambient temperatures.

## FAQ

**Q: My Daikin Aurora runs in defrost mode very frequently when it's below 20°F outside. Is this normal or a fault?**
A: On cold-climate heat pumps, defrost frequency increases significantly at low ambient temperatures because the outdoor coil accumulates frost rapidly. Defrost cycles every 30–60 minutes at 10–20°F outdoor temperature is normal for the Aurora operating at full heating capacity. If defrost runs but doesn't complete (you see error U4 or E4 immediately after defrost), then there is a fault in the defrost termination circuit.

**Q: The Daikin Aurora shows a fault code then clears it on its own without me doing anything. Should I be concerned?**
A: Yes. Self-clearing fault codes indicate intermittent faults that the system can recover from automatically , but intermittent faults are often early-stage hardware failures. Log every fault code with its timestamp. If the same code appears repeatedly over a few weeks, schedule a service call before it becomes a system-down failure.

**Q: Can the Daikin Aurora operate during a power outage if I have a backup generator?**
A: Yes, but the generator output must be clean sine wave (not modified sine wave) and sized appropriately. The Aurora's inverter compressor requires clean AC power. Modified sine wave generators cause inverter faults (U2, E1). A properly sized whole-home inverter generator of at least 5,000W continuous output is needed for a typical Aurora system.

**Q: My Aurora shows E4 (low pressure) but only during cooling, not heating. Is that consistent with a refrigerant leak?**
A: Refrigerant leaks will typically manifest during both heating and cooling, but the symptoms are more severe in cooling mode (where suction pressures are naturally lower). A leak that causes E4 in cooling but not obvious symptoms in heating suggests a small, slow leak. Have a technician check static refrigerant pressure and perform a leak search.
