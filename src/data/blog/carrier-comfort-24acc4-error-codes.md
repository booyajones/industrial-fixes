---
title: "Carrier Comfort 24ACC4 AC Error Codes - Full Flash Code Guide"
description: "Complete flash code guide for the Carrier Comfort 24ACC4 central air conditioner. Diagnose capacitor, compressor, fan motor, and pressure faults using the LED blink sequence."
pubDatetime: 2026-04-25T00:00:00Z
author: "Marcus Webb"
tags:
  - hvac
  - error-codes
---

The Carrier Comfort 24ACC4 is a single-stage central air conditioner in Carrier's Comfort (entry-level) lineup. Unlike Carrier's communicating Infinity systems, the 24ACC4 uses a conventional LED flash code system on its control board to communicate faults. Reading the flash code is the fastest way to narrow down what's wrong — and for many faults, the fix is a straightforward DIY repair.

## What Do 24ACC4 Flash Codes Mean?

The 24ACC4 outdoor unit has a green status LED on the control board, visible through the service access panel. The LED flashes in distinct patterns: the number of flashes, the pause between groups, and whether the light is solid or blinking all carry diagnostic meaning.

**To read the flash code:**
1. Shut off the thermostat.
2. Open the service panel (the small access door on the side of the outdoor unit — not the main panel).
3. Count the flashes, pause, repeat. The pattern repeats continuously.

**Carrier 24ACC4 LED Flash Code Table:**

| Flash Pattern | Meaning |
|---------------|---------|
| Solid green | Normal operation |
| 2 flashes | High pressure fault |
| 3 flashes | Low pressure fault |
| 4 flashes | Open start capacitor / compressor not starting |
| 5 flashes | Outdoor fan motor fault |
| 6 flashes | Compressor trip / thermal overload |
| 7 flashes | Low voltage to control board |
| 8 flashes | Communication fault (if paired with a communicating thermostat) |
| Rapid continuous blink | Control board fault / board needs replacement |
| No LED | No power to control board |

## How to Fix It

**1. 2 Flashes — High Pressure Fault**

The high-pressure switch tripped, protecting the compressor from damaging over-pressure conditions. Causes and fixes:

- **Dirty outdoor coil:** This is the #1 cause. Use a garden hose to gently rinse the coil fins from the inside out (remove the top panel to spray outward). Never use a pressure washer — it bends the fins.
- **Blocked outdoor unit:** Vegetation, debris, or structures too close to the unit restrict airflow. Maintain at least 18 inches of clearance on all sides.
- **Outdoor fan not running:** See 5-flash code below. If the fan isn't moving air, high pressure builds rapidly.
- **Overcharge:** If the system was recently recharged, excess refrigerant causes high head pressure. Measure subcooling; it should be 10–15°F for R-22 or R-410A systems.
- **Reset:** After clearing the root cause, restore power and let the system run. The high-pressure switch auto-resets on the 24ACC4 once pressure drops.

**2. 3 Flashes — Low Pressure Fault**

The low-pressure switch tripped, indicating insufficient refrigerant pressure on the suction side. Causes:

- **Low refrigerant charge:** The most common cause. Refrigerant leaks over time, especially at the Schrader valve cores and flare connections. This requires EPA 608-certified work to add refrigerant — do not attempt yourself.
- **Dirty air filter / blocked return air:** Restricted indoor airflow freezes the evaporator coil, dropping suction pressure. Check and replace the filter first.
- **Frozen indoor coil:** If the coil is frozen, turn the thermostat to fan-only mode for 2 hours to defrost before re-diagnosing.
- **Failed indoor TXV or piston:** A stuck-closed expansion device starves the compressor of refrigerant.

**3. 4 Flashes — Start Capacitor / Compressor Not Starting**

The compressor attempted to start but failed to reach running speed. Almost always a capacitor problem:

- **Dual run capacitor failure:** The 24ACC4 uses a dual run capacitor (shared by compressor and fan motor). Test with a capacitor meter — the compressor side should be within 5% of rated µF (usually 35–80 µF depending on model). A reading more than 10% low means replacement.
- **Hard start kit:** If the capacitor tests good but the compressor still struggles to start (especially in high heat), add a hard start kit. It provides an extra capacitance boost during startup.
- **Compressor winding failure:** If the capacitor is good, measure compressor winding resistance. All three readings should be within 1–2 ohms of each other. A reading near zero on any winding = shorted compressor.

**4. 5 Flashes — Outdoor Fan Motor Fault**

The outdoor fan motor failed to run or stalled. Diagnosis:

- With power OFF, spin the fan blade by hand. If it doesn't spin freely, the bearings are seized.
- Check the fan motor capacitor (part of the dual run cap). Test capacitance and replace if low.
- Apply power briefly and test: if the motor hums but doesn't spin, the capacitor is bad or the motor start winding is open.
- If the motor runs at reduced speed or runs hot to the touch, the motor is failing and needs replacement.

**5. 6 Flashes — Compressor Thermal Overload / Trip**

The compressor's internal thermal overload protector tripped due to overheating:

