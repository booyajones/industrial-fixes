---
title: "Goodman Furnace 2 Flashes — Pressure Switch Stuck Closed Fix"
description: "Goodman furnace 2 slow flashes means pressure switch stuck closed. Learn what causes it, how to diagnose, and how to fix it with this step-by-step guide."
pubDatetime: 2026-04-26T12:00:00Z
modDatetime: 2026-04-26T12:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - goodman
  - furnace
  - hvac
  - error-code
---

## Goodman Furnace 2 Flashes — What It Means

**2 slow flashes** on a Goodman furnace control board means the **pressure switch is stuck closed (or closed when it shouldn't be)** — the control board sees the pressure switch in the closed position before the inducer motor has started, which shouldn't be possible under normal conditions. The furnace interprets this as a fault and refuses to proceed through the ignition sequence.

This code also applies to **Amana furnaces** and some **Coleman furnaces** that share the same Goodman control board platform.

Unlike 3-flash (switch open, no draft), 2-flash is the opposite condition — the switch appears closed when it should be open. It's less common but usually has a straightforward fix.

[Jump to Fix](#fix)

## Common Causes

- **Pressure switch stuck closed (failed switch)** — The diaphragm inside the switch can stick in the closed position due to moisture, age, or debris. The switch needs to open freely at rest and close only when the inducer builds draft.
- **Water in the pressure switch hose** — Condensate water can back up through the hose into the pressure switch port, holding the diaphragm closed. This is common on 90%+ efficiency models.
- **Short circuit in the pressure switch wiring** — If the two wires connected to the pressure switch are touching each other or shorted to ground, the control board reads a continuous closed signal.
- **Wrong pressure switch installed** — If a switch with incorrect pressure ratings was installed, it may close at atmospheric pressure and stay closed.
- **Inducer motor running when it shouldn't be** — In rare cases, a stuck inducer relay on the control board can spin the inducer before the call-for-heat sequence begins, legitimately closing the pressure switch early.

## Step-by-Step Diagnosis {#fix}

1. **Disconnect power to the furnace** — Before anything else, turn off the furnace at the breaker or the service switch. Wait 30 seconds.

2. **Locate the pressure switch** — The pressure switch is a small round or oval component usually mounted near the inducer housing or on the vestibule panel, with a small rubber hose connected to one port and 2 electrical wires on the other side.

3. **Check the hose for water** — Disconnect the hose from the pressure switch port. If water drips out, that's your answer. Blow out the hose and clear the condensate drain (see below). Hold the hose end up above the switch level temporarily to prevent re-entry.

4. **Test the pressure switch with a multimeter** — With power off and the hose disconnected, set your multimeter to continuity/resistance mode. Test across the two switch terminals. A good, resting pressure switch should read **open** (no continuity) at atmospheric pressure with no suction applied. If it reads closed (continuity) at rest, the switch is failed and needs replacement.

5. **Inspect the wiring** — Check the two wires connecting to the pressure switch for bare spots, pinched insulation, or any place where the wires could be touching each other or the furnace chassis. A short reads as a permanent "closed" signal.

6. **Check the control board's inducer relay** — With power on, before calling for heat, the inducer should be completely off. If you can hear or feel the inducer running at rest (before any thermostat call), the inducer relay on the control board may be stuck, genuinely closing the pressure switch prematurely.

## How to Fix It

**Water in the pressure switch hose:**
Drain the hose and clear the condensate drain. On 90%+ efficiency furnaces, the condensate drain must flow freely for the furnace to operate normally. Flush the drain line with water or blow it clear with compressed air. Add condensate treatment tablets to prevent future algae blockages.

**Failed pressure switch stuck closed:**
Replace the pressure switch. They're inexpensive — typically $15–30. Match the pressure rating printed on the switch label (measured in inches of water column, e.g., -0.65" WC or -1.05" WC). Reconnect the hose and wire harness. This is a 10-minute repair with a screwdriver and needle-nose pliers.

**Shorted wiring:**
Find the short and repair it. If insulation has worn through where a wire contacts a sheet metal edge, add a rubber grommet or re-route the wire away from the sharp edge. In severe cases, replace the wiring harness.

**Failed control board with stuck inducer relay:**
This is the most expensive diagnosis. If the control board is energizing the inducer relay when it shouldn't be, the board needs replacement. Confirm this only after ruling out all other causes.

## Parts You May Need

| Part | Notes |
|------|-------|
| [Goodman Pressure Switch](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-goodman-furnace-2-flashes&tag=errorcodefixes-20) | Match exact pressure rating (WC value) from old switch label |
| [Furnace Pressure Switch Hose](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-goodman-furnace-2-flashes&tag=errorcodefixes-20) | 1/4" or 3/8" ID vinyl; buy a foot or two |
| [Condensate Drain Treatment](https://www.amazon.com/s?ascsubtag=ecf-goodman-furnace-2-flashes&k=condensate+drain+pan+treatment+tablets&tag=errorcodefixes-20) | Prevents algae-caused clogs |
| [Goodman Control Board](https://www.amazon.com/dp/B0CNZGZ1HS?ascsubtag=ecf-goodman-furnace-2-flashes&tag=errorcodefixes-20) | Only if relay is confirmed stuck — verify model number |
| [Furnace Wire Harness](https://www.amazon.com/s?ascsubtag=ecf-goodman-furnace-2-flashes&k=furnace+wire+harness&tag=errorcodefixes-20) | For severe wiring damage; match model |

## When to Call a Technician

If you've confirmed the pressure switch tests open at rest, the hose is clear of water, and the wiring shows no shorts — but 2 flashes continues — the problem is likely on the control board itself. Control board replacement is straightforward but involves disconnecting and reconnecting multiple wire harnesses. If you're not comfortable mapping the harness connections before removal, a technician is the right call. Take photos of all wire positions before disconnecting anything.

## Related Flash Codes

- [Goodman Furnace 3 Flashes — Pressure Switch Open](/posts/goodman-furnace-3-flashes/)
- [Goodman Furnace 4 Flashes — Open High Limit Switch](/posts/goodman-furnace-4-flashes/)

## See Also

- [Goodman Furnace 4 Flashes — Open High Limit Switch Fix](/posts/goodman-furnace-4-flashes/)
- [Goodman GMS96 Error Codes — Fault Code Guide](/posts/goodman-gms96-error-codes/)
- [Goodman GSX13 Air Conditioner Error Codes — Fault Code Diagnostic Guide](/posts/goodman-gsx13-error-codes/)
- [Goodman vs Bryant Furnaces — A Service Tech's Honest Comparison (2026)](/posts/goodman-vs-bryant-furnaces/)
