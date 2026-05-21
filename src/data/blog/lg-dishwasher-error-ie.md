---
title: "LG Dishwasher Error IE — Water Inlet Fix"
description: "LG dishwasher error IE means the control board started a wash cycle and opened the water inlet valve, but didn't see the sump fill to the correct level..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Industrial Error Code Fixes"
slug: lg-dishwasher-error-ie
featured: false
draft: false
tags:
  - lg
  - water-inlet-failure
  - troubleshooting
---
## Quick answer

LG dishwasher error IE means the control board started a wash cycle and opened the water inlet valve, but didn't see the sump fill to the correct level within the watch window (typically 8-12 minutes). About 40% of these in the field are restricted inlet filters or kinked supply lines reducing fill rate, not a failed valve or sensor. Inspect the inlet hose and the inline screen at the valve before swapping parts.

## What IE means on an LG dishwasher

LG dishwashers (LDF, LDP, LDT, LDS series, and the newer QuadWash and TrueSteam units) measure sump fill level with either a pressure-sensing fill switch (older models) or an integrated optical/conductive sensor in the sump (newer models). At the start of a wash cycle, the board opens the water inlet solenoid valve (24V coil) and starts a fill timer. When the sensor reports fill complete (typically 1.0-1.5 liters depending on the cycle), the board closes the valve and starts the wash pump. If the fill never completes within 8-12 minutes, the board cancels the cycle, drains residual water, and posts IE.

The water inlet valve on an LG dishwasher is a simple solenoid with a flow restrictor designed to deliver 1.0-1.2 GPM at 30-120 psi inlet pressure. Behind the flow restrictor is a 60-mesh inline screen that traps sediment from the household supply. Over years of service, this screen can clog with calcium scale, rust particles from old pipes, or sediment after city water work — the result is severely reduced flow rate, slow fill, and eventual IE timeout.

QuadWash models (LDF, LDT series post-2017) add a flow meter in series with the valve. These models can detect not just "no fill" but also "slow fill" — and the IE code can fire even on a unit that's filling, if the flow rate falls below threshold.

## Common causes (ranked by frequency)

In LG dishwasher service experience:

1. **Clogged inline inlet screen at the valve** — about 30%. The 60-mesh screen behind the valve inlet has accumulated scale and sediment.
2. **Kinked or pinched water supply line** — about 18%. The 3/8-inch braided supply line crushed under the cabinet during install or by storage of cleaning supplies under the sink.
3. **Failed water inlet valve solenoid** — about 15%. Coil open, valve stuck closed, valve stuck partially open (slow fill that times out).
4. **Closed or partially-closed shutoff valve at the wall** — about 10%. Often missed because the homeowner doesn't know there's a stop valve.
5. **Failed sump fill sensor or pressure switch** — about 10%. Water is filling fine but the sensor doesn't report it.
6. **Float switch stuck open by debris in the sump** — about 8%. The float can't rise; sensor never sees fill complete.
7. **Main control PCB fault (rare)** — about 5%. Board's valve driver or sensor input failed.
8. **Wrong inlet hose washer or missing screen reinstalled after a prior valve change** — about 4%. Common after DIY repairs.

**Pro nugget:** LG dishwashers use the 5220FR series water inlet valves (5220FR2006H most common on older units, 5221DD1003E on QuadWash). Both have an integrated 60-mesh screen *and* an integrated flow restrictor that's matched to the valve's flow path. Generic universal dishwasher valves typically deliver 1.5-2.0 GPM — way over LG's designed 1.0-1.2 GPM. Installing a universal valve gets the fill faster initially but causes the board's flow timing logic to misread fill complete, and you'll get inconsistent wash performance (cycle ends with food still on dishes) without a hard fault. Always use the LG-spec valve; the flow restrictor calibration matters.

## Step-by-step fix

Before you start: shut off water at the wall valve under the sink, and disconnect power at the breaker (LG dishwashers are typically hardwired).

1. **Confirm the code.** Display reads "IE" or "1E" on newer models. On Smart Diagnosis-equipped units, hold the diagnostic button against a phone running ThinQ to decode any subcategory.

2. **Verify the supply.** Open the wall valve fully (turn counter-clockwise until it stops). Disconnect the supply line at the dishwasher inlet. Hold the end of the line in a bucket and have someone open the valve for 5 seconds. You should get roughly a gallon — vigorous flow. If flow is weak, the wall valve is bad, the supply pipe is partially closed (saddle valves are notorious), or the house has low water pressure.

3. **Inspect the inline screen.** With the supply disconnected, look into the dishwasher inlet (where the supply hose threads on). You should see a small mesh screen — pull it out with needle-nose pliers if needed. Rinse it under the tap. If it's packed with scale or sediment, soak it in CLR or vinegar for 30 minutes, then re-install.

