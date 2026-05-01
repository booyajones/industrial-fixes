---
title: "Goodman Heat Pump Error Codes - What It Means and How to Fix It"
description: "Complete guide to Goodman heat pump flash codes and diagnostic patterns for GSZ, DSZC, and GSXC series units. Find your code, understand the fault, and fix it fast."
pubDatetime: 2026-04-25T00:00:00Z
author: "Marcus Webb"
tags:
  - hvac
  - error-codes
---

Goodman heat pumps are installed in millions of American homes. When something goes wrong, the control board speaks via a blinking LED — a simple diagnostic language that tells you exactly what's failing. This guide covers all flash codes for Goodman heat pump systems including the GSZ, GSXC, DSZC, and ARUF series, plus the newer communicating models.

## What Does Goodman Heat Pump Error Codes Mean?

The diagnostic LED lives on the control board inside the air handler. On conventional (non-communicating) Goodman systems, the LED blinks a pattern you count. On communicating systems (using the ComfortNet protocol or matched with an AM/AMST air handler), the thermostat may display fault codes directly.

**Flash codes reset automatically** after the fault clears. If you want to force a reset, turn the thermostat to OFF for 30 seconds, then restore power.

### Complete Goodman Heat Pump Flash Code Reference

| Flashes | Fault | What It Means |
|---------|-------|---------------|
| 1 | Normal — heating or cooling running | No fault, system is operating |
| 2 | System lockout (pressure switch) | Low or high refrigerant pressure |
| 3 | Draft or pressure switch fault | Pressure switch stuck open or failed inducer (applies to matched air handler/furnace) |
| 4 | Open high-limit device | Overheating — filter or airflow issue |
| 5 | Flame sense fault | Dirty sensor or no ignition (matched gas furnace) |
| 6 | Defrost control fault | Defrost board or reversing valve problem |
| 7 | Lockout after 5 ignition failures | Gas/ignition fault (matched gas furnace) |
| 8 | Flame sensed after valve closed | Stuck gas valve — call a tech immediately |
| 9 | Fault in outdoor unit | See outdoor unit LED for detail |
| Continuous on | Control board fault | Replace board |
| Continuous off | No power to control board | Check breakers, fuses, transformer |

### 2 Flashes — Pressure Switch Lockout (Most Common)

This is the most frequently seen Goodman heat pump fault. The system has detected either low refrigerant pressure (suction side) or high refrigerant pressure (discharge side) and shut down to protect the compressor.

**Low pressure causes:** Refrigerant leak, restricted metering device (TXV or orifice), or a dirty indoor coil. **High pressure causes:** Dirty outdoor condenser coil, failed condenser fan motor, refrigerant overcharge, or non-condensable gases in the system.

**Start here:** Check that the outdoor fan is running when the compressor is on. If the fan isn't running but the compressor is, the fan motor or capacitor has failed, causing high pressure. If both are running and you still get 2 flashes, you need a tech with gauges.

### 4 Flashes — High Limit Open

On a Goodman heat pump with a matched gas furnace, 4 flashes means the heat exchanger is overheating. On a heat pump-only air handler, this indicates the electric strip heat high limit has tripped.

**In both cases: check the filter immediately.** A clogged filter is the cause 60% of the time. If the filter is clean, check that all registers are open, the blower is running, and the coil isn't iced over.

### 6 Flashes — Defrost Control Fault

The defrost board isn't initiating defrost properly, or the reversing valve isn't shifting during defrost. In heating mode, the outdoor coil can ice over without proper defrost cycles.

Look at the outdoor unit. If it's a solid block of ice all the way around the coil and the fan blades, the defrost system isn't working. Common causes: failed defrost thermostat (mounted on the coil), failed defrost board, or a stuck reversing valve.

### 9 Flashes — Outdoor Unit Fault

The air handler is reporting a fault from the outdoor heat pump unit. Walk outside and look at the control board LED on the outdoor unit — it will have its own flash code. Compare it against the outdoor unit fault table in the installation manual (search your outdoor unit model number + "installation instructions PDF" on Google — Goodman posts them free).

## How to Fix It

