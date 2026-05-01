---
title: "Tempstar Ion Heat Pump Error Codes - Fault Code Diagnostics"
description: "Full fault code reference for the Tempstar Ion variable-speed heat pump, covering all Ion system communicating errors, control board faults, and step-by-step troubleshooting. Includes sensor, reversing valve, and compressor lockout diagnostics."
pubDatetime: 2026-04-25T00:00:00Z
author: "Marcus Webb"
tags:
  - hvac
  - error-codes
---

The Tempstar Ion is ICP Group's premium variable-speed heat pump, sharing the same Ion communicating platform with Heil and Comfortmaker. It's a sophisticated system — variable-speed compressor, electronic expansion valve, and two-wire communicating thermostat integration — and when it faults, it tells you exactly what's wrong. But only if you know the code.

This guide decodes every Tempstar Ion heat pump fault code and walks you through the diagnostic and repair steps.

## What Does the Tempstar Ion Error Code Mean?

The Ion label on Tempstar (and Heil) units identifies the communicating control architecture. Unlike older non-communicating systems where you only got basic on/off fault behavior, the Ion platform sends bidirectional data between the outdoor unit, the air handler, and the thermostat. Every fault is logged, timestamped, and categorized as either a soft fault (auto-recoverable) or a hard lockout (requires manual reset).

The Ion System Control Thermostat is your primary diagnostic interface. Navigate to **Settings → Service → Fault History** to pull the full log. If you don't have the communicating thermostat, the control board LED on the outdoor unit flashes fault codes in sequences.

---

## Tempstar Ion Heat Pump Fault Codes

### Fault 1 — High Pressure Lockout
Discharge-side pressure exceeded the high-pressure switch setpoint (approximately 610 PSI on R-410A systems). The compressor shut down to prevent damage.

**Most common causes:**
- Dirty or blocked outdoor condenser coil
- Condenser fan not running at full speed
- Refrigerant overcharge
- Electronic expansion valve (EEV) not opening properly

**What to do:** Power down the unit and inspect the condenser coil for debris — leaves, cottonwood, and grass clippings are frequent culprits. Clear debris, hose off the coil gently, and confirm the fan blades spin freely. If the coil is clean, you'll need refrigerant gauges to check for overcharge. Do not restart repeatedly after a high-pressure lockout without identifying the cause.

### Fault 2 — Low Pressure Lockout
Suction-side pressure dropped below the low-pressure switch setpoint. This is almost always a refrigerant-related fault.

**Most common causes:**
- Low refrigerant charge due to a leak
- Frozen indoor coil from restricted airflow
- Failed electronic expansion valve (stuck closed)

**What to do:** Check the air filter before assuming a refrigerant problem. A severely clogged filter restricts indoor coil airflow enough to freeze the coil and drop suction pressure. If the filter is clean and the indoor coil isn't frozen, suspect a refrigerant leak and call a licensed HVAC technician.

### Fault 3 — Defrost Fault
The defrost cycle failed to complete or didn't initiate when expected. The Tempstar Ion uses demand-based defrost — the outdoor coil sensor triggers defrost only when frost is actually detected, making Fault 3 relatively uncommon unless there's a specific sensor or valve problem.

**Most common causes:**
- Failed outdoor coil temperature sensor (see Fault 4)
- Reversing valve not switching to cooling mode during defrost
- Extremely heavy frost accumulation from low refrigerant charge

**What to do:** Trigger a manual defrost cycle via the Ion thermostat service menu. Listen for the reversing valve to click when the cycle initiates. If no click is heard and the solenoid tests open, replace the solenoid coil.

### Fault 4 — Outdoor Coil Sensor Fault
The outdoor coil thermistor is reading out of range, open, or shorted. This sensor is critical for defrost control.

**What to do:** Locate the sensor clipped to the outdoor coil tubing. Disconnect and measure resistance — at approximately 77°F (25°C), most NTC thermistors read near 10kΩ. An open reading (OL on the multimeter) or very low resistance indicates a failed sensor. Replacement sensors are inexpensive and clip-on.

