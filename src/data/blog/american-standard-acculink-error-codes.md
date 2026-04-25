---
title: "American Standard AccuLink Error Codes - What They Mean and How to Fix Them"
description: "American Standard AccuLink communicating systems display fault codes on the thermostat when something goes wrong — this guide covers the most common codes, what each one means, and how to fix them."
pubDatetime: 2026-04-25T00:00:00Z
tags: [hvac, error-codes, american-standard, acculink]
---

## What Does the American Standard AccuLink System Do?

American Standard AccuLink is a communicating HVAC platform — the thermostat, air handler or furnace, and outdoor unit all talk to each other over a dedicated data bus. This communication allows precise system coordination, advanced diagnostics, and fault reporting directly on the thermostat display.

When something fails, the AccuLink Platinum 850 or 950 thermostat (or the older AccuLink Comfort Control) logs a fault code and often shuts down the affected function. The good news: these codes pinpoint the problem more precisely than older non-communicating systems, where you'd be guessing from symptom alone.

**Note:** American Standard AccuLink and Trane ComfortLink II are closely related platforms. American Standard and Trane are both Trane Technologies brands, and their communicating systems share substantial hardware and software architecture. Many fault codes and solutions apply to both.

---

## Most Common AccuLink Fault Codes

### 79 — Loss of Communication (Indoor Unit)
The thermostat lost communication with the air handler or furnace. Check the 4-wire communicating cable between the thermostat and indoor unit. Inspect all terminal connections for looseness or corrosion. Also check that the air handler control board hasn't lost power.

### 80 — Loss of Communication (Outdoor Unit)
The indoor unit lost communication with the outdoor condensing unit. Check the communication wire between indoor and outdoor unit. This is a 2-conductor data wire in addition to standard power wiring. Inspect terminal blocks at both ends.

### 81 — Loss of Communication (Multiple Devices)
Broader communication failure — the system can't see multiple components. Often caused by a failed system control board or a wiring fault that affects the entire communication bus.

### 107 — High-Pressure Lockout
The high-pressure safety switch tripped. Most common causes: dirty condenser coil, low refrigerant (counterintuitively, low charge causes high discharge pressure in some conditions), blocked airflow around the outdoor unit, or failed condenser fan motor. This is a refrigerant-side issue — requires a licensed HVAC technician to diagnose properly.

### 108 — Low-Pressure Lockout
The low-pressure safety switch tripped. Common causes: low refrigerant charge (leak), failed metering device, or extremely cold outdoor temperatures causing liquid refrigerant to back up. Refrigerant work requires EPA 608 certification.

### 172 — Outdoor Unit Communication Fault
The outdoor unit's control board is not responding on the communication bus. Could be a failed outdoor board, a wiring fault, or a blown fuse on the outdoor board. Check the fuse on the outdoor control board first — it's often a 3A or 5A glass fuse.

### 173 — Indoor Unit Communication Fault
Same as 172, but the indoor air handler's control board is the unresponsive device. Check power to the air handler and inspect the control board fuse.

### 178 — Indoor-to-Outdoor Communication Fault
(See also our Carrier Infinity 178 guide — this code is shared across Trane/American Standard.) Communication dropped between indoor and outdoor units. Trace the communication cable, check connections at both ends.

### 199 — System Control Fault
The system's main control board (often inside the air handler) has thrown an internal fault. This may require board replacement. Before replacing, verify input voltage to the board is correct and check all fuses.

### 268 — Outdoor Unit Thermistor Fault
A temperature sensor (thermistor) on the outdoor unit is reading out of range or has failed. The outdoor ambient thermistor or discharge line thermistor may be disconnected or failed. Check connector seating and test resistance with a multimeter.

---

## How to Fix AccuLink Faults

1. **Read and record the full fault history.** On the AccuLink thermostat, navigate to: **Menu → Diagnostics → Fault History**. Write down every fault code and the timestamp. Patterns tell you more than single codes.

2. **Clear the fault and test.** After recording, clear the fault list and let the system attempt a normal cycle. If the same code returns within minutes, the problem is active. If it doesn't return for hours, you may have a transient or intermittent issue.

3. **Check power at all units.** Confirm the air handler, outdoor unit, and thermostat all have proper power. Check breakers, disconnects, and fuses. A brown-out or momentary power drop can cause communication faults that clear on their own.

4. **Inspect all communication wiring.** AccuLink uses a 4-wire communicating setup: R (24V power), C (common), Y/Y2 (call signals), and a data/communication wire. Inspect every connection at the thermostat sub-base, air handler board, and outdoor unit board. Tighten any loose screws. Clean any oxidized terminals with electrical contact cleaner.

