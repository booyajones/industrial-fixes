---
title: "Amana AVXC18 Heat Pump Error Codes - Communicating System Fault Guide"
description: "Complete fault guide for the Amana AVXC18 variable-capacity heat pump, covering communicating system codes, control board faults, reversing valve issues, and refrigerant diagnostics. Includes practical repair steps and parts guidance for homeowners and HVAC technicians."
pubDatetime: 2026-04-25T00:00:00Z
author: "Dana Kowalski"
tags:
  - hvac
  - error-codes
---

The Amana AVXC18 is Amana's top-tier variable-capacity split-system heat pump platform from the Goodman-Amana family. It uses an inverter-driven compressor, ComfortNet communicating controls, outdoor thermistors, and a variable-speed fan motor to modulate capacity and maintain steady temperatures. When a fault occurs, the AVXC18 can report it through the outdoor control board LED, through ComfortNet thermostat diagnostics, and through stored fault history on the control board. This guide covers the codes most owners and techs run into, what they mean, and how to fix them without replacing parts blindly.

## What Does an Amana AVXC18 Error Code Mean?

The AVXC18 uses a communicating logic board that tracks pressure, temperature, compressor drive status, and system communication. On a matched ComfortNet system, the thermostat gives you the cleanest readout. Without that thermostat, you can still read board LEDs and service diagnostics at the outdoor unit.

These systems often generate two types of faults:
- **Hard lockout faults**, which shut the unit down until the condition clears or power resets.
- **Soft protection faults**, which reduce compressor speed or suspend operation for a short time to protect the inverter or compressor.

### Common AVXC18 Error Codes and Flash Codes

| Code | Meaning |
|------|---------|
| L0 | Normal operation, no active fault |
| L1 | High pressure protection fault |
| L2 | Low pressure protection fault |
| L3 | Discharge temperature protection fault |
| L4 | Compressor overcurrent or inverter overload |
| L5 | Outdoor ambient sensor fault |
| L6 | Outdoor coil temperature sensor fault |
| L7 | Suction line temperature sensor fault |
| L8 | Discharge line temperature sensor fault |
| L9 | Communication fault with indoor unit or thermostat |
| H0 | Inverter module communication fault |
| H1 | Inverter module internal protection fault |
| H2 | Compressor startup failure or locked rotor |
| H3 | Outdoor fan motor fault |
| H4 | Reversing valve fault |
| H5 | EEPROM or control board memory fault |
| H6 | Line voltage out of range |
| H7 | Electronic expansion valve fault |

On some board revisions, the same faults appear as LED flash counts rather than the exact L- or H-series codes. Goodman-Amana inverter boards often flash a repeating sequence that service literature maps back to the codes above.

### Communicating System Faults

The AVXC18 was built around **ComfortNet**, Goodman-Amana's communicating control platform. That matters because a ComfortNet mismatch can create faults that look like bad outdoor parts when the real problem is communication.

**L9 communication fault** shows up when the outdoor unit loses the indoor air handler or thermostat data bus. The inverter heat pump depends on indoor coil temperature and system demand information to modulate properly. If it loses that information, the unit may shut down or fall into a limited backup mode.

### Reversing Valve and Refrigerant Faults

**H4 reversing valve fault** means the unit could not verify or maintain the expected mode change between heating and cooling. On a heat pump, the reversing valve redirects refrigerant flow. If the solenoid fails, wiring opens, or the valve body sticks, you get wrong supply air temperature and poor capacity.

**L1, L2, and L3** cover the main refrigerant-side protection events:
- **L1 high pressure** usually means poor outdoor airflow, overcharge, or a metering problem.
- **L2 low pressure** usually points to low charge, indoor airflow problems in cooling, or a restriction.
- **L3 discharge temperature protection** means the compressor discharge line got too hot, which often happens with low refrigerant charge or a restricted EEV.

### Inverter and Compressor Faults

The AVXC18's variable-capacity compressor runs from an inverter drive. That makes **L4, H0, H1, and H2** critical.

