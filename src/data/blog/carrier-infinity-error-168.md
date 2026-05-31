---
title: "Carrier Infinity System Communication Error 168 — Wiring & Board Fix"
author: "Marcus Webb"
pubDatetime: 2026-04-24T21:00:00Z
modDatetime: 2026-04-24T21:00:00Z
slug: carrier-infinity-error-168
featured: false
draft: false
tags:
  - carrier
  - infinity-system
  - furnace
  - communicating-system
  - error-codes
description: "Carrier Infinity error 168 is a communication fault between the furnace control board and the Infinity system — here's how to diagnose the data bus wiring and control boards that cause it."
---

## Error Code: Carrier Infinity Error 168

**What it means:** Error 168 on the Carrier Infinity communicating HVAC system indicates a communication failure between the furnace control board (IFC) and the Infinity system network. The Infinity system uses a proprietary four-wire data bus (called the SAB — System Automation Bus) to connect the furnace, air handler, outdoor unit, thermostat, and accessories. Error 168 means the furnace IFC is not receiving valid data from the Infinity network, or is not transmitting correctly on it.

This is specific to Carrier Infinity and Bryant Evolution communicating systems — it will not appear on conventional (non-communicating) furnaces. These systems are common in high-end residential installs from approximately 2007–present.

## Common Causes

- **SAB wiring fault** — The four-wire communication cable (typically labeled 1, 2, C, and D on the terminal strip) has a loose connection, damaged conductor, or pinched wire where it passes through the furnace cabinet. This is the most common cause by far.
- **Failed Infinity control board (IFC)** — The furnace's Infinity control board has failed its communication processor. The IFC is a specialized board that runs both furnace operations AND the SAB network interface.
- **Outdoor unit board failure** — If the outdoor unit (condenser or heat pump) has a failed control board, the entire Infinity network can drop, triggering error 168 at the furnace.
- **Thermostat communication fault** — A failed Infinity thermostat or one that has lost its address on the network can disrupt the bus and trigger 168 at other devices.
- **Short or ground fault on the SAB wiring** — A staple through the communication wire, a pinched wire in a door jam, or wire insulation chafing against sheet metal can cause bus faults that show up as error 168.
- **Power surge** — Lightning strikes or power surges can damage the communication interface chips on multiple boards simultaneously.

## Step-by-Step Fix {#step-by-step-fix}

1. **Access the fault detail on the Infinity thermostat.** Navigate to the diagnostic menu (Menu → Diagnostics or Alerts). Error 168 should show the source device (furnace, air handler, outdoor unit) — note which device is reporting the error and which devices it can't see.

2. **Inspect all SAB wiring connections.** The SAB cable connects to every component's control board at a 4-terminal connector labeled 1, 2, C, D (or similar). At the furnace, open the control panel and check that all four wires are seated firmly in the IFC terminal block. Tug each wire gently — loose wires are a very common cause of intermittent error 168.

3. **Trace the SAB cable for physical damage.** Follow the four-wire cable from the furnace to where it exits the cabinet and runs to other components. Look for pinches at the furnace access panel edge (extremely common — closing the panel can nick the wire over time), staples that have pierced the insulation, or bare wire touching sheet metal.

4. **Isolate the bus.** Disconnect the SAB wiring at each component one at a time, starting with the outdoor unit, and restart the furnace after each disconnection. If error 168 clears when a specific device is disconnected, that device (or its wiring run) is the source of the fault.

5. **Check for SAB bus voltage.** With a multimeter, measure voltage between SAB terminals 1 and 2 at the furnace IFC. A healthy Carrier Infinity data bus shows approximately 24VAC between these terminals when idle. Zero voltage suggests a failed IFC or power supply issue.

6. **Power-cycle all components.** Turn off power to the furnace, outdoor unit, and thermostat simultaneously. Wait 2 minutes. Restore power in order: furnace first, then outdoor unit, then thermostat. Some transient communication errors clear with a clean power cycle.

7. **Replace the furnace IFC if wiring checks out.** If all wiring is intact, all connections are tight, and the bus voltage is absent at the furnace IFC, the IFC is likely failed. The Infinity IFC is model-specific — verify the part number on the existing board label before ordering.

8. **Replace the thermostat as a last resort.** If the error persists after IFC replacement, and the outdoor unit checks out, the Infinity thermostat's communication module may have failed. Carrier Infinity thermostats are expensive ($200–$400) but failure does occur, particularly in high-humidity environments where condensation reaches the thermostat housing.

## Parts Often Needed {#parts-often-needed}

| Part | Part Number | Typical Cost | Where to Buy |
|------|-------------|--------------|--------------|
| Carrier Infinity IFC (58CVX/58MVC series) | HK42FZ034 | $250–$400 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-carrier-infinity-error-168&k=Carrier+Infinity+IFC+HK42FZ034&tag=errorcodefixes-20) \| Johnstone Supply |
| Carrier Infinity IFC (58CTX/58MTA series) | HK42FZ018 | $200–$350 | [Amazon](https://www.amazon.com/s?k=Carrier+Infinity+IFC+%2858CTX%2F58MTA+series%29&tag=errorcodefixes-20) \| RepairClinic |
| SAB communication cable (4-wire, 18 AWG, per foot) | — | $0.30–$0.60/ft | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-carrier-infinity-error-168&k=18+awg+4+conductor+thermostat+wire&tag=errorcodefixes-20) \| Home Depot |
| Infinity Touch thermostat | TP-NAC01-A | $300–$450 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-carrier-infinity-error-168&k=Carrier+Infinity+Touch+thermostat+TP-NAC01-A&tag=errorcodefixes-20) \| Carrier dealer |
| Outdoor unit control board (varies by model) | — | $200–$500 | [Amazon](https://www.amazon.com/s?k=Outdoor+unit+control+board+%28varies+by+model%29&tag=errorcodefixes-20) \| Carrier dealer |

## When to Call a Professional

The Carrier Infinity system's communicating architecture is significantly more complex than conventional HVAC wiring. Correctly diagnosing error 168 requires understanding the SAB topology, being able to interpret the Infinity diagnostic menus, and having a multimeter comfortable measuring low-voltage data bus signals. If you're not familiar with these systems, the risk of replacing expensive boards unnecessarily is high. A Carrier-certified technician can run the Infinity system's built-in network diagnostic routine, which identifies exactly which device is failing to communicate — saving hours of trial-and-error.

> **Pro tip:** Before replacing any boards for error 168, check whether all Infinity components are on the same electrical phase. On two-story homes where the outdoor unit is on a 240V circuit and the furnace is on a different leg, phase alignment issues can disrupt the SAB bus. The four SAB wires must span only one electrical phase to communicate correctly.

## Related Articles

- [Carrier 11 Error Code — Causes & Fix](/posts/carrier-11-error-code/)
- [Carrier 12 Error Code — Causes & Fix](/posts/carrier-12-error-code/)
- [Carrier 13 Error Code — Limit Switch Lockout Fix](/posts/carrier-13-error-code/)
- [Carrier 13 Soft Lockout — What's Different from Hard Lockout](/posts/carrier-13-soft-lockout/)
- [Carrier 14 Error Code — Causes & Fix](/posts/carrier-14-error-code/)
