---
title: "Trane ComfortLink II Communicating Thermostat Fault Codes - What They Mean and How to Fix Them"
description: "Trane ComfortLink II fault codes tell you exactly what's wrong with your communicating HVAC system — this guide covers the most common communication faults, their causes, and step-by-step fixes."
pubDatetime: 2026-04-25T00:00:00Z
tags: [hvac, error-codes, trane, comfortlink]
---

## What Does a Trane ComfortLink II Fault Code Mean?

The Trane ComfortLink II is a communicating thermostat and control platform. Unlike older thermostats that just send a "call for cooling" signal, ComfortLink II runs a two-way digital conversation with your air handler or furnace and outdoor unit — sharing data like operating pressures, temperatures, motor speeds, and fault conditions.

When something breaks down in that conversation, or when a system component reports a problem, a fault code appears on the ComfortLink II display. These codes are organized by source: thermostat, indoor unit, outdoor unit, or the communication link between them.

Trane and American Standard use the same underlying communicating platform (both are Trane Technologies products), so fault codes and repair procedures are largely identical between the two brands.

---

## Key ComfortLink II Communication Fault Codes

### Communication Loss Faults

**Code 79 — Thermostat Lost Communication with Indoor Unit**
The ComfortLink II thermostat can't reach the air handler or furnace on the communication bus. Start by checking the 4-wire cable between the thermostat and air handler. Inspect terminal connections at the thermostat sub-base and air handler control board. A blown fuse on the air handler board also causes this — check the 3A fuse.

**Code 80 — Indoor Unit Lost Communication with Outdoor Unit**
The air handler lost its data link to the outdoor condensing unit. Inspect the communication cable between indoor and outdoor units. On communicating Trane systems, this is a separate data conductor alongside the standard power wiring. Check both terminal blocks — indoor board and outdoor board — for loose connections or corrosion.

**Code 81 — Multiple Communication Device Losses**
The system can't reach two or more communicating components simultaneously. This often points to a failed system control board or a bus-level wiring fault. Check the 24V transformer — if transformer output has dropped, the entire communication bus can fail.

**Code 172 — Outdoor Control Board Not Responding**
The outdoor unit's control board is not answering on the communication bus. Check power to the outdoor unit, verify the disconnect is on, and inspect the outdoor board fuse. If the board has power and the fuse is good, the board itself may have failed.

**Code 173 — Indoor Control Board Not Responding**
Same as 172 but for the indoor air handler control board. Verify power, check fuses, inspect wiring.

### System Operation Faults

**Code 107 — High-Pressure Lockout**
The high-pressure switch opened, shutting down the compressor. Causes: dirty condenser coil, blocked airflow around the outdoor unit, outdoor fan motor failure, or refrigerant-side issues. Clean the condenser coil first — this fixes the majority of high-pressure lockout calls in summer.

**Code 108 — Low-Pressure Lockout**
Low-pressure switch opened. Most common cause is low refrigerant (a leak), but also possible during very cold weather. Requires refrigerant pressure testing — EPA 608 certification required.

**Code 126 — Outdoor Fan Fault**
The outdoor fan motor is not operating as expected. Could be a failed motor, a failed capacitor, or a control board not sending the correct signal. Check capacitor first — it's the most common outdoor fan failure.

**Code 165 — Defrost Fault**
On heat pump systems, the defrost cycle failed to complete properly. Causes: failed defrost control board, failed defrost thermostat/sensor, or a refrigerant charge issue.

**Code 268 — Thermistor Fault (Outdoor)**
An outdoor temperature sensor is reading out of range or has an open/shorted circuit. Disconnect and test the thermistor resistance with a multimeter — compare to the resistance-temperature table in your service manual.

**Code 534 — Variable Speed Motor Fault**
The ECM (electronically commutated motor) in the air handler reported a fault. ECM faults can be transient (clear on power cycle) or permanent (motor failure). If the code returns after clearing and restoring power, the motor or its module needs replacement.

---

## How to Fix ComfortLink II Communication Faults

1. **Pull the full fault history first.** On the ComfortLink II XL950 or XL850, navigate to: **Menu → Diagnostics → Equipment Faults**. Record every code. The history helps identify whether this is an isolated event or a recurring pattern.

2. **Power cycle the system.** Turn off the thermostat, kill the air handler breaker, kill the outdoor unit disconnect. Wait 30 seconds. Restore power: outdoor unit first, then air handler, then thermostat. Communication faults sometimes clear after a full power cycle when caused by a brown-out or power surge.

3. **Check the communication cable connections.** ComfortLink II uses a 4-wire bus: R (24V hot), C (common), Y/Y2 (call signals), and a communication data wire. At every connection point — thermostat sub-base, air handler terminal board, outdoor unit terminal board — check that every screw is tight and no wire is partially pulled out. Re-seat any suspicious connections.

4. **Inspect the 24V transformer.** Measure voltage between R and C at the air handler terminal board. It should read 24–28V AC. Lower voltage means a failing transformer or an overloaded control circuit. A shorted wire can drag down transformer voltage and cause system-wide communication failures.

5. **Check control board fuses.** The air handler and outdoor control boards both have fuses protecting the control circuit — typically 3A slow-blow fuses. A blown fuse looks like a communication failure from the thermostat. Replace any blown fuse and identify what caused it before assuming the board failed.

6. **Test wire continuity.** Use a multimeter to test every conductor in the communication cable from end to end. An open circuit on the communication data wire kills the digital link while leaving the 24V power circuit intact — the thermostat has power but can't talk to the equipment.

