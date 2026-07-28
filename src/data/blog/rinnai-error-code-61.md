---
title: "Rinnai Error Code 61 — Causes & Fix"
description: "What Rinnai error code 61 means, why the combustion fan faults, and how to fix it step by step."
pubDatetime: 2026-04-22T12:00:00Z
modDatetime: 2026-04-22T12:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - boiler
  - rinnai
money_part: "Combustion fan assembly"
most_likely_cause: "Failed combustion fan motor"
---

## What this code means
Rinnai error code 61 indicates a **combustion fan (inducer) fault** — the unit's PCB commanded the fan to start but didn't receive the expected speed feedback (typically via a Hall effect sensor in the motor) within the startup window. The combustion fan must prove adequate airflow before the gas valve opens for ignition; without confirmed fan operation, code 61 locks out the unit to prevent unsafe combustion or gas accumulation. This is one of the more common Rinnai fault codes on units over 5 years old.

## Common Causes

- **Failed combustion fan motor** — Bearing wear is the most common cause; the fan turns slowly or not at all and the Hall sensor reports no speed feedback.
- **Wiring fault to the fan** — A loose or damaged wire to the motor or the Hall sensor circuit prevents the board from seeing the speed signal.
- **Blocked fan or flue restriction** — Debris lodged in the fan housing prevents the impeller from reaching operating speed.
- **PCB fan output failure** — The board's fan driver circuit fails and doesn't send proper drive voltage to the motor.

## Step-by-Step Fix {#fix}

1. **Listen during startup** — When calling for hot water, the combustion fan should spin up audibly within a few seconds. Silence or sluggish spin points directly to the fan or its power supply.
2. **Check the fan for obstructions** — With power off, open the unit and inspect the fan housing for debris. Try to spin the impeller by hand — it should spin freely and quietly.
3. **Check wiring to the fan** — Inspect the motor connector and the Hall sensor connector for loose pins or corrosion. Reseat both connectors firmly.
4. **Test fan supply voltage** — With the unit calling for hot water and the PCB attempting to start the fan, measure voltage at the fan power connector. Presence of correct voltage (typically 100–120V or DC depending on model) with no fan spin = failed motor.
5. **Test Hall sensor continuity** — The Hall sensor provides a pulsed signal as the fan spins. With power applied and the fan running (if you can get it to spin manually), check for a pulsing voltage at the Hall sensor output wire.
6. **Replace the combustion fan** — Rinnai fans are model-specific. Match the part number to your unit's model label. Replace the fan assembly completely, including the motor and impeller.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Combustion fan assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-rinnai-error-code-61&k=Combustion+fan+assembly&tag=errorcodefixes-20) \| Rinnai model-specific; do not substitute — RPM and CFM specs must match |
| Hall sensor (if separate) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-rinnai-error-code-61&k=Hall+sensor+%28if+separate%29&tag=errorcodefixes-20) \| On some models the Hall sensor is replaceable independent of the motor |
| PCB (main control board) | [Amazon](https://www.amazon.com/s?k=PCB+%28main+control+board%29&tag=errorcodefixes-20) \| Only if fan supply voltage is confirmed absent at the board output |
## When to Call a Pro

Combustion fan replacement on Rinnai units requires working near the gas valve and burner assembly. If you're not comfortable with gas appliance service, have a Rinnai-certified technician handle the repair. Always verify gas is off before opening the combustion chamber.
