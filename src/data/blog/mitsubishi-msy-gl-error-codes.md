---
title: "Mitsubishi MSY-GL Mini-Split Error Codes - Full Fault Guide"
description: "Complete Mitsubishi MSY-GL mini-split error code reference. All P-series flash codes, remote control codes, and diagnostic faults with DIY fix steps."
pubDatetime: 2026-04-25T00:00:00Z
author: errorcodefixes.com
tags:
  - hvac
  - error-codes
---

The Mitsubishi MSY-GL series is a single-zone ductless mini-split available in 9,000 to 24,000 BTU capacities. As an inverter-driven system using R-410A (or R-32 in newer production), it offers precise temperature control but also sophisticated self-diagnostics. When the MSY-GL detects a problem, it displays a code on the remote controller LCD, blinks the indoor unit's operation lamp in a specific pattern, and in some configurations stores the fault in memory accessible via a wireless remote test function.

## What Does a Mitsubishi MSY-GL Error Code Mean?

The MSY-GL uses two diagnostic systems simultaneously:

**Remote controller display codes** , alphanumeric codes visible on the remote's LCD when a fault is active. These follow Mitsubishi's standard "P" and "E" naming convention.

**Indoor unit LED flash codes** , the indoor unit's OPERATION lamp (green) and TIMER lamp (orange) blink in patterns. Count the OPERATION lamp blinks for the first digit, then the TIMER lamp blinks for the second digit.

### P-Series Flash Codes (Alphanumeric Display)

**P1 , Intake Sensor Error**
The room temperature thermistor (the sensor that reads intake air temperature through the front panel) has failed or is disconnected. Without this sensor, the unit cannot regulate room temperature accurately. Check the sensor's connector on the indoor PCB and test resistance: the MSY-GL intake sensor should read approximately 10K ohms at room temperature.

**P2 , Pipe (Liquid Line) Temperature Sensor Error**
The refrigerant pipe temperature sensor clipped to the indoor coil's liquid line has failed. This sensor monitors refrigerant state during operation. A failed P2 sensor causes the unit to run poorly and eventually fault. Replace the sensor , it clips onto the liquid line tubing.

**P4 , Drain Sensor Error**
The drain water level sensor in the condensate pan has detected a fault. This can mean the sensor itself has failed or the drain pan is filling with water (blocked drain, failed condensate pump). Check the drain line first , a simple clearing with a shop vac often resolves P4.

**P5 , Drain Float Switch Trip (Drain Full)**
The drain float switch has physically lifted, indicating the condensate pan is overflowing. The unit shuts down to prevent water damage. This is not a sensor failure , water is physically present. Clear the condensate drain immediately. A blocked drain line, improperly sloped installation, or failed drain pump causes P5.

**P6 , Freezing/Overheating Protection**
The unit has activated its protection mode due to the indoor coil operating outside safe temperature limits. In cooling mode, P6 means the coil is freezing (low refrigerant charge, low airflow from dirty filter or blocked return, or fan motor fault). In heating mode, P6 means the coil is overheating. Clean the filter first; if P6 returns immediately, suspect refrigerant charge issues.

**P8 , Outdoor Unit Protection (High Discharge Temp)**
The outdoor unit's compressor discharge temperature has exceeded safe limits. In cooling: dirty outdoor coil, failed outdoor fan, high ambient temperature, or refrigerant overcharge. In heating: low refrigerant or severe outdoor coil icing. Clean the outdoor coil and verify the outdoor fan runs freely.

**P9 , Inverter PCB Overheat Protection**
The outdoor unit's inverter board has overheated. The cooling fins on the outdoor unit's inverter module are dirty or blocked. This commonly occurs when the outdoor unit is installed in a confined space with inadequate clearance or when airflow is blocked by vegetation, fencing, or snow accumulation around the unit.

**EE , Communication Error (Indoor to Outdoor)**
The indoor and outdoor units have lost communication. Check the inter-unit wiring: the MSY-GL uses a 3-wire or 4-wire cable between indoor and outdoor units (L1, L2/Neutral, Ground, and S for signal). The S (signal) wire is the communication wire. Verify it's connected firmly at both units and is not damaged.

### LED Flash Code Table

| OPERATION Blinks | TIMER Blinks | Code | Meaning |
|-----------------|-------------|------|---------|
| 1 | 1 | 6607 | Room sensor fault (= P1) |
| 1 | 2 | 6608 | Pipe sensor fault (= P2) |
| 2 | 1 | 6810 | Outdoor fan fault |
| 2 | 3 | 6813 | Compressor fault |
| 3 | 1 | 6203 | Drain fault (= P4) |
| 3 | 5 | 6207 | Drain overflow (= P5) |
| 4 | 1 | 1301 | Coil temp (freeze/overheat, = P6) |
| 5 | 1 | 6601 | Outdoor protection (= P8) |
| 5 | 4 | 6831 | Inverter overheat (= P9) |
| 8 | 8 | EE | Communication fault |

## How to Fix It

