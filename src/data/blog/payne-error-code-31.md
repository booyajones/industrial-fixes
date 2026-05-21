---
title: "Payne Error Code 31 — Pressure Switch Did Not Open Fix"
description: "Payne code 31 means the integrated furnace control sees the pressure switch already closed at the start of a heat call, before the inducer has run — the..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: payne-error-code-31
featured: false
draft: false
tags:
  - payne
  - hvac
  - error-codes
  - pressure-switch-did-not-open
---
## Quick answer

Payne code 31 means the integrated furnace control sees the pressure switch already closed at the start of a heat call, before the inducer has run — the switch should sit open at rest and close only when the inducer develops draft. About 50% of these are pressure switches with stuck diaphragms; another 20% are switch hoses kinked or melted against the inducer body. Bench-test the switch with a meter before assuming the worst.

## What code 31 means on a Payne

Payne is Carrier's entry-level brand — same Indianapolis assembly line as Carrier and Bryant, same Carrier-engineered control board, just a stripped-down feature set and a different cabinet badge. The diagnostic codes, the part numbers, and the service procedures are identical between Payne, Bryant, and Carrier for matching model years. A Payne PG9MAA furnace and a Carrier 58CVA furnace use the same HK42FZ-series control board, the same HK06WC-series pressure switch, the same EF32CW-series gas valve.

Where Payne differs from Carrier and Bryant: the dealer channel (Payne goes through HVAC supply houses and selected dealers rather than the Carrier dealer network), the feature set (Payne furnaces are typically single-stage with PSC blowers, while equivalent Carrier units offer two-stage and ECM blowers), and the warranty terms (Payne typically carries 5-year parts standard, with the longer 10-year option only on registered units). The diagnostic LED behind the lower door uses the same flash code system as Carrier: three slow flashes, pause, one fast flash = code 31.

Code 31 fires when the integrated control checks the pressure switch state at the beginning of a heat call and finds it closed. The pressure switch is normally open at rest — vacuum from the running inducer pulls the diaphragm down, closes the contacts, and tells the board "draft is present." A switch that's stuck closed at rest means the board can't trust the next closed reading as proof of draft. Safety mode: refuse to ignite, post code 31, wait 5 minutes, retry.

## Common causes (ranked by frequency)

In Payne field service:

1. **Stuck-closed pressure switch diaphragm** — about 50%. Same Carrier-sourced switch as Bryant; same failure mode where the silicone diaphragm sticks against the contact plate after years of vacuum cycling.
2. **Kinked or melted pressure switch hose** — about 18%. Routing tight against the inducer body, melts under heat.
3. **Water in the switch hose holding residual vacuum** — about 12%. Condensate from a 90% AFUE wicks up the hose and traps a vacuum bubble.
4. **Pressure switch shorted internally** — about 10%. Contacts welded from a power surge or aging.
5. **Wrong replacement switch installed in prior service** — about 5%. Generic switch with a setpoint that doesn't match the unit's draft profile.
6. **Control board sensing circuit failure** — about 3%. The 24V switch-sense input on the IFC has failed.
7. **Wiring or connector issue at the switch** — about 2%. Loose spade or chafed wire.

**Pro nugget:** Payne furnaces ship with the same HK06WC084 pressure switch as Carrier and Bryant 90% AFUE single-switch units — but the **Payne PG8MAA 80% AFUE non-condensing** uses a different switch (HK06WB175, setpoint -0.30 WC instead of -0.40 WC). The two switches look nearly identical and have the same physical form factor, so a tech who grabs the wrong one off the truck installs a -0.40 switch in a -0.30 application. The unit will run, but the switch will be marginal and trip code 31 intermittently in low-draft conditions. Always confirm the stamped setpoint on the original before ordering a replacement.

## Step-by-step fix

Before you start: shut off power at the furnace switch, shut off gas at the gas cock, wait 5 minutes for inducer spin-down.

1. **Confirm the code.** Open the lower door, watch the LED through a power cycle. Three slow + one fast = 31. Photo the wiring diagram on the inside of the door for reference.

2. **Disconnect power for 5 minutes.** Let any residual vacuum bleed out of the switch hose. A mechanically-stuck switch sometimes releases temporarily during cool-down — but it will stick again, so still replace it.

3. **Ohm-test the pressure switch at rest.** Power off, pull the two electrical spade terminals off the switch (note positions). Set a meter to continuity. A working normally-open switch reads open (OL or infinity) with no vacuum on the hose. A stuck-closed switch reads near zero. If it reads closed, replace it.

4. **Inspect the switch hose.** Pull the hose off both the inducer body and the switch port. Look for: visible kinks, melt marks where the hose touched the inducer body, water droplets inside, white scale buildup, brittleness from heat aging. Blow through the hose — should pass air freely. Replace with same-diameter silicone tubing (1/4-inch ID, high-temp red silicone) if any damage.

5. **Check hose routing.** Re-route with at least 1/4-inch clearance from any hot surface. Use a small zip tie if needed to hold the hose away from the inducer body. The factory routing on Payne uses a small plastic clip that often breaks during prior service — replace the clip or substitute a zip tie.

