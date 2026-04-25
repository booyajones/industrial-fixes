---
title: "Carrier Infinity Touch Thermostat Error Codes - What It Means and How to Fix It"
description: "Full guide to Carrier Infinity Touch thermostat alert codes and system faults. Covers every common error number with diagnosis steps and what to check before calling a technician."
pubDatetime: 2026-04-25T00:00:00Z
author: errorcodefixes.com
tags:
  - hvac
  - error-codes
---

The Carrier Infinity Touch thermostat (model SYSTXCCITC01) is the control hub for the Infinity communicating system. When a component faults, the thermostat logs an alert code with a description right on the screen — no LED counting required. This guide walks through every common alert code, what it means, and how to resolve it.

## What Does Carrier Infinity Touch Thermostat Error Codes Mean?

Alert codes appear in the **Alerts** menu on the touchscreen. Navigate there by tapping **Menu → Alerts**. Each alert shows a code number, a short description, and the date/time it occurred. Some clear on their own once the condition resolves; others require manual clearing after you fix the underlying issue.

The Carrier Infinity system uses a communication bus called Infinity Control. Codes in the 100–199 range are typically indoor unit (air handler or furnace) faults. Codes in the 200–299 range usually indicate outdoor unit issues. Codes in the 300+ range are often communication or control-level faults.

### Alert 111 — Ignition Failure

The furnace attempted to light and failed after three tries. The control board locks out and displays this code. Common causes: no gas supply, failed hot surface igniter, dirty flame sensor, or faulty gas valve.

**Check first:** Is the gas supply valve at the furnace fully open? Did a gas company shut-off or meter issue occur? If gas is confirmed, see the igniter and flame sensor parts below.

### Alert 114 — Rollout Switch Open

A rollout limit switch tripped, which means flames were detected outside the heat exchanger — a serious safety condition. This requires an HVAC technician. Do not reset and keep running the system. The cause is typically a cracked heat exchanger, blocked flue, or improper combustion air.

### Alert 125 — High Limit Switch Open

The furnace overheated and the high limit switch opened to prevent damage. Most common cause: a clogged air filter restricting airflow. Replace the filter first, then reset the system. If the limit trips again, the heat exchanger may be cracked or the blower motor may be failing.

### Alert 126 — Inducer Pressure Switch Fault

The pressure switch monitoring the draft inducer motor is stuck open or stuck closed. The inducer motor may have failed, a hose connecting the pressure switch may be cracked or clogged with condensate, or the pressure switch itself has failed.

**Quick check:** With the furnace running, listen for the inducer motor to spin up before ignition. If you hear nothing, the inducer has likely failed.

### Alert 168 — Loss of Communication with Indoor Unit

The thermostat lost its data link to the indoor air handler or furnace. This is one of the most common Carrier Infinity alerts. See our dedicated [Carrier Infinity Error 168 article](/posts/carrier-infinity-error-168) for the full fix guide. Short version: check the 4-wire comm bus connections at both ends, check for a blown fuse on the indoor control board, and verify 24V power at the indoor unit.

### Alert 178 — Loss of Communication with Outdoor Unit

Same as 168 but for the outdoor unit. Check the 4-wire communication bus at the outdoor unit terminal strip. Also check that the outdoor unit disconnect is on and the unit has 240V power. Corroded terminals and rodent-chewed wiring are frequent culprits.

### Alert 179 — Communication Error (Multiple Components)

Both indoor and outdoor units show communication loss simultaneously. Usually indicates a problem with the control transformer (24V supply) or the thermostat itself rather than a specific component. Check fuses, verify 24V at the transformer secondary, and try powering the thermostat off for 30 seconds.

### Alert 200 — Outdoor Unit Fault (General)

Catch-all for outdoor unit issues that don't map to a specific numbered fault. Check the outdoor unit for obvious issues (ice buildup, tripped contactor, capacitor bulge) and examine the status LED on the outdoor unit control board.

### Alert 227 — Low Pressure Fault

Refrigerant pressure is too low on the suction side. The system likely has a refrigerant leak or a metering device problem. Requires a technician with gauges and EPA 608 certification.

### Alert 228 — High Pressure Fault

High-side pressure exceeded the cutoff. Common causes: dirty condenser coil, failed condenser fan motor, or refrigerant overcharge. Clean the outdoor coil and verify the fan is running before calling a technician.

### Alert 232 — Outdoor Temperature Sensor Fault

The outdoor ambient temperature sensor has failed or is reading out of range. The sensor is a 10K thermistor typically mounted on the outdoor unit's control board or base pan. Replacement is inexpensive.

### Alert 280 — Compressor Fault

