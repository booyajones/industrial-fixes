---
title: "Heat Pump Auxiliary Heat Always On - Causes and Fixes"
description: "Why your heat pump auxiliary heat runs constantly, how to tell normal operation from a real failure, and step-by-step fixes for reversing valve faults, low refrigerant, and balance point issues."
pubDatetime: 2026-04-25T00:00:00Z
author: errorcodefixes.com
tags:
  - hvac
  - error-codes
---

Your heat pump's auxiliary heat is supposed to be a backup — a brief supplement when the outdoor temperature drops too low for the heat pump to keep up on its own. When auxiliary heat runs constantly, you're burning expensive electric resistance heat instead of the efficient refrigerant-based heat pump cycle. Depending on your electric rate and home size, aux heat running all day can add $100–$400 to a monthly heating bill.

The challenge is that aux heat running isn't always a problem. Sometimes the system is working exactly as designed. This guide walks you through distinguishing normal operation from a real fault, then diagnosing and fixing the most common causes.

## What Does "Auxiliary Heat Always On" Mean?

Most heat pump thermostats have a separate "Aux Heat" or "Emergency Heat" indicator. If this light is on whenever the system is heating, it means the electric resistance elements in your air handler are active. The question is: why?

Heat pumps use auxiliary heat in two legitimate scenarios:
1. **Outdoor temperature is below the balance point** (typically 30–40°F for standard heat pumps, 0–15°F for cold-climate inverter heat pumps). Below this temperature, the heat pump can't extract enough heat from the air to match your home's heat loss, so aux heat supplements.
2. **Emergency defrost:** During the defrost cycle, the system briefly runs aux heat to prevent cold air from blowing into the house while the outdoor coil thaws.

If aux heat is running continuously at temperatures above your balance point — say, 45°F outside — you have a real problem.

## Normal Operation vs. Real Failure

**Normal:** Aux heat light comes on when it's below 35°F and outdoor temps are in the teens or single digits. Aux runs for a few hours during extreme cold, then shuts off as temps rise.

**Also normal:** Aux runs briefly (5–15 minutes) during each defrost cycle. Defrost happens every 30–90 minutes in cold, humid weather.

**Problem signal:** Aux heat runs continuously when outdoor temperature is 40°F or above. Aux heat runs even in moderate weather (50s, 60s). The system never runs in heat pump mode at all — it's always on emergency heat even though the thermostat isn't set to emergency heat.

## How to Fix It

**1. Check the Balance Point Setting**

Many communicating thermostats (Honeywell T10, Ecobee, Nest, Carrier Infinity, etc.) have a configurable balance point or "aux heat lockout temperature." If this is set too high — say, 50°F — the system will call for aux heat every time it's below 50°F outside, which is most of winter.

- On a Honeywell T10 Pro or similar: go to Installer Setup and look for "Balance Point" or "Aux Lockout Temp." Set it to 35°F for standard heat pumps, or lower (25–30°F) for high-efficiency inverter units.
- On Ecobee: Settings > Installation Settings > Equipment > Heat Pump > Aux Heat Lockout Temperature.
- On Nest: Equipment > Heat Pump Balance. Set to "Max Savings" to minimize aux use.

A correctly set balance point fixes a lot of "aux heat always on" complaints with no hardware repair needed.

**2. Check the Outdoor Temperature Sensor**

Most heat pump systems use an outdoor temperature sensor to decide when to enable auxiliary heat. If this sensor fails and reads artificially low (like -20°F), the system thinks it's always in emergency territory and runs aux heat constantly.

- Locate the outdoor sensor: it's usually a small thermistor clipped to the outdoor unit or mounted on the house exterior near the thermostat.
- Compare its reading in the thermostat's diagnostic menu to an independent thermometer.
- If the sensor reads 10–20°F colder than actual, it's failed. Replace it.

**3. Check for a Stuck or Failing Reversing Valve**

The reversing valve is the component that switches a heat pump between heating and cooling mode. In heating mode, the reversing valve routes refrigerant so the outdoor coil acts as the evaporator (absorbing heat from outside air) and the indoor coil acts as the condenser (releasing heat inside).

If the reversing valve is stuck in cooling mode (or stuck mid-position), the heat pump runs but blows cold or lukewarm air in heating mode. The system detects that the temperature isn't rising and eventually calls for aux heat to compensate — which then runs continuously trying to make up for the non-functioning heat pump.

**Diagnose a stuck reversing valve:**
- Set the thermostat to cooling mode. Check if the system cools effectively.
- Set the thermostat to heating mode. Check if the discharge air (from the registers) is warm.
- If it cools fine but won't heat (or heats fine but won't cool), the reversing valve is stuck in one position.
- You can also measure suction and discharge line temperatures in both modes. In heating mode, the suction line (large copper pipe) should be cold/frosted; in cooling mode, it should be cold. If these are reversed, the valve is stuck.

Reversing valve replacement is an intermediate-level HVAC repair — it requires recovering the refrigerant, brazing in the new valve, pulling a vacuum, and recharging. Most homeowners call a tech for this one.

**4. Check Refrigerant Charge**

Low refrigerant charge is a major cause of heat pumps that struggle to heat. A heat pump extracts heat from outdoor air and moves it inside via the refrigerant circuit. With insufficient refrigerant, the heat pump's capacity drops dramatically — it can't keep up, so aux heat runs to fill the gap.

Signs of low refrigerant in heating mode:
- Ice or frost on the outdoor unit that doesn't fully clear during defrost.
- Suction line pressure lower than expected for outdoor ambient temperature.
- Low suction line superheat.
- System runs continuously in heating mode without reaching setpoint.

