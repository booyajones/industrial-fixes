---
title: "York Affinity Error Codes - What It Means and How to Fix It"
description: "Full York Affinity furnace and heat pump error code guide covering all flash codes for the YP9C, TG9S, TG9Y, and Affinity series. Find your code and fix it step by step."
pubDatetime: 2026-04-25T00:00:00Z
author: "Marcus Webb"
tags:
  - hvac
  - error-codes
---

York Affinity is York's premium residential product line, covering high-efficiency furnaces (96%+ AFUE) and heat pumps. The Affinity series includes models like the TG9S, YP9C, YZF, and YZV. Like most modern HVAC equipment, these units use a diagnostic LED to report fault codes when something goes wrong. This guide covers the full flash code library for York Affinity furnaces and the most common heat pump codes.

## What Does York Affinity Error Codes Mean?

For York Affinity furnaces, there's a small status LED visible through the sight glass on the furnace door panel. It blinks a two-digit code: count the short blinks (first digit), wait for the pause, then count the longer blinks (second digit). The pattern repeats continuously until the fault clears.

On communicating Affinity systems (matched with a York Latitude or Affinity thermostat), the thermostat screen shows the fault code directly — no counting required.

### York Affinity Furnace Flash Code Table

| Code | Fault Description | Urgency |
|------|-------------------|---------|
| 1-1 | Normal — no call for heat | None |
| 1-2 | Normal — heating | None |
| 2-1 | Pressure switch stuck open | High |
| 2-2 | Pressure switch stuck closed | Medium |
| 2-3 | Secondary pressure switch stuck open | High |
| 2-4 | Secondary pressure switch stuck closed | Medium |
| 3-1 | Primary limit switch open | High |
| 3-2 | Secondary limit / rollout switch open | Critical |
| 3-3 | Draft inducer motor fault | High |
| 3-4 | Blower motor fault | High |
| 4-1 | Ignition failure — lockout | High |
| 4-2 | Flame sensor fault | Medium |
| 4-3 | Flame detected with valve closed | Critical |
| 5-1 | Gas valve 1 circuit fault | High |
| 5-2 | Gas valve 2 circuit fault | High |
| 6-1 | Low flame signal | Medium |
| 6-2 | Communication error | Medium |
| 7-1 | Control board fault | Critical |

### Code 2-1 — Pressure Switch Stuck Open

The pressure switch monitors draft (negative pressure created by the inducer motor). When it reads open, the furnace won't fire because it can't confirm safe venting conditions.

**Walk through in order:**
1. Listen for the inducer motor — it should spin up within a few seconds of a heat call. If you hear nothing, check power to the inducer.
2. Find the small rubber hose running from the inducer housing to the pressure switch. Disconnect it and blow through it. If clogged (common on 90%+ models with condensate), clear it.
3. Check the condensate trap — a clogged trap builds up water in the inducer housing, blocking the pressure tap.
4. If the inducer runs and the hose is clear, test the pressure switch for continuity when the inducer is running.

### Code 3-1 — Primary Limit Switch Open

Overheating. The heat exchanger surface temperature exceeded the limit (typically 140°F–170°F on Affinity furnaces). **Check the filter first.** A clogged filter is the cause in more than half of 3-1 codes.

After filter replacement: check that every supply register in the house is open, verify the return air system isn't undersized or blocked, and confirm the blower wheel is clean.

### Code 3-2 — Rollout Switch Open

Flames escaped the combustion chamber. This is a safety shutdown that demands investigation before restarting. Press the red manual reset button on the rollout switch (located near the burners). If it trips again within a heating cycle, do not restart — a cracked heat exchanger or blocked flue is likely.

### Code 4-1 — Ignition Failure Lockout

The furnace tried to ignite three times and gave up. Possible causes:
- No gas (check gas supply valve, meter, other gas appliances)
- Failed hot surface igniter (should glow bright orange-white within 17 seconds)
- Dirty flame sensor
- Low gas pressure

Test the igniter by measuring its resistance (should read 40–90 ohms on most York Affinity igniters). Infinite resistance = cracked igniter.

### Code 4-3 — Flame Detected with Valve Closed

The flame sensor is detecting a flame when the gas valve should be closed. This is either a shorted flame sensor, a faulty control board, or (rarely) a gas valve leaking through. Turn off gas and call a technician.

### Code 7-1 — Control Board Fault

The control board has detected an internal fault. Try cycling power at the disconnect for 30 seconds. If the code returns immediately, the board needs replacement. York Affinity boards are model-specific — always verify the part number on the existing board before ordering.

## How to Fix It

