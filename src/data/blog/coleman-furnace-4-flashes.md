---
title: "Coleman Furnace 4 Flashes — Open High Limit Switch Fix (Also Goodman and Amana)"
author: "Industrial Error Code Fixes"
pubDatetime: 2026-04-26T17:45:00Z
featured: false
draft: false
tags:
  - hvac
  - coleman
  - furnace
  - heating
description: "Coleman furnace 4 flashes means the high limit switch has opened due to overheating. Also applies to Goodman and Amana furnaces. Step-by-step diagnosis and fix."
---

## Coleman Furnace 4 Flashes — What It Means

A Coleman furnace flashing **4 blinks** on the LED diagnostic light means the **high limit switch has opened** — a thermal safety device tripped because the supply air or heat exchanger temperature climbed above the safe operating limit (typically 170–200°F). The furnace shuts off the burners immediately when the high limit opens, and the LED flashes 4 times repeatedly until the system is reset or the root cause is corrected.

**This fault also applies to Goodman, Amana, and York furnaces.** Coleman is part of the York/Johnson Controls family, and Goodman and Amana share the same control board logic and diagnostic flash codes through their common ownership under Daikin. If your Goodman or Amana furnace is also showing 4 flashes, this guide applies to your unit.

A clogged air filter causes 4 flashes in approximately 80% of cases. Start there before chasing any other component.

[Jump to Fix](#fix)

## Common Causes

- **Dirty or clogged air filter** — The single most common cause. A filter that hasn't been changed in 3–6 months restricts return airflow enough to cause the heat exchanger to overheat and trip the high limit. If the furnace is firing 4 flashes and the filter hasn't been changed recently, change it first.
- **Blocked supply or return air registers** — Closed supply registers in multiple rooms, furniture pushed against return grilles, or a return air duct that has collapsed internally reduces the airflow volume the furnace needs to carry away heat.
- **Failed blower motor or run capacitor** — The blower must start within 30–60 seconds of the burners lighting and run at full speed throughout the heating cycle. A failed run capacitor causes the blower to run at reduced speed or not start at all, allowing heat to build up rapidly.
- **High limit switch failure** — A limit switch that has tripped too many times can fail in the open position, causing it to trip at normal operating temperatures. A cold limit switch that reads open on a multimeter has failed.
- **Cracked heat exchanger** — A crack in the primary or secondary heat exchanger disrupts airflow dynamics and can create hot spots that trigger the limit switch repeatedly, even with good filter and blower operation. This is a serious CO safety issue.
- **Undersized ductwork or over-sized furnace** — A furnace that is oversized for the home or connected to undersized supply ductwork cannot move enough air to control heat exchanger temperature, causing chronic high limit trips.

## Step-by-Step Fix {#fix}

1. **Replace the air filter — do this first** — If you haven't changed the filter in the last 30–60 days, stop and do it before anything else. Even a filter that "doesn't look that dirty" may be restricting airflow enough to trip the high limit. Use a fresh filter of the same MERV rating — keep it at MERV 8 or lower for standard residential gas furnaces to avoid excessive static pressure.

2. **Check every supply and return register** — Walk through every room and confirm supply registers are open. Check that furniture, rugs, and curtains are not blocking any return air grilles. A house with several closed registers has the same effect on the furnace as a dirty filter.

3. **Verify blower operation** — After the burners light, the blower should come on within 30–90 seconds. Stand at a supply register — airflow should be strong and consistent. Weak or no airflow from registers despite the furnace running points to a failed blower capacitor or motor.

4. **Test the run capacitor** — Remove the blower access panel and locate the run capacitor (cylindrical or oval capacitor on the blower housing). Discharge the capacitor by shorting its terminals through a 20,000-ohm resistor. Test capacitance with a capacitor meter — compare to the rating printed on the capacitor label. A capacitor that reads more than 10% below its rated value has failed.

5. **Test the high limit switch** — Turn off power at the disconnect. With a multimeter set to continuity, place probes across the high limit switch terminals. A healthy, cool high limit switch shows continuity (closed). A switch that reads open at room temperature has failed and needs replacement. Note: the limit switch is normally closed — it opens on overtemperature.

6. **Inspect the heat exchanger** — If 4 flashes returns within one or two heating cycles after correcting the filter and blower, have a licensed HVAC technician inspect the heat exchanger. A cracked exchanger is a carbon monoxide hazard and the furnace must be taken out of service immediately if a crack is confirmed.

## Parts You May Need

| Part | Notes |
|------|-------|
| High limit switch | [Amazon](https://www.amazon.com/dp/B0BN3TRG9R?tag=errorcodefixes-20) — Replace when switch tests open at room temperature; match temperature rating (stamped on switch body) |
| Blower motor run capacitor | [Amazon](https://www.amazon.com/dp/B01M05L7B3?tag=errorcodefixes-20) — Match microfarad (µF) and voltage rating exactly; inexpensive and common failure |
| Furnace air filter (1") | [Amazon](https://www.amazon.com/dp/B0CLBFXLYJ?tag=errorcodefixes-20) — Replace every 30–60 days; keep MERV 8 or lower |
| Blower motor | [Amazon](https://www.amazon.com/s?k=coleman+furnace+blower+motor&tag=errorcodefixes-20) — Replace if capacitor is within spec but motor won't reach rated speed |

## When to Call a Technician

If 4 flashes returns after replacing the filter, confirming blower operation, and replacing a failed limit switch, the heat exchanger requires inspection. A cracked heat exchanger allows combustion gases including carbon monoxide to enter the supply air stream — this is a life-safety issue. Do not operate the furnace. Have a licensed HVAC technician perform a combustion analysis and heat exchanger inspection using a scope or combustion analyzer before the system is returned to service.

## Related Articles

- [Goodman Furnace 4 Flashes — High Limit Fault Fix](/posts/goodman-furnace-4-flashes/)
- [Goodman Furnace 3 Flashes — Pressure Switch Fault Fix](/posts/goodman-furnace-3-flashes/)
- [Goodman Furnace 2 Flashes — Causes & Fix](/posts/goodman-furnace-2-flashes/)
- [Coleman EVCON Furnace Error Codes — Complete Guide](/posts/coleman-evcon-furnace-error-codes/)
- [Coleman Furnace E2 Error Code — Causes & Fix](/posts/coleman-furnace-e2-error-code/)
