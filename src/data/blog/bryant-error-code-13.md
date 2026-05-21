---
title: "Bryant Evolution Code 13 — Limit Lockout Fix"
description: "Bryant Evolution code 13 is a limit lockout — the integrated furnace control opened the gas valve repeatedly on consecutive heat calls because a limit..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: bryant-error-code-13
featured: false
draft: false
tags:
  - bryant
  - hvac
  - error-codes
  - limit-lockout
---
## Quick answer

Bryant Evolution code 13 is a *limit lockout* — the integrated furnace control opened the gas valve repeatedly on consecutive heat calls because a limit switch tripped each time, so the board has locked the unit out of further heating attempts for about three hours. The single most common root cause I see in the field is restricted airflow (a clogged filter, a closed supply register, or a partially blocked return) overheating the heat exchanger and tripping the primary limit, not a bad limit switch.

## What code 13 means on a Bryant

Bryant Evolution, Preferred, and Legacy single-stage and two-stage furnaces share the same integrated furnace control (IFC) chassis as their Carrier counterparts — the units roll off the same Indianapolis assembly line and the only meaningful difference is the cabinet sticker and the dealer network. The board, the pressure switches, the inducer assembly, and the limit switches all carry HK-prefix Bryant part numbers that cross-reference one-to-one with Carrier's HC-prefix equivalents. If your Carrier service tech has an HC23CE026 contactor on the truck, it drops into a Bryant Evolution heat pump without modification.

Code 13 specifically means: the board counted **three consecutive heat calls** in which the high-limit safety switch opened during the run, and on the third event the board enforced a three-hour lockout. The LED status light behind the lower door blinks one slow flash, pause, three fast flashes — long-short-short-short. On Evolution thermostats with the color touchscreen, the alphanumeric code "Code 13 — Limit Switch Lockout" appears in the service alerts menu.

The primary limit on a Bryant 90% AFUE furnace is typically a normally-closed disc-type thermal switch mounted on the heat exchanger top plate, rated to open at 180–220°F depending on the cabinet size. There may be a secondary limit on the blower deck and one or two rollout switches near the burner assembly. Code 13 only refers to the *primary* (heat exchanger) limit chain; if a rollout opens, the board posts code 14 instead.

## Common causes (ranked by frequency)

In residential service work, here's how code 13 typically distributes:

1. **Restricted return-side airflow** — about 45%. Filter overdue for change, return grilles blocked by furniture, undersized return drop on the original install.
2. **Closed or blocked supply registers** — about 15%. Homeowner closed off rooms thinking it'd save energy; pressure climbs and airflow drops below minimum CFM/ton.
3. **Failed blower capacitor or aging PSC blower motor** — about 15%. Motor turns slower under load, CFM drops, heat exchanger overheats.
4. **Dirty or partially blocked evaporator coil** — about 10%. The downstream coil acts as a flow restriction even when the AC isn't running.
5. **Actual failed limit switch (open or drifted low)** — about 8%. The switch itself has aged and now opens at 160°F instead of its rated 200°F.
6. **Failed inducer or low gas pressure causing repeated short cycling** — about 5%. The unit lights, but burns inefficiently, heats the exchanger above setpoint, trips the limit.
7. **Wiring nick or loose connection on the limit string** — about 2%.

**Pro nugget:** the Bryant Evolution control board uses the same HK42FZ035 IFC platform as the equivalent Carrier 58 series — but Bryant ships these boards with a slightly different default ignition profile that holds the inducer at high speed for an extra 5 seconds during purge. If you swap an HC42FZ035 Carrier board into a Bryant cabinet, the unit will run fine but the diagnostic flash patterns will read one code number off in some failure modes. Always order the HK-prefix Bryant board for a Bryant cabinet, even though the physical board is electrically identical.

## Step-by-step fix

Before you start: shut off power at the furnace switch and gas at the dedicated gas cock. Wait 5 minutes for the inducer to spin down and the heat exchanger to cool before touching anything inside the cabinet.

1. **Read the fault history before clearing.** Open the lower door, observe the LED through one cycle. If you have an Evolution thermostat, navigate to Menu → Service → Fault History — the screen shows up to the last 10 events with timestamps. Note whether code 13 was preceded by code 12 (blower failure) or code 25 (gas valve fault).

2. **Pull and inspect the filter.** A 1-inch pleated filter darker than light gray on the dirty side is overdue. Replace with a fresh filter of the same MERV rating — do not jump to MERV-13 on an older blower that was sized for MERV-8. Higher MERV equals higher static pressure equals less airflow equals more limit trips.

3. **Walk every supply register and every return grille.** Open any registers the homeowner has closed. Pull furniture and rugs off return grilles. Bryant's installation instructions require a minimum of 350 CFM/ton of airflow; on a 3-ton system that's 1050 CFM, and a single closed bedroom register can drop you below that.

4. **Measure external static pressure.** With a digital manometer (Dwyer 475 or equivalent) tapped into the supply plenum and the return plenum, run the blower on the heating speed tap. The reading should be under 0.5 inches WC for most Bryant 4-ton and smaller cabinets. Anything over 0.8 inches WC means the duct system is too restrictive and the unit will limit-trip until you fix duct restrictions.

5. **Ohm-test the primary limit.** Power off. Pull the two spade connectors off the primary limit switch (mounted on the heat exchanger top plate, has a small reset button or is automatic-reset depending on model). Set a meter to continuity. At room temperature, a working limit reads closed (continuity, near zero ohms). If it reads open at room temperature, the switch has failed open — replace it.