6. **Replace the switch.** Order the exact OEM Payne part by the stamped switch number on the original (HK06WC084 for most 90% AFUE singles, HK06WB175 for 80% AFUE singles). Two screws and two spade terminals. Bench-test the new switch on continuity before installing to confirm it reads open at rest.

7. **Restore power and observe.** Cycle the gas valve back on. Initiate a heat call from the thermostat. Cold start sequence: 24V to board → inducer energizes → 15-30 sec pre-purge → switch should click closed (audible click) → HSI warmup 30-45 sec → gas valve clicks open → flame establishes → blower delay 30-90 sec → blower on. If code 31 returns immediately at startup, the new switch is defective (rare but happens) or the board's sensing circuit has failed.

8. **Test response with a manometer.** Tee a digital manometer into the switch hose. During inducer startup, watch the negative pressure climb. You should see vacuum cross the switch setpoint (e.g., 0.40 inches WC) within 5-10 seconds, and the switch should click closed at that pressure. If draft never reaches setpoint, the inducer is failing or the vent is partially blocked.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Pressure switch (90% AFUE, single, 0.40 WC) | Payne HK06WC084 | $45-70 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| Pressure switch (80% AFUE, single, 0.30 WC) | Payne HK06WB175 | $40-65 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| Pressure switch (90% AFUE, dual) | Payne HK06NB124 | $65-95 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| Silicone hose (1/4 inch, high-temp) | Generic | $5-10/ft | [Amazon](https://www.amazon.com), [Home Depot](https://www.homedepot.com) |
| Integrated furnace control | Payne HK42FZ020 | $235-340 | [RepairClinic](https://www.repairclinic.com), [Lowes](https://www.lowes.com) |
| Inducer assembly | Payne 320725-756 | $290-410 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| 24V transformer (40VA) | Payne HT01BD110 | $55-85 | [Amazon](https://www.amazon.com), [Home Depot](https://www.homedepot.com) |

Carrier/Bryant/Payne cross-reference: every Payne part above interchanges with Carrier and Bryant equivalents one-to-one. Carrier sells these with HC-prefix stickers, Bryant with HK-prefix, Payne with HK-prefix — same physical parts. If your supply house has the Carrier number in stock and the Payne number on backorder, the Carrier part drops in without modification.

## When to call a professional

Call a licensed HVAC tech when:

- You've replaced the switch (bench-tested as open), inspected the hose, and code 31 returns immediately on the next cycle. That points to a control board sensing fault — IFC board replacement requires accurate wiring transfer and proper grounding.
- You smell flue gas (slightly acrid, sweet) anywhere near the furnace. Code 31 can coincide with vent leaks; needs CO testing.
- The pressure switch hose has water and you can't trace where it's coming from. On a 90% AFUE unit, water in the hose suggests condensate path issues — needs combustion analysis.
- The unit is under Payne warranty. Replacing the IFC or the gas valve outside authorized service voids the parts warranty.

## FAQs

**Why is the Payne switch the same part as the Carrier?**
Same parent company (Carrier Corp.), same factory, same engineering. Payne is the value brand, Bryant is mid-tier, Carrier is premium — but the underlying components are shared across the three brands for cost reasons.

**Can I jumper the pressure switch to get heat tonight?**
No. The pressure switch is the only safety preventing the burners from lighting into a blocked vent or a failed inducer. Jumpering it can put CO into your home. Use a space heater overnight.

**My switch tests open on the bench but the unit still throws 31. What now?**
That indicates the board is reading the switch state incorrectly. Power down for 10 minutes (full discharge of the IFC), then re-test. If code 31 persists, the board's 24V sensing input is bad — replace the IFC.

**The hose has white scale inside. Is that scale a problem?**
Yes. Mineral scale from condensate exposure can partially block the hose orifice, holding vacuum after the inducer stops and tripping code 31 on the next cycle. Replace the hose with fresh silicone tubing and inspect the condensate trap upstream.

**Difference between Payne code 31 and code 32?**
Code 31 = pressure switch stuck closed at rest. Code 32 = pressure switch didn't close after inducer started (the inverse — typically blocked vent, dead inducer, or failed switch open). Different diagnostic paths.

## Related guides

- [Carrier 31 Error Code — Pressure Switch Fix](/posts/carrier-31-error-code)
- [Bryant Error Code 13 — Limit Lockout Fix](/posts/bryant-error-code-13)
- [Heil 3-Flash Error Code — Pressure Switch Fix](/posts/heil-flash-code-3)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Carrier vs Trane furnaces compared](/posts/carrier-vs-trane-furnaces/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Goodman vs Bryant furnaces compared](/posts/goodman-vs-bryant-furnaces/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Mitsubishi vs Daikin mini splits](/posts/mitsubishi-vs-daikin-mini-splits/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Best HVAC manometer (2026)](/posts/best-manometer-for-hvac/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Best refrigerant gauge set (2026)](/posts/best-refrigerant-gauge-set/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Best refrigerant leak detector](/posts/best-refrigerant-leak-detector/)

