---
title: "York YZV Heat Pump Error Codes - Variable Speed Fault Diagnostics"
description: "Complete fault guide for the York YZV variable-speed heat pump, covering all control board and communicating system fault codes, iQ Drive inverter diagnostics, refrigerant issues, and sensor failures. Includes practical repair steps and parts guidance for homeowners and HVAC technicians."
pubDatetime: 2026-04-25T00:00:00Z
author: "Dana Kowalski"
tags:
  - hvac
  - error-codes
---

The York YZV is Johnson Controls' flagship variable-speed split-system heat pump. It uses an inverter-driven compressor, a communicating control platform, electronic expansion control, and a variable-speed outdoor fan to hit high efficiency ratings while holding tight temperature control. When the YZV develops a fault, the outdoor control board records the issue, flashes a status LED, and on communicating installs sends a numeric code to the thermostat or service tool. This guide covers the codes you are most likely to see, what they mean inside the equipment, and how to diagnose them without guessing.

## What Does a York YZV Error Code Mean?

The YZV reports faults in two layers. The outdoor unit's control board uses LED flash sequences for field diagnosis at the cabinet. Communicating systems and York service tools translate those into numeric or descriptive codes. On many YZV installs, the indoor thermostat or Hx thermostat interface will show the fault history if the system is fully communicating.

Because the YZV is inverter-based, not every fault means a hard shutdown. Some faults force the unit into a reduced-capacity protection mode. That matters because you may still get some heating or cooling even while the system is protecting the compressor.

### Common York YZV Fault Codes

| Code | Meaning |
|------|---------|
| 1 flash / Code 101 | Normal standby or no active fault |
| 2 flashes / Code 201 | High pressure protection fault |
| 3 flashes / Code 202 | Low pressure protection fault |
| 4 flashes / Code 203 | Discharge temperature protection fault |
| 5 flashes / Code 204 | Outdoor ambient sensor fault |
| 6 flashes / Code 205 | Outdoor coil sensor fault |
| 7 flashes / Code 206 | Suction temperature sensor fault |
| 8 flashes / Code 207 | Discharge temperature sensor fault |
| 9 flashes / Code 208 | Communication fault between outdoor and indoor controls |
| 10 flashes / Code 209 | Inverter communication fault |
| 11 flashes / Code 210 | Inverter module internal fault |
| 12 flashes / Code 211 | Compressor start or rotor lock fault |
| 13 flashes / Code 212 | Outdoor fan motor fault |
| 14 flashes / Code 213 | Reversing valve fault |
| 15 flashes / Code 214 | Electronic expansion valve fault |
| 16 flashes / Code 215 | EEPROM or main board memory fault |
| 17 flashes / Code 216 | Line voltage out of range |

### How the YZV iQ Drive System Works

York uses a variable-speed inverter platform that many techs refer to as an iQ Drive-style system. The compressor does not start across the line like a conventional single-stage unit. Instead, the inverter rectifies incoming AC power into DC, then generates a variable-frequency output to control compressor speed. That is why codes 209, 210, and 211 matter so much.

**Code 209** means the outdoor main control cannot talk to the inverter. This may be a failed communication harness, a loose plug, or a dead inverter module.

**Code 210** means the inverter itself detected an internal problem. That can include DC bus overvoltage, undervoltage, overcurrent, overheated power transistors, or a failed internal temperature sensor.

**Code 211** means the inverter tried to spin the compressor and could not. That points to a mechanically locked compressor, bad winding, or a severe refrigerant floodback issue that prevented normal startup.

### Refrigerant and Sensor Faults

The YZV protects itself aggressively when pressures or temperatures move out of range.

**High pressure fault (201)** usually means the outdoor coil cannot reject heat. Dirty condenser coil, failed outdoor fan, overcharge, non-condensables, or a closed liquid line service valve can all cause it.

**Low pressure fault (202)** usually means low charge, indoor airflow restriction in cooling mode, or a metering problem. Because the YZV modulates, low pressure can appear as a soft protection event before a hard lockout.

**Discharge temperature fault (203)** is one of the most useful codes. If the compressor discharge line runs too hot, the system is warning you about poor cooling of the compressor. Low charge, high compression ratio, or a restricted EEV can all drive this code.

Sensor codes 204 through 207 tell you the control board lost a temperature input. On these systems, the sensors are 10k thermistors. When one opens or shorts, the board loses a key operating reference and either shuts down or falls back to a protection mode.

## How to Fix It

