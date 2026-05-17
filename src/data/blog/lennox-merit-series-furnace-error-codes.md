---
title: "Lennox Merit Series Furnace Error Codes - What It Means and How to Fix It"
description: "Complete Lennox Merit series furnace flash code reference covering all LED blink patterns, fault causes, and step-by-step fixes for the ML193, ML180, and related models."
pubDatetime: 2026-04-25T00:00:00Z
author: "Marcus Webb"
tags:
  - hvac
  - error-codes
---

The Lennox Merit series includes some of the most common furnaces installed in American homes — models like the ML193, ML180, ML195, and their predecessors. These units use a diagnostic LED on the control board to communicate faults via flash codes. This guide covers every code, what it means, and how to fix it.

## What Does Lennox Merit Series Furnace Error Codes Mean?

Locate the observation window on the furnace door. Behind it sits the control board with a status LED — usually amber or green. The LED blinks a two-digit pattern: a short set of blinks (the first digit), a pause, then a longer set of blinks (the second digit). Some older Merit models use a single-digit code.

**Complete Flash Code Reference**

| Code | Fault | Notes |
|------|-------|-------|
| 1 flash | Normal — furnace is off, no call for heat | No action needed |
| 2 flashes | Normal operation — heating | No action needed |
| 1-1 | System lockout (retry limit exceeded) | Reset by cycling thermostat or power |
| 1-2 | Blower on before lockout | Associated with failed heat |
| 2-2 | Low pressure switch stuck open | Inducer or pressure switch fault |
| 2-3 | Low pressure switch stuck closed | Stuck switch or inducer not running |
| 3-1 | High limit switch open | Overheating — check filter first |
| 3-2 | Flame sensed with gas valve closed | Flame sensor fault or grounding issue |
| 3-3 | Rollout switch open | Safety shutdown — requires inspection |
| 3-4 | High limit switch stuck open | Limit failed open |
| 4-1 | Ignition failure after max retries | Igniter, gas, or flame sensor |
| 4-2 | Ignition proving failure | Flame sensor contaminated |
| 4-4 | Gas valve relay fault | Control board failure |
| 5-1 | Unexpected flame | Gas valve leaking; call a tech |
| 5-2 | Low flame signal | Flame sensor or gas pressure |

### Code 2-2 — Low Pressure Switch Stuck Open

The pressure switch monitors whether the draft inducer is creating enough negative pressure to safely operate the burners. If it reads open when it should be closed, the furnace won't fire.

**Common causes:** Failed inducer motor, cracked or kinked pressure switch hose, clogged condensate drain (on 90%+ models), or a failed pressure switch itself. Start by blowing out the rubber hose connecting the inducer housing to the pressure switch — clogs are the #1 cause on Merit 90+ models.

### Code 3-1 — High Limit Switch Open

The heat exchanger is getting too hot. On most Merit furnaces, the high limit opens at 170°F–200°F. The almost always cause: blocked airflow.

**Fix it in order:**
1. Replace the air filter (do this first, every time)
2. Verify all supply and return registers are open
3. Check the blower wheel for debris
4. Confirm the blower motor is running at the right speed
5. If airflow is fine, test the limit switch with a multimeter for continuity when cold

### Code 3-3 — Rollout Switch Open

This is a safety alert. Flames rolled out of the combustion chamber — a sign of blocked flue, cracked heat exchanger, or inadequate combustion air. Do not reset and run the furnace without determining the cause. Carbon monoxide exposure is a real risk here.

### Code 4-1 — Ignition Failure (Lockout)

The furnace attempted ignition the maximum number of times (usually 3) and locked out. Check gas supply, verify the igniter glows (it should get bright orange/white within 15–20 seconds of a heating call), and check the flame sensor rod.

### Code 4-2 — Ignition Proving Failure

The flame lights but the flame sensor can't prove it's there. The sensor rod is almost certainly dirty. Clean it with fine steel wool or light sandpaper — no chemicals.

## How to Fix It

