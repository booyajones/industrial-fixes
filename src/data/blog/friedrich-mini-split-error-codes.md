---
title: "Friedrich Mini-Split Error Codes - What It Means and How to Fix It"
description: "Friedrich mini-split systems use E-codes and F-codes to report sensor faults, fan failures, pressure protection events, and communication problems. This guide covers the most important Friedrich Uni-Fit, Kühl, and ductless error codes in one place."
pubDatetime: 2026-04-25T00:00:00Z
author: "Dana Kowalski"
tags:
  - hvac
  - error-codes
---

Friedrich is a top-5 North American HVAC brand with over 70 years in the market, yet their mini-split error code documentation is nearly impossible to find online. If you've searched "Friedrich mini-split error code" and come up empty, you're not alone - Friedrich's error code documentation is scattered across installer manuals and is not indexed publicly in any comprehensive form. This guide consolidates Friedrich mini-split error codes across the Uni-Fit (FPHB), Kühl (FPHB/SS Series), and Ductless (MWHP/MWHPS Series) product lines.

## What Does Friedrich Mini-Split Error Codes Mean?

Friedrich mini-split systems use a two-part error code system visible on the indoor unit display or remote controller. Codes in the E-series (E1-E9) are temperature and pressure sensor faults. Codes in the F-series (F1-F9) are operational or protective faults related to the refrigerant cycle, compressor, and communication.

The indoor unit display shows the code as a flashing number or alphanumeric code. On some Friedrich models, the code also appears through LED blink sequences on the indoor unit status light - count blinks per cycle if the display is not showing a number.

Friedrich uses the same core control platform across the Uni-Fit, Kühl, and Ductless lines, so the E and F codes are consistent across model families. However, some codes are only active on specific models (for example, F8 condensate fault is only present on drain-pump equipped units).

### Friedrich Mini-Split E-Code Reference (Sensor Faults)

**E1 - Indoor Coil Temperature Sensor Fault (Indoor Unit)**
The indoor evaporator coil thermistor (Tc sensor) is reading outside its operational range.

Causes:
- Failed indoor coil thermistor
- Loose connector at the indoor control board
- Thermistor displaced from the coil fin - the sensor clips onto the evaporator coil and can fall off with vibration

Diagnostic: Disconnect the Tc sensor connector from the indoor board. Measure resistance at 70°F - expected reading is 10kΩ (10,000 ohms). Open circuit or zero ohms confirms failure. The sensor clips onto the indoor evaporator coil and typically has a 2-pin JST-style connector.

**E2 - Indoor Ambient (Room) Temperature Sensor Fault**
The indoor air temperature thermistor (Ta sensor) is faulty.

Causes:
- Failed indoor ambient thermistor
- Sensor physically blocked or in direct sunlight skewing readings
- Loose connector

Note: On Friedrich Kühl models, the indoor ambient sensor is sometimes integrated into the remote controller rather than the indoor unit itself. If the remote is showing E2, try replacing the remote's batteries - a dead remote battery can sometimes cause false E2 readings on Friedrich systems.

**E3 - Outdoor Ambient Temperature Sensor Fault**
The outdoor ambient thermistor is reading out of range.

Causes:
- Failed outdoor ambient sensor
- Moisture intrusion into outdoor unit sensor connector
- Wiring damage (UV degradation on outdoor units after 5+ years)

**E4 - Outdoor Coil Temperature Sensor Fault (Outdoor Unit)**
The outdoor heat exchanger (condenser) coil thermistor is faulty.

Causes:
- Failed outdoor coil sensor
- Physical damage from debris (a rock or hail strike on the outdoor unit fins can damage the sensor clip)
- Corrosion on the outdoor sensor connector

**E5 - Discharge Line Temperature Sensor Fault**
The compressor discharge temperature thermistor is reporting out-of-range values.

Causes:
- Failed discharge thermistor
- Wiring damage on the high-temperature discharge line area
- Connector corrosion from refrigerant oil mist

