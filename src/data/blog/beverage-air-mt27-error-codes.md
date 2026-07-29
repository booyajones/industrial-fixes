---
title: "Beverage-Air MT27 Error Codes - What They Mean and How to Fix Them"
description: "The Beverage-Air MT27 displays fault codes on its digital controller when refrigeration or sensor problems occur — this guide covers every error code specific to the MT27 model, how to diagnose each one, and the exact parts needed."
pubDatetime: 2026-04-25T00:00:00Z
tags: [hvac, error-codes, beverage-air, commercial-refrigerator]
---

## What Does a Beverage-Air MT27 Error Code Mean?

The Beverage-Air MT27 is a 27-cubic-foot merchandiser-style reach-in refrigerator commonly found in convenience stores, bars, and food service kitchens. It uses a Dixell or equivalent digital controller that monitors cabinet temperature and sensor inputs, displaying error codes when something is out of range.

Error codes on the MT27 appear on the controller's digital readout, often alternating between the set temperature and the fault code. Unlike some commercial units that simply stop functioning without explanation, the MT27's controller gives you a starting point for diagnosis.

**Important:** Beverage-Air uses several different controller models across the MT27 production run. The most common is the Dixell XR06CX or equivalent. If your controller looks different from the standard Dixell keypad layout, check the manual inside the unit's service panel for your specific controller's error code list.

---

## Beverage-Air MT27 Error Codes

### E1 — Probe 1 Fault (Cabinet Air Sensor)

**What it means:** The primary cabinet air temperature sensor is reading out of range, has an open circuit, or has a short circuit. This is the sensor the controller uses to maintain cabinet temperature.

**Symptoms:** Display alternates between set temperature and E1. The unit may continue running at a default output level or shut down the compressor, depending on controller configuration.

**Diagnosis and fix:**
1. Locate probe 1 — it's typically positioned inside the cabinet in the return air stream, often near the top of the unit behind the evaporator cover.
2. Check the wiring connector where it plugs into the controller board — corrosion and loose pins are responsible for the majority of E1 errors.
3. With the probe disconnected, measure resistance with a multimeter:
   - At 77°F (25°C): approximately 10 kΩ
   - At 35°F (2°C): approximately 25–30 kΩ
4. If resistance is open (infinite) or shorted (near 0 ohms), the probe has failed. Replace with a compatible NTC 10K thermistor probe.
5. If resistance is within range, the problem is the connection or the controller board.

