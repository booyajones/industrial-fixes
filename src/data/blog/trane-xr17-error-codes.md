---
title: "Trane XR17 Heat Pump Error Codes - Fault Code and Flash Code Guide"
description: "Complete fault code and LED flash code guide for the Trane XR17 heat pump, covering all diagnostic blink codes, ComfortLink II communicating thermostat faults, refrigerant issues, and defrost problems. Written for homeowners and HVAC service technicians."
pubDatetime: 2026-04-25T00:00:00Z
author: "Marcus Webb"
tags:
  - hvac
  - error-codes
---

The Trane XR17 is Trane's mid-tier two-speed heat pump, introduced as part of their post-2020 lineup refresh. It pairs with both conventional thermostats and the Trane ComfortLink II communicating system, and it runs on R-410A with a two-speed scroll compressor. When something fails, the XR17 reports it through the outdoor unit control board's diagnostic LED, a blink sequence that identifies the fault. Units connected to a ComfortLink II thermostat also report numeric codes on the display. This guide covers both systems.

## What Does a Trane XR17 Error Code Mean?

The XR17 control board has a single diagnostic LED visible through the cabinet louvered panel (or after removing the service panel). Fault codes flash as a number of blinks, pause, then repeat. Count the complete sequence twice before logging the number, a partial sequence during a transition can mislead diagnosis.

When connected to a Trane ComfortLink II or Nexia thermostat, the XR17 reports numeric fault codes directly to the thermostat display and to the Nexia app if the thermostat is connected to Wi-Fi.

### LED Blink Code Reference

| Blink Count | Fault |
|-------------|-------|
| 2 blinks | High-pressure lockout |
| 3 blinks | Low-pressure lockout |
| 4 blinks | Discharge line overtemperature |
| 5 blinks | Open start/run capacitor (detected via motor start failure) |
| 6 blinks | Outdoor fan motor fault |
| 7 blinks | Outdoor ambient sensor fault |
| 8 blinks | Coil temperature sensor fault |
| 9 blinks | Discharge temperature sensor fault |
| 10 blinks | Suction temperature sensor fault |
| 11 blinks | Low-speed compressor winding fault |
| 12 blinks | Communication fault (with indoor unit or thermostat) |
| 13 blinks | Reversing valve fault |
| 14 blinks | Defrost control fault |
| Continuous flash | Normal operation, no fault |

A **continuous rapid flash** means the unit is running normally. A solid light (no flash) means the board has lost power or has failed. No light at all while the disconnect is closed points to a blown fuse on the control board (the XR17 has a 3A automotive-style blade fuse on the board) or a failed transformer.

### ComfortLink II Numeric Fault Codes

| Code | Meaning |
|------|---------|
| 171 | High pressure fault |
| 172 | Low pressure fault |
| 173 | Low pressure during defrost, expected, only a fault outside defrost |
| 174 | Discharge temperature exceeded limit |
| 175 | Outdoor fan fault |
| 176 | Ambient temperature sensor fault |
| 177 | Coil temperature sensor fault |
| 178 | Discharge temperature sensor fault |
| 179 | Suction temperature sensor fault |
| 180 | Communication fault, outdoor unit to air handler |
| 181 | Communication fault, outdoor unit to thermostat |
| 182 | Reversing valve fault |
| 183 | Compressor fault (low-speed winding) |
| 184 | Defrost board fault |
| 190 | Outdoor unit voltage out of range |

### Refrigerant Fault Diagnosis (Codes 171–174)

The XR17 uses Copeland ZP two-speed scroll compressors, which have both a low-speed (single-phase) and high-speed (start winding) operation mode. High-pressure trips (code 171/2 blinks) at extreme outdoor temperatures are sometimes normal, above 115°F ambient in cooling mode, the unit may cycle on high pressure. Outside of extreme conditions, a high-pressure trip means restricted airflow across the outdoor coil, an overcharged system, non-condensables in the refrigerant, or a failed outdoor fan.

Low-pressure trips (code 172/3 blinks) in cooling mode are almost always a low refrigerant charge. In heating mode, a low-pressure trip can occur during cold ambient conditions (below 0°F) when the system is undersized for the load, this is a capacity limitation, not necessarily a refrigerant issue.

Discharge temperature faults (code 174/4 blinks) indicate the compressor discharge line exceeded the cutout temperature, typically set at 240–260°F on the XR17. This happens with low refrigerant charge (high superheat), a restricted liquid line or TXV, or a compressor that's running in very high ambient conditions. Persistent discharge temperature faults with normal refrigerant charge point to a restricted TXV or liquid line filter-drier.