Refrigerant diagnosis and recharge requires EPA 608 certification and proper gauges. If you suspect low refrigerant, have a tech measure the charge. Adding refrigerant without fixing the leak is a temporary patch — find and fix the leak first.

**5. Check the Defrost Board / Defrost Timer**

A heat pump defrosts on a schedule (time or demand-based) to clear frost from the outdoor coil. If the defrost board or sensor fails:
- The unit may get stuck in defrost mode, running aux heat continuously while it "defrosts."
- The unit may never initiate defrost, allowing the outdoor coil to ice over completely. A fully iced coil can't absorb heat — the heat pump effectively stops working, forcing aux heat to take over.

Check the outdoor unit for excessive frost or solid ice buildup. If you find a brick of ice on the outdoor coil when it's 35°F outside, the defrost system has failed. This requires board or sensor replacement.

**6. Verify the Heat Pump Isn't Locked Out**

Some thermostats have an "outdoor lockout" that prevents the heat pump from running below a set temperature. If this lockout is set too high, the heat pump never runs during cold weather and aux heat runs 100% of the time.

Find this setting in the installer configuration on your thermostat. A standard setting is 35°F for conventional heat pumps. Cold-climate units (Bosch IDS, Mitsubishi Hyper Heat, Carrier Greenspeed) can operate down to -13°F and should have the lockout set very low or disabled.

**7. Check Indoor Coil and Air Handler**

A severely restricted indoor coil (dirty coil, clogged filter) reduces the heat pump's ability to transfer heat into the home. In extreme cases, the heat pump runs but can't move enough heat to satisfy the thermostat — aux heat activates to compensate.

- Replace the air filter if it hasn't been changed in more than 3 months.
- Inspect the indoor coil for dust and debris buildup. A dirty coil needs professional cleaning.
- Check all supply and return registers for blockages (furniture, closed dampers).

## Parts You May Need

| Part | Use | Amazon Link |
|------|-----|-------------|
| Outdoor Temperature Sensor (NTC Thermistor) | Replace failed outdoor sensor causing false aux lockout | [View on Amazon](https://www.amazon.com/s?k=outdoor+temperature+sensor+NTC+thermistor+HVAC&tag=errorcodefixes-20) |
| Refrigerant Manifold Gauge Set | Diagnose refrigerant charge level | [View on Amazon](https://www.amazon.com/s?k=refrigerant+manifold+gauge+set+heat+pump&tag=errorcodefixes-20) |
| Defrost Control Board (universal or OEM) | Replace failed defrost initiation board | [View on Amazon](https://www.amazon.com/s?k=heat+pump+defrost+control+board&tag=errorcodefixes-20) |
| Honeywell T10 Pro Smart Thermostat | Replace thermostat with misconfigured balance point | [View on Amazon](https://www.amazon.com/s?k=Honeywell+T10+Pro+smart+thermostat+heat+pump&tag=errorcodefixes-20) |
| Programmable Balance Point Thermostat | Thermostat with configurable aux lockout for heat pump | [View on Amazon](https://www.amazon.com/s?k=heat+pump+thermostat+balance+point+configurable&tag=errorcodefixes-20) |

## When to Call a Pro

- **Reversing valve replacement:** Requires refrigerant recovery, brazing, vacuum, and recharge. Not a DIY repair.
- **Refrigerant issues:** Low charge diagnosis and leak repair requires EPA 608 certification and specialized equipment.
- **Defrost board diagnosis on older systems:** If you don't have the service manual and the defrost timing/demand circuit, improper diagnosis leads to unnecessary part replacement.
- **Aux heat that won't run at all:** If the heat pump fails entirely in cold weather and aux heat also doesn't engage, you may have a failed sequencer or heating element — a safety issue that needs professional attention.

## FAQ

**Q: Is it bad for my heat pump to run on aux heat all winter?**

A: It's not dangerous, but it's expensive. Electric resistance heat (aux heat) produces one unit of heat per unit of electricity consumed — a Coefficient of Performance (COP) of 1.0. A heat pump in mild weather achieves a COP of 2.5–4.0, meaning it produces 2.5–4x more heat per dollar of electricity. Running aux heat all winter costs 2–4x more than running in heat pump mode.

**Q: What temperature should aux heat kick in?**

A: For a standard heat pump (not cold-climate), aux heat typically kicks in when outdoor temperature drops below 30–40°F AND the heat pump can't maintain setpoint. For cold-climate inverter heat pumps (Bosch IDS 2.0, Mitsubishi Hyper Heat, Daikin Aurora), aux heat may never be needed above 0°F. The exact balance point depends on your home's heat loss and your heat pump's rated capacity.

**Q: My thermostat shows "Em Heat" (Emergency Heat) but I didn't set it. Why?**

A: If the thermostat is in emergency heat mode without your input, either someone accidentally activated it or the thermostat has a software glitch. Manually check the thermostat settings and confirm it's set to "Heat" — not "Emergency Heat." Emergency Heat bypasses the heat pump entirely and runs only the electric resistance elements, which is very expensive for sustained use.

**Q: How long does a defrost cycle last?**

A: A normal defrost cycle runs for 5–15 minutes, typically ending when the outdoor coil temperature reaches 57°F or after a maximum of 10 minutes — whichever comes first. If your unit is in "defrost mode" for 30+ minutes repeatedly, the defrost termination sensor or board has failed.

**Q: My aux heat light came on for the first time ever. Should I be worried?**

A: Not necessarily. If it's extremely cold outside (below 25–30°F), aux heat engaging for the first time is completely normal — your system is working correctly. If it's 45°F outside and aux heat is running constantly, that warrants investigation using the steps above.