**Part:** NTC 10K thermistor probe, 6-inch insertion type — compatible with Dixell XR06CX. Available from Parts Town and Beverage-Air parts distributors. Typical Beverage-Air part number for cabinet probe: **502-022A** (verify against your model's parts diagram).

### E2 — Probe 2 Fault (Defrost / Evaporator Sensor)

**What it means:** The evaporator coil temperature sensor is out of range or has failed. This sensor controls defrost termination — it tells the controller when the evaporator coil has warmed up enough to end a defrost cycle.

**Symptoms:** E2 code on display. Common secondary symptom: the unit gets stuck in defrost mode (if the controller can't confirm defrost is done, it runs defrost indefinitely, which eventually raises cabinet temperature and triggers a secondary alarm).

**Diagnosis and fix:**
1. Locate probe 2 — it's clipped to the evaporator coil fins, typically in the middle or upper section of the evaporator.
2. If the evaporator is iced over, run a manual defrost first. On the Dixell XR06CX: press the DEF button once to initiate manual defrost.
3. After defrost, test probe resistance same as E1 procedure.
4. Check that the probe is properly clipped to the coil — if it's floating in air rather than contacting the coil surface, it gives incorrect readings and may cause E2.

**Part:** Evaporator coil probe, NTC 10K — Beverage-Air part **502-023A** (verify). Same basic spec as the cabinet probe but may have a longer lead or different clip.

### E3 — High Temperature Alarm

**What it means:** Cabinet temperature has risen above the high-temperature alarm setpoint (the controller default is typically set point + 9°F, or approximately 46°F for a refrigerator set at 37°F). The cabinet is genuinely too warm — this is a temperature alarm, not a sensor fault.

**Common causes:**
- Dirty condenser coil
- Failed condenser fan motor
- Failed evaporator fan motor
- Door gasket failure
- High ambient temperature (above 90°F around the unit)
- Low refrigerant charge

**Fix:**
1. Check condenser coil — pull the MT27 from the wall and inspect the rear-mounted condenser. Clean with compressed air if dusty.
2. Verify condenser fan and evaporator fan are both running. On the MT27, the evaporator fan is inside the cabinet (usually at the top behind a cover) and the condenser fan is at the rear of the unit.
3. Check door gaskets — run your hand around the door seal with the door closed. You should feel no cold air escaping. Replace gaskets that are torn, cracked, or flattened.
4. If fans and coil are fine, have a technician check refrigerant charge.

### E4 — Defrost Timeout

**What it means:** The defrost cycle failed to complete within the maximum allowed time (typically 45–60 minutes). The evaporator heater may have failed, the defrost termination sensor may not be reading correctly, or the hi-limit thermostat opened.

**Fix:**
1. Verify the defrost heater is energized during defrost — use a clamp meter to check for current draw on the defrost heater circuit.
2. Test defrost heater resistance: disconnect and measure. Expect 20–100 ohms depending on wattage. An open circuit = burned out heater.
3. Check the hi-limit thermostat (typically a disc-type thermostat in series with the heater) — it should have continuity at room temperature. If it's open, the heater circuit is interrupted.
4. Verify probe 2 is properly positioned — if it reads too cold (because it's touching a thick ice layer rather than the coil), defrost will run indefinitely until timeout.

### E5 — EEPROM / Controller Memory Fault

**What it means:** The controller's internal memory has a read/write error or configuration fault. Less common than E1–E4 but worth knowing.

**Fix:**
1. Power cycle the unit — unplug for 60 seconds.
2. If E5 returns after power cycle, the controller needs replacement.
3. Before replacing, verify input voltage to the controller is stable — voltage fluctuations can corrupt controller memory.

### Alarm (AL) — General Temperature Alarm

**What it means:** Some MT27 controllers display "AL" instead of E3 for a high-temperature alarm, or display AL alongside a fault code to indicate an active alarm condition.

The fix is the same as E3 — trace the cause of high cabinet temperature.

---

## How to Access and Configure the Dixell XR06CX Controller on the MT27

To view current temperature: the main display shows it continuously.

To change the set point:
1. Press and hold the **SET** button for 3 seconds.
2. Use the **up/down arrows** to adjust the set point.
3. Press **SET** again to confirm.

To initiate manual defrost:
- Press the **DEF** (snowflake) button once.

To access parameters (for technicians):
- Press and hold **SET** and **DOWN arrow** simultaneously for 5 seconds.
- Enter password (default: 22).
- Navigate parameters with arrows, press SET to confirm each.

---

## Parts You May Need

| Part | Why | Approx. Cost |
|------|-----|-------------|
| [Cabinet temperature probe — Beverage-Air 502-022A](https://www.amazon.com/s?ascsubtag=ecf-beverage-air-mt27-error-codes&k=Cabinet+temperature+probe+%E2%80%94+Beverage-Air+502-022A&tag=errorcodefixes-20) | E1 fault — cabinet sensor failed | $20–$40 |
| [Evaporator probe — Beverage-Air 502-023A](https://www.amazon.com/s?ascsubtag=ecf-beverage-air-mt27-error-codes&k=Evaporator+probe+%E2%80%94+Beverage-Air+502-023A&tag=errorcodefixes-20) | E2 fault — defrost termination sensor | $20–$40 |
| [Defrost heater (model-specific wattage)](https://www.amazon.com/s?ascsubtag=ecf-beverage-air-mt27-error-codes&k=Defrost+heater+%28model-specific+wattage%29&tag=errorcodefixes-20) | E4 — burned out heater | $45–$90 |
| [Hi-limit defrost thermostat](https://www.amazon.com/s?ascsubtag=ecf-beverage-air-mt27-error-codes&k=Hi-limit+defrost+thermostat&tag=errorcodefixes-20) | E4 — open thermostat interrupting heater | $15–$30 |
| [Condenser fan motor — Beverage-Air 501-052A](https://www.amazon.com/s?ascsubtag=ecf-beverage-air-mt27-error-codes&k=Condenser+fan+motor+%E2%80%94+Beverage-Air+501-052A&tag=errorcodefixes-20) | E3 — condenser fan failure | $60–$120 |
| [Evaporator fan motor — Beverage-Air 501-105A](https://www.amazon.com/s?ascsubtag=ecf-beverage-air-mt27-error-codes&k=Evaporator+fan+motor+%E2%80%94+Beverage-Air+501-105A&tag=errorcodefixes-20) | E3 — evaporator fan failure | $40–$80 |
| [Door gasket — MT27 (per door, left or right hinge)](https://www.amazon.com/s?ascsubtag=ecf-beverage-air-mt27-error-codes&k=Door+gasket+%E2%80%94+MT27+%28per+door%2C+left+or+right+hinge%29&tag=errorcodefixes-20) | E3 — seal failure causing warm cabinet | $35–$70 |
| [Dixell XR06CX controller](https://www.amazon.com/s?ascsubtag=ecf-beverage-air-mt27-error-codes&k=Dixell+XR06CX+controller&tag=errorcodefixes-20) | E5 or persistent unexplained faults | $60–$120 |

Verify all Beverage-Air part numbers against your MT27's specific serial number at Parts Town or Beverage-Air's parts portal. The MT27 series has had production changes across its run — using the serial number pulls the exact parts diagram for your unit.

---

## When to Call a Pro

- **E3 persisting after cleaning condenser and verifying fans:** Refrigerant charge or expansion device issue — requires EPA 608 certified technician and manifold gauges.
- **E4 recurring after heater replacement:** If the heater burns out repeatedly, the defrost cycle duration may be set too long, or the hi-limit thermostat is allowing too-high temperatures that stress the heater.
- **Refrigerant work on newer MT27 units:** Post-2020 Beverage-Air MT27 units may use R-290 (propane) refrigerant. Check the data plate. R-290 requires specific training and approved flammable refrigerant tools — do not service the refrigerant circuit without them.
- **Controller replacement with parameter reprogramming:** Replacement Dixell controllers ship with default parameters that may not match Beverage-Air's factory configuration. A technician can restore the correct parameter set from Beverage-Air's documentation.

---

## Frequently Asked Questions

**Q: My Beverage-Air MT27 display is flashing but I can't tell if it's a code or just the temperature. How do I read it?**

The Dixell XR06CX alternates between the set temperature and any active alarm or fault. Count the display cycles — it typically shows the temperature for 2 seconds and the fault code for 2 seconds. Stand in front of the unit and watch for a full cycle. If you see "E" followed by a number, that's your fault code.

**Q: How do I know what refrigerant my MT27 uses?**

Check the data plate on the rear or inside the compressor compartment. It lists the refrigerant type and charge weight. MT27 units built before approximately 2018 typically use R-134a. Newer units have been transitioning to R-290. Never add refrigerant to a unit without confirming what type it uses.

**Q: Can I replace the Dixell controller on the MT27 with a different brand?**

Technically yes, but you need a controller with compatible sensor inputs (NTC 10K thermistors), the same relay output configuration, and the correct defrost cycle logic. The Dixell XR06CX is widely available and the simplest replacement. Using a different controller requires verifying wiring compatibility and reprogramming all parameters from scratch.

**Q: Beverage-Air MT27 is not cooling but no error code shows. What should I check?**

If there's no error code, the sensors are reading in-range temperatures — which means either the cabinet is genuinely not cold (check if the compressor is running) or the sensors are mispositioned and reading ambient air instead of cold air. Check that the compressor starts and runs. If it runs but the cabinet doesn't cool, it's a refrigerant or refrigeration system issue. If the compressor doesn't start, check the compressor relay and capacitor.

**Q: The MT27 goes into defrost every 2 hours and it's affecting my product temperature. Is this normal?**

A defrost cycle every 2 hours is a common factory setting but may be too frequent for your environment. On the Dixell XR06CX, defrost interval is parameter **dI** (defrost interval). Access the parameter menu (SET + DOWN arrow, password 22) and adjust **dI** to a longer interval — 4–6 hours is typical for most commercial refrigerators. A more frequent defrost is sometimes needed in high-humidity environments but causes unnecessary temperature swings otherwise.
