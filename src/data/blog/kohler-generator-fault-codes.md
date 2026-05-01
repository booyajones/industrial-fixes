---
title: "Kohler Generator Fault Codes — Complete Guide"
description: "Kohler generator fault codes for RES, RESVL, and commercial series: all alarm codes, causes, and step-by-step fixes for Kohler standby generators."
pubDatetime: 2026-04-22T19:00:00Z
modDatetime: 2026-04-22T19:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - generator
  - kohler
  - electrical
---

## Kohler Generator Fault Codes — Quick Reference

Kohler standby generators use the Decision-Maker controller (Decision-Maker 3000 on residential units, Decision-Maker 3500/6000 on commercial). Fault codes appear on the controller's LCD display and are logged in fault history. Alarms are classified as pre-alarms (warnings) and shutdowns.

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixes-20) | Type | Meaning | Quick Fix |
|------|------|---------|-----------|
| [Low Battery](https://www.amazon.com/s?k=Low+Battery&tag=errorcodefixes-20) | Warning | Battery voltage low | Test and replace battery |
| [Battery Charger Fault](https://www.amazon.com/s?k=Battery+Charger+Fault&tag=errorcodefixes-20) | Warning | Charging circuit issue | Check charger; check AC power to charger |
| [Fail to Start](https://www.amazon.com/s?k=Fail+to+Start&tag=errorcodefixes-20) | Shutdown | Engine did not start after retries | Check fuel, battery, starter |
| [Low Oil Pressure](https://www.amazon.com/s?k=Low+Oil+Pressure&tag=errorcodefixes-20) | Shutdown | Oil pressure below limit | Check oil level and condition |
| [High Engine Temperature](https://www.amazon.com/s?k=High+Engine+Temperature&tag=errorcodefixes-20) | Shutdown | Coolant or oil over-temp | Check coolant, oil, fan |
| [Overspeed](https://www.amazon.com/s?k=Overspeed&tag=errorcodefixes-20) | Shutdown | Engine RPM too high | Governor fault |
| [Underspeed](https://www.amazon.com/s?k=Underspeed&tag=errorcodefixes-20) | Shutdown | Engine RPM too low | Load, governor, or fuel issue |
| [High AC Voltage](https://www.amazon.com/s?k=High+AC+Voltage&tag=errorcodefixes-20) | Shutdown | Generator output voltage high | AVR fault |
| [Low AC Voltage](https://www.amazon.com/s?k=Low+AC+Voltage&tag=errorcodefixes-20) | Shutdown | Generator output voltage low | AVR fault; high load |
| [Overcurrent](https://www.amazon.com/s?k=Overcurrent&tag=errorcodefixes-20) | Shutdown | Load exceeds generator capacity | Reduce load; check for fault |
| [Ground Fault](https://www.amazon.com/s?k=Ground+Fault&tag=errorcodefixes-20) | Shutdown | Ground fault in system | Inspect wiring; call electrician |
| [Exercise Overdue](https://www.amazon.com/s?k=Exercise+Overdue&tag=errorcodefixes-20) | Warning | Generator hasn't run exercise | Run manual exercise; check schedule |
| [Line Power Available](https://www.amazon.com/s?k=Line+Power+Available&tag=errorcodefixes-20) | Status | Utility power has returned | Normal status — transfer pending |

## Most Common Faults

### Fail to Start
Like all standby generators, Kohler units most commonly fail to start due to battery or fuel issues. The Decision-Maker controller will display "Fail to Start" after 3 crank attempts (approximately 30 seconds of total cranking). 

**Diagnosis sequence:**
1. Check battery voltage: should be 12.4–12.8V at rest. Less than 12V indicates a discharged or failed battery.
2. Check battery connections: corrosion on battery terminals is extremely common in outdoor generator installations. Clean with baking soda solution.
3. Check fuel level: confirm the generator fuel supply valve is open and the tank is not empty or contaminated.
4. Check spark (gas models) or glow plugs (diesel): if the battery and fuel are confirmed good, check the ignition system.

### Low Oil Pressure Shutdown
After confirming oil level is correct, check oil condition — oil that has emulsified (appears milky) indicates coolant is mixing with oil, a serious engine problem. Fresh oil that's black after only a short runtime may indicate the engine is using oil abnormally. If oil level and condition are both correct, test the oil pressure sender with a mechanical gauge — senders do fail.

### High Engine Temperature
On Kohler liquid-cooled generators (12–150 kW range), high engine temperature shutdowns require checking:
- Coolant level in radiator and overflow tank
- Radiator fins for debris blockage (especially important in installations near plant life)
- Cooling fan clutch or fan belt (belt-driven fans)
- Thermostat function
- Raw water pump impeller (on marine or industrial units with raw water cooling)

### Overspeed
The Kohler governor maintains engine speed at 3600 RPM (60 Hz) or 1800 RPM (60 Hz for 4-pole units). An overspeed alarm means the engine exceeded 10% above target RPM. Common causes:
- Broken governor spring (most common on high-hours units)
- Governor linkage stuck in open position
- Electronic governor actuator failure
- Fuel delivery problem causing uncontrolled speed surge on startup

### Ground Fault
A ground fault alarm indicates current flowing in an unintended path to ground in the generator's AC output circuit. This is a serious electrical fault. **Do not operate the generator with an active ground fault.** A licensed electrician should diagnose and repair ground fault conditions.

## Kohler Weekly Exercise
Configure the automatic exercise schedule via the Decision-Maker controller: Menu → Exercise → Set Time. Kohler recommends a minimum 30-minute weekly exercise at approximately 30% load.

## When to Call a Pro
AVR adjustments, governor repair, and any electrical fault (overcurrent, ground fault, voltage faults) require a Kohler-authorized service technician.