4. **Inspect the supply hose.** Pull the hose out of the cabinet, check for kinks (any bend tighter than 4-inch radius is too tight), check for crushing. Replace with a fresh braided supply line if you see damage. Cost is $12-20 for a quality stainless braided line.

5. **Test the inlet valve solenoid.** With power restored and the supply line disconnected, find the inlet valve at the lower left of the dishwasher (remove the kick panel and the side trim). Ohm-test the solenoid coil — typically 800-1200 ohms for an LG valve. Open coil (OL) means a dead solenoid. Briefly energize the valve with 24V from a bench supply or with the dishwasher in service test mode — water should flow.

6. **Check the float switch.** Remove the dishwasher's lower spray arm and rinse cup. Look at the bottom of the tub — there's a small plastic float (about 1-1.5 inches tall, typically white or red). The float should move freely up and down. Lift it manually. Underneath the tub is a microswitch that's actuated by the float — when the float is up, the switch should be closed (low ohms on a meter). Stuck float means food debris jammed it; clean and re-test.

7. **Enter service test mode.** LG dishwashers have a hidden service test mode — typically hold the Power button + Delay Start for 5 seconds (varies by model — check the service manual). Service mode lets you energize the inlet valve directly, run the pumps independently, and step through fault history.

8. **Run a test fill.** With everything reassembled, restore power and water. Start a Rinse Only cycle. The valve should open within 30 seconds, water should flow visibly into the sump (you can see it through the lower spray arm), and the cycle should advance to the wash phase within 1-2 minutes. If IE returns, the valve is still partially blocked or the sensor isn't reporting fill.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Water inlet valve (older LDF series) | LG 5220FR2006H | $45-85 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| Water inlet valve (QuadWash) | LG 5221DD1003E | $65-115 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| Float switch assembly | LG 6601EL3001A | $35-65 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| Inlet hose (3/8" braided stainless) | Generic / Camco | $12-20 | [Home Depot](https://www.homedepot.com), [Amazon](https://www.amazon.com) |
| Inline filter screen | LG 5006DD1001E | $8-15 | [RepairClinic](https://www.repairclinic.com) |
| Sump assembly with sensor (QuadWash) | LG AJU72992604 | $185-285 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| Main control PCB | LG EBR-series (model-specific) | $145-285 | [RepairClinic](https://www.repairclinic.com) |

The LG 5220FR2006H valve is a workhorse — fits dozens of LDF, LDS, LDP models from 2008-2017. Confirm model fit before ordering.

## When to call a professional

Call an appliance tech when:

- You've cleared the inlet, replaced the valve, and IE returns. The next suspects are the flow meter (QuadWash) or main PCB — both require model-specific parts and diagnostic procedures.
- You see water leaking under the dishwasher. Independent of IE, this points to a tub crack, pump seal failure, or door gasket — needs immediate attention.
- The cycle starts but the dishwasher fills continuously without IE — water keeps coming until you abort. The valve is stuck open or the float switch failed in the "low" position. This is potentially flood-causing; isolate water immediately.
- The unit is under LG warranty (1 year parts, 10 years on the direct-drive motor on Inverter Direct Drive models).

## FAQs

**Will an inline water filter fix IE permanently?**
A pre-filter on the dishwasher supply reduces sediment accumulation on the inline screen — a good preventive measure on hard-water households. It doesn't fix a current IE, but it prevents recurrence.

**Can I clean the inlet screen instead of replacing the valve?**
Yes, if the screen is just dirty. Pull it, soak in CLR or white vinegar for 30 minutes, rinse, reinstall. If the screen is damaged (torn mesh) or if scale has eaten into the valve body, replace the whole valve.

**My LG ran fine for years and just started throwing IE. What changed?**
Likely either (a) the city did work on the water main and stirred up sediment that clogged your screen, (b) the inline screen accumulated enough scale over years to finally restrict flow below threshold, or (c) the valve solenoid is starting to fail and is partially closed.

**Will softened water prevent IE?**
Softened water reduces calcium scale accumulation on the inlet screen but introduces sodium that can corrode the valve solenoid faster. Net effect is roughly neutral on IE frequency — but softened water dramatically improves wash quality.

**Difference between IE and OE?**
IE = inlet error (not filling). OE = outlet error (not draining). Different fault paths and different parts. If you see OE, check the drain pump and drain hose.

## Related guides

- [LG Washer Error LE — Motor Lock Fix](/posts/lg-washer-error-le)
- [LG Refrigerator Error ER RF — Evap Fan Motor Fix](/posts/lg-refrigerator-error-er-rf)
- [GE Dishwasher Error Code LC — Leak Detected Fix](/posts/ge-dishwasher-error-code-lc)