### Fault 5 — Outdoor Ambient Sensor Fault
The outdoor ambient air temperature sensor has failed. This sensor helps the control system determine capacity limits, defrost frequency, and efficiency optimization.

**What to do:** The ambient sensor is typically mounted inside the outdoor unit cabinet, near the control board. Unplug and test resistance in the same manner as Fault 4. Replace if out of spec.

### Fault 6 — Indoor Coil Sensor Fault
The indoor coil thermistor is failed or reading implausibly. On variable-speed systems, this sensor is part of the EEV control loop — without accurate coil temperature data, the system can't properly regulate refrigerant flow.

**What to do:** Access the air handler, locate the thermistor clipped to the indoor coil tubing, and test resistance. This is a straightforward DIY sensor replacement on most Ion-platform air handlers.

### Fault 7 — Blower Motor Fault
The air handler's variable-speed ECM blower motor reported a fault or failed to achieve the requested airflow within its timeout window.

**Most common causes:**
- Blocked return air (collapsed duct, closed registers)
- Very dirty air filter
- ECM motor module failure
- Communication issue between air handler control board and motor

**What to do:** Check all air restrictions first — this is the most common cause of Fault 7. If airflow is unrestricted and the motor still faults, the ECM module (the electronics bolted to the back of the motor) may have failed. On many Tempstar air handlers, the module can be replaced separately from the motor — verify compatibility before ordering.

### Fault 8 — Communication Fault
The Ion system bus lost communication between components. One of the units — outdoor, indoor, or thermostat — has dropped off the two-wire data bus.

**Most common causes:**
- Loose or damaged communication wire terminal
- Reversed wire polarity
- Failed control board
- Power loss to one component

**What to do:**
1. Verify both units have power (check breakers for both indoor and outdoor units)
2. Inspect the two-wire communication bus connections at both control boards and the thermostat
3. Check for correct polarity — the Tempstar Ion communication bus is polarity-dependent
4. Look for damaged, kinked, or pinched wiring between units
5. Re-strip and re-terminate any suspicious connections

### Fault 9 — Compressor Fault / Inverter Lockout
The variable-speed compressor's inverter drive detected an abnormal condition and initiated a hard lockout. This protects the compressor from damage.

**Most common causes:**
- Input voltage out of specification
- Compressor winding fault (short to ground, phase-to-phase short)
- Inverter drive overtemperature
- Rapid cycling damage from repeated short-cycling

**What to do:** This is a hard lockout requiring manual reset. Wait 30 full minutes before attempting restart. Check supply voltage at the outdoor unit disconnect — it must be within ±10% of nameplate rating (typically 208–240V). If the unit locks out again immediately after a proper restart, do not continue cycling. Call a technician — the inverter drive or compressor requires professional diagnosis.

### Fault 10 — Reversing Valve Fault
The reversing valve failed to shift between heating and cooling mode as commanded by the control board. The system detected operation in the wrong refrigerant flow direction.

**Most common causes:**
- Failed reversing valve solenoid coil (open circuit)
- Mechanically stuck valve spool
- Low 24V control voltage

**What to do:** Measure solenoid coil resistance across the two terminals — expect 20–40Ω depending on the model. An open reading means the coil is burned out and should be replaced. If the coil tests good, the valve spool may be mechanically stuck — this requires refrigerant recovery by a licensed technician.

### Fault 11 — High Discharge Temperature
The discharge line sensor detected compressor discharge temperatures above safe limits. This often accompanies low refrigerant charge or failed EEV operation.

**What to do:** Don't restart repeatedly. Check for other fault codes present simultaneously — Fault 2 (low pressure) alongside Fault 11 is a strong indicator of low refrigerant charge. Call a technician.

---

## How to Fix It

1. **Pull the fault history** from the Ion thermostat first — timestamps and frequency tell you whether this is a one-time event or a developing failure.
2. **Start with the air filter** — replace it before anything else. Restricted airflow causes Faults 2, 6, 7, and sometimes 1.
3. **Clean the outdoor coil** — use a garden hose at low pressure on the exterior fins. Never use a pressure washer.
4. **Test all thermistors** — sensors fail before boards do. A $20 sensor is always the first thing to rule out.
5. **Check communication wiring** — re-terminate all connections if Fault 8 is present.
6. **Verify supply voltage** — use a multimeter at the disconnect when the fault is active.
7. **For refrigerant faults (Faults 1, 2, 11)** — limit restarts to two attempts before calling a pro. Continued operation under a refrigerant fault damages the compressor.

