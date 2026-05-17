---
title: "Carrier 13 Error Code — Limit Switch Lockout Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-03-03T08:00:00Z
modDatetime: 2024-03-03T08:00:00Z
slug: carrier-13-error-code
featured: true
draft: false
tags:
  - hvac
  - carrier
  - furnace
  - limit-switch
  - overheating
description: "Carrier error code 13 means the limit switch tripped due to overheating. This guide covers every cause and fix — from clogged filters to cracked heat exchangers."
---

## Error Code: Carrier 13

**What it means:** Code 1-3 is a limit switch lockout. The high-temperature limit switch inside the heat exchanger section tripped because the furnace sensed temperatures above the safe operating threshold (typically 200°F on the primary limit). This is a thermal safety device — when it trips, the gas valve closes but the blower continues running to cool the heat exchanger down. If the limit trips repeatedly, the board locks out with code 13.

The limit switch is doing exactly what it's designed to do. The fault is almost never the switch itself — it's whatever is causing the furnace to overheat.

## Common Causes

- **Dirty or clogged air filter** — Restricts airflow over the heat exchanger. The single most common cause. A filter that's been in place more than 90 days in a normal home can cause limit trips.
- **Blocked or closed supply/return registers** — Too many closed registers starves the system of airflow. The heat exchanger can't shed heat fast enough.
- **Failed or undersized blower motor** — A blower running at reduced speed (failed capacitor, bad winding) doesn't move enough air. The heat exchanger overheats even with a clean filter.
- **Blocked flue or restricted heat exchanger** — Scale, debris, or a bird nest in the flue pipe reduces combustion airflow and traps heat inside the exchanger.
- **Cracked heat exchanger** — A cracked exchanger disrupts airflow patterns and can cause hot spots that repeatedly trip the limit even when the blower is running correctly.
- **Limit switch out of calibration or failed open** — Rare, but older limit switches can drift low and trip at normal operating temperatures.

## Step-by-Step Fix {#step-by-step-fix}

1. **Check and replace the air filter immediately.** Pull the filter, hold it to light — if you can't see light through it, it's too dirty. Replace it now with the correct size and MERV rating (MERV 8–11 is ideal for most residential systems; MERV 13+ can restrict airflow on older furnaces).

2. **Inspect and open all supply and return registers.** Walk the home and confirm every register is open. Check for furniture blocking returns. The rule of thumb: never close more than 20% of supply registers on a forced-air system.

3. **Check blower wheel and motor operation.** Remove the blower access panel (bottom of the furnace). Inspect the blower wheel for dust buildup — a caked blower wheel can reduce airflow by 30–40%. Clean with a brush and vacuum. Check that the blower runs at full speed during operation; a humming motor that doesn't spin suggests a failed run capacitor.

4. **Test the run capacitor.** With power OFF, discharge the capacitor (short its terminals through a 20K resistor), remove it, and test with a capacitor meter. The µF reading should be within 5–10% of the value printed on the capacitor label. Outside that range = replace.

5. **Inspect the flue pipe for obstructions.** Trace the flue pipe from the furnace to the exterior and look for blockages, disconnected joints, or debris. A blocked flue prevents combustion gases from drafting and causes heat to back up into the heat exchanger.

6. **Manually reset the limit switch if needed.** Many Carrier limit switches are auto-reset — they reset when the exchanger cools down. Some older or supplemental limit switches have a manual reset button (small red or white button on the switch body). Press it firmly. If the limit requires manual reset every heat cycle, the underlying cause has not been fixed.

7. **Check the heat exchanger for cracks.** With the furnace off and cooled, insert a combustion analyzer probe into each heat exchanger cell and look for CO readings while the blower is running. Alternatively, watch for flame rollout or visible flame distortion through the sight glass during ignition. A cracked exchanger requires full replacement — do not continue operating.

8. **Verify return air temperature.** Clip a thermometer to the return air plenum. Temperature should be 55–75°F during steady-state operation. Above 80°F return air (common in homes with returns too close to the furnace) indicates system-level airflow problems.

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Typical Cost | Where to Buy |
|------|-------------|---------------|
| High-limit switch (Carrier #HH12ZB195 or equiv.) | $15–$40 | [Amazon](https://www.amazon.com/dp/B0BN3TRG9R?ascsubtag=ecf-carrier-13-error-code&tag=errorcodefixes-20) \| [Johnstone Supply](https://www.johnstonesupply.com/) |
| Blower motor run capacitor (match µF and voltage) | $10–$30 | [Amazon](https://www.amazon.com/dp/B01M05L7B3?ascsubtag=ecf-carrier-13-error-code&tag=errorcodefixes-20) \| [RepairClinic](https://www.repairclinic.com/Search/SearchResult?searchterm=blower+capacitor+carrier) |
| ECM blower motor (Carrier OEM #HC43AE116) | $200–$500 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-carrier-13-error-code&k=Carrier+HC43AE116+ECM+blower+motor&tag=errorcodefixes-20) \| [RepairClinic](https://www.repairclinic.com/Search/SearchResult?searchterm=HC43AE116) |
| Air filter (16x25x1, MERV 8) | $8–$25 | [Amazon](https://www.amazon.com/dp/B0CLBFXLYJ?ascsubtag=ecf-carrier-13-error-code&tag=errorcodefixes-20) \| [Home Depot](https://www.homedepot.com/s/16x25x1%20merv%208%20filter) |

## When to Call a Professional

If you've replaced the filter, opened all registers, confirmed the blower runs at full speed, and the furnace still trips code 13 within one or two heat cycles — stop running the furnace and call a tech. At this point the most likely culprit is a cracked heat exchanger, which is a carbon monoxide hazard. Tell the tech: "Code 13 limit lockout, filter is new, blower runs fine, still tripping. I need a combustion analysis and heat exchanger inspection."

> **Pro tip:** A limit switch that trips in the first 5 minutes of a heat cycle (not the end) almost always points to a blower problem — the heat exchanger overheats before the blower gets it up to speed. A limit that trips after 20–30 minutes of continuous running usually points to airflow restriction (dirty filter, blocked registers). The timing tells you which direction to dig.

## See Also

- [Carrier 58CVA Furnace Error Codes — Fault Code Diagnostic Guide](/posts/carrier-58cva-error-codes/)
- [Carrier Infinity System Communication Error Codes — Complete Guide](/posts/carrier-infinity-system-error-codes/)
- [Carrier 13 Soft Lockout — What's Different from Hard Lockout](/posts/carrier-13-soft-lockout/)
- [Carrier 24ACC Air Conditioner Error Codes — Fault Code Diagnostic Guide](/posts/carrier-24acc-error-codes/)

## Related Articles

- [Carrier 11 Error Code — Causes & Fix](/posts/carrier-11-error-code/)
- [Carrier 12 Error Code — Causes & Fix](/posts/carrier-12-error-code/)
- [Carrier 13 Soft Lockout — What's Different from Hard Lockout](/posts/carrier-13-soft-lockout/)
- [Carrier 14 Error Code — Causes & Fix](/posts/carrier-14-error-code/)
- [Carrier 21 Error Code — Gas Heating Lockout Fix](/posts/carrier-21-error-code/)
