---
title: "Rinnai RU130iN Tankless Water Heater Error Codes - Full Fault Guide"
description: "Complete error code reference for the Rinnai RU130iN condensing tankless water heater — the highest-capacity residential Rinnai unit. Covers all fault codes including Error 79 scale sensor, gas pressure faults, and advanced diagnostics."
pubDatetime: 2026-04-25T00:00:00Z
author: "James Rutherford"
tags:
  - hvac
  - error-codes
---

The Rinnai RU130iN is the highest-capacity residential condensing tankless water heater in the Rinnai lineup, producing up to 130,000 BTU/hr with a 0.96 Uniform Energy Factor. It's designed for high-demand households — large homes, large families, or applications that would overwhelm a standard tankless unit. Like all condensing gas heaters, the RU130iN has both a primary and a secondary heat exchanger, a condensate system, and a scale detection sensor — all of which add diagnostic complexity.

This guide decodes every Rinnai RU130iN error code and tells you how to fix each one.

## What Does the Rinnai RU130iN Error Code Mean?

Each code on the RU130iN identifies the safety system or component that stopped the unit from heating water normally. Some codes point to gas supply or ignition. Others point to scale buildup, fan speed, condensate management, or one of the thermistors that protect the condensing heat exchangers. Reading the code correctly helps you avoid blind resets that waste time and can damage the unit.

## How Rinnai Error Codes Work

