---
title: "Navien NCB-700 Combination Boiler Error Codes - Full Fault Guide"
description: "Full fault code guide for the Navien NCB-700 combination boiler. Covers error codes E001 through E109, diagnostic steps, and repair options for both heating and domestic hot water circuits."
pubDatetime: 2026-04-25T00:00:00Z
author: "Marcus Webb"
tags:
  - hvac
  - error-codes
---

The Navien NCB-700 is a high-efficiency condensing combination boiler that handles both space heating and domestic hot water in a single wall-hung unit. It's a popular choice for homes without ductwork that want hydronic radiant heat or baseboard heating alongside on-demand hot water. Like all Navien products, the NCB-700 uses a detailed error code system that narrows down faults quickly — if you know what to look for.

This guide covers every NCB-700 error code from E001 through E109, with diagnostic steps and repair guidance for each.

## What Does Each NCB-700 Error Code Mean?

### E001 — Ignition Failure

The unit attempted to ignite and failed after the standard number of retries. The burner never achieved a stable flame signal.

**Causes:** No gas supply, gas valve not fully open, dirty or failed igniter, cracked or fouled flame sensor rod, control board not sending ignition signal.

### E003 — Ignition Failure During Operation

The flame was established but went out during normal operation. This is a mid-cycle flame loss, not a startup failure.

**Causes:** Low gas pressure, draft/venting problem drawing combustion gases back, failed flame sensor, gas valve sticking closed mid-cycle.

### E004 — False Flame Detection

The control board detects a flame signal when the gas valve is commanded closed. This is a safety fault — the board thinks there's an uncontrolled flame.

**Causes:** Shorted or leaking flame sensor wire, failed gas valve not closing completely, control board fault.

### E010 — Abnormal Air Pressure (Combustion Air Fan Fault)

The air pressure switch indicates abnormal pressure. The fan may not be running, the pressure switch may be stuck, or there's a blockage in the combustion air path.

**Causes:** Blocked air intake or exhaust vent, faulty inducer fan motor, failed air pressure switch, disconnected pressure switch tubing.

### E011 — Fan Speed Error

The control board is commanding the fan to run but the tachometer feedback indicates the RPM is out of range.

**Causes:** Fan motor bearing failure, loose fan-to-motor coupling, tachometer wire disconnected, control board output driver failure.

### E012 — Exhaust High Temperature

The exhaust temperature sensor has detected temperatures above the safe threshold. This is often a sign of restricted venting or a heat exchanger problem.

**Causes:** Blocked flue outlet, cracked or failed exhaust thermistor, scale buildup in the heat exchanger reducing thermal transfer.

### E016 — Over-Heating (DHW Outlet Too High)

The domestic hot water outlet temperature has exceeded the maximum safe limit.

**Causes:** Very low DHW flow rate with high burner demand, failed DHW outlet thermistor (reading low, causing the board to fire the burner continuously), scale buildup.

### E027 — Water Leak Detected

The NCB-700 has an internal water leak sensor. E027 fires when moisture is detected inside the unit cabinet.

**Causes:** Failed O-ring or seal in the water circuit, cracked heat exchanger, loose fitting on the hydronic or DHW side.

### E030 — DHW Inlet Thermistor Fault

The DHW (domestic hot water) inlet temperature sensor has failed or gone out of range.

### E031 — DHW Outlet Thermistor Fault

The DHW outlet temperature sensor has failed.

### E032 — Central Heating Supply Thermistor Fault

The heating circuit supply (flow) thermistor has failed.

### E033 — Central Heating Return Thermistor Fault

The heating circuit return thermistor has failed.

### E047 — PCB (Control Board) Internal Fault

The main PCB has detected an internal error. This usually requires board replacement unless a power cycle clears it.

### E060 — Gas Valve Fault

The gas valve circuit has returned an abnormal signal. The valve may not be opening or closing as commanded.

### E109 — Fan Pressure Switch Did Not Open

After a purge cycle, the pressure switch should open (indicating fan off). If it stays closed, E109 fires. This often means the pressure switch is stuck closed or the tubing is kinked.

---

## How to Fix It

### Fixing E001 / E003 — Ignition and Flame Loss

1. **Verify gas supply.** Check that the main gas shutoff to the boiler is fully open. If other gas appliances work, check the unit's internal gas valve shutoff.

2. **Inspect the igniter.** The igniter electrode should have a clean tip with no carbon deposits. Clean with fine-grit sandpaper. Check the igniter gap — Navien specifies approximately 3–4mm between the electrode and ground.

3. **Clean the flame sensor rod.** Use fine steel wool or a clean cloth to polish the sensor rod. Even a thin film of oxidation can prevent reliable flame current signal.

4. **Check gas pressure.** Use a manometer on the gas valve test port. Navien NCB-700 requires 3.5–10.5 inches water column (WC) natural gas supply pressure at the unit inlet. Low pressure = E001.

5. **Inspect venting.** Check both the combustion air intake and exhaust outlet for obstruction (bird nests, ice in winter, debris). A blocked flue also causes ignition failure because combustion gases can't exhaust.

### Fixing E010 / E011 — Fan and Air Pressure Issues

