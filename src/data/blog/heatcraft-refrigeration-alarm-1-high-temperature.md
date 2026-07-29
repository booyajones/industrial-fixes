---
title: "Heatcraft Refrigeration Alarm 1 — High Temperature Fault Fix"
author: "Marcus Webb"
pubDatetime: 2024-03-15T08:00:00Z
modDatetime: 2024-03-15T08:00:00Z
slug: heatcraft-refrigeration-alarm-1-high-temperature
featured: false
draft: false
tags:
  - refrigeration
  - heatcraft
  - walk-in
  - commercial-refrigeration
description: "Heatcraft refrigeration Alarm 1 means high box temperature on Bohn, Larkin, and Climate Control walk-in unit controllers — here's how to diagnose and fix it."
---

## Error Code: Heatcraft Refrigeration Alarm 1

**What it means:** Alarm 1 on Heatcraft, Bohn, Larkin, and Climate Control walk-in refrigeration unit controllers indicates that the box temperature has risen above the high-temperature alarm setpoint. This is a critical alert — product in the walk-in is at risk and the alarm will not clear until the box temperature drops back within the programmed range.

Heatcraft's EC (Electronic Controller) series — including the Bohn BEC, Larkin LEC, and Climate Control CEC — all share the same alarm numbering convention. Alarm 1 is always high box temperature regardless of which brand badge is on the unit controller.

This alarm does not necessarily mean the refrigeration system has failed completely. In some cases the box is simply recovering from a long door-open event, a high product load, or a recent defrost cycle. But it can also signal a serious mechanical failure. Know the difference before you touch anything.

## Common Causes

- **Extended door open or high product load** — The most benign cause. A walk-in that's been loaded with warm product or had the door propped open will trigger Alarm 1 during recovery. Check the alarm timestamp against recent activity.
- **Evaporator fan motor failure** — One or more evaporator fans have stopped. The coil is cold but air isn't moving through the box. The coil may be frosted solid. Check each fan individually — on multi-fan units, one motor can fail while others continue, causing slow temperature rise.
- **Defrost heater or defrost control failure** — A defrost that didn't terminate correctly leaves the coil under a thick ice sheet that blocks airflow. The box temp climbs even though the compressor is running and the coil itself is attempting to cool.
- **Refrigerant leak or low charge** — Reduced refrigerant produces elevated suction superheat, high discharge temperature, and a box that slowly warms over hours or days. Check for oil spots on the lineset or oil accumulation at the coil.
- **Condenser coil fouled or condenser fan failed** — On remote condensing units, a dirty condenser or failed condenser fan causes high head pressure, compressor cycling on the high-pressure switch, and a box that can't pull down. The condenser is often overlooked during walk-in service calls.
- **Temperature sensor failure** — If the box temperature sensor (thermistor) has drifted or failed high, the controller reads a higher temperature than actual. The box may be fine. Check sensor resistance against the temperature/resistance curve in the service manual.

## Step-by-Step Fix {#step-by-step-fix}

1. **Check the actual box temperature independently.** Use a calibrated thermometer or temperature probe — do not trust the controller display until you've verified the sensor. If the box feels and measures cold (at or near setpoint), suspect a sensor fault rather than an actual high-temperature condition.

2. **Verify all evaporator fans are running.** Open the walk-in, stand near the evaporator unit, and confirm you can hear and feel airflow from all fan positions. On a failed fan, you'll feel significantly reduced airflow from that section of the coil. Inspect each fan blade — sometimes debris stops a blade while the motor hums, tripping thermal protection and shutting the motor down.

3. **Inspect the evaporator coil for ice blockage.** If the coil face is solid ice or frost is packed heavily between the fins, a defrost failure has occurred. A properly functioning defrost cycle should clear the coil fully. Manually initiate a defrost cycle via the controller (typically hold the defrost button 3–5 seconds) and observe whether the heaters energize and the ice begins to melt.

4. **Check the condenser unit.** Walk to the condensing unit (or remote condenser location). Confirm the condenser fan(s) are running. Look at the condenser coil face for debris, grease, or cottonwood seed accumulation that blocks airflow. A dirty condenser is extremely common in restaurant environments. Clean with coil cleaner and a fin comb if fouled.

5. **Measure suction and discharge pressure (requires refrigeration gauges).** Attach service manifold gauges to the service ports. Compare readings against the expected values for your refrigerant and box temperature. Low suction pressure + high superheat = low charge or restriction. High discharge pressure = condenser issue or overcharge.

6. **Check the temperature sensor resistance.** Disconnect the sensor wiring from the controller and measure resistance with a multimeter. Heatcraft EC controllers typically use a standard 10 kΩ NTC thermistor at 77°F (25°C). At a box temperature of 35°F, expect approximately 16–18 kΩ. An open circuit (OL) or a reading far outside the expected range indicates a failed sensor.

7. **Replace faulty components based on findings.** Evaporator fan motors are typically available as generic replacements matched by frame size, CFM, and voltage. Defrost heaters and termination thermostats are model-specific. Temperature sensors are often available as aftermarket replacements — verify connector type and thermistor curve before ordering.

8. **Clear the alarm after repair.** On Heatcraft EC controllers, press and hold the Alarm Reset button (or navigate to the alarm menu on LCD units) to clear Alarm 1 after the box temperature has returned to setpoint. Document the alarm with timestamp in your service log.

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Part Number | Typical Cost | Where to Buy |
|------|------------|-------------|-------------|
| Evaporator Fan Motor (typical) | Match by HP/frame/RPM | $45–$120 | [Search on Amazon](https://www.amazon.com/s?ascsubtag=ecf-heatcraft-refrigeration-alarm-1-high-temperature&k=Heatcraft+Evaporator+Fan+Motor+%28typical%29&tag=errorcodefixes-20) \| Parts Town / Grainger |
| NTC Temperature Sensor (10kΩ) | Model-specific | $20–$45 | [Search on Amazon](https://www.amazon.com/s?ascsubtag=ecf-heatcraft-refrigeration-alarm-1-high-temperature&k=Heatcraft+NTC+Temperature+Sensor+%2810k%CE%A9%29&tag=errorcodefixes-20) \| Parts Town / Heatcraft dealer |
| Defrost Termination Thermostat | Model-specific | $15–$35 | [Search on Amazon](https://www.amazon.com/s?ascsubtag=ecf-heatcraft-refrigeration-alarm-1-high-temperature&k=Heatcraft+Defrost+Termination+Thermostat&tag=errorcodefixes-20) \| Parts Town |
| Heatcraft EC Controller | Model-specific | $180–$350 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-heatcraft-refrigeration-alarm-1-high-temperature&k=Model-specific+Heatcraft+EC+Controller&tag=errorcodefixes-20) \| Heatcraft dealer |
## When to Call a Professional

Any diagnosis involving refrigerant — checking pressures, adding charge, finding and repairing leaks — requires EPA 608 certification and proper recovery equipment. Do not attempt to add refrigerant to a walk-in cooler without verifying the existing charge and finding the source of any leak. Repeatedly topping off a leaking system is expensive, environmentally irresponsible, and will eventually cause compressor failure from oil loss. A refrigeration technician should handle any system that won't pull down despite clean coils, running fans, and a good condenser — the root cause is almost always a refrigerant-side issue.

> **Pro tip:** Alarm 1 events that happen at the same time every day — especially in the early morning — are almost always defrost-related. Check whether your defrost schedule is set correctly for the actual conditions of your box. A walk-in with heavy frost buildup needs more frequent or longer defrost cycles. Most Heatcraft controllers allow you to increase defrost frequency directly from the controller menu without a service call.