- Allow 30 minutes for the compressor to cool down and the overload to reset.
- Check for root causes: high discharge pressure (dirty coil), low refrigerant (low suction pressure), high ambient temperature without adequate clearance around the unit.
- If the compressor trips repeatedly within the first hour of operation, the compressor itself may be failing.
- Measure compressor amperage with a clamp meter. If amperage exceeds the nameplate RLA (Rated Load Amps) by more than 10–15%, the compressor is drawing excessive current.

**6. 7 Flashes — Low Voltage**

The control board is receiving less than 24V on the low-voltage circuit. Causes:

- **Low-voltage fuse blown:** Check the 3-amp or 5-amp fuse on the indoor air handler control board. A short-circuited thermostat wire or a shorted contactor coil blows this fuse. Replace the fuse and trace the short.
- **Transformer failure:** The indoor unit's transformer steps down line voltage to 24V. Measure at the transformer secondary terminals. If you read less than 24V, the transformer is failing.
- **Undersized transformer:** Zoning systems with multiple thermostats can overload the original transformer. Upgrade to a higher-VA transformer.

**7. No LED — No Power to Control Board**

- Check the outdoor unit's disconnect switch and circuit breaker.
- Verify the control fuse on the outdoor unit's board (typically a 3A fuse).
- Measure voltage at the contactor input terminals. If you read 240V but the board has no power, the board may have failed.

## Parts You May Need

| Part | Use | Amazon Link |
|------|-----|-------------|
| Dual Run Capacitor (35/5 µF or 45/5 µF, 370V) | Fix 4-flash or 5-flash fault | [View on Amazon](https://www.amazon.com/dp/B01M05L7B3?ascsubtag=ecf-carrier-comfort-24acc4-error-codes&tag=errorcodefixes-20) |
| Hard Start Kit (SPP5 or equivalent) | Help struggling compressor start | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-carrier-comfort-24acc4-error-codes&k=hard+start+kit+HVAC+compressor&tag=errorcodefixes-20) |
| Outdoor Fan Motor (1/4 HP, 825 RPM, 5-wire) | Replace seized or failed fan motor | [View on Amazon](https://www.amazon.com/dp/B0D2L5NSMM?ascsubtag=ecf-carrier-comfort-24acc4-error-codes&tag=errorcodefixes-20) |
| Digital Capacitor Meter | Test run capacitors accurately | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-carrier-comfort-24acc4-error-codes&k=digital+capacitor+meter+HVAC&tag=errorcodefixes-20) |
| AC Contactor 2-Pole 30A 24V Coil | Replace pitted or worn contactor | [View on Amazon](https://www.amazon.com/dp/B0CJFZQVPT?ascsubtag=ecf-carrier-comfort-24acc4-error-codes&tag=errorcodefixes-20) |

## When to Call a Pro

- **3 flashes (low pressure):** Refrigerant work requires EPA 608 certification. Never attempt to add refrigerant yourself.
- **4 flashes with good capacitor:** Compressor diagnosis and replacement is a major repair — a failed compressor often warrants full system replacement given the 24ACC4's age and R-22 refrigerant costs.
- **6 flashes that won't clear:** Compressor mechanical failure is serious and requires professional evaluation.
- **Any electrical fault** where you're not confident testing 240V circuits: hire a licensed technician.

## FAQ

**Q: My 24ACC4 flashes 4 times but the capacitor tested fine. What's next?**

A: First, try a hard start kit — even a slightly weakened capacitor can cause start failures in high heat. If a hard start kit doesn't help, check compressor winding resistance with an ohmmeter (power off, disconnect wires). If windings test good, check supply voltage under load — low voltage causes high current and prevents startup. If all that checks out, the compressor contactor may have pitted contacts creating voltage drop at the compressor terminals.

**Q: How do I know if my 24ACC4 uses R-22 or R-410A?**

A: Check the nameplate on the outdoor unit — it lists the refrigerant type under "Refrigerant" or "Charge." The 24ACC4 model line spans several years; older units use R-22, while units manufactured after approximately 2010 use R-410A. You can also look at the service port size: R-410A ports are larger than R-22 ports.

**Q: The green LED is solid but the system isn't cooling. What does that mean?**

A: A solid green LED means the control board sees no faults. If the system is running (you can hear the compressor and fans) but not cooling, the most likely culprits are low refrigerant charge, a dirty evaporator coil, or a failed capacitor that's allowing weak compressor operation without tripping a fault. Check your filter and outdoor coil first, then have a tech check the refrigerant charge.

**Q: What size capacitor does the Carrier 24ACC4 use?**

A: Capacitor specs vary by unit tonnage and age. The dual run capacitor values are printed on the capacitor itself and on the unit's wiring diagram inside the service panel. Common values for the 24ACC4 are 35+5 µF or 45+5 µF at 370V or 440V. Always replace with the exact rated value — never substitute a lower µF capacitor.

## See Also

- [Carrier VRF System Error Codes Guide](/posts/carrier-vrf-error-codes/)
- [Carrier 25 Error Code — Causes & Fix](/posts/carrier-25-error-code/)
- [Carrier AquaSnap Chiller Fault Codes — 30RB/30RQ Guide](/posts/carrier-aquasnap-fault-codes/)
- [Carrier Error Code 19 - Causes & Fix](/posts/carrier-error-code-19/)