The RU130iN displays two-digit error codes on the front panel controller. The controller also has a fault history function — press and hold the Up and Down buttons simultaneously (consult your specific model's manual for the exact key combination) to scroll through recent faults. Some codes are auto-resetting; others are hard lockouts that require pressing the On/Off button to reset.

If you have the Rinnai Control-R Wi-Fi module installed, faults also appear in the Rinnai Control-R app with more descriptive text.

---

## Rinnai RU130iN Error Codes

### Error 11 — No Ignition
The unit attempted to fire the burner but did not detect ignition within the trial period.

**Causes:**
- Gas shutoff valve closed
- Gas pressure too low (below 4" WC for natural gas, 8" WC for LP)
- Igniter electrode fouled or cracked
- Gas valve not opening
- Inlet water pressure insufficient to activate flow switch

**Fix:**
1. Confirm gas valve is open and supply pressure is adequate
2. Check that other gas appliances work — if not, you have a supply issue
3. Inspect the igniter electrode for carbon buildup or a cracked porcelain insulator
4. Check inlet water pressure — RU130iN requires minimum 10 PSI, recommended 30–80 PSI
5. Verify the flow sensor isn't stuck — minimum activation flow is 0.5 GPM

### Error 12 — Flame Failure During Operation
The unit ignited but the flame sensor lost signal mid-cycle.

**Causes:**
- Flame rod fouled with carbon
- Intermittent gas pressure drop during high-demand events
- Combustion air disruption

**Fix:** Clean or replace the flame rod. If Error 12 only occurs when other gas appliances run simultaneously, the gas supply line may be undersized — a licensed plumber or gas fitter needs to evaluate gas line sizing.

### Error 13 — Abnormal Combustion / Air-Fuel Ratio Fault
The combustion system detected abnormal conditions in the air-fuel mixture.

**Causes:**
- Air intake contaminated with recirculated exhaust
- Vent terminal orientation incorrect
- Combustion air fan underperforming
- Dirty burner assembly or secondary heat exchanger fouled with scale

**Fix:** Check vent terminations for proper installation — intake and exhaust must not be within 12" of each other on the same wall. Inspect intake screen for blockage.

### Error 14 — High-Limit Switch (Thermal Fuse) Tripped
The thermal protection device opened due to overtemperature in the heat exchanger.

**Causes:**
- Scale buildup restricting heat transfer (primary cause on the RU130iN after several years of hard water use)
- Combustion fan failure
- Blocked flue

**Fix:** The high-limit device on the RU130iN is a manual-reset type on some configurations. Check for a reset button on the heat exchanger area. Before resetting, identify the overtemperature cause — descale the unit if scale is suspected. If the thermal cutout is a fuse type (one-time), it must be replaced.

### Error 16 — Outlet Water Temperature Too High
The hot water outlet temperature exceeded the high-temperature safety threshold.

**Causes:**
- Very low water flow through the unit
- Setpoint above 140°F combined with low demand
- Outlet temperature sensor failure

**Fix:** Verify the unit has adequate flow. Reduce setpoint to 120°F for most residential applications. Check the outlet thermistor if low-flow causes have been ruled out.

### Error 25 — Bypass Servo Fault
The RU130iN uses an internal bypass servo valve to mix hot and cold water when necessary for temperature stability. Error 25 indicates this valve has failed or is operating out of spec.

**Fix:** The bypass servo is a motor-actuated valve inside the unit. Test for binding or physical failure. On the RU130iN, this is typically a service part — order by model number.

### Error 31 — Inlet Temperature Sensor Fault
The cold water inlet thermistor failed.

**Fix:** Locate, disconnect, and test the inlet thermistor resistance. At 68°F (20°C), the sensor should read approximately 10–15kΩ. Replace if out of spec. Inspect the connector for corrosion from condensate exposure.

### Error 32 — Outlet Temperature Sensor Fault
The hot water outlet thermistor failed.

**Fix:** Same procedure as Error 31, applied to the outlet thermistor.

### Error 33 — Secondary Heat Exchanger Sensor Fault
The thermistor monitoring the condensing secondary heat exchanger failed.

**What it means:** The secondary heat exchanger is the component that makes the RU130iN condensing — it extracts latent heat from flue gases. Its sensor is critical for managing the heat exchange process and protecting the component from overtemperature.

**Fix:** Test the secondary HX thermistor resistance. Also inspect the secondary heat exchanger for scale, corrosion, or damage from neglected condensate drain maintenance (see Error 79).

### Error 34 — Combustion Gas Temperature Too High
The flue gas leaving the primary heat exchanger is too hot, indicating poor heat transfer — almost always due to scale buildup.

**Fix:** Descale the primary heat exchanger immediately. If not addressed, this leads to Error 14 (thermal fuse) and potential heat exchanger failure.

### Error 41 — Combustion Fan Fault
The combustion air/exhaust fan failed to reach required speed, or the RPM sensor (Hall effect sensor) is not reading correctly.

**Causes:**
- Fan motor bearing failure
- Fan blade physically blocked
- Hall effect tachometer failure
- Control board fan output failure

**Fix:** Check the fan for free rotation. Listen for bearing noise on startup. Test the tachometer signal — with the fan spinning, there should be a pulsing DC signal from the Hall effect sensor. A flat DC signal indicates tachometer failure.

### Error 52 — Gas Valve Abnormality
The gas valve circuit reported an abnormal condition.

**Fix:** Test solenoid coil resistance and supply voltage. On the RU130iN, the gas valve uses two solenoids — test each coil individually. Replace the valve if coils show open resistance.

### Error 61 — Burner Combustion Fan (Persistent Fault)
A persistent or unrecoverable fan fault after multiple restart attempts.

**Fix:** Fan motor replacement.

### Error 65 — Water Flow Sensor Fault
The flow sensor turbine failed or is producing an invalid signal.

**Fix:** Clean the turbine housing — mineral deposits from hard water commonly foul the turbine and cause erratic flow readings. If cleaning doesn't restore function, replace the flow sensor.

### Error 70 — Control PCB Fault
The main control board detected an internal fault.

**Fix:** Check all wiring harness connections. Power cycle. If the fault persists, the control board needs replacement. The RU130iN's main PCB is available as a service part — verify the part number matches your specific model year.

### Error 79 — Scale Buildup Detected (Scale Sensor Alert)
This is one of the most important fault codes on the Rinnai RU130iN. Rinnai's Circ-Logic scale detection system monitors the secondary heat exchanger for mineral scale accumulation. Error 79 is the alert that scale has reached a level requiring service.

**Why this matters:** The condensing secondary heat exchanger on the RU130iN is an expensive and critical component. Scale buildup acts as insulation, causing:
- Reduced efficiency (you're paying more for the same hot water)
- Overtemperature in the heat exchanger (leading to Error 14 or Error 34)
- Accelerated corrosion of heat exchanger walls
- Premature heat exchanger failure (replacement cost: $400–$900 in parts)

**How to fix Error 79:**

1. **Perform a complete descaling flush.** Use the service ports on the inlet and outlet lines. Circulate a descaling solution (white vinegar is acceptable; Rinnai-approved descaler works better on stubborn scale) through the unit for 45–60 minutes.

2. **Reset the scale detection system.** After descaling, the scale sensor counter needs to be reset — refer to the service manual for the specific reset procedure on the RU130iN (typically involves holding specific button combinations on the controller).

3. **Check condensate drain.** If the condensate drain was partially blocked before Error 79, the secondary heat exchanger may have had standing acidic water — inspect for corrosion.

4. **Implement a maintenance schedule.** Annual descaling is mandatory in hard water areas. Consider a whole-house water softener or an inline scale inhibitor if water hardness exceeds 120 mg/L.

### Error 90 — Communication Fault (External Devices)
Communication lost with an external device — a cascade controller, Control-R Wi-Fi module, or other accessory.

**Fix:** Check wiring connections to external modules. Restart the external device. If using Control-R, verify the module's power supply.

---

## How to Fix It

1. **Check gas supply first** for ignition faults — confirm gas valve position and pressure at the unit.
2. **Flush for scale** whenever Error 79, 34, or 14 appears — don't ignore scale warnings.
3. **Inspect condensate drain** monthly in hard water areas — blocked condensate is the RU130iN's most destructive maintenance failure.
4. **Test sensors before boards** — thermistors for Errors 31, 32, 33 are cheap and fail frequently.
5. **Check the combustion fan** on Error 41 before ordering a control board — bearing failure is much more common than board failure.
6. **Pull fault history** before resetting — the timestamp log helps identify patterns on intermittent faults.

---

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|-------------|
| [Rinnai Tankless Descaler Flush Kit](https://www.amazon.com/s?ascsubtag=ecf-rinnai-ru130in-error-codes&k=Rinnai+tankless+water+heater+descaler+flush+kit&tag=errorcodefixes-20) | Error 79 fix — required scale maintenance; protects secondary HX | $25–$60 |
| [Condensate Neutralizer Replacement Media](https://www.amazon.com/s?ascsubtag=ecf-rinnai-ru130in-error-codes&k=condensate+neutralizer+media+replacement+tankless&tag=errorcodefixes-20) | Annual condensate maintenance on condensing units | $15–$35 |
| [Gas Water Heater Flame Rod](https://www.amazon.com/s?ascsubtag=ecf-rinnai-ru130in-error-codes&k=gas+water+heater+igniter+flame+rod+sensor&tag=errorcodefixes-20) | Error 12 fix — ionization sensor replacement | $15–$45 |
| [NTC Thermistor 10K Water Heater Sensor](https://www.amazon.com/s?ascsubtag=ecf-rinnai-ru130in-error-codes&k=NTC+thermistor+sensor+tankless+water+heater&tag=errorcodefixes-20) | Errors 31/32/33 — temperature sensor replacement | $12–$30 |
| [Tankless Water Heater Flow Sensor Turbine](https://www.amazon.com/s?ascsubtag=ecf-rinnai-ru130in-error-codes&k=tankless+water+heater+flow+sensor+turbine+replacement&tag=errorcodefixes-20) | Error 65 fix — flow sensor turbine replacement | $20–$55 |

---

## When to Call a Pro

Call a licensed plumber or HVAC technician for:

- **Error 79 that persists after descaling** — the scale sensor or secondary heat exchanger may require professional service
- **Error 52 (gas valve)** — gas system work requires licensed tradespeople
- **Error 14 with recurring thermal fuse failure** — the root cause (scale, fan) needs professional diagnosis
- **Error 41 (fan) where motor replacement doesn't clear the fault** — the control board output may be failed
- **Any scenario where flue gas or condensate appears to be leaking** — safety emergency; shut down the unit and call immediately
- **Cascade installation faults** — multi-unit cascade systems require manufacturer-trained technicians for proper commissioning

---

## Frequently Asked Questions

**Q: What does Error 79 really mean on the Rinnai RU130iN?**

A: Error 79 is Rinnai's scale detection alert. The RU130iN monitors the secondary (condensing) heat exchanger for scale accumulation using a dedicated scale sensor. When detected scale reaches a maintenance threshold, Error 79 fires. It's a maintenance reminder, not a catastrophic failure — but ignoring it leads to catastrophic failure. Flush the unit immediately and implement annual maintenance.

**Q: How is the RU130iN different from the RU98iN or RU80iN?**

A: The RU130iN is Rinnai's highest residential BTU condensing unit at 130,000 BTU/hr. The RU98iN produces 98,000 BTU/hr and the RU80iN produces 80,000 BTU/hr. All use the same error code system and condensing platform — this guide applies to all three. The main practical difference for homeowners is hot water capacity (GPM output) and the circuit breaker size for the combustion fan and controls.

**Q: My RU130iN shows Error 11 but I can see the pilot igniting. Is the sensor bad?**

A: If you can see sparking during ignition but the burner doesn't stay lit, the issue is likely the gas valve not opening fully (check gas pressure) or the flame rod not detecting the flame (carbon fouling). If the burner does light but Error 11 still appears, the flame rod may be reading intermittently — the rod position may have shifted out of the flame path. This is also common after someone services the unit and doesn't correctly reseat the ignition assembly.

**Q: Can I use the RU130iN with a recirculation system?**

A: Yes — the RU130iN is compatible with dedicated return-line recirculation using the Rinnai RECiRC pump or an external pump. The Circ-Logic feature can be programmed for scheduled or demand-triggered recirculation. Using recirculation increases scale accumulation rate — consider bi-annual descaling if the unit runs recirculation frequently.

## See Also

- [Rinnai Error Code 33 — Causes & Fix](/posts/rinnai-error-code-33/)
- [Rinnai Error Code 11 — No Ignition Fix](/posts/rinnai-error-code-11/)
- [Rinnai Error Code 25 — Causes & Fix](/posts/rinnai-error-code-25/)
- [Rinnai I120CN Tankless Water Heater Error Codes: Complete Guide](/posts/rinnai-i120cn-error-codes/)