1. **Read the flash code.** Count the short blinks before the pause (first digit) and the blinks after (second digit). Write it down.
2. **Reset the system.** Turn the thermostat to OFF for 30 seconds, then back to HEAT. Watch whether the same code returns.
3. **Replace the filter.** Before anything else, if you have a 3-1 (high limit) code, install a new filter. This clears the problem 50% of the time.
4. **Check the pressure switch hose.** On 90+ Merit furnaces, the drain trap and pressure switch hose are common failure points. Blow through the hose to confirm it's clear.
5. **Test the inducer.** On a call for heat, the inducer should spin up within seconds. If you hear nothing, check for 120V at the inducer motor leads. No voltage = control board. Voltage but no spin = failed motor.
6. **Clean the flame sensor.** Remove the single-screw flame sensor rod. Lightly sand the metal rod (not the porcelain) with fine-grit sandpaper. Reinstall.
7. **Test the igniter.** With power off, check resistance across the igniter: 40–200 ohms is normal. Infinite resistance = cracked igniter, replace it.
8. **Check the rollout switch.** Code 3-3 requires manual reset — press the red button on the switch (located near the burners). It will reset only after it cools. If it trips again, stop and call a tech.

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|-------------|
| Hot surface igniter (45K BTU, 120V) | Fixes Code 4-1 ignition failure | $20–$45 — [Search on Amazon](https://www.amazon.com/dp/B00BTLLJ40?ascsubtag=ecf-lennox-merit-series-furnace-error-codes&tag=errorcodefixes-20) |
| Flame sensor rod (universal) | Fixes Code 4-2 proving failure | $10–$20 — [Search on Amazon](https://www.amazon.com/dp/B0CZ7M9V4D?ascsubtag=ecf-lennox-merit-series-furnace-error-codes&tag=errorcodefixes-20) |
| Draft inducer motor (Lennox 10J62) | Fixes Code 2-2 when motor fails | $100–$250 — [Search on Amazon](https://www.amazon.com/dp/B00FDZ90B2?ascsubtag=ecf-lennox-merit-series-furnace-error-codes&tag=errorcodefixes-20) |
| Pressure switch (0.48" WC) | Fixes Code 2-2 after hose checks out | $15–$30 — [Search on Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-lennox-merit-series-furnace-error-codes&tag=errorcodefixes-20) |
| High limit switch (200°F auto-reset) | Fixes Code 3-4 stuck-open limit | $15–$30 — [Search on Amazon](https://www.amazon.com/dp/B0BN3TRG9R?ascsubtag=ecf-lennox-merit-series-furnace-error-codes&tag=errorcodefixes-20) |
| Control board (LB-100021E) | Fixes Code 4-4 gas valve relay fault | $100–$200 — [Search on Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?ascsubtag=ecf-lennox-merit-series-furnace-error-codes&tag=errorcodefixes-20) |

## When to Call a Pro

- **Code 3-3 (rollout switch)** — Don't run the furnace until a technician confirms the heat exchanger is intact and the flue is clear. Carbon monoxide risk.
- **Code 5-1 (unexpected flame)** — Gas is getting through when it shouldn't. This is a gas valve fault. Turn off the gas and call immediately.
- **Code 1-1 persistent lockout** — If the furnace locks out repeatedly even after resetting, a deeper problem exists. A tech needs to watch the full ignition sequence.
- Any smell of gas or burning plastic.
- The blower motor is making grinding, squealing, or scraping sounds — a seizing motor can overheat the heat exchanger.

## Frequently Asked Questions

**Q: My Lennox Merit furnace shows a 3-1 code but I just replaced the filter last week. What else could cause overheating?**

A: A new filter doesn't rule out airflow problems. Check that every supply vent in the house is open (closing vents increases static pressure and restricts airflow). Verify the return air grille isn't blocked by furniture. Also confirm the blower wheel isn't caked with dust — a dirty blower moves far less air than a clean one, regardless of filter condition.

**Q: How do I manually reset the Lennox Merit furnace after a lockout?**

A: Turn the thermostat completely off and wait 30 seconds. Turn it back to HEAT. The control board should reset and attempt to re-fire. For a rollout switch (code 3-3), you also need to physically press the red reset button on the switch itself before the board will allow ignition.

**Q: The furnace runs for 10 minutes then shuts off and flashes 3-1. It restarts after 20 minutes. What is this cycle called?**

A: This is called a short-cycling high-limit trip. The heat exchanger overheats, the limit opens, the furnace shuts off, the limit resets once cool, and the cycle repeats. It's putting enormous stress on the heat exchanger. Every heat-cool-heat cycle risks cracking it. Fix the airflow problem before the heat exchanger fails — that turns a $30 filter problem into a $1,500 repair.

**Q: Can I replace the Lennox Merit furnace flame sensor myself?**

A: Yes, this is one of the simpler DIY HVAC repairs. Turn off power at the furnace disconnect, locate the sensor rod (a metal rod on a porcelain holder, with one wire attached), remove the single screw, clean the rod with fine sandpaper, and reinstall. The whole job takes under 10 minutes. If cleaning doesn't help, replace the sensor — a universal rod costs under $20.

**Q: The Lennox Merit furnace is blinking but I can't figure out the pattern. Any tricks?**

A: The LED blinks in groups. Watch for a short blink (first digit), a 1-2 second pause, then more blinks (second digit), then a longer pause before it repeats. If you're still confused, pull up the furnace manual (search for your model number + "installation instructions PDF" — Lennox posts them free online). The LED code chart is always printed on the inside of the furnace door panel too.

## Related Articles

- [Lennox Error Code 292 — Ignition Failure Fix](/posts/lennox-292-error-code/)
- [Lennox EL296V Error Codes — Variable-Speed Furnace Diagnostic Guide](/posts/lennox-el296v-error-codes/)
- [Lennox Elite Series Furnace Error Codes — Fault Code Diagnostic Guide](/posts/lennox-elite-series-furnace-codes/)
- [Lennox 103 Error Code — Causes & Fix](/posts/lennox-error-code-103/)
- [Lennox Error Code 111 — Causes & Fix](/posts/lennox-error-code-111/)
