---
title: "Goodman GVZC18 Heat Pump Error Codes: iQ Drive Fault Diagnostics"
description: "Complete guide to Goodman GVZC18 variable-speed heat pump fault codes, iQ Drive communicating system errors, and DIY fixes."
pubDatetime: 2026-04-25T00:00:00Z
author: "Marcus Webb"
tags:
  - hvac
  - error-codes
---

The Goodman GVZC18 is a variable-speed heat pump built around the iQ Drive inverter-driven compressor platform. Unlike single-stage units that either run at full capacity or shut off, the GVZC18 modulates from roughly 25% to 100% capacity based on load, which means better humidity control, quieter operation, and significantly lower energy bills. It also means the fault code system is more sophisticated than what you'd see on a standard heat pump.

When the GVZC18 detects a problem, it communicates faults through a communicating thermostat (like the ComfortNet system), the indoor air handler's communicating board, and a local LED on the outdoor control board. This guide covers all three display paths and tells you exactly what to do when a fault appears.

## What Does the Goodman GVZC18 iQ Drive Fault System Mean?

The GVZC18 uses a two-tier fault system:

**Tier 1 – LED flash codes** on the outdoor control board. These are visible to anyone with a screwdriver and a flashlight and don't require a communicating thermostat.

**Tier 2 – Communicating system fault codes** displayed as alphanumeric codes on the ComfortNet thermostat or the AMST/ARUF air handler's board. These provide much more detail.

### LED Flash Codes (Outdoor Board)

| Flash Count | Fault | Severity |
|---|---|---|
| 1 | Normal / standby | None |
| 2 | High-pressure lockout | High |
| 3 | Low-pressure lockout | High |
| 4 | Ambient/coil sensor fault | Medium |
| 5 | Discharge temperature over-limit | High |
| 6 | iQ Drive inverter fault | High |
| 7 | Communication loss (outdoor to indoor) | Medium |
| 8 | Compressor over-current | High |
| 9 | Locked rotor / compressor won't start | High |
| 10 | Defrost thermistor fault | Medium |
| 11 | Reversing valve fault | High |
| 12 | Low supply voltage | Medium |

### ComfortNet Communicating Fault Codes

When paired with a ComfortNet thermostat, faults appear as two-character codes. Key codes:

| Code | Description |
|---|---|
| E1 | Indoor/outdoor communication failure |
| E2 | Outdoor board internal fault |
| E4 | High-pressure trip |
| E5 | Low-pressure trip |
| E6 | iQ Drive inverter over-temperature |
| E7 | iQ Drive DC bus over-voltage |
| E8 | iQ Drive DC bus under-voltage |
| E9 | Compressor discharge over-temperature |
| F1 | Defrost sensor circuit open or shorted |
| F2 | Liquid line sensor fault |
| F3 | Outdoor ambient sensor fault |

## How to Fix It

### Code 6 / E6, iQ Drive Inverter Fault

This is the most unique fault to the GVZC18. The iQ Drive is a variable-frequency inverter that controls compressor speed. When it throws a fault, the compressor shuts down completely.

1. **Cut power at the outdoor disconnect.** Wait 5 full minutes before restoring. The iQ Drive capacitors hold charge after power loss, 5 minutes lets them fully discharge and allows the inverter to reset.
2. **Check for adequate airflow.** The inverter runs hot. Blocked coil fins or a failed fan motor causes inverter over-temperature faults.
3. **Inspect the inverter board** (located in the outdoor electrical compartment). Look for bulged capacitors, burned traces, or obvious heat damage. Visible damage = board replacement.
4. **Verify supply voltage.** The GVZC18 requires 208/230VAC ±10%. Low voltage stresses the inverter and causes repeated faults.
5. **If the fault returns within one hour of reset**, the inverter board likely needs replacement. This is a warranty item, GVZC18 units carry a 10-year parts warranty when registered.

### Code 2 / E4, High-Pressure Lockout

1. **Clean the outdoor coil.** Use a coil cleaner spray and rinse from inside out.
2. **Verify outdoor fan operation.** On a variable-speed unit, the fan modulates speed, a fan running at reduced speed may not be providing enough airflow.
3. **Check for coil damage.** Bent fins reduce airflow. Use a fin comb to straighten.
4. **If refrigerant overcharge is suspected**, only a certified technician with gauges can confirm and correct it.

### Code 3 / E5, Low-Pressure Lockout

1. **Replace the indoor filter.** A clogged filter reduces airflow and drops suction pressure below the lockout threshold.
2. **Look for frozen indoor coil.** Shut system off, run fan-only for 2–3 hours, then restart.
3. **Check suction line service valve.** Must be fully open.
4. **Persistent low-pressure codes = refrigerant leak.** Call a technician.

### Code 7 / E1, Communication Loss

The iQ Drive communicates over a four-wire bus between the outdoor board and indoor air handler. Communication faults are often wiring issues.

1. **Inspect the four-wire communication cable** between indoor and outdoor units. Look for staple damage, rodent chewing, or loose terminal connections.
2. **Verify wire color assignments match** at both ends, one transposed wire kills communication.
3. **Check that both units have 24VAC power.**
4. **Try a full power cycle**, cut power to both units for 60 seconds and restore.

### Code 9, Locked Rotor / Compressor Won't Start

1. **Check the dual run capacitor first.** Even on variable-speed units, the capacitor assists compressor starting.
2. **Listen at startup.** A humming compressor that doesn't spin = failed start capacitor or locked rotor.
3. **Let the unit sit for 30 minutes** if it just tripped on over-current. A thermally tripped compressor won't restart until it cools.
4. **Persistent locked rotor = compressor replacement**, call a technician.