1. **Identify the flash code.** Count blinks, note the pattern, write it down.
2. **Check the basics first.** Filter condition, all circuit breakers on (including the outdoor disconnect), thermostat set correctly.
3. **Look at the outdoor unit.** Is the fan spinning? Is the coil blocked with ice, leaves, or cottonwood? Is the compressor making abnormal sounds?
4. **Reset the fault.** Thermostat to OFF → wait 30 seconds → back to HEAT or COOL. Watch the first 5 minutes of operation closely.
5. **For 2-flash lockouts:** Feel the suction line (larger insulated copper pipe) at the outdoor unit. In cooling mode it should be cold and slightly sweating. If it's warm or frosted solid, you have a refrigerant problem.
6. **For 4-flash limit trips:** Swap the filter. Verify every register in the house is open. Check the blower wheel for buildup.
7. **For 6-flash defrost faults:** Manually trigger defrost mode if available (most Goodman defrost boards have a TEST jumper — short it for 2–3 seconds).
8. **Replace the capacitor** if the fan isn't running or the compressor is slow to start. This is the #1 DIY fix on Goodman heat pumps.

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|-------------|
| Dual run capacitor (45/5 MFD, 440V) | Compressor or fan won't start — most common DIY fix | $15–$35 — [Search on Amazon](https://www.amazon.com/dp/B01M05L7B3?tag=errorcodefixes-20) |
| Contactor (30–40A, 24V coil) | Compressor won't start even with good capacitor | $20–$40 — [Search on Amazon](https://www.amazon.com/dp/B0CJFZQVPT?tag=errorcodefixes-20) |
| Defrost thermostat (Goodman B1226404) | Fixes 6-flash defrost fault | $15–$30 — [Search on Amazon](https://www.amazon.com/s?k=Goodman+defrost+thermostat+B1226404&tag=errorcodefixes-20) |
| Defrost control board (Goodman HK32EA001) | Fixes 6-flash when thermostat is fine | $40–$90 — [Search on Amazon](https://www.amazon.com/s?k=Goodman+defrost+board+HK32EA001&tag=errorcodefixes-20) |
| Reversing valve solenoid | Fixes stuck reversing valve (no mode switch) | $30–$70 — [Search on Amazon](https://www.amazon.com/s?k=heat+pump+reversing+valve+solenoid+24V&tag=errorcodefixes-20) |
| Condenser fan motor (208–230V, 1/5 HP) | Replaces failed outdoor fan motor | $60–$150 — [Search on Amazon](https://www.amazon.com/dp/B0D2L5NSMM?tag=errorcodefixes-20) |

## When to Call a Pro

- Any 2-flash code that returns within an hour of resetting — refrigerant diagnosis and charging requires EPA 608 certification and gauge manifolds.
- Ice buildup that covers the entire outdoor unit and doesn't clear after running defrost mode.
- The compressor is making grinding, clanking, or rattling sounds — these indicate internal mechanical failure.
- You replaced the capacitor and contactor and the outdoor unit still won't run.
- Code 8 (flame sensed with gas valve closed) on a matched furnace — the gas valve is stuck open, which is a fire/CO risk. Shut off gas and call immediately.
- The system blows warm air in cooling mode or cold air in heating mode — the reversing valve may be stuck, which requires refrigerant recovery to replace.

## Frequently Asked Questions

**Q: My Goodman heat pump runs in cooling but won't heat. No error codes. What's wrong?**

A: The most common cause is a stuck reversing valve. In cooling mode, the valve is in one position; in heating mode, it must shift. If it's stuck, the unit will cool but not heat (or vice versa). A tech can confirm this with temperature measurements across the valve body. Sometimes the solenoid coil on the valve fails — that's a much cheaper fix than replacing the whole valve.

**Q: How do I know if my Goodman heat pump is low on refrigerant?**

A: Signs include: the outdoor unit ices up in cooling mode, the suction line is warmer than expected, the system runs constantly without reaching setpoint, and high electricity bills. The definitive test requires refrigerant gauges. Note that adding refrigerant without fixing the leak is a temporary fix — you'll be back in the same spot within a season.

**Q: The Goodman heat pump outdoor unit is iced over solid. Should I pour hot water on it?**

A: Don't. Hot water can crack the coil if the ice is thick. Let it thaw naturally in defrost mode or in ambient air above 40°F. If the ice keeps coming back within a day, the defrost system isn't working. If ice builds up in cooling mode, you have a refrigerant or airflow problem, not a defrost issue.

**Q: Can I run my Goodman heat pump in heat mode when it's 15°F outside?**

A: Goodman heat pumps are rated for heating down to around 0°F–5°F on newer models, but efficiency drops sharply below 30–35°F. Most systems have electric strip heaters in the air handler that kick in as backup heat. If the outdoor temperature is below the unit's rating and the heat strips aren't working, you won't get adequate heating. Check that the aux/emergency heat setting works independently.

**Q: My Goodman heat pump is 12 years old and needs a new compressor. Is it worth fixing?**

A: At 12 years old with a compressor failure, this is a genuine replace-or-repair decision. A compressor replacement runs $1,200–$2,500 installed. A new efficient heat pump system runs $4,000–$8,000 installed. If the rest of the system (coils, electrical, ductwork) is in good shape and the compressor is still under the 10-year parts warranty (Goodman offers this if registered within 60 days of install), repair can make sense. If the warranty expired, the economics usually favor replacement, especially with current energy-efficiency incentives and utility rebates.

## Related Articles

- [Goodman 1 Flash Error Code — What It Means](/posts/goodman-1-flash-error-code/)
- [Goodman 2 Flash Error Code — Causes & Fix](/posts/goodman-2-flash-error-code/)
- [Goodman 3 Flash Error Code — Pressure Switch Stuck Open Fix](/posts/goodman-3-flash-error-code/)
- [Goodman 4 Flash Error Code — Causes & Fix](/posts/goodman-4-flash-error-code/)
- [Goodman 5 Flash Error Code — Causes & Fix](/posts/goodman-5-flash-error-code/)