1. **Inspect vent pipes.** Clear any obstruction from the intake and exhaust pipes at the exterior wall termination.

2. **Check the pressure switch tubing.** The small rubber hose connecting the blower housing to the pressure switch can crack or disconnect. Inspect and reconnect if loose.

3. **Test the pressure switch.** With the fan running, use a multimeter to verify the switch changes state. A switch that stays open regardless of fan speed is failed.

4. **Check fan RPM feedback.** Disconnect the tachometer wire from the control board and test with a multimeter. No signal while the motor is running indicates a failed hall sensor on the fan.

### Fixing E030–E033 — Thermistor Faults

1. Power down at the breaker.
2. Locate the failed thermistor (labeled in the Navien service manual by circuit).
3. Test resistance with a multimeter — at 68°F, NTC thermistors should read approximately 10,000–12,000 ohms.
4. Replace the thermistor. Navien thermistors are unit-specific; order by model and position (DHW inlet, DHW outlet, CH flow, CH return).

### Fixing E027 — Water Leak

1. Visually inspect all internal connections with a flashlight. Look for wetness around fittings, the heat exchanger face, and the condensate drain pan.
2. Check all O-rings and compression fittings on the domestic hot water and heating circuits.
3. If the primary heat exchanger is leaking, a replacement unit is typically required — Navien heat exchangers are not field-repaired.

---

## Parts You May Need

| Part | What It Fixes | Amazon Link |
|------|--------------|-------------|
| Navien NCB-700 Igniter Electrode | E001 ignition failure | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-navien-ncb-700-error-codes&k=navien+combination+boiler+igniter+electrode&tag=errorcodefixes-20) |
| Flame Sensor Rod (Navien compatible) | E001 / E003 flame detection | [View on Amazon](https://www.amazon.com/s?k=Flame+Sensor+Rod+%28Navien+compatible%29&tag=errorcodefixes-20) |
| NTC Thermistor Replacement 10K | E030 / E031 / E032 / E033 thermistor fault | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-navien-ncb-700-error-codes&k=navien+thermistor+replacement+boiler&tag=errorcodefixes-20) |
| Condensing Boiler Air Pressure Switch | E010 / E109 pressure switch fault | [View on Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-navien-ncb-700-error-codes&tag=errorcodefixes-20) |
| Navien Gas Valve Replacement | E060 gas valve fault | [View on Amazon](https://www.amazon.com/dp/B0015KAHHA?ascsubtag=ecf-navien-ncb-700-error-codes&tag=errorcodefixes-20) |
| Boiler Descaling Flush Kit | Scale-related overheating and thermistor faults | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-navien-ncb-700-error-codes&k=boiler+descaling+kit+hydronic&tag=errorcodefixes-20) |

---

## When to Call a Pro

The NCB-700 is a high-pressure hydronic system that combines gas combustion with both heating and domestic hot water circuits. Call a licensed professional if:

- **E001 or E003 persists** after cleaning the igniter and flame sensor — gas valve replacement or control board diagnosis requires a licensed gas technician.
- **E027 appears** — internal water leaks on a pressurized hydronic system can escalate quickly and should be assessed immediately.
- **E047 (PCB fault)** — control board replacement on a combination boiler requires careful commissioning of both heating and DHW circuits.
- **You smell gas** — shut the gas off at the main, leave the building, and call your gas utility before anything else.
- The boiler is under warranty — DIY repairs may void coverage. Navien's standard warranty requires licensed installer involvement for major component replacement.

---

## FAQ

**Q: How do I reset the Navien NCB-700 after an error code?**
A: Press and hold the Reset button on the front panel for 3 seconds. For E047 or persistent codes, power cycle at the breaker (off for 60 seconds, then back on).

**Q: The NCB-700 shows E001 only on the first ignition attempt of the day. Why?**
A: This is often air trapped in the gas line after an extended off period. The unit purges air on the first attempt and ignites on retry. If the code clears on retry without lockout, this is usually normal. If it locks out, check gas pressure.

**Q: My NCB-700 shows E010 but the fan sounds like it's running fine. What's wrong?**
A: The pressure switch tubing is the most likely culprit. A small crack or disconnection in the tubing between the fan housing and the pressure switch will cause E010 even when the fan is running normally.

**Q: Can I use the NCB-700 for radiant floor heating?**
A: Yes — the NCB-700 is commonly used with radiant floor systems. It requires a mixing valve to bring supply temperatures down to radiant-appropriate levels (typically 80–120°F). The unit itself can supply up to 180°F.

**Q: What is the NCB-700's minimum water pressure requirement?**
A: The system requires a minimum of 7.25 PSI (0.5 bar) on the heating circuit side. Below this, the low water pressure sensor may trigger and prevent operation.

## See Also

- [Navien Error Code E021 — Cold Water Inlet Thermistor Fault Fix](/posts/navien-error-code-e021/)
- [Navien NPE-A 016 — Overheat Lockout Fix](/posts/navien-water-heater-error-code-016/)
- [Navien E006 Error Code — Causes & Fix](/posts/navien-error-code-e006/)
- [Navien E030 Error Code — Causes & Fix](/posts/navien-error-code-e030/)