## How to Fix It

### For High Pressure Fault (Code 171, 2 blinks)

1. Turn the thermostat to OFF. The XR17 has an automatic reset high-pressure switch, wait 5–10 minutes for the switch to reset and pressure to equalize.
2. Inspect the outdoor coil for fouling: dirt, cottonwood debris, grass clippings, or ice buildup. Rinse the coil from inside out with a hose (low pressure, not a pressure washer).
3. Check that the outdoor fan is spinning and moving airflow away from the coil. A fan blade that's spinning but not generating airflow has a blade pitch problem or is turning backward.
4. Check outdoor unit clearances, the XR17 requires a minimum of 18 inches clearance on all sides and 24 inches above the top discharge.
5. Connect manifold gauges and run the system in cooling mode. High-side pressure should not exceed 450 psig at 95°F ambient. If it climbs above 500 psig before the coil is dirty and the fan is working, suspect an overcharge or non-condensables.

### For Low Pressure Fault (Code 172, 3 blinks)

1. Check for ice on the suction line and outdoor coil. Excessive ice formation in cooling mode indicates low refrigerant charge or an airflow problem indoors.
2. If the indoor coil is iced, turn the system to FAN ONLY to thaw it. Once thawed (30–60 minutes), resume cooling operation and monitor pressures.
3. If suction pressures remain low after the system is fully thawed (below 100 psig in cooling at 75°F indoor), the system needs refrigerant, but don't add it without finding the leak first.
4. Perform a visual leak check: look for oily residue on refrigerant line connections, the coil, service valves, and compressor fittings.

### For Sensor Faults (Codes 176–179)

1. Locate the faulty sensor. The ambient sensor mounts on the outdoor cabinet or coil guard; the coil sensor clips to the outdoor coil; discharge and suction sensors clamp onto the refrigerant lines near the compressor.
2. Unplug the sensor connector from the control board and measure resistance. Trane XR17 sensors are 10k NTC thermistors, approximately 10,000 ohms at 77°F.
3. Replace if open circuit or shorted to zero. Trane/American Standard uses sensor part number **BAYSENSNDR01A** across multiple outdoor units, including the XR17.
4. After replacing, clear the fault by cycling power to the unit (breaker off, wait 30 seconds, restore).

### For Communication Fault (Codes 180, 181, 12 blinks)

1. The XR17 uses a 4-wire communication bus. Verify wiring at the outdoor unit terminal block, terminals are labeled 1, 2, 3, 4 (or A, B, R, C depending on board revision).
2. Check for 24VAC between the R and C terminals at the outdoor unit. If absent, the transformer in the air handler may have failed, or there's a blown fuse.
3. Inspect communication wires for any damage, especially where they pass through the cabinet wall or along conduit runs.
4. Try disconnecting the thermostat from the bus. If the fault clears, the thermostat's communication module may have failed.
5. Perform a full power cycle: breaker off, outdoor disconnect off, wait 60 seconds, restore.

### For Reversing Valve Fault (Code 182, 13 blinks)

1. Check whether the unit is blowing correct temperature air relative to the mode selected at the thermostat.
2. At the outdoor unit terminal block, check for 24VAC on the O or B terminal (which one depends on thermostat configuration, O energizes RV in cool, B energizes in heat).
3. Trace the 24V wire from the terminal block to the reversing valve solenoid. Check for loose connections at the solenoid spade terminals.
4. Measure solenoid coil resistance: 15–40 ohms is normal. Open circuit means the solenoid has burned out.
5. If solenoid and wiring check out, the 4-way valve body itself is stuck. This requires refrigerant recovery and replacement by a certified technician.

### For Defrost Fault (Code 184, 14 blinks)