### Code 10 / F1, Defrost Thermistor Fault

1. **Locate the defrost thermistor** clipped to the outdoor coil.
2. **Check the wiring harness** for corrosion or breaks.
3. **Measure thermistor resistance.** At room temperature (~70°F), resistance should be approximately 10K–12K ohms. Infinite or zero = replace.

### Code 11, Reversing Valve Fault

1. **Confirm the fault** by verifying the unit heats when cooling is called, or cools when heat is called.
2. **Test solenoid coil.** Should have 24VAC when energized and read 10–30 ohms resistance.
3. **Try energizing and de-energizing the solenoid** while listening for a click inside the valve body.
4. **No click despite good solenoid** = stuck valve, technician required for brazing repair.

## Parts You May Need

| Part | Use | Link |
|---|---|---|
| Dual Run Capacitor (45+5 µF, 440V) | Compressor/fan start faults, Code 9 | [View on Amazon](https://www.amazon.com/dp/B01M05L7B3?ascsubtag=ecf-goodman-gvzc18-heat-pump-error-codes&tag=errorcodefixes-20) |
| Defrost Thermistor / NTC Sensor | Code 10 / F1 defrost sensor fault | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-goodman-gvzc18-heat-pump-error-codes&k=goodman+defrost+thermistor+sensor&tag=errorcodefixes-20) |
| 2-Pole 30A Contactor | Pitted contacts, voltage drop at startup | [View on Amazon](https://www.amazon.com/dp/B0CJFZQVPT?ascsubtag=ecf-goodman-gvzc18-heat-pump-error-codes&tag=errorcodefixes-20) |
| Reversing Valve Solenoid Coil | Code 11 reversing valve fault | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-goodman-gvzc18-heat-pump-error-codes&k=reversing+valve+solenoid+coil+hvac&tag=errorcodefixes-20) |
| HVAC Communication Cable (4-conductor) | Code 7 / E1 communication wiring | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-goodman-gvzc18-heat-pump-error-codes&k=hvac+4+conductor+communication+wire&tag=errorcodefixes-20) |
| Goodman Outdoor Control Board | Code 6 inverter board replacement | [View on Amazon](https://www.amazon.com/s?k=Goodman+Outdoor+Control+Board&tag=errorcodefixes-20) |

## When to Call a Pro

**DIY-friendly repairs:** Capacitor replacement, contactor swap, thermistor replacement, coil cleaning, communication wire replacement, power cycling.

**Call a technician for:**
- **iQ Drive inverter board replacement.** While the part is DIY-installable in theory, Goodman's 10-year parts warranty requires factory-certified service for warranty claims on major components. A technician also has diagnostic software to pull full inverter fault logs.
- **Refrigerant work** (Codes 2 and 3 that don't clear with coil cleaning). EPA 608 certification required.
- **Reversing valve brazed replacement.** Requires nitrogen purging, torch work, and refrigerant handling.
- **Compressor replacement.** On a GVZC18, the variable-speed scroll compressor is a significant cost item, get a full system quote before approving compressor replacement on a unit over 8 years old.

## FAQ

**How do I access the ComfortNet fault log on my GVZC18?**
On the ComfortNet thermostat, navigate to Menu → Service → Fault History. The thermostat stores the last several faults with timestamps. If you don't have a ComfortNet thermostat, you're limited to the LED flash codes on the outdoor board.

**My GVZC18 runs in low-speed mode continuously but never switches to high. Is this a fault?**
Not necessarily. The variable-speed iQ Drive is designed to modulate capacity to match the load, and on mild days it will run at very low capacity for extended periods, this is exactly what it should do. It only becomes a fault if the unit can't meet setpoint in extreme cold or heat. If it can't keep up when it should, check for low refrigerant or a failing inverter.

**What is the difference between a soft lockout and a hard lockout on the GVZC18?**
A soft lockout (1–3 occurrences) allows automatic restart after a reset delay. A hard lockout (repeated faults in a short window) requires manual power cycling at the disconnect. Hard lockouts protect the compressor from repeated stress, if you're seeing hard lockouts, the underlying cause must be diagnosed before continuing to reset.

**Why does my GVZC18 defrost cycle seem to run for a long time?**
The GVZC18 runs defrost until the defrost thermistor confirms the outdoor coil has cleared, up to a maximum of about 10 minutes. If defrost seems to run constantly or terminates unusually early, Code 10 (defrost thermistor fault) is the likely culprit, check the thermistor resistance.

**My unit is 4 years old and threw Code 6. Is the inverter board covered under warranty?**
Yes, Goodman's 10-year parts limited warranty covers the iQ Drive inverter board if the unit was registered within 60 days of installation. You'll need a licensed HVAC contractor to submit the warranty claim. If registration was skipped, the standard 5-year parts warranty may still apply.

## See Also

- [Goodman 2 Flash Error Code — Causes & Fix](/posts/goodman-2-flash-error-code/)
- [Goodman ComfortNet Communicating System Error Codes — Complete Guide](/posts/goodman-communicating-error-codes/)
- [Goodman Furnace E3 Error Code — Draft Motor Fault](/posts/goodman-furnace-e3-error-code/)
- [Goodman GSZC18 Heat Pump Error Codes — Fault Code Diagnostic Guide](/posts/goodman-gszc18-error-codes/)