1. **Identify the code.** Two-digit blink pattern. Write it down before anything else.
2. **Check the filter.** Before spending money on parts, install a fresh filter. Responsible for a significant percentage of all furnace calls.
3. **Reset the fault.** Thermostat to OFF, wait 30 seconds, restore. A transient fault may clear.
4. **Inspect the inducer and pressure switch hose** for any 2-x code. Hose clogs are the single most common York Affinity service call on 90%+ models.
5. **Clean the flame sensor.** For 4-2 or 6-1 codes, remove the flame sensor rod and clean the metal tip with fine sandpaper. Takes 5 minutes and costs nothing.
6. **Test the igniter.** Measure resistance with the furnace powered off. Replace if it reads out of spec or shows any cracking.
7. **Check limit switch continuity.** A failed limit switch can read open even when the heat exchanger is cold. Test with a multimeter for continuity — it should have continuity when cold.
8. **For 3-2 (rollout):** After pressing the manual reset, closely watch the burner flames through the sight glass on the next heating cycle. Flames should stay inside the heat exchanger. If they roll toward the door, stop the furnace.

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|-------------|
| Hot surface igniter (York S1-02528326000) | Fixes Code 4-1 ignition failure | $25–$50 — [Search on Amazon](https://www.amazon.com/dp/B00BTLLJ40?tag=errorcodefixes-20) |
| Flame sensor (universal 1/4" rod) | Fixes Code 4-2 flame sense fault | $10–$20 — [Search on Amazon](https://www.amazon.com/dp/B0CZ7M9V4D?tag=errorcodefixes-20) |
| Draft inducer motor (York S1-02435625000) | Fixes Code 3-3 inducer fault | $120–$280 — [Search on Amazon](https://www.amazon.com/dp/B00FDZ90B2?tag=errorcodefixes-20) |
| Pressure switch (York S1-02528333000) | Fixes Code 2-1 when hose is clear | $20–$45 — [Search on Amazon](https://www.amazon.com/dp/B013J2J97A?tag=errorcodefixes-20) |
| High limit switch (York S1-02535710000) | Fixes Code 3-1 when limit is failed | $20–$40 — [Search on Amazon](https://www.amazon.com/dp/B0BN3TRG9R?tag=errorcodefixes-20) |
| Control board (York S1-33102956000) | Fixes Code 7-1 board fault | $150–$350 — [Search on Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?tag=errorcodefixes-20) |

## When to Call a Pro

- **Code 3-2 (rollout)** — Any rollout condition warrants a professional inspection of the heat exchanger and flue system before you run the furnace again.
- **Code 4-3 (flame with valve closed)** — Gas valve issues require immediate attention and EPA-certified technician work.
- **Code 7-1 (control board)** if power cycling doesn't clear it — board replacement on Affinity systems can be complicated due to model-specific firmware.
- The furnace runs for 2–3 minutes then shuts off with a limit fault and never fully heats the house (cycling high-limit, heat exchanger stress).
- Any gas odor near the furnace — leave the home and call the gas company.

## Frequently Asked Questions

**Q: My York Affinity TG9S is showing a 2-1 code every winter but fine the rest of the year. Why is it seasonal?**

A: This is classic condensate trap blockage. 90%+ furnaces produce water as a byproduct of combustion. In winter, with the furnace running constantly, the condensate drain path can partially freeze or develop a biofilm blockage. The water backs up into the inducer housing, blocking the pressure tap port, and the switch trips. Flush the condensate trap and drain line each fall before heating season.

**Q: Can I use an aftermarket control board on a York Affinity furnace?**

A: Technically yes, but be careful. York Affinity boards are not universal — they match specific motor configurations and gas valve types. Using a generic board often requires re-wiring and may disable safety features. Source an OEM replacement board using the part number from your existing board. Used boards from eBay can work but come with obvious risks.

**Q: The York Affinity furnace blinks 3-4 (blower motor fault). The blower runs fine in cooling mode. What's different in heating?**

A: In heating mode, the blower typically runs at a different speed tap than in cooling. A failed speed tap on an ECM (variable speed) blower motor can cause the blower to work on one speed setting but fail on another. Have a tech test the motor's full speed range. On older PSC motors, a failed capacitor (which is speed-specific) can cause the same issue.

**Q: York Affinity showing code 6-1 (low flame signal) and the flame sensor is brand new. What else could cause this?**

A: Ground path. The flame sensor works by passing a small current through the flame — the current only completes if the burner has a solid chassis ground. Check that the burner itself has good metal-to-metal contact with the furnace casing. A corroded or painted-over ground connection will cause low flame signal even with a new sensor. Also check gas pressure — low supply pressure produces a smaller flame that's harder to sense.

**Q: How long should a York Affinity furnace last?**

A: With annual maintenance (filter changes, cleaning, safety checks), a York Affinity can last 20–25 years. The heat exchanger typically outlasts other components. The most common age-related failures are the igniter (every 5–10 years), the inducer motor (10–15 years), and the control board (10–15 years). None of these are reasons to replace the whole system.

## Related Articles

- [York 2 Flashes Error Code — Causes & Fix](/posts/york-2-flashes-error-code/)
- [York 3 Flashes Error Code — Causes & Fix](/posts/york-3-flashes-error-code/)
- [York 4 Flashes Error Code — Open Limit Device Fix](/posts/york-4-flashes-error-code/)
- [York 5 Flashes Error Code — Causes & Fix](/posts/york-5-flashes-error-code/)
- [York Furnace 6 Flashes Error Code — Pressure Switch Fault Fix](/posts/york-6-flashes-pressure-switch-fault/)
