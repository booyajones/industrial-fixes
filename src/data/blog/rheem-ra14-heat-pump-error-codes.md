---
title: "Rheem RA14 Heat Pump Error Codes - What It Means and How to Fix It"
description: "Complete guide to Rheem RA14 heat pump flash codes and diagnostic LED patterns. Learn what each code means and how to resolve the fault yourself before calling a tech."
pubDatetime: 2026-04-25T00:00:00Z
author: "Marcus Webb"
tags:
  - hvac
  - error-codes
---

The Rheem RA14 is a 14 SEER single-stage heat pump in the Classic series, one of the most widely installed units across residential homes in the U.S. When something goes wrong, the control board communicates via a diagnostic LED that blinks in a specific pattern. Count the flashes, compare them below, and you'll know exactly what the system is telling you.

## What Does Rheem RA14 Heat Pump Error Codes Mean?

The RA14 uses a single amber or green LED on the control board (located inside the air handler or furnace, not the outdoor unit). Power the system off, wait 30 seconds, then power back on and watch the LED blink pattern.

**Flash Code Reference Table**

| Flash Count | Fault Description | Priority |
|-------------|-------------------|----------|
| 1 flash | Normal operation — no fault | — |
| 2 flashes | Low-pressure switch open (lockout) | High |
| 3 flashes | High-pressure switch open (lockout) | High |
| 4 flashes | Open thermostat (T-stat circuit fault) | Medium |
| 5 flashes | Outdoor unit not communicating | Medium |
| 6 flashes | Defrost thermostat open | Medium |
| 7 flashes | Fault in the refrigerant system (flood-back detected) | High |
| 8 flashes | Loss of charge / pressure trip during cooling | High |
| Continuous on | Control board internal fault | Critical |
| Continuous off | No power to control board | Critical |

### 2 Flashes — Low-Pressure Lockout

The low-pressure switch tripped. This almost always means one of three things: the refrigerant charge is low due to a leak, the metering device (TXV or fixed orifice) is restricted, or the outdoor coil is blocked and not allowing proper refrigerant flow.

Start by checking the outdoor unit for debris, ice buildup, or collapsed fins. If the coil looks fine, the system likely needs refrigerant leak detection and recharge — that's EPA 608 certified technician territory.

### 3 Flashes — High-Pressure Lockout

High-side pressure exceeded the cutoff (typically 650 psig for R-410A). Common culprits: dirty condenser coil, failed condenser fan motor, refrigerant overcharge, or a non-condensable gas (air) in the system.

Clean the condenser coil with a hose from the inside out. Check that the fan blade spins freely and the motor runs. If both look fine, the system needs a pressure check with gauges.

### 4 Flashes — Open Thermostat Circuit

The control board isn't seeing a call from the thermostat. Check the wiring at both the thermostat and the air handler terminal strip. A loose Y wire is the most common cause. Also check for a blown 3A or 5A fuse on the control board.

### 5 Flashes — Outdoor Unit Communication Fault

The air handler and outdoor unit aren't talking. On communicating systems, check the comm wire (typically a 4-wire cable). On conventional systems, check the Y, G, and C wire connections at both ends. Also verify the outdoor unit has 240V power.

### 6 Flashes — Defrost Thermostat Open

The defrost thermostat (mounted on the outdoor coil) is reading open when it shouldn't be. Replace the thermostat — part number 47-21517-02 is a common replacement for Rheem/Ruud units. In cold climates this can also be caused by a defrost board that's not initiating defrost cycles properly.

### 7 Flashes — Refrigerant Flood-Back

Liquid refrigerant is returning to the compressor — a serious condition that can destroy the compressor. Causes include a stuck-open TXV, low airflow across the indoor coil, or a refrigerant overcharge. Do not run the system until this is diagnosed.

### 8 Flashes — Loss of Charge (Cooling Lockout)

Similar to 2 flashes but specifically triggered during a cooling cycle. The refrigerant charge is low. The system has locked out to protect the compressor. Requires leak detection, repair, and recharge.

## How to Fix It