- **L4** means the compressor or drive current went above the safe limit.
- **H0** means the outdoor main board cannot talk to the inverter.
- **H1** means the inverter detected an internal fault like overtemperature, DC bus fault, or drive failure.
- **H2** means the compressor failed to start or the rotor locked.

If these codes repeat, you need real electrical and refrigerant diagnosis. Guessing between inverter and compressor on these systems gets expensive.

## How to Fix It

### For Pressure and Temperature Protection Faults (L1, L2, L3)

1. Shut the unit off at the thermostat and let it sit for 10 minutes.
2. Inspect the outdoor coil for dirt, leaves, cottonwood, pet hair, or any airflow restriction around the cabinet.
3. Verify the outdoor fan runs and ramps normally when the compressor starts. If the compressor ramps but the fan lags or stalls, high pressure faults follow fast.
4. Check the indoor air filter and indoor coil airflow if the fault happened during cooling.
5. If you have gauges and certification, compare system pressures to ambient conditions. Low pressure with oil residue around fittings points to a leak. High pressure with a clean coil and normal fan operation points to overcharge, restriction, or non-condensables.
6. For repeated L3 discharge temperature faults, inspect the discharge temperature sensor first before condemning the refrigerant circuit.

### For Sensor Faults (L5 through L8)

1. Turn off power before unplugging sensors.
2. Locate the failed sensor: ambient on the cabinet, coil sensor on the outdoor coil, suction and discharge sensors strapped to refrigerant lines.
3. Disconnect the sensor and read resistance with a multimeter. These are typically 10k NTC thermistors.
4. At room temperature, expect about 10,000 ohms. Open or shorted readings confirm failure.
5. Inspect wiring for rub-through near sheet metal edges or hot copper lines.
6. Replace the bad sensor. Goodman-Amana outdoor thermistor replacements commonly cross to **0130M00068** or similar model-specific sensor kits. Verify by serial number before ordering.

### For Communication Fault (L9)

1. Check the ComfortNet communication wiring between thermostat, indoor unit, and outdoor unit.
2. Confirm the indoor unit has power and the low-voltage fuse is intact.
3. Power cycle the full system in order: thermostat off, indoor breaker off, outdoor disconnect off, wait 60 seconds, then restore indoor power first and outdoor power second.
4. Reseat low-voltage and data connectors on the outdoor board.
5. If the fault keeps returning, verify that the thermostat and indoor equipment are actually ComfortNet-compatible. A mismatched conventional thermostat setup can cause recurring communication faults on some installs.

### For Inverter and Compressor Faults (L4, H0, H1, H2)

1. Verify line voltage at the unit. The AVXC18 expects stable 208 to 240VAC. Low voltage or brownout conditions trigger inverter faults.
2. Inspect the inverter harness and control plugs for heat damage, corrosion, or loose pins.
3. Clean dust and debris away from the inverter heat sink and electronic compartment.
4. For H2 compressor startup fault, disconnect power and ohm the compressor windings. The readings should be balanced across all terminal pairs.
5. Check each terminal to ground. Any continuity to ground means compressor failure.
6. If windings look normal and H0 or H1 persist, the inverter module is the more likely failure point.

### For Outdoor Fan Fault (H3)

1. Watch whether the fan starts with the compressor call.
2. Check the fan motor connector and wiring harness.
3. If the fan twitches, hums, or starts intermittently, suspect the motor module.
4. A weak outdoor fan on a variable-capacity heat pump often causes secondary high-pressure faults, so fix H3 first before chasing refrigerant codes.

### For Reversing Valve Fault (H4)

1. Command the system from cooling to heating and listen for the reversing valve shift.
2. Measure 24VAC at the reversing valve solenoid during the mode change.
3. Check solenoid coil resistance. A burned open coil will read infinite resistance.
4. If voltage and coil resistance are both normal but the system still runs in the wrong mode, the valve body is mechanically stuck and must be replaced.

### For EEV Fault (H7)

