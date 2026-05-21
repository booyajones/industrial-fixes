---
title: "Heatcraft Beacon II E1 Error Code — Sensor Fault Fix"
description: "Heatcraft Beacon II E1 means the controller can't read one of its connected temperature sensors — open, shorted, or wildly out of range. It's almost always..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Marcus Webb"
slug: heatcraft-beacon-ii-error-code
featured: false
draft: false
tags:
  - heatcraft
  - commercial-refrigeration
  - refrigeration
  - temperature-sensor-fault
  - troubleshooting
---
## Quick answer

Heatcraft Beacon II E1 means the controller can't read one of its connected temperature sensors — open, shorted, or wildly out of range. It's almost always the air or coil sensor probe itself (about 70% of my calls), a chafed sensor lead, or a disconnected sensor at the controller terminal. Verify with a meter at the sensor before ordering a controller.

## What Beacon II E1 means

The Heatcraft Beacon II is the OEM electronic refrigeration controller installed on most Heatcraft walk-in cooler and freezer evaporator units shipped since approximately 2007 (replacing the original Beacon I). It manages defrost timing, fan operation, EEV control on capable units, alarm output, and basic refrigeration logic. The Beacon II reads multiple temperature sensors depending on the configured application:

- **Air sensor (T1)** — measures return air temperature, typically used as the control variable for cooler/freezer setpoint.
- **Coil sensor (T2)** — measures evaporator coil temperature, used for defrost termination and frost protection.
- **Discharge sensor (T3)** — on some installations, monitors compressor discharge for high-temp alarm.
- **Auxiliary sensor (T4)** — optional, used for product temperature monitoring or other application-specific input.

All Heatcraft Beacon II sensors are 10 kΩ NTC thermistors at 25 °C (77 °F). When the Beacon II reads any sensor input below the expected resistance range (short circuit, typically below 100 Ω indicated) or above the expected range (open circuit, infinite resistance), it displays "E1" and a sub-code identifying which sensor faulted: E1.1 for T1, E1.2 for T2, etc.

E1 is a hard fault on the Beacon II. The controller continues to display the temperature it was reading just before the fault, but it stops executing defrost cycles and may default to a fixed compressor on/off pattern depending on which sensor failed. On a freezer application, sustained E1 on the coil sensor can result in a frosted-up evaporator that eventually loses cooling capacity entirely.

E1 is the most common Beacon II fault by a significant margin — sensors live in a high-moisture, high-temperature-cycling environment and lead-to-body solder joints fail over time.

## Common causes (ranked by frequency)

1. **Failed air or coil sensor element** — most common. Lead-to-thermistor body joint corrodes from condensate exposure. Reads open on a meter.
2. **Chafed sensor lead** — usually at the strain relief where the sensor harness exits the evaporator housing.
3. **Disconnected sensor at controller terminal** — vibration or recent service work, sensor plug not fully seated.
4. **Wrong sensor type installed** — generic 10 kΩ NTC with different Beta value will read out of range to Beacon II firmware.
5. **Failed controller input** — water damage on the Beacon II board from condensate dripping onto the housing. Rare but real.
6. **Pinched or crushed sensor cable** — typically by ceiling tile work, electrical conduit installation, or rack systems.
7. **Loose terminal screw at the controller** — sensor wire backs out under vibration, intermittent E1.

## Step-by-step fix

1. **Read the sub-code carefully.** The Beacon II display will show "E1.X" where X is 1, 2, 3, or 4 indicating which sensor faulted. T1 air, T2 coil, T3 discharge, T4 aux. This tells you which sensor to investigate first.