1. **Identify the flash code.** Count the blinks on the LED. There's usually a pause between sequences.
2. **Reset the fault.** Turn the thermostat to OFF, then cut power at the breaker for 30 seconds. Restore power and watch whether the fault returns.
3. **Check the basics first.** Dirty filter, blocked outdoor unit, tripped breaker, or a loose wire account for about 60% of service calls.
4. **Inspect the outdoor coil.** Rinse gently with a garden hose from the inside out. Never use a pressure washer.
5. **Verify refrigerant line temperatures.** The suction line (larger insulated line) should feel cold and slightly sweating in cooling mode. If it's warm or frosted over, you have a refrigerant issue.
6. **Check the defrost board.** On units with a defrost issue (6 flashes), put the system into test defrost mode: locate the W2 or TEST jumper on the defrost board and short it for 3 seconds.
7. **Inspect all electrical connections.** Terminal strips corrode over time. Wiggle every wire and look for discoloration or burn marks.
8. **Call a certified technician** for anything involving refrigerant (2, 3, 7, or 8 flash codes).

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|-------------|
| Defrost thermostat (47-21517-02) | Fixes 6-flash defrost open fault | $15–$30 — [Search on Amazon](https://www.amazon.com/s?ascsubtag=ecf-rheem-ra14-heat-pump-error-codes&k=Rheem+defrost+thermostat+47-21517-02&tag=errorcodefixes-20) |
| Control board (47-102684-83) | Fixes continuous-on or board faults | $80–$150 — [Search on Amazon](https://www.amazon.com/s?k=Control+board+%2847-102684-83%29&tag=errorcodefixes-20) |
| Capacitor (dual run, 45/5 MFD) | Common cause of fan or compressor failure | $15–$35 — [Search on Amazon](https://www.amazon.com/dp/B01M05L7B3?ascsubtag=ecf-rheem-ra14-heat-pump-error-codes&tag=errorcodefixes-20) |
| Contactor (40A single-pole) | Fails when the compressor won't start | $20–$40 — [Search on Amazon](https://www.amazon.com/dp/B0CJFZQVPT?ascsubtag=ecf-rheem-ra14-heat-pump-error-codes&tag=errorcodefixes-20) |
| TXV expansion valve (R-410A) | Required if flood-back is diagnosed | $60–$120 — [Search on Amazon](https://www.amazon.com/s?ascsubtag=ecf-rheem-ra14-heat-pump-error-codes&k=TXV+expansion+valve+R410A+heat+pump&tag=errorcodefixes-20) |
| 3A control board fuse | Fixes no-control faults from blown fuse | $5–$10 — [Search on Amazon](https://www.amazon.com/s?k=3A+control+board+fuse&tag=errorcodefixes-20) |

## When to Call a Pro

Call a licensed HVAC technician if:

- The flash code indicates 2, 3, 7, or 8 flashes — these require refrigerant gauges and EPA 608 certification to diagnose and repair properly.
- The compressor won't start even after capacitor and contactor replacement.
- You see burn marks, melted wiring, or smell something burnt near the control board.
- The unit ices up completely (solid block of ice around the outdoor coil) and doesn't recover after defrost mode.
- You replaced a part and the same flash code returned within a day.

Refrigerant work is legally restricted. Any diagnosis involving system pressure checks must be done by a certified technician.

## Frequently Asked Questions

**Q: My Rheem RA14 is blinking 3 times and the outdoor fan is running but the compressor isn't. What's wrong?**

A: Three flashes signal a high-pressure trip. The most common culprit when the fan is running but the compressor isn't is a dirty condenser coil or an overcharge. Rinse the coil and reset the system. If the fault returns within a few minutes, you need a technician with gauges to check the high-side pressure and refrigerant charge.

**Q: The LED is completely off. Is the heat pump dead?**

A: Not necessarily. A dark LED usually means no 24V control power. Check the main breaker, the disconnect at the outdoor unit, and the fuse or breaker on the air handler control board. If all of those are fine and the LED is still off, the transformer (24V, 40VA) may have failed.

**Q: How do I put the Rheem RA14 into defrost mode manually?**

A: Locate the defrost control board inside the air handler. Find the TEST pins or W2/Y jumper. Short these two pins with a small wire or screwdriver for 3–5 seconds. The unit will enter a defrost cycle, the reversing valve will shift, and the outdoor fan will stop. The cycle ends when the defrost thermostat closes (coil temperature rises above ~55°F) or after a maximum time limit of 10 minutes.

**Q: How often should I clean the Rheem RA14 condenser coil?**

A: At minimum, once per year before cooling season. If you're in a dusty area or near cottonwood trees, clean it twice. A dirty coil is the single most preventable cause of high-pressure faults and compressor failure.

**Q: My RA14 was installed 8 years ago and keeps blinking 2 or 3 flashes. Is it time to replace?**

A: Not necessarily. If the refrigerant charge is low due to a slow leak, a tech can locate the leak, repair it, and recharge the system. However, if the compressor is making grinding or rattling noises, or the leak is in the coil (which is expensive to replace), a cost comparison between repair and replacement is worth running. Units over 10–12 years old with major component failures often make more economic sense to replace.