1. Shut the system off at the thermostat and let pressures equalize for 10 minutes before troubleshooting active faults.
2. For high or low pressure faults, inspect the outdoor coil, confirm the outdoor fan ramps normally, and check indoor airflow restrictions before assuming a refrigerant problem.
3. For sensor faults, power down the unit, locate the failed thermistor, and measure resistance. A healthy 10k thermistor should read close to 10,000 ohms at 77°F.
4. For communication and inverter faults, check low-voltage system wiring, reseat inverter harness plugs, verify stable 208 to 240VAC line voltage, and inspect the inverter heat sink for debris.
5. For compressor startup faults, disconnect power, ohm the compressor windings, and check each terminal to ground before condemning the compressor or inverter.
6. For reversing valve or EEV faults, verify the electrical signal first. If voltage is present and the component still does not respond, the part itself has likely failed.

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|-------------|
| [York Outdoor Sensor S1-02543234000](https://www.amazon.com/s?ascsubtag=ecf-york-yzv-heat-pump-error-codes&k=York+S1-02543234000+sensor&tag=errorcodefixes-20) | Replaces failed ambient or coil thermistors for codes 204 and 205 | $20–$45 |
| [York Line Temperature Sensor S1-02545392000](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-york-yzv-heat-pump-error-codes&tag=errorcodefixes-20) | Used for suction or discharge temperature faults on many YZV units | $20–$45 |
| [York YZV Outdoor Control Board](https://www.amazon.com/dp/B0CNZGZ1HS?ascsubtag=ecf-york-yzv-heat-pump-error-codes&tag=errorcodefixes-20) | Needed for persistent board memory or communication faults | $180–$420 |
| [Heat Pump Reversing Valve Solenoid 24V](https://www.amazon.com/s?ascsubtag=ecf-york-yzv-heat-pump-error-codes&k=heat+pump+reversing+valve+solenoid+24V&tag=errorcodefixes-20) | Fixes common reversing valve electrical failures tied to code 213 | $20–$45 |
| [ECM Outdoor Fan Motor for York Heat Pump](https://www.amazon.com/dp/B0D2L5NSMM?ascsubtag=ecf-york-yzv-heat-pump-error-codes&tag=errorcodefixes-20) | Replaces failed variable-speed fan motor causing code 212 and high pressure | $120–$320 |
| [R-410A Manifold Gauge Set](https://www.amazon.com/s?ascsubtag=ecf-york-yzv-heat-pump-error-codes&k=R-410A+manifold+gauge+set&tag=errorcodefixes-20) | Required for accurate refrigerant diagnosis on pressure and temperature faults | $45–$120 |

## When to Call a Pro

Call a licensed HVAC technician when:

- You have repeated 201 or 202 pressure faults and do not know the refrigerant condition. Leak search and charging are not DIY jobs.
- The unit throws 210 or 211 and compressor or inverter work is on the table. Those are expensive parts, and bad diagnosis gets expensive fast.
- Code 214 returns after a restart. EEV work requires opening the sealed system.
- The outdoor fan on this inverter platform shows partial or erratic operation. A tech needs to verify whether the board, motor module, or command signal failed.
- You suspect a control compatibility issue between the indoor and outdoor communicating components. York communicating systems can generate misleading secondary faults when one matched component is wrong.

Sensor replacement, wiring inspection, coil cleaning, and basic voltage checks are fine for a skilled DIYer. Refrigerant, inverter, compressor, and EEV work belong with a pro.

## Frequently Asked Questions

**Q: My York YZV still heats and cools a little even though it has an inverter fault. How is that possible?**
A: The control may be running in a protective low-capacity mode before it commits to a full lockout. Variable-speed systems do this to protect the compressor while still providing some comfort. Do not treat that as normal operation. The fault still needs diagnosis.

**Q: What is the difference between a communication fault and an inverter communication fault?**
A: A regular communication fault means the outdoor unit lost contact with the indoor system controls or thermostat. An inverter communication fault means the outdoor main board cannot talk to the inverter module inside the same unit. One is a system wiring problem. The other is usually inside the outdoor cabinet.

**Q: The YZV throws a high pressure fault on very hot afternoons only. What should I check first?**
A: Start with the condenser coil and the outdoor fan. Variable-speed systems react hard to restricted heat rejection. If the coil is dirty or the fan is weak, the unit may run fine in mild weather and trip only on peak heat days.

**Q: Can a bad sensor cause the YZV to short cycle?**
A: Yes. If the board loses ambient, coil, suction, or discharge temperature input, it may default into protection logic that limits runtime or shuts the compressor down early. A sensor that reads wrong but has not failed completely can be even more confusing than an open sensor because it can produce believable but incorrect operating decisions.

## See Also

- [York 7 Flashes Error Code — Ignition Lockout Fix](/posts/york-7-flashes-error-code/)
- [York Furnace Error Codes — Complete Guide](/posts/york-furnace-error-codes/)
- [York Furnace E4 Error Code — Ignition Failure](/posts/york-furnace-error-code-e4/)
- [York 3 Flashes Error Code — Causes & Fix](/posts/york-3-flashes-error-code/)
