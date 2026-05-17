---
title: "Carrier Furnace Error Code 33 — Flame Rollout & High Limit Switch Fix"
description: "Carrier error code 33 means flame rollout or limit circuit fault. Learn causes, step-by-step diagnosis, and how to fix it fast — dirty filter is #1."
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

## Carrier Error Code 33 — What It Means

Carrier error code 33 is a **limit circuit fault** — the furnace's high limit switch or flame rollout switch has opened, cutting off the burner to prevent overheating or fire. On most Carrier furnace control boards, code 33 displays as **3 LED flashes followed by 3 flashes** (a 3-3 blink pattern). The furnace will attempt to restart but lockout persists until the underlying cause is resolved.

This code covers two related but distinct safeties:

- **High limit switch** — trips when the heat exchanger temperature exceeds ~200°F, usually from restricted airflow
- **Flame rollout switch** — trips when flames escape the combustion area (rollout), a serious condition requiring immediate inspection

In 80% of cases, a clogged air filter is the root cause. Check that first before anything else.

[Jump to Fix](#fix)

## Common Causes

- **Dirty or clogged air filter** — Restricted airflow causes the heat exchanger to overheat and trip the high limit switch. This is by far the most common cause.
- **Blocked or closed supply/return vents** — Too many closed registers creates the same overheating condition as a dirty filter.
- **Faulty high limit switch** — The switch itself can fail in the open position, triggering code 33 even when temperatures are normal.
- **Flame rollout** — Cracked heat exchanger, blocked flue, or burner misalignment can cause flames to roll out of the combustion chamber, tripping the rollout switch.
- **Failed inducer motor** — A weak or seized inducer motor reduces combustion airflow, causing overheating.
- **Blower motor failure** — If the circulating blower isn't moving air across the heat exchanger, temperatures spike rapidly.

## Step-by-Step Diagnosis {#fix}

1. **Check the air filter first** — Pull the filter and inspect it. If it's gray and clogged, replace it immediately. A new filter resolves the majority of code 33 calls. After replacement, turn the furnace off and back on.

2. **Check all supply and return vents** — Walk the house and verify every register is open. A common mistake is closing too many vents in unused rooms, which creates backpressure and overheating.

3. **Let the furnace cool for 30 minutes** — If the high limit switch tripped due to overheating, it must cool down before it will reset. After cooling and with a clean filter installed, attempt a restart.

4. **Locate and inspect the high limit switch** — The limit switch is usually a disc-shaped or cylindrical component mounted on the heat exchanger plenum. With power off, use a multimeter set to continuity/resistance. A good limit switch reads near 0Ω (closed). An open reading (infinite resistance) when cold indicates a failed switch.

5. **Inspect for flame rollout signs** — Open the burner compartment and look for soot, scorch marks, or discoloration around the burner area or on the burner box walls. Any evidence of rollout is a serious safety issue — stop and call a technician.

6. **Check the inducer motor** — Start the furnace and listen for the inducer to spin up before ignition. A slow, grinding, or non-starting inducer causes code 33. You can confirm with amp draw testing.

7. **Inspect the flue/vent pipe** — A blocked or disconnected vent pipe prevents proper draft and can cause both overheating and rollout. Check the entire vent path from the furnace to where it exits the building.

## How to Fix It

**Dirty filter:** Replace with the correct size filter. Check it every 30–60 days going forward.

**Faulty high limit switch:** Disconnect power, remove the 2-wire connector from the switch, replace the switch. Most Carrier furnaces use a universal 190°F or 200°F limit switch — match the temperature rating on the old switch.

**Failed blower motor:** The blower motor can be tested with a multimeter for continuity across windings. If seized or open, replace the motor or the entire blower assembly.

**Flame rollout switch:** If only the rollout switch tripped (not the high limit), there may be a manual-reset button on the switch — a small red button. Press it once after the burner area has cooled completely. If it trips again immediately, do not reset it again. A cracked heat exchanger or blocked flue is the likely cause and requires professional repair.

**Inducer motor failure:** Replace the inducer motor assembly. This is a moderate DIY repair — power off, remove the vent connection, unscrew the inducer housing, swap the motor.

## Parts You May Need

| Part | Notes |
|------|-------|
| [Furnace Air Filter](https://www.amazon.com/dp/B0CLBFXLYJ?ascsubtag=ecf-carrier-error-code-33&tag=errorcodefixes-20) | Check size on existing filter label; replace every 1–3 months |
| [Furnace High Limit Switch](https://www.amazon.com/dp/B0BN3TRG9R?ascsubtag=ecf-carrier-error-code-33&tag=errorcodefixes-20) | Match temperature rating (usually 190°F or 200°F) and mounting style |
| [Flame Rollout Switch](https://www.amazon.com/dp/B0BN3TRG9R?ascsubtag=ecf-carrier-error-code-33&tag=errorcodefixes-20) | Verify amperage rating; some Carrier models use manual-reset type |
| [Furnace Inducer Motor](https://www.amazon.com/dp/B00FDZ90B2?ascsubtag=ecf-carrier-error-code-33&tag=errorcodefixes-20) | Match HP, voltage, and RPM from OEM label |
| [Furnace Blower Motor](https://www.amazon.com/s?ascsubtag=ecf-carrier-error-code-33&k=carrier+furnace+blower+motor&tag=errorcodefixes-20) | Check HP, voltage, and RPM; direct-drive vs. belt-drive varies by model |

## When to Call a Technician

If you see soot, scorch marks, or discoloration in the burner compartment — stop. This indicates actual flame rollout, which can mean a cracked heat exchanger. A cracked heat exchanger allows combustion gases (including carbon monoxide) to enter your living space. Do not run the furnace until a qualified HVAC technician has inspected and pressure-tested the heat exchanger. This is a safety emergency, not a DIY repair.

Also call a tech if code 33 returns immediately after replacing the high limit switch and filter — there's an underlying airflow or combustion problem that needs professional diagnosis.

## Related Error Codes

- [Carrier Furnace Error Code 31 — Pressure Switch Open](/posts/carrier-error-code-31/)
- [Carrier Furnace Error Code 13 — Limit Circuit Lockout](/posts/carrier-error-code-13/)