1. Check whether the outdoor coil has excessive ice buildup. In heating mode, defrost should initiate when the outdoor coil drops below 30°F.
2. Locate the defrost sensor (clips onto the outdoor coil, typically at the bottom circuit). Measure resistance, should be 10k NTC like other sensors.
3. Check defrost board jumpers (if adjustable) for proper defrost initiation settings, some boards have DIP switches or jumpers for 30/60/90 minute intervals.
4. If the coil is iced solid and defrost never fires, suspect the defrost sensor or the board's defrost relay.

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|-------------|
| [Trane Outdoor Sensor BAYSENSNDR01A](https://www.amazon.com/s?ascsubtag=ecf-trane-xr17-error-codes&k=Trane+BAYSENSNDR01A+outdoor+sensor&tag=errorcodefixes-20) | Universal sensor replacement for ambient, coil, discharge, suction faults | $20–$40 |
| [Trane XR17 Control Board](https://www.amazon.com/s?k=Trane+XR17+Control+Board&tag=errorcodefixes-20) | Replace on persistent defrost faults (code 184) or board failure | $150–$350 |
| [Heat Pump Reversing Valve Solenoid 24V](https://www.amazon.com/s?ascsubtag=ecf-trane-xr17-error-codes&k=heat+pump+reversing+valve+solenoid+24V+coil&tag=errorcodefixes-20) | Burnt solenoid is common cause of reversing valve faults (code 182) | $20–$45 |
| [Start/Run Capacitor for Heat Pump](https://www.amazon.com/dp/B01M05L7B3?ascsubtag=ecf-trane-xr17-error-codes&tag=errorcodefixes-20) | Failed capacitor causes compressor and fan start faults (5 blinks) | $15–$35 |
| [HVAC Coil Cleaner Spray](https://www.amazon.com/s?ascsubtag=ecf-trane-xr17-error-codes&k=HVAC+outdoor+coil+cleaner+spray&tag=errorcodefixes-20) | Clean fouled outdoor coil to prevent high-pressure trips | $12–$25 |
| [Trane ComfortLink II Thermostat XL824](https://www.amazon.com/s?ascsubtag=ecf-trane-xr17-error-codes&k=Trane+XL824+ComfortLink+thermostat&tag=errorcodefixes-20) | Enables full numeric fault code display on the XR17 | $150–$275 |

## When to Call a Pro

Certain XR17 faults fall outside DIY scope:

- **Any refrigerant-related fault (codes 171, 172, 174) with confirmed pressure abnormality.** R-410A requires EPA 608 certification to handle. Don't add refrigerant without a leak test.
- **Compressor fault (code 183, 11 blinks).** Two-speed compressor diagnosis and replacement requires specialized knowledge and refrigerant recovery.
- **Reversing valve body failure.** Valve replacement requires brazing and a system evacuation and recharge.
- **Defrost board faults (code 184) that persist after sensor replacement.** Defrost board replacement on some XR17 revisions requires recalibrating defrost timer settings.
- **Voltage faults (code 190).** Low voltage (below 187VAC) at the unit can damage the compressor, this is a utility or electrical panel issue that needs an electrician.

Sensor replacements, capacitor swaps, coil cleaning, and communication wiring troubleshooting are manageable DIY repairs with basic electrical knowledge.

## Frequently Asked Questions

**Q: My Trane XR17 blinks 3 times then pauses, over and over. The refrigerant tech says the charge is fine. What else causes a low-pressure fault?**
A: A faulty low-pressure switch is the next most likely cause. The switch should be closed (showing continuity) at normal operating pressures. Check ohms across the switch terminals while the system is off and pressures are equalized. If the switch reads open at 120+ psig, it has failed. Also check for a pinched or cracked capillary tube on the switch, a small leak in the capillary tube will cause the switch to read low pressure even when the system isn't.

**Q: The XR17 went into defrost during a 60°F day and ran in defrost for 20 minutes. Is that normal?**
A: No. Defrost should only initiate when the outdoor coil temperature drops below roughly 30°F, which typically means outdoor ambient below 45°F. A defrost cycle at 60°F suggests the defrost sensor is reading incorrectly (probably detached from the coil) or the defrost board is initiating based on time alone regardless of coil temperature. Check that the defrost sensor clip is firmly pressed against the coil surface.

**Q: What's the difference between the Trane XR17 and XR15? Do they use the same fault codes?**
A: The XR17 uses a two-speed compressor and generates more specific faults related to compressor speed selection. The XR15 is a single-speed unit with a simplified control board. Fault codes overlap significantly but aren't identical, always confirm your specific model before ordering control board replacements.

**Q: My XR17 runs fine in cooling but won't heat. Code 182 shows on the thermostat. Can I confirm the reversing valve is the problem before calling a tech?**
A: Yes. Go to the outdoor unit while it's in heating mode. Find the reversing valve (a copper cylinder with four refrigerant lines soldered to it, located near the compressor). Touch the top of the valve, you should feel a vibration if the valve body is moving. Also locate the solenoid coil mounted on the valve and feel whether it's warm (energized) or cold (de-energized). If the solenoid is warm but the valve body isn't shifting, the valve body is stuck. If the solenoid is cold when it should be energized, the electrical circuit to the solenoid has failed.