**E6 - Suction Line Temperature Sensor Fault**
The suction pipe thermistor (between evaporator and compressor inlet) is faulty.

Causes:
- Failed suction line thermistor
- Insulation-covered thermistor dislodged from the suction pipe

**E7 - High Pressure Sensor Fault (Some Models)**
On Friedrich models equipped with a pressure transducer (higher-end Ductless and Uni-Fit models), the high-side pressure transducer is reading out of range.

Causes:
- Failed pressure transducer
- Wiring fault on the signal cable

**E8 - Defrost Sensor Fault**
The defrost temperature sensor on the outdoor coil is faulty. Without this sensor, the unit cannot execute proper defrost cycles in heating mode.

Causes:
- Failed defrost thermistor
- Sensor displaced from clip position on outdoor coil

**E9 - Compressor Temperature Sensor Fault (Inverter Models)**
On Friedrich inverter models, the compressor body temperature sensor is faulty.

Causes:
- Failed compressor thermistor
- Heat damage to sensor wiring near compressor body

### Friedrich Mini-Split F-Code Reference (Operational Faults)

**F1 - High Pressure Protection Lockout**
The refrigerant system exceeded the high-pressure cutout threshold. The high-pressure switch (HPS) or pressure transducer tripped.

Causes:
- Dirty or blocked outdoor coil (condenser fins clogged with dirt, cottonwood seeds, or debris)
- Outdoor fan motor failure - fan not moving air across the condenser
- Refrigerant overcharge
- Ambient temperature exceeding the operating range (above 115°F outdoor ambient on some models)
- Kinked or blocked liquid line

**F2 - Low Pressure Protection / Freeze Protection Lockout**
The system pressure dropped below the low-pressure cutout, or the indoor coil thermistor detected freezing conditions.

Causes:
- Refrigerant leak
- Severely dirty indoor air filter restricting airflow across the evaporator
- Indoor fan motor failure
- Low outdoor ambient temperature operation without low-ambient kit
- Blocked return air

**F3 - Compressor Overcurrent / Overload**
The compressor drew more current than the control board's rated threshold.

Causes:
- Failed compressor (winding fault)
- Low voltage at the unit (below 200VAC on 208/230V systems)
- Locked rotor - compressor seized
- Failed compressor capacitor (on non-inverter models)
- Low refrigerant causing compressor to work harder

**F4 - Indoor Fan Motor Fault**
The indoor blower motor is not running at the commanded speed, has stalled, or failed to start.

Causes:
- Failed indoor ECM fan motor
- Blower wheel jammed with debris
- Failed motor capacitor (on AC motor models)
- Motor winding failure

**F5 - Communication Fault (Indoor to Outdoor)**
The communication between the indoor and outdoor unit control boards has been interrupted.

Causes:
- Damaged communication wiring (the multi-conductor communication cable between indoor and outdoor units)
- Reversed polarity on the communication bus
- Failed indoor control board
- Failed outdoor control board
- Power to one unit without power to the other

This is the most common F-code on Friedrich mini-splits installed by non-specialists. The communication cable must be wired to the correct terminals - on Friedrich units, this is typically labeled S, S1, or COM on both the indoor and outdoor terminal blocks.

**F6 - Outdoor Fan Motor Fault**
The outdoor condenser fan motor failed or is not reaching commanded speed.

Causes:
- Failed outdoor fan motor
- Fan blade obstructed (a twig or leaf inside the outdoor unit)
- Failed motor capacitor
- Motor control board fault

**F7 - Inverter / IPM Fault (Inverter Models)**
The inverter power module that drives the variable-speed compressor detected an overcurrent, overtemperature, or internal fault.

Causes:
- Compressor winding fault drawing excessive current
- IPM module failure
- High ambient temperature inside the outdoor unit reducing IPM heat sink cooling
- Refrigerant undercharge causing compressor to run hot

**F8 - Condensate Drain / Float Switch Fault (Models with Drain Pump)**
The condensate water level float switch activated, indicating the drain pump is not removing water or the drain is blocked.