2. **Note the controller part number and connections.** Heatcraft Beacon II controllers commonly carry part numbers in the 28907901 family (varies by feature configuration — some models include EEV control, some don't). Note which terminals on the controller have wires landing on them — typically T1 lands on terminals 1-2 of the sensor block, T2 on 3-4, etc. Reference the wiring diagram glued inside the evaporator electrical panel.

3. **Disconnect the suspect sensor at the controller and ohm it cold.** With the box at near-setpoint, pull the sensor leads at the controller terminal block. Measure resistance between the two leads. A healthy 10 kΩ NTC sensor at 35 °F (cooler air or coil) should read approximately 28-30 kΩ. At 0 °F (freezer coil) it should read about 85-90 kΩ. At 77 °F (room temp, if you've pulled it for testing) about 10 kΩ.

   Reference table for Heatcraft 10 kΩ NTC sensors (Beta 3977):
   - 100 °F (38 °C): ~6 kΩ
   - 77 °F (25 °C): ~10 kΩ
   - 50 °F (10 °C): ~20 kΩ
   - 35 °F (2 °C): ~28 kΩ
   - 32 °F (0 °C): ~33 kΩ
   - 0 °F (-18 °C): ~85 kΩ
   - -10 °F (-23 °C): ~115 kΩ

   OL (open) or near-zero (short) means the sensor element or lead is failed.

4. **Pull the sensor and inspect the lead routing.** Locate the sensor — air sensors are typically clipped near the evaporator inlet in the conditioned space, coil sensors are clipped to a coil return bend partway down the evap face. Follow the lead from the sensor body back to the controller. Look for: insulation worn through where the lead exits the evap housing, kinks where the lead is bent sharply around chassis edges, and condensate buildup at the sensor body.

5. **Replace the sensor with the OEM Heatcraft part.** Don't substitute a generic 10 kΩ NTC — Beta value matters. Heatcraft sells sensor replacement kits with the lead pre-attached and the correct connector for the Beacon II terminal block. Part numbers are in the 28907901 family and vary by length and application. The standard air/coil sensor kit is typically 28907901 (10-ft lead) or the longer-lead variant for ducted applications.

6. **Clip the new sensor to the original location.** For coil sensors, this is critical. The sensor must clip to a coil return bend, not just dangle in the air or sit against a fin. The Heatcraft service manual specifies the exact coil location for each evaporator model — usually the second or third return bend from the inlet side, on the discharge tube of that bend. Clipping the sensor to a different location will give the controller misleading information about defrost termination timing.

7. **Re-route the lead through proper strain reliefs and reconnect.** Use the existing strain reliefs and conduit clamps. If the original lead routing chafed through, add a piece of split loom or a rubber grommet at the chafe point. Reconnect at the controller, torque the terminal screws to about 4-5 in-lb (small terminals — easy to strip).

8. **Clear the E1 fault and verify operation.** Press the reset or clear-fault button on the Beacon II (varies by configuration — typically the down-arrow held for 3 seconds). The display should return to normal temperature reading. Verify by toggling between sensor displays (some Beacon II models let you cycle through T1, T2, T3 display via the up-arrow) that all sensors read sensible values.

> **Field knowledge nugget:** On Heatcraft walk-in freezers with Beacon II controllers installed since approximately 2015, I see a specific E1.2 (coil sensor) failure pattern related to defrost-water exposure. The coil sensor lead enters the evap housing through a grommet at the bottom, and during a defrost cycle, the meltwater that drips off the coil sometimes runs along the lead, into the grommet, and accumulates at the sensor body's heat-shrink boot. Over 2-3 years of cycling, the heat-shrink eventually wicks moisture inward and the sensor lead-to-body junction corrodes. The diagnostic tell: E1.2 occurs only after a defrost cycle, the unit appears to work fine between defrosts but logs the fault during or just after defrost terminate. Fix is replacement of the coil sensor with the OEM kit AND repositioning the lead so it routes *upward* from the sensor body for the first 4-6 inches before turning down toward the housing — this creates a moisture drip loop that prevents wicking. While you're in there, **apply dielectric grease to the new sensor's heat-shrink boot** to add a moisture barrier. The Beacon II sensor replacement kit (Heatcraft 28907901 series) includes a small dielectric grease packet for exactly this purpose. Use it.

**Safety:** Walk-in coolers and freezers create a unique safety hazard — **the door can latch shut behind a tech**. Always use a wedge or doorstop to hold the walk-in door open while servicing, and verify the interior safety release mechanism functions before entering. Heatcraft walk-ins are required to have an interior glow-in-the-dark safety release per OSHA 29 CFR 1910.36, but worn or painted-over releases sometimes fail. On freezer service calls in temperatures below 0 °F, limit work time to 15-20 minutes at a stretch and warm up between sessions — frostbite from contact with cold metal and from prolonged exposure is a real risk. Refrigeration service requires EPA 608 certification; opening sealed-system service ports requires Type II certification at minimum.

## Parts that may need replacement

| Part | OEM Number (typical) | Typical Cost | Where to Buy |
|---|---|---|---|
| Beacon II air/coil sensor kit (10 ft) | 28907901 | $85–$145 | [Parts Town](https://www.partstown.com?aff=PLACEHOLDER-PT) |
| Beacon II air/coil sensor kit (long lead) | 28907901-LL | $115–$185 | [Parts Town](https://www.partstown.com?aff=PLACEHOLDER-PT) |
| Beacon II controller (basic config) | 28907901-BASIC | $385–$585 | [Parts Town](https://www.partstown.com?aff=PLACEHOLDER-PT) |
| Beacon II controller (EEV config) | 28907901-EEV | $585–$785 | [Parts Town](https://www.partstown.com?aff=PLACEHOLDER-PT) |
| Sensor mounting clip kit | 28907901-CLIP | $15–$35 | [Parts Town](https://www.partstown.com?aff=PLACEHOLDER-PT) / [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| Dielectric grease, 1 oz tube | Permatex 22058 | $4–$10 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) / [Home Depot](https://www.homedepot.com?aff=PLACEHOLDER-HD) |

Always order the sensor with the mounting clip — Heatcraft clips don't reliably re-grip after being removed.

## When to call a professional

Call a CFESA-certified commercial refrigeration tech if:

- The controller itself appears damaged (water staining, scorch marks, swollen components). Beacon II replacements require config matching to the evaporator model and refrigeration application.
- E1 returns immediately after sensor replacement with verified-good OEM part. That points to a controller input failure.
- The walk-in is under Heatcraft warranty (typically 1 year parts, 5 year compressor) — authorized servicer required.
- You suspect refrigeration-side issues stacked with the E1 (uneven cooling, frost patterns out of normal, compressor short-cycling) — those need full system diagnosis.
- The walk-in is part of a multi-evaporator parallel rack system where the Beacon II is networked to a central controller. Network configuration on the central controller is its own discipline.

## FAQs

**How do I clear a Beacon II E1 code?**
Press and hold the down-arrow (or service reset button, varies by model) for 3 seconds with the fault on display. If the underlying cause is fixed, the fault clears and the controller returns to normal display. If the cause persists, E1 returns within minutes.

**Will Beacon II E1 stop the walk-in from cooling?**
Depends on which sensor faulted. E1.1 (air sensor) usually stops compressor operation since the controller can't measure setpoint. E1.2 (coil sensor) often allows continued cooling but stops defrost cycles, eventually leading to coil frost-up. Either way, fix it promptly.

**Can I use a generic 10 kΩ thermistor as a Beacon II replacement?**
Electrically maybe, practically no. Heatcraft uses sensors with Beta value 3977 and the Beacon II firmware lookup table assumes that curve. Generic sensors with different Beta values will read several degrees off and you'll see drift or nuisance faults. Use OEM.

**Where exactly does the coil sensor mount on a Heatcraft evaporator?**
On standard evaporator coils, the coil sensor clips to a return bend on the second or third pass from the inlet side, on the discharge tube of that bend (not the suction tube). The Heatcraft IOM (installation/operation manual) for the specific evap model has a diagram showing the exact location. Mounting on the wrong location messes up defrost termination timing.

**My walk-in is reading correctly but throws E1 anyway — what's wrong?**
Likely a chafed lead with an intermittent open. The sensor reads correctly most of the time but the controller's continuous ADC sampling catches the intermittent open and logs E1. Pull the lead and inspect along its entire length, especially at strain reliefs.

## Related guides

- [Copeland Discus Compressor Trip Codes Reference](/posts/copeland-discus-trip-code)
- [Kelvinator Walk-In Controller Fault Codes](/posts/kelvinator-walkin-error-code)
- [Manitowoc E03 Error Code — Probe / Thermistor Open Fix](/posts/manitowoc-e03-error-code)