7. **For refrigerant faults (107, 108):** Stop here and call a tech. Don't attempt to recharge or diagnose refrigerant pressure without proper training and certification.

---

## Parts You May Need

| Part | Why | Approx. Cost |
|------|-----|-------------|
| [ComfortLink II XL950 thermostat](https://www.amazon.com/s?ascsubtag=ecf-trane-communicating-thermostat-fault-codes&k=ComfortLink+II+XL950+thermostat&tag=errorcodefixes-20) | Thermostat control failure | $250–$450 |
| [Trane air handler control board (model-specific)](https://www.amazon.com/dp/B0CNZGZ1HS?ascsubtag=ecf-trane-communicating-thermostat-fault-codes&tag=errorcodefixes-20) | Indoor board not responding — code 173 | $150–$350 |
| [Trane outdoor control board (model-specific)](https://www.amazon.com/dp/B0CNZGZ1HS?ascsubtag=ecf-trane-communicating-thermostat-fault-codes&tag=errorcodefixes-20) | Outdoor board failure — code 172 | $250–$500 |
| [24V transformer (40VA)](https://www.amazon.com/s?ascsubtag=ecf-trane-communicating-thermostat-fault-codes&k=24V+transformer+%2840VA%29&tag=errorcodefixes-20) | Weak or failed transformer causing bus voltage drop | $30–$60 |
| [3A slow-blow glass fuse](https://www.amazon.com/s?ascsubtag=ecf-trane-communicating-thermostat-fault-codes&k=3A+slow-blow+glass+fuse&tag=errorcodefixes-20) | Blown board fuse | $5–$10 |
| [18 AWG 4-conductor wire](https://www.amazon.com/s?ascsubtag=ecf-trane-communicating-thermostat-fault-codes&k=18+AWG+4-conductor+wire&tag=errorcodefixes-20) | Replace communication cable run | $0.30–$0.60/ft |
| [Outdoor thermistor sensor](https://www.amazon.com/s?ascsubtag=ecf-trane-communicating-thermostat-fault-codes&k=Outdoor+thermistor+sensor&tag=errorcodefixes-20) | Code 268 — thermistor fault | $20–$60 |
| [Condenser fan capacitor](https://www.amazon.com/s?ascsubtag=ecf-trane-communicating-thermostat-fault-codes&k=Condenser+fan+capacitor&tag=errorcodefixes-20) | Code 126 — fan fault (check cap first) | $15–$35 |

Trane parts are available through Trane parts distributors, Johnstone Supply, and HVAC distributors. For control boards, always match to your specific model — the model number is on the data plate inside the air handler or on the outdoor unit. Common air handler board part numbers include **CNT05713** and **X13511576010** depending on model generation.

---

## When to Call a Pro

- **Any refrigerant fault (107, 108, 165 when charge-related):** Requires EPA 608 certification.
- **Code 534 (ECM motor fault):** ECM motor diagnosis requires specific test procedures and the correct replacement module matched to your motor. A tech with ECM tools can read the motor fault memory directly.
- **Persistent code 81 after wiring checks:** A system-wide bus failure often requires a technician with a service laptop running Trane's ComfortLink diagnostic software to identify the exact failing device.
- **Control board replacement:** ComfortLink II replacement boards sometimes require commissioning steps — a tech familiar with the platform can complete this correctly.

---

## Frequently Asked Questions

**Q: What's the difference between ComfortLink and ComfortLink II?**

The original ComfortLink was a zoning and communicating control system from the early 2000s. ComfortLink II is the current platform, introduced around 2009 and refined since. The hardware and fault code systems are different. This guide covers ComfortLink II (XL850, XL950, and related equipment).

**Q: My ComfortLink II thermostat says "System Offline" — is that the same as a fault code?**

"System Offline" typically means the thermostat has lost communication with the indoor unit (similar to code 79). It's not a distinct fault code — it's the thermostat's way of displaying a communication failure. Start with the wiring inspection and power check procedures above.

**Q: Code 80 cleared itself overnight. Should I still investigate?**

Yes. A self-clearing fault code usually means a marginal connection or a component that's failing intermittently. The fact that it cleared doesn't mean the problem is gone. Log the date and time, and watch for recurrence. Intermittent fault 80 that only happens on cold mornings is almost always a loose terminal connection that tightens and loosens with thermal cycling.

**Q: Can I upgrade from an older Trane thermostat to a ComfortLink II XL950?**

If your air handler and outdoor unit are ComfortLink II compatible (XL and XV series equipment from approximately 2009 forward), yes. If your equipment is older and non-communicating, you can install the XL950 but it will operate in conventional mode without the communicating features. Check Trane's compatibility tool or your equipment model numbers before buying.

**Q: How do I find the fault history on the XL950 vs. the older XL850?**

On the **XL950**: tap the Menu icon → Equipment → Faults. On the **XL850**: press Menu → Diagnostics → Fault History. Both store up to 25 faults with timestamps. On the older Comfort Control II, you access faults by pressing and holding the fan icon for 5 seconds.

## Related Articles

- [Trane 1 Flash Error Code — Causes & Fix](/posts/trane-1-flash-error-code/)
- [Trane Error Code 126 — Ignition Lockout Fix](/posts/trane-126-error-code/)
- [Trane 2 Flashes Error Code — Causes & Fix](/posts/trane-2-flashes-error-code/)
- [Trane 3 Flashes Error Code — Pressure Switch Fault Fix](/posts/trane-3-flashes-error-code/)
- [Trane 3 Flash Pressure Switch Fault — Detailed Diagnosis Guide](/posts/trane-3-flashes-pressure-switch/)