1. Inspect the EEV harness at the valve and board.
2. Power cycle the unit so the valve can re-home.
3. If the fault returns, the EEV motor or board output is failing.
4. EEV replacement requires sealed-system work by a licensed technician.

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|-------------|
| [Goodman Amana Outdoor Thermistor 0130M00068](https://www.amazon.com/s?ascsubtag=ecf-amana-avxc18-heat-pump-error-codes&k=Goodman+Amana+0130M00068+thermistor&tag=errorcodefixes-20) | Replaces failed outdoor temperature sensors for L5 through L8 faults | $15–$35 |
| [Amana AVXC18 Outdoor Control Board](https://www.amazon.com/dp/B0CNZGZ1HS?ascsubtag=ecf-amana-avxc18-heat-pump-error-codes&tag=errorcodefixes-20) | Needed for repeated memory, communication, or board-level inverter faults | $180–$420 |
| [Heat Pump Reversing Valve Solenoid Coil 24V](https://www.amazon.com/s?ascsubtag=ecf-amana-avxc18-heat-pump-error-codes&k=heat+pump+reversing+valve+solenoid+24V+coil&tag=errorcodefixes-20) | Fixes common H4 electrical faults when the valve coil burns open | $20–$45 |
| [Amana or Goodman ECM Outdoor Fan Motor](https://www.amazon.com/dp/B0D2L5NSMM?ascsubtag=ecf-amana-avxc18-heat-pump-error-codes&tag=errorcodefixes-20) | Replaces failed outdoor fan motor causing H3 and secondary pressure faults | $120–$320 |
| [ComfortNet Thermostat](https://www.amazon.com/s?ascsubtag=ecf-amana-avxc18-heat-pump-error-codes&k=ComfortNet+thermostat+Amana+Goodman&tag=errorcodefixes-20) | Gives full communicating diagnostics and proper control logic for AVXC18 systems | $120–$260 |
| [R-410A Leak Detection Kit](https://www.amazon.com/s?ascsubtag=ecf-amana-avxc18-heat-pump-error-codes&k=R-410A+refrigerant+leak+detection+kit&tag=errorcodefixes-20) | Helps locate leaks when repeated L2 faults point to low charge | $20–$60 |

## When to Call a Pro

Call a licensed HVAC technician when:

- L1, L2, or L3 keep returning after airflow and filter checks. Variable-capacity sealed-system diagnosis needs gauges, charging charts, and experience.
- H0, H1, or H2 repeat. Inverter and compressor diagnosis on these systems is expensive and easy to get wrong without meter readings and manufacturer procedures.
- H4 persists after you confirm the solenoid has power. A stuck reversing valve requires refrigerant recovery and brazing.
- H7 returns after a restart. EEV work requires opening the sealed system.
- The ComfortNet system appears mismatched or misconfigured. A pro can verify compatible indoor, outdoor, and thermostat boards and firmware.

Sensor swaps, wiring checks, filter changes, and coil cleaning are reasonable DIY tasks. Refrigerant, inverter, compressor, and reversing valve body work are not.

## Frequently Asked Questions

**Q: My Amana AVXC18 throws L9 and then L1 a few minutes later. Which code matters more?**
A: Start with L9. If the outdoor unit loses communication, it may stop receiving proper fan and capacity commands, which can create secondary pressure faults. Restore communication first, then see whether the L1 high pressure fault still appears.

**Q: Can a bad outdoor fan motor cause an inverter fault on the AVXC18?**
A: Yes. If the fan cannot reject heat, system pressures rise and the inverter has to work harder under poor operating conditions. That can trigger overcurrent or internal protection faults that look like inverter failures when the real root cause is airflow.

**Q: The system still runs after an L3 discharge temperature fault. Is that normal?**
A: Sometimes. The board may reduce compressor speed to protect the unit before going into a full lockout. That does not mean the problem solved itself. Check airflow, charge condition, and the discharge sensor before the fault turns into a bigger repair.

**Q: Does the AVXC18 require a ComfortNet thermostat?**
A: It works best with one. You can run some Goodman-Amana inverter systems in non-communicating mode with adapter controls, but you lose diagnostics and some modulation behavior. If you want full fault visibility and the best performance, matched ComfortNet controls are the right setup.