1. **Read the remote controller display first.** The alphanumeric code on the remote is the most direct diagnosis tool. If the remote shows P1, P2, P4, etc., that's your starting point. If the remote is not displaying a code but the unit is stopped, hold the CHECK button on the remote for 5 seconds to enter diagnostic mode and retrieve stored faults.
2. **Clean the air filter.** A dirty filter causes P6 in cooling mode, and is the easiest fix. The MSY-GL's filter is accessible by lifting the front panel. Wash it with warm water, dry it completely, and reinstall.
3. **Check the condensate drain (P4, P5).** Locate the drain outlet on the side or bottom of the indoor unit. Attach a wet-dry vac to the drain outlet and suction for 30 seconds to clear any blockage. Pour a cup of water into the pan after cleaning to confirm free flow.
4. **Inspect the outdoor unit.** For P8 and P9, go to the outdoor unit. Check that the condenser fins are not clogged with dirt or debris. Verify the outdoor fan blade spins freely by hand (with power off). Clean the fins with a gentle hose spray from inside out.
5. **Check inter-unit wiring for EE.** Locate the inter-unit terminal strip on both the indoor and outdoor units. Verify that all three or four wires (especially the S signal wire) are seated firmly in their terminals and are not corroded. Tighten terminal screws if loose.
6. **Test sensors with a multimeter.** For P1 and P2, access the indoor unit PCB, unplug the suspect sensor connector, and measure resistance across the two sensor wires. At 77°F (25°C), sensors should read close to 10,000 ohms. A reading of zero or infinite resistance confirms a failed sensor.
7. **Check refrigerant charge (P6 persistent, P8).** If P6 returns immediately after cleaning the filter and the airflow is good, low refrigerant is likely. Call a licensed technician to check refrigerant charge with gauges.

## Parts You May Need

| Part | Use | Buy on Amazon |
|------|-----|---------------|
| Mitsubishi MSY-GL Replacement Remote Controller | Replace failed remote; also used to retrieve fault codes | [View on Amazon](https://www.amazon.com/s?k=mitsubishi+mini+split+replacement+remote+controller&tag=errorcodefixes-20) |
| 10K NTC Thermistor Sensor (for MSY series) | Replace P1 intake or P2 pipe sensor | [View on Amazon](https://www.amazon.com/s?k=10k+ntc+thermistor+mini+split+temperature+sensor&tag=errorcodefixes-20) |
| Mini-Split Condensate Drain Pump | Install if gravity drain is insufficient; resolves persistent P4/P5 | [View on Amazon](https://www.amazon.com/s?k=mini+split+condensate+drain+pump+230v&tag=errorcodefixes-20) |
| Nu-Calgon Coil Cleaner (No-Rinse Spray) | Clean indoor coil to improve airflow and resolve P6 | [View on Amazon](https://www.amazon.com/s?k=nu-calgon+no+rinse+coil+cleaner+hvac&tag=errorcodefixes-20) |
| 14/3 Multi-Conductor Wire (50 ft) | Replace corroded inter-unit wiring for EE communication faults | [View on Amazon](https://www.amazon.com/s?k=14+3+stranded+copper+wire+50+ft+hvac&tag=errorcodefixes-20) |
| Mini-Split Line Set Insulation Wrap | Protect refrigerant lines after service | [View on Amazon](https://www.amazon.com/s?k=mini+split+line+set+foam+insulation+wrap&tag=errorcodefixes-20) |

## When to Call a Pro

- **P6 that returns immediately after cleaning the filter.** Persistent freeze protection faults indicate low refrigerant charge or a failed expansion valve , both require a licensed HVAC technician with gauges.
- **P8 or P9 that returns after cleaning the outdoor unit.** Inverter or compressor failure diagnosis requires an inverter PCB tester and technical service documentation.
- **EE communication fault that persists after checking all wiring.** A shorted outdoor unit PCB or failed inverter communication circuit requires board-level diagnosis.
- **Any fault code accompanied by refrigerant odor.** Refrigerant leaks require EPA-certified technicians.
- **Fault codes that return within 24 hours of clearing.** A fault code that comes back immediately means the repair isn't complete , call for professional diagnosis rather than continuing to reset.

## FAQ

**Q: The MSY-GL shows no code on the remote but the unit just stopped working and the OPERATION light is blinking. How do I find the fault?**
A: Hold the CHECK button on the remote for 5 seconds. The remote enters a diagnostic mode that reads stored fault codes from the indoor unit's PCB memory. The last fault code is displayed on the remote screen. Write it down before pressing any other buttons , it clears when you exit.

**Q: My MSY-GL shows P6 only during cooling on very hot days. Is this normal or a sign of low refrigerant?**
A: P6 on hot days during peak load is a legitimate warning sign of undercharge. On a properly charged MSY-GL, P6 should not activate during cooling even on a 95°F day with the filter clean and airflow unrestricted. If you see P6 consistently above 85°F ambient, have refrigerant charge verified by a technician.

**Q: How often should I clean the MSY-GL filter?**
A: Mitsubishi recommends cleaning the filter every two weeks during periods of heavy use. In practice, monthly cleaning is adequate for most residential applications. The filter is washable , rinse it with warm water, air dry completely, and reinstall. Never run the unit without the filter in place; the indoor coil becomes a dust collector and degrades efficiency rapidly.

**Q: Can I add a second indoor unit to my MSY-GL outdoor unit?**
A: No. The MSY-GL outdoor units are single-zone only. If you need multi-zone capability, you would need to upgrade to a Mitsubishi MXZ multi-zone outdoor unit. The MSY-GL indoor heads are compatible with MXZ systems, so you could retain your indoor units if you replace the outdoor unit.