The compressor protection circuit tripped. This could be an internal overload, a failed start capacitor, or a seized compressor. Check the run capacitor first (it's the most common and cheapest fix). If the capacitor tests good and the compressor still won't start, you need a technician.

## How to Fix It

1. **Read the full alert description on the screen.** The Infinity Touch shows more than just a number — the description often points directly at the faulty component.
2. **Check the basics.** Air filter, thermostat batteries (if applicable), and all power switches before diving into components.
3. **Navigate to Alerts → History.** This shows you the sequence of faults, which is often more informative than the current single alert.
4. **Reset the system.** For most alerts, navigate to **Menu → System Configuration → Reset System** or simply cycle the breaker for 30 seconds.
5. **Clear the alert after repair.** Once fixed, go to **Menu → Alerts → Clear All** to remove the logged fault.
6. **Update firmware.** Older Infinity Touch thermostats have firmware bugs that cause spurious communication errors. Check carrier.com for the current firmware version.
7. **Inspect the 4-wire bus.** For any communication fault (168, 178, 179), trace the 4-wire cable from the thermostat to each component. Look for loose connections, corroded pins, or damage.
8. **Replace components systematically.** Start with the cheapest and most accessible part (fuses, sensors) before moving to boards and compressors.

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|-------------|
| Hot surface igniter (HH18HA499) | Fixes Alert 111 — ignition failures | $20–$40 — [Search on Amazon](https://www.amazon.com/s?k=Carrier+hot+surface+igniter+HH18HA499&tag=errorcodefixes-20) |
| Flame sensor rod | Fixes Alert 111 when igniter is fine | $10–$20 — [Search on Amazon](https://www.amazon.com/s?k=furnace+flame+sensor+rod+Carrier&tag=errorcodefixes-20) |
| Draft inducer motor | Fixes Alert 126 when motor is dead | $80–$200 — [Search on Amazon](https://www.amazon.com/s?k=Carrier+inducer+motor+replacement&tag=errorcodefixes-20) |
| Pressure switch (vent/inducer) | Fixes Alert 126 when motor runs fine | $15–$35 — [Search on Amazon](https://www.amazon.com/s?k=Carrier+furnace+pressure+switch&tag=errorcodefixes-20) |
| Dual run capacitor (45/5 MFD) | Fixes Alert 280 compressor/fan issues | $15–$35 — [Search on Amazon](https://www.amazon.com/s?k=dual+run+capacitor+45+5+MFD+440V&tag=errorcodefixes-20) |
| Outdoor temperature sensor (10K NTC) | Fixes Alert 232 | $10–$25 — [Search on Amazon](https://www.amazon.com/s?k=10K+NTC+thermistor+HVAC+outdoor+sensor&tag=errorcodefixes-20) |

## When to Call a Pro

- **Alert 114 (Rollout Switch)** — Stop using the system immediately. A cracked heat exchanger can allow carbon monoxide into your living space. Call a technician today.
- **Alert 227 or 228** — Any refrigerant fault requires EPA 608 certification. Don't add refrigerant without finding and fixing the leak first.
- **Alert 280** — If the capacitor checks out and the compressor won't start, a failed compressor is a major repair. Get quotes for both repair and replacement.
- The thermostat screen is blank or unresponsive after checking power — the thermostat itself may have failed.
- You're seeing multiple different alert codes on the same day, which suggests a larger electrical or control system issue.

## Frequently Asked Questions

**Q: The Carrier Infinity Touch shows Alert 168 every few days but clears itself. Should I be worried?**

A: Intermittent communication errors that clear on their own often indicate a marginal connection — a wire that's barely making contact or a terminal that expands and contracts with temperature. It won't fix itself permanently. Pull and reseat every connector on the 4-wire bus and clean the terminals. If it keeps coming back, the indoor control board or the thermostat itself may be failing.

**Q: How do I clear all alerts on the Carrier Infinity Touch thermostat?**

A: Tap **Menu** on the home screen, then **Alerts**, then **Clear All** (bottom right). This clears the logged fault history but does not fix the underlying issue. If the cause isn't resolved, the alert will return.

**Q: My Infinity Touch shows the wrong outdoor temperature. Is this an alert issue?**

A: It could be Alert 232 (outdoor sensor fault), or simply a sensor that's shaded/exposed wrong. If the displayed temperature is wildly off (e.g., 200°F or -40°F), the sensor has failed. If it's off by 5–10 degrees, check whether the sensor is in direct sunlight or near a heat source.

**Q: Can I use a non-Carrier thermostat with the Infinity system?**

A: Not recommended. The Infinity system uses proprietary communication protocol. A standard 24V thermostat will technically operate the system in a basic mode (no variable speed, no alerts, no diagnostics), but you lose all the efficiency and diagnostic features. Third-party Infinity-compatible stats exist but require careful selection by model year.

**Q: The Infinity Touch is 10 years old. Should I replace the thermostat or the whole system?**

A: The thermostat itself is rarely the reason to replace a system. If the HVAC equipment is working but the thermostat screen has failed or it won't communicate, replacing the thermostat alone (around $200–$400 installed) is almost always the right call. Only consider a full system replacement if the equipment itself has major mechanical issues.

## Related Articles

- [Carrier 11 Error Code — Causes & Fix](/posts/carrier-11-error-code/)
- [Carrier 12 Error Code — Causes & Fix](/posts/carrier-12-error-code/)
- [Carrier 13 Error Code — Limit Switch Lockout Fix](/posts/carrier-13-error-code/)
- [Carrier 13 Soft Lockout — What's Different from Hard Lockout](/posts/carrier-13-soft-lockout/)
- [Carrier 14 Error Code — Causes & Fix](/posts/carrier-14-error-code/)
