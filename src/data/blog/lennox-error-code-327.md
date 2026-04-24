---
title: "Lennox Error Code 327 — Causes & Fix"
description: "What Lennox error code 327 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T09:00:00Z
modDatetime: 2026-04-22T09:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - lennox
---

## Lennox Error Code 327 — What It Means

Lennox fault code 327 is a limit fault — the high-temperature limit switch opened during a heating cycle. The limit switch is a thermal safety device in the heat exchanger plenum or supply air compartment. It opens when heat exchanger temperatures exceed the safe threshold (typically 140–200°F depending on switch rating), then resets automatically once temperatures drop. If the limit trips repeatedly, the board logs 327 and eventually locks out. Repeated limit trips mean either airflow across the heat exchanger is inadequate, or the heat exchanger itself is running too hot.

[Jump to Fix](#fix)

## Common Causes

- **Dirty air filter** — A clogged filter restricts return airflow, causing heat to build up in the heat exchanger compartment until the limit opens. This is the most common cause by a wide margin.
- **Closed or blocked supply/return registers** — Closing too many registers in the distribution system raises static pressure and reduces airflow, same effect as a dirty filter.
- **Failed indoor blower motor** — If the blower fails to start or runs at reduced speed, heat accumulates in the plenum rapidly. Check motor capacitor and confirm motor runs at call for heat.
- **Undersized ductwork or refrigerant coil icing** — Frozen evaporator coils or excessively restrictive ductwork reduce airflow to the point where limits trip even with a clean filter and working blower.

## Step-by-Step Fix {#fix}

1. **Check and replace the filter** — Pull the filter and inspect. A grey-packed or collapsed filter is an immediate replacement. Install a fresh filter of the correct MERV rating (avoid MERV 13+ on older systems without variable-speed blowers).
2. **Verify all registers are open** — Walk the system and confirm supply and return registers are not closed, blocked by furniture, or covered by rugs.
3. **Check blower operation** — With the furnace running, confirm the indoor blower starts within 60–90 seconds of burner ignition. Put your hand near the return grille — you should feel strong suction. A slow or non-running blower requires capacitor or motor diagnosis.
4. **Inspect the evaporator coil (A/C coil)** — If installed, verify the coil above the furnace is not iced. A frozen coil in cooling season dramatically restricts airflow during subsequent heat calls.
5. **Reset and monitor** — Replace the filter, restore all registers to open, and cycle the furnace. If it runs through a full cycle without tripping the limit, airflow was the cause. If it trips again quickly, move to blower and coil diagnosis.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Air filter (1" or 4" media) | [Amazon](https://www.amazon.com/s?k=Air+filter+%281%22+or+4%22+media%29&tag=errorcodefixes-20) \| Replace on schedule; 1" filters need monthly checks in dusty environments |
| Blower motor capacitor | [Amazon](https://www.amazon.com/s?k=Blower+motor+capacitor&tag=errorcodefixes-20) \| Test capacitance before condemning the motor |
| High-limit switch | [Amazon](https://www.amazon.com/s?k=High-limit+switch&tag=errorcodefixes-20) \| Replace if it doesn't reset after the system cools down |
## When to Call a Pro

If the limit trips with a clean filter and a confirmed-running blower, the heat exchanger may be failing or the system is significantly oversized or underducted. A technician with a manometer can measure static pressure and identify whether the ductwork is the root cause.