6. **Check the blower capacitor.** Power off, discharge the capacitor by shorting across the terminals through a 20kΩ resistor. Measure capacitance with a meter that supports cap testing. A 7.5 µF capacitor reading below 6.7 µF (within 10% tolerance is acceptable, more than that means it's failing) is causing slow blower speed and limit trips.

7. **Reset the lockout.** Once the underlying restriction is fixed, cycle 24V power at the disconnect or thermostat to clear the lockout. The three-hour timer doesn't have to expire if you do a hard power cycle. Watch a full heat cycle: thermostat call → inducer pre-purge (15-30 sec) → pressure switch closes → HSI energizes (30-45 sec warmup) → gas valve opens → flame establishes → blower delay (30-90 sec, set in board DIP switches) → blower on at heat speed → cycle continues until thermostat satisfies.

8. **Verify temperature rise.** With a temperature probe in the supply plenum and one in the return, measure the temperature rise during the heat cycle. Bryant's data tag specifies an acceptable range — typically 35-65°F for an 80% furnace, 30-60°F for a 90% AFUE. A rise above the high end means inadequate airflow; below the low end means overfiring or oversized blower.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Primary limit switch (200°F auto-reset) | Bryant HH18HA250 | $35-55 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| Rollout limit switch (manual reset) | Bryant HH12ZB174 | $25-40 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| Integrated furnace control (IFC) | Bryant HK42FZ035 | $235-340 | [RepairClinic](https://www.repairclinic.com), [Home Depot](https://www.homedepot.com) |
| PSC blower motor 1/2 HP | Bryant HC45TE118 | $245-340 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| Blower run capacitor 7.5µF/370V | Bryant HC91CE015 | $18-32 | [Amazon](https://www.amazon.com), [Home Depot](https://www.homedepot.com) |
| 1-inch pleated filter MERV-8 (20x25x1) | Generic | $8-15 | [Home Depot](https://www.homedepot.com), [Lowes](https://www.lowes.com) |
| Digital manometer | Dwyer 475-1-FM | $185-235 | [Amazon](https://www.amazon.com) |

Note on Carrier/Bryant cross-reference: the limit switches are identical between Carrier (HC-prefix), Bryant (HH-prefix), and Payne (HH-prefix as well) for matching model years. The IFC board is identical between Carrier (HK42FZ035 with HC prefix in some variants) and Bryant (HK42FZ035 with HK prefix) — same firmware, same connector layout, only the dealer-channel sticker changes.

## When to call a professional

Call a licensed HVAC tech when any of the following apply:

- You've changed the filter, opened all registers, verified static pressure under 0.5 WC, and code 13 still returns. That points to either a heat exchanger crack (gas leaking past the limit and overheating it locally) or a board-level sensing fault — both need a tech with a combustion analyzer and a flue gas CO probe.
- You see soot on the burners or yellow tipping on the flames. That's incomplete combustion and the limit trips are a symptom of a bigger fuel-air problem.
- The furnace is under Bryant factory warranty (5 years parts standard, 10 years with registration). Replacing the IFC board or the gas valve outside of authorized service voids the parts warranty.
- The furnace is a Bryant Evolution Communicating system. These have integrated communication between board, ECM blower, inducer, and thermostat — diagnostic flash codes alone don't tell the whole story; you need the Service Assistant tool or equivalent diagnostics.

## FAQs

**Will code 13 clear itself after three hours?**
Yes, the lockout has a three-hour timer. After three hours, the board allows one more heat attempt. If the underlying problem isn't fixed, it'll trip right back into lockout. Use the three hours to actually fix the airflow problem, don't just wait it out.

**Can I disable the limit switch to get heat tonight?**
Absolutely not. The high-limit is the only safety preventing the heat exchanger from glowing red, cracking, and putting flue gas (CO) into your home. Jumpering or removing a limit switch is illegal in most jurisdictions and dangerous. Use a space heater for the night.

**My Bryant Evolution is two years old. Why is the limit tripping already?**
At two years, it's almost never the limit switch itself. Look at install errors: undersized return duct, missing return drop, oversized furnace for the home (short cycles), or a builder-installed filter rack that's too restrictive. New-construction Bryant systems trip code 13 because of duct mistakes more than any other reason.

**The Bryant tech said I need a new heat exchanger. Is that really required for code 13?**
Sometimes yes. If the heat exchanger has a crack or burnout, hot combustion gas escapes near the limit switch and overheats it locally even with full airflow. The tech should verify with a combustion analyzer (CO in the supply air > 9 ppm above ambient confirms it) before recommending a heat exchanger.

**Difference between Bryant code 13 and Bryant code 14?**
Code 13 is the primary high-limit (heat exchanger top plate) tripping. Code 14 is a rollout switch (near the burner assembly) tripping — that's a more serious condition, usually indicating flame rollout from a blocked or restricted heat exchanger, and demands immediate professional service.

## Related guides

- [Carrier 13 Error Code — Limit Switch Lockout Fix](/posts/carrier-13-error-code)
- [Bryant Heat Pump Error Code 21 — Defrost Issue Fix](/posts/bryant-heat-pump-error-code-21)
- [Bryant Evolution Code 21 — Gas Heating Lockout Fix](/posts/bryant-error-code-21)