Causes:
- Blocked condensate drain line (algae growth most common)
- Failed condensate drain pump
- Drain pump check valve stuck

**F9 - Mode Conflict / Mode Switch Fault**
Multiple indoor units connected to the same outdoor unit are calling for conflicting modes (one heating, one cooling) simultaneously, or the mode selector is receiving conflicting signals.

Causes (multi-zone systems):
- Individual zone settings calling for opposing modes simultaneously
- Failed mode switch
- Wiring error in multi-zone configuration

## How to Fix It

**Step 1: For any E-code, test the specific sensor.**
Friedrich sensors are all NTC thermistors. At 77°F (25°C), most read 10kΩ. At 32°F (0°C), they read approximately 32kΩ. At 104°F (40°C), they read approximately 5kΩ. An open circuit or zero ohms confirms failure. Most Friedrich sensors use simple 2-pin connectors and clip onto their respective coil sections - no refrigerant work is needed to replace them.

**Step 2: For F1 (high pressure), clean the outdoor coil first.**
Turn off the unit. Using a garden hose, spray water through the outdoor coil from the inside out (through the fan opening). Apply Coil Cleaner Spray (non-acid type) first if fins are heavily clogged. On Friedrich Uni-Fit models, the coil is a wrap-around design - clean all sides. Verify the outdoor fan spins when powered. F1 clears in the majority of cases once the coil is clean.

**Step 3: For F2 (low pressure / freeze), check the indoor filter first.**
Remove the indoor unit filter cover and inspect the filter. A completely clogged filter restricts airflow enough to ice the evaporator and trigger F2. Clean or replace the filter. Reconnect power and test. If F2 persists with a clean filter, inspect the indoor coil - ice formation confirms low refrigerant charge. Do not run the unit further without a refrigerant check by a certified HVAC technician.

