---
title: "York Furnace E4 Error Code — Ignition Failure"
description: "What the York furnace E4 error code means, why ignition fails, and how to fix it step by step."
pubDatetime: 2026-04-22T14:00:00Z
modDatetime: 2026-04-22T14:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - york
money_part: "Hot surface ignitor"
most_likely_cause: "Dirty or failed hot surface ignitor (HSI)"
---

## What this code means
On York furnaces with LED display panels (YP9C, TM9V, and related models), E4 indicates an ignition failure — the control board attempted to light the burners, but no flame was detected within the trial-for-ignition period. After typically three failed ignition attempts, the board locks out and displays E4. This is a safety lock that prevents unburned gas from accumulating. The furnace will remain locked out until the fault is cleared.

## Common Causes

- **Dirty or failed hot surface ignitor (HSI)** — The silicon nitride or silicon carbide ignitor is the most common E4 cause. It glows orange-hot to light the gas; a cracked ignitor won't heat enough, and a film-coated ignitor won't reach ignition temperature in time.
- **Weak or no gas pressure** — If the gas valve opens but pressure at the manifold is below the minimum (typically 3.5" W.C. for natural gas), the burner flame may be too small to detect.
- **Faulty gas valve** — The gas valve solenoid may be receiving 24VAC but not opening fully — or at all. Internal valve failure, though less common than ignitor failure, produces the same E4 result.
- **Failed flame sensor (dirty or cracked)** — Even if ignition occurs, a contaminated flame sensor won't detect the flame and will cause the board to shut down the gas valve, logging E4. The microamp signal from a dirty sensor is too low for the board to accept.
- **Incorrect gas type or pressure** — A furnace set up for natural gas but receiving propane (or vice versa), or a gas supply pressure outside the operating range, will fail to sustain ignition.

## Step-by-Step Fix {#fix}

1. **Reset the lockout** — Turn the thermostat off, wait 30 seconds, and restore the call for heat. If the lockout is temporary (power interruption, momentary low gas pressure), the furnace will attempt ignition again.
2. **Inspect the hot surface ignitor** — With power off and the furnace cool, locate the ignitor in the burner assembly. Visually inspect for cracks — even a hairline crack will prevent it from reaching ignition temperature. If cracked, replace it. Handle only by the ceramic base; skin oils on the element shorten its life.
3. **Test the ignitor** — With power on but a call for heat initiated, watch the ignitor during the pre-ignition period. It should glow bright orange within 20–30 seconds. A dull red glow means it's failing. Measure resistance with an ohmmeter when cold — most HSIs read 40–75 ohms; an open circuit (OL) means it's dead.
4. **Clean or replace the flame sensor** — The flame sensor is a metal rod in the burner flame path, connected by a single wire. Pull the wire connector, remove the sensor (one screw), and clean the rod with fine steel wool or a Scotch-Brite pad. Reinstall and test. If E4 recurs, replace the sensor.
5. **Check gas supply pressure** — With a manometer connected to the gas valve inlet tap, measure supply pressure with the furnace calling for heat. Natural gas should be 5–7" W.C.; propane 11–14" W.C. Low pressure means a supply issue (utility, regulator, or undersized piping).
6. **Test the gas valve** — Confirm 24VAC at the gas valve terminals when the board energizes it during trial for ignition. If voltage is present but no gas flows, the valve is faulty.
7. **Clear the fault** — After repairs, power cycle the furnace and verify successful ignition with steady flame.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Hot surface ignitor | [Amazon](https://www.amazon.com/dp/B00BTLLJ40?ascsubtag=ecf-york-furnace-error-code-e4&tag=errorcodefixes-20) \| Match exact part — York uses both 120V silicon carbide and 80V silicon nitride types |
| Flame sensor | [Amazon](https://www.amazon.com/s?k=Flame+sensor&tag=errorcodefixes-20) \| Universal sensors work but OEM preferred for reliability |
| Gas valve | [Amazon](https://www.amazon.com/dp/B0015KAHHA?ascsubtag=ecf-york-furnace-error-code-e4&tag=errorcodefixes-20) \| Replace only after confirming 24VAC at valve terminals with no gas flow |
| Control board | [Amazon](https://www.amazon.com/s?k=Control+board&tag=errorcodefixes-20) \| Last resort — if ignitor, sensor, and gas valve all check out |
## When to Call a Pro

Gas valve replacement requires leak-testing all connections with a manometer or soap solution. If you're not comfortable working with gas lines or you have propane (higher pressure, different hazard profile), call a licensed HVAC technician.
