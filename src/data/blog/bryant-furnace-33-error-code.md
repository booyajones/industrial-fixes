---
title: "Bryant Furnace 33 Error Code — Limit Device Lockout"
description: "What the Bryant furnace 33 error code means, why the limit switch trips, and how to fix it step by step."
pubDatetime: 2026-04-22T14:00:00Z
modDatetime: 2026-04-22T14:00:00Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - hvac
  - bryant
money_part: "Air filter"
most_likely_cause: "Restricted airflow - dirty filter"
---

## What this code means
On Bryant furnaces, error code 33 indicates a limit device fault — the high-limit switch, rollout switch, or auxiliary limit has opened during operation. These are thermal safety devices. The primary high-limit switch is mounted on the heat exchanger plenum and opens when the plenum temperature exceeds a safe threshold (typically 180–200°F). When any limit device opens while the burners are firing, the control board immediately shuts the gas valve, logs fault 33, and blinks the status LED 33 times. Repeated limit trips eventually cause a hard lockout that requires manual reset.

## Common Causes

- **Restricted airflow — dirty filter** — The single most common cause of fault 33. A clogged air filter starves the heat exchanger of return air, causing plenum temperatures to spike until the high-limit trips. Check this first, always.
- **Blocked or closed supply/return registers** — Too many closed registers increases static pressure, reduces airflow, and causes the same overheating pattern as a dirty filter.
- **Failed blower motor or capacitor** — If the indoor blower isn't running or runs slowly, heat builds in the heat exchanger with no airflow to remove it. The blower should start 30–60 seconds into the heat cycle.
- **Dirty evaporator coil (summer buildup)** — A heavily fouled evaporator coil downstream of the furnace restricts airflow across the heat exchanger, causing the same overheating as a dirty filter.
- **Rollout switch tripped** — The rollout switches are mounted around the burner compartment and trip if flame rolls out of the burners (indicating a cracked heat exchanger or blocked flue). A tripped rollout switch must be investigated before manual reset.
- **Faulty limit switch** — A limit switch that trips below its rated temperature (due to age or physical damage) produces nuisance 33 faults even with good airflow.

## Step-by-Step Fix {#fix}

1. **Check and replace the air filter** — Power down the furnace and inspect the filter. A filter so clogged it holds its shape when removed is the problem. Replace with a clean filter of the same MERV rating. Do not upsize to a higher MERV filter unless the system was designed for it — high-MERV filters restrict more airflow.
2. **Verify all registers are open** — Walk the house and confirm all supply and return registers are open and unobstructed. Move furniture away from floor registers.
3. **Check blower operation** — With the furnace running in fan-only mode (turn fan to ON at the thermostat), confirm the blower starts and runs at full speed. A slow or non-starting blower needs its capacitor tested (run capacitor, typically 5–10 µF).
4. **Check the rollout switches** — Locate the rollout switches around the burner assembly (they look like small round buttons with a reset button on top). Press the reset button on any that have tripped. Rollout switch trips are serious — investigate the cause before restarting.
5. **Inspect the high-limit switch** — With power off, locate the high-limit switch (usually mounted on the supply plenum above the heat exchanger). Test continuity across the limit terminals; it should show closed (continuity) at room temperature. If it's open at room temperature, it's failed and needs replacement.
6. **Clean the evaporator coil** — If the coil is visibly blocked with dust and debris, clean it with a no-rinse coil cleaner. This is especially important if the 33 fault started appearing after summer AC use.
7. **Reset and monitor** — After repairs, run a full heat cycle and monitor the fault indicator. Fault 33 should not recur with adequate airflow restored.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Air filter | [Amazon](https://www.amazon.com/dp/B0CLBFXLYJ?ascsubtag=ecf-bryant-furnace-33-error-code&tag=errorcodefixes-20) \| Replace every 1–3 months; most 33 faults are dirty-filter faults |
| Blower motor run capacitor | [Amazon](https://www.amazon.com/dp/B01M05L7B3?ascsubtag=ecf-bryant-furnace-33-error-code&tag=errorcodefixes-20) \| Test before replacing motor — most blower motor failures are capacitor failures |
| High-limit switch | [Amazon](https://www.amazon.com/dp/B0BN3TRG9R?ascsubtag=ecf-bryant-furnace-33-error-code&tag=errorcodefixes-20) \| Match rated temperature from original switch body |
| Rollout switch | [Amazon](https://www.amazon.com/dp/B0BN3TRG9R?ascsubtag=ecf-bryant-furnace-33-error-code&tag=errorcodefixes-20) \| Replace after investigating the root cause of the rollout event |
| Blower motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-bryant-furnace-33-error-code&k=Blower+motor&tag=errorcodefixes-20) \| Replace if motor is seized or draws excessive amps with good capacitor |
## When to Call a Pro

A tripped rollout switch is never a nuisance fault — it means flame exited the burner box, which only happens with a blocked flue or a cracked heat exchanger. Both are serious safety issues. Have a licensed HVAC technician perform a combustion analysis and heat exchanger inspection before restarting the furnace after a rollout event.
