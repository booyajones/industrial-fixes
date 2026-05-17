---
title: "Carrier Furnace Error Code 13 — Limit Circuit Lockout Fix"
description: "Carrier error code 13 means limit circuit lockout after repeated high-limit trips. It auto-resets after 3 hours. Here's what caused it and how to fix it."
pubDatetime: 2026-04-26T12:00:00Z
modDatetime: 2026-04-26T12:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - carrier
  - furnace
  - hvac
  - error-code
---

## Carrier Error Code 13 — What It Means

Carrier error code 13 is a **limit circuit lockout** — the furnace's high limit switch has opened and tripped so many times during a single heating cycle that the control board has locked the furnace out entirely. On most Carrier control boards, code 13 displays as a **1-3 blink pattern** (1 flash, pause, 3 flashes).

Here's the important detail most people don't know: **code 13 auto-resets after 3 hours**. The furnace will attempt to restart on its own. This is why so many people search for code 13 — they wake up cold, see the code, and then an hour or two later the furnace starts working again. It seems fixed, but the underlying problem is still there and will cause another lockout.

Code 13 is not the root problem. It's the furnace telling you code 33 (limit fault) happened repeatedly and it's done trying until things cool down. Fix the cause of the repeated limit trips or you'll be back here again.

In 80% of cases, a clogged air filter is the entire problem. Check that first.

[Jump to Fix](#fix)

## Common Causes

- **Dirty or clogged air filter** — Restricted airflow causes the heat exchanger to overheat repeatedly, tripping the high limit switch on each heating cycle until the board locks out. This is the #1 cause.
- **Blocked supply or return vents** — Too many closed registers chokes airflow. Same result as a dirty filter — repeated overheating until lockout.
- **Failed blower motor or capacitor** — If the indoor blower isn't moving air across the heat exchanger, temperatures spike every time the burner fires.
- **Faulty high limit switch** — A limit switch that's lost its calibration trips at too low a temperature, causing repeated nuisance trips that eventually trigger code 13.
- **Dirty evaporator coil** — A clogged A/C coil blocks airflow through the furnace, especially in heating season when the coil can freeze over or accumulate dust.
- **Collapsed or undersized ductwork** — Crushed, disconnected, or improperly sized ducts restrict airflow without any obvious external sign.

## Step-by-Step Diagnosis {#fix}

1. **Wait for the furnace to auto-reset if needed** — If code 13 is showing right now and the furnace is in lockout, you can either wait 3 hours for the auto-reset or turn the furnace off at the breaker for 30 seconds, then back on. The lockout clears on power cycle as well.

2. **Replace the air filter immediately** — This is the mandatory first step. Pull the filter. If it's dirty, replace it. A clogged filter is the cause of code 13 in the vast majority of residential cases. Don't skip this step.

3. **Open all supply and return vents** — Walk every room and confirm every register is fully open. Closing off too many registers creates the same overheating condition as a dirty filter.

4. **Confirm the blower runs** — With the filter replaced and the furnace restarted, confirm the indoor blower starts within 30–60 seconds of the burner igniting. If the blower doesn't start, or starts slowly, that's your problem.

5. **Let the furnace run through a full cycle** — Watch it start, run, and shut off cleanly. If it runs to temperature and shuts off normally (not on a limit trip), the filter replacement may have solved it. Monitor for 24 hours.

6. **Test the blower motor and capacitor** — If the blower sounds slow or labored, the run capacitor is a likely culprit. It's a cylindrical component in the blower compartment, usually $10–20. A bulging or leaking capacitor needs immediate replacement.

7. **Test the high limit switch** — If the furnace trips again even with a clean filter and all vents open, the limit switch itself may be faulty. Power off, pull the 2-wire harness, test with a multimeter for continuity when cold (should be closed). An open reading at room temperature = failed switch.

## How to Fix It

**Dirty filter (most likely):** Replace with the correct size and MERV rating. Check it monthly. Set a reminder. This is the most preventable furnace failure there is.

**Blower capacitor failure:** Discharge the capacitor before handling (short the terminals with an insulated screwdriver or resistor). Replace with an exact match on µF rating and voltage rating. A $15 capacitor can restore full blower performance.

**Blower motor failure:** Test motor windings for continuity — open windings indicate a failed motor. Match HP, RPM, voltage, and shaft size for the replacement.

**Faulty high limit switch:** With power off, disconnect the limit switch, test with a multimeter. Replace if it reads open at room temperature. Match the temperature rating stamped on the body (common: 190°F, 200°F, 210°F).

**Ductwork issues:** Collapsed ducts are usually in unconditioned spaces (attics, crawlspaces). Have an HVAC technician inspect and repair the duct system if you suspect this.

## Parts You May Need

| Part | Notes |
|------|-------|
| [Furnace Air Filter](https://www.amazon.com/dp/B0CLBFXLYJ?ascsubtag=ecf-carrier-error-code-13&tag=errorcodefixes-20) | Always start here — check size on existing filter frame |
| [Carrier High Limit Switch](https://www.amazon.com/dp/B0BN3TRG9R?ascsubtag=ecf-carrier-error-code-13&tag=errorcodefixes-20) | Match temperature rating stamped on switch body |
| [Furnace Blower Motor Capacitor](https://www.amazon.com/s?ascsubtag=ecf-carrier-error-code-13&k=furnace+blower+motor+capacitor&tag=errorcodefixes-20) | Match µF and VAC rating exactly |
| [Carrier Furnace Blower Motor](https://www.amazon.com/s?ascsubtag=ecf-carrier-error-code-13&k=carrier+furnace+blower+motor&tag=errorcodefixes-20) | Match HP, RPM, voltage; direct-drive vs belt-drive varies |
| [Carrier Control Board](https://www.amazon.com/dp/B0CNZGZ1HS?ascsubtag=ecf-carrier-error-code-13&tag=errorcodefixes-20) | Last resort if board is misreading limit circuit signals |

## The 3-Hour Auto-Reset — Why People Get Fooled

Code 13 creates a frustrating cycle: furnace stops, you see the code, you can't get heat, you wait or search online, and a few hours later it just... starts working again. You assume you fixed it by power cycling it or that it was a fluke. But code 13 came back because the high limit switch tripped **repeatedly** — meaning the underlying overheating condition is real. The next cold night, it trips again.

Don't let the auto-reset fool you into thinking it's resolved. Fix the filter, fix the airflow, fix the blower — and code 13 won't come back.

## When to Call a Technician

If you've replaced the air filter, confirmed all vents are open, replaced the limit switch, and the furnace still goes into code 13 lockout — call a technician. Persistent overheating can crack the heat exchanger over time, which is a serious safety hazard (carbon monoxide). A tech can measure temperature rise across the heat exchanger, assess ductwork sizing, and catch a cracked exchanger before it becomes dangerous.

## Related Error Codes

- [Carrier Furnace Error Code 33 — Flame Rollout & High Limit Switch Fix](/posts/carrier-error-code-33/)
- [Carrier Furnace Error Code 31 — Pressure Switch Open Fix](/posts/carrier-error-code-31/)
