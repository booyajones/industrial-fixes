---
title: "Carrier Furnace Error Code 31 — Pressure Switch Open Fix"
description: "Carrier error code 31 means the pressure switch failed to close. Blocked condensate, cracked hose, or weak inducer. Step-by-step diagnosis and fix."
pubDatetime: 2026-04-26T12:00:00Z
modDatetime: 2026-04-26T12:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - carrier
  - furnace
  - hvac
  - error-code
---

## Carrier Error Code 31 — What It Means

Carrier error code 31 is a **pressure switch open** fault — the furnace's draft inducer motor started but the control board never received confirmation from the pressure switch that adequate combustion airflow was established. Without that signal, the furnace locks out ignition and flashes code 31 on the LED (a 3-1 blink pattern: 3 flashes, pause, 1 flash).

The pressure switch is a small safety device that monitors negative pressure created by the inducer motor. When the inducer spins up and creates proper draft, the switch closes and allows the ignition sequence to proceed. Code 31 means that switch never closed — either because the draft wasn't strong enough, or because there's a mechanical/electrical problem with the switch or its hose.

[Jump to Fix](#fix)

## Common Causes

- **Blocked condensate drain line** — On high-efficiency (90%+) Carrier furnaces, condensate water can back up and clog the pressure switch port or hose, preventing the switch from seeing the correct pressure. This is the most common cause on 90%+ models.
- **Cracked or disconnected pressure switch hose** — The small rubber or vinyl hose connecting the inducer housing to the pressure switch can crack, come loose, or develop a pinhole. Any leak means the switch won't see enough pressure to close.
- **Failed draft inducer motor** — A weak, slow, or seized inducer motor can't generate sufficient negative pressure to close the pressure switch. Listen for unusual sounds or slow startup.
- **Blocked intake or exhaust vent pipe** — A bird nest, ice dam, or debris in the PVC vent pipes prevents proper draft, leaving the pressure switch open.
- **Failed pressure switch** — The switch diaphragm wears out over time and can fail open permanently.
- **Blocked inducer wheel** — Debris, corrosion, or accumulated grime on the inducer impeller reduces draft even when the motor runs at normal speed.

## Step-by-Step Diagnosis {#fix}

1. **Listen to the inducer on startup** — Call for heat and stand near the furnace. You should hear the inducer motor spin up first (a whooshing or humming sound). If it sounds weak, slow, or doesn't start at all, the inducer is likely the problem.

2. **Check the outdoor vent pipes** — Walk outside and inspect both the intake and exhaust PVC pipes where they exit the wall or roof. Remove any visible obstruction. In cold climates, check for ice blocking the pipe opening. On horizontal runs, look for sagging sections that collect water and block airflow.

3. **Check the condensate drain** — On 90%+ efficiency models, trace the condensate drain from the furnace to where it terminates (usually a floor drain or condensate pump). Disconnect the drain line at the furnace and blow it out with compressed air or pour water through it to confirm it flows freely. A clogged drain is a 10-minute fix.

4. **Inspect the pressure switch hose** — Locate the small tubing connecting the inducer housing (or collector box) to the pressure switch. Run your fingers along every inch of it. Look for cracks, holes, kinks, or loose connections at either end. A cracked hose is a common and cheap fix.

5. **Test the pressure switch manually** — With the inducer running and the furnace calling for heat, carefully disconnect the hose from the pressure switch and apply gentle mouth suction directly to the port. If the furnace proceeds to ignition, the switch is functional — the problem is insufficient draft reaching it. If nothing changes, the switch itself may be failed.

6. **Test the pressure switch with a multimeter** — Power off the furnace. Disconnect the hose from the switch. With the multimeter on continuity, apply suction to the switch port (a hand vacuum pump works perfectly). The switch should close (show continuity) with suction applied and open when released. If it stays open regardless, replace the switch.

## How to Fix It

**Blocked condensate drain:** Flush or blow clear the entire drain line. Treat with condensate drain tablets to prevent future algae buildup. If a condensate pump is installed, confirm it's functioning.

**Cracked pressure hose:** Cut a new piece of the same diameter tubing (1/4" or 3/8" ID vinyl or rubber). Replace the entire hose — don't just tape over a crack, as it will fail again quickly.

**Failed pressure switch:** Disconnect the hose and 2-wire connector, remove the mounting screws, and swap in a replacement switch with the same pressure rating (printed on the switch body in inches of WC). This is a straightforward repair — 10–15 minutes.

**Weak inducer motor:** If the motor is weak but still running, check whether the run capacitor (if applicable) has failed — a bad capacitor causes slow motor operation. Replace the capacitor first (it's cheap) before replacing the whole motor.

**Blocked vent pipe:** Clear the obstruction and ensure the pipe terminates correctly per Carrier installation specs (minimum clearances from grade, windows, and gas meters). On cold-climate installs, ensure the pipe termination is using a proper termination fitting rated for ice conditions.

## Parts You May Need

| Part | Notes |
|------|-------|
| [Carrier Pressure Switch](https://www.amazon.com/s?k=carrier+furnace+pressure+switch&tag=errorcodefixes-20) | Match pressure rating (WC) from label on existing switch |
| [Furnace Pressure Switch Hose](https://www.amazon.com/s?k=furnace+pressure+switch+hose&tag=errorcodefixes-20) | Standard 1/4" or 3/8" ID vinyl tubing |
| [Carrier Inducer Motor](https://www.amazon.com/s?k=carrier+furnace+draft+inducer+motor&tag=errorcodefixes-20) | Match HP, RPM, and voltage from inducer motor label |
| [Condensate Drain Treatment](https://www.amazon.com/s?k=condensate+drain+treatment+tablets+hvac&tag=errorcodefixes-20) | Prevents algae buildup |
| [Condensate Pump](https://www.amazon.com/s?k=hvac+condensate+pump&tag=errorcodefixes-20) | Replace if pump has failed and is backing up into the system |

## When to Call a Technician

If the inducer sounds healthy, the vent pipes are clear, the condensate drain flows freely, the pressure hose is intact, and you've replaced the pressure switch — and code 31 continues — the issue may be inside the inducer housing (cracked collector box, failed gasket) or on the control board. A cracked collector box can leak enough pressure to prevent switch closure even with a functioning inducer. This diagnosis requires removing the inducer assembly and pressure-testing the collector box, which is a job for a qualified HVAC technician.

## Related Error Codes

- [Carrier Furnace Error Code 33 — Flame Rollout & High Limit Switch Fix](/posts/carrier-error-code-33/)
- [Carrier Furnace Error Code 13 — Limit Circuit Lockout](/posts/carrier-error-code-13/)