**Step 4: For F5 (communication fault), trace the communication wire.**
The communication cable between indoor and outdoor units carries the control signals. Locate this cable (it's separate from the power cable - typically a smaller 3 or 4-conductor cable). Check both terminal blocks for loose connections. On Friedrich units, the communication terminals are labeled and the polarity matters - swap the S and S1 (or + and -) connections if F5 appeared after a recent installation or wire repair.

**Step 5: For F7 (inverter fault), check voltage at the outdoor unit first.**
Measure voltage at the outdoor unit disconnect during operation. On 208/230V systems, voltage should be between 197V and 253V. Voltage sag below 190V during startup can trigger F7 even with a healthy compressor. If voltage is normal and F7 persists, the IPM module requires replacement - this is a refrigerant-adjacent repair requiring a licensed technician.

**Step 6: For F8 (condensate fault), clear the drain line.**
Mix 1 cup of undiluted white vinegar and pour it into the indoor unit drain pan (access from behind the front panel after removing the filter). Let it sit for 30 minutes, then flush with clean water. On Friedrich ductless models with drain pumps, also verify the pump operates when 12VDC is applied directly to its terminals. A failed pump requires replacement.

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|-------------|
| [Friedrich Indoor Coil Thermistor (E1/E8 sensor)](https://www.amazon.com/s?k=Friedrich+mini+split+coil+thermistor+sensor&tag=errorcodefixes-20) | Replaces indoor coil or defrost temperature sensor | $15-$30 |
| [Friedrich Outdoor Ambient Thermistor (E3/E4)](https://www.amazon.com/s?k=Friedrich+mini+split+outdoor+thermistor&tag=errorcodefixes-20) | Replaces outdoor temperature sensor | $12-$25 |
| [Indoor ECM Fan Motor (F4)](https://www.amazon.com/dp/B0D2L5NSMM?tag=errorcodefixes-20) | Replaces failed indoor blower motor | $120-$220 |
| [Outdoor Fan Motor (F6)](https://www.amazon.com/dp/B0D2L5NSMM?tag=errorcodefixes-20) | Replaces failed condenser fan motor | $90-$180 |
| [Friedrich Indoor Control Board](https://www.amazon.com/dp/B0CNZGZ1HS?tag=errorcodefixes-20) | Replaces failed indoor PCB (F5 after wiring confirmed) | $120-$250 |
| [Friedrich Outdoor Control Board / IPM](https://www.amazon.com/dp/B0CNZGZ1HS?tag=errorcodefixes-20) | Replaces failed outdoor PCB or inverter module | $200-$450 |
| [Condensate Drain Pump (F8)](https://www.amazon.com/s?k=mini+split+condensate+drain+pump+replacement&tag=errorcodefixes-20) | Replaces failed condensate pump on drain-pump models | $35-$65 |
| [Coil Cleaning Spray (Non-Acid)](https://www.amazon.com/s?k=HVAC+coil+cleaner+non-acid+spray&tag=errorcodefixes-20) | Cleans blocked outdoor coil causing F1 | $12-$20 |

## When to Call a Pro

Friedrich recommends licensed HVAC technicians for all refrigerant-related work:

- **F1 that persists after coil cleaning**: May indicate refrigerant overcharge requiring recovery and recharge
- **F2 with confirmed ice on indoor coil and clean filter**: Refrigerant leak diagnosis and recharge requires EPA 608 certification
- **F7 (inverter fault)**: IPM module replacement is refrigerant-adjacent and requires expertise
- **Any refrigerant smell or visible oil staining on refrigerant lines**: Indicates a leak - call a pro immediately

For warranty service on Friedrich products, contact Friedrich's customer support at 1-800-541-6645. Friedrich offers a 5-year parts and labor warranty on most mini-split systems when installed by a licensed contractor.

## Frequently Asked Questions

**Q: My Friedrich Kühl mini-split shows E2 on the remote display but the indoor unit seems fine. What should I check?**
A: On Friedrich Kühl models, the E2 ambient sensor is sometimes embedded in the remote controller itself rather than on the indoor unit. Try replacing the remote's batteries - a weak battery can cause erratic thermistor readings. If that doesn't fix it, use the unit in manual mode from the indoor unit controls while you order a replacement remote.

**Q: Friedrich F5 appears every time it rains. Is this a wiring issue?**
A: F5 during rain events typically points to moisture intrusion into the communication wiring conduit or the outdoor unit terminal block. Inspect the conduit where the communication cable enters the outdoor unit - the conduit should be sealed to prevent water infiltration. If water is getting into the terminal block, seal around the cable entry point with weatherproof silicone after drying the terminals and confirming the connections are tight.

**Q: The Friedrich mini-split shows F1 only in summer when outdoor temps are above 100°F. Is this normal?**
A: Marginally normal for base-tier Friedrich models - most standard mini-splits have an upper outdoor operating limit of 115°F. If your ambient regularly hits 100-110°F and the coil is clean, the system may simply be reaching its design limit. Shade the outdoor unit from direct afternoon sun (without blocking airflow) and keep the condenser coil clean. If F1 occurs below 100°F, the coil cleaning or refrigerant charge needs attention.

**Q: How do I find the correct part numbers for Friedrich mini-split sensors? The model number tag is faded.**
A: Contact Friedrich directly with your unit's serial number (which is more durable than the model tag) at 1-800-541-6645. Alternatively, remove the indoor unit front cover and photograph the control board - the part number is printed on the board itself and can be used to find compatible replacement sensors. Most Friedrich sensors cross-reference to generic 10kΩ NTC thermistors available at HVAC parts suppliers.

**Q: What's the difference between E-codes and F-codes on Friedrich?**
A: E-codes (E1-E9) are exclusively sensor faults - a thermistor or transducer has failed or is reporting bad data. These do not indicate refrigerant or mechanical system problems. F-codes (F1-F9) are operational faults - the refrigerant system, compressor, fan motors, or communication system has a real problem. E-codes are generally DIY-repairable (replace the sensor). F-codes often require professional diagnosis, especially F1, F2, F3, and F7.
