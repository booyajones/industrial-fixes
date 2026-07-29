---
title: "Carrier 58UX Furnace Error Codes — Flash Code Diagnostic Guide"
description: "Complete guide to Carrier 58UX furnace error codes and flash sequences, covering common faults like pressure switch, ignition, and high-limit failures with step-by-step fixes."
pubDatetime: 2026-04-22T22:00:00Z
modDatetime: 2026-04-22T22:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - carrier
  - furnace
money_part: "Flame sensor"
---

## Carrier 58UX Furnace Error Codes — What They Mean

The Carrier 58UX is an upflow/horizontal single-stage gas furnace in the Performance series. It uses a standard single-speed PSC blower motor and a diagnostic LED on the control board to communicate fault conditions through flash sequences. Observe the LED (visible through the sight glass on the lower access panel) to read the flash code — count the rapid flashes, then the slow flashes.

## Carrier 58UX Flash Code Reference

| Flash Code | Meaning |
|------------|---------|
| Steady on | Normal — no call for heat |
| Steady off | No power to control board |
| 2 flashes | System lockout — retry limit exceeded |
| 3 flashes | Pressure switch open |
| 4 flashes | Open high-limit device |
| 5 flashes | Flame sensed with gas valve de-energized |
| 6 flashes | 115V power reversed or control board fault |
| 7 flashes | Low flame signal / dirty flame sensor |
| 8 flashes | Check ignitor circuit |
| 9 flashes | Pressure switch hose connection reversed |
| 13 flashes | Limit switch cycle lockout (repeated trips) |
| 14 flashes | Ignition lockout (failed to prove flame 3 times) |
| 33 flashes | Pressure switch opens during heat cycle |
| 34 flashes | Ignition proving failed — intermittent flame |

## Common Causes by Code

- **Code 3 — Pressure switch open** — On the 58UX, check the rubber grommet where the pressure tubing enters the inducer housing. These grommets crack and cause air leaks that prevent the switch from closing. Also check the condensate drain for blockage.
- **Code 4 — High limit open** — Restricted airflow from dirty filter, closed registers, or dirty evaporator coil. The 58UX has a manual-reset rollout switch in addition to the auto-reset limit — if the rollout has tripped, you must manually press the red button on the switch before the furnace will operate.
- **Code 7 — Weak flame signal** — Dirty flame sensor is the usual culprit. The flame sensor on the 58UX is accessed by removing the burner access panel. Clean the rod with fine steel wool or emery cloth and check for cracks in the ceramic insulator.
- **Code 14 — Ignition lockout** — Hot surface ignitor failure is most common. Check the ignitor for cracks visually (don't touch with bare hands). Resistance should be between 40–90 ohms at room temperature. Low gas pressure or a sticky gas valve can also cause this code.
- **Code 33 — Pressure switch opens during run** — Usually condensate-related on the 58UX since it is a 90%+ efficiency furnace. The secondary heat exchanger produces condensate; if the drain backs up mid-cycle, the inducer inlet pressure changes and the pressure switch opens.

## Step-by-Step Fix {#fix}

1. **Identify the code** — Note all flashes before doing anything. A two-code pattern like 3-3 means 33, not a Code 3 twice.
2. **Check condensate drain** — For any pressure switch code, pour water through the condensate drain and confirm it flows freely. The 58UX uses a PVC condensate trap mounted internally — confirm it is not cracked or plugged with algae.
3. **Inspect the filter** — For Code 4 and 13, check the filter first. A completely clogged filter can cause limit trips in under two minutes of run time.
4. **Test the rollout switches** — On the 58UX, locate the rollout switches on the burner box. With power off, check continuity across each switch — should be closed (continuity). A tripped rollout switch indicates cracked heat exchanger or flame rollout; do not reset repeatedly without finding the cause.
5. **Verify ignitor** — For Code 8 and 14, measure ignitor resistance. If outside the 40–90 ohm range, replace it. Also confirm the ignitor control relay on the board is clicking during the ignition trial.
6. **Reset and monitor** — After repairs, cycle power at the disconnect switch, turn the thermostat to Heat, and watch one full cycle to confirm no fault recurrence.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Flame sensor | [Amazon](https://www.amazon.com/s?k=Flame+sensor&tag=errorcodefixes-20) \| Most common; clean first, replace if cracked |
| Hot surface ignitor | [View on Amazon](https://www.amazon.com/dp/B00BTLLJ40?ascsubtag=ecf-carrier-58ux-error-codes&tag=errorcodefixes-20) \| 120V silicon nitride type for 58UX |
| Pressure switch | [View on Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-carrier-58ux-error-codes&tag=errorcodefixes-20) \| Confirm correct water column rating (typically 0.85" or 1.2") |
| Inducer motor | [View on Amazon](https://www.amazon.com/dp/B00FDZ90B2?ascsubtag=ecf-carrier-58ux-error-codes&tag=errorcodefixes-20) \| If inducer is weak or noisy, pressure switch faults follow |
| High-limit switch | [View on Amazon](https://www.amazon.com/dp/B0BN3TRG9R?ascsubtag=ecf-carrier-58ux-error-codes&tag=errorcodefixes-20) \| Auto-reset type; check continuity before replacing |
| Rollout switch | [View on Amazon](https://www.amazon.com/dp/B0BN3TRG9R?ascsubtag=ecf-carrier-58ux-error-codes&tag=errorcodefixes-20) \| Manual reset; investigate cause before resetting |
## When to Call a Pro

A cracked heat exchanger can cause rollout switch trips and carbon monoxide hazards. If you see repeated rollout trips, persistent combustion odors, or visible cracks in the heat exchanger panels, do not operate the furnace — call a licensed HVAC technician immediately. Gas valve and refrigerant-side diagnostics also require professional tools and certification.
