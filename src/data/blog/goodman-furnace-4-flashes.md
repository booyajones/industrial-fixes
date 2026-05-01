---
title: "Goodman Furnace 4 Flashes — Open High Limit Switch Fix"
description: "Goodman furnace 4 slow flashes means the high limit switch is open. Dirty filter causes 80% of cases. Step-by-step diagnosis and fix guide."
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

## Goodman Furnace 4 Flashes — What It Means

**4 slow flashes** on a Goodman furnace control board means the **high limit switch is open** — the furnace detected dangerously high temperatures in the heat exchanger and shut the burners off to prevent damage or fire. The LED on the control board blinks 4 times, pauses, then repeats.

This code also applies to **Amana furnaces** and some **Coleman furnaces** that share the same Goodman control board platform.

The high limit switch is a safety device. When it opens, it's telling you the heat exchanger got too hot — which almost always means the furnace wasn't getting enough airflow. In 80% of cases, a clogged air filter is the entire problem.

[Jump to Fix](#fix)

## Common Causes

- **Dirty or clogged air filter** — This is the #1 cause. A restricted filter chokes off airflow across the heat exchanger, temperatures spike, and the limit switch opens. Start here.
- **Blocked return or supply vents** — Too many closed registers prevents air from circulating, same effect as a dirty filter.
- **Failed blower motor** — If the indoor blower isn't running or is running slowly, heat builds up rapidly in the plenum.
- **Faulty high limit switch** — After years of cycling, limit switches can fail in the open position even when temperatures are normal.
- **Dirty evaporator coil** — A clogged A/C coil upstream of the blower restricts airflow just like a dirty filter.
- **Collapsed ductwork** — Crushed or disconnected duct sections choke return or supply airflow without any visible warning.

## Step-by-Step Diagnosis {#fix}

1. **Replace the air filter** — Pull the filter and look at it. If it's gray, brown, or visibly clogged, that's your answer. Replace it with the correct size, turn the thermostat off, wait 30 minutes for the heat exchanger to cool, then try again.

2. **Open all supply and return vents** — Walk through the house and make sure every register is fully open. Closing too many registers in unused rooms is a common mistake that triggers high-limit trips.

3. **Confirm the blower is running** — Set the thermostat fan to ON (not AUTO). The indoor blower should run continuously. If it doesn't start at all, you likely have a blower motor or capacitor issue, not a limit switch problem.

4. **Wait for reset** — The high limit switch is auto-reset on most Goodman models. Once the heat exchanger cools (15–30 minutes with airflow restored), it closes on its own. If the furnace fires up and runs fine after a filter change and cool-down, you're done.

5. **Test the limit switch** — Power the furnace off at the breaker. Locate the limit switch — it's mounted on the plenum above the heat exchanger, usually round or rectangular with 2 wires. Use a multimeter set to continuity. A good (closed) switch reads near 0Ω. If it reads open (infinite resistance) when cold, the switch has failed and needs replacement.

6. **Check the blower motor and capacitor** — If the blower is slow or struggling, the run capacitor may have failed. Capacitors are inexpensive and a common failure point on older blower motors. A bulging or leaking capacitor is a clear sign of failure.

7. **Inspect the evaporator coil** — If you have central air conditioning, the evaporator coil sits in the air handler above the furnace. A visibly iced-over or dirty coil will block airflow. This requires a professional to clean safely.

## How to Fix It

**Dirty filter:** Replace immediately. Use a filter with the MERV rating your system was designed for — higher MERV isn't always better and can actually restrict airflow on lower-capacity systems.

**Failed high limit switch:** Disconnect power, pull the 2-wire harness off the limit switch, use a multimeter to confirm it's failed open, then swap in a replacement. Match the temperature rating stamped on the switch body (common ratings: 130°F, 150°F, 170°F, 190°F, 200°F).

**Failed blower capacitor:** The run capacitor is usually a cylindrical component in the blower compartment. Discharge it before handling (short the terminals with an insulated screwdriver), then replace with the same µF and voltage rating.

**Blower motor failure:** If the capacitor tests good and the motor still won't run, test the motor windings for continuity. An open winding means the motor needs replacement. Match HP, voltage, RPM, and shaft size.

## Parts You May Need

| Part | Notes |
|------|-------|
| [Furnace Air Filter](https://www.amazon.com/dp/B0CLBFXLYJ?tag=errorcodefixes-20) | Check size printed on existing filter frame |
| [Goodman High Limit Switch](https://www.amazon.com/dp/B0BN3TRG9R?tag=errorcodefixes-20) | Match temperature rating stamped on switch body |
| [Furnace Blower Motor Capacitor](https://www.amazon.com/dp/B01M05L7B3?tag=errorcodefixes-20) | Match µF and voltage rating exactly |
| [Goodman Furnace Blower Motor](https://www.amazon.com/s?k=goodman+furnace+blower+motor+replacement&tag=errorcodefixes-20) | Match HP, RPM, and voltage from motor label |
| [Goodman Control Board](https://www.amazon.com/dp/B0CNZGZ1HS?tag=errorcodefixes-20) | Last resort if board is misreading limit switch signal |

## When to Call a Technician

If you've replaced the filter, confirmed all vents are open, and the furnace still trips 4 flashes within a few minutes of running — stop operating it and call a technician. A furnace that repeatedly overheats can crack the heat exchanger, which allows carbon monoxide to leak into your home. A cracked heat exchanger requires full heat exchanger or furnace replacement — it cannot be repaired.

Also call a pro if you see any soot, burn marks, or discoloration inside the burner compartment.

## Related Flash Codes

- [Goodman Furnace 3 Flashes — Pressure Switch Open](/posts/goodman-furnace-3-flashes/)
- [Goodman Furnace 2 Flashes — Pressure Switch Stuck Closed](/posts/goodman-furnace-2-flashes/)
