---
title: "Ruud Achiever Plus Furnace Error Codes - Flash Code Guide"
description: "Ruud Achiever Plus furnace LED blink codes 1 through 9 decoded. What each flash pattern means, DIY fixes, and when to call a tech."
pubDatetime: 2026-04-25T00:00:00Z
author: "Marcus Webb"
tags:
  - hvac
  - error-codes
---

The Ruud Achiever Plus is a legacy gas furnace that remains in service in millions of homes across North America. Built as a workhorse unit, it uses a single diagnostic LED on the control board to communicate fault conditions. Understanding the LED blink codes on this furnace is one of the most practical DIY HVAC skills you can develop , these codes tell you exactly why your furnace isn't heating, often saving you the $150+ diagnostic fee on a service call.

## What Does a Ruud Achiever Plus Furnace Error Code Mean?

The diagnostic LED is located on the main control board inside the lower furnace cabinet. It's visible through the small viewing window on the access door , you don't need to open anything to read it. Watch the LED for about 10–15 seconds to catch a full cycle of the blink pattern. The furnace blinks a number of times, pauses for 2–3 seconds, then repeats the same pattern. That number of blinks is your fault code.

A solid continuous ON means the board has power and is in normal operation with no faults. A solid continuous OFF with no blinking means the board has no power. A rapid sequence of blinks without a consistent pause-and-repeat pattern indicates a board failure.

### Ruud Achiever Plus Blink Code Reference

**1 Flash , Normal Operation / System in Standby**
One slow flash per second is the healthy heartbeat of the control board. The board is powered, no faults are present, and the system is waiting for a thermostat call. If you see 1 flash but the furnace isn't running when you expect heat, the problem is at the thermostat or the wiring between the thermostat and furnace.

**2 Flashes , System Lockout**
The furnace reached the maximum number of ignition retry attempts and locked out for safety. This is the most common fault code homeowners see. The furnace tried to light, couldn't prove a flame, and gave up. Before calling a tech, reset the furnace: cut power at the furnace switch or breaker for 30 seconds, then restore. If it heats normally for a day and then locks out again, the root cause hasn't been fixed.

**3 Flashes , Draft Pressure Fault (Pressure Switch Open)**
The furnace's draft pressure switch is not closing. The inducer motor should create negative pressure in the flue that causes the pressure switch to close, allowing the ignition sequence to proceed. If the switch doesn't close, the furnace stops. Check the vent termination outside for blockages (birds' nests, ice, debris). Check the pressure switch hose running from the inducer housing , it cracks and disconnects over time. A split hose is a 15-minute DIY fix.

**4 Flashes , Open High-Limit Switch**
The furnace overheated. The high-limit switch on the heat exchanger tripped open to prevent damage. The #1 cause is a dirty air filter , replace it now. Also check every supply and return register in the house to ensure none are blocked or closed. A dirty blower wheel (dusty fins reduce airflow significantly) and a failed blower motor also trigger this code.

**5 Flashes , Flame Sensed Without Call for Heat (False Flame)**
The control board is detecting a flame signal when it hasn't commanded the gas valve to open. This indicates either a leaking gas valve (gas is flowing when it shouldn't be) or an electrical fault causing the flame sense circuit to read a false positive. This is a gas safety issue. Do not reset and run the furnace. Call a licensed HVAC technician.

**6 Flashes , Rollout Limit Switch Open**
The manual-reset rollout limit switch has tripped. Rollout switches are positioned near the burners and trip if flames extend outside the combustion chamber ("roll out"). This happens when the flue is blocked, the heat exchanger is cracked, or the inducer motor is failing. A rollout switch trip is a carbon monoxide warning. Do not reset it and run the furnace without professional inspection.

**7 Flashes , Gas Valve / Igniter Fault**
The furnace commanded the gas valve to open and the igniter to energize, but no flame was established. Different from Code 2 (which is the final lockout after all retries are exhausted) , Code 7 is the per-attempt fault. A failed hot surface igniter is the most common cause. The igniter should glow bright orange during the ignition trial , if it doesn't visibly glow, it's failed. Silicon carbide igniters are fragile; never touch them with bare hands.

**8 Flashes , Loss of Flame During Run Cycle**
The flame established and proved at the sensor, but then went out during normal operation. The flame sensor may be dirty (most common), gas pressure may be fluctuating, or there is a combustion issue (insufficient combustion air). Clean the flame sensor rod with fine steel wool , this resolves the majority of Code 8 calls.

**9 Flashes , Ignition Lockout , Check Gas Supply**
The furnace attempted ignition but received no flame response at all , the gas valve may not be opening, gas supply may be off, or the gas valve has failed. Verify the gas shutoff valve at the furnace is fully open (handle parallel to the pipe). Check that other gas appliances in the home (range, water heater) are receiving gas. If gas is confirmed at other appliances, the furnace gas valve is the likely failure point.

## How to Fix It