---

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|-------------|
| [NTC Thermistor Sensor for Heat Pump](https://www.amazon.com/s?k=NTC+thermistor+10K+HVAC+heat+pump+sensor&tag=errorcodefixes-20) | Fixes Faults 4, 5, 6 — coil and ambient sensor replacements | $12–$40 |
| [Heat Pump Reversing Valve Solenoid](https://www.amazon.com/s?k=heat+pump+reversing+valve+solenoid+coil+replacement&tag=errorcodefixes-20) | Fault 10 fix; solenoid replacement resolves most valve faults | $20–$55 |
| [ECM Blower Motor Replacement Module](https://www.amazon.com/s?k=ECM+motor+module+replacement+HVAC&tag=errorcodefixes-20) | Fault 7 fix; often cheaper than replacing full ECM motor assembly | $75–$250 |
| [Digital Multimeter with AC Voltage](https://www.amazon.com/dp/B08ZJSN5X3?tag=errorcodefixes-20) | Essential for testing sensors, voltage, and solenoid coils | $25–$85 |
| [HVAC Communication Wire 18/2](https://www.amazon.com/s?k=HVAC+thermostat+wire+18+2+communication&tag=errorcodefixes-20) | Replaces damaged Ion system bus wiring for Fault 8 | $12–$35 |

---

## When to Call a Pro

Call a licensed HVAC technician if:

- **Fault 9 (compressor/inverter lockout) won't clear** — the inverter drive or compressor likely needs replacement
- **Faults 1 or 2 keep returning** after cleaning the coil and verifying airflow — refrigerant system work requires certification
- **Fault 10 persists** after solenoid replacement — a stuck valve spool requires refrigerant recovery
- **Multiple faults appear simultaneously** — complex fault combinations usually indicate a failing control board or refrigerant system issue

The Tempstar Ion is a premium system. Its variable-speed technology and electronic controls make it far more efficient than conventional heat pumps — but they also mean diagnosis requires the right tools and knowledge. Use the fault log to give your tech a head start.

---

## Frequently Asked Questions

**Q: The Tempstar Ion and Heil Ion show the same fault codes. Are they really identical systems?**

A: Yes — the Tempstar Ion and Heil Ion heat pumps are built on the same ICP Group platform, share identical control boards, sensors, fault codes, and service procedures. The only differences are cosmetic (cabinet color, badge) and the dealer network through which they're sold. A Heil Ion service manual is fully applicable to the Tempstar Ion. Parts are completely interchangeable.

**Q: My Tempstar Ion shows Fault 3 (defrost fault) every winter. Is this a problem?**

A: Occasional defrost faults in extreme cold weather are less concerning than faults that occur repeatedly at moderate temperatures. If Fault 3 only appears during sub-zero events, the system may be reaching its operational limits — check your model's minimum operating temperature spec. If Fault 3 appears at normal winter temperatures, inspect the outdoor coil sensor and verify the reversing valve is switching properly. Repeated defrost faults in moderate weather suggest a failing sensor or valve solenoid.

**Q: Can I use any communicating thermostat with the Tempstar Ion, or does it need the Ion-specific model?**

A: The Tempstar Ion requires a communicating thermostat compatible with the Ion System Control protocol. The Ion System Control Thermostat is the intended pairing. Non-communicating thermostats will work for basic on/off control but will lose variable-speed modulation, fault logging, and efficiency optimization — essentially turning your premium variable-speed system into a single-stage unit. Use the Ion thermostat to get what you paid for.

**Q: How is the Tempstar Ion different from the Tempstar regular heat pump models?**

A: The "Ion" designation specifically identifies units using the Ion communicating platform with variable-speed compressor technology. Standard Tempstar heat pumps (non-Ion models) use single or two-stage compressors and simpler control boards. The fault code systems are different — this guide applies only to Tempstar Ion models.