5. **Check control board fuses.** Most AccuLink control boards have a 3A or 5A fuse protecting the 24V control circuit. A blown fuse kills power to the board, which looks like a communication fault from the thermostat's perspective.

6. **Test communication wire continuity.** With a multimeter, test each wire in the communication cable from one end to the other. Any open wire needs to be repaired or the cable replaced.

7. **For refrigerant-related faults (107, 108):** Do not attempt to diagnose refrigerant pressure faults yourself. These require manifold gauges and EPA 608 certification. Call a technician.

---

## Parts You May Need

| Part | Why | Approx. Cost |
|------|-----|-------------|
| [AccuLink thermostat (Platinum 850 or 950)](https://www.amazon.com/s?k=AccuLink+thermostat+%28Platinum+850+or+950%29&tag=errorcodefixes-20) | Thermostat control board failure | $200–$400 |
| [Air handler control board (model-specific)](https://www.amazon.com/s?k=Air+handler+control+board+%28model-specific%29&tag=errorcodefixes-20) | Indoor board communication fault | $150–$350 |
| [Outdoor unit control board (model-specific)](https://www.amazon.com/s?k=Outdoor+unit+control+board+%28model-specific%29&tag=errorcodefixes-20) | Outdoor board failure — 172/80 faults | $250–$500 |
| [4-conductor 18 AWG thermostat wire](https://www.amazon.com/s?k=4-conductor+18+AWG+thermostat+wire&tag=errorcodefixes-20) | Replace damaged communication cable | $0.30–$0.60/ft |
| [3A glass fuse (5-pack)](https://www.amazon.com/s?k=3A+glass+fuse+%285-pack%29&tag=errorcodefixes-20) | Blown board fuse | $5–$10 |
| [Electrical contact cleaner](https://www.amazon.com/s?k=Electrical+contact+cleaner&tag=errorcodefixes-20) | Clean corroded terminals | $8–$15 |
| [Thermistor sensor (model-specific)](https://www.amazon.com/s?k=Thermistor+sensor+%28model-specific%29&tag=errorcodefixes-20) | Replace failed temperature sensor — 268 fault | $20–$60 |

For control boards, use your air handler or outdoor unit model number to find the exact part. American Standard parts are available through Johnstone Supply, Winsupply, and the Trane parts portal. Common indoor board part numbers include **CNT05713** and **CNT05524** for various XR and XV series air handlers — always verify against your specific model.

---

## When to Call a Pro

- **Any refrigerant fault (107, 108):** Refrigerant diagnosis and recharge requires EPA certification. Don't skip this step.
- **Persistent communication faults after wiring inspection:** A failed control board needs a technician to confirm and replace, especially because AccuLink replacement boards sometimes require commissioning with the communicating system.
- **System control fault 199:** Main board failures often need hands-on diagnosis to rule out power issues before replacing expensive parts.
- **Multiple simultaneous fault codes:** This pattern often indicates a system-wide issue — bad ground, failing transformer, or a control board that's taking out everything downstream.

---

## Frequently Asked Questions

**Q: My AccuLink thermostat shows a fault code but the system is still running. Should I be worried?**

It depends on the code. Some faults are logged but non-lockout — the system keeps running and flags the issue for the next maintenance visit. Others cause a lockout. Check the fault code against this list. If it's a pressure or safety fault, call a tech even if the system is running — continuing to run through a safety fault can damage equipment.

**Q: The AccuLink thermostat shows "waiting" after I clear a fault. Is this normal?**

Yes. AccuLink implements a short time delay after a fault clear before restarting the system. This protects the compressor from rapid cycling. Wait 5 minutes after clearing the code — if the system doesn't start, check whether the fault re-appeared.

**Q: Can I replace an AccuLink thermostat with a standard thermostat?**

Technically yes, but you lose all communicating features, fault diagnostics, and may lose some efficiency modes. The outdoor unit will operate in "conventional mode" from a non-communicating thermostat. Some features like variable speed control may not work at all. If budget is the concern, a replacement AccuLink thermostat is the cleaner fix.

**Q: Fault code 80 keeps coming back every morning. What's causing it?**

This is classic thermal expansion behavior. Metal terminals contract overnight and a marginal connection opens up enough to break communication. Check the outdoor unit terminal block — the communication wire terminals are often the culprit. Re-terminate and tighten all screws at the outdoor board. If the problem persists through summer, the outdoor board itself may be failing.

**Q: How do I access the full fault history on the Platinum 950 thermostat?**

From the home screen: tap **Menu → Diagnostics → Fault History**. The 950 stores up to 25 faults with timestamps. This is extremely useful for intermittent issues — the fault timestamp tells you when it happened, which often correlates with temperature, weather, or time-of-day patterns that help identify the cause.