1. **Start with the air filter.** A clogged filter is responsible for 3-flash, 4-flash, and many 2-flash codes (overheating induces ignition timing problems). Pull the filter, hold it up to a light source , if you can't see light through it, it's overdue.
2. **Check the flue.** Walk outside and locate the PVC exhaust pipe (90° elbows at the wall) or the metal vent cap. Make sure nothing is blocking the terminal. In winter, ice dams around PVC terminations are common.
3. **Inspect the pressure switch hose.** For a 3-flash code, locate the clear or black rubber hose running from the inducer housing to the pressure switch (a small round component with electrical terminals). If the hose is cracked, kinked, or disconnected, replace it with matching 3/8" ID tubing.
4. **Clean the flame sensor.** The flame sensor is a metal rod in a ceramic holder positioned in the burner assembly. Disconnect the wire, pull the sensor (one screw), and lightly rub the rod with steel wool or fine sandpaper. Reinstall and test.
5. **Test the igniter.** Set your multimeter to resistance mode. A good silicon carbide igniter reads 30–200 ohms. An open reading (OL) means the igniter has failed. Replace it.
6. **Check gas pressure.** A manometer connected to the gas valve inlet tapping should read approximately 3.5–7 inches water column on natural gas. Low gas pressure on cold days (high demand on utility) can trigger multiple fault codes.
7. **Reset the rollout switch (Code 6 only , with caution).** The rollout switch has a small red button on its face. You can press it to reset. But only do this after you've confirmed the flue is clear and there's no visible sign of flame rollout damage. Call a tech if you see any scorching near the burners.

## Parts You May Need

| Part | Use | Buy on Amazon |
|------|-----|---------------|
| Norton 271N Hot Surface Igniter | Replace failed igniter for Code 2, 7, or 9 | [View on Amazon](https://www.amazon.com/dp/B00BTLLJ40?tag=errorcodefixes-20) |
| Furnace Flame Sensor Rod | Fix dirty or failed flame sensor causing Code 8 | [View on Amazon](https://www.amazon.com/dp/B0CZ7M9V4D?tag=errorcodefixes-20) |
| HVAC Pressure Switch Universal (.50 WC) | Replace failed pressure switch for Code 3 | [View on Amazon](https://www.amazon.com/dp/B013J2J97A?tag=errorcodefixes-20) |
| 3/8 ID Pressure Switch Hose (Clear PVC, 5 ft) | Replace cracked pressure switch tubing | [View on Amazon](https://www.amazon.com/s?k=3+8+id+clear+vinyl+tubing+pressure+hose&tag=errorcodefixes-20) |
| 20x25x1 MERV-8 Furnace Filter (6 pack) | Clear high-limit and draft faults from restricted airflow | [View on Amazon](https://www.amazon.com/s?k=20x25x1+merv+8+furnace+filter&tag=errorcodefixes-20) |
| Rollout Limit Switch (Ruud/Rheem compatible, 250°F) | Replace tripped rollout switch after professional inspection | [View on Amazon](https://www.amazon.com/dp/B0BN3TRG9R?tag=errorcodefixes-20) |

## When to Call a Pro

**5-flash code , immediately.** A false flame detection or leaking gas valve is a combustion safety hazard. Do not run the furnace.

**6-flash code , before resetting.** Rollout limit trips must be inspected for heat exchanger cracks, which can leak carbon monoxide into living spaces. A cracked heat exchanger requires furnace replacement.

**4-flash code that returns after a clean filter.** Persistent high-limit faults after filter replacement suggest a cracked heat exchanger or failed blower motor, both of which require professional diagnosis.

**Any fault code involving gas pressure.** Gas valve replacement and pressure adjustment require a licensed technician with a manometer.

**Fault codes that return within 24 hours of reset.** If the furnace is cycling into lockout daily, it is not safe to keep resetting without finding the root cause.

## FAQ

**Q: My Ruud Achiever Plus shows 3 flashes but I already replaced the pressure switch , what else can cause this?**
A: On the Achiever Plus, blocked condensate drain lines cause the same 3-flash code as a failed pressure switch. The condensate trap (especially on models with a secondary heat exchanger) can fill with water if the drain is blocked, and the water column in the pressure hose causes the switch to misread draft. Check and clear the condensate drain first, then replace the switch if needed.

**Q: How long does a Ruud Achiever Plus typically last?**
A: These furnaces were designed with a 20-year service life. Many remain in service at 25+ years. The heat exchanger, blower motor, and control board are the most common end-of-life failures. If you're getting multiple fault codes on a unit over 18 years old, compare repair cost to replacement , parts for legacy units are increasingly expensive.

**Q: Can I replace the Achiever Plus control board with a universal aftermarket board?**
A: Yes. Universal control boards from ICM Controls, White-Rodgers, and Robertshaw are compatible with most Ruud Achiever Plus single-stage models. Match the igniter type (silicon carbide vs. silicon nitride), blower motor type (multi-speed PSC), and accessory output requirements to your specific model.

**Q: The Achiever Plus shows 4 flashes after I turned on the heat for the first time this season. Is that normal?**
A: It can happen when the unit sits all summer. Dust accumulates on the blower wheel over summer, reducing airflow. A high-limit trip on first-of-season startup often means the blower wheel needs cleaning. Pull the blower drawer, inspect the wheel, and vacuum the fins. It can be dramatic how much debris builds up over 6 months.
